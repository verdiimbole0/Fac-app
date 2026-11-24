"""Modèles Excel de LA TRÉSO SOUS CONTRÔLE (formules vivantes, données d'exemple MAKAO, fictives)."""
import sys, os
from datetime import date, timedelta
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(ROOT, "data"))
import fil_rouge as F
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.chart import LineChart, BarChart, Reference
from openpyxl.comments import Comment

NAVY = "0A1E3F"; TEAL = "1B9E8F"; GREY = "F3F5F8"; INPUT = "FFF7D6"
FT = "Arial"
H = Font(name=FT, bold=True, color="FFFFFF", size=10); HF = PatternFill("solid", fgColor=NAVY)
T = Font(name=FT, bold=True, color=NAVY, size=13); N = Font(name=FT, size=10); B = Font(name=FT, size=10, bold=True)
IN = Font(name=FT, size=10, color="0000FF"); INF = PatternFill("solid", fgColor=INPUT)
NOTE = Font(name=FT, size=9, italic=True, color="5B6B82")
thin = Side(style="thin", color="D5DCE6"); BOX = Border(bottom=thin)
NUM = '#,##0;-#,##0;"-"'; NUM2 = '#,##0.00;-#,##0.00;"-"'; PCT = '0.0%;-0.0%;"-"'; DT = 'dd/mm/yyyy'

def title(ws, text, sub):
    ws["A1"] = text; ws["A1"].font = T
    ws["A2"] = sub; ws["A2"].font = NOTE
    ws["A3"] = "Cellules jaunes à texte bleu : saisie. Cellules blanches : formules, ne pas modifier. Données d'exemple : cas fictif MAKAO Distribution."
    ws["A3"].font = NOTE
def header(ws, row, cols, widths=None):
    for i, c in enumerate(cols, 1):
        x = ws.cell(row=row, column=i, value=c); x.font = H; x.fill = HF; x.alignment = Alignment(wrap_text=True, vertical="center")
    if widths:
        for i, w in enumerate(widths, 1): ws.column_dimensions[chr(64+i) if i <= 26 else "A"].width = w
def put(ws, r, c, v, inp=False, fmt=None, bold=False):
    x = ws.cell(row=r, column=c, value=v); x.font = (IN if inp else (B if bold else N)); x.border = BOX
    if inp: x.fill = INF
    if fmt: x.number_format = fmt
    return x

# ---------------- A1 -------------------------------------------------------------
def a1(wb):
    ws = wb.create_sheet("A1_Situation_jour"); title(ws, "A1. Situation journalière de trésorerie", "Disponible prouvé à une date donnée, toutes devises converties en USD.")
    ws["A5"] = "Date de la situation"; put(ws, 5, 2, date(2025, 12, 31), True, DT)
    header(ws, 7, ["Compte", "Devise", "Solde en devise", "Taux (CDF pour 1 USD ; 1 pour USD)", "Solde en USD", "Preuve"], [38, 9, 16, 20, 15, 30])
    rows = [("Banque Alpha, compte USD", "USD", 11400, 1, "Relevé bancaire"), ("Banque Alpha, compte CDF", "CDF", 3420000, 2850, "Relevé bancaire"),
            ("Caisse USD", "USD", 600, 1, "Billetage signé"), ("Caisse CDF", "CDF", 1140000, 2850, "Billetage signé"),
            ("Monnaie électronique", "USD", 1400, 1, "Capture datée du solde"), ("", "", None, None, "")]
    for i, (a, b, c, d, f) in enumerate(rows):
        r = 8 + i; put(ws, r, 1, a, True); put(ws, r, 2, b, True); put(ws, r, 3, c, True, NUM); put(ws, r, 4, d, True, NUM)
        put(ws, r, 5, f'=IF(OR(C{r}="",D{r}=""),0,C{r}/D{r})', fmt=NUM); put(ws, r, 6, f, True)
    put(ws, 14, 1, "Total des disponibilités (USD)", bold=True); put(ws, 14, 5, "=SUM(E8:E13)", fmt=NUM, bold=True)
    put(ws, 16, 1, "Source du taux de change"); put(ws, 16, 2, "Taux pédagogique fictif du livre ; en pratique : taux indicatif de la Banque Centrale du Congo du jour", True)
    return {"A1_Situation_jour!E14": 15000}

