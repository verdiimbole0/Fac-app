"""Données centrales du cas fil rouge (fictif et pédagogique).
MAKAO Distribution SARL : toutes les valeurs du livre proviennent de ce fichier.
Montants en USD sauf mention contraire. Taux pédagogique : 1 USD = 2 850 CDF (fictif, 31/12/2025)."""
from datetime import date, timedelta
from collections import OrderedDict, defaultdict

RATE = 2850  # CDF pour 1 USD, taux pédagogique fictif au 31/12/2025

# ---------------- Chapitre 1 : T4 2025 --------------------------------------
Q4 = OrderedDict(
    ventes=300_000, cout_marchandises=216_000, personnel=27_000, charges_ext=21_000,
    amortissements=6_000, interets=2_000)
Q4['resultat'] = Q4['ventes'] - sum(Q4[k] for k in ['cout_marchandises','personnel','charges_ext','amortissements','interets'])
Q4_CASH = OrderedDict(
    tresorerie_ouverture=70_000, creances_ouverture=84_000, creances_cloture=126_000,
    achats=240_000, stock_variation=24_000, dettes_f_ouverture=88_000, dettes_f_cloture=92_000,
    remboursement_emprunt=9_000, investissement=18_000)
Q4_CASH['encaissements_clients'] = Q4_CASH['creances_ouverture'] + Q4['ventes'] - Q4_CASH['creances_cloture']
Q4_CASH['paiements_fournisseurs'] = Q4_CASH['dettes_f_ouverture'] + Q4_CASH['achats'] - Q4_CASH['dettes_f_cloture']
Q4_CASH['decaissements'] = (Q4_CASH['paiements_fournisseurs'] + Q4['personnel'] + Q4['charges_ext'] + Q4['interets']
                            + Q4_CASH['remboursement_emprunt'] + Q4_CASH['investissement'])
Q4_CASH['variation'] = Q4_CASH['encaissements_clients'] - Q4_CASH['decaissements']
Q4_CASH['tresorerie_cloture'] = Q4_CASH['tresorerie_ouverture'] + Q4_CASH['variation']
assert Q4['cout_marchandises'] == Q4_CASH['achats'] - Q4_CASH['stock_variation']
BRIDGE = [("Résultat avant impôt du trimestre", Q4['resultat']),
          ("+ Amortissements (charge sans sortie d'argent)", Q4['amortissements']),
          ("- Hausse des créances clients", -(Q4_CASH['creances_cloture']-Q4_CASH['creances_ouverture'])),
          ("- Hausse des stocks", -Q4_CASH['stock_variation']),
          ("+ Hausse des dettes fournisseurs", Q4_CASH['dettes_f_cloture']-Q4_CASH['dettes_f_ouverture']),
          ("- Remboursement du capital de l'emprunt", -Q4_CASH['remboursement_emprunt']),
          ("- Achat d'un véhicule de livraison", -Q4_CASH['investissement'])]
assert sum(v for _, v in BRIDGE) == Q4_CASH['variation']

# ---------------- Chapitre 2 : diagnostic au 31/12/2025 ----------------------
DISPO = OrderedDict([
    ("Banque Alpha, compte USD", 11_400),
    ("Banque Alpha, compte CDF (3 420 000 CDF)", 3_420_000 / RATE),
    ("Caisse USD", 600),
    ("Caisse CDF (1 140 000 CDF)", 1_140_000 / RATE),
    ("Monnaie électronique (portefeuille mobile)", 1_400),
])
DISPO_TOTAL = sum(DISPO.values())
assert DISPO_TOTAL == Q4_CASH['tresorerie_cloture'] == 15_000

BUCKETS = ["Non échu", "1-30 j", "31-60 j", "61-90 j", "+90 j"]
CLIENTS = OrderedDict([
    ("Groupe scolaire Les Palmiers", [18_000, 9_000, 3_000, 0, 0]),
    ("Bâtir Kongo (BTP)",           [12_000, 6_000, 2_000, 0, 4_000]),
    ("Clinique Lumière",            [14_000, 6_000, 0, 0, 0]),
    ("Hôtel Fleuve Bleu",           [10_000, 5_000, 0, 0, 0]),
    ("ASBL Espoir Rural",           [8_000, 4_000, 0, 2_000, 0]),
    ("Transports Rapides (STR)",    [6_000, 2_000, 0, 0, 0]),
    ("Cabinet Nsimba & Associés",   [4_000, 2_000, 0, 0, 0]),
    ("Autres clients (23)",         [8_000, 1_000, 0, 0, 0]),
])
CREANCES_BUCKETS = [sum(v[i] for v in CLIENTS.values()) for i in range(5)]
CREANCES_TOTAL = sum(CREANCES_BUCKETS)
assert CREANCES_TOTAL == Q4_CASH['creances_cloture'] == 126_000
DSO_31DEC = CREANCES_TOTAL / Q4['ventes'] * 92  # jours (T4 = 92 jours)

