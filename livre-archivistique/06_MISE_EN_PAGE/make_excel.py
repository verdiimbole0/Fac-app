#!/usr/bin/env python3
"""Les dix modèles de l'ouvrage en classeurs Excel modifiables (annexes A à J).
Chaque classeur : Mode d'emploi · Modèle (vierge, formules et listes) · Exemple (cas fictif Horizon) · Listes."""
import pathlib, datetime as dt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule, CellIsRule, DataBarRule
from openpyxl.chart import BarChart, Reference
from openpyxl.utils import get_column_letter as L

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "04_ANNEXES"
OUT.mkdir(exist_ok=True)

NAVY, NAVY2, PAST, PASTL, PMID = "0A1E3F", "1F3A68", "DCE9F7", "EFF5FC", "8FB4E0"
MOUT, OCRE, MOUTL, ORANGE, ORL, BORD, BORL, WHITE = "D9A520", "A8761A", "FBF3DC", "E07B39", "FDF1E7", "7B1E30", "F7EBEE", "FFFFFF"
FONT = "Calibri"
thin = Side(style="thin", color="BFD3EC")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
CREDIT = "Modèle issu de l'ouvrage « L'archivistique : principes et pratiques du métier d'archiviste », Verdi Imbole, 2026. Reproduction autorisée pour les besoins internes de l'acquéreur."

def fill(c): return PatternFill(fill_type="solid", start_color=c, end_color=c)