# ---------------- A2 -------------------------------------------------------------
def a2(wb):
    ws = wb.create_sheet("A2_Budget_mensuel"); title(ws, "A2. Budget mensuel de trésorerie", "Exemple : budget initial de MAKAO, janvier à juin 2026 (chapitre 3).")
    ms = list(range(1, 7)); header(ws, 5, ["USD"] + [F.MOIS[m] for m in ms] + ["Total"], [38] + [13]*7)
    cats = [c for c in F.DEC_CAT if any(F.M_BASE[m]['dec'].get(c, 0) for m in ms)]
    r_enc0 = 8; r_enctot = r_enc0 + len(F.ENC_CAT); r_dechd = r_enctot + 1; r_dec0 = r_dechd + 1
    r_dectot = r_dec0 + len(cats); r_sol = r_dectot + 1; r_res = r_sol + 1; r_ecart = r_res + 1
    C = lambda j: chr(66 + j)
    put(ws, 6, 1, "Trésorerie d'ouverture (a)", bold=True); put(ws, 6, 2, F.OPENING, True, NUM)
    for j in range(1, 6): put(ws, 6, 2+j, f"={C(j-1)}{r_sol}", fmt=NUM)
    put(ws, 6, 8, "=B6", fmt=NUM); put(ws, 7, 1, "ENCAISSEMENTS", bold=True)
    for i, c in enumerate(F.ENC_CAT):
        r = r_enc0 + i; put(ws, r, 1, c)
        for j, m in enumerate(ms): put(ws, r, 2+j, round(F.M_BASE[m]['enc'].get(c, 0), 2), True, NUM)
        put(ws, r, 8, f"=SUM(B{r}:G{r})", fmt=NUM)
    put(ws, r_enctot, 1, "Total encaissements (b)", bold=True)
    for j in range(7): put(ws, r_enctot, 2+j, f"=SUM({C(j)}{r_enc0}:{C(j)}{r_enctot-1})", fmt=NUM, bold=True)
    put(ws, r_dechd, 1, "DÉCAISSEMENTS", bold=True)
    for i, c in enumerate(cats):
        r = r_dec0 + i; put(ws, r, 1, c)
        for j, m in enumerate(ms): put(ws, r, 2+j, round(F.M_BASE[m]['dec'].get(c, 0), 2), True, NUM)
        put(ws, r, 8, f"=SUM(B{r}:G{r})", fmt=NUM)
    put(ws, r_dectot, 1, "Total décaissements (c)", bold=True)
    for j in range(7): put(ws, r_dectot, 2+j, f"=SUM({C(j)}{r_dec0}:{C(j)}{r_dectot-1})", fmt=NUM, bold=True)
    put(ws, r_sol, 1, "Solde final (a + b - c)", bold=True)
    for j in range(6): put(ws, r_sol, 2+j, f"={C(j)}6+{C(j)}{r_enctot}-{C(j)}{r_dectot}", fmt=NUM, bold=True)
    put(ws, r_sol, 8, f"=G{r_sol}", fmt=NUM, bold=True)
    put(ws, r_res, 1, "Réserve de sécurité visée"); put(ws, r_res, 2, F.RESERVE_CIBLE, True, NUM)
    put(ws, r_ecart, 1, "Écart à la réserve")
    for j in range(6): put(ws, r_ecart, 2+j, f"={C(j)}{r_sol}-$B${r_res}", fmt=NUM)
    ws.conditional_formatting.add(f"B{r_sol}:G{r_ecart}", CellIsRule(operator="lessThan", formula=["0"], font=Font(color="B00020", bold=True)))
    return {f"A2_Budget_mensuel!B{r_sol}": -4750, f"A2_Budget_mensuel!G{r_sol}": 25150, f"A2_Budget_mensuel!D{r_sol}": 4600}

