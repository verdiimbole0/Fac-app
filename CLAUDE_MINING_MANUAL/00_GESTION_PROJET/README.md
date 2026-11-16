# LA MINE AUGMENTÉE

*Maîtriser Claude et l'intelligence artificielle générative dans les métiers et les processus miniers.*

Projet éditorial — manuel de formation professionnelle (6 parties, 43 chapitres, 13 annexes).

## Arborescence

| Dossier | Contenu |
|---|---|
| `00_GESTION_PROJET/` | Pilotage : plan éditorial, cartographie des compétences, charte éditoriale, scénario fil conducteur, suivi de production, registre des sources |
| `01_MANUSCRIT/` | Sources Markdown du manuscrit, un fichier par chapitre, rangés par partie (`PARTIE_0_LIMINAIRES` à `PARTIE_VI`) |
| `02_ILLUSTRATIONS/` | Schémas, infographies, graphiques (PNG + SVG), photographies sous licence libre, illustrations schématiques de l'interface Claude |
| `03_EXERCICES_ET_DONNEES/` | Jeux de données fictifs (CSV, XLSX), documents d'exercice (DOCX, PDF) |
| `04_ANNEXES/` | Annexes A à M (Markdown) |
| `05_BIBLIOGRAPHIE_WEBOGRAPHIE/` | Bibliographie, webographie et registre machine-lisible des sources |
| `06_PRODUCTION_FINALE/` | Livrables : manuscrit DOCX et PDF |
| `07_CONTROLE_QUALITE/` | Rapports de contrôle qualité |
| `08_OUTILS/` | Scripts de production (figures, données, assemblage DOCX/PDF) |

## Reconstruire le livre

```bash
cd CLAUDE_MINING_MANUAL
python3 08_OUTILS/generer_donnees.py      # jeux de données d'exercice
python3 08_OUTILS/generer_figures.py      # schémas et graphiques
python3 08_OUTILS/couvertures.py          # 1re et 4e de couverture
python3 08_OUTILS/construire_livre.py     # DOCX + PDF dans 06_PRODUCTION_FINALE/
python3 08_OUTILS/controle_qualite.py     # rapport de contrôle qualité + plan éditorial
```

Dépendances : Python 3 (matplotlib, openpyxl, python-docx, fonttools), pandoc ≥ 3, LibreOffice (conversion PDF), polices EB Garamond (paquet `fonts-ebgaramond`) et césure française (`hyphen-fr`).

**Polices :** le gras d'EB Garamond fourni par Debian est incomplet (pas de lettres accentuées). Installer les fichiers de `08_OUTILS/polices/` (licence OFL, fichier joint) dans `~/.local/share/fonts/`, retirer `EBGaramond12-Bold` du système, puis lancer `fc-cache -f`. Créer l'alias fontconfig `Garamond` → `EB Garamond 12`.

## Maquette

Format 15,5 × 23,5 cm, marges en miroir, titres courants (titre du livre en page paire, chapitre en page impaire), folios centrés, EB Garamond 11 pt, alinéas et justification avec césure, titres sans gras, tableaux à filets, encadrés à filets cuivre sur fond crème. Pages liminaires sans titre courant ; le corps commence en belle page ; la 4e de couverture tombe toujours en page paire.

## Livrables

| Livrable | Emplacement |
|---|---|
| Livre Word éditable | `06_PRODUCTION_FINALE/LA_MINE_AUGMENTEE.docx` |
| Livre PDF (610 pages, couvertures incluses) | `06_PRODUCTION_FINALE/LA_MINE_AUGMENTEE.pdf` |
| Couverture et 4e de couverture | `02_ILLUSTRATIONS/COUVERTURES/` (PDF vectoriel + PNG 300 dpi) |
| Sources Markdown | `01_MANUSCRIT/`, `04_ANNEXES/` |
| Illustrations | `02_ILLUSTRATIONS/` (+ `PHOTOGRAPHIES/CREDITS_PHOTOS.json`) |
| Données d'exercice | `03_EXERCICES_ET_DONNEES/` |
| Registre bibliographique | `05_BIBLIOGRAPHIE_WEBOGRAPHIE/REGISTRE_SOURCES.csv` |
| Contrôle qualité | `07_CONTROLE_QUALITE/RAPPORT_CONTROLE_QUALITE.md` |

**Photographies :** 10 photographies sous licence libre (Wikimedia Commons) sont intégrées, avec titre, auteur, source, licence et liens dans chaque légende, et récapitulées à l'Annexe M.5. Elles ont été fournies par l'éditeur et intégrées avec `08_OUTILS/integrer_photos.py`.

## Avertissement

L'entreprise **Mbiyo Copper Cobalt SA (MCC)** et toutes ses données sont **fictives**. Les informations sur Claude reflètent la documentation officielle consultée le **16 novembre 2026** ; elles évoluent rapidement et doivent être revérifiées avant chaque réédition.
