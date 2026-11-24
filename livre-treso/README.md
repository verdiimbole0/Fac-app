# LA TRÉSO SOUS CONTRÔLE

Manuel de gestion de trésorerie de Verdi Imbole (A5, 121 pages).

## Livrables (`livrables/`)
- `LA_TRESO_SOUS_CONTROLE.docx` : manuel Word modifiable
- `LA_TRESO_SOUS_CONTROLE.pdf` : version PDF (A5, polices intégrées)
- `illustrations/` : les 12 figures (PNG 300 dpi)
- `Registre_des_sources.docx` / `.md` : références, URL, licences, registre des illustrations
- `outils_excel/` : 10 modèles Excel séparés + classeur combiné `Outils_Treso_sous_controle.xlsx`
- `Rapport_controle_qualite.docx` / `.md`

## Sources du livre
- `data/fil_rouge.py` : données centrales du cas MAKAO et de l'ASBL (toutes les valeurs du livre)
- `content/*.md` : texte du manuscrit (balisage simple : `@table`, `@figure`, encadrés `:::type`)
- `build/` : générateurs (Word, graphiques, Excel, sommaire et index)

## Reconstruire
Prérequis : Python 3 avec python-docx, openpyxl, matplotlib ; LibreOffice ; polices Montserrat et Source Sans 3 installées.
```bash
python3 build/charts.py && build/make_all.sh && python3 build/build_excel.py
```
`make_all.sh` génère le Word, l'exporte en PDF et recalcule sommaire et index (deux passes).