FOURNISSEURS = OrderedDict([  # dettes au 31/12 : (montant, échéance)
    ("Papeteries Unies (échu le 20/12)", (12_000, date(2026,1,5))),
    ("Grossiste InfoPlus",              (40_000, date(2026,1,10))),
    ("Mobilier Express",                (22_000, date(2026,1,25))),
    ("Papeteries Unies",                (18_000, date(2026,1,25))),
])
DETTES_TOTAL = sum(v[0] for v in FOURNISSEURS.values())
assert DETTES_TOTAL == Q4_CASH['dettes_f_cloture'] == 92_000

FIXES = OrderedDict([  # charges récurrentes mensuelles décaissées
    ("Loyer (le 5)", 4_000), ("Autres charges externes (10 et 20)", 3_000),
    ("Cotisations sociales et impôt sur salaires (le 15)", 2_100),
    ("Échéance d'emprunt : 3 000 capital + 650 intérêts (le 20)", 3_650),
    ("Salaires nets (le 28)", 9_000)])
FIXES_TOTAL = sum(FIXES.values())  # 21 750
RESERVE_CIBLE = 22_000  # environ un mois de décaissements fixes

# ---------------- Chapitre 3 : prévisionnel janvier-juin 2026 ----------------
VENTES_2026 = OrderedDict([(1,95_000),(2,100_000),(3,105_000),(4,100_000),(5,105_000),(6,110_000)])
PROFIL_BASE = [0.20, 0.45, 0.30, 0.05]   # part encaissée en M, M+1, M+2, M+3
PROFIL_AMELIORE = [0.30, 0.50, 0.18, 0.02]
TAUX_ACHAT = 0.72
COLLECT_DAYS = [5, 12, 19, 26]
MOIS = {1:"Janvier",2:"Février",3:"Mars",4:"Avril",5:"Mai",6:"Juin",7:"Juillet",8:"Août",9:"Septembre",10:"Octobre",11:"Novembre",12:"Décembre"}
def de(m):
    n = MOIS[m].lower()
    return ("d'" if n[0] in "aeiouy" else "de ") + n

ENC_CAT = ["Créances au 31/12", "Ventes du mois (comptant)", "Ventes des mois précédents"]
DEC_CAT = ["Fournisseurs", "Salaires", "Cotisations et impôts sur salaires", "Loyer",
           "Autres charges externes", "Emprunt (capital + intérêts)", "Investissements",
           "Compte courant d'associé"]

def _spread(events, month, amount, cat, label, year=2026):
    """Répartit un encaissement mensuel en 4 tranches égales (5, 12, 19, 26)."""
    if month > 12: month, year = month-12, year+1
    q = round(amount/4, 2)
    parts = [q, q, q, round(amount-3*q, 2)]
    for d, p in zip(COLLECT_DAYS, parts):
        events.append((date(year, month, d), 'E', cat, label, p))

def build_events(profil=PROFIL_BASE, profil_from=1, existing=None, adjustments=None, months=6):
    ev = []
    # Créances existantes (calendrier prévisionnel)
    existing = existing or [  # (mois, montant, libellé)
        (1, 45_000, "Factures de décembre"), (2, 30_000, "Factures de décembre"), (3, 5_000, "Factures de décembre"),
        (1, 30_000, "Factures de novembre"), (2, 5_000, "Factures de novembre"),
        (1, 5_000, "Factures d'octobre"), (2, 2_000, "Facture de septembre (Espoir Rural)")]
    for m, a, lab in existing:
        _spread(ev, m, a, ENC_CAT[0], lab)
    for m, s in VENTES_2026.items():
        p = profil if m >= profil_from else PROFIL_BASE
        for k, share in enumerate(p):
            if m+k <= months:
                _spread(ev, m+k, s*share, ENC_CAT[1] if k == 0 else ENC_CAT[2], f"Ventes {de(m)}")
    # Fournisseurs existants
    for lab, (a, d) in [(k, (v[0], v[1])) for k, v in FOURNISSEURS.items()]:
        ev.append((d, 'D', DEC_CAT[0], lab, a))
    # Achats 2026 payés à M+1 (10 et 25)
    for m, s in VENTES_2026.items():
        if m+1 <= months:
            a = s*TAUX_ACHAT
            ev.append((date(2026, m+1, 10), 'D', DEC_CAT[0], f"Achats {de(m)} (50 %)", a/2))
            ev.append((date(2026, m+1, 25), 'D', DEC_CAT[0], f"Achats {de(m)} (50 %)", a/2))
    for m in range(1, months+1):
        ev.append((date(2026, m, 5), 'D', DEC_CAT[3], "Loyer", 4_000))
        ev.append((date(2026, m, 10), 'D', DEC_CAT[4], "Charges externes", 1_500))
        ev.append((date(2026, m, 20), 'D', DEC_CAT[4], "Charges externes", 1_500))
        ev.append((date(2026, m, 15), 'D', DEC_CAT[2], "Cotisations et IPR", 2_100))
        ev.append((date(2026, m, 20), 'D', DEC_CAT[5], "Échéance d'emprunt", 3_650))
        ev.append((date(2026, m, 28), 'D', DEC_CAT[1], "Salaires", 9_000))
    ev.append((date(2026, 1, 30), 'D', DEC_CAT[7], "Remboursement compte courant de la gérante", 5_000))
    ev.append((date(2026, 3, 16), 'D', DEC_CAT[6], "Renouvellement matériel informatique", 6_000))
    for adj in (adjustments or []):
        adj(ev)
    return sorted(ev, key=lambda e: (e[0], e[1] == 'E'))  # sorties avant entrées le même jour (prudence)

