# -*- coding: utf-8 -*-
"""Figures de la partie III, construites à partir des jeux de données fictifs de MCC."""
import csv, datetime as dt
from collections import Counter, defaultdict
import numpy as np
from fig_lib import *

D = ROOT / "03_EXERCICES_ET_DONNEES" / "CSV"
SRC = "Données fictives MCC (03_EXERCICES_ET_DONNEES). Graphique réalisé pour cet ouvrage."

def lire(nom):
    with open(D / nom, encoding="utf-8") as f:
        lignes = [l for l in f if not l.startswith("#")]
    return list(csv.DictReader(lignes, delimiter=";"))

def num(x):
    try: return float(str(x).replace(",", "."))
    except ValueError: return None

def pied(fig, txt=SRC):
    fig.text(0.5, -0.03, txt, ha="center", fontsize=7.6, style="italic", color=MID)

def workflow(name, titre, etapes, couleurs=None, sous=None, w=11.5, note_txt=None):
    n = len(etapes); fig, ax = canvas(w, 4.6, 115, 46); title(ax, titre, y=43.5, fs=12)
    bw = (111 - (n - 1) * 2.4) / n
    for i, (h, d) in enumerate(etapes):
        x = 2 + i * (bw + 2.4); c = (couleurs or [NAVY] * n)[i]
        box(ax, x, 25, bw, 10, h, fc=c, ec=c, color="white", bold=True, fs=8.8)
        ax.text(x + bw / 2, 15.5, d, ha="center", va="center", fontsize=7.6, color=INK)
        if i < n - 1: arrow(ax, (x + bw, 30), (x + bw + 2.4, 30), color=GOLD, lw=2)
    if note_txt: note(ax, note_txt, y=4)
    return save(fig, name)

H, C = GREEN, TURQ  # étapes humaines / assistées

def f17_2():
    return workflow("fig17_2_workflow_exploration", "Exploration : du terrain au rapport, avec Claude en appui documentaire",
        [("Collecte terrain", "observations,\nlogs, photos\n(géologue)"), ("Saisie & QA/QC", "bases de données,\nanalyses labo,\ncontrôles"),
         ("Structuration", "Claude : tableaux,\nrésumés de logs,\ncontrôles de cohérence"), ("Interprétation", "modèle géologique,\nhypothèses\n(géologue)"),
         ("Rédaction", "Claude : premier jet\ndu rapport, figures\nà partir des données"), ("Revue & signature", "personne\ncompétente")],
        [H, H, C, H, C, H], note_txt="Vert : étapes humaines — turquoise : étapes assistées par Claude. Illustration réalisée pour cet ouvrage.")

def f18_1():
    rows = lire("MCC_sondages_analyses.csv")
    cu = [num(r["Cu_pct"]) for r in rows if num(r["Cu_pct"]) is not None and num(r["Cu_pct"]) <= 100]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2))
    a1.hist(cu, bins=40, color=NAVY, edgecolor="white"); a1.axvline(0.8, color=RED, ls="--", lw=1.5)
    a1.text(0.85, a1.get_ylim()[1] * 0.85, "coupure\n0,8 % Cu", color=RED, fontsize=8)
    a1.set_title("Distribution des teneurs en Cu (échantillons)", fontsize=10.5); a1.set_xlabel("Cu (%)"); a1.set_ylabel("Nombre d'échantillons")
    style_axes(a1)
    co = [(num(r["Cu_pct"]), num(r["Co_pct"])) for r in rows if num(r["Cu_pct"]) not in (None,) and num(r["Co_pct"]) is not None]
    x = [a for a, b in co if a <= 100]; y = [b for a, b in co if a <= 100]
    a2.scatter(x, y, s=8, color=TURQ, alpha=0.6)
    out = [(a, b) for a, b in co if b > 1.0 and a <= 100]
    for a, b in out:
        a2.scatter([a], [b], s=60, facecolor="none", edgecolor=RED, lw=1.6); a2.annotate("valeur aberrante\n(à vérifier)", (a, b), xytext=(a + 0.6, b - 0.3), fontsize=7.5, color=RED)
    a2.set_title("Relation Cu – Co (échantillons)", fontsize=10.5); a2.set_xlabel("Cu (%)"); a2.set_ylabel("Co (%)"); style_axes(a2)
    fig.tight_layout(); pied(fig, "La valeur Cu = 112 % (erreur de saisie) est exclue du graphique ; la valeur de Co ×10 est entourée. " + SRC)
    return save(fig, "fig18_1_teneurs_sondages", "GRAPHIQUES")

