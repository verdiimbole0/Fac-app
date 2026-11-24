# LA TRÉSO SOUS CONTRÔLE

Manuel de gestion de trésorerie de Verdi Imbole (A5, 123 pages intérieures).

## Livrables (`livrables/`)
- `LA_TRESO_SOUS_CONTROLE.docx` : manuel Word modifiable
- `LA_TRESO_SOUS_CONTROLE.pdf` : intérieur pour l'impression (A5, polices intégrées)
- `LA_TRESO_SOUS_CONTROLE_edition_lecture.pdf` : édition lecture avec 1re et 4e de couverture
- `couverture/` : 1re et 4e de couverture, maquette d'impression complète (dos + fonds perdus)
- `illustrations/` : les 12 figures (PNG 300 dpi)
- `Registre_des_sources.docx` / `.md` : références, URL, licences, registre des illustrations
- `outils_excel/` : 10 modèles Excel séparés + classeur combiné `Outils_Treso_sous_controle.xlsx`
- `Rapport_controle_qualite.docx` / `.md`

## Sources du livre
- `data/fil_rouge.py` : données centrales du cas MAKAO et de l'ASBL (toutes les valeurs du livre)
- `content/*.md` : texte du manuscrit (balisage simple : `@table`, `@figure`, encadrés `:::type`)
- `build/` : générateurs (Word, graphiques, Excel, sommaire et index)

## Reconstruire
Prérequis : Python 3 avec python-docx, openpyxl, matplotlib, Pillow ; LibreOffice avec le dictionnaire de césure hyphen-fr ; polices Montserrat, Source Sans 3 et Source Serif 4 installées.
```bash
python3 build/charts.py && python3 build/visuals.py && build/make_all.sh && python3 build/cover.py 123 && python3 build/build_excel.py
```
`make_all.sh` génère le Word, l'exporte en PDF et recalcule sommaire et index (deux passes).