OPENING = 15_000

def monthly(ev, months=6):
    rows = OrderedDict()
    bal = OPENING
    for m in range(1, months+1):
        enc = defaultdict(float); dec = defaultdict(float)
        for d, t, c, l, a in ev:
            if d.year == 2026 and d.month == m:
                (enc if t == 'E' else dec)[c] += a
        E = sum(enc.values()); D = sum(dec.values())
        rows[m] = dict(ouverture=bal, enc=dict(enc), dec=dict(dec), E=E, D=D, cloture=bal+E-D)
        bal += E-D
    return rows

WEEK1 = date(2026, 1, 5)
def weekly(ev, n=13, opening=OPENING, start=WEEK1):
    rows = []
    bal = opening
    for w in range(n):
        a = start + timedelta(days=7*w); b = a + timedelta(days=6)
        enc = defaultdict(float); dec = defaultdict(float); low = bal; run = bal
        for d, t, c, l, amt in ev:
            if a <= d <= b:
                (enc if t == 'E' else dec)[c] += amt
                run += amt if t == 'E' else -amt
                low = min(low, run)
        E = sum(enc.values()); D = sum(dec.values())
        rows.append(dict(sem=w+1, debut=a, fin=b, ouverture=bal, enc=dict(enc), dec=dict(dec), E=E, D=D,
                         cloture=bal+E-D, plus_bas=low))
        bal += E-D
    return rows

def daily_min(ev, until=date(2026, 6, 30)):
    bal = OPENING; low = (bal, date(2026, 1, 1))
    for d, t, c, l, a in ev:
        if d > until: break
        bal += a if t == 'E' else -a
        if bal < low[0]: low = (bal, d)
    return low

EV_BASE = build_events()
M_BASE = monthly(EV_BASE)
W_BASE = weekly(EV_BASE)

if __name__ == "__main__":
    print("Q4", dict(Q4), dict(Q4_CASH))
    print("DSO", DSO_31DEC)
    for m, r in M_BASE.items():
        print(MOIS[m], round(r['ouverture']), round(r['E']), round(r['D']), round(r['cloture']))
    for r in W_BASE:
        print(r['sem'], r['debut'], round(r['ouverture']), round(r['E']), round(r['D']), round(r['cloture']), round(r['plus_bas']))
    print("min", daily_min(EV_BASE))

# ---------------- Chapitre 4 : actions sur les encaissements -----------------
EXISTING_AMELIORE = [
    (1, 45_000, "Factures de décembre"), (2, 30_000, "Factures de décembre"), (3, 5_000, "Factures de décembre"),
    (1, 35_000, "Factures de novembre (relance)"),
    (1, 5_000, "Factures d'octobre"), (1, 2_000, "Facture de septembre (Espoir Rural)"),
    (3, 2_000, "Bâtir Kongo : accord sur le litige (50 %)")]
EV_ENC = build_events(profil=PROFIL_AMELIORE, profil_from=2, existing=EXISTING_AMELIORE)
M_ENC = monthly(EV_ENC); W_ENC = weekly(EV_ENC)

# ---------------- Chapitre 5 : plan de paiement raisonné ---------------------
def _move(label_start, old, new_parts):
    def f(ev):
        for i, e in enumerate(ev):
            if e[3].startswith(label_start) and e[0] == old:
                tot = e[4]; ev.pop(i)
                for d, share in new_parts:
                    ev.append((d, e[1], e[2], e[3] + (" (échéancier)" if len(new_parts) > 1 else " (reporté)"), tot*share))
                return
        raise ValueError(label_start)
    return f