def f18_2():
    rows = lire("MCC_qaqc_standards_blancs.csv")
    fig, (ax, ab) = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw=dict(width_ratios=[1.6, 1]), layout="constrained")
    crm = [r for r in rows if num(r["valeur_certifiee_Cu_pct"]) > 0]
    z = [(num(r["valeur_mesuree_Cu_pct"]) - num(r["valeur_certifiee_Cu_pct"])) / (0.025 * num(r["valeur_certifiee_Cu_pct"])) for r in crm]
    ax.plot(range(1, len(z) + 1), z, "o-", color=NAVY, ms=4.5, lw=1)
    for k, c in [(2, ORANGE), (3, RED)]:
        for sg in (1, -1): ax.axhline(sg * k, color=c, ls="--", lw=1.1)
    ax.axhline(0, color=GREEN, lw=1.2)
    for i, v in enumerate(z):
        if abs(v) > 3:
            ax.scatter([i + 1], [v], s=150, facecolor="none", edgecolor=RED, lw=2)
            ax.annotate(crm[i]["id"] + " hors tolérance", (i + 1, v), xytext=(i + 2, v - 0.6), fontsize=8, color=RED)
    ax.set_ylabel("Écart normalisé (nombre d'écarts-types)"); ax.set_xlabel("Ordre d'insertion des standards certifiés")
    ax.set_title("Standards certifiés (fictifs) : écart à la valeur certifiée", fontsize=10); style_axes(ax)
    bl = [r for r in rows if num(r["valeur_certifiee_Cu_pct"]) == 0]
    bv = [num(r["valeur_mesuree_Cu_pct"]) for r in bl]
    ab.bar(range(1, len(bv) + 1), bv, color=[RED if v > 0.05 else TURQ for v in bv])
    ab.axhline(0.05, color=RED, ls="--", lw=1.1); ab.text(0.6, 0.055, "seuil d'alerte (exercice)", color=RED, fontsize=7.5)
    for i, v in enumerate(bv):
        if v > 0.05: ab.annotate(bl[i]["id"] + " : contamination ?", (i + 1, v), xytext=(max(1, i - 3), v * 0.85), fontsize=8, color=RED)
    ab.set_title("Blancs : Cu mesuré (%)", fontsize=10); ab.set_xlabel("Ordre d'insertion des blancs"); style_axes(ab)
    pied(fig, "Tolérances de l'exercice : ± 3 écarts-types (2,5 % relatif) ; blancs < 0,05 % Cu. " + SRC)
    return save(fig, "fig18_2_carte_controle_qaqc", "GRAPHIQUES")

def f19_2():
    rows = lire("MCC_production_journaliere_S1_2026.csv")
    m = defaultdict(float)
    for r in rows: m[r["date"][:7]] += num(r["minerai_traite_t"]) / 1000
    mois = sorted(m); vals = [m[k] for k in mois]
    fig, ax = plt.subplots(figsize=(9.5, 4.2))
    ax.bar([k[5:] for k in mois], vals, color=[TURQ if v >= 195 else ORANGE for v in vals], width=0.6)
    ax.axhline(200, color=RED, ls="--", lw=1.3); ax.text(5.45, 201.5, "budget 200 kt", color=RED, fontsize=8.5, ha="right")
    for i, v in enumerate(vals): ax.text(i, v + 1.5, f"{v:.0f}", ha="center", fontsize=8.5)
    ax.set_ylim(0, 230); ax.set_ylabel("Minerai traité (kt)"); ax.set_xlabel("Mois 2026")
    ax.set_title("Minerai traité par mois, premier semestre 2026 (somme des données journalières)", fontsize=10.5)
    style_axes(ax); pied(fig, "Les mois de saison des pluies sont pénalisés ; avril compte une journée manquante (anomalie volontaire). " + SRC)
    return save(fig, "fig19_2_minerai_traite_mensuel", "GRAPHIQUES")