# ---------------- A3 -------------------------------------------------------------
def a3(wb):
    mv = wb.create_sheet("A3_Mouvements"); title(mv, "A3. Prévisionnel 13 semaines : onglet de saisie des mouvements", "Une ligne par mouvement prévu ou réalisé, triée par date (sorties avant entrées le même jour).")
    put(mv, 5, 1, "Trésorerie d'ouverture"); put(mv, 5, 6, F.OPENING, True, NUM)
    header(mv, 6, ["Date", "Sens (E/D)", "Catégorie", "Libellé", "Montant", "Solde cumulé"], [12, 10, 30, 46, 13, 14])
    dv = DataValidation(type="list", formula1='"E,D"', allow_blank=True); mv.add_data_validation(dv)
    evs = [e for e in F.EV_PLAN if e[0] <= date(2026, 4, 5)]
    r = 7
    for d, t, c, l, a in evs:
        put(mv, r, 1, d, True, DT); put(mv, r, 2, t, True); dv.add(mv.cell(row=r, column=2)); put(mv, r, 3, c, True); put(mv, r, 4, l, True)
        put(mv, r, 5, round(a, 2), True, NUM2); put(mv, r, 6, f'=F{r-1 if r > 7 else 5}+IF(B{r}="E",E{r},-E{r})', fmt=NUM2); r += 1
    lastrow = r - 1
    sy = wb.create_sheet("A3_13_semaines"); title(sy, "A3. Prévisionnel glissant sur 13 semaines", "Synthèse calculée à partir de l'onglet A3_Mouvements. Exemple : MAKAO après les décisions des chapitres 4 et 5.")
    header(sy, 5, ["Semaine", "Début", "Fin", "Ouverture", "Entrées", "Sorties", "Clôture", "Point bas", "Alerte"], [9, 12, 12, 13, 13, 13, 13, 13, 16])
    rng = f"$A$7:$A${lastrow}"; amt = f"A3_Mouvements!$E$7:$E${lastrow}"; sens = f"A3_Mouvements!$B$7:$B${lastrow}"; dat = f"A3_Mouvements!$A$7:$A${lastrow}"; sol = f"A3_Mouvements!$F$7:$F${lastrow}"
    for w in range(13):
        r = 6 + w
        put(sy, r, 1, f"S{w+1}"); 
        if w == 0: put(sy, r, 2, F.WEEK1, True, DT)
        else: put(sy, r, 2, f"=B{r-1}+7", fmt=DT)
        put(sy, r, 3, f"=B{r}+6", fmt=DT)
        put(sy, r, 4, "=A3_Mouvements!F5" if w == 0 else f"=G{r-1}", fmt=NUM)
        put(sy, r, 5, f'=SUMIFS({amt},{sens},"E",{dat},">="&B{r},{dat},"<="&C{r})', fmt=NUM)
        put(sy, r, 6, f'=SUMIFS({amt},{sens},"D",{dat},">="&B{r},{dat},"<="&C{r})', fmt=NUM)
        put(sy, r, 7, f"=D{r}+E{r}-F{r}", fmt=NUM)
        put(sy, r, 8, f'=IF(COUNTIFS({dat},">="&B{r},{dat},"<="&C{r})=0,D{r},MIN(D{r},_xlfn.MINIFS({sol},{dat},">="&B{r},{dat},"<="&C{r})))', fmt=NUM)
        put(sy, r, 9, f'=IF(H{r}<0,"DÉFICIT",IF(H{r}<$B$21,"Sous la réserve",""))')
    put(sy, 20, 1, "Point bas des 13 semaines", bold=True); put(sy, 20, 8, "=MIN(H6:H18)", fmt=NUM, bold=True)
    put(sy, 21, 1, "Réserve de sécurité"); put(sy, 21, 2, F.RESERVE_CIBLE, True, NUM)
    sy.conditional_formatting.add("G6:H18", CellIsRule(operator="lessThan", formula=["0"], font=Font(color="B00020", bold=True)))
    ch = LineChart(); ch.title = "Clôture et point bas hebdomadaires"; ch.height = 7; ch.width = 16
    ch.add_data(Reference(sy, min_col=7, min_row=5, max_row=18), titles_from_data=True); ch.add_data(Reference(sy, min_col=8, min_row=5, max_row=18), titles_from_data=True)
    ch.set_categories(Reference(sy, min_col=1, min_row=6, max_row=18)); ch.roundedCorners = False; ch.legend.overlay = False; ch.title.overlay = False
    ch.x_axis.delete = False; ch.y_axis.delete = False; sy.add_chart(ch, "A24")
    exp = {}
    for w, row in enumerate(F.W_PLAN): exp[f"A3_13_semaines!G{6+w}"] = row['cloture']; exp[f"A3_13_semaines!H{6+w}"] = row['plus_bas']
    return exp