ADJ_DEC = [
    _move("Papeteries Unies (échu", date(2026,1,5), [(date(2026,1,5),0.5),(date(2026,1,19),0.5)]),
    _move("Grossiste InfoPlus", date(2026,1,10), [(date(2026,1,10),0.5),(date(2026,2,6),0.5)]),
    _move("Remboursement compte courant", date(2026,1,30), [(date(2026,6,30),1)]),
    _move("Renouvellement matériel", date(2026,3,16), [(date(2026,5,18),1)]),
]
EV_PLAN = build_events(profil=PROFIL_AMELIORE, profil_from=2, existing=EXISTING_AMELIORE, adjustments=ADJ_DEC)
M_PLAN = monthly(EV_PLAN); W_PLAN = weekly(EV_PLAN)

if __name__ == "__main__":
    for name, M, W, EV in [("ENC", M_ENC, W_ENC, EV_ENC), ("PLAN", M_PLAN, W_PLAN, EV_PLAN)]:
        print("==", name)
        for m, r in M.items(): print(MOIS[m], round(r['E']), round(r['D']), round(r['cloture']))
        for r in W: print(r['sem'], r['debut'], round(r['E']), round(r['D']), round(r['cloture']), round(r['plus_bas']))
        print("min", daily_min(EV))

# ---------------- Janvier réalisé (chapitres 3, 7, 8) -------------------------
JAN_PREVU_ENC = OrderedDict([("Créances au 31/12", 87_000), ("Ventes du mois (comptant)", 19_000)])
JAN_REEL_ENC = OrderedDict([("Créances au 31/12", 83_000), ("Ventes du mois (comptant)", 18_400)])
JAN_PREVU_DEC = OrderedDict([("Fournisseurs", 72_000), ("Salaires", 9_000), ("Cotisations et impôts sur salaires", 2_100),
    ("Loyer", 4_000), ("Autres charges externes", 3_000), ("Emprunt (capital + intérêts)", 3_650)])
JAN_REEL_DEC = OrderedDict([("Fournisseurs", 76_800), ("Salaires", 9_000), ("Cotisations et impôts sur salaires", 2_100),
    ("Loyer", 4_000), ("Autres charges externes", 4_400), ("Emprunt (capital + intérêts)", 3_650)])
JAN_VENTES_REELLES = 92_000
assert sum(JAN_PREVU_ENC.values()) == round(M_PLAN[1]['E']) and sum(JAN_PREVU_DEC.values()) == round(M_PLAN[1]['D'])
JAN = dict(prevu_E=sum(JAN_PREVU_ENC.values()), reel_E=sum(JAN_REEL_ENC.values()),
           prevu_D=sum(JAN_PREVU_DEC.values()), reel_D=sum(JAN_REEL_DEC.values()))
JAN['prevu_C'] = OPENING + JAN['prevu_E'] - JAN['prevu_D']
JAN['reel_C'] = OPENING + JAN['reel_E'] - JAN['reel_D']
DOUBLE_PAIEMENT = 4_800; REPARATION = 1_400
# Rapprochement bancaire Banque Alpha USD au 31/01/2026
DISPO_31JAN = OrderedDict([("Banque Alpha, compte USD", None), ("Banque Alpha, compte CDF (2 280 000 CDF)", 2_280_000/RATE),
    ("Caisse USD et CDF (450 USD + 855 000 CDF)", 450 + 855_000/RATE), ("Monnaie électronique", 1_900)])
DISPO_31JAN["Banque Alpha, compte USD"] = JAN['reel_C'] - sum(v for v in DISPO_31JAN.values() if v)
REC = dict(livre=DISPO_31JAN["Banque Alpha, compte USD"], cheque_non_presente=5_000, remise_non_creditee=3_500, frais=110)
REC['banque'] = REC['livre'] + REC['cheque_non_presente'] - REC['remise_non_creditee'] - REC['frais']
REC['rapproche'] = REC['livre'] - REC['frais']
assert REC['rapproche'] == REC['banque'] - REC['cheque_non_presente'] + REC['remise_non_creditee']
TRESO_31JAN = JAN['reel_C'] - REC['frais']
CREANCES_31JAN = [73_600, 33_000, 6_000, 0, 4_000]
assert sum(CREANCES_31JAN) == CREANCES_TOTAL + JAN_VENTES_REELLES - sum(JAN_REEL_ENC.values())
DETTES_31JAN = DETTES_TOTAL + JAN_VENTES_REELLES*TAUX_ACHAT - (JAN_REEL_DEC["Fournisseurs"] - DOUBLE_PAIEMENT)
DSO_31JAN = sum(CREANCES_31JAN) / (100_000 + 100_000 + JAN_VENTES_REELLES) * 92
DPO_31JAN = DETTES_31JAN / (80_000 + 80_000 + JAN_VENTES_REELLES*TAUX_ACHAT) * 92