def f20_2():
    fig, ax = canvas(11, 5.6, 110, 56); title(ax, "Cycle forage-minage : ce que Claude peut faire… et ce qu'il ne fait pas", y=53.5, fs=12)
    et = ["Conception\ndu tir", "Forage", "Chargement\ndes trous", "Tir et\nsécurisation", "Contrôle\npost-tir", "Retour\nd'expérience"]
    for i, e in enumerate(et):
        x = 2 + i * 18; c = RED if i in (0, 2, 3) else NAVY
        box(ax, x, 33, 16, 10, e, fc=c, ec=c, color="white", bold=True, fs=8.8)
        if i < 5: arrow(ax, (x + 16, 38), (x + 18, 38), color=GOLD, lw=2)
    box(ax, 2, 4, 52, 24, "", fc=LIGHTTURQ, ec=TURQ)
    ax.text(28, 25, "Claude peut aider à…", ha="center", fontsize=10, fontweight="bold", color=TURQ)
    ax.text(4, 15, "• structurer les rapports de tir et de poste\n• synthétiser les mesures de vibrations validées\n• préparer les check-lists et causeries\n"
            "• analyser l'historique (fragmentation, ratés)\n• rédiger les retours d'expérience", fontsize=8.4, va="center")
    box(ax, 56, 4, 52, 24, "", fc=LIGHTRED, ec=RED)
    ax.text(82, 25, "Claude ne fait jamais…", ha="center", fontsize=10, fontweight="bold", color=RED)
    ax.text(58, 15, "• concevoir ou valider un plan de tir\n• fixer charges, retards, distances de sécurité\n• autoriser un tir, lever une évacuation\n"
            "• gérer un raté ou un explosif non détoné\n• décider des distances aux riverains", fontsize=8.4, va="center")
    ax.text(2, 46, "■ étapes à forte exigence de sécurité (personnes habilitées uniquement)", fontsize=8, color=RED)
    return save(fig, "fig20_2_forage_minage_frontiere")

def f21_2():
    fig, ax = canvas(12, 4.8, 120, 48); title(ax, "Schéma de traitement simplifié de l'usine de MCC (fictif)", y=45.5, fs=12)
    s = [("Concassage\nbroyage", GREY), ("Lixiviation\nacide", LIGHTGOLD), ("Décantation\nCCD", GREY), ("Extraction par\nsolvant (SX)", LIGHTTURQ),
         ("Électrolyse\n(EW)", LIGHTNAVY), ("Cathodes Cu\n≈ 50 kt/an", GOLD)]
    for i, (n, c) in enumerate(s):
        x = 2 + i * 19.5; box(ax, x, 26, 17, 11, n, fc=c, ec=NAVY, fs=8.8, bold=(i == 5))
        if i < 5: arrow(ax, (x + 17, 31.5), (x + 19.5, 31.5), color=NAVY, lw=1.8)
    box(ax, 60, 6, 22, 10, "Précipitation\ndu cobalt", fc=LIGHTTURQ, ec=NAVY, fs=8.8)
    box(ax, 88, 6, 24, 10, "Hydroxyde de Co\n≈ 4,5 kt Co/an", fc=GOLD, ec=NAVY, fs=8.8, bold=True)
    arrow(ax, (72, 26), (71, 16), color=NAVY, lw=1.5); ax.text(73, 21, "raffinat\n(purge)", fontsize=7.5, color=MID)
    arrow(ax, (82, 11), (88, 11), color=NAVY, lw=1.8)
    box(ax, 22, 6, 30, 10, "Résidus → parc Kilima", fc="#E3D7B8", ec="#9C8665", fs=8.6)
    arrow(ax, (49, 26), (40, 16), color=MID, lw=1.3)
    note(ax, "Récupérations du scénario : Cu 88 %, Co 70 %. Schéma simplifié, non contractuel. Illustration réalisée pour cet ouvrage.", y=1.5)
    return save(fig, "fig21_2_schema_usine")

def f21_3():
    rows = lire("MCC_production_journaliere_S1_2026.csv")
    d = [dt.date.fromisoformat(r["date"]) for r in rows]; rec = [num(r["recuperation_Cu_pct"]) for r in rows]
    fig, ax = plt.subplots(figsize=(10, 4)); ax.plot(d, rec, color=NAVY, lw=1)
    ax.axhline(100, color=RED, ls=":", lw=1); ax.text(d[2], 101.5, "100 % = limite physique", color=RED, fontsize=8)
    i = int(np.argmax(rec)); ax.scatter([d[i]], [rec[i]], s=120, facecolor="none", edgecolor=RED, lw=2)
    ax.annotate(f"{rec[i]:.1f} % le {d[i].strftime('%d/%m')} : impossible\n→ erreur de saisie à corriger à la source", (d[i], rec[i]), xytext=(d[i] + dt.timedelta(days=12), 116), fontsize=8, color=RED,
                arrowprops=dict(arrowstyle="-|>", color=RED))
    ax.set_ylabel("Récupération Cu (%)"); ax.set_title("Récupération journalière du cuivre, S1 2026", fontsize=10.5); style_axes(ax); pied(fig)
    return save(fig, "fig21_3_recuperation_journaliere", "GRAPHIQUES")

