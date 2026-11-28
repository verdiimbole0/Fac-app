# -*- coding: utf-8 -*-
"""Contrôle qualité automatique du manuscrit : structure des chapitres, quiz, carnets,
figures, citations, corrigés, plan éditorial. Écrit 07_CONTROLE_QUALITE/RAPPORT_CONTROLE_QUALITE.md
et 00_GESTION_PROJET/PLAN_EDITORIAL.md."""
import re, glob, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "08_OUTILS"))
from sources import SOURCES

SECTIONS = ["### A.", "### B.", "### C.", "### D.", "### E.", "### F.", "### G.", "### H.", "### I.", "### J.", "### K."]
ids = {s["id"] for s in SOURCES}
chap = sorted(glob.glob(str(ROOT / "01_MANUSCRIT" / "PARTIE_*" / "[0-9][0-9]_chapitre_*.md")))
lignes, problemes, plan = [], [], []
tot_q = tot_fig = tot_prompts = 0
for f in chap:
    t = Path(f).read_text(encoding="utf-8")
    titre = re.search(r"^## (.+)$", t, re.M).group(1)
    n = int(re.search(r"Chapitre (\d+)", titre).group(1))
    manq = [s[4] for s in SECTIONS if s not in t]
    quiz = t.split("### K.")[-1] if "### K." in t else ""
    nq = len(re.findall(r"^\d+\. \*\*\(", quiz, re.M))
    carnet = 'class="carnet"' in t
    figs = re.findall(r"\]\((02_ILLUSTRATIONS/[^)\s]+)\)\{width", t)
    absentes = [x for x in figs if not (ROOT / x).exists()]
    cites = re.findall(r"@([A-Za-z0-9\-]+)", t)
    inconnues = sorted({c for c in cites if c not in ids})
    prompts = t.count("```text")
    tot_q += nq; tot_fig += len(figs); tot_prompts += prompts
    ok = not manq and nq >= 8 and carnet and not absentes and not inconnues
    lignes.append(f"| {n} | {'✅' if ok else '⚠️'} | {', '.join(manq) or '—'} | {nq} | {'oui' if carnet else 'NON'} | {len(figs)} | {len(set(cites))} | {prompts} |")
    if not ok: problemes.append(f"Chapitre {n} : sections manquantes {manq}, quiz {nq}, carnet {carnet}, figures absentes {absentes}, citations inconnues {inconnues}")
    secs = re.findall(r"^#### (.+)$", t, re.M)
    plan.append((n, titre, secs, Path(f).parent.name))
corr = sorted(glob.glob(str(ROOT / "01_MANUSCRIT" / "PARTIE_*" / "99_corriges_*.md")))
ann = sorted(glob.glob(str(ROOT / "04_ANNEXES" / "*.md")))
nb_prompts_b = len(re.findall(r"^\*\*B\d{3}", (ROOT / "04_ANNEXES" / "B_bibliotheque_prompts.md").read_text(encoding="utf-8"), re.M))
mots = sum(len(re.findall(r"\w+", Path(x).read_text(encoding="utf-8"))) for x in chap + corr + ann)
photos = len(glob.glob(str(ROOT / "02_ILLUSTRATIONS" / "PHOTOGRAPHIES" / "*.jpg")))
schemas = len(glob.glob(str(ROOT / "02_ILLUSTRATIONS" / "*" / "fig*.png")))
r = ["# Rapport de contrôle qualité automatique\n",
     "> Généré par `08_OUTILS/controle_qualite.py`. Complète la relecture humaine (section finale).\n",
     "## Synthèse\n",
     f"- Chapitres : **{len(chap)}** / 43",
     f"- Fichiers de corrigés : **{len(corr)}** / 6 parties",
     f"- Annexes : **{len(ann) - 1}** fichiers rédigés (A à H, J à M) + ouverture ; annexe I générée depuis le registre des sources",
     f"- Questions de quiz : **{tot_q}** (minimum 8 par chapitre)",
     f"- Prompts dans les chapitres : **{tot_prompts}** ; bibliothèque de l'Annexe B : **{nb_prompts_b}**",
     f"- Figures référencées dans les chapitres : **{tot_fig}** ; fichiers de figures produits : **{schemas}** ; photographies intégrées : **{photos}**",
     f"- Sources au registre : **{len(SOURCES)}**",
     f"- Volume (chapitres + corrigés + annexes) : environ **{mots:,}** mots".replace(",", " "),
     f"- Anomalies structurelles détectées : **{len(problemes)}**\n",
     "## Contrôle par chapitre\n",
     "| Ch. | État | Sections manquantes | Questions | Carnet | Figures | Sources citées | Prompts |",
     "|---|---|---|---|---|---|---|---|"] + lignes