# Reprévision au 1er février
def reprevision():
    ev = [e for e in EV_PLAN if e[0] >= date(2026, 2, 1)]
    out = []
    for d, t, c, l, a in ev:
        if l == "Ventes de janvier":
            a = a * JAN_VENTES_REELLES / VENTES_2026[1]
        if l.startswith("Achats de janvier"):
            a = JAN_VENTES_REELLES * TAUX_ACHAT / 2
            if d == date(2026, 2, 25):
                a -= DOUBLE_PAIEMENT; l = l + " net de l'avoir Mobilier Express"
        if l == "Factures de décembre" and d == date(2026, 2, 5):
            a -= 2_000  # Clinique Lumière a payé en avance en janvier
        out.append((d, t, c, l, a))
    out.append((date(2026, 2, 12), 'E', ENC_CAT[0], "Groupe scolaire Les Palmiers (retard de janvier)", 6_000))
    return sorted(out, key=lambda e: (e[0], e[1] == 'E'))
EV_REPREV = reprevision()
W_REPREV = weekly(EV_REPREV, n=9, opening=TRESO_31JAN, start=date(2026, 2, 2))

def monthly_from(ev, opening, months):
    rows = OrderedDict(); bal = opening
    for m in months:
        E = sum(a for d,t,c,l,a in ev if d.month == m and t == 'E'); D = sum(a for d,t,c,l,a in ev if d.month == m and t == 'D')
        rows[m] = dict(ouverture=bal, E=E, D=D, cloture=bal+E-D); bal += E-D
    return rows
M_REPREV = monthly_from(EV_REPREV, TRESO_31JAN, [2,3,4,5,6])

def low_from(ev, opening, until):
    bal = opening; low = (bal, None)
    for d,t,c,l,a in ev:
        if d > until: break
        bal += a if t == 'E' else -a
        if bal < low[0]: low = (bal, d)
    return low

if __name__ == "__main__":
    print("JAN", JAN, "rec", REC, "treso31", TRESO_31JAN, "dispo", {k: round(v,2) for k,v in DISPO_31JAN.items()})
    print("DSO31", DSO_31JAN, "DPO31", DPO_31JAN, "dettes31", DETTES_31JAN)
    for r in W_REPREV: print(r['sem'], r['debut'], round(r['E']), round(r['D']), round(r['cloture']), round(r['plus_bas']))
    for m,r in M_REPREV.items(): print(MOIS[m], round(r['E']), round(r['D']), round(r['cloture']))
    print("low", low_from(EV_REPREV, TRESO_31JAN, date(2026,6,30)))

# ---------------- Chapitre 6 : financement du besoin de février ---------------
BESOIN = dict(montant=round(-low_from(EV_REPREV, TRESO_31JAN, date(2026,2,11))[0]), jours=2, plafond=20_000)
EV_DECISION = sorted([((date(2026,2,13),)+e[1:]) if (e[0]==date(2026,2,10) and e[3].startswith("Achats de janvier")) else e
                      for e in EV_REPREV], key=lambda e: (e[0], e[1] == 'E'))
LOW_DECISION = low_from(EV_DECISION, TRESO_31JAN, date(2026,6,30))
def interet(c, taux, j): return c*taux*j/360
def couts_financement(besoin, jours, second=0, jours2=0, plafond=20_000):
    out = OrderedDict()
    i = interet(besoin,.18,jours)+interet(second,.18,jours2); out["Découvert autorisé"] = dict(
        hyp="18 %/an ; commission de plus fort découvert 0,10 % ; frais d'autorisation 100 USD/an",
        interets=i, frais=0.001*besoin+100)
    i = interet(besoin,.15,jours)+interet(second,.15,jours2); out["Facilité de caisse"] = dict(
        hyp="15 %/an ; frais d'ouverture 1 % du plafond (200 USD), valable 12 mois", interets=i, frais=0.01*plafond)
    out["Crédit de trésorerie 1 mois"] = dict(hyp="13 %/an sur 20 000 USD pendant 30 jours ; frais de dossier 1 %",
        interets=interet(plafond,.13,30), frais=0.01*plafond)
    out["Avance de la gérante (compte courant)"] = dict(hyp="0 % ; convention écrite et validation de l'assemblée",
        interets=0, frais=0)
    out["Report négocié de 3 jours (fournisseur)"] = dict(hyp="aucun coût financier ; accord écrit du fournisseur",
        interets=0, frais=0)
    for v in out.values(): v['total'] = v['interets'] + v['frais']
    return out
