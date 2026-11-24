#!/bin/bash
# usage: sheet.sh first last out
rm -f /tmp/claude-0/pg-*
pdftoppm -r 55 -png -f $1 -l $2 /home/user/Fac-app/livre-treso/livrables/LA_TRESO_SOUS_CONTROLE.pdf /tmp/claude-0/pg
python3 -c "
from PIL import Image; import glob
fs=sorted(glob.glob('/tmp/claude-0/pg-*.png')); ims=[Image.open(f) for f in fs]
w,h=ims[0].size; cols=8; rows=(len(ims)+cols-1)//cols
c=Image.new('RGB',(w*cols,h*rows),'grey')
for i,im in enumerate(ims): c.paste(im,((i%cols)*w,(i//cols)*h))
c.save('$3')"
