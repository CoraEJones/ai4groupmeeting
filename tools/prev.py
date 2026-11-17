import os, sys
from pptx import Presentation
a,b,out=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
W=os.environ.get('W','/workspace/slides/full-meeting-rT7meI')
p=Presentation(W+'/'+sys.argv[4] if len(sys.argv)>4 else W+'/preview-g6.pptx')
ids=p.slides._sldIdLst
for i,el in enumerate(list(ids)):
    if not (a-1<=i<=b-1): ids.remove(el)
p.save(out)