FIN_COURT = couts_financement(BESOIN['montant'], 2)
FIN_30J = OrderedDict()
for nom, taux, frais in [("Découvert autorisé", .18, 0.001*20_000+100), ("Facilité de caisse", .15, 200),
                         ("Crédit de trésorerie 1 mois", .13, 200)]:
    i = interet(20_000, taux, 30); FIN_30J[nom] = dict(interets=i, frais=frais, total=i+frais,
                                                      teg=(i+frais)/20_000*360/30)
AFFACT = dict(factures=15_000, avance=0.8*15_000, commission=0.015*15_000, interets=interet(12_000,.14,30))
AFFACT['total'] = AFFACT['commission'] + AFFACT['interets']

# ---------------- Chapitre 9 : perte du principal client ---------------------
PART_PALMIERS = 0.24
OPEN_AVR = M_REPREV[3]['cloture']
SCEN = OrderedDict([
    ("Optimiste", dict(pertes={4:.24, 5:.12, 6:.12}, profil=PROFIL_AMELIORE, retard=0.0, litige=0.0)),
    ("Réaliste", dict(pertes={4:.24, 5:.24, 6:.24}, profil=PROFIL_AMELIORE, retard=1.0, litige=0.0)),
    ("Pessimiste", dict(pertes={4:.24, 5:.24, 6:.24}, profil=PROFIL_BASE, retard=0.5, litige=0.5)),
])
def scenario(p, mesures=False):
    ev = []
    for d,t,c,l,a in EV_REPREV:
        if d < date(2026,4,1): continue
        if l in ("Ventes d'avril","Ventes de mai","Ventes de juin") or l.startswith("Achats d'avril") \
           or l.startswith("Achats de mai"):
            continue
        if t == 'E' and c == ENC_CAT[2]:  # encaissements de ventes antérieures : part Palmiers
            pal = a*PART_PALMIERS
            ev.append((d,t,c,l,a-pal))
            ev.append((d,t,c,"Palmiers (normal)", pal*(1-p['retard']-p['litige'])))
            if p['retard']:
                nd = date(2026, d.month+1, d.day) if d.month < 12 else d
                if nd <= date(2026,6,30): ev.append((nd,t,c,"Palmiers (retard)", pal*p['retard']))
            continue
        ev.append((d,t,c,l,a))
    for m in (4,5,6):
        s = VENTES_2026[m]*(1-p['pertes'][m])
        for k, share in enumerate(p['profil']):
            if m+k <= 6: _spread(ev, m+k, s*share, ENC_CAT[1] if k==0 else ENC_CAT[2], f"Ventes {m}")
        if m+1 <= 6:
            a = s*TAUX_ACHAT - (10_000 if (mesures and m == 4) else 0)
            ev.append((date(2026,m+1,10),'D',DEC_CAT[0],f"Achats {m}",a/2)); ev.append((date(2026,m+1,25),'D',DEC_CAT[0],f"Achats {m}",a/2))
    if mesures:
        new = []
        for e in ev:
            if e[3].startswith("Renouvellement matériel") or e[3].startswith("Remboursement compte courant"): continue
            if e[3] == "Charges externes": e = (e[0],e[1],e[2],e[3],e[4]-250)
            new.append(e)
        ev = new
    return sorted(ev, key=lambda e:(e[0], e[1]=='E'))
SCEN_RES = OrderedDict()
for nom, p in SCEN.items():
    ev = scenario(p); SCEN_RES[nom] = dict(m=monthly_from(ev, OPEN_AVR, [4,5,6]), low=low_from(ev, OPEN_AVR, date(2026,6,30)))
EV_SCEN_MES = scenario(SCEN["Réaliste"], mesures=True)
SCEN_MES = dict(m=monthly_from(EV_SCEN_MES, OPEN_AVR, [4,5,6]), low=low_from(EV_SCEN_MES, OPEN_AVR, date(2026,6,30)))
EV_SCEN_PES_MES = scenario(SCEN["Pessimiste"], mesures=True)
SCEN_PES_MES = dict(m=monthly_from(EV_SCEN_PES_MES, OPEN_AVR, [4,5,6]), low=low_from(EV_SCEN_PES_MES, OPEN_AVR, date(2026,6,30)))
BASE_AVR = dict(m=monthly_from([e for e in EV_REPREV if e[0]>=date(2026,4,1)], OPEN_AVR, [4,5,6]),
                low=low_from([e for e in EV_REPREV if e[0]>=date(2026,4,1)], OPEN_AVR, date(2026,6,30)))

