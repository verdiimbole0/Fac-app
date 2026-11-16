# -*- coding: utf-8 -*-
"""Photographies Wikimedia Commons sous licence libre.

1) `python3 photos.py emplacements` : crée des emplacements réservés (images JPEG
   clairement marquées « photographie à intégrer ») aux noms de fichiers attendus
   par le manuscrit. C'est l'état livré : le téléchargement automatisé depuis
   l'environnement de production a été refusé par Wikimedia (politique anti-robots).
2) `python3 photos.py telecharger "VotreOutil/1.0 (contact: votre.adresse@exemple.org)"` :
   à lancer depuis votre poste, avec un User-Agent comportant VOTRE contact
   (exigence de la politique Wikimedia). Remplace les emplacements par les vraies
   photographies (vignettes 1280 px). Une pause est respectée entre les fichiers.
Les crédits (auteur, licence, page source) sont dans 02_ILLUSTRATIONS/PHOTOGRAPHIES/CREDITS_PHOTOS.json.
"""
import json, sys, time, hashlib, urllib.parse, urllib.request, io, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

D = Path(__file__).resolve().parents[1] / "02_ILLUSTRATIONS" / "PHOTOGRAPHIES"
CRED = json.loads((D / "CREDITS_PHOTOS.json").read_text(encoding="utf-8"))

def police(t, gras=False):
    for f in (f"/usr/share/fonts/truetype/inter/Inter-{'SemiBold' if gras else 'Regular'}.ttf",
              f"/usr/share/fonts/truetype/dejavu/DejaVuSans{'-Bold' if gras else ''}.ttf"):
        try: return ImageFont.truetype(f, t)
        except OSError: continue
    return ImageFont.load_default()

def emplacements():
    for c in CRED:
        im = Image.new("RGB", (1600, 1000), "#EEF1F5"); d = ImageDraw.Draw(im)
        d.rectangle([20, 20, 1580, 980], outline="#0B2545", width=6)
        for k in range(0, 1600, 40): d.line([(k, 980), (k + 300, 680)], fill="#E1E6ED", width=2)
        d.text((800, 150), "PHOTOGRAPHIE À INTÉGRER", fill="#B23A48", font=police(64, True), anchor="mm")
        d.text((800, 230), "(emplacement réservé — l'image n'est pas encore intégrée)", fill="#B23A48", font=police(34), anchor="mm")
        y = 340
        for lab, val in [("Fichier Commons", c["titre_commons"][5:]), ("Auteur", c["auteur"]), ("Licence", c["licence"]), ("Source", c["page"]), ("Sujet", c["description"])]:
            for i, l in enumerate(textwrap.wrap(f"{lab} : {val}", 70)[:3]):
                d.text((90, y), l, fill="#0B2545" if i == 0 else "#222831", font=police(34, i == 0 and lab != "Source")); y += 48
            y += 14
        d.text((800, 930), "Commande : python3 08_OUTILS/photos.py telecharger \"<User-Agent avec votre contact>\"", fill="#5B6B7F", font=police(28), anchor="mm")
        im.save(D / c["fichier"], quality=88)
    print(len(CRED), "emplacements créés")

def telecharger(ua):
    ok = 0
    for c in CRED:
        n = c["titre_commons"][5:].replace(" ", "_"); h = hashlib.md5(n.encode()).hexdigest(); q = urllib.parse.quote(n)
        url = f"https://upload.wikimedia.org/wikipedia/commons/thumb/{h[0]}/{h[:2]}/{q}/1280px-{q}"
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": ua}), timeout=120)
            im = Image.open(io.BytesIO(r.read())).convert("RGB"); im.save(D / c["fichier"], quality=88)
            c["statut"] = "intégrée"; ok += 1; print("OK", c["fichier"])
        except Exception as e:
            print("ÉCHEC", c["fichier"], e)
        time.sleep(5)
    (D / "CREDITS_PHOTOS.json").write_text(json.dumps(CRED, ensure_ascii=False, indent=1), encoding="utf-8")
    print(ok, "/", len(CRED), "photographies intégrées. Mettez à jour les légendes (« Photographie à intégrer » → « Photographie »).")

if __name__ == "__main__":
    if sys.argv[1:2] == ["emplacements"]: emplacements()
    elif sys.argv[1:2] == ["telecharger"] and len(sys.argv) > 2: telecharger(sys.argv[2])
    else: print(__doc__)