# ---------------- A4 -------------------------------------------------------------
def a4(wb):
    ws = wb.create_sheet("A4_Creances"); title(ws, "A4. Suivi des créances clients", "Une ligne par facture. Exemple : créances de MAKAO au 31/12/2025 (total 126 000 USD).")
    put(ws, 4, 10, "Date d'analyse"); put(ws, 4, 11, date(2025, 12, 31), True, DT)
    header(ws, 5, ["Client", "N° facture", "Date facture", "Montant", "Échéance", "Payé", "Reste", "Jours de retard", "Tranche", "Dernière action", "Date promise", "Statut"],
           [28, 14, 12, 11, 12, 10, 11, 10, 11, 22, 12, 12])
    special = {("Groupe scolaire Les Palmiers", 1): ("FA-2025-1187", date(2025, 11, 28), date(2025, 12, 28)),
               ("Clinique Lumière", 0): ("FA-2025-1290", date(2025, 12, 21), date(2026, 1, 20)),
               ("ASBL Espoir Rural", 3): ("FA-2025-0890", date(2025, 9, 15), date(2025, 10, 15)),
               ("Bâtir Kongo (BTP)", 4): ("FA-2025-0951", date(2025, 8, 16), date(2025, 9, 15))}
    due = [date(2026, 1, 20), date(2025, 12, 20), date(2025, 11, 15), date(2025, 10, 15), date(2025, 9, 15)]
    r = 6; k = 1300
    for cl, b in F.CLIENTS.items():
        for i, v in enumerate(b):
            if not v: continue
            num, dfac, ech = special.get((cl, i), (f"FA-2025-{k}", due[i] - timedelta(days=30), due[i])); k += 1
            put(ws, r, 1, cl, True); put(ws, r, 2, num, True); put(ws, r, 3, dfac, True, DT); put(ws, r, 4, v, True, NUM); put(ws, r, 5, ech, True, DT)
            put(ws, r, 6, 0, True, NUM); put(ws, r, 7, f"=D{r}-F{r}", fmt=NUM); put(ws, r, 8, f"=IF(G{r}>0,MAX(0,$K$4-E{r}),0)", fmt="0")
            put(ws, r, 9, f'=IF(G{r}=0,"Soldée",IF(H{r}=0,"Non échu",IF(H{r}<=30,"1-30 j",IF(H{r}<=60,"31-60 j",IF(H{r}<=90,"61-90 j","+90 j")))))')
            put(ws, r, 10, "Litige : chaises abîmées" if (cl.startswith("Bâtir") and i == 4) else "", True); put(ws, r, 11, None, True, DT); put(ws, r, 12, "", True)
            r += 1
    last = r - 1; put(ws, r, 1, "Total", bold=True); put(ws, r, 7, f"=SUM(G6:G{last})", fmt=NUM, bold=True); tot = r
    b0 = tot + 3; ws.cell(row=b0-1, column=1, value="Balance âgée (calculée)").font = T
    header(ws, b0, ["Client"] + F.BUCKETS + ["Total"])
    for j, cl in enumerate(F.CLIENTS):
        rr = b0 + 1 + j; put(ws, rr, 1, cl)
        for i, bk in enumerate(F.BUCKETS):
            col = chr(66+i); put(ws, rr, 2+i, f'=SUMIFS($G$6:$G${last},$A$6:$A${last},$A{rr},$I$6:$I${last},{col}${b0})', fmt=NUM)
        put(ws, rr, 7, f"=SUM(B{rr}:F{rr})", fmt=NUM)
    rt = b0 + 1 + len(F.CLIENTS); put(ws, rt, 1, "Total", bold=True)
    for i in range(6): put(ws, rt, 2+i, f"=SUM({chr(66+i)}{b0+1}:{chr(66+i)}{rt-1})", fmt=NUM, bold=True)
    put(ws, rt+2, 1, "DSO (jours) : créances / ventes de la période × jours"); put(ws, rt+2, 4, 300000, True, NUM); put(ws, rt+2, 5, 92, True, "0")
    put(ws, rt+2, 7, f"=G{rt}/D{rt+2}*E{rt+2}", fmt="0.0"); ws.cell(row=rt+2, column=4).comment = Comment("Ventes du T4 2025 (USD)", "VI")
    exp = {f"A4_Creances!G{rt}": 126000, f"A4_Creances!G{rt+2}": round(F.DSO_31DEC, 2)}
    for i, v in enumerate(F.CREANCES_BUCKETS): exp[f"A4_Creances!{chr(66+i)}{rt}"] = v
    return exp

# ---------------- A5 -------------------------------------------------------------
def a5(wb):
    ws = wb.create_sheet("A5_Dettes"); title(ws, "A5. Suivi des dettes fournisseurs", "Exemple : dettes de MAKAO au 31/12/2025 et facture MX-1187 saisie deux fois en janvier.")
    put(ws, 4, 10, "Date d'analyse"); put(ws, 4, 11, date(2026, 1, 2), True, DT)
    header(ws, 5, ["Fournisseur", "N° facture", "Date", "Montant", "Échéance", "Payé", "Reste", "Jours avant échéance", "Priorité", "Contrôle doublon"], [26, 13, 12, 11, 12, 10, 11, 12, 13, 16])
    dv = DataValidation(type="list", formula1='"Obligatoire,Critique,Négociable,Différable"', allow_blank=True); ws.add_data_validation(dv)
    rows = [("Papeteries Unies", "PU-4410", date(2025, 11, 20), 12000, date(2025, 12, 20), "Négociable"),
            ("Grossiste InfoPlus", "IP-88231", date(2025, 12, 10), 40000, date(2026, 1, 10), "Critique"),
            ("Mobilier Express", "MX-1187", date(2025, 12, 12), 4800, date(2026, 1, 25), "Négociable"),
            ("Mobilier Express", "MX-1195", date(2025, 12, 26), 17200, date(2026, 1, 25), "Négociable"),
            ("Papeteries Unies", "PU-4502", date(2025, 12, 26), 18000, date(2026, 1, 25), "Négociable"),
            ("Mobilier Express", "MX-1187", date(2025, 12, 12), 4800, date(2026, 1, 25), "Négociable")]
    for i, (a, b, c, d, e, p) in enumerate(rows):
        r = 6 + i; put(ws, r, 1, a, True); put(ws, r, 2, b, True); put(ws, r, 3, c, True, DT); put(ws, r, 4, d, True, NUM); put(ws, r, 5, e, True, DT)
        put(ws, r, 6, 0, True, NUM); put(ws, r, 7, f"=D{r}-F{r}", fmt=NUM); put(ws, r, 8, f"=E{r}-$K$4", fmt="0"); put(ws, r, 9, p, True); dv.add(ws.cell(row=r, column=9))
        put(ws, r, 10, f'=IF(COUNTIFS($A$6:$A$20,A{r},$B$6:$B$20,B{r})>1,"DOUBLON","")')
    put(ws, 12, 4, "Ligne 11 : seconde saisie de MX-1187, à supprimer. Total réel des dettes = 92 000 USD.")
    ws["D12"].font = NOTE
    put(ws, 13, 1, "Total saisi", bold=True); put(ws, 13, 7, "=SUM(G6:G11)", fmt=NUM, bold=True)
    put(ws, 14, 1, "Total hors doublons", bold=True); put(ws, 14, 7, '=SUMIFS(G6:G11,J6:J11,"")+SUMIFS(G6:G11,J6:J11,"DOUBLON")/2', fmt=NUM, bold=True)
    ws.conditional_formatting.add("J6:J20", CellIsRule(operator="equal", formula=['"DOUBLON"'], font=Font(color="B00020", bold=True)))
    return {"A5_Dettes!G14": 92000, "A5_Dettes!G13": 96800}