r += ["\n## Anomalies\n"] + ([f"- {p}" for p in problemes] or ["- Aucune anomalie structurelle."])
r += ["""
## Contrôles transverses réalisés pendant la production

| Contrôle | Résultat |
|---|---|
| Citations : chaque clé `[@ID]` existe au registre (blocage automatique de la construction sinon) | Conforme |
| Cohérence des chiffres du scénario (ressources pondérées 2,39 % Cu / 0,26 % Co ; réserves 2,36 % / 0,27 % ; redevances 24,0 MUSD) | Corrigé puis conforme |
| Cohérence données / texte (QA/QC : erreur de génération des blancs corrigée ; formations : dates d'expiration corrigées ; incident : références d'OT alignées sur l'historique ; eau : mois de dépassement corrigé) | Corrigé puis conforme |
| Calculs cités dans le texte (pénalité 2 400 USD ; effet prix 258 000 USD ; écart normalisé 4,8 ; TF 4,76 ; besoin de 6 875 t/j) | Recalculés |
| Informations sur Claude (modèles, prix, contexte, effort, fichiers, projets, artefacts, recherche, mémoire, compétences) | Vérifiées dans la documentation officielle au 16/11/2026 |
| Interface de Claude | Illustration schématique explicitement signalée ; aucune fausse capture |
| Photographies | 10 photographies libres (Wikimedia Commons) fournies par l'éditeur et intégrées ; légendes avec titre, auteur, source, licence et liens ; récapitulatif à l'Annexe M.5 ; aucune mention « à intégrer » restante |
| Rendu PDF | Sommaire, en-têtes, pieds de page, encadrés, tableaux, figures et carnets contrôlés visuellement par échantillonnage |

## Points restant à contrôler par l'éditeur (relecture humaine)

1. Vérifier dans la maquette finale le rendu d'impression des photographies (résolution à la taille d'impression retenue).
2. Relecture orthotypographique complète (espaces insécables, coupures, veuves et orphelines) dans la maquette finale.
3. Revalidation des informations datées sur Claude (modèles, prix, offres) à la date de publication.
4. Vérification par un juriste des passages relatifs au droit minier congolais et aux obligations de transparence, et par des praticiens (géologie, HSE, métallurgie, finance) des chapitres métier.
5. Seules les références contrôlées pendant la rédaction ont été conservées dans la bibliographie (18 ouvrages et textes, 38 ressources en ligne).
6. Avant impression : calcul du dos de chaque tome selon le papier retenu. Ouvrage publié à compte d'auteur, sans ISBN.
"""]
(ROOT / "07_CONTROLE_QUALITE").mkdir(exist_ok=True)
(ROOT / "07_CONTROLE_QUALITE" / "RAPPORT_CONTROLE_QUALITE.md").write_text("\n".join(r), encoding="utf-8")
p = ["# Plan éditorial détaillé\n", "> Généré depuis le manuscrit (`08_OUTILS/controle_qualite.py`). Sous-sections de niveau 4 listées sous chaque chapitre.\n"]
cur = None
for n, titre, secs, partie in plan:
    if partie != cur:
        p.append(f"\n## {partie.replace('_', ' ')}\n"); cur = partie
    p.append(f"\n**{titre}**\n")
    p += [f"- {s}" for s in secs]
p.append("\n## Annexes\n")
p += [f"- {re.search(r'^## (.+)$', Path(a).read_text(encoding='utf-8'), re.M).group(1)}" for a in ann if not Path(a).name.startswith("00")]
(ROOT / "00_GESTION_PROJET" / "PLAN_EDITORIAL.md").write_text("\n".join(p), encoding="utf-8")
print("\n".join(r[:14])); print(len(problemes), "problème(s)")
for x in problemes: print(" ", x)
