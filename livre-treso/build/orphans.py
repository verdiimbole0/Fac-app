import subprocess,re
PDF='livrables/LA_TRESO_SOUS_CONTROLE.pdf'
n=int(subprocess.run(['pdfinfo',PDF],capture_output=True,text=True).stdout.split('Pages:')[1].split()[0])
labels=("À RETENIR","EXEMPLE PRATIQUE","CAS FIL ROUGE","CONSEIL PROFESSIONNEL","ATTENTION","ERREUR FRÉQUENTE","À VOUS DE JOUER","VOTRE PROCHAINE ACTION","OBJECTIFS","FORMULE","PROMPT PRÊT","Tableau ","Question ")
for i in range(1,n+1):
    t=subprocess.run(['pdftotext','-layout','-f',str(i),'-l',str(i),PDF,'-'],capture_output=True,text=True).stdout
    L=[x.strip() for x in t.split('\n') if x.strip()]
    if len(L)<3: print(i,"PAGE QUASI VIDE"); continue
    body=L[:-1]  # retirer le numéro
    last=body[-1]
    if last.startswith(labels) or re.match(r'^\d+\.\d+ ',last) or last.startswith(('Q1','Corrigé','QCM')):
        print(i, "FIN DE PAGE :", last[:70])
