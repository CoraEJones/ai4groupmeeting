# minimal OMML builder + matplotlib fallback image
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
CM='<a:latin typeface="Cambria Math" panose="02040503050406030204" pitchFamily="18" charset="0"/><a:ea typeface="Cambria Math" panose="02040503050406030204" pitchFamily="18" charset="0"/><a:cs typeface="Cambria Math" panose="02040503050406030204" pitchFamily="18" charset="0"/>'
def _rpr(sz,col,it,b): return f'<a:rPr lang="en-US" sz="{sz*100}" b="{1 if b else 0}" i="{1 if it else 0}"><a:solidFill><a:srgbClr val="{col}"/></a:solidFill>{CM}</a:rPr>'
TEXMAP={'δ':r'\delta ','σ':r'\sigma ','θ':r'\theta ','×':r'\times ','≈':r'\approx ','⇒':r'\Rightarrow ','−':'-','°':r'^{\circ}','∞':r'\infty ','·':r'\cdot ','%':r'\%','–':'-','@':'@',' ':r'\ ','|':'|'}
def _tex(s,it):
    out=''
    for ch in s:
        if ch in TEXMAP: out+=TEXMAP[ch]
        elif ch.isalpha() and not it: out+=r'\mathrm{'+ch+'}'
        else: out+=ch
    return out
def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
class N:
    pass
def R(t,it=None,b=False,col=None):
    n=N(); n.k='r'; n.t=t; n.it=(len(t)==1 and t.isalpha()) if it is None else it; n.b=b; n.col=col; return n
def F(a,b): n=N(); n.k='f'; n.a=a; n.b_=b; return n
def SUB(a,s): n=N(); n.k='sub'; n.a=a; n.s=s; return n
def SUP(a,s): n=N(); n.k='sup'; n.a=a; n.s=s; return n
def DL(a,beg='|',end='|'): n=N(); n.k='d'; n.a=a; n.beg=beg; n.end=end; return n
def RAD(a): n=N(); n.k='rad'; n.a=a; return n
def L(x): return x if isinstance(x,list) else [x]
def om(nodes,sz,col):
    o=''
    for n in L(nodes):
        c=n.col if getattr(n,'col',None) else col
        if n.k=='r':
            sty='' if n.it and not n.b else f'<m:rPr><m:sty m:val="{"bi" if (n.it and n.b) else ("b" if n.b else "p")}"/></m:rPr>'
            o+=f'<m:r>{sty}{_rpr(sz,c,n.it,n.b)}<m:t xml:space="preserve">{esc(n.t)}</m:t></m:r>'
        elif n.k=='f': o+=f'<m:f><m:fPr><m:ctrlPr>{_rpr(sz,col,True,False)}</m:ctrlPr></m:fPr><m:num>{om(n.a,sz,col)}</m:num><m:den>{om(n.b_,sz,col)}</m:den></m:f>'
        elif n.k=='sub': o+=f'<m:sSub><m:sSubPr><m:ctrlPr>{_rpr(sz,col,True,False)}</m:ctrlPr></m:sSubPr><m:e>{om(n.a,sz,col)}</m:e><m:sub>{om(n.s,sz,col)}</m:sub></m:sSub>'
        elif n.k=='sup': o+=f'<m:sSup><m:sSupPr><m:ctrlPr>{_rpr(sz,col,True,False)}</m:ctrlPr></m:sSupPr><m:e>{om(n.a,sz,col)}</m:e><m:sup>{om(n.s,sz,col)}</m:sup></m:sSup>'
        elif n.k=='rad': o+=f'<m:rad><m:radPr><m:degHide m:val="1"/><m:ctrlPr>{_rpr(sz,col,True,False)}</m:ctrlPr></m:radPr><m:deg/><m:e>{om(n.a,sz,col)}</m:e></m:rad>'
        elif n.k=='d': o+=f'<m:d><m:dPr><m:begChr m:val="{n.beg}"/><m:endChr m:val="{n.end}"/><m:ctrlPr>{_rpr(sz,col,True,False)}</m:ctrlPr></m:dPr><m:e>{om(n.a,sz,col)}</m:e></m:d>'
    return o