if __name__ == "__main__":
    print("BESOIN", BESOIN, "LOWDEC", LOW_DECISION, "LOWREPREV", low_from(EV_REPREV, TRESO_31JAN, date(2026,6,30)))
    for k,v in FIN_COURT.items(): print(k, {a: round(b,2) for a,b in v.items() if a!='hyp'})
    for k,v in FIN_30J.items(): print(k, {a: round(b,4) for a,b in v.items()})
    print("AFFACT", AFFACT, "OPEN_AVR", OPEN_AVR)
    print("BASE", {m: round(r['cloture']) for m,r in BASE_AVR['m'].items()}, BASE_AVR['low'])
    for n,r in SCEN_RES.items(): print(n, {m:(round(x['E']),round(x['D']),round(x['cloture'])) for m,x in r['m'].items()}, round(r['low'][0]), r['low'][1])
    print("MES", {m:(round(x['E']),round(x['D']),round(x['cloture'])) for m,x in SCEN_MES['m'].items()}, SCEN_MES['low'])
    print("PESMES", {m:round(x['cloture']) for m,x in SCEN_PES_MES['m'].items()}, SCEN_PES_MES['low'])

# ---------------- Chapitre 10 : ASBL Mains Unies pour l'Éducation (fictive) ----
ASBL_BUDGET = OrderedDict([("Personnel du projet", 18_000), ("Activités (formations, kits de lecture)", 20_000),
    ("Équipement (bibliothèques mobiles)", 6_000), ("Suivi-évaluation", 2_500), ("Frais administratifs (7 %)", 3_500)])
assert sum(ASBL_BUDGET.values()) == 50_000
ASBL_ACT = {2:2000,3:3000,4:2000,5:2000,6:1000,7:1000,8:1000,9:3000,10:2000,11:2000,12:1000}
assert sum(ASBL_ACT.values()) == 20_000
def asbl_depenses(m):
    d = OrderedDict([("Personnel", 1_500), ("Activités", ASBL_ACT.get(m, 0)), ("Équipement", 6_000 if m == 3 else 0),
        ("Suivi-évaluation", {6:1_000, 12:1_500}.get(m, 0)), ("Frais administratifs", 875 if m in (3,6,9,12) else 0)])
    return d
assert sum(sum(asbl_depenses(m).values()) for m in range(1,13)) == 50_000
def asbl_tableau(tranches):
    rows = []; bal = 0
    for m in range(1, 13):
        rec = tranches.get(m, 0); dep = sum(asbl_depenses(m).values())
        rows.append(dict(m=m, ouverture=bal, recettes=rec, depenses=dep, cloture=bal+rec-dep)); bal += rec-dep
    return rows
ASBL_PREVU = asbl_tableau({1:20_000, 4:20_000})   # tranche 2 attendue le 30 avril
ASBL_REEL = asbl_tableau({1:20_000, 6:20_000})    # tranche 2 reçue le 15 juin
ASBL_COMPTE_31MARS = OrderedDict([("Projet « Lire pour réussir » (fonds affectés)", ASBL_PREVU[2]['cloture']),
    ("Projet « Eau potable » (fonds affectés, autre bailleur)", 8_400), ("Fonds propres non affectés (cotisations, dons libres)", 12_000)])

# ---------------- Chapitre 12 : mission au 30 juin 2026 -------------------------
C12_DISPO = OrderedDict([("Banque Alpha, compte USD", 52_300), ("Banque Alpha, compte CDF (5 700 000 CDF)", 5_700_000/RATE),
    ("Caisse Kinshasa (solde comptable)", 1_100), ("Monnaie électronique", 3_500)])
C12_CAISSE_COMPTEE = 1_040
C12_CREANCES = [64_000, 18_000, 9_000, 3_000, 4_000]
C12_DETTES = OrderedDict([("InfoPlus, achats de mai (délai 45 jours)", (9_800, date(2026,7,10))),
    ("Fournisseurs, achats de juin (50 %)", (30_600, date(2026,7,10))), ("Fournisseurs, achats de juin (50 %) ", (30_600, date(2026,7,25)))])