# ---------------- A6 -------------------------------------------------------------
def a6(wb):
    ws = wb.create_sheet("A6_Calendrier_paiements"); title(ws, "A6. Calendrier des paiements", "Exemple : plan de paiement de MAKAO, semaine du 5 au 11 janvier 2026 (chapitre 5).")
    put(ws, 4, 1, "Trésorerie disponible pour la semaine"); put(ws, 4, 3, 41500, True, NUM)
    header(ws, 6, ["Date prévue", "Bénéficiaire", "Montant", "Catégorie", "Validé par", "Statut", "Disponible restant", "Alerte"], [12, 32, 12, 14, 14, 12, 16, 14])
    rows = [(date(2026, 1, 5), "Loyer de janvier", 4000, "Obligatoire"), (date(2026, 1, 5), "Papeteries Unies (1re part)", 6000, "Négociable"),
            (date(2026, 1, 10), "Charges externes", 1500, "Obligatoire"), (date(2026, 1, 10), "Grossiste InfoPlus (1re part)", 20000, "Critique")]
    for i, (d, b, m, c) in enumerate(rows):
        r = 7 + i; put(ws, r, 1, d, True, DT); put(ws, r, 2, b, True); put(ws, r, 3, m, True, NUM); put(ws, r, 4, c, True); put(ws, r, 5, "Gérante", True); put(ws, r, 6, "Prévu", True)
        put(ws, r, 7, f"=$C$4-SUM($C$7:C{r})", fmt=NUM); put(ws, r, 8, f'=IF(G{r}<0,"INSUFFISANT","")')
    return {"A6_Calendrier_paiements!G10": 10000}

# ---------------- A7 -------------------------------------------------------------
def a7(wb):
    ws = wb.create_sheet("A7_Rapprochement"); title(ws, "A7. Rapprochement bancaire", "Exemple : compte USD de MAKAO à la Banque Alpha au 31/01/2026 (chapitre 7).")
    for c, w in zip("ABCDE", [46, 13, 4, 46, 13]): ws.column_dimensions[c].width = w
    header(ws, 5, ["Côté comptabilité", "USD", "", "Côté banque", "USD"])
    r = F.REC
    put(ws, 6, 1, "Solde selon la comptabilité"); put(ws, 6, 2, r['livre'], True, NUM); put(ws, 6, 4, "Solde selon le relevé bancaire"); put(ws, 6, 5, r['banque'], True, NUM)
    put(ws, 7, 1, "- Frais bancaires non comptabilisés"); put(ws, 7, 2, -r['frais'], True, NUM); put(ws, 7, 4, "- Chèques émis non présentés"); put(ws, 7, 5, -r['cheque_non_presente'], True, NUM)
    put(ws, 8, 1, "+ Virements reçus non comptabilisés"); put(ws, 8, 2, 0, True, NUM); put(ws, 8, 4, "+ Remises non encore créditées"); put(ws, 8, 5, r['remise_non_creditee'], True, NUM)
    put(ws, 9, 1, "Autres ajustements (à détailler)"); put(ws, 9, 2, 0, True, NUM); put(ws, 9, 4, "Autres ajustements (à détailler)"); put(ws, 9, 5, 0, True, NUM)
    put(ws, 10, 1, "Solde rapproché", bold=True); put(ws, 10, 2, "=SUM(B6:B9)", fmt=NUM, bold=True); put(ws, 10, 4, "Solde rapproché", bold=True); put(ws, 10, 5, "=SUM(E6:E9)", fmt=NUM, bold=True)
    put(ws, 12, 1, "Contrôle", bold=True); put(ws, 12, 2, '=IF(ABS(B10-E10)<0.01,"RAPPROCHÉ","ÉCART À EXPLIQUER")', bold=True)
    put(ws, 14, 1, "Préparé par / date"); put(ws, 14, 2, "", True); put(ws, 15, 1, "Revu par / date"); put(ws, 15, 2, "", True)
    return {"A7_Rapprochement!B10": r['rapproche'], "A7_Rapprochement!E10": r['rapproche'], "A7_Rapprochement!B12": "RAPPROCHÉ"}