def tex(nodes):
    o=''
    for n in L(nodes):
        if n.k=='r':
            s=_tex(n.t,n.it); o+=(r'\mathbf{'+s+'}') if n.b else s
        elif n.k=='f': o+=r'\frac{'+tex(n.a)+'}{'+tex(n.b_)+'}'
        elif n.k=='sub': o+='{'+tex(n.a)+'}_{'+tex(n.s)+'}'
        elif n.k=='sup': o+='{'+tex(n.a)+'}^{'+tex(n.s)+'}'
        elif n.k=='rad': o+=r'\sqrt{'+tex(n.a)+'}'
        elif n.k=='d': o+=r'\left'+n.beg+tex(n.a)+r'\right'+n.end
    return o
def fallback_png(lines,sz,col,path):
    fig=plt.figure(figsize=(0.01,0.01),dpi=300)
    txt='\n'.join('$'+tex(l)+'$' for l in lines)
    fig.text(0,0,txt,fontsize=sz,color='#'+col,math_fontfamily='cm',linespacing=1.4,ha='left',va='bottom')
    fig.savefig(path,dpi=300,transparent=True,bbox_inches='tight',pad_inches=0.02); plt.close(fig)
    w,h=Image.open(path).size; return w/300,h/300
def eq_shape(NSDECL,id,name,x,y,w,h,lines,sz,col,rid,img_wh,E,algn='ctr',anchor='ctr'):
    jc={'ctr':'center','l':'left','r':'right'}[algn]
    paras=''.join(f'<a:p><a:pPr algn="{algn}"><a:buNone/></a:pPr><a14:m><m:oMathPara><m:oMathParaPr><m:jc m:val="{jc}"/></m:oMathParaPr><m:oMath>{om(l,sz,col)}</m:oMath></m:oMathPara></a14:m><a:endParaRPr lang="en-US" sz="{sz*100}" dirty="0"/></a:p>' for l in lines)
    iw,ih=img_wh; s=min(w/iw,h/ih,1.0); fw,fh=iw*s,ih*s
    fx={'ctr':x+(w-fw)/2,'l':x,'r':x+w-fw}[algn]; fy={'ctr':y+(h-fh)/2,'t':y,'b':y+h-fh}[anchor]
    return f'''<mc:AlternateContent {NSDECL} xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"><mc:Choice xmlns:a14="http://schemas.microsoft.com/office/drawing/2010/main" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" Requires="a14"><p:sp><p:nvSpPr><p:cNvPr id="{id}" name="{name}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="{E(x)}" y="{E(y)}"/><a:ext cx="{E(w)}" cy="{E(h)}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr><p:txBody><a:bodyPr wrap="square" lIns="0" tIns="0" rIns="0" bIns="0" anchor="{anchor}" rtlCol="0"><a:noAutofit/></a:bodyPr><a:lstStyle/>{paras}</p:txBody></p:sp></mc:Choice><mc:Fallback><p:sp><p:nvSpPr><p:cNvPr id="{id+5000}" name="{name}"/><p:cNvSpPr txBox="1"><a:spLocks noRot="1" noChangeAspect="1" noMove="1" noResize="1" noEditPoints="1" noAdjustHandles="1" noChangeArrowheads="1" noChangeShapeType="1" noTextEdit="1"/></p:cNvSpPr><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="{E(fx)}" y="{E(fy)}"/><a:ext cx="{E(fw)}" cy="{E(fh)}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></a:blipFill><a:ln><a:noFill/></a:ln></p:spPr><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="en-US"><a:noFill/></a:rPr><a:t> </a:t></a:r></a:p></p:txBody></p:sp></mc:Fallback></mc:AlternateContent>'''