def f22_2():
    rows = [r for r in lire("MCC_maintenance_ordres_travail.csv") if r["type"] == "Correctif" and num(r["duree_arret_h"]) and num(r["duree_arret_h"]) > 0]
    h = Counter();
    for r in rows: h[r["systeme"]] += num(r["duree_arret_h"])
    items = h.most_common(); labs = [k for k, _ in items]; vals = [v for _, v in items]; cum = np.cumsum(vals) / sum(vals) * 100
    fig, ax = plt.subplots(figsize=(10, 4.4)); ax.bar(labs, vals, color=NAVY)
    ax2 = ax.twinx(); ax2.plot(labs, cum, color=GOLD, marker="o", lw=2); ax2.set_ylim(0, 105); ax2.axhline(80, color=RED, ls="--", lw=1)
    ax2.set_ylabel("% cumulé", color=GOLD); ax.set_ylabel("Heures d'arrêt (correctif)")
    ax.set_title("Pareto des heures d'arrêt en maintenance corrective par système (juil. 2025 – avr. 2026)", fontsize=10.5)
    ax.tick_params(axis="x", rotation=25, labelsize=8.5); style_axes(ax); fig.tight_layout(); pied(fig)
    return save(fig, "fig22_2_pareto_maintenance", "GRAPHIQUES")

def f23_1():
    rows = lire("MCC_incidents_HSE_2025_2026.csv")
    t = Counter(r["type"] for r in rows); z = Counter(r["zone"] for r in rows)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2))
    k1 = t.most_common(); a1.barh([k for k, _ in k1][::-1], [v for _, v in k1][::-1], color=TURQ); a1.set_title("Incidents par type", fontsize=10.5); style_axes(a1, False)
    k2 = z.most_common(); a2.barh([k for k, _ in k2][::-1], [v for _, v in k2][::-1], color=NAVY); a2.set_title("Incidents par zone", fontsize=10.5); style_axes(a2, False)
    for a in (a1, a2): a.tick_params(labelsize=8.5)
    fig.suptitle(f"Registre HSE 2025-2026 : {len(rows)} événements déclarés", fontsize=11, color=NAVY, fontweight="bold"); fig.tight_layout(); pied(fig)
    return save(fig, "fig23_1_incidents_hse", "GRAPHIQUES")

def f23_3():
    return workflow("fig23_3_workflow_incident", "Rapport d'incident assisté : qui fait quoi ?",
        [("Déclaration", "témoins,\nsuperviseur\n(humain)"), ("Mise en forme", "Claude : chronologie,\nfaits, lacunes\nsignalées"), ("Enquête", "équipe d'enquête :\nterrain, entretiens,\ncauses (humain)"),
         ("Rédaction", "Claude : rapport\nau format MCC\nà partir des faits"), ("Revue critique", "Claude : check-list ;\nresponsable HSE :\nrelecture"), ("Validation", "direction :\nactions, signature\n(humain)")],
        [H, C, H, C, C, H], note_txt="Claude ne détermine ni les causes, ni la gravité, ni les responsabilités. Illustration réalisée pour cet ouvrage.")

def f24_1():
    rows = [r for r in lire("MCC_suivi_qualite_eau.csv")]
    st = sorted(set(r["station"] for r in rows)); fig, ax = plt.subplots(figsize=(10, 4.3))
    cols = {s: c for s, c in zip(st, [NAVY, RED, TURQ, GOLD])}
    for s in st:
        rr = [r for r in rows if r["station"] == s]; ax.plot([r["mois"][2:] for r in rr], [num(r["Cu_mg_L"]) for r in rr], marker="o", ms=3.5, color=cols[s], label=s)
    ax.axhline(0.5, color=RED, ls="--", lw=1.2); ax.text(0.2, 0.52, "limite de l'exercice : 0,5 mg/L (fictive)", color=RED, fontsize=8)
    ax.set_ylabel("Cu dissous (mg/L)"); ax.set_title("Suivi mensuel du cuivre dissous aux stations de MCC (2025-2026)", fontsize=10.5)
    ax.tick_params(axis="x", rotation=60, labelsize=7.5); ax.legend(frameon=False, fontsize=8); style_axes(ax); fig.tight_layout(); pied(fig)
    return save(fig, "fig24_1_suivi_eau_cuivre", "GRAPHIQUES")