# ---------------- A8 -------------------------------------------------------------
CHECKS = [("Caisse", "Plafond d'encaisse respecté (1 500 USD)", "Quotidienne", "Caissière"), ("Caisse", "Arrêté de caisse quotidien signé", "Quotidienne", "Caissière"),
 ("Caisse", "Comptage inopiné avec procès-verbal de billetage", "Mensuelle", "Gérante"), ("Caisse", "Pièces de caisse numérotées et signées", "Quotidienne", "Comptable"),
 ("Banque", "Rapprochement bancaire signé et revu", "Mensuelle", "Comptable / RAF"), ("Banque", "Éléments en suspens de plus de 30 jours analysés", "Mensuelle", "RAF"),
 ("Banque", "Droits d'accès bancaires revus", "Trimestrielle", "Gérante"), ("Paiements", "Double validation au-delà de 2 000 USD", "Chaque paiement", "Gérante"),
 ("Paiements", "Contrôle des doublons avant paiement", "Chaque paiement", "Comptable"), ("Paiements", "Paiement sur facture originale validée", "Chaque paiement", "Comptable"),
 ("Paiements", "Jour unique de paiement hebdomadaire respecté", "Hebdomadaire", "RAF"), ("Achats", "Bon de commande signé selon les seuils", "Chaque achat", "Chef de service"),
 ("Achats", "Trois devis au-delà de 5 000 USD", "Chaque achat", "Gérante"), ("Fournisseurs", "Contre-appel avant changement de coordonnées bancaires", "Chaque changement", "RAF"),
 ("Fournisseurs", "Rapprochement des relevés fournisseurs", "Mensuelle", "Comptable"), ("Fournisseurs", "Revue du fichier fournisseurs", "Annuelle", "RAF"),
 ("Créances", "Balance âgée mise à jour", "Hebdomadaire", "Responsable recouvrement"), ("Créances", "Relances tracées selon le calendrier", "Hebdomadaire", "Responsable recouvrement"),
 ("Monnaie électronique", "Rapprochement du portefeuille", "Mensuelle", "Comptable"), ("Monnaie électronique", "Codes détenus par deux personnes, plafonds actifs", "Trimestrielle", "Gérante"),
 ("Projets (ASBL)", "Solde bancaire ventilé par origine des fonds", "Mensuelle", "Trésorier"), ("Projets (ASBL)", "Avances justifiées dans le délai", "Hebdomadaire", "Trésorier"),
 ("IA et données", "Données anonymisées avant usage d'un assistant IA", "Chaque usage", "Utilisateur"), ("IA et données", "Résultat d'IA vérifié par un responsable", "Chaque usage", "RAF")]
def a8(wb):
    ws = wb.create_sheet("A8_Checklist_CI"); title(ws, "A8. Checklist de contrôle interne", "24 contrôles issus des chapitres 7, 10 et 11.")
    header(ws, 5, ["Domaine", "Contrôle", "Fréquence", "Responsable", "Fait", "Date", "Commentaire"], [20, 52, 16, 22, 8, 12, 30])
    dv = DataValidation(type="list", formula1='"Oui,Non"', allow_blank=True); ws.add_data_validation(dv)
    for i, (a, b, c, d) in enumerate(CHECKS):
        r = 6 + i; put(ws, r, 1, a); put(ws, r, 2, b); put(ws, r, 3, c); put(ws, r, 4, d)
        put(ws, r, 5, "Oui" if i % 4 else "Non", True); dv.add(ws.cell(row=r, column=5)); put(ws, r, 6, None, True, DT); put(ws, r, 7, "", True)
    last = 5 + len(CHECKS)
    put(ws, last+2, 1, "Taux de conformité", bold=True); put(ws, last+2, 5, f'=IF(COUNTA(E6:E{last})=0,"",COUNTIF(E6:E{last},"Oui")/COUNTA(E6:E{last}))', fmt=PCT, bold=True)
    ws.conditional_formatting.add(f"E6:E{last}", CellIsRule(operator="equal", formula=['"Non"'], font=Font(color="B00020", bold=True)))
    return {f"A8_Checklist_CI!E{last+2}": 18/24}