C12_VENTES_KIN = OrderedDict([(7, 78_000), (8, 80_000), (9, 83_000)])
C12_ONG = 12_000; C12_AGENCE = {9: 15_000}
C12_FIXES_KIN = 21_250
def c12_events(decisions=True):
    ev = []
    def add(d, t, c, l, a): ev.append((d, t, c, l, a))
    for m, a, l in [(7,44_800,"Créances non échues (70 %)"),(8,19_200,"Créances non échues (30 %)"),(7,18_000,"Créances 1-30 j"),
                    (8,9_000,"Créances 31-60 j"),(9,1_500,"Créances 61-90 j (50 %)")]:
        _spread(ev, m, a, "Créances au 30/06", l)
    for m, s in C12_VENTES_KIN.items():
        for k, sh in enumerate(PROFIL_AMELIORE):
            if m+k <= 9: _spread(ev, m+k, s*sh, "Ventes Kinshasa", f"Ventes {de(m)}")
    for m in (7, 8, 9):
        if m+2 <= 9: add(date(2026, m+2, 26), 'E', "ONG Santé Plus", f"Facture {de(m)} (60 jours)", C12_ONG)
    add(date(2026,9,19), 'E', "Agence Lubumbashi", "Ventes de septembre (comptant 60 %)", 9_000)
    for lab,(a,d) in C12_DETTES.items(): add(d,'D',"Fournisseurs",lab.strip(),a)
    for m in (7, 8):
        s = C12_VENTES_KIN[m] + C12_ONG + C12_AGENCE.get(m, 0)
        add(date(2026,m+1,10),'D',"Fournisseurs",f"Achats {de(m)} (50 %)", s*TAUX_ACHAT/2)
        add(date(2026,m+1,25),'D',"Fournisseurs",f"Achats {de(m)} (50 %)", s*TAUX_ACHAT/2)
    for m in (7, 8, 9):
        add(date(2026,m,5),'D',"Loyer","Loyer Kinshasa",4_000)
        add(date(2026,m,10),'D',"Charges externes","Charges externes",1_250); add(date(2026,m,20),'D',"Charges externes","Charges externes",1_250)
        add(date(2026,m,15),'D',"Cotisations et impôts sur salaires","Cotisations et IPR",2_100)
        add(date(2026,m,20),'D',"Emprunt","Échéance d'emprunt",3_650)
        add(date(2026,m,28),'D',"Salaires","Salaires Kinshasa",9_000)
        if m >= 8:
            add(date(2026,m,5),'D',"Loyer","Loyer agence",1_200); add(date(2026,m,20),'D',"Charges externes","Charges agence",500)
            add(date(2026,m,28),'D',"Salaires","Salaires agence",1_800)
    add(date(2026,7,31),'D',"Impôts","Solde d'impôt sur le résultat 2025 (hypothèse du cas)",7_500)
    add(date(2026,8,3),'D',"Investissements","Aménagement agence Lubumbashi",15_000)
    add(date(2026,8,17),'D',"Fournisseurs","Stock initial agence (comptant)",20_000)
    if decisions:
        add(date(2026,9,28),'D',"Compte courant d'associé","Remboursement compte courant (après validation)",5_000)
        add(date(2026,9,21),'D',"Investissements","Matériel informatique (si réserve > 22 000)",6_000)
    return sorted(ev, key=lambda e: (e[0], e[1] == 'E'))
C12_OPEN = sum(C12_DISPO.values()) - (C12_DISPO["Caisse Kinshasa (solde comptable)"] - C12_CAISSE_COMPTEE) - 450
C12_EV = c12_events()
C12_W = weekly(C12_EV, n=13, opening=C12_OPEN, start=date(2026, 6, 29))
C12_M = monthly_from(C12_EV, C12_OPEN, [7, 8, 9])

if __name__ == "__main__":
    for r in ASBL_PREVU: print('P', r)
    for r in ASBL_REEL: print('R', r['m'], r['cloture'])
    print(ASBL_COMPTE_31MARS)
    print("C12_OPEN", C12_OPEN)
    for r in C12_W: print(r['sem'], r['debut'], round(r['E']), round(r['D']), round(r['cloture']), round(r['plus_bas']))
    for m,r in C12_M.items(): print(MOIS[m], round(r['E']), round(r['D']), round(r['cloture']))

C12_EV_SANS = c12_events(decisions=False)
C12_W_SANS = weekly(C12_EV_SANS, n=13, opening=C12_OPEN, start=date(2026, 6, 29))
def c12_mesures(ev):
    out = []
    for e in ev:
        if e[3] == "Stock initial agence (comptant)":
            out.append((e[0], e[1], e[2], "Stock initial agence, 1re livraison", 10_000))
            out.append((date(2026,9,14), e[1], e[2], "Stock initial agence, 2e livraison", 10_000)); continue
        out.append(e)
    out.append((date(2026,7,15),'E',"ONG Santé Plus","Avance de démarrage négociée (20 % du 1er trimestre)", 7_200))
    out = [((date(2026,9,26),'E','ONG Santé Plus',e[3]+" (net de l'avance)", e[4]-7_200) if e[3].startswith("Facture de juillet") else e) for e in out]
    return sorted(out, key=lambda e: (e[0], e[1] == 'E'))
C12_EV_MES = c12_mesures(C12_EV_SANS)
C12_W_MES = weekly(C12_EV_MES, n=13, opening=C12_OPEN, start=date(2026, 6, 29))
C12_M_MES = monthly_from(C12_EV_MES, C12_OPEN, [7, 8, 9])
if __name__ == "__main__":
    for nm, W in [("SANS", C12_W_SANS), ("MES", C12_W_MES)]:
        print(nm, [(r['sem'], round(r['cloture']), round(r['plus_bas'])) for r in W])
    print({m: round(r['cloture']) for m,r in C12_M_MES.items()})
