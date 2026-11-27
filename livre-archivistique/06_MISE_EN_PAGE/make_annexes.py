#!/usr/bin/env python3
"""Fichiers modifiables des annexes : registre Excel + modèles Word."""
import pathlib, subprocess, re, unicodedata
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.worksheet.table import Table, TableStyleInfo
import build, make_docx

ROOT = build.ROOT
OUT = ROOT / "04_ANNEXES"
OUT.mkdir(exist_ok=True)
NAVY, GOLD = "0A1E3F", "2D5A3B"

def registre():
    wb = Workbook()
    ws = wb.active; ws.title = "Registre"
    cols = ["Cote", "Rubrique", "Intitulé", "Date début", "Date fin", "Service producteur", "Support", "Mots-clés",
            "Confidentialité", "Localisation", "DUA (années)", "Sort final", "Échéance (année)", "Statut", "Observations"]
    widths = [22, 10, 42, 11, 11, 12, 11, 30, 16, 14, 11, 11, 13, 12, 30]
    ws.append(cols)
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[ws.cell(1, i).column_letter].width = w
        c = ws.cell(1, i); c.font = Font(bold=True, color="FFFFFF", name="Calibri"); c.fill = PatternFill("solid", fgColor=NAVY)
        c.alignment = Alignment(wrap_text=True, vertical="center")
    ex = [["HOR/02.03/2024/0001", "02.03", "Factures fournisseurs, janvier 2024", 2024, 2024, "FIN", "Papier", "facture ; fournisseur", "Interne", "A-02-3-045", 10, "D", None, "En place", "Durée fictive : à valider selon la loi applicable"],
          ["HOR/03.02/2019/014", "03.02", "Dossier individuel, MUKENDI Paul", 2019, 2024, "RHU", "Papier", "contrat ; départ ; formateur", "Confidentiel", "B-01-2-008", 5, "T", None, "En place", "Exemple fictif"],
          ["HOR/05.01/2022/003", "05.01", "Convention Fondation Alizé, projet Cap Emploi", 2022, 2025, "DIR", "Mixte", "convention ; avenant ; Alizé", "Confidentiel", "A-05-1-001", None, "C", None, "En place", "Exemple fictif"]]
    for r in ex:
        ws.append(r)
    n = 500
    for row in range(2, n + 2):
        ws.cell(row, 13).value = f'=IF(AND(ISNUMBER(E{row}),ISNUMBER(K{row})),E{row}+K{row},"")'
    ws.freeze_panes = "A2"
    tab = Table(displayName="Registre", ref=f"A1:O{n+1}")
    tab.tableStyleInfo = TableStyleInfo(name="TableStyleLight9", showRowStripes=True)
    ws.add_table(tab)
    # paramètres
    ps = wb.create_sheet("Paramètres")
    lists = {"Rubriques": ["01.01", "01.02", "01.03", "01.04", "01.05", "02.01", "02.02", "02.03", "02.04", "02.05", "02.06", "02.07",
                           "03.01", "03.02", "03.03", "03.04", "03.05", "04.01", "04.02", "04.03", "04.04", "05.01", "05.02", "05.03",
                           "06.01", "06.02", "06.03", "06.04", "07.01", "07.02", "07.03", "07.04"],
             "Services": ["DIR", "FIN", "RHU", "PRG", "LOG", "COM"], "Supports": ["Papier", "Numérique", "Mixte"],
             "Confidentialité": ["Public", "Interne", "Confidentiel", "Strictement confidentiel"],
             "Sort final": ["C", "D", "T"], "Statut": ["En place", "Prêté", "Versé", "Gelé", "Éliminé"]}
    for j, (k, vals) in enumerate(lists.items(), 1):
        c = ps.cell(1, j, k); c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor=NAVY)
        ps.column_dimensions[c.column_letter].width = 22
        for i, v in enumerate(vals, 2):
            ps.cell(i, j, v)
    ps.cell(1, 8, "Mode d'emploi").font = Font(bold=True, color=NAVY, size=12)
    for i, t in enumerate(["Modifiez les listes de cet onglet pour les adapter à votre plan de classement et à vos services.",
                           "La colonne Échéance se calcule automatiquement : année de fin + DUA.",
                           "Une cote saisie deux fois apparaît en rouge (contrôle d'unicité).",
                           "Les durées des exemples sont fictives : fixez-les selon votre tableau de gestion validé.",
                           "Modèle accompagnant l'ouvrage « L'archivistique : principes et pratiques du métier d'archiviste », Verdi Imbole, 2026."], 2):
        ps.cell(i, 8, t)
    ps.column_dimensions["H"].width = 100
    def dv(col, listcol, nvals):
        letter = ps.cell(1, listcol).column_letter
        d = DataValidation(type="list", formula1=f"=Paramètres!${letter}$2:${letter}${nvals+1}", allow_blank=True)
        ws.add_data_validation(d); d.add(f"{col}2:{col}{n+1}")
    dv("B", 1, len(lists["Rubriques"])); dv("F", 2, 6); dv("G", 3, 3); dv("I", 4, 4); dv("L", 5, 3); dv("N", 6, 5)
    red = PatternFill("solid", fgColor="F4C7C3")
    ws.conditional_formatting.add(f"A2:A{n+1}", FormulaRule(formula=[f'AND($A2<>"",COUNTIF($A$2:$A${n+1},$A2)>1)'], fill=red))
    wb.save(OUT / "Registre_suivi_documentaire.xlsx")

def word_templates():
    md = (build.MS / "annexes.md").read_text()
    fm, body = build.split_front(md)
    blocks = re.split(r"^## ", body, flags=re.M)[1:]
    ref = make_docx.OUTD / "reference.docx"
    lua = make_docx.OUTD / "boxes.lua"
    for b in blocks:
        title = b.splitlines()[0].strip()
        letter = re.match(r"Annexe (\w)", title).group(1)
        slug = re.sub(r"[^A-Za-z0-9]+", "_", unicodedata.normalize("NFKD", title.split("·")[1].strip()).encode("ascii", "ignore").decode())[:50].strip("_")
        src = f"# {title}\n\n" + "\n".join(b.splitlines()[1:]) + "\n\n*Modèle issu de l'ouvrage « L'archivistique : principes et pratiques du métier d'archiviste », Verdi Imbole, 2026. Reproduction autorisée pour les besoins internes de l'acquéreur.*\n"
        tmp = make_docx.OUTD / f"annexe_{letter}.md"; tmp.write_text(src)
        out = OUT / f"Annexe_{letter}_{slug}.docx"
        subprocess.run(["pandoc", str(tmp), "-o", str(out), "--reference-doc", str(ref), "--lua-filter", str(lua)], check=True)
        make_docx.postprocess_light(out)
        print("ok", out.name)

if __name__ == "__main__":
    registre()
    word_templates()