def f25_1():
    rows = lire("MCC_registre_plaintes.csv"); cats = sorted(set(r["categorie"] for r in rows)); vil = ["Kasongo-Mbiyo", "Lupanda", "Mwinda"]
    fig, ax = plt.subplots(figsize=(10, 4.4)); left = np.zeros(len(cats))
    for v, c in zip(vil, [NAVY, GOLD, TURQ]):
        vals = np.array([sum(1 for r in rows if r["categorie"] == k and r["village"] == v) for k in cats])
        ax.barh(cats, vals, left=left, color=c, label=v); left += vals
    ax.set_xlabel("Nombre de plaintes"); ax.legend(frameon=False, fontsize=8.5); ax.set_title("Plaintes communautaires par catégorie et par village (2025-2026)", fontsize=10.5)
    style_axes(ax, False); fig.tight_layout(); pied(fig)
    return save(fig, "fig25_1_plaintes", "GRAPHIQUES")

def f25_2():
    return workflow("fig25_2_mecanisme_plaintes", "Mécanisme de gestion des plaintes : place de Claude",
        [("Réception", "orale, écrite,\ncomité local\n(agent CLO)"), ("Enregistrement", "Claude : résumé,\ncatégorie proposée,\ntraduction"), ("Évaluation", "responsable RC :\ngravité, urgence,\nenquête"),
         ("Réponse", "Claude : projet de\nréponse ; validation\nhumaine"), ("Suivi & clôture", "accord du plaignant,\nretour au village\n(humain)"), ("Analyse", "Claude : tendances,\nrapport trimestriel")],
        [H, C, H, C, H, C], note_txt="La relation avec les communautés reste humaine ; Claude assiste l'enregistrement, la rédaction et l'analyse. Illustration réalisée pour cet ouvrage.")

def f26_1():
    rows = lire("MCC_bons_de_commande.csv"); m = [num(r["montant_USD"]) for r in rows]
    fig, ax = plt.subplots(figsize=(10, 4.2)); bins = np.arange(0, 20001, 500)
    ax.hist([x for x in m if x <= 20000], bins=bins, color=NAVY, edgecolor="white")
    ax.axvline(10000, color=RED, ls="--", lw=1.5); ax.text(10150, ax.get_ylim()[1] * 0.85, "seuil d'approbation\n10 000 USD", color=RED, fontsize=8.5)
    ax.annotate("3 commandes à 9 800 USD\nle même jour, même fournisseur", xy=(9800, 3), xytext=(12500, ax.get_ylim()[1] * 0.45), fontsize=8, color=RED, arrowprops=dict(arrowstyle="-|>", color=RED))
    ax.set_xlabel("Montant de la commande (USD, ≤ 20 000)"); ax.set_ylabel("Nombre de commandes")
    ax.set_title("Distribution des montants de commandes : repérer les fractionnements sous le seuil", fontsize=10.5); style_axes(ax); pied(fig)
    return save(fig, "fig26_1_commandes_seuil", "GRAPHIQUES")

def f27_1():
    return workflow("fig27_1_veille_reglementaire", "Veille réglementaire et conformité assistées",
        [("Sources officielles", "Journal officiel,\nministère, ITIE,\nnormes (humain)"), ("Tri & résumé", "Claude : résumé,\nobligations,\néchéances"), ("Analyse d'impact", "juriste :\napplicabilité,\ninterprétation"),
         ("Registre", "Claude : mise à\njour du registre\ndes obligations"), ("Plan d'action", "responsables\nmétiers (humain)"), ("Contrôle", "audit, preuves\nde conformité")],
        [H, C, H, C, H, H], note_txt="Toute interprétation engageante relève du juriste. Illustration réalisée pour cet ouvrage.")

