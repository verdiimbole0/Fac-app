import sys,glob
from PIL import Image, ImageDraw
files=sorted(glob.glob(sys.argv[1]))
cols=int(sys.argv[3]); per=int(sys.argv[4])
for k in range(0,len(files),per):
    ims=[Image.open(f) for f in files[k:k+per]]
    w,h=ims[0].size; rows=(len(ims)+cols-1)//cols
    sheet=Image.new('RGB',(cols*w+(cols+1)*6,rows*h+(rows+1)*6),'#888')
    for i,im in enumerate(ims):
        sheet.paste(im,(6+(i%cols)*(w+6),6+(i//cols)*(h+6)))
    sheet.save(f"{sys.argv[2]}_{k//per+1:02d}.png")