# ---- mixed text + inline OMML paragraph shape
def _textesc(s):
    return s.replace('\\','\\\\').replace('$',r'\$').replace('%',r'\%').replace('_',r'\_').replace('^',r'\^').replace('#',r'\#').replace('&',r'\&')
def mixed_png(paras,sz,path):
    import matplotlib as mpl
    lines=[]
    for parts in paras:
        s=''
        for p in parts:
            if p[0]=='t': s+=_textesc(p[1])
            else: s+='$'+tex(p[1])+'$'
        lines.append(s)
    fig=plt.figure(figsize=(0.01,0.01),dpi=300)
    fig.text(0,0,'\n'.join(lines),fontsize=sz,color='black',family='Carlito',math_fontfamily='cm',linespacing=1.3,ha='left',va='bottom')
    fig.savefig(path,dpi=300,transparent=True,bbox_inches='tight',pad_inches=0.02); plt.close(fig)
    w,h=Image.open(path).size; return w/300,h/300
def mixed_shape(NSDECL,id,name,x,y,w,h,paras,sz,rid,img_wh,E,algn='l',anchor='ctr',blue='316886'):
    def run(t,emph):
        col=blue if emph else '000000'
        return f'<a:r><a:rPr lang="en-US" sz="{sz*100}" b="{1 if emph else 0}" dirty="0"><a:solidFill><a:srgbClr val="{col}"/></a:solidFill><a:latin typeface="Calibri"/><a:ea typeface="Calibri"/><a:cs typeface="Calibri"/></a:rPr><a:t>{esc(t)}</a:t></a:r>'
    ps=''
    for parts in paras:
        body=''
        for p in parts:
            if p[0]=='t': body+=run(p[1],p[2] if len(p)>2 else False)
            else: body+=f'<a14:m><m:oMath>{om(p[1],sz,"000000")}</m:oMath></a14:m>'
        ps+=f'<a:p><a:pPr algn="{algn}"><a:buNone/></a:pPr>{body}<a:endParaRPr lang="en-US" sz="{sz*100}" dirty="0"/></a:p>'
    iw,ih=img_wh; s=min(w/iw,h/ih,1.0); fw,fh=iw*s,ih*s
    fx={'ctr':x+(w-fw)/2,'l':x,'r':x+w-fw}[algn]; fy={'ctr':y+(h-fh)/2,'t':y,'b':y+h-fh}[anchor]
    return f'''<mc:AlternateContent {NSDECL} xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"><mc:Choice xmlns:a14="http://schemas.microsoft.com/office/drawing/2010/main" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" Requires="a14"><p:sp><p:nvSpPr><p:cNvPr id="{id}" name="{name}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="{E(x)}" y="{E(y)}"/><a:ext cx="{E(w)}" cy="{E(h)}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr><p:txBody><a:bodyPr wrap="square" lIns="0" tIns="0" rIns="0" bIns="0" anchor="{anchor}" rtlCol="0"><a:noAutofit/></a:bodyPr><a:lstStyle/>{ps}</p:txBody></p:sp></mc:Choice><mc:Fallback><p:sp><p:nvSpPr><p:cNvPr id="{id+5000}" name="{name}"/><p:cNvSpPr txBox="1"><a:spLocks noRot="1" noChangeAspect="1" noMove="1" noResize="1" noEditPoints="1" noAdjustHandles="1" noChangeArrowheads="1" noChangeShapeType="1" noTextEdit="1"/></p:cNvSpPr><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="{E(fx)}" y="{E(fy)}"/><a:ext cx="{E(fw)}" cy="{E(fh)}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></a:blipFill><a:ln><a:noFill/></a:ln></p:spPr><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="en-US"><a:noFill/></a:rPr><a:t> </a:t></a:r></a:p></p:txBody></p:sp></mc:Fallback></mc:AlternateContent>'''