def f28_1():
    import openpyxl
    wb = openpyxl.load_workbook(ROOT / "03_EXERCICES_ET_DONNEES" / "EXCEL" / "MCC_budget_reel_S1_2026.xlsx"); ws = wb["Budget vs réel"]
    rows = list(ws.iter_rows(min_row=3, values_only=True)); e = defaultdict(float)
    for r in rows: e[r[1]] += r[4]
    items = sorted(e.items(), key=lambda kv: kv[1])
    fig, ax = plt.subplots(figsize=(10, 4.4))
    ax.barh([k for k, _ in items], [v for _, v in items], color=[RED if v > 0 else GREEN for _, v in items])
    for i, (_, v) in enumerate(items): ax.text(v + (0.05 if v >= 0 else -0.05), i, f"{v:+.2f}".replace(".", ","), va="center", ha="left" if v >= 0 else "right", fontsize=8)
    ax.axvline(0, color=INK, lw=0.8); ax.set_xlabel("Écart cumulé réel – budget (MUSD) ; rouge = dépassement")
    ax.set_title("Écarts budgétaires cumulés par centre de coût, S1 2026", fontsize=10.5); style_axes(ax, False); fig.tight_layout(); pied(fig)
    return save(fig, "fig28_1_ecarts_budget", "GRAPHIQUES")

def f29_1():
    return workflow("fig29_1_cycle_audit", "Le cycle d'audit interne assisté par Claude",
        [("Planification", "univers d'audit,\nrisques\n(auditeur)"), ("Préparation", "Claude : programme\nde travail, check-\nlists, demandes"), ("Tests", "Claude : analyses\nde données (code) ;\nauditeur : preuves"),
         ("Constats", "Claude : rédaction\nformat CCCRR ;\nauditeur : validation"), ("Rapport", "revue qualité,\ncontradictoire\n(humain)"), ("Suivi", "Claude : suivi des\nrecommandations")],
        [H, C, C, C, H, C], note_txt="Le jugement d'audit et l'opinion restent ceux de l'auditeur. Illustration réalisée pour cet ouvrage.")

def f30_1():
    rows = lire("MCC_matrice_formations.csv"); ref = dt.date(2026, 11, 16)
    cat = Counter()
    for r in rows:
        d = (dt.date.fromisoformat(r["date_expiration"]) - ref).days
        cat[r["formation"], "expirée" if d < 0 else ("< 90 jours" if d < 90 else "valide")] += 1
    forms = sorted(set(r["formation"] for r in rows)); fig, ax = plt.subplots(figsize=(10, 4.4)); left = np.zeros(len(forms))
    for s, c in [("expirée", RED), ("< 90 jours", ORANGE), ("valide", GREEN)]:
        v = np.array([cat[f, s] for f in forms]); ax.barh(forms, v, left=left, color=c, label=s); left += v
    ax.legend(frameon=False, fontsize=8.5); ax.set_xlabel("Nombre d'habilitations"); ax.set_title("État des formations obligatoires au 16/11/2026", fontsize=10.5)
    style_axes(ax, False); fig.tight_layout(); pied(fig)
    return save(fig, "fig30_1_formations", "GRAPHIQUES")

def f31_1():
    return workflow("fig31_1_reporting_direction", "Du terrain au conseil : la chaîne de reporting assistée",
        [("Données sources", "systèmes métier,\nrapports validés"), ("Consolidation", "Claude Code / code :\ncalculs, contrôles\nde cohérence"), ("Analyse", "contrôleur de gestion\n+ Claude : écarts,\ntendances"),
         ("Rédaction", "Claude : synthèse\nexécutive, slides"), ("Revue", "direction :\nmessages, arbitrages\n(humain)"), ("Gouvernance", "conseil :\ndécisions\n(humain)")],
        [H, C, C, C, H, H])

def f32_1():
    return workflow("fig32_1_devoir_diligence_ocde", "Le cadre en cinq étapes du devoir de diligence de l'OCDE, et l'appui de Claude",
        [("1. Systèmes de\ngestion solides", "Claude : rédaction\nde politiques,\nprocédures"), ("2. Identifier et\névaluer les risques", "Claude : analyse\ndocumentaire des\nfournisseurs"),
         ("3. Stratégie de\nréponse aux risques", "humain : décisions ;\nClaude : plans\nd'action"), ("4. Audit indépendant\ntiers", "auditeurs\nindépendants"), ("5. Rapport annuel", "Claude : premier\njet du rapport")],
        [NAVY, NAVY, NAVY, NAVY, NAVY], note_txt="Étapes d'après OCDE (2016), Guide sur le devoir de diligence (3e éd.). Rôles de Claude : proposition de l'auteur. Illustration réalisée pour cet ouvrage.")

ALL = [f17_2, f18_1, f18_2, f19_2, f20_2, f21_2, f21_3, f22_2, f23_1, f23_3, f24_1, f25_1, f25_2, f26_1, f27_1, f28_1, f29_1, f30_1, f31_1, f32_1]
if __name__ == "__main__":
    for f in ALL: print(f())