# ---------------- A9 -------------------------------------------------------------
def a9(wb):
    ws = wb.create_sheet("A9_Tableau_de_bord"); title(ws, "A9. Tableau de bord de trésorerie", "Exemple : MAKAO au 31/01/2026 (chapitre 8). Saisie en colonne B, indicateurs calculés en dessous.")
    ws.column_dimensions["A"].width = 46; ws.column_dimensions["B"].width = 14; ws.column_dimensions["C"].width = 14; ws.column_dimensions["D"].width = 14; ws.column_dimensions["E"].width = 16
    inputs = [("Trésorerie disponible après rapprochement", F.TRESO_31JAN), ("Décaissements fixes mensuels", F.FIXES_TOTAL),
              ("Encaissements prévus du mois", F.JAN['prevu_E']), ("Encaissements réalisés du mois", F.JAN['reel_E']),
              ("Décaissements prévus du mois", F.JAN['prevu_D']), ("Décaissements réalisés du mois", F.JAN['reel_D']),
              ("Créances clients totales", sum(F.CREANCES_31JAN)), ("Créances échues de plus de 30 jours", sum(F.CREANCES_31JAN[2:])),
              ("Ventes des 3 derniers mois", 100000 + 100000 + F.JAN_VENTES_REELLES), ("Dettes fournisseurs", F.DETTES_31JAN),
              ("Achats des 3 derniers mois", 80000 + 80000 + F.JAN_VENTES_REELLES*F.TAUX_ACHAT), ("Nombre de jours de la période", 92),
              ("Point bas prévisionnel (13 semaines)", F.BESOIN['montant']*-1), ("Réserve de sécurité visée", F.RESERVE_CIBLE)]
    header(ws, 5, ["Donnée", "Valeur"])
    for i, (a, v) in enumerate(inputs): put(ws, 6+i, 1, a); put(ws, 6+i, 2, round(v, 2), True, NUM)
    header(ws, 22, ["Indicateur", "Valeur", "Seuil", "Sens", "État"])
    ind = [("Couverture (mois)", "=B6/B7", 1, ">=", "0.00"), ("Taux de réalisation des encaissements", "=B9/B8", 0.95, ">=", PCT),
           ("Écart sur décaissements", "=(B11-B10)/B10", 0.03, "<=", PCT), ("DSO (jours)", "=B12/B14*B17", 35, "<=", "0.0"),
           ("Part des créances de plus de 30 jours", "=B13/B12", 0.05, "<=", PCT), ("DPO (jours)", "=B15/B16*B17", 30, ">=", "0.0"),
           ("Point bas prévisionnel (USD)", "=B18", 0, ">=", NUM), ("Écart à la réserve (USD)", "=B6-B19", 0, ">=", NUM)]
    for i, (a, f, s, sens, fmt) in enumerate(ind):
        r = 23 + i; put(ws, r, 1, a); put(ws, r, 2, f, fmt=fmt); put(ws, r, 3, s, True, fmt); put(ws, r, 4, sens)
        put(ws, r, 5, f'=IF(D{r}=">=",IF(B{r}>=C{r},"OK","ALERTE"),IF(B{r}<=C{r},"OK","ALERTE"))')
    ws.conditional_formatting.add("E23:E30", CellIsRule(operator="equal", formula=['"ALERTE"'], font=Font(color="B00020", bold=True)))
    return {"A9_Tableau_de_bord!B23": F.TRESO_31JAN/F.FIXES_TOTAL, "A9_Tableau_de_bord!B26": F.DSO_31JAN, "A9_Tableau_de_bord!B28": F.DPO_31JAN,
            "A9_Tableau_de_bord!B24": F.JAN['reel_E']/F.JAN['prevu_E']}