def banner(ws, title, subtitle, ncols, letter):
    """Bandeau de titre aux couleurs de l'ouvrage."""
    last = L(ncols)
    ws.merge_cells(f"A1:{last}1"); ws.merge_cells(f"A2:{last}2")
    c = ws["A1"]; c.value = f"ANNEXE {letter} · {title.upper()}"
    c.font = Font(name=FONT, size=15, bold=True, color=WHITE); c.fill = fill(NAVY); c.alignment = Alignment(vertical="center", indent=1)
    ws.row_dimensions[1].height = 30
    c = ws["A2"]; c.value = subtitle
    c.font = Font(name=FONT, size=10, italic=True, color=NAVY); c.fill = fill(PAST); c.alignment = Alignment(vertical="center", indent=1, wrap_text=True)
    ws.row_dimensions[2].height = 30
    cols = [NAVY2, PMID, MOUT, ORANGE, BORD]
    for i in range(1, ncols + 1):  # filet aux cinq couleurs
        ws.cell(3, i).fill = fill(cols[(i - 1) * len(cols) // ncols])
    ws.row_dimensions[3].height = 4

def label(ws, cell, text, value=None, merge_to=None, width_note=None):
    """Champ d'en-tête : étiquette ocre + zone de saisie bleu pastel."""
    c = ws[cell]; c.value = text
    c.font = Font(name=FONT, size=9, bold=True, color=OCRE)
    c.alignment = Alignment(vertical="center", wrap_text=True)
    col, row = c.column, c.row
    if (ws.row_dimensions[row].height or 0) < 26:
        ws.row_dimensions[row].height = 26
    t = ws.cell(row, col + 1)
    if merge_to and merge_to > col + 1:
        ws.merge_cells(start_row=row, start_column=col + 1, end_row=row, end_column=merge_to)
    t.fill = fill(PASTL); t.border = BOX; t.font = Font(name=FONT, size=10, color=NAVY)
    t.alignment = Alignment(vertical="center", wrap_text=True)
    if value is not None:
        t.value = value
    return t

def header_row(ws, row, headers, widths=None, color=NAVY):
    for i, h in enumerate(headers, 1):
        c = ws.cell(row, i, h)
        c.font = Font(name=FONT, size=9.5, bold=True, color=WHITE); c.fill = fill(color)
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center"); c.border = BOX
        if widths:
            ws.column_dimensions[L(i)].width = widths[i - 1]
    ws.row_dimensions[row].height = 34

def body(ws, r0, r1, ncols, formula_cols=(), center_cols=(), wrap=True, zebra=True):
    for r in range(r0, r1 + 1):
        for cidx in range(1, ncols + 1):
            c = ws.cell(r, cidx)
            c.border = BOX
            c.font = Font(name=FONT, size=10, color=NAVY if cidx not in formula_cols else NAVY2, italic=cidx in formula_cols)
            c.alignment = Alignment(wrap_text=wrap, vertical="top", horizontal="center" if cidx in center_cols else "left")
            if cidx in formula_cols:
                c.fill = fill(MOUTL)
            elif zebra and (r - r0) % 2 == 1:
                c.fill = fill(PASTL)

def dv_list(ws, rng, src, prompt=None):
    d = DataValidation(type="list", formula1=src, allow_blank=True, showErrorMessage=True,
                       errorTitle="Valeur non prévue", error="Choisissez une valeur dans la liste (modifiable dans l'onglet Listes).")
    if prompt:
        d.promptTitle = "Aide"; d.prompt = prompt; d.showInputMessage = True
    ws.add_data_validation(d); d.add(rng)

def dv_int(ws, rng, lo, hi, msg):
    d = DataValidation(type="whole", operator="between", formula1=str(lo), formula2=str(hi), allow_blank=True,
                       showErrorMessage=True, errorTitle="Valeur hors plage", error=msg)
    ws.add_data_validation(d); d.add(rng)

def dv_date(ws, rng):
    d = DataValidation(type="date", operator="greaterThan", formula1="DATE(1900,1,1)", allow_blank=True,
                       showErrorMessage=True, errorTitle="Date attendue", error="Saisissez une date (jj/mm/aaaa).")
    ws.add_data_validation(d); d.add(rng)

def print_setup(ws, landscape=True, title_rows=None):
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.orientation = "landscape" if landscape else "portrait"
    ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins.left = ws.page_margins.right = 0.4; ws.page_margins.top = 0.5; ws.page_margins.bottom = 0.6
    if title_rows:
        ws.print_title_rows = title_rows
    ws.oddFooter.left.text = "Verdi Imbole · L'archivistique"; ws.oddFooter.left.size = 8
    ws.oddFooter.right.text = "Page &P / &N"; ws.oddFooter.right.size = 8
    ws.sheet_view.showGridLines = False

def footer_note(ws, row, ncols):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
    c = ws.cell(row, 1, CREDIT); c.font = Font(name=FONT, size=8, italic=True, color="5A6476"); c.alignment = Alignment(wrap_text=True)
    ws.row_dimensions[row].height = 24

def lists_sheet(wb, lists):
    ws = wb.create_sheet("Listes")
    ws.sheet_view.showGridLines = False
    for j, (k, vals) in enumerate(lists.items(), 1):
        c = ws.cell(1, j, k); c.font = Font(name=FONT, bold=True, color=WHITE); c.fill = fill(NAVY2)
        ws.column_dimensions[L(j)].width = max(16, len(k) + 4)
        for i, v in enumerate(vals, 2):
            ws.cell(i, j, v).border = BOX
    n = len(lists) + 2
    ws.cell(1, n, "Ces listes alimentent les menus déroulants. Ajoutez ou modifiez des valeurs dans les cellules prévues : les menus suivent.").font = Font(name=FONT, italic=True, color=OCRE)
    refs = {}
    for j, (k, vals) in enumerate(lists.items(), 1):
        refs[k] = f"=Listes!${L(j)}$2:${L(j)}${len(vals) + 1 + 10}"  # 10 lignes de réserve
    return refs

def guide_sheet(wb, letter, title, purpose, steps, example, tips):
    ws = wb.active; ws.title = "Mode d'emploi"
    ws.column_dimensions["A"].width = 3; ws.column_dimensions["B"].width = 110
    banner(ws, title, purpose, 2, letter)
    r = 5
    def block(t, lines, color):
        nonlocal r
        c = ws.cell(r, 2, t); c.font = Font(name=FONT, bold=True, size=11, color=WHITE); c.fill = fill(color); c.alignment = Alignment(indent=1)
        r += 1
        for ln in lines:
            c = ws.cell(r, 2, ln); c.font = Font(name=FONT, size=10.5, color=NAVY); c.alignment = Alignment(wrap_text=True, indent=1, vertical="top")
            ws.row_dimensions[r].height = 16 * max(1, len(ln) // 120 + 1)
            r += 1
        r += 1
    block("COMMENT UTILISER CE MODÈLE", [f"{i}. {s}" for i, s in enumerate(steps, 1)], NAVY)
    block("EXEMPLE D'UTILISATION (cas fictif : Organisation Horizon)", [example], MOUT)
    block("BONNES PRATIQUES ET PRÉCAUTIONS", ["• " + t for t in tips], ORANGE)
    block("CODE COULEUR DES CELLULES", ["Bleu pastel : zone de saisie.   Jaune moutarde clair : calcul automatique, ne pas écraser.   Orange ou bordeaux : alerte à traiter."], NAVY2)
    c = ws.cell(r, 2, CREDIT); c.font = Font(name=FONT, size=8.5, italic=True, color="5A6476"); c.alignment = Alignment(wrap_text=True)
    ws.sheet_view.showGridLines = False
    print_setup(ws, landscape=False)
    return ws

def copy_as_example(wb, src_name, data_fn):
    """Duplique la feuille modèle et la remplit avec l'exemple fictif."""
    src = wb[src_name]
    ex = wb.copy_worksheet(src); ex.title = "Exemple Horizon"
    # copy_worksheet ne recopie ni les mises en forme conditionnelles ni les listes déroulantes
    for rng in src.conditional_formatting:
        for rule in rng.rules:
            ex.conditional_formatting.add(str(rng.sqref), rule)
    import copy as _copy
    for d in src.data_validations.dataValidation:
        ex.add_data_validation(_copy.copy(d))
    ex.freeze_panes = src.freeze_panes
    if src.auto_filter.ref:
        ex.auto_filter.ref = src.auto_filter.ref
    ex.print_title_rows = src.print_title_rows
    ex.sheet_view.showGridLines = False
    ex.sheet_properties.tabColor = MOUT
    data_fn(ex)
    return ex

def set_print_areas(wb):
    """Zone d'impression : en-tête + lignes utiles (40 lignes vierges sur les modèles)."""
    for ws in wb.worksheets:
        if ws.title in ("Listes", "Mode d'emploi", "Fiche"):
            continue
        hdr = next((r for r in range(4, 15) if ws.cell(r, 1).fill.fgColor.rgb in ("00" + NAVY, "FF" + NAVY) and ws.cell(r, 2).value), None)
        if hdr is None:
            continue
        last_data = hdr
        for r in range(hdr + 1, ws.max_row + 1):
            if any(ws.cell(r, c).value not in (None, "") and not str(ws.cell(r, c).value).startswith("=") for c in range(2, ws.max_column + 1)):
                last_data = r
        limit = max(last_data + (40 if ws.title != "Exemple Horizon" else 3), hdr + 20)
        ws.print_area = f"A1:{L(ws.max_column)}{min(limit, ws.max_row)}"

def finish(wb, name, model_name):
    set_print_areas(wb)
    wb[model_name].sheet_properties.tabColor = NAVY
    wb["Mode d'emploi"].sheet_properties.tabColor = ORANGE
    wb["Listes"].sheet_properties.tabColor = PMID
    order = ["Mode d'emploi"] + [x for x in wb.sheetnames if x not in ("Mode d'emploi", "Exemple Horizon", "Listes")] + ["Exemple Horizon", "Listes"]
    wb._sheets = [wb[s] for s in order]
    wb.active = 1
    wb.properties.creator = "Verdi Imbole"; wb.properties.title = name
    wb.save(OUT / f"{name}.xlsx")
    print("ok", name)

SERVICES = ["DIR", "FIN", "RHU", "PRG", "LOG", "COM"]
CONF = ["Public", "Interne", "Confidentiel", "Strictement confidentiel"]
SORT = ["C", "D", "T"]

# ======================================================================= A
def annexe_A():
    wb = Workbook()
    guide_sheet(wb, "A", "Fiche d'inventaire des archives",
                "Recenser, local par local et système par système, les volumes, les périodes et l'état des archives (diagnostic, collecte, déménagement).",
                ["Renseignez l'en-tête : organisation, local ou système inventorié, date et auteur.",
                 "Ajoutez une ligne par lot : boîte, armoire, dossier, répertoire numérique ou boîte mail.",
                 "Choisissez l'unité (ml, boîtes, Go) et l'état de conservation dans les menus déroulants.",
                 "Les totaux par unité et le nombre de lots en état critique se calculent seuls.",
                 "Signalez toute urgence (humidité, moisissures, accès libre) dans la colonne prévue : elle passe en orange."],
                "Ligne 1 : « Cartons Projets 2019-2021, sous-sol », PRG, 2019-2021, 1,2 ml, papier, état critique (moisissures visibles), urgence : isoler immédiatement.",
                ["Ne déplacez aucun lot avant d'avoir noté sa provenance.", "Photographiez les locaux : les photos complètent l'inventaire.",
                 "1 mètre linéaire (ml) = 1 mètre de tablette occupée ; une boîte standard de 10 cm = 0,10 ml."])
    refs = lists_sheet(wb, {"Services": SERVICES, "Unités": ["ml", "boîtes", "Go"], "Supports": ["Papier", "Numérique", "Mixte"],
                            "État": ["Bon", "Moyen", "Dégradé", "Critique"], "Urgence": ["Aucune", "À surveiller", "Immédiate"]})
    ws = wb.create_sheet("Inventaire", 1)
    H = ["N°", "Désignation du lot (boîte, armoire, dossier, répertoire)", "Service producteur", "Date début", "Date fin", "Volume", "Unité", "Support", "État de conservation", "Urgence", "Observations"]
    W = [15, 44, 12, 10, 10, 9, 9, 11, 14, 13, 36]
    banner(ws, "Fiche d'inventaire des archives", "Une ligne par lot. Les cellules bleues se saisissent, les cellules moutarde se calculent.", len(H), "A")
    label(ws, "A5", "Organisation", merge_to=4); label(ws, "F5", "Local / système", merge_to=8)
    label(ws, "A6", "Date", merge_to=4); label(ws, "F6", "Réalisé par", merge_to=8)
    ws["B6"].number_format = "dd/mm/yyyy"
    header_row(ws, 9, H, W)
    r0, r1 = 10, 109
    for r in range(r0, r1 + 1):
        ws.cell(r, 1, f'=IF(B{r}="","",ROW()-{r0-1})')
    body(ws, r0, r1, len(H), formula_cols=(1,), center_cols=(1, 3, 4, 5, 6, 7, 8, 9, 10))
    dv_list(ws, f"C{r0}:C{r1}", refs["Services"]); dv_list(ws, f"G{r0}:G{r1}", refs["Unités"]); dv_list(ws, f"H{r0}:H{r1}", refs["Supports"])
    dv_list(ws, f"I{r0}:I{r1}", refs["État"]); dv_list(ws, f"J{r0}:J{r1}", refs["Urgence"])
    dv_int(ws, f"D{r0}:E{r1}", 1800, 2100, "Saisissez une année sur 4 chiffres.")
    ws.conditional_formatting.add(f"I{r0}:I{r1}", CellIsRule(operator="equal", formula=['"Critique"'], fill=fill(BORL), font=Font(color=BORD, bold=True)))
    ws.conditional_formatting.add(f"I{r0}:I{r1}", CellIsRule(operator="equal", formula=['"Dégradé"'], fill=fill(ORL), font=Font(color="B65A1F", bold=True)))
    ws.conditional_formatting.add(f"J{r0}:J{r1}", CellIsRule(operator="equal", formula=['"Immédiate"'], fill=fill(ORANGE), font=Font(color=WHITE, bold=True)))
    ws.conditional_formatting.add(f"D{r0}:E{r1}", FormulaRule(formula=[f'AND(ISNUMBER($D{r0}),ISNUMBER($E{r0}),$E{r0}<$D{r0})'], fill=fill(BORL)))
    for cell, t, f_ in (("J5", "Total ml", f'=SUMIF(G{r0}:G{r1},"ml",F{r0}:F{r1})'), ("J6", "Total boîtes", f'=SUMIF(G{r0}:G{r1},"boîtes",F{r0}:F{r1})'),
                        ("J7", "Total Go", f'=SUMIF(G{r0}:G{r1},"Go",F{r0}:F{r1})'), ("A7", "Lots inventoriés", f'=COUNTA(B{r0}:B{r1})'),
                        ("F7", "Lots en état critique", f'=COUNTIF(I{r0}:I{r1},"Critique")')):
        t_ = label(ws, cell, t); t_.value = f_; t_.fill = fill(MOUTL)
    ws.freeze_panes = "C10"
    print_setup(ws, title_rows="9:9")
    footer_note(ws, r1 + 3, len(H))
    def ex(e):
        e["B5"] = "Organisation Horizon (cas fictif)"; e["G5"] = "Sous-sol, ancien magasin"; e["B6"] = dt.date(2026, 3, 2); e["G6"] = "Esther, référente archives"
        rows = [("Cartons « Projets 2019-2021 »", "PRG", 2019, 2021, 1.2, "ml", "Papier", "Critique", "Immédiate", "Moisissures visibles sur 3 boîtes : isoler"),
                ("Classeurs factures fournisseurs", "FIN", 2018, 2022, 3.4, "ml", "Papier", "Moyen", "À surveiller", "Humidité 72 à 80 % relevée"),
                ("Boîtes dossiers du personnel sortis", "RHU", 2015, 2023, 14, "boîtes", "Papier", "Bon", "Aucune", "Accès non fermé à clé"),
                ("Disque partagé « COMMUN »", "DIR", 2017, 2026, 186, "Go", "Numérique", "Moyen", "À surveiller", "Doublons nombreux, pas de nommage"),
                ("Armoire contrats et conventions", "DIR", 2016, 2026, 0.8, "ml", "Papier", "Bon", "Aucune", "Originaux mêlés aux copies"),
                ("Photos d'événements (clés USB)", "COM", 2019, 2025, 42, "Go", "Numérique", "Dégradé", "Immédiate", "Une clé illisible : copier les autres")]
        for i, row in enumerate(rows):
            for j, v in enumerate(row, 2):
                e.cell(10 + i, j, v)
    copy_as_example(wb, "Inventaire", ex)
    finish(wb, "Annexe_A_Fiche_d_inventaire_des_archives", "Inventaire")

# ======================================================================= B
PLAN = [("01", "Gouvernance et direction", "DIR", "Statuts, PV, plans stratégiques"),
        ("01.01", "Statuts et textes fondateurs", "DIR", "Statuts, règlement intérieur"), ("01.02", "Assemblée générale", "DIR", "Convocations, PV, rapports"),
        ("01.03", "Conseil d'administration", "DIR", "Ordres du jour, PV"), ("01.04", "Stratégie et planification", "DIR", "Plans stratégiques, plans annuels"),
        ("01.05", "Correspondance de direction", "DIR", "Courriers signés par la direction"),
        ("02", "Finances et comptabilité", "FIN", "Budgets, comptabilité, audits"),
        ("02.01", "Budgets", "FIN", "Budgets prévisionnels, révisions"), ("02.02", "Comptabilité générale", "FIN", "Journaux, grand livre, états financiers"),
        ("02.03", "Factures fournisseurs", "FIN", "Factures, avoirs"), ("02.04", "Recettes et dons", "FIN", "Reçus, attestations de dons"),
        ("02.05", "Banque et trésorerie", "FIN", "Relevés, rapprochements"), ("02.06", "Fiscalité", "FIN", "Déclarations"), ("02.07", "Audits et contrôles", "FIN", "Rapports d'audit"),
        ("03", "Ressources humaines", "RHU", "Recrutement, dossiers, paie"),
        ("03.01", "Recrutement", "RHU", "Offres, candidatures retenues"), ("03.02", "Dossiers individuels", "RHU", "Contrats, avenants, attestations"),
        ("03.03", "Paie et déclarations sociales", "RHU", "Bulletins, déclarations"), ("03.04", "Formation", "RHU", "Plans, attestations"),
        ("03.05", "Relations sociales, santé et sécurité", "RHU", "Registres, PV"),
        ("04", "Programmes et projets", "PRG", "Conception, exécution, évaluation"),
        ("04.01", "Conception et montage", "PRG", "Notes conceptuelles, cadres logiques"), ("04.02", "Dossiers de projets", "PRG", "Un dossier par projet"),
        ("04.03", "Suivi-évaluation", "PRG", "Indicateurs, rapports d'évaluation"), ("04.04", "Bénéficiaires", "PRG", "Inscriptions, listes de présence"),
        ("05", "Partenariats et financements", "COM", "Conventions, rapports aux bailleurs"),
        ("05.01", "Conventions de financement", "DIR", "Conventions, avenants"), ("05.02", "Rapports aux bailleurs", "PRG", "Rapports narratifs et financiers"),
        ("05.03", "Partenariats opérationnels", "COM", "Conventions de partenariat"),
        ("06", "Logistique, achats et patrimoine", "LOG", "Achats, contrats, biens"),
        ("06.01", "Achats", "LOG", "Devis, bons de commande"), ("06.02", "Contrats et baux", "LOG", "Contrats de services, baux"),
        ("06.03", "Inventaire des biens", "LOG", "Fiches de biens, véhicules"), ("06.04", "Assurances", "LOG", "Polices, sinistres"),
        ("07", "Communication", "COM", "Publications, presse, images"),
        ("07.01", "Publications", "COM", "Rapports annuels, brochures"), ("07.02", "Presse et réseaux sociaux", "COM", "Communiqués, revues de presse"),
        ("07.03", "Photothèque et vidéothèque", "COM", "Photos décrites, autorisations"), ("07.04", "Événements", "COM", "Programmes, listes")]

def annexe_B():
    wb = Workbook()
    guide_sheet(wb, "B", "Modèle de plan de classement",
                "Structurer l'ensemble des documents de l'organisation par fonctions et activités, avec une codification décimale commune au papier et au numérique.",
                ["Remplacez ou complétez les rubriques proposées par celles de votre organisation (le modèle est prérempli avec un plan type d'ASBL).",
                 "Saisissez le code au format 01 (fonction), 01.01 (activité) ou 01.01.01 (sous-activité) : le niveau se calcule seul.",
                 "Indiquez le service qui détient l'exemplaire principal et la confidentialité par défaut.",
                 "Un code en double ou mal formé est signalé en bordeaux dans la colonne Contrôle.",
                 "Faites valider le plan par la direction, puis reportez-le à l'identique dans l'arborescence numérique."],
                "La facture d'un traiteur pour un atelier du projet Cap Emploi est classée en 02.03 (Factures fournisseurs), avec le code du projet en métadonnée ; la liste de présence de l'atelier est classée en 04.02, dans le dossier du projet.",
                ["Organisez par fonctions et non par services : les fonctions survivent aux réorganisations.", "Trois ou quatre niveaux au maximum.",
                 "Ne réutilisez jamais un code supprimé ; gardez des réserves (08, 09…).", "Proscrivez les rubriques « Divers »."])
    refs = lists_sheet(wb, {"Services": SERVICES, "Confidentialité": CONF})
    ws = wb.create_sheet("Plan de classement", 1)
    H = ["Code", "Niveau", "Intitulé de la rubrique", "Service (exemplaire principal)", "Exemples de documents", "Confidentialité par défaut", "Observations", "Contrôle"]
    W = [10, 8, 40, 16, 44, 18, 28, 20]
    banner(ws, "Modèle de plan de classement", "Plan fonctionnel codifié. Prérempli avec le plan type de l'Organisation Horizon : adaptez-le.", len(H), "B")
    label(ws, "A5", "Organisation", merge_to=3); label(ws, "D5", "Version / date", merge_to=5); label(ws, "F5", "Validé par", merge_to=7)
    header_row(ws, 7, H, W)
    r0, r1 = 8, 207
    for r in range(r0, r1 + 1):
        ws.cell(r, 2, f'=IF(A{r}="","",LEN(A{r})-LEN(SUBSTITUTE(A{r},".",""))+1)')
        ws.cell(r, 8, f'=IF(A{r}="","",IF(COUNTIF($A${r0}:$A${r1},A{r})>1,"Code en double",IF(MOD(LEN(A{r})+1,3)<>0,"Format à vérifier","OK")))')
    body(ws, r0, r1, len(H), formula_cols=(2, 8), center_cols=(1, 2, 4, 6, 8), zebra=False)
    for r in range(r0, r1 + 1):
        ws.cell(r, 1).number_format = "@"
    for i, (code, lib, svc, ex) in enumerate(PLAN):
        r = r0 + i
        ws.cell(r, 1, code); ws.cell(r, 3, lib); ws.cell(r, 4, svc); ws.cell(r, 5, ex)
        ws.cell(r, 6, "Confidentiel" if code.startswith("03") or code in ("04.04", "02.07") else "Interne")
    dv_list(ws, f"D{r0}:D{r1}", refs["Services"]); dv_list(ws, f"F{r0}:F{r1}", refs["Confidentialité"])
    ws.conditional_formatting.add(f"A{r0}:G{r1}", FormulaRule(formula=[f'$B{r0}=1'], fill=fill(NAVY2), font=Font(color=WHITE, bold=True)))
    ws.conditional_formatting.add(f"A{r0}:G{r1}", FormulaRule(formula=[f'$B{r0}=3'], fill=fill(PASTL), font=Font(italic=True, color=NAVY)))
    ws.conditional_formatting.add(f"H{r0}:H{r1}", FormulaRule(formula=[f'AND($H{r0}<>"",$H{r0}<>"OK")'], fill=fill(BORL), font=Font(color=BORD, bold=True)))
    ws.conditional_formatting.add(f"C{r0}:C{r1}", FormulaRule(formula=[f'$B{r0}=2'], font=Font(color=NAVY)))
    ws.freeze_panes = "A8"
    print_setup(ws, title_rows="7:7")
    footer_note(ws, r1 + 2, len(H))
    def ex(e):
        e["B5"] = "Organisation Horizon (cas fictif)"; e["E5"] = "v1.0 · mars 2026"; e["G5"] = "Mireille, directrice exécutive"
        r = r0 + len(PLAN)
        for code, lib, svc, exm in [("04.02.01", "Projet Cap Emploi 2025-2027", "PRG", "Conception, exécution, rapports"), ("04.02.02", "Projet Ateliers numériques", "PRG", "Dossier complet du projet")]:
            e.cell(r, 1, code); e.cell(r, 3, lib); e.cell(r, 4, svc); e.cell(r, 5, exm); e.cell(r, 6, "Interne"); r += 1
        e.cell(r0 + 1, 7, "Originaux signés uniquement")
    copy_as_example(wb, "Plan de classement", ex)
    finish(wb, "Annexe_B_Modele_de_plan_de_classement", "Plan de classement")

# ======================================================================= C
def annexe_C():
    wb = Workbook()
    guide_sheet(wb, "C", "Registre de suivi documentaire",
                "Décrire, localiser et suivre chaque dossier jusqu'à son sort final : c'est le répertoire, l'index et l'outil d'alerte de vos archives.",
                ["Une ligne par dossier (ou par boîte). Saisissez la cote au format HOR/02.03/2026/0157, adaptée à votre organisation.",
                 "Choisissez rubrique, service, support, confidentialité, sort final et statut dans les menus déroulants (onglet Listes modifiable).",
                 "Saisissez l'année de fin du dossier et la DUA en années : l'année d'échéance se calcule seule.",
                 "La colonne Alerte signale les dossiers dont l'échéance est atteinte (à proposer à l'élimination ou au versement) et ceux qui sont gelés.",
                 "Utilisez les filtres de la ligne d'en-tête pour retrouver un dossier par mot-clé, rubrique ou période."],
                "HOR/05.01/2022/003 · Convention Fondation Alizé, projet Cap Emploi · 2022-2025 · DIR · Mixte · convention ; avenant ; Alizé · Confidentiel · A-05-1-001 · sort C · En place.",
                ["Une cote ne se réutilise jamais : les doublons s'affichent en bordeaux.", "Séparez la cote (identité) de la localisation (emplacement).",
                 "Les durées des exemples sont fictives : appliquez votre tableau de gestion validé.", "Un dossier « Gelé » (litige, audit, enquête) ne doit jamais être éliminé."])
    plan_codes = [c for c, *_ in PLAN if "." in c]
    refs = lists_sheet(wb, {"Rubriques": plan_codes, "Services": SERVICES, "Supports": ["Papier", "Numérique", "Mixte"], "Confidentialité": CONF,
                            "Sort final": SORT, "Statut": ["En place", "Prêté", "Versé", "Gelé", "Éliminé"]})
    ws = wb.create_sheet("Registre", 1)
    H = ["Cote", "Rubrique", "Intitulé", "Année début", "Année fin", "Service", "Support", "Mots-clés", "Confidentialité", "Localisation", "DUA (années)", "Sort final", "Échéance", "Statut", "Alerte", "Observations"]
    W = [21, 9, 36, 8, 8, 9, 10, 26, 15, 12, 8, 7, 9, 10, 20, 26]
    banner(ws, "Registre de suivi documentaire", "Répertoire des dossiers avec localisation, durée d'utilité administrative, sort final et alertes automatiques.", len(H), "C")
    label(ws, "A5", "Organisation", merge_to=3); label(ws, "F5", "Mis à jour le", merge_to=8)
    ws["G5"].value = "=TODAY()"; ws["G5"].number_format = "dd/mm/yyyy"; ws["G5"].fill = fill(MOUTL)
    label(ws, "J5", "Dossiers décrits", merge_to=11); ws["K5"].value = "=COUNTA(A8:A1007)"; ws["K5"].fill = fill(MOUTL)
    label(ws, "M5", "Échéances", merge_to=15); ws["N5"].value = '=COUNTIF(O8:O1007,"Échéance atteinte*")'; ws["N5"].fill = fill(MOUTL)
    header_row(ws, 7, H, W)
    r0, r1 = 8, 1007
    for r in range(r0, r1 + 1):
        ws.cell(r, 13, f'=IF(AND(ISNUMBER(E{r}),ISNUMBER(K{r})),E{r}+K{r},"")')
        ws.cell(r, 15, f'=IF(A{r}="","",IF(N{r}="Gelé","Gelé : ne pas éliminer",IF(OR(N{r}="Éliminé",N{r}="Versé"),"",IF(AND(ISNUMBER(M{r}),M{r}<=YEAR(TODAY())),"Échéance atteinte ("&L{r}&")",""))))')
    body(ws, r0, r1, len(H), formula_cols=(13, 15), center_cols=(2, 4, 5, 6, 7, 9, 11, 12, 13, 14), wrap=False)
    dv_list(ws, f"B{r0}:B{r1}", refs["Rubriques"]); dv_list(ws, f"F{r0}:F{r1}", refs["Services"]); dv_list(ws, f"G{r0}:G{r1}", refs["Supports"])
    dv_list(ws, f"I{r0}:I{r1}", refs["Confidentialité"]); dv_list(ws, f"L{r0}:L{r1}", refs["Sort final"]); dv_list(ws, f"N{r0}:N{r1}", refs["Statut"])
    dv_int(ws, f"D{r0}:E{r1}", 1800, 2100, "Saisissez une année sur 4 chiffres."); dv_int(ws, f"K{r0}:K{r1}", 0, 200, "DUA en années (0 à 200).")
    ws.conditional_formatting.add(f"A{r0}:A{r1}", FormulaRule(formula=[f'AND($A{r0}<>"",COUNTIF($A${r0}:$A${r1},$A{r0})>1)'], fill=fill(BORL), font=Font(color=BORD, bold=True)))
    ws.conditional_formatting.add(f"O{r0}:O{r1}", FormulaRule(formula=[f'LEFT($O{r0},8)="Échéance"'], fill=fill(ORL), font=Font(color="B65A1F", bold=True)))
    ws.conditional_formatting.add(f"O{r0}:O{r1}", FormulaRule(formula=[f'LEFT($O{r0},4)="Gelé"'], fill=fill(BORD), font=Font(color=WHITE, bold=True)))
    ws.conditional_formatting.add(f"I{r0}:I{r1}", FormulaRule(formula=[f'LEFT($I{r0},7)="Confide"'], font=Font(color=BORD, bold=True)))
    ws.conditional_formatting.add(f"I{r0}:I{r1}", FormulaRule(formula=[f'LEFT($I{r0},7)="Stricte"'], font=Font(color=BORD, bold=True)))
    ws.auto_filter.ref = f"A7:P{r1}"
    ws.freeze_panes = "B8"
    print_setup(ws, title_rows="7:7")
    footer_note(ws, r1 + 2, len(H))
    def ex(e):
        e["B5"] = "Organisation Horizon (cas fictif)"
        rows = [("HOR/01.02/2024/001", "01.02", "AG ordinaire 2024, dossier complet", 2024, 2024, "DIR", "Papier", "assemblée générale ; comptes ; élection", "Interne", "A-01-1-002", None, "C", "En place"),
                ("HOR/02.03/2014/0001", "02.03", "Factures fournisseurs, exercice 2014", 2014, 2014, "FIN", "Papier", "facture ; fournisseur", "Interne", "A-02-1-003", 10, "D", "En place"),
                ("HOR/02.07/2023/002", "02.07", "Audit externe des comptes 2022", 2023, 2023, "FIN", "Mixte", "audit ; commissaire ; rapport", "Confidentiel", "A-02-4-031", 10, "C", "Prêté"),
                ("HOR/03.02/2019/014", "03.02", "Dossier individuel, MUKENDI Paul", 2019, 2024, "RHU", "Papier", "contrat ; départ ; formateur", "Confidentiel", "B-01-2-008", 5, "T", "Gelé"),
                ("HOR/05.01/2022/003", "05.01", "Convention Fondation Alizé, projet Cap Emploi", 2022, 2025, "DIR", "Mixte", "convention ; avenant ; Alizé", "Confidentiel", "A-05-1-001", None, "C", "En place"),
                ("HOR/06.02/2021/004", "06.02", "Contrat Delta Transports", 2021, 2024, "LOG", "Papier", "transport ; véhicule ; antenne Est", "Interne", "A-03-1-012", 5, "D", "En place")]
        for i, row in enumerate(rows):
            for j, v in enumerate(row, 1):
                e.cell(r0 + i, j if j < 13 else j + 1, v)
        e.cell(r0, 16, "Durées fictives : à fixer selon le tableau de gestion validé"); e.cell(r0 + 3, 16, "Litige en cours : destruction suspendue")
    copy_as_example(wb, "Registre", ex)
    finish(wb, "Annexe_C_Registre_de_suivi_documentaire", "Registre")

# ======================================================================= D
def annexe_D():
    wb = Workbook()
    guide_sheet(wb, "D", "Fiche de prêt et de consultation",
                "Tracer chaque sortie ou consultation d'un dossier : qui, quoi, quand, avec quelle autorisation, et quand il revient.",
                ["Onglet Fiche : imprimez une fiche par prêt et placez-en un exemplaire à l'emplacement du dossier sorti.",
                 "Onglet Registre des prêts : saisissez chaque prêt sur une ligne ; la date de retour prévue se calcule à partir de la durée.",
                 "Le statut (En cours, Rendu, En retard) et le nombre de jours de retard se calculent automatiquement.",
                 "Pour un dossier confidentiel, l'autorisation est obligatoire : son absence est signalée.",
                 "Examinez chaque mois les prêts en retard (filtre sur la colonne Statut)."],
                "Le dossier HOR/02.07/2023/002 (audit des comptes 2022) est prêté au trésorier le 12/03 pour 5 jours ; la fiche reste à l'emplacement A-02-4-031 jusqu'au retour.",
                ["Pas de prêt d'original confidentiel hors du bâtiment : préférez une consultation sur place ou une copie.", "Contrôlez au retour que le dossier est complet.",
                 "La fiche de prêt ne remplace jamais le dossier : elle signale son absence."])
    refs = lists_sheet(wb, {"Type": ["Prêt (sortie du local)", "Consultation sur place", "Copie remise"], "Confidentialité": CONF,
                            "Services": SERVICES + ["Externe"], "Complet au retour": ["Oui", "Non"]})
    # --- fiche imprimable
    f = wb.create_sheet("Fiche", 1)
    for c, w in zip("ABCD", (30, 34, 22, 30)):
        f.column_dimensions[c].width = w
    banner(f, "Fiche de prêt et de consultation", "À imprimer et à placer à l'emplacement du dossier sorti pendant toute la durée du prêt.", 4, "D")
    rows = ["N° de fiche", "Type", "Cote et intitulé du dossier", "Niveau de confidentialité", "Demandeur (nom, fonction, service)", "Motif de la demande",
            "Autorisation (si confidentiel) : nom, date, signature", "Date de sortie", "Date de retour prévue", "Signature du demandeur",
            "Date de retour effectif", "Dossier complet au retour ?", "Observations", "Visa de l'archiviste au retour"]
    for i, t in enumerate(rows):
        r = 5 + i
        c = f.cell(r, 1, t); c.font = Font(name=FONT, bold=True, size=10, color=WHITE); c.fill = fill(NAVY2 if i % 2 == 0 else NAVY)
        c.alignment = Alignment(wrap_text=True, vertical="center", indent=1); c.border = BOX
        f.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
        for cc in range(2, 5):
            f.cell(r, cc).border = BOX; f.cell(r, cc).fill = fill(PASTL)
        f.row_dimensions[r].height = 30
    dv_list(f, "B6", refs["Type"]); dv_list(f, "B8", refs["Confidentialité"]); dv_list(f, "B16", refs["Complet au retour"])
    for r in (12, 13, 15):
        f.cell(r, 2).number_format = "dd/mm/yyyy"
    f.conditional_formatting.add("B8", FormulaRule(formula=['OR(LEFT($B$8,7)="Confide",LEFT($B$8,7)="Stricte")'], fill=fill(BORL), font=Font(color=BORD, bold=True)))
    print_setup(f, landscape=False)
    footer_note(f, 21, 4)
    # --- registre des prêts
    ws = wb.create_sheet("Registre des prêts", 2)
    H = ["N° fiche", "Type", "Cote", "Intitulé du dossier", "Confidentialité", "Demandeur", "Service", "Autorisation (nom)", "Date de sortie", "Durée (jours)", "Retour prévu", "Retour effectif", "Complet ?", "Statut", "Jours de retard", "Contrôle"]
    W = [8, 18, 20, 30, 15, 18, 9, 18, 11, 8, 11, 11, 8, 11, 9, 24]
    banner(ws, "Registre des prêts et consultations", "Une ligne par prêt. Statut, retard et contrôles se calculent seuls.", len(H), "D")
    label(ws, "A5", "Prêts en cours", merge_to=2); ws["B5"].value = '=COUNTIF(N8:N507,"En cours")+COUNTIF(N8:N507,"En retard")'; ws["B5"].fill = fill(MOUTL)
    label(ws, "D5", "Dont en retard"); ws["E5"].value = '=COUNTIF(N8:N507,"En retard")'; ws["E5"].fill = fill(MOUTL)
    header_row(ws, 7, H, W)
    r0, r1 = 8, 507
    for r in range(r0, r1 + 1):
        ws.cell(r, 11, f'=IF(AND(ISNUMBER(I{r}),ISNUMBER(J{r})),I{r}+J{r},"")')
        ws.cell(r, 14, f'=IF(C{r}="","",IF(ISNUMBER(L{r}),"Rendu",IF(AND(ISNUMBER(K{r}),TODAY()>K{r}),"En retard","En cours")))')
        ws.cell(r, 15, f'=IF(N{r}="En retard",TODAY()-K{r},"")')
        ws.cell(r, 16, f'=IF(C{r}="","",IF(AND(OR(LEFT(E{r},7)="Confide",LEFT(E{r},7)="Stricte"),H{r}=""),"Autorisation manquante",IF(M{r}="Non","Dossier incomplet au retour","OK")))')
        for c in (9, 11, 12):
            ws.cell(r, c).number_format = "dd/mm/yyyy"
    body(ws, r0, r1, len(H), formula_cols=(11, 14, 15, 16), center_cols=(1, 5, 7, 9, 10, 11, 12, 13, 14, 15), wrap=False)
    dv_list(ws, f"B{r0}:B{r1}", refs["Type"]); dv_list(ws, f"E{r0}:E{r1}", refs["Confidentialité"]); dv_list(ws, f"G{r0}:G{r1}", refs["Services"])
    dv_list(ws, f"M{r0}:M{r1}", refs["Complet au retour"]); dv_date(ws, f"I{r0}:I{r1}"); dv_date(ws, f"L{r0}:L{r1}"); dv_int(ws, f"J{r0}:J{r1}", 0, 365, "Durée en jours.")
    ws.conditional_formatting.add(f"N{r0}:N{r1}", CellIsRule(operator="equal", formula=['"En retard"'], fill=fill(ORANGE), font=Font(color=WHITE, bold=True)))
    ws.conditional_formatting.add(f"N{r0}:N{r1}", CellIsRule(operator="equal", formula=['"Rendu"'], font=Font(color=NAVY2)))
    ws.conditional_formatting.add(f"P{r0}:P{r1}", FormulaRule(formula=[f'AND($P{r0}<>"",$P{r0}<>"OK")'], fill=fill(BORL), font=Font(color=BORD, bold=True)))
    ws.auto_filter.ref = f"A7:P{r1}"; ws.freeze_panes = "D8"
    print_setup(ws, title_rows="7:7")
    footer_note(ws, r1 + 2, len(H))
    def ex(e):
        today = dt.date.today()
        rows = [(1, "Prêt (sortie du local)", "HOR/02.07/2023/002", "Audit externe des comptes 2022", "Confidentiel", "Trésorier (CA)", "DIR", "Mireille", today - dt.timedelta(days=12), 5, None, None),
                (2, "Consultation sur place", "HOR/05.01/2022/003", "Convention Fondation Alizé", "Confidentiel", "Auditeur du bailleur", "Externe", "Mireille", today - dt.timedelta(days=6), 1, today - dt.timedelta(days=6), "Oui"),
                (3, "Prêt (sortie du local)", "HOR/06.02/2021/004", "Contrat Delta Transports", "Interne", "Samuel", "PRG", None, today - dt.timedelta(days=2), 10, None, None),
                (4, "Prêt (sortie du local)", "HOR/03.02/2019/014", "Dossier individuel, MUKENDI Paul", "Confidentiel", "Avocat de l'ASBL", "Externe", None, today - dt.timedelta(days=3), 7, None, None)]
        for i, row in enumerate(rows):
            vals = list(row)
            e.cell(r0 + i, 1, vals[0]); e.cell(r0 + i, 2, vals[1]); e.cell(r0 + i, 3, vals[2]); e.cell(r0 + i, 4, vals[3]); e.cell(r0 + i, 5, vals[4])
            e.cell(r0 + i, 6, vals[5]); e.cell(r0 + i, 7, vals[6]); e.cell(r0 + i, 8, vals[7]); e.cell(r0 + i, 9, vals[8]); e.cell(r0 + i, 10, vals[9])
            e.cell(r0 + i, 12, vals[10]); e.cell(r0 + i, 13, vals[11])
    copy_as_example(wb, "Registre des prêts", ex)
    finish(wb, "Annexe_D_Fiche_de_pret_et_de_consultation", "Fiche")

# ======================================================================= E
def annexe_E():
    wb = Workbook()
    guide_sheet(wb, "E", "Tableau de gestion et de conservation",
                "Fixer, pour chaque série de documents, la durée d'utilité administrative (DUA), son point de départ, le sort final et le fondement de la règle.",
                ["Une ligne par série documentaire, en suivant votre plan de classement.",
                 "Renseignez l'exemplaire principal, le point de départ (clôture de l'exercice, fin du contrat, départ du salarié…) et la DUA.",
                 "Choisissez le sort final : C (conservation), D (destruction), T (tri) ; pour T, décrivez les modalités de tri.",
                 "Renseignez toujours le fondement (texte de loi, clause contractuelle ou décision interne) : la colonne Contrôle signale les manques.",
                 "Faites valider le tableau par la direction et un juriste ou un expert-comptable, puis datez la version."],
                "02.03 · Factures fournisseurs · FIN · clôture de l'exercice · 10 ans · D · fondement : droit comptable national et convention avec la Fondation Alizé (durées fictives à valider).",
                ["Aucune durée n'est universelle : vérifiez les textes de votre pays et vos engagements contractuels.", "Quand plusieurs valeurs coexistent, retenez la durée la plus longue.",
                 "Une durée sans point de départ est inapplicable.", "Révisez le tableau chaque année et après tout changement de loi."])
    plan_codes = [c for c, *_ in PLAN]
    refs = lists_sheet(wb, {"Rubriques": plan_codes, "Services": SERVICES, "Sort final": SORT,
                            "Point de départ": ["Date du document", "Clôture de l'exercice", "Fin du contrat", "Départ du salarié", "Clôture du projet", "Fin de la convention", "Date de la réunion", "Publication"],
                            "Type de fondement": ["Texte légal ou réglementaire", "Clause contractuelle", "Exigence du bailleur", "Décision interne", "Avis archivistique"]})
    ws = wb.create_sheet("Tableau de gestion", 1)
    H = ["Rubrique", "Série documentaire", "Exemplaire principal", "Point de départ", "DUA (années)", "DUA illimitée ?", "Sort final", "Modalités de tri (si T)", "Type de fondement", "Référence précise du fondement", "Observations", "Contrôle"]
    W = [15, 32, 11, 18, 8, 9, 8, 26, 20, 34, 26, 24]
    banner(ws, "Tableau de gestion et de conservation", "Référentiel des durées de conservation. Chaque durée doit avoir un fondement écrit.", len(H), "E")
    label(ws, "A5", "Organisation", merge_to=3); label(ws, "D5", "Version", merge_to=5); label(ws, "G5", "Validé par (direction)", merge_to=9); label(ws, "J5", "Date de validation")
    ws["K5"].number_format = "dd/mm/yyyy"
    label(ws, "A6", "Juriste / expert-comptable", merge_to=3); label(ws, "D6", "Séries décrites", merge_to=5); ws["E6"].value = '=COUNTA(B9:B308)'; ws["E6"].fill = fill(MOUTL)
    label(ws, "G6", "Lignes à compléter", merge_to=9); ws["H6"].value = '=COUNTIF(L9:L308,"<>OK")-COUNTBLANK(L9:L308)'; ws["H6"].fill = fill(MOUTL)
    header_row(ws, 8, H, W)
    r0, r1 = 9, 308
    for r in range(r0, r1 + 1):
        ws.cell(r, 12, f'=IF(B{r}="","",IF(I{r}&J{r}="","Fondement manquant",IF(D{r}="","Point de départ manquant",IF(AND(E{r}="",F{r}<>"Oui"),"DUA manquante",IF(G{r}="","Sort final manquant",IF(AND(G{r}="T",H{r}=""),"Modalités de tri manquantes","OK"))))))')
    body(ws, r0, r1, len(H), formula_cols=(12,), center_cols=(1, 3, 5, 6, 7))
    dv_list(ws, f"A{r0}:A{r1}", refs["Rubriques"]); dv_list(ws, f"C{r0}:C{r1}", refs["Services"]); dv_list(ws, f"D{r0}:D{r1}", refs["Point de départ"])
    dv_list(ws, f"G{r0}:G{r1}", refs["Sort final"]); dv_list(ws, f"I{r0}:I{r1}", refs["Type de fondement"]); dv_list(ws, f"F{r0}:F{r1}", '"Oui,Non"')
    dv_int(ws, f"E{r0}:E{r1}", 0, 200, "DUA en années.")
    ws.conditional_formatting.add(f"L{r0}:L{r1}", FormulaRule(formula=[f'AND($L{r0}<>"",$L{r0}<>"OK")'], fill=fill(ORL), font=Font(color="B65A1F", bold=True)))
    ws.conditional_formatting.add(f"G{r0}:G{r1}", CellIsRule(operator="equal", formula=['"C"'], fill=fill(NAVY2), font=Font(color=WHITE, bold=True)))
    ws.conditional_formatting.add(f"G{r0}:G{r1}", CellIsRule(operator="equal", formula=['"T"'], fill=fill(MOUT), font=Font(color=NAVY, bold=True)))
    ws.conditional_formatting.add(f"G{r0}:G{r1}", CellIsRule(operator="equal", formula=['"D"'], fill=fill(BORD), font=Font(color=WHITE, bold=True)))
    ws.auto_filter.ref = f"A8:L{r1}"; ws.freeze_panes = "C9"
    print_setup(ws, title_rows="8:8")
    footer_note(ws, r1 + 2, len(H))
    def ex(e):
        e["B5"] = "Organisation Horizon (cas fictif)"; e["E5"] = "v1.2"; e["H5"] = "Mireille"; e["K5"] = dt.date(2026, 6, 15); e["B6"] = "Cabinet comptable et avocat (fictifs)"
        rows = [("01.02", "PV et dossiers d'AG", "DIR", "Date de la réunion", None, "Oui", "C", None, "Décision interne", "Archives définitives : mémoire de la gouvernance"),
                ("02.03", "Factures fournisseurs", "FIN", "Clôture de l'exercice", 10, "Non", "D", None, "Texte légal ou réglementaire", "Droit comptable national, à préciser (durée fictive)"),
                ("02.05", "Relevés bancaires", "FIN", "Clôture de l'exercice", 10, "Non", "D", None, "Texte légal ou réglementaire", "À préciser (durée fictive)"),
                ("03.02", "Dossiers individuels du personnel", "RHU", "Départ du salarié", 5, "Non", "T", "Conserver contrat, attestations et éléments utiles aux droits à pension", "Texte légal ou réglementaire", "Droit social national, à préciser (durée fictive)"),
                ("04.02", "Dossiers de projets", "PRG", "Clôture du projet", 10, "Non", "T", "Conserver rapports finaux et photos significatives", "Exigence du bailleur", "Convention Fondation Alizé, clause d'audit"),
                ("05.01", "Conventions de financement", "DIR", "Fin de la convention", None, "Oui", "C", None, "Clause contractuelle", "Conventions signées avec les bailleurs"),
                ("06.01", "Devis non retenus", "LOG", "Date du document", 2, "Non", "D", None, "", "")]
        for i, row in enumerate(rows):
            for j, v in enumerate(row, 1):
                e.cell(r0 + i, j, v)
        e.cell(r0 + 6, 11, "Exemple volontairement incomplet : voir la colonne Contrôle")
    copy_as_example(wb, "Tableau de gestion", ex)
    finish(wb, "Annexe_E_Tableau_de_gestion_et_de_conservation", "Tableau de gestion")

# ======================================================================= F
def annexe_F():
    wb = Workbook()
    guide_sheet(wb, "F", "Bordereau de versement",
                "Décrire les documents transférés par un service vers le local ou le service d'archives, et acter le transfert de responsabilité.",
                ["Le service versant remplit l'en-tête (numéro de versement, service, date) et une ligne par boîte.",
                 "Pour chaque boîte : cote, intitulé des dossiers, années extrêmes, DUA, sort final et confidentialité ; l'échéance se calcule seule.",
                 "Le nombre de boîtes et le volume (0,10 ml par boîte standard, modifiable) se calculent automatiquement.",
                 "L'archiviste contrôle la conformité, saisit la localisation attribuée, puis les deux parties signent le bloc de signatures.",
                 "Imprimez en deux exemplaires : un pour le service, un pour les archives."],
                "Versement annuel du service FIN en février 2027 : 14 boîtes, pièces de l'exercice 2025, cotes HOR/02.03/2025/0001 à 0014, localisées A-02-3-046 à 059.",
                ["Triez avant de verser : retirez doubles, brouillons et documents sans valeur.", "Une boîte contenant des documents confidentiels se scelle et se signale.",
                 "Le bordereau est conservé aussi longtemps que les documents qu'il décrit."])
    refs = lists_sheet(wb, {"Services": SERVICES, "Sort final": SORT, "Confidentialité": CONF, "Conformité": ["Conforme", "Conforme avec réserves", "Non conforme"]})
    ws = wb.create_sheet("Bordereau", 1)
    H = ["N° de boîte", "Cote", "Intitulé des dossiers contenus", "Année début", "Année fin", "DUA (années)", "Sort final", "Échéance", "Confidentialité", "Localisation (archiviste)"]
    W = [8, 22, 46, 9, 9, 9, 8, 10, 16, 18]
    banner(ws, "Bordereau de versement", "À remplir par le service versant ; la localisation et le contrôle sont complétés par l'archiviste.", len(H), "F")
    label(ws, "A5", "N° de versement", merge_to=2); label(ws, "C5", "Service versant").alignment = Alignment(horizontal="left")
    label(ws, "E5", "Date du versement", merge_to=7); ws["F5"].number_format = "dd/mm/yyyy"; label(ws, "H5", "Volume par boîte (ml)", merge_to=9); ws["I5"].value = 0.10
    label(ws, "A6", "Nombre de boîtes", merge_to=2); ws["B6"].value = "=COUNTA(B9:B48)"; ws["B6"].fill = fill(MOUTL)
    label(ws, "C6", "Volume total (ml)"); ws["D6"].value = "=B6*I5"; ws["D6"].fill = fill(MOUTL); ws["D6"].number_format = "0.00"
    label(ws, "E6", "Boîtes confidentielles", merge_to=7); ws["F6"].value = '=COUNTIF(I9:I48,"Confidentiel")+COUNTIF(I9:I48,"Strictement confidentiel")'; ws["F6"].fill = fill(MOUTL)
    dv_list(ws, "D5", refs["Services"])
    header_row(ws, 8, H, W)
    r0, r1 = 9, 48
    for r in range(r0, r1 + 1):
        ws.cell(r, 8, f'=IF(AND(ISNUMBER(E{r}),ISNUMBER(F{r})),E{r}+F{r},"")')
    body(ws, r0, r1, len(H), formula_cols=(8,), center_cols=(1, 4, 5, 6, 7, 8, 9, 10))
    dv_list(ws, f"G{r0}:G{r1}", refs["Sort final"]); dv_list(ws, f"I{r0}:I{r1}", refs["Confidentialité"]); dv_int(ws, f"D{r0}:E{r1}", 1800, 2100, "Année sur 4 chiffres.")
    ws.conditional_formatting.add(f"I{r0}:I{r1}", FormulaRule(formula=[f'OR(LEFT($I{r0},7)="Confide",LEFT($I{r0},7)="Stricte")'], fill=fill(BORL), font=Font(color=BORD, bold=True)))
    ws.conditional_formatting.add(f"B{r0}:B{r1}", FormulaRule(formula=[f'AND($B{r0}<>"",COUNTIF($B${r0}:$B${r1},$B{r0})>1)'], fill=fill(BORL), font=Font(color=BORD, bold=True)))
    # bloc signatures
    s = r1 + 2
    for col, title in ((1, "LE CHEF DU SERVICE VERSANT"), (6, "L'ARCHIVISTE (PRISE EN CHARGE)")):
        ws.merge_cells(start_row=s, start_column=col, end_row=s, end_column=col + 3 if col == 1 else 10)
        c = ws.cell(s, col, title); c.font = Font(name=FONT, bold=True, color=WHITE); c.fill = fill(NAVY); c.alignment = Alignment(indent=1)
        for k, t in enumerate(["Nom :", "Date :", "Signature :"] + (["Contrôle de conformité :", "Réserves :"] if col == 6 else []), 1):
            c = ws.cell(s + k, col, t); c.font = Font(name=FONT, bold=True, color=OCRE)
            ws.merge_cells(start_row=s + k, start_column=col + 1, end_row=s + k, end_column=col + 3 if col == 1 else 10)
            ws.cell(s + k, col + 1).fill = fill(PASTL); ws.cell(s + k, col + 1).border = BOX
            ws.row_dimensions[s + k].height = 22
    dv_list(ws, f"G{s+4}", refs["Conformité"])
    ws.freeze_panes = "C9"
    print_setup(ws, title_rows="8:8")
    footer_note(ws, s + 7, len(H))
    def ex(e):
        e["B5"] = "V-2027-003"; e["D5"] = "FIN"; e["F5"] = dt.date(2027, 2, 15)
        for i in range(6):
            e.cell(r0 + i, 1, i + 1); e.cell(r0 + i, 2, f"HOR/02.03/2025/{i+1:04d}")
            e.cell(r0 + i, 3, f"Factures fournisseurs 2025, {['janvier-février','mars-avril','mai-juin','juillet-août','septembre-octobre','novembre-décembre'][i]}")
            e.cell(r0 + i, 4, 2025); e.cell(r0 + i, 5, 2025); e.cell(r0 + i, 6, 10); e.cell(r0 + i, 7, "D"); e.cell(r0 + i, 9, "Interne"); e.cell(r0 + i, 10, f"A-02-3-{46+i:03d}")
        e.cell(r0 + 6, 1, 7); e.cell(r0 + 6, 2, "HOR/02.07/2025/001"); e.cell(r0 + 6, 3, "Rapport d'audit des comptes 2024"); e.cell(r0 + 6, 4, 2025); e.cell(r0 + 6, 5, 2025)
        e.cell(r0 + 6, 6, 10); e.cell(r0 + 6, 7, "C"); e.cell(r0 + 6, 9, "Confidentiel"); e.cell(r0 + 6, 10, "A-02-4-032")
        e.cell(r1 + 3, 2, "Jonas, RAF"); e.cell(r1 + 3, 7, "Esther, référente archives"); e.cell(r1 + 6, 7, "Conforme")
    copy_as_example(wb, "Bordereau", ex)
    finish(wb, "Annexe_F_Bordereau_de_versement", "Bordereau")

# ======================================================================= G
def annexe_G():
    wb = Workbook()
    guide_sheet(wb, "G", "Procès-verbal de destruction",
                "Prouver qu'une élimination a été autorisée et réalisée conformément au tableau de gestion, sans suspension en cours.",
                ["Listez les dossiers proposés à l'élimination (extraits du registre de suivi : alerte « Échéance atteinte »).",
                 "Pour chaque ligne, vérifiez l'absence de suspension (litige, audit, enquête) et indiquez la référence du tableau de gestion.",
                 "Toute ligne marquée « Suspension : Oui » s'affiche en bordeaux « NE PAS DÉTRUIRE » et doit être retirée du lot.",
                 "Choisissez le mode de destruction ; le volume total se calcule seul.",
                 "Recueillez les visas (service producteur, archives, direction, autorité d'archives si la loi l'exige), puis conservez le PV et le certificat du prestataire."],
                "PV n° 2027-01 : élimination des factures fournisseurs 2014 à 2016 (DUA fictive de 10 ans échue), 3 ml, broyage par prestataire avec certificat n° 4471 ; le dossier RH gelé pour litige est exclu.",
                ["Ne détruisez jamais un document visé par un litige, un audit ou une enquête, même si sa DUA est échue.", "Le PV et le certificat se conservent durablement.",
                 "Pour les archives publiques, vérifiez si l'autorisation préalable de l'administration des archives est requise."])
    refs = lists_sheet(wb, {"Suspension": ["Non", "Oui"], "Mode de destruction": ["Broyage interne", "Prestataire certifié", "Effacement sécurisé", "Destruction physique du support"], "Unités": ["ml", "Go", "boîtes"]})
    ws = wb.create_sheet("Procès-verbal", 1)
    H = ["Cote", "Intitulé", "Année début", "Année fin", "Volume", "Unité", "Référence du tableau de gestion", "Suspension (litige, audit, enquête) ?", "Contrôle"]
    W = [22, 40, 9, 9, 8, 8, 22, 16, 20]
    banner(ws, "Procès-verbal de destruction", "Les documents décrits ont une DUA échue selon le tableau de gestion et ne font l'objet d'aucune suspension.", len(H), "G")
    label(ws, "A5", "PV n°"); label(ws, "C5", "Tableau de gestion (version)", merge_to=4); label(ws, "F5", "Date de destruction", merge_to=7); ws["G5"].number_format = "dd/mm/yyyy"
    label(ws, "A6", "Mode de destruction"); dv_list(ws, "B6", refs["Mode de destruction"]); label(ws, "C6", "Prestataire et n° de certificat", merge_to=7)
    label(ws, "A7", "Lieu"); label(ws, "C7", "Volume total (ml)", merge_to=4); ws["D7"].value = '=SUMIF(F10:F49,"ml",E10:E49)'; ws["D7"].fill = fill(MOUTL)
    label(ws, "F7", "Lignes bloquées", merge_to=7); ws["G7"].value = '=COUNTIF(H10:H49,"Oui")'; ws["G7"].fill = fill(MOUTL)
    header_row(ws, 9, H, W)
    r0, r1 = 10, 49
    for r in range(r0, r1 + 1):
        ws.cell(r, 9, f'=IF(A{r}="","",IF(H{r}="Oui","NE PAS DÉTRUIRE",IF(H{r}="","Vérifier la suspension",IF(G{r}="","Référence manquante","Éliminable"))))')
    body(ws, r0, r1, len(H), formula_cols=(9,), center_cols=(3, 4, 5, 6, 8, 9))
    dv_list(ws, f"H{r0}:H{r1}", refs["Suspension"]); dv_list(ws, f"F{r0}:F{r1}", refs["Unités"])
    ws.conditional_formatting.add(f"A{r0}:I{r1}", FormulaRule(formula=[f'$H{r0}="Oui"'], fill=fill(BORL), font=Font(color=BORD, bold=True)))
    ws.conditional_formatting.add(f"I{r0}:I{r1}", CellIsRule(operator="equal", formula=['"NE PAS DÉTRUIRE"'], fill=fill(BORD), font=Font(color=WHITE, bold=True)))
    ws.conditional_formatting.add(f"I{r0}:I{r1}", FormulaRule(formula=[f'OR($I{r0}="Vérifier la suspension",$I{r0}="Référence manquante")'], fill=fill(ORL), font=Font(color="B65A1F", bold=True)))
    s = r1 + 2
    roles = ["Service producteur", "Responsable des archives", "Direction (autorisation)", "Autorité d'archives (si requise)"]
    for i, t in enumerate(roles):
        col = 1 + i * 2 if i < 3 else 7
        c = ws.cell(s, col, t); c.font = Font(name=FONT, bold=True, color=WHITE); c.fill = fill(NAVY2 if i % 2 else NAVY); c.alignment = Alignment(wrap_text=True, indent=1)
        for k, lab in enumerate(["Nom :", "Date :", "Visa :"], 1):
            cc = ws.cell(s + k, col, lab); cc.font = Font(name=FONT, bold=True, color=OCRE)
            ws.cell(s + k, col + 1).fill = fill(PASTL); ws.cell(s + k, col + 1).border = BOX
    ws.row_dimensions[s].height = 30
    ws.cell(s + 5, 1, "Ce procès-verbal et le certificat du prestataire sont conservés durablement.").font = Font(name=FONT, italic=True, color=NAVY)
    ws.freeze_panes = "B10"
    print_setup(ws, title_rows="9:9")
    footer_note(ws, s + 7, len(H))
    def ex(e):
        e["B5"] = "2027-01"; e["D5"] = "v1.2 du 15/06/2026"; e["G5"] = dt.date(2027, 3, 4); e["B6"] = "Prestataire certifié"; e["D6"] = "Société fictive, certificat n° 4471"; e["B7"] = "Locaux du prestataire"
        rows = [("HOR/02.03/2014/0001", "Factures fournisseurs, exercice 2014", 2014, 2014, 1, "ml", "02.03 · DUA 10 ans · D", "Non"),
                ("HOR/02.03/2015/0001", "Factures fournisseurs, exercice 2015", 2015, 2015, 1, "ml", "02.03 · DUA 10 ans · D", "Non"),
                ("HOR/02.03/2016/0001", "Factures fournisseurs, exercice 2016", 2016, 2016, 1, "ml", "02.03 · DUA 10 ans · D", "Non"),
                ("HOR/03.02/2019/014", "Dossier individuel, MUKENDI Paul", 2019, 2024, 0.05, "ml", "03.02 · DUA 5 ans · T", "Oui"),
                ("HOR/06.01/2022/011", "Devis non retenus 2022", 2022, 2022, 0.1, "ml", "", "")]
        for i, row in enumerate(rows):
            for j, v in enumerate(row, 1):
                e.cell(r0 + i, j, v)
    copy_as_example(wb, "Procès-verbal", ex)
    finish(wb, "Annexe_G_Proces_verbal_de_destruction", "Procès-verbal")

# ======================================================================= H
DIAG = [("Organisation", "Existe-t-il une politique, un responsable désigné, des correspondants ?"),
        ("Classement", "Existe-t-il un plan de classement commun ? Est-il appliqué au numérique ?"),
        ("Instruments de recherche", "Les dossiers sont-ils cotés, décrits, localisés ? Quel est le délai moyen de recherche ?"),
        ("Conservation", "Local adapté ? Climat mesuré ? Matériel ? Plan d'urgence ?"),
        ("Durées et élimination", "Tableau de gestion ? Versements ? PV de destruction ? Suspensions gérées ?"),
        ("Numérique", "Arborescence, nommage, formats, sauvegardes testées, comptes personnels ?"),
        ("Sécurité", "Classification, droits d'accès revus, prêts tracés, incidents enregistrés ?"),
        ("Conformité", "Textes applicables identifiés ? Exigences des bailleurs ? Données personnelles ?")]

def annexe_H():
    wb = Workbook()
    guide_sheet(wb, "H", "Fiche de diagnostic archivistique",
                "Établir un état des lieux structuré en huit domaines, mesurer les risques et hiérarchiser les recommandations.",
                ["Renseignez l'en-tête (organisation, date, services rencontrés, volumes papier et numériques).",
                 "Pour chaque domaine, notez vos constats factuels et attribuez un niveau de risque de 1 (faible) à 5 (critique).",
                 "La priorité se calcule seule (Haute à partir de 4, Moyenne à 3) et le graphique se met à jour.",
                 "Rédigez une recommandation concrète par domaine, avec un responsable et une échéance.",
                 "Le score global et le nombre de priorités hautes alimentent le rapport de diagnostic (chapitre 10)."],
                "Horizon, mars 2026 : conservation 5 (local humide, moisissures), classement 5 (aucun plan), numérique 4 (fichiers sur 15 postes) ; score global 4,1 sur 5 ; trois priorités hautes traitées dans les 30 premiers jours.",
                ["Distinguez le symptôme (dossier perdu) de la cause (absence de fiche de prêt).", "Appuyez chaque constat sur une preuve : photo, relevé, entretien, document.",
                 "Refaites le diagnostic chaque année pour mesurer les progrès."])
    refs = lists_sheet(wb, {"Niveau de risque": [1, 2, 3, 4, 5], "Services": SERVICES})
    ws = wb.create_sheet("Diagnostic", 1)
    H = ["Domaine", "Questions clés", "Constats (faits observés)", "Niveau de risque (1 à 5)", "Priorité", "Recommandation", "Responsable", "Échéance"]
    W = [20, 40, 44, 11, 11, 44, 14, 12]
    banner(ws, "Fiche de diagnostic archivistique", "Huit domaines, un niveau de risque de 1 (faible) à 5 (critique), des recommandations hiérarchisées.", len(H), "H")
    label(ws, "A5", "Organisation", merge_to=3); label(ws, "D5", "Date", merge_to=5); ws["E5"].number_format = "dd/mm/yyyy"; label(ws, "F5", "Réalisé par", merge_to=8)
    label(ws, "A6", "Volume papier (ml)"); label(ws, "C6", "Volume numérique (Go)").alignment = Alignment(horizontal="left"); label(ws, "F6", "Services rencontrés", merge_to=8)
    header_row(ws, 8, H, W)
    r0 = 9; r1 = r0 + len(DIAG) - 1
    for i, (d, q) in enumerate(DIAG):
        r = r0 + i
        ws.cell(r, 1, d); ws.cell(r, 2, q)
        ws.cell(r, 5, f'=IF(D{r}="","",IF(D{r}>=4,"Haute",IF(D{r}=3,"Moyenne","Basse")))')
        ws.row_dimensions[r].height = 48
    body(ws, r0, r1, len(H), formula_cols=(5,), center_cols=(4, 5, 7, 8))
    for r in range(r0, r1 + 1):
        ws.cell(r, 1).font = Font(name=FONT, bold=True, color=NAVY); ws.cell(r, 8).number_format = "dd/mm/yyyy"
    dv_int(ws, f"D{r0}:D{r1}", 1, 5, "Niveau de risque de 1 (faible) à 5 (critique).")
    ws.conditional_formatting.add(f"D{r0}:D{r1}", DataBarRule(start_type="num", start_value=0, end_type="num", end_value=5, color=ORANGE))
    ws.conditional_formatting.add(f"E{r0}:E{r1}", CellIsRule(operator="equal", formula=['"Haute"'], fill=fill(BORD), font=Font(color=WHITE, bold=True)))
    ws.conditional_formatting.add(f"E{r0}:E{r1}", CellIsRule(operator="equal", formula=['"Moyenne"'], fill=fill(MOUT), font=Font(color=NAVY, bold=True)))
    ws.conditional_formatting.add(f"E{r0}:E{r1}", CellIsRule(operator="equal", formula=['"Basse"'], fill=fill(PAST), font=Font(color=NAVY)))
    s = r1 + 2
    for k, (t, f_) in enumerate([("Score global (moyenne sur 5)", f'=IF(COUNT(D{r0}:D{r1})=0,"",ROUND(AVERAGE(D{r0}:D{r1}),1))'),
                                 ("Priorités hautes", f'=COUNTIF(E{r0}:E{r1},"Haute")'), ("Domaines évalués", f'=COUNT(D{r0}:D{r1})&" / {len(DIAG)}"')]):
        label(ws, f"A{s+k}", t, merge_to=3); ws.cell(s + k, 4, f_).fill = fill(MOUTL); ws.cell(s + k, 4).font = Font(name=FONT, bold=True, size=12, color=NAVY)
        ws.cell(s + k, 4).alignment = Alignment(horizontal="center"); ws.cell(s + k, 4).number_format = "0.0" if k == 0 else "General"
        ws.cell(s + k, 2).value = None
    for k in range(3):
        ws.unmerge_cells(start_row=s + k, start_column=2, end_row=s + k, end_column=3)
        ws.merge_cells(start_row=s + k, start_column=1, end_row=s + k, end_column=3)
    ch = BarChart(); ch.type = "bar"; ch.style = 10; ch.title = "Niveau de risque par domaine"; ch.y_axis.scaling.min = 0; ch.y_axis.scaling.max = 5
    ch.add_data(Reference(ws, min_col=4, min_row=8, max_row=r1), titles_from_data=True); ch.set_categories(Reference(ws, min_col=1, min_row=r0, max_row=r1))
    ch.legend = None; ch.height = 7.2; ch.width = 17
    ch.series[0].graphicalProperties.solidFill = ORANGE; ch.series[0].graphicalProperties.line.solidFill = ORANGE
    ws.add_chart(ch, f"F{s}")
    ws.freeze_panes = "B9"
    print_setup(ws, title_rows="8:8"); ws.page_setup.fitToHeight = 1
    footer_note(ws, s + 18, len(H))
    def ex(e):
        e["B5"] = "Organisation Horizon (cas fictif)"; e["E5"] = dt.date(2026, 3, 9); e["G5"] = "Esther et Jonas"; e["B6"] = 38; e["D6"] = 410; e["G6"] = "DIR, FIN, RHU, PRG, LOG, COM"
        data = [(4, "Aucune politique ; personne n'est désigné.", "Désigner une référente archives ; rédiger une politique d'une page.", "Mireille"),
                (5, "Aucun plan de classement ; dossiers « Divers » partout.", "Construire un plan fonctionnel en 7 fonctions.", "Esther"),
                (4, "Ni cotes ni répertoire ; recherches de plusieurs heures.", "Registre de suivi Excel, cotation HOR.", "Esther"),
                (5, "Sous-sol à 72-80 % d'humidité ; moisissures sur 10 boîtes.", "Déménager au 1er étage ; traiter les boîtes moisies.", "Jonas"),
                (3, "Pas de tableau de gestion ; destructions au cas par cas.", "Tableau de gestion validé par les conseils.", "Jonas"),
                (4, "Fichiers sur 15 postes et 3 comptes personnels.", "Espace unique, nommage, sauvegardes 3-2-1.", "Jonas"),
                (4, "Dossiers RH dans une armoire ouverte ; prêts non tracés.", "Armoire fermée, fiches de prêt, matrice des accès.", "Grâce"),
                (3, "Exigences des bailleurs connues mais non formalisées.", "Recenser les obligations contractuelles.", "Samuel")]
        for i, (n, c, rec, resp) in enumerate(data):
            r = r0 + i
            e.cell(r, 3, c); e.cell(r, 4, n); e.cell(r, 6, rec); e.cell(r, 7, resp); e.cell(r, 8, dt.date(2026, 4 + (i % 3), 30))
    copy_as_example(wb, "Diagnostic", ex)
    # le graphique n'est pas recopié par copy_worksheet : on l'ajoute à l'exemple
    ex = wb["Exemple Horizon"]
    ch2 = BarChart(); ch2.type = "bar"; ch2.style = 10; ch2.title = "Niveau de risque par domaine"; ch2.y_axis.scaling.min = 0; ch2.y_axis.scaling.max = 5
    ch2.add_data(Reference(ex, min_col=4, min_row=8, max_row=r1), titles_from_data=True); ch2.set_categories(Reference(ex, min_col=1, min_row=r0, max_row=r1))
    ch2.legend = None; ch2.height = 7.2; ch2.width = 17
    ch2.series[0].graphicalProperties.solidFill = ORANGE; ch2.series[0].graphicalProperties.line.solidFill = ORANGE
    ex.add_chart(ch2, f"F{s}"); ex.page_setup.fitToHeight = 1
    finish(wb, "Annexe_H_Fiche_de_diagnostic_archivistique", "Diagnostic")

# ======================================================================= I
POLICY = [("1. Objet", "La présente politique fixe les principes et les règles de gestion des documents produits et reçus par [l'organisation], afin de garantir leur valeur de preuve, leur sécurité, leur accessibilité et le respect des obligations légales et contractuelles."),
          ("2. Champ d'application", "Elle s'applique à tous les documents, quels que soient leur forme et leur support, à tous les services, sites, salariés, bénévoles et prestataires."),
          ("3. Principes", "Respect des fonds ; gestion dès la création ; documents de l'organisation conservés exclusivement sur ses supports et espaces ; conservation selon le tableau de gestion ; aucune destruction hors procédure ; protection des données personnelles ; traçabilité."),
          ("4. Rôles et responsabilités", "Direction ; responsable des archives ; chefs de service ; correspondants ; collaborateurs ; informatique (voir l'onglet Rôles)."),
          ("5. Référentiels", "Plan de classement ; tableau de gestion ; grille de classification ; convention de nommage ; matrice des accès."),
          ("6. Règles opérationnelles", "Enregistrement du courrier ; constitution des dossiers ; versements annuels ; prêts et consultations ; élimination avec PV ; suspension en cas de litige, d'audit ou d'enquête ; numérisation ; sauvegardes."),
          ("7. Usage de l'intelligence artificielle", "Outils autorisés ; données interdites ; validation humaine proportionnée à l'enjeu ; traçabilité de l'usage."),
          ("8. Contrôle et révision", "Indicateurs trimestriels ; récolement annuel par sondage ; revue annuelle de la politique présentée à la direction."),
          ("9. Entrée en vigueur", "La politique entre en vigueur le [date] et s'impose à tous.")]
ROLES = ["Direction", "Responsable des archives", "Chefs de service", "Correspondants archives", "Collaborateurs", "Informatique"]
ACTS = ["Approuver la politique et le tableau de gestion", "Tenir le plan de classement à jour", "Classer les documents courants", "Préparer les versements annuels",
        "Prendre en charge et localiser les versements", "Autoriser les éliminations", "Réaliser les éliminations et le PV", "Gérer les droits d'accès numériques",
        "Former le personnel", "Signaler et traiter les incidents", "Réaliser la revue annuelle"]
RACI_DEFAULT = [["A", "R", "C", "I", "I", "I"], ["A", "R", "C", "C", "I", ""], ["", "C", "A", "R", "R", ""], ["", "C", "A", "R", "I", ""],
                ["I", "A", "C", "R", "", ""], ["A", "R", "C", "", "", ""], ["A", "R", "C", "", "", ""], ["A", "C", "C", "", "", "R"],
                ["I", "A", "C", "R", "I", "C"], ["I", "A", "R", "R", "R", "R"], ["A", "R", "C", "C", "", "C"]]

def annexe_I():
    wb = Workbook()
    guide_sheet(wb, "I", "Modèle de politique d'archivage",
                "Rédiger, suivre et faire approuver la politique d'archivage, et répartir clairement les responsabilités (matrice RACI).",
                ["Onglet Politique : adaptez le texte de chaque section dans la colonne « Texte » (les mentions entre crochets sont à remplacer).",
                 "Désignez un rédacteur par section et suivez l'avancement : l'avancement global se calcule seul.",
                 "Onglet Rôles (RACI) : pour chaque activité, indiquez qui Réalise (R), qui est Approbateur et responsable final (A), qui est Consulté (C), qui est Informé (I).",
                 "La colonne Contrôle vérifie qu'il y a exactement un A et au moins un R par activité.",
                 "Une fois toutes les sections validées, copiez le texte dans un document à en-tête de l'organisation et faites-le approuver."],
                "Horizon : neuf sections rédigées par Esther et Jonas, relues par l'avocat, adoptées par le conseil d'administration au mois 12 ; matrice RACI annexée.",
                ["Une politique courte, claire et appliquée vaut mieux qu'un long document ignoré.", "Faites approuver au plus haut niveau (direction ou conseil d'administration).",
                 "Un seul « A » par activité : c'est la règle d'or d'une matrice RACI."])
    refs = lists_sheet(wb, {"Statut": ["À rédiger", "En cours", "Relu", "Validé"], "RACI": ["R", "A", "C", "I"]})
    ws = wb.create_sheet("Politique", 1)
    H = ["Section", "Texte (à adapter)", "Rédacteur", "Statut", "Date de validation"]
    W = [26, 90, 16, 12, 14]
    banner(ws, "Modèle de politique d'archivage", "Texte modèle à adapter, avec suivi de rédaction et de validation.", len(H), "I")
    label(ws, "A5", "Organisation"); label(ws, "C5", "Version", merge_to=4)
    label(ws, "A6", "Approuvée par"); label(ws, "C6", "Date d'approbation", merge_to=4); ws["D6"].number_format = "dd/mm/yyyy"
    label(ws, "A7", "Avancement"); ws["B7"].value = '=COUNTIF(D10:D18,"Validé")/9'; ws["B7"].number_format = "0%"; ws["B7"].fill = fill(MOUTL)
    header_row(ws, 9, H, W)
    r0 = 10; r1 = r0 + len(POLICY) - 1
    for i, (sec, txt) in enumerate(POLICY):
        r = r0 + i
        ws.cell(r, 1, sec); ws.cell(r, 2, txt); ws.cell(r, 4, "À rédiger")
        ws.row_dimensions[r].height = 62
    body(ws, r0, r1, len(H), center_cols=(3, 4, 5))
    for r in range(r0, r1 + 1):
        ws.cell(r, 1).font = Font(name=FONT, bold=True, color=NAVY); ws.cell(r, 5).number_format = "dd/mm/yyyy"
    dv_list(ws, f"D{r0}:D{r1}", refs["Statut"]); dv_date(ws, f"E{r0}:E{r1}")
    ws.conditional_formatting.add(f"B7", DataBarRule(start_type="num", start_value=0, end_type="num", end_value=1, color=MOUT))
    for val, bg, fg in (("Validé", NAVY2, WHITE), ("Relu", PAST, NAVY), ("En cours", MOUTL, OCRE), ("À rédiger", ORL, "B65A1F")):
        ws.conditional_formatting.add(f"D{r0}:D{r1}", CellIsRule(operator="equal", formula=[f'"{val}"'], fill=fill(bg), font=Font(color=fg, bold=True)))
    ws.conditional_formatting.add(f"B{r0}:B{r1}", FormulaRule(formula=[f'ISNUMBER(SEARCH("[",$B{r0}))'], font=Font(color="B65A1F")))
    print_setup(ws, landscape=False, title_rows="9:9")
    footer_note(ws, r1 + 2, len(H))
    # --- RACI
    rw = wb.create_sheet("Rôles (RACI)", 2)
    Hr = ["Activité"] + ROLES + ["Contrôle"]
    banner(rw, "Matrice des responsabilités (RACI)", "R = réalise · A = approuve et répond du résultat · C = consulté · I = informé. Un seul A par activité.", len(Hr), "I")
    header_row(rw, 5, Hr, [40] + [14] * len(ROLES) + [24])
    for i, a in enumerate(ACTS):
        r = 6 + i
        rw.cell(r, 1, a)
        for j, v in enumerate(RACI_DEFAULT[i], 2):
            rw.cell(r, j, v or None)
        last = L(1 + len(ROLES))
        rw.cell(r, 2 + len(ROLES), f'=IF(COUNTIF(B{r}:{last}{r},"A")<>1,"Un seul A requis",IF(COUNTIF(B{r}:{last}{r},"R")<1,"Au moins un R requis","OK"))')
        rw.row_dimensions[r].height = 22
    rr1 = 6 + len(ACTS) - 1
    body(rw, 6, rr1, len(Hr), formula_cols=(len(Hr),), center_cols=tuple(range(2, len(Hr) + 1)))
    dv_list(rw, f"B6:{L(1+len(ROLES))}{rr1}", refs["RACI"])
    rng = f"B6:{L(1+len(ROLES))}{rr1}"
    for val, bg, fg in (("A", BORD, WHITE), ("R", NAVY2, WHITE), ("C", MOUT, NAVY), ("I", PAST, NAVY)):
        rw.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=[f'"{val}"'], fill=fill(bg), font=Font(color=fg, bold=True)))
    cl = L(len(Hr))
    rw.conditional_formatting.add(f"{cl}6:{cl}{rr1}", FormulaRule(formula=[f'${cl}6<>"OK"'], fill=fill(ORL), font=Font(color="B65A1F", bold=True)))
    rw.freeze_panes = "B6"; rw.sheet_properties.tabColor = BORD
    print_setup(rw, title_rows="5:5")
    footer_note(rw, rr1 + 2, len(Hr))
    def ex(e):
        e["B5"] = "Organisation Horizon (cas fictif)"; e["D5"] = "v1.0"; e["B6"] = "Conseil d'administration"; e["D6"] = dt.date(2026, 12, 10)
        e.cell(r0, 2, POLICY[0][1].replace("[l'organisation]", "l'Organisation Horizon")); e.cell(r1, 2, POLICY[-1][1].replace("[date]", "1er janvier 2027"))
        for i in range(len(POLICY)):
            e.cell(r0 + i, 3, "Esther" if i % 2 == 0 else "Jonas"); e.cell(r0 + i, 4, "Validé" if i < 7 else "Relu")
            if i < 7: e.cell(r0 + i, 5, dt.date(2026, 11, 20))
    copy_as_example(wb, "Politique", ex)
    finish(wb, "Annexe_I_Modele_de_politique_d_archivage", "Politique")

# ======================================================================= J
CHECK = ["Une politique d'archivage approuvée existe et a été revue depuis moins d'un an.",
         "Un responsable des archives et des correspondants sont formellement désignés.",
         "Le plan de classement est appliqué au papier et au numérique.",
         "Le tableau de gestion est validé et chaque durée a un fondement écrit.",
         "Tout courrier entrant est enregistré au registre d'arrivée.",
         "Les prêts sont tracés ; aucun prêt en retard de plus de 30 jours.",
         "Le local est fermé, l'accès limité, le climat relevé chaque semaine.",
         "Les documents sont classifiés ; les droits d'accès ont été revus depuis moins d'un an.",
         "Les accès des personnes parties ont été désactivés à leur départ.",
         "Chaque élimination fait l'objet d'un PV signé ; aucune suspension n'a été ignorée.",
         "Les sauvegardes respectent la règle 3-2-1 et une restauration a été testée.",
         "Aucun document de l'organisation n'est stocké sur un compte personnel.",
         "Un récolement par sondage a été réalisé dans l'année, les écarts traités.",
         "La piste d'audit d'un échantillon d'opérations est complète.",
         "Les incidents sont enregistrés, analysés et suivis d'actions correctives.",
         "L'usage de l'IA est encadré par des règles écrites et une validation humaine."]
DOMAINS = ["Gouvernance", "Gouvernance", "Classement", "Conservation et élimination", "Traçabilité", "Traçabilité", "Conservation et élimination", "Sécurité",
           "Sécurité", "Conservation et élimination", "Numérique", "Numérique", "Contrôle", "Contrôle", "Contrôle", "Numérique"]

def annexe_J():
    wb = Workbook()
    guide_sheet(wb, "J", "Checklist de contrôle interne des archives",
                "Évaluer chaque année, point par point, la maîtrise des archives et suivre les actions correctives.",
                ["Pour chacun des 16 points, choisissez Oui, Non ou Sans objet, et indiquez la preuve examinée.",
                 "Un « Non » appelle une action corrective : décrivez-la, nommez un responsable et fixez une échéance.",
                 "Le taux de conformité global (hors « Sans objet ») et le taux par domaine se calculent seuls.",
                 "Les actions dont l'échéance est dépassée s'affichent en orange.",
                 "Archivez la checklist remplie : elle constitue elle-même une preuve de contrôle pour l'auditeur."],
                "Horizon, 2026 : 14 points sur 16 conformes (88 %) ; les points 9 (accès non désactivés) et 12 (comptes personnels) font l'objet d'un plan d'action confié à Jonas.",
                ["Un « Oui » sans preuve vaut un « Non ».", "Faites remplir la checklist par une personne et revoir par une autre (séparation des tâches).",
                 "Comparez d'une année sur l'autre pour suivre la tendance."])
    refs = lists_sheet(wb, {"Réponse": ["Oui", "Non", "Sans objet"], "Responsables": ["Direction", "Responsable des archives", "RAF", "RH", "Informatique", "Chef de service"]})
    ws = wb.create_sheet("Checklist", 1)
    H = ["N°", "Domaine", "Point de contrôle", "Réponse", "Preuve examinée", "Action corrective", "Responsable", "Échéance", "Suivi"]
    W = [5, 18, 56, 11, 28, 32, 16, 11, 16]
    banner(ws, "Checklist de contrôle interne des archives", "16 points de contrôle, taux de conformité automatique et suivi des actions correctives.", len(H), "J")
    label(ws, "A5", "Organisation", merge_to=3); label(ws, "D5", "Date du contrôle", merge_to=5); ws["E5"].number_format = "dd/mm/yyyy"
    label(ws, "F5", "Contrôlé par", merge_to=6); label(ws, "H5", "Revu par", merge_to=9)
    header_row(ws, 8, H, W)
    r0 = 9; r1 = r0 + len(CHECK) - 1
    for i, (pt, dom) in enumerate(zip(CHECK, DOMAINS)):
        r = r0 + i
        ws.cell(r, 1, i + 1); ws.cell(r, 2, dom); ws.cell(r, 3, pt)
        ws.cell(r, 9, f'=IF(D{r}="","À évaluer",IF(D{r}="Oui","Conforme",IF(D{r}="Sans objet","",IF(F{r}="","Action à définir",IF(AND(ISNUMBER(H{r}),H{r}<TODAY()),"Échéance dépassée","Action en cours")))))')
        ws.cell(r, 8).number_format = "dd/mm/yyyy"
        ws.row_dimensions[r].height = 30
    body(ws, r0, r1, len(H), formula_cols=(9,), center_cols=(1, 4, 7, 8, 9))
    dv_list(ws, f"D{r0}:D{r1}", refs["Réponse"]); dv_list(ws, f"G{r0}:G{r1}", refs["Responsables"]); dv_date(ws, f"H{r0}:H{r1}")
    ws.conditional_formatting.add(f"D{r0}:D{r1}", CellIsRule(operator="equal", formula=['"Oui"'], fill=fill(NAVY2), font=Font(color=WHITE, bold=True)))
    ws.conditional_formatting.add(f"D{r0}:D{r1}", CellIsRule(operator="equal", formula=['"Non"'], fill=fill(BORD), font=Font(color=WHITE, bold=True)))
    ws.conditional_formatting.add(f"I{r0}:I{r1}", CellIsRule(operator="equal", formula=['"Échéance dépassée"'], fill=fill(ORANGE), font=Font(color=WHITE, bold=True)))
    ws.conditional_formatting.add(f"I{r0}:I{r1}", CellIsRule(operator="equal", formula=['"Action à définir"'], fill=fill(ORL), font=Font(color="B65A1F", bold=True)))
    ws.conditional_formatting.add(f"I{r0}:I{r1}", CellIsRule(operator="equal", formula=['"Conforme"'], font=Font(color=NAVY2, bold=True)))
    # synthèse
    label(ws, "A6", "Taux de conformité", merge_to=3)
    ws["D6"].value = f'=IF(COUNTIF(D{r0}:D{r1},"Oui")+COUNTIF(D{r0}:D{r1},"Non")=0,"",COUNTIF(D{r0}:D{r1},"Oui")/(COUNTIF(D{r0}:D{r1},"Oui")+COUNTIF(D{r0}:D{r1},"Non")))'
    ws["D6"].number_format = "0%"; ws["D6"].fill = fill(MOUTL); ws["D6"].font = Font(name=FONT, bold=True, size=12, color=NAVY)
    ws.conditional_formatting.add("D6", DataBarRule(start_type="num", start_value=0, end_type="num", end_value=1, color=MOUT))
    label(ws, "F6", "Non-conformités", merge_to=6); ws["G6"].value = f'=COUNTIF(D{r0}:D{r1},"Non")'; ws["G6"].fill = fill(MOUTL)
    label(ws, "H6", "Échéances dépassées", merge_to=9); ws["I6"].value = f'=COUNTIF(I{r0}:I{r1},"Échéance dépassée")'; ws["I6"].fill = fill(MOUTL)
    s = r1 + 2
    c = ws.cell(s, 2, "Conformité par domaine"); c.font = Font(name=FONT, bold=True, color=WHITE); c.fill = fill(NAVY)
    ws.cell(s, 3).fill = fill(NAVY)
    for k, d in enumerate(sorted(set(DOMAINS))):
        r = s + 1 + k
        ws.cell(r, 2, d).font = Font(name=FONT, bold=True, color=NAVY)
        ws.cell(r, 3, f'=IF(COUNTIFS($B${r0}:$B${r1},B{r},$D${r0}:$D${r1},"Oui")+COUNTIFS($B${r0}:$B${r1},B{r},$D${r0}:$D${r1},"Non")=0,"",COUNTIFS($B${r0}:$B${r1},B{r},$D${r0}:$D${r1},"Oui")/(COUNTIFS($B${r0}:$B${r1},B{r},$D${r0}:$D${r1},"Oui")+COUNTIFS($B${r0}:$B${r1},B{r},$D${r0}:$D${r1},"Non")))')
        ws.cell(r, 3).number_format = "0%"; ws.cell(r, 3).fill = fill(MOUTL); ws.cell(r, 3).border = BOX; ws.cell(r, 2).border = BOX
    ws.conditional_formatting.add(f"C{s+1}:C{s+len(set(DOMAINS))}", DataBarRule(start_type="num", start_value=0, end_type="num", end_value=1, color=NAVY2))
    ws.freeze_panes = "D9"
    print_setup(ws, title_rows="8:8")
    footer_note(ws, s + len(set(DOMAINS)) + 2, len(H))
    def ex(e):
        e["B5"] = "Organisation Horizon (cas fictif)"; e["E5"] = dt.date(2026, 11, 2); e["G5"] = "Jonas, RAF"; e["I5"] = "Auditeur externe"
        proofs = ["PV du CA du 10/12/2026", "Note de désignation", "Contrôle de 30 dossiers", "Tableau v1.2 signé", "Registre 2026", "Registre des prêts",
                  "Relevés hebdomadaires", "Matrice des accès revue", "", "PV 2026-01 et 2026-02", "Test de restauration du 14/11", "", "Récolement de juin",
                  "5 dépenses de projet", "Registre des incidents", "Politique IA (section 7)"]
        for i in range(len(CHECK)):
            r = r0 + i
            e.cell(r, 4, "Non" if i in (8, 11) else "Oui"); e.cell(r, 5, proofs[i] or None)
        e.cell(r0 + 8, 5, "2 comptes actifs d'anciens salariés"); e.cell(r0 + 8, 6, "Désactiver et intégrer la revue des accès à la procédure de départ"); e.cell(r0 + 8, 7, "Informatique"); e.cell(r0 + 8, 8, dt.date(2026, 11, 15))
        e.cell(r0 + 11, 5, "1 compte de stockage personnel utilisé"); e.cell(r0 + 11, 6, "Rapatrier les fichiers et fermer le compte"); e.cell(r0 + 11, 7, "RAF"); e.cell(r0 + 11, 8, dt.date(2027, 1, 31))
    copy_as_example(wb, "Checklist", ex)
    finish(wb, "Annexe_J_Checklist_de_controle_interne_des_archives", "Checklist")

if __name__ == "__main__":
    for fn in (annexe_A, annexe_B, annexe_C, annexe_D, annexe_E, annexe_F, annexe_G, annexe_H, annexe_I, annexe_J):
        fn()
