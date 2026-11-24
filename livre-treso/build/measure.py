import json,subprocess
pm=json.load(open('build/pagemap.json'))
n=int(subprocess.run(['pdfinfo','livrables/LA_TRESO_SOUS_CONTROLE.pdf'],capture_output=True,text=True).stdout.split('Pages:')[1].split()[0])
starts=[p for k,l,p in pm['toc']]+[n+1]
for (k,l,p),nxt in zip(pm['toc'],starts[1:]):
    last=nxt-1
    t=subprocess.run(['pdftotext','-layout','-f',str(last),'-l',str(last),'livrables/LA_TRESO_SOUS_CONTROLE.pdf','-'],capture_output=True,text=True).stdout
    print(f"{l[:40]:42s} p{p}-{last} ({last-p+1}p) last={len([x for x in t.split(chr(10)) if x.strip()])}")