# ---------------- A10 ------------------------------------------------------------
def a10(wb):
    ws = wb.create_sheet("A10_Analyse_ecarts"); title(ws, "A10. Analyse des écarts", "Exemple : janvier 2026 de MAKAO (chapitre 3).")
    header(ws, 5, ["Catégorie", "Prévu", "Réalisé", "Écart", "Écart %", "Nature", "Explication", "Action et responsable"], [34, 12, 12, 12, 10, 12, 40, 30])
    dv = DataValidation(type="list", formula1='"Décalage,Volume,Anomalie,Imprévu"', allow_blank=True); ws.add_data_validation(dv)
    expl = {"Créances au 31/12": ("Décalage", "Palmiers -6 000 reporté à février ; Clinique +2 000 anticipé", "Relance Palmiers (RAF)"),
            "Ventes du mois (comptant)": ("Volume", "Ventes de 92 000 au lieu de 95 000", "Suivi commercial"),
            "Fournisseurs": ("Anomalie", "Facture MX-1187 payée deux fois", "Avoir obtenu ; contrôle des doublons"),
            "Autres charges externes": ("Imprévu", "Réparation du groupe électrogène", "Régularisation écrite")}
    rows = [(k, p, F.JAN_REEL_ENC[k]) for k, p in F.JAN_PREVU_ENC.items()] + [(k, p, F.JAN_REEL_DEC[k]) for k, p in F.JAN_PREVU_DEC.items()]
    for i, (k, p, rv) in enumerate(rows):
        r = 6 + i; put(ws, r, 1, k); put(ws, r, 2, p, True, NUM); put(ws, r, 3, rv, True, NUM); put(ws, r, 4, f"=C{r}-B{r}", fmt=NUM)
        put(ws, r, 5, f'=IF(B{r}=0,"",D{r}/B{r})', fmt=PCT); e = expl.get(k, ("", "", ""))
        put(ws, r, 6, e[0], True); dv.add(ws.cell(row=r, column=6)); put(ws, r, 7, e[1], True); put(ws, r, 8, e[2], True)
    put(ws, 15, 1, "Total encaissements", bold=True); put(ws, 15, 2, "=SUM(B6:B7)", fmt=NUM, bold=True); put(ws, 15, 3, "=SUM(C6:C7)", fmt=NUM, bold=True); put(ws, 15, 4, "=C15-B15", fmt=NUM, bold=True)
    put(ws, 16, 1, "Total décaissements", bold=True); put(ws, 16, 2, "=SUM(B8:B13)", fmt=NUM, bold=True); put(ws, 16, 3, "=SUM(C8:C13)", fmt=NUM, bold=True); put(ws, 16, 4, "=C16-B16", fmt=NUM, bold=True)
    put(ws, 17, 1, "Trésorerie d'ouverture"); put(ws, 17, 2, F.OPENING, True, NUM); put(ws, 17, 3, "=B17", fmt=NUM)
    put(ws, 18, 1, "Solde fin de période", bold=True); put(ws, 18, 2, "=B17+B15-B16", fmt=NUM, bold=True); put(ws, 18, 3, "=C17+C15-C16", fmt=NUM, bold=True); put(ws, 18, 4, "=C18-B18", fmt=NUM, bold=True)
    put(ws, 20, 1, "Seuil d'explication obligatoire : écart > 2 % ou > 1 000 USD.")
    ws["A20"].font = NOTE
    return {"A10_Analyse_ecarts!B18": F.JAN['prevu_C'], "A10_Analyse_ecarts!C18": F.JAN['reel_C']}

MODELS = [("01_Situation_journaliere", a1), ("02_Budget_mensuel", a2), ("03_Previsionnel_13_semaines", a3), ("04_Suivi_creances", a4),
          ("05_Suivi_dettes_fournisseurs", a5), ("06_Calendrier_paiements", a6), ("07_Rapprochement_bancaire", a7),
          ("08_Checklist_controle_interne", a8), ("09_Tableau_de_bord", a9), ("10_Analyse_ecarts", a10)]
def readme(wb, names):
    ws = wb.active; ws.title = "Lisez-moi"; ws.column_dimensions["A"].width = 110
    lines = ["LA TRÉSO SOUS CONTRÔLE : outils pratiques", "© 2026 Verdi Imbole. Modèles d'accompagnement du livre ; usage personnel et professionnel du lecteur.",
             "", "Mode d'emploi", "1. Les cellules jaunes à texte bleu sont des zones de saisie ; les cellules blanches contiennent des formules.",
             "2. Les données d'exemple reprennent le cas fictif MAKAO Distribution du livre : remplacez-les par les vôtres.",
             "3. Montants en USD. Taux de change pédagogique fictif : 2 850 CDF pour 1 USD. Utilisez le taux officiel du jour dans votre organisation.",
             "4. Compatibles Excel 2019 et versions ultérieures et Google Sheets (MIN.SI.ENS / MINIFS requis pour l'onglet A3).",
             "5. Ne jamais saisir d'identifiants bancaires ni de mots de passe dans ces fichiers.", "", "Onglets"] + names
    for i, l in enumerate(lines, 1):
        c = ws.cell(row=i, column=1, value=l); c.font = T if i == 1 else (B if l in ("Mode d'emploi", "Onglets") else N)
def build():
    out = os.path.join(ROOT, "livrables", "outils_excel"); allexp = {}
    wb = Workbook(); readme(wb, [n.replace("_", " ") for n, _ in MODELS])
    for n, f in MODELS: allexp.update(f(wb))
    for ws in wb.worksheets: ws.sheet_view.showGridLines = False
    wb.save(os.path.join(out, "Outils_Treso_sous_controle.xlsx"))
    single = {}
    for n, f in MODELS:
        w = Workbook(); readme(w, [n.replace("_", " ")]); exp = f(w)
        for ws in w.worksheets: ws.sheet_view.showGridLines = False
        p = os.path.join(out, f"{n}.xlsx"); w.save(p); single[p] = exp
    import json
    json.dump({"combined": {k: v for k, v in allexp.items()}, "single": single}, open(os.path.join(ROOT, "build", "excel_expected.json"), "w"), ensure_ascii=False, default=str)
if __name__ == "__main__": build(); print("ok")
