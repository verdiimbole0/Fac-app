# ASBL AUGMENTÉE — Comment implémenter l'IA dans vos processus

Manuscrit de Verdi Imbole (titre et sous-titre provisoires). Version complète soumise à la validation de l'auteur — novembre 2026.

## Livrables (`06_LIVRABLES/`)

| Fichier | Contenu |
|---|---|
| `MANUSCRIT_FINAL.pdf` | Version de relecture et d'impression, 17 × 24 cm, ≈ 426 pages, table des matières paginée |
| `MANUSCRIT_FINAL.docx` | Version Word modifiable (mettre à jour la table des matières à l'ouverture ; installer les polices Source Serif 4, Source Sans 3 et JetBrains Mono, licence OFL) |
| `MANUSCRIT_SOURCE.md` | Manuscrit assemblé en Markdown |
| `ANNEXES.zip` | 22 annexes (.md, .docx, .xlsx) et données d'exercice |

## Arborescence

```
01_RECHERCHE_DOCUMENTAIRE/  registre des sources (CSV + commentaire), registre des licences d'images
02_MANUSCRIT/               sources Markdown : liminaires, parties 1 à 6 (modules 1 à 22), conclusion, pages finales
03_ILLUSTRATIONS/           figures originales SVG, versions PNG, crédits, note sur les captures
04_ANNEXES/                 22 annexes + données d'exercice (fichier fictif de dépenses du module 13)
05_CONTROLE_QUALITE/        rapports de contrôle (factuel, scientifique, comptable, bibliographique, éditorial, illustrations, final)
06_LIVRABLES/               fichiers compilés
07_OUTILS/                  scripts de production (figures, annexes, compilation, contrôles), styles, polices
```

## Recompiler

Depuis `ASBL_AUGMENTEE/` (pandoc, Python 3 avec openpyxl et python-docx, Node.js avec Playwright/Chromium) :

```bash
python3 07_OUTILS/figures.py 03_ILLUSTRATIONS/figures
NODE_PATH=$(npm root -g) node 07_OUTILS/render_png.js "$PWD/03_ILLUSTRATIONS/figures" "$PWD/03_ILLUSTRATIONS/png"
python3 07_OUTILS/make_reference.py
python3 07_OUTILS/annexes.py
python3 07_OUTILS/build.py
python3 07_OUTILS/controles.py
```

Le module 13 s'appuie sur des tests réellement exécutés : `python3 07_OUTILS/tests_audit.py 04_ANNEXES/donnees_exercices/depenses_RCE_T1_2026.csv 04_ANNEXES/donnees_exercices/fournisseurs_RCE.csv`.

## Points à valider par l'auteur

Voir `05_CONTROLE_QUALITE/controle_final.md`.

## Composants tiers

Polices Source Serif 4, Source Sans 3 et JetBrains Mono : SIL Open Font License 1.1 (`07_OUTILS/fonts/`). Paged.js (MIT) pour la mise en page du PDF (`07_OUTILS/vendor/`).
