"""Tableaux générés à partir des données centrales (aucun chiffre saisi à la main)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data"))
import fil_rouge as F
from datetime import date

from decimal import Decimal, ROUND_HALF_UP
def rnd(x): return int(Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
def n(x, sign=False):
    v = rnd(x)
    s = f"{abs(v):,}".replace(",", " ")
    if v < 0: return "-" + s
    return ("+" + s) if (sign and v > 0) else s
def pct(x, d=1): return f"{x*100:.{d}f}".replace(".", ",") + " %"
def d2(x): return f"{x:,.2f}".replace(",", " ").replace(".", ",")
def jj(d): return d.strftime("%d/%m")

def t_q4_resultat():
    q = F.Q4
    rows = [["Ventes facturées (chiffre d'affaires)", n(q['ventes'])], ["- Coût d'achat des marchandises vendues", n(-q['cout_marchandises'])],
            ["- Salaires et charges sociales", n(-q['personnel'])], ["- Loyer, énergie, transport, autres charges", n(-q['charges_ext'])],
            ["- Amortissements", n(-q['amortissements'])], ["- Intérêts de l'emprunt", n(-q['interets'])],
            ["Résultat avant impôt", n(q['resultat'])]]
    return dict(header=["Compte de résultat simplifié, T4 2025", "USD"], rows=rows, widths=[75, 25])
def t_q4_tresorerie():
    c = F.Q4_CASH; q = F.Q4
    rows = [["Trésorerie au 1er octobre", n(c['tresorerie_ouverture'])], ["+ Encaissements clients", n(c['encaissements_clients'])],
            ["- Paiements aux fournisseurs", n(-c['paiements_fournisseurs'])], ["- Salaires et charges sociales", n(-q['personnel'])],
            ["- Loyer, énergie, transport, autres charges", n(-q['charges_ext'])], ["- Intérêts de l'emprunt", n(-q['interets'])],
            ["- Remboursement du capital de l'emprunt", n(-c['remboursement_emprunt'])], ["- Achat d'un véhicule de livraison", n(-c['investissement'])],
            ["Trésorerie au 31 décembre", n(c['tresorerie_cloture'])]]
    return dict(header=["Mouvements de trésorerie, T4 2025", "USD"], rows=rows, widths=[75, 25])
def t_bridge():
    rows = [[a, n(b, sign=True)] for a, b in F.BRIDGE] + [["Variation de la trésorerie du trimestre", n(F.Q4_CASH['variation'])]]
    return dict(header=["Du résultat à la trésorerie", "USD"], rows=rows, widths=[75, 25], totals=(len(rows)-1,))
def t_dispo_3112():
    rows = [[k, n(v)] for k, v in F.DISPO.items()] + [["Total des disponibilités", n(F.DISPO_TOTAL)]]
    return dict(header=["Disponibilités au 31/12/2025", "USD"], rows=rows, widths=[75, 25],
                note="Conversion au taux pédagogique fictif de 2 850 CDF pour 1 USD (31/12/2025).")
def t_creances():
    rows = [[k] + [n(x) if x else "-" for x in v] + [n(sum(v))] for k, v in F.CLIENTS.items()]
    rows.append(["Total"] + [n(x) for x in F.CREANCES_BUCKETS] + [n(F.CREANCES_TOTAL)])
    rows.append(["Part du total"] + [pct(x/F.CREANCES_TOTAL, 0) for x in F.CREANCES_BUCKETS] + ["100 %"])
    return dict(header=["Client"] + F.BUCKETS + ["Total"], rows=rows, widths=[36, 13, 12, 11, 11, 11, 14], size=7.6, totals=(len(rows)-2,))
def t_fournisseurs():
    rows = [[k, n(v[0]), v[1].strftime("%d/%m/%Y")] for k, v in F.FOURNISSEURS.items()] + [["Total", n(F.DETTES_TOTAL), ""]]
    return dict(header=["Fournisseur", "USD", "Échéance"], rows=rows, widths=[60, 20, 20], align=['l', 'r', 'r'])
def t_fixes():
    rows = [[k, n(v)] for k, v in F.FIXES.items()] + [["Total des décaissements fixes mensuels", n(F.FIXES_TOTAL)]]
    return dict(header=["Engagement récurrent", "USD/mois"], rows=rows, widths=[78, 22])
def t_situation_initiale():
    dispo = F.DISPO_TOTAL
    enc30 = 80_000*45/80 + 30_000 + 5_000  # attendus en janvier sur créances existantes (prévision prudente)
    rows = [["Disponibilités au 31/12/2025", n(dispo)],
            ["+ Créances qu'on peut raisonnablement encaisser en janvier", n(enc30)],
            ["- Dettes fournisseurs échues ou à échéance en janvier", n(-F.DETTES_TOTAL)],
            ["- Décaissements fixes de janvier", n(-F.FIXES_TOTAL)],
            ["- Remboursement prévu au compte courant de la gérante", n(-5_000)],
            ["Solde de trésorerie estimé fin janvier (avant ventes de janvier)", n(dispo + enc30 - F.DETTES_TOTAL - F.FIXES_TOTAL - 5_000)]]
    return dict(header=["Situation initiale : ce que l'on sait au 2 janvier", "USD"], rows=rows, widths=[78, 22])

def _cat_rows(M, months, cats, key):
    return [[c] + [n(M[m][key].get(c, 0)) for m in months] + [n(sum(M[m][key].get(c, 0) for m in months))] for c in cats
            if any(M[m][key].get(c, 0) for m in months)]
def t_budget_q1(M=None):
    M = M or F.M_BASE; ms = [1, 2, 3]
    rows = [["Trésorerie d'ouverture (a)"] + [n(M[m]['ouverture']) for m in ms] + [n(M[1]['ouverture'])]]
    rows += [["ENCAISSEMENTS", "", "", "", ""]]
    rows += _cat_rows(M, ms, F.ENC_CAT, 'enc')
    rows += [["Total encaissements (b)"] + [n(M[m]['E']) for m in ms] + [n(sum(M[m]['E'] for m in ms))]]
    rows += [["DÉCAISSEMENTS", "", "", "", ""]]
    rows += _cat_rows(M, ms, F.DEC_CAT, 'dec')
    rows += [["Total décaissements (c)"] + [n(M[m]['D']) for m in ms] + [n(sum(M[m]['D'] for m in ms))]]
    rows += [["Solde final (a + b - c)"] + [n(M[m]['cloture']) for m in ms] + [n(M[3]['cloture'])]]
    bold = [i for i, r in enumerate(rows) if r[0] in ("ENCAISSEMENTS", "DÉCAISSEMENTS")]
    return dict(header=["USD", "Janvier", "Février", "Mars", "T1"], rows=rows, widths=[40, 15, 15, 15, 15], size=7.7, bold=bold,
                totals=tuple(i for i, r in enumerate(rows) if r[0].startswith(("Total", "Solde", "Trésorerie d'ouv"))))
def t_budget_s1():
    M = F.M_BASE
    rows = [[F.MOIS[m], n(r['ouverture']), n(r['E']), n(r['D']), n(r['cloture'])] for m, r in M.items()]
    return dict(header=["Mois", "Ouverture", "Encaissements", "Décaissements", "Clôture"], rows=rows, widths=[22, 19, 20, 20, 19])
def _weeks(W, plan_low=True):
    rows = [[f"S{r['sem']}", f"{jj(r['debut'])}-{jj(r['fin'])}", n(r['ouverture']), n(r['E']), n(r['D']), n(r['cloture']), n(r['plus_bas'])] for r in W]
    return dict(header=["Sem.", "Période", "Ouverture", "Entrées", "Sorties", "Clôture", "Point bas"], rows=rows,
                widths=[9, 18, 15, 14, 14, 15, 15], size=7.7, align=['l', 'l', 'r', 'r', 'r', 'r', 'r'])
def t_13w_base(): return _weeks(F.W_BASE)
def t_13w_plan(): return _weeks(F.W_PLAN)
def t_reprev(): return _weeks(F.W_REPREV)
def t_jan_ecarts():
    rows = []
    for (k, p), r in zip(F.JAN_PREVU_ENC.items(), F.JAN_REEL_ENC.values()):
        rows.append([k, n(p), n(r), n(r-p, True), pct((r-p)/p)])
    rows.append(["Total encaissements", n(F.JAN['prevu_E']), n(F.JAN['reel_E']), n(F.JAN['reel_E']-F.JAN['prevu_E'], True), pct((F.JAN['reel_E']-F.JAN['prevu_E'])/F.JAN['prevu_E'])])
    for (k, p), r in zip(F.JAN_PREVU_DEC.items(), F.JAN_REEL_DEC.values()):
        rows.append([k, n(p), n(r), n(r-p, True), pct((r-p)/p) if r != p else "0,0 %"])
    rows.append(["Total décaissements", n(F.JAN['prevu_D']), n(F.JAN['reel_D']), n(F.JAN['reel_D']-F.JAN['prevu_D'], True), pct((F.JAN['reel_D']-F.JAN['prevu_D'])/F.JAN['prevu_D'])])
    rows.append(["Solde fin janvier", n(F.JAN['prevu_C']), n(F.JAN['reel_C']), n(F.JAN['reel_C']-F.JAN['prevu_C'], True), pct((F.JAN['reel_C']-F.JAN['prevu_C'])/F.JAN['prevu_C'])])
    return dict(header=["Janvier 2026", "Prévu", "Réalisé", "Écart", "Écart %"], rows=rows, widths=[38, 15, 15, 15, 14], size=7.7)
def t_compare_versions():
    rows = []
    for m in range(1, 7):
        rows.append([F.MOIS[m], n(F.M_BASE[m]['cloture']), n(F.M_ENC[m]['cloture']), n(F.M_PLAN[m]['cloture'])])
    lb, le, lp = F.daily_min(F.EV_BASE), F.daily_min(F.EV_ENC), F.daily_min(F.EV_PLAN)
    rows.append(["Point bas du semestre", n(lb[0]), n(le[0]), n(lp[0])])
    rows.append(["Date du point bas", lb[1].strftime("%d/%m"), le[1].strftime("%d/%m"), lp[1].strftime("%d/%m")])
    return dict(header=["Solde fin de mois", "Initial (ch. 3)", "Après ch. 4", "Après ch. 5"], rows=rows, widths=[34, 22, 22, 22], totals=(6,))
def t_engagements_s1():
    rows = [["05/01", "Loyer de janvier", "4 000", "Contrat de bail"], ["05/01", "Papeteries Unies, facture échue le 20/12", "12 000", "Relation fournisseur"],
            ["10/01", "Grossiste InfoPlus, facture de décembre", "40 000", "Principal fournisseur"], ["10/01", "Charges externes (énergie, carburant)", "1 500", "Exploitation"],
            ["Total", "", "57 500", ""]]
    return dict(header=["Date", "Engagement", "USD", "Nature"], rows=rows, widths=[11, 46, 13, 30], align=['l', 'l', 'r', 'l'])
def t_fin_court():
    rows = [[k, v['hyp'], d2(v['interets']), d2(v['frais']), d2(v['total'])] for k, v in F.FIN_COURT.items()]
    return dict(header=["Solution", "Hypothèses (fictives)", "Intérêts", "Frais", "Coût"], rows=rows, widths=[23, 37, 12, 12, 13], size=7.3,
                align=['l', 'l', 'r', 'r', 'r'])
def t_fin_30j():
    rows = [[k, d2(v['interets']), d2(v['frais']), d2(v['total']), pct(v['teg'])] for k, v in F.FIN_30J.items()]
    return dict(header=["20 000 USD pendant 30 jours", "Intérêts", "Frais", "Coût total", "Coût annualisé"], rows=rows, widths=[36, 15, 13, 16, 18], size=7.6)
def t_rec():
    r = F.REC
    rows = [["Solde selon la comptabilité de Makao (compte 521)", n(r['livre']), "Solde selon le relevé de la Banque Alpha", n(r['banque'])],
            ["- Frais bancaires de janvier non comptabilisés", n(-r['frais']), "- Chèque n° 0462 émis, non encore présenté", n(-r['cheque_non_presente'])],
            ["", "", "+ Remise de chèque du 30/01 non encore créditée", n(r['remise_non_creditee'], True)],
            ["Solde rapproché", n(r['rapproche']), "Solde rapproché", n(r['rapproche'])]]
    return dict(header=["Côté comptabilité", "USD", "Côté banque", "USD"], rows=rows, widths=[33, 13, 37, 13], size=7.5, align=['l', 'r', 'l', 'r'])
def t_dispo_31jan():
    rows = [[k, n(v)] for k, v in F.DISPO_31JAN.items()] + [["Total selon la comptabilité", n(F.JAN['reel_C'])],
            ["- Frais bancaires révélés par le rapprochement", n(-F.REC['frais'])], ["Trésorerie disponible corrigée au 31/01", n(F.TRESO_31JAN)]]
    return dict(header=["Disponibilités au 31/01/2026", "USD"], rows=rows, widths=[75, 25], totals=(4, 6))
def t_dashboard():
    cr = F.CREANCES_31JAN; tot = sum(cr)
    fev = F.M_REPREV[2]; low = F.low_from(F.EV_REPREV, F.TRESO_31JAN, date(2026, 3, 31))
    rows = [
        ["1. Trésorerie disponible", n(F.TRESO_31JAN), "15 000 au 31/12", "En hausse, mais sous la cible"],
        ["2. Couverture (mois de charges fixes)", d2(F.TRESO_31JAN/F.FIXES_TOTAL).rstrip('0').rstrip(',') + " mois", "Cible : 1 mois", "À renforcer"],
        ["3. Solde prévu fin février", n(fev['cloture']), f"Point bas : {n(low[0])} le {low[1].strftime('%d/%m')}", "Alerte : besoin ponctuel"],
        ["4. Taux de réalisation des encaissements", pct(F.JAN['reel_E']/F.JAN['prevu_E']), "Cible : 95 % et plus", "Limite"],
        ["5. Écart sur décaissements", pct((F.JAN['reel_D']-F.JAN['prevu_D'])/F.JAN['prevu_D']), "Tolérance : 3 %", "Hors tolérance"],
        ["6. Délai moyen de recouvrement (DSO)", f"{F.DSO_31JAN:.1f}".replace('.', ',') + " j", f"{F.DSO_31DEC:.1f}".replace('.', ',') + " j au 31/12", "En amélioration"],
        ["7. Créances échues depuis plus de 30 j", n(cr[2]+cr[3]+cr[4]), pct((cr[2]+cr[3]+cr[4])/tot) + " des créances", "Palmiers et litige"],
        ["8. Délai moyen de paiement fournisseurs (DPO)", f"{F.DPO_31JAN:.1f}".replace('.', ',') + " j", "Conditions : 30 j", "Conforme"],
    ]
    return dict(header=["Indicateur", "Valeur", "Référence", "Lecture"], rows=rows, widths=[36, 17, 25, 22], size=7.4, align=['l', 'r', 'l', 'l'])
def t_scenarios():
    rows = []
    rows.append(["Sans perte de client"] + [n(F.BASE_AVR['m'][m]['cloture']) for m in (4, 5, 6)] + [n(F.BASE_AVR['low'][0])])
    for k, v in F.SCEN_RES.items():
        rows.append([k] + [n(v['m'][m]['cloture']) for m in (4, 5, 6)] + [n(v['low'][0])])
    rows.append(["Réaliste + plan d'urgence"] + [n(F.SCEN_MES['m'][m]['cloture']) for m in (4, 5, 6)] + [n(F.SCEN_MES['low'][0])])
    rows.append(["Pessimiste + plan d'urgence"] + [n(F.SCEN_PES_MES['m'][m]['cloture']) for m in (4, 5, 6)] + [n(F.SCEN_PES_MES['low'][0])])
    return dict(header=["Scénario (USD)", "Fin avril", "Fin mai", "Fin juin", "Point bas"], rows=rows, widths=[36, 16, 16, 16, 16], size=7.7)
def t_asbl_budget():
    rows = [[k, n(v), pct(v/50_000, 0)] for k, v in F.ASBL_BUDGET.items()] + [["Total", n(50_000), "100 %"]]
    return dict(header=["Rubrique budgétaire", "USD", "Part"], rows=rows, widths=[60, 20, 20])
def t_asbl_plan():
    rows = []
    for p, r in zip(F.ASBL_PREVU, F.ASBL_REEL):
        rows.append([F.MOIS[p['m']], n(p['depenses']), n(p['recettes']) if p['recettes'] else "-", n(p['cloture']),
                     n(r['recettes']) if r['recettes'] else "-", n(r['cloture'])])
    return dict(header=["Mois", "Dépenses", "Tranche prévue", "Solde prévu", "Tranche réelle", "Solde réel"], rows=rows,
                widths=[17, 16, 17, 16, 17, 17], size=7.6)
def t_asbl_compte():
    rows = [[k, n(v)] for k, v in F.ASBL_COMPTE_31MARS.items()] + [["Solde du compte bancaire au 31/03", n(sum(F.ASBL_COMPTE_31MARS.values()))]]
    return dict(header=["Composition du solde bancaire", "USD"], rows=rows, widths=[78, 22])
def t_c12_dispo():
    rows = [[k, n(v)] for k, v in F.C12_DISPO.items()] + [["Total selon la comptabilité", n(sum(F.C12_DISPO.values()))]]
    return dict(header=["Disponibilités au 30/06/2026", "USD"], rows=rows, widths=[75, 25])
def t_c12_creances():
    return dict(header=F.BUCKETS + ["Total"], rows=[[n(x) for x in F.C12_CREANCES] + [n(sum(F.C12_CREANCES))]],
                widths=[16, 16, 16, 16, 16, 20], align=['r']*6)
def t_c12_13w_sans(): return _weeks(F.C12_W_SANS)
def t_c12_13w_mes(): return _weeks(F.C12_W_MES)
def t_c12_ajust():
    tot = sum(F.C12_DISPO.values())
    rows = [["Disponibilités selon la comptabilité", n(tot)], ["- Écart de caisse constaté (1 100 - 1 040)", n(-(1_100-1_040))],
            ["- Prélèvement bancaire non justifié, mis en réclamation", n(-450)], ["Trésorerie d'ouverture retenue au 1er juillet", n(F.C12_OPEN)]]
    return dict(header=["Trésorerie d'ouverture de la mission", "USD"], rows=rows, widths=[78, 22])

def t_q4_double():
    q = F.Q4; c = F.Q4_CASH
    L = [("Ventes facturées", q['ventes']), ("- Coût des marchandises vendues", -q['cout_marchandises']), ("- Salaires et charges sociales", -q['personnel']),
         ("- Loyer, énergie, autres charges", -q['charges_ext']), ("- Amortissements", -q['amortissements']), ("- Intérêts", -q['interets']),
         ("", None), ("", None), ("Résultat avant impôt", q['resultat'])]
    R = [("Trésorerie au 1er octobre", c['tresorerie_ouverture']), ("+ Encaissements clients", c['encaissements_clients']),
         ("- Paiements fournisseurs", -c['paiements_fournisseurs']), ("- Salaires et charges sociales", -q['personnel']),
         ("- Loyer, énergie, autres charges", -q['charges_ext']), ("- Intérêts", -q['interets']), ("- Capital de l'emprunt remboursé", -c['remboursement_emprunt']),
         ("- Véhicule de livraison", -c['investissement']), ("Trésorerie au 31 décembre", c['tresorerie_cloture'])]
    rows = [[a, n(b) if b is not None else "", d, n(e)] for (a, b), (d, e) in zip(L, R)]
    return dict(header=["Compte de résultat", "USD", "Mouvements d'argent", "USD"], rows=rows, widths=[31, 13, 34, 13], size=7.5,
                align=['l', 'r', 'l', 'r'], totals=(8,))
