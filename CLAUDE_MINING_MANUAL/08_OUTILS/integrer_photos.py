# -*- coding: utf-8 -*-
"""Intègre les photographies fournies (dossier source en argument) à leurs emplacements,
réécrit les légendes avec titre, auteur, source, licence et liens, et met à jour les crédits.
Usage : python3 integrer_photos.py DOSSIER_PHOTOS"""
import json, re, sys, glob
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "02_ILLUSTRATIONS" / "PHOTOGRAPHIES"
SRC = Path(sys.argv[1])

LICENCES = {
    "CC BY 3.0": "https://creativecommons.org/licenses/by/3.0/deed.fr",
    "CC BY 4.0": "https://creativecommons.org/licenses/by/4.0/deed.fr",
    "CC BY-SA 3.0": "https://creativecommons.org/licenses/by-sa/3.0/deed.fr",
    "CC BY-SA 4.0": "https://creativecommons.org/licenses/by-sa/4.0/deed.fr",
}
# Nom d'auteur affiché (nettoyé des mentions techniques de Commons)
AUTEURS = {"photo_pelle_camion": "Sandrerro", "photo_niosh_camion_recul": "NIOSH (National Institute for Occupational Safety and Health)",
           "photo_electrolyse_luilu": "Gécamines", "photo_parc_residus_mt_isa": "L. Plass (State Library of Queensland)",
           "photo_revegetation_csiro": "Nick Pitsas, CSIRO"}
# Largeur d'affichage selon l'orientation, pour préserver la lisibilité
def largeur(w, h):
    r = w / h
    return "85%" if r >= 1.6 else ("78%" if r >= 1.3 else "62%")

cred = json.loads((DEST / "CREDITS_PHOTOS.json").read_text(encoding="utf-8"))
par_titre = {c["titre_commons"][5:].replace(" ", "_"): c for c in cred}
dims = {}
for f in sorted(SRC.iterdir()):
    c = par_titre.get(f.stem + f.suffix)
    if c is None:
        print("Ignoré (non référencé) :", f.name); continue
    im = Image.open(f); im = im.convert("RGB"); im.thumbnail((1800, 1800))
    out = DEST / c["fichier"]; im.save(out, "JPEG", quality=90, optimize=True)
    dims[c["fichier"]] = im.size
    c["statut"] = "intégrée (fichier fourni par l'éditeur, redimensionné à 1 800 px max)"
    c["url_licence"] = LICENCES.get(c["licence"], "")
    c["auteur_affiche"] = AUTEURS.get(c["fichier"][:-4], c["auteur"])
    print("Intégrée :", c["fichier"], im.size, c["licence"])
(DEST / "CREDITS_PHOTOS.json").write_text(json.dumps(cred, ensure_ascii=False, indent=1), encoding="utf-8")
cmap = {c["fichier"]: c for c in cred}

motif = re.compile(r"!\[(Figure [\d.]+) — (.+?) PHOTOGRAPHIE À INTÉGRER.*?\]\((02_ILLUSTRATIONS/PHOTOGRAPHIES/(photo_[a-z0-9_]+\.jpg))\)\{width=\d+%\}")
n = 0
for md in glob.glob(str(ROOT / "01_MANUSCRIT" / "**" / "*.md"), recursive=True):
    t = Path(md).read_text(encoding="utf-8")
    def rep(m):
        global n
        fig, titre, chemin, fichier = m.group(1), m.group(2).strip(), m.group(3), m.group(4)
        c = cmap[fichier]
        if fichier not in dims: return m.group(0)
        titre_c = c["titre_commons"][5:].rsplit(".", 1)[0]
        lic = c["licence"]
        lic_txt = f"[{lic}]({c['url_licence']})" if c.get("url_licence") else ("domaine public" if "Public" in lic else lic)
        modif = " ; image redimensionnée pour l'édition" if lic.startswith("CC") else ""
        leg = (f"{fig} — {titre} Titre original : « {titre_c} ». Auteur : {c['auteur_affiche']}. "
               f"Source : Wikimedia Commons, [{c['page']}]({c['page']}) (consulté le 16/11/2026). "
               f"Licence : {lic_txt}{modif}. Photographie d'illustration, sans lien avec l'entreprise fictive MCC.")
        n += 1
        return f"![{leg}]({chemin}){{width={largeur(*dims[fichier])}}}"
    t2 = motif.sub(rep, t)
    if t2 != t: Path(md).write_text(t2, encoding="utf-8")
print(n, "légendes réécrites")
reste = [md for md in glob.glob(str(ROOT / "01_MANUSCRIT" / "**" / "*.md"), recursive=True) if "À INTÉGRER" in Path(md).read_text(encoding="utf-8")]
print("Mentions « À INTÉGRER » restantes :", reste or "aucune")
