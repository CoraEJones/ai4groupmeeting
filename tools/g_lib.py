import copy, os, re, shutil
from lxml import etree
from PIL import Image
W=os.environ.get('W','/workspace/slides/full-meeting-rT7meI')
U=W+'/unpacked/ppt'
NS={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
P='{%s}'%NS['p']; A='{%s}'%NS['a']
E=lambda inch:int(round(inch*914400))
BLUE='316886'


def crop_to(src,dst,ratio,maxw=1400):
    im=Image.open(src).convert('RGB'); w,h=im.size
    if w/h>ratio: nw=int(h*ratio); im=im.crop(((w-nw)//2,0,(w-nw)//2+nw,h))
    else: nh=int(w/ratio); im=im.crop((0,(h-nh)//2,w,(h-nh)//2+nh))
    if im.width>maxw: im=im.resize((maxw,int(maxw*im.height/im.width)),Image.LANCZOS)
    im.save(dst)

def add_rel(slide, rid, target):
    f=f'{U}/slides/_rels/{slide}.rels'; t=open(f).read()
    if f'Id="{rid}"' not in t:
        t=t.replace('</Relationships>',f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/{target}"/></Relationships>')
        open(f,'w').write(t)

def rpr(bold=False,color='000000',sz=20):
    return f'<a:rPr lang="en-US" sz="{sz*100}" b="{1 if bold else 0}" dirty="0"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill><a:latin typeface="Calibri"/><a:ea typeface="Calibri"/><a:cs typeface="Calibri"/></a:rPr>'
def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def runs(parts,sz=20,base='000000'):
    # parts: list of (text, emph) ; emph -> bold blue
    return ''.join(f'<a:r>{rpr(e,BLUE if e else base,sz)}<a:t>{esc(t)}</a:t></a:r>' for t,e in parts)
def para(parts,sz=20,algn='ctr',base='000000',ln=None):
    lnx=f'<a:lnSpc><a:spcPct val="{ln}"/></a:lnSpc>' if ln else ''
    return f'<a:p><a:pPr algn="{algn}">{lnx}<a:buNone/></a:pPr>{runs(parts,sz,base)}<a:endParaRPr lang="en-US" sz="{sz*100}" dirty="0"><a:latin typeface="Calibri"/></a:endParaRPr></a:p>'
NSDECL='xmlns:a="%s" xmlns:p="%s" xmlns:r="%s"'%(NS['a'],NS['p'],NS['r'])
def textbox(id,name,x,y,w,h,paras,anchor='ctr'):
    return etree.fromstring(f'<p:sp {NSDECL}><p:nvSpPr><p:cNvPr id="{id}" name="{name}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="{E(x)}" y="{E(y)}"/><a:ext cx="{E(w)}" cy="{E(h)}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr><p:txBody><a:bodyPr wrap="square" lIns="0" tIns="0" rIns="0" bIns="0" anchor="{anchor}" rtlCol="0"><a:noAutofit/></a:bodyPr><a:lstStyle/>{"".join(paras)}</p:txBody></p:sp>')
def pic(id,name,rid,x,y,w,h):
    return etree.fromstring(f'<p:pic {NSDECL}><p:nvPicPr><p:cNvPr id="{id}" name="{name}"/><p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr/></p:nvPicPr><p:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill><p:spPr><a:xfrm><a:off x="{E(x)}" y="{E(y)}"/><a:ext cx="{E(w)}" cy="{E(h)}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>')
def set_text(sp,paras):
    tb=sp.find(P+'txBody')
    for p in tb.findall(A+'p'): tb.remove(p)
    for x in paras: tb.append(etree.fromstring(x.replace('<a:p>',f'<a:p {NSDECL}>',1)))
def setxf(sp,x,y,w,h):
    xf=sp.find('.//'+A+'xfrm'); xf.find(A+'off').set('x',str(E(x))); xf.find(A+'off').set('y',str(E(y)))
    xf.find(A+'ext').set('cx',str(E(w))); xf.find(A+'ext').set('cy',str(E(h)))

def load(s):
    t=etree.parse(f'{U}/slides/{s}'); tree=t.getroot().find('.//'+P+'spTree'); return t,tree
def byname(tree):
    d={}
    for el in tree:
        c=el.find('.//'+P+'cNvPr')
        if c is not None: d.setdefault(c.get('name'),[]).append(el)
    return d
def drop(tree,names):
    for el in list(tree):
        c=el.find('.//'+P+'cNvPr')
        if c is not None and c.get('name') in names: tree.remove(el)
def save(t,s): t.write(f'{U}/slides/{s}',xml_declaration=True,encoding='UTF-8',standalone=True)

def notes(slide, text):
    rel=open(f'{U}/slides/_rels/{slide}.rels').read()
    n=re.search(r'notesSlides/(notesSlide\d+\.xml)',rel).group(1)
    t=etree.parse(f'{U}/notesSlides/{n}')
    for sp in t.getroot().iter(P+'sp'):
        ph=sp.find('.//'+P+'ph')
        if ph is not None and ph.get('type')=='body':
            tb=sp.find(P+'txBody')
            for p in tb.findall(A+'p'): tb.remove(p)
            for line in text.strip().split('\n'):
                tb.append(etree.fromstring(f'<a:p {NSDECL}><a:r><a:rPr lang="zh-CN" altLang="en-US" sz="1800" dirty="0"/><a:t>{esc(line)}</a:t></a:r></a:p>'))
    t.write(f'{U}/notesSlides/{n}',xml_declaration=True,encoding='UTF-8',standalone=True)


def cell(txt,bold=False,color='000000',fill=None,algn='ctr'):
    f=f'<a:solidFill><a:srgbClr val="{fill}"/></a:solidFill>' if fill else '<a:noFill/>'
    ln=''.join(f'<a:{s}><a:noFill/></a:{s}>' for s in ('lnL','lnR','lnT','lnB'))
    return f'<a:tc><a:txBody><a:bodyPr/><a:lstStyle/><a:p><a:pPr algn="{algn}"><a:buNone/></a:pPr><a:r>{rpr(bold,color,18)}<a:t>{esc(txt)}</a:t></a:r></a:p></a:txBody><a:tcPr marL="91440" marR="91440" marT="45720" marB="45720" anchor="ctr">{ln}{f}</a:tcPr></a:tc>'
def prune_rels(S):
    f=f'{U}/slides/_rels/{S}.rels'; t=open(f).read(); x=open(f'{U}/slides/{S}').read()
    for m in re.findall(r'<Relationship [^>]*/>',t):
        i=re.search(r'Id="([^"]+)"',m).group(1)
        if ('/image"' in m or '/chart"' in m) and f'"{i}"' not in x: t=t.replace(m,'')
    open(f,'w').write(t)
