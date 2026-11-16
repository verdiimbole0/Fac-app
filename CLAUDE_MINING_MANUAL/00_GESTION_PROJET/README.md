# CLAUDE ET L'INTELLIGENCE ARTIFICIELLE AU SERVICE DE L'INDUSTRIE MINIÈRE

*Le guide pratique pour comprendre, maîtriser et intégrer l'IA dans les métiers et processus de l'industrie minière.*

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
python3 08_OUTILS/construire_livre.py     # DOCX + PDF dans 06_PRODUCTION_FINALE/
python3 08_OUTILS/controle_qualite.py     # rapport de contrôle qualité + plan éditorial
```

Dépendances : Python 3 (matplotlib, openpyxl, python-docx), pandoc ≥ 3, LibreOffice (conversion PDF).

## Livrables

| Livrable | Emplacement |
|---|---|
| Manuscrit Word éditable | `06_PRODUCTION_FINALE/CLAUDE_ET_IA_INDUSTRIE_MINIERE.docx` |
| Manuscrit PDF (391 pages) | `06_PRODUCTION_FINALE/CLAUDE_ET_IA_INDUSTRIE_MINIERE.pdf` |
| Sources Markdown | `01_MANUSCRIT/`, `04_ANNEXES/` |
| Illustrations | `02_ILLUSTRATIONS/` (+ `PHOTOGRAPHIES/CREDITS_PHOTOS.json`) |
| Données d'exercice | `03_EXERCICES_ET_DONNEES/` |
| Registre bibliographique | `05_BIBLIOGRAPHIE_WEBOGRAPHIE/REGISTRE_SOURCES.csv` |
| Contrôle qualité | `07_CONTROLE_QUALITE/RAPPORT_CONTROLE_QUALITE.md` |

**Photographies :** les 14 photographies sélectionnées (licences libres, crédits complets) sont des emplacements réservés : Wikimedia a refusé le téléchargement automatisé. Pour les intégrer : `python3 08_OUTILS/photos.py telecharger "MonOutil/1.0 (contact: adresse@exemple.org)"`, puis reconstruire.

## Avertissement

L'entreprise **Mbiyo Copper Cobalt SA (MCC)** et toutes ses données sont **fictives**. Les informations sur Claude reflètent la documentation officielle consultée le **16 novembre 2026** ; elles évoluent rapidement et doivent être revérifiées avant chaque réédition.
