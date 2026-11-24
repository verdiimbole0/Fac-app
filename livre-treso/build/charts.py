import sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(ROOT, "data"))
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
for f in os.listdir(os.path.expanduser("~/.fonts")): fm.fontManager.addfont(os.path.expanduser("~/.fonts/" + f))
import fil_rouge as F
from datetime import date
NAVY = "#0A1E3F"; TEAL = "#1B9E8F"; GREY = "#F3F5F8"; MID = "#5B6B82"; LIGHT = "#C9D1DC"; WARN = "#8A9BB3"
plt.rcParams.update({"font.family": "Source Sans 3", "font.size": 8.5, "axes.edgecolor": LIGHT, "axes.labelcolor": NAVY,
                     "xtick.color": MID, "ytick.color": MID, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.titleweight": "bold", "axes.titlesize": 9, "axes.titlecolor": NAVY, "figure.dpi": 100})
OUT = os.path.join(ROOT, "illustrations")
def fmt(v): return f"{v:,.0f}".replace(",", " ")
def kfmt(x, p): return f"{x/1000:.0f} k"
def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=300, bbox_inches="tight", facecolor="white"); plt.close(fig)

def fig_parcours():
    fig, ax = plt.subplots(figsize=(4.6, 3.4)); ax.set_xlim(0, 10.4); ax.set_ylim(0, 7.2); ax.axis("off")
    def box(x, y, w, h, t, fc, fs=7.6):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.18", fc=fc, ec="none"))
        ax.text(x+w/2, y+h/2, t, ha="center", va="center", color="white", fontsize=fs, fontfamily="Montserrat", fontweight="bold", linespacing=1.2)
    def arr(a, b, t="", c=TEAL, off=(0, 0)):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=9, color=c, lw=1.2))
        if t: ax.text((a[0]+b[0])/2+off[0], (a[1]+b[1])/2+off[1], t, ha="center", va="center", fontsize=6.9, color=NAVY)
    box(3.2, 2.9, 4.0, 1.5, "TRÉSORERIE\ncaisse, banque,\nmonnaie électronique", NAVY, fs=7.4)
    box(0.1, 5.6, 2.9, 1.1, "Clients", TEAL); box(3.75, 5.6, 2.9, 1.1, "Associés,\nbanques, bailleurs", TEAL, fs=6.9)
    box(7.4, 5.6, 2.9, 1.1, "Cessions\nd'actifs", TEAL, fs=7)
    box(0.1, 0.3, 2.9, 1.1, "Fournisseurs", "#2E4A75"); box(3.75, 0.3, 2.9, 1.1, "Salariés, État,\nbailleur du local", "#2E4A75", fs=6.9)
    box(7.4, 0.3, 2.9, 1.1, "Équipements,\nvéhicules", "#2E4A75", fs=7)
    arr((1.6, 5.55), (3.7, 4.45), "encaissements\nd'exploitation", off=(-1.0, -0.15))
    arr((5.2, 5.55), (5.2, 4.45), "financement", off=(0.95, 0))
    arr((8.8, 5.55), (6.7, 4.45), "investissement", off=(1.05, -0.15))
    arr((3.7, 2.85), (1.6, 1.45), "achats", c=NAVY, off=(-0.75, 0.05))
    arr((5.2, 2.85), (5.2, 1.45), "salaires,\nimpôts, loyer", c=NAVY, off=(0.95, 0))
    arr((6.7, 2.85), (8.8, 1.45), "achats d'actifs", c=NAVY, off=(0.95, 0.05))
    ax.text(5.2, 6.95, "ENTRÉES", ha="center", fontsize=7, color=TEAL, fontfamily="Montserrat", fontweight="bold")
    ax.text(5.2, 0.0, "SORTIES", ha="center", fontsize=7, color=NAVY, fontfamily="Montserrat", fontweight="bold")
    save(fig, "fig01_parcours_argent.png")

def fig_bridge():
    items = F.BRIDGE; labels = ["Résultat", "Amortis-\nsements", "Créances", "Stocks", "Dettes\nfourn.", "Emprunt", "Véhicule", "Variation\ntrésorerie"]
    fig, ax = plt.subplots(figsize=(4.6, 2.6)); cum = 0
    for i, (lab, v) in enumerate(items):
        bottom = cum if v >= 0 else cum + v
        ax.bar(i, abs(v), bottom=bottom, color=TEAL if v >= 0 else NAVY, width=0.62)
        ax.text(i, bottom + abs(v) + 1500, ("+" if v > 0 else "") + fmt(v), ha="center", fontsize=6.6, color=NAVY)
        cum += v
    ax.bar(len(items), cum, color="#B23A3A" if False else WARN, width=0.62)
    ax.text(len(items), cum - 5000, fmt(cum), ha="center", fontsize=6.8, color=NAVY, fontweight="bold")
    ax.axhline(0, color=MID, lw=0.7); ax.set_xticks(range(len(labels))); ax.set_xticklabels(labels, fontsize=6.4)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(kfmt)); ax.set_ylabel("USD"); ax.set_ylim(-62000, 40000)
    ax.set_title("T4 2025 : résultat +28 000 USD, trésorerie -55 000 USD", loc="left")
    save(fig, "fig02_resultat_tresorerie.png")

def fig_ageing():
    fig, ax = plt.subplots(figsize=(4.5, 2.1)); b = F.CREANCES_BUCKETS
    cols = [TEAL, "#5FB8AE", "#2E4A75", NAVY, "#7A1F2B"]
    ax.barh(range(5), b, color=[TEAL, "#6CB9B0", "#4A6890", NAVY, "#3A3F4A"], height=0.6)
    for i, v in enumerate(b): ax.text(v + 1000, i, f"{fmt(v)} USD ({v/sum(b)*100:.0f} %)".replace(".", ","), va="center", fontsize=7, color=NAVY)
    ax.set_yticks(range(5)); ax.set_yticklabels(F.BUCKETS); ax.invert_yaxis(); ax.set_xlim(0, 105000)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(kfmt)); ax.set_title("Ancienneté des créances au 31/12/2025 (total 126 000 USD)", loc="left")
    save(fig, "fig03_anciennete_creances.png")

def _weekly_line(ax, W, color, label, ls="-", marker="o"):
    x = [r['sem'] for r in W]; ax.plot(x, [r['cloture'] for r in W], color=color, lw=1.6, marker=marker, ms=3, label=label + " (clôture)", ls=ls)
    ax.plot(x, [r['plus_bas'] for r in W], color=color, lw=0.8, ls=":", label=label + " (point bas)")

def fig_13w_base():
    fig, ax = plt.subplots(figsize=(4.6, 2.5))
    _weekly_line(ax, F.W_BASE, NAVY, "Prévision initiale")
    ax.axhline(0, color="#7A1F2B", lw=0.8); ax.axhline(F.RESERVE_CIBLE, color=TEAL, lw=0.8, ls="--")
    ax.text(13.3, F.RESERVE_CIBLE, "réserve\ncible", fontsize=6.3, color=TEAL, va="center")
    ax.fill_between([0.5, 13.5], -25000, 0, color="#7A1F2B", alpha=0.06)
    ax.set_xticks(range(1, 14)); ax.set_xticklabels([f"S{i}" for i in range(1, 14)], fontsize=6.5); ax.set_xlim(0.5, 14.2)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(kfmt)); ax.set_ylim(-25000, 32000)
    ax.legend(fontsize=6.3, frameon=False, loc="upper left", ncol=2); ax.set_title("Prévisionnel 13 semaines (5 janvier-5 avril 2026)", loc="left")
    save(fig, "fig04_13_semaines.png")

def fig_versions():
    fig, ax = plt.subplots(figsize=(4.6, 2.5)); ms = list(range(1, 7))
    for M, c, lab, ls in [(F.M_BASE, NAVY, "Prévision initiale", "-"), (F.M_ENC, "#6CB9B0", "Après actions sur les encaissements", "--"), (F.M_PLAN, TEAL, "Après plan de paiement", "-")]:
        ax.plot(ms, [M[m]['cloture'] for m in ms], color=c, lw=1.7, ls=ls, marker="o", ms=3, label=lab)
    ax.axhline(0, color="#7A1F2B", lw=0.8); ax.axhline(F.RESERVE_CIBLE, color=MID, lw=0.7, ls=":")
    ax.set_xticks(ms); ax.set_xticklabels([F.MOIS[m][:4] + "." for m in ms]); ax.yaxis.set_major_formatter(plt.FuncFormatter(kfmt))
    ax.legend(fontsize=6.4, frameon=False, loc="upper left"); ax.set_title("Solde de fin de mois selon les décisions prises", loc="left")
    save(fig, "fig05_versions.png")

def fig_dashboard():
    fig, axs = plt.subplots(2, 2, figsize=(4.8, 3.9)); fig.subplots_adjust(hspace=0.6, wspace=0.42)
    ax = axs[0][0]; W = F.W_REPREV
    ax.bar([r['sem'] for r in W], [r['cloture'] for r in W], color=[TEAL if r['plus_bas'] >= 0 else NAVY for r in W], width=0.6)
    ax.plot([r['sem'] for r in W], [r['plus_bas'] for r in W], color="#7A1F2B", lw=0.9, marker="v", ms=2.5)
    ax.axhline(0, color=MID, lw=0.6); ax.axhline(F.RESERVE_CIBLE, color=TEAL, lw=0.6, ls="--")
    ax.set_title("Soldes prévus, 9 semaines", loc="left", fontsize=7.5); ax.yaxis.set_major_formatter(plt.FuncFormatter(kfmt))
    ax.set_xticks([r['sem'] for r in W]); ax.set_xticklabels([f"S{r['sem']}" for r in W], fontsize=5.5); ax.tick_params(labelsize=6)
    ax = axs[0][1]; cats = ["Encaiss.", "Décaiss."]
    ax.bar([0-0.18, 1-0.18], [F.JAN['prevu_E'], F.JAN['prevu_D']], width=0.36, color=LIGHT, label="Prévu")
    ax.bar([0+0.18, 1+0.18], [F.JAN['reel_E'], F.JAN['reel_D']], width=0.36, color=[TEAL, NAVY], label="Réalisé")
    ax.set_xticks([0, 1]); ax.set_xticklabels(cats, fontsize=6.5); ax.yaxis.set_major_formatter(plt.FuncFormatter(kfmt)); ax.tick_params(labelsize=6)
    ax.set_title("Janvier : prévu (gris) / réalisé", loc="left", fontsize=7.5); ax.set_ylim(0, 125000)
    ax = axs[1][0]; cr = F.CREANCES_31JAN
    ax.barh(range(5), cr, color=[TEAL, "#6CB9B0", "#4A6890", NAVY, "#3A3F4A"], height=0.6); ax.invert_yaxis()
    ax.set_yticks(range(5)); ax.set_yticklabels(F.BUCKETS, fontsize=6); ax.xaxis.set_major_formatter(plt.FuncFormatter(kfmt)); ax.tick_params(labelsize=6)
    ax.set_title("Créances au 31/01 par ancienneté", loc="left", fontsize=7.5)
    ax = axs[1][1]
    ax.bar(["31/12", "31/01"], [F.DSO_31DEC, F.DSO_31JAN], color=[LIGHT, TEAL], width=0.5)
    for i, v in enumerate([F.DSO_31DEC, F.DSO_31JAN]): ax.text(i, v + 0.8, f"{v:.1f} j".replace(".", ","), ha="center", fontsize=6.5, color=NAVY)
    ax.axhline(30, color=NAVY, lw=0.7, ls="--"); ax.text(0.5, 26.5, "délai contractuel : 30 j", fontsize=5.5, color="white", ha="center")
    ax.set_ylim(0, 45); ax.tick_params(labelsize=6); ax.set_title("Délai moyen de recouvrement", loc="left", fontsize=7.5)
    save(fig, "fig06_tableau_de_bord.png")

def fig_scenarios():
    fig, ax = plt.subplots(figsize=(4.6, 2.5)); x = [3, 4, 5, 6]; o = F.OPEN_AVR
    ax.plot(x, [o] + [F.BASE_AVR['m'][m]['cloture'] for m in (4, 5, 6)], color=LIGHT, lw=1.5, marker="o", ms=3, label="Sans perte de client")
    st = {"Optimiste": ("#6CB9B0", "-"), "Réaliste": (TEAL, "-"), "Pessimiste": (NAVY, "-")}
    for k, v in F.SCEN_RES.items():
        ax.plot(x, [o] + [v['m'][m]['cloture'] for m in (4, 5, 6)], color=st[k][0], lw=1.6, marker="o", ms=3, label=k)
    ax.plot(x, [o] + [F.SCEN_PES_MES['m'][m]['cloture'] for m in (4, 5, 6)], color=NAVY, lw=1.2, ls="--", marker="s", ms=2.5, label="Pessimiste + plan d'urgence")
    ax.axhline(0, color="#7A1F2B", lw=0.8); ax.axhline(F.RESERVE_CIBLE, color=MID, lw=0.6, ls=":")
    ax.set_xticks(x); ax.set_xticklabels(["31/03", "30/04", "31/05", "30/06"]); ax.yaxis.set_major_formatter(plt.FuncFormatter(kfmt))
    ax.legend(fontsize=6, frameon=False, loc="upper left", ncol=2); ax.set_ylim(-2000, 72000)
    ax.set_title("Trésorerie fin de mois selon les scénarios", loc="left")
    save(fig, "fig07_scenarios.png")

def fig_asbl():
    fig, ax = plt.subplots(figsize=(4.6, 2.4)); ms = list(range(1, 13))
    ax.bar([m-0.2 for m in ms], [r['cloture'] for r in F.ASBL_PREVU], width=0.4, color=LIGHT, label="Solde prévu (tranche 2 fin avril)")
    ax.bar([m+0.2 for m in ms], [r['cloture'] for r in F.ASBL_REEL], width=0.4, color=[TEAL if r['cloture'] >= 0 else NAVY for r in F.ASBL_REEL], label="Solde réel (tranche 2 le 15 juin)")
    ax.axhline(0, color=MID, lw=0.7); ax.set_xticks(ms); ax.set_xticklabels([F.MOIS[m][:3] for m in ms], fontsize=6.4)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(kfmt)); ax.legend(fontsize=6.2, frameon=False, loc="upper right")
    ax.set_title("Trésorerie du projet « Lire pour réussir » (50 000 USD)", loc="left")
    save(fig, "fig08_asbl_projet.png")

def fig_ia_cycle():
    fig, ax = plt.subplots(figsize=(4.5, 2.4)); ax.set_xlim(0, 10); ax.set_ylim(0, 4.6); ax.axis("off")
    steps = [("1. PRÉPARER", "données anonymisées\net vérifiées"), ("2. DEMANDER", "contexte, tâche,\nformat, contraintes"),
             ("3. VÉRIFIER", "totaux, logique,\nsources"), ("4. DÉCIDER", "un humain valide\net assume")]
    for i, (a, b) in enumerate(steps):
        x = 0.15 + i*2.5
        ax.add_patch(FancyBboxPatch((x, 1.5), 2.1, 2.1, boxstyle="round,pad=0.04,rounding_size=0.2", fc=NAVY if i % 2 == 0 else TEAL, ec="none"))
        ax.text(x+1.05, 3.05, a, ha="center", color="white", fontsize=7.6, fontfamily="Montserrat", fontweight="bold")
        ax.text(x+1.05, 2.2, b, ha="center", va="center", color="white", fontsize=7.2)
        if i < 3: ax.add_patch(FancyArrowPatch((x+2.15, 2.55), (x+2.5, 2.55), arrowstyle="-|>", mutation_scale=9, color=MID))
    ax.add_patch(FancyArrowPatch((8.8, 1.45), (1.2, 1.45), arrowstyle="-|>", mutation_scale=9, color=LIGHT, connectionstyle="arc3,rad=-0.25"))
    ax.text(5, 0.25, "Si la vérification échoue : on corrige les données ou la demande, puis on recommence", ha="center", fontsize=7, color=MID)
    save(fig, "fig09_cycle_ia.png")

def fig_separation():
    fig, ax = plt.subplots(figsize=(4.6, 2.3)); ax.set_xlim(0, 10); ax.set_ylim(0, 4.4); ax.axis("off")
    st = [("Demander", "chef de service"), ("Approuver", "gérante ou\ndélégué"), ("Payer", "comptable\n(prépare)"), ("Signer", "2 signataires\nbancaires"), ("Contrôler", "personne\nindépendante")]
    for i, (a, b) in enumerate(st):
        x = 0.1 + i*2.0
        ax.add_patch(FancyBboxPatch((x, 1.6), 1.7, 1.9, boxstyle="round,pad=0.04,rounding_size=0.2", fc=[TEAL, NAVY, TEAL, NAVY, "#2E4A75"][i], ec="none"))
        ax.text(x+0.85, 3.0, a.upper(), ha="center", color="white", fontsize=7.2, fontfamily="Montserrat", fontweight="bold")
        ax.text(x+0.85, 2.2, b, ha="center", va="center", color="white", fontsize=6.9)
        if i < 4: ax.add_patch(FancyArrowPatch((x+1.72, 2.55), (x+2.0, 2.55), arrowstyle="-|>", mutation_scale=8, color=MID))
    ax.text(5, 0.9, "Règle d'or : une même personne ne réalise jamais seule deux étapes successives", ha="center", fontsize=7.4, color=NAVY, fontweight="bold")
    ax.text(5, 0.35, "(dans une très petite structure, compenser par une revue mensuelle par la direction)", ha="center", fontsize=6.8, color=MID)
    save(fig, "fig10_separation_fonctions.png")

def fig_c12():
    fig, ax = plt.subplots(figsize=(4.6, 2.5))
    _weekly_line(ax, F.C12_W_SANS, NAVY, "Sans mesures"); _weekly_line(ax, F.C12_W_MES, TEAL, "Avec mesures", marker="s")
    ax.axhline(0, color="#7A1F2B", lw=0.8); ax.axhline(F.RESERVE_CIBLE, color=MID, lw=0.6, ls="--")
    ax.set_xticks(range(1, 14)); ax.set_xticklabels([f"S{i}" for i in range(1, 14)], fontsize=6.3)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(kfmt)); ax.legend(fontsize=5.9, frameon=False, loc="upper right", ncol=2)
    ax.set_ylim(-12000, 100000); ax.set_title("Mission : 13 semaines, juillet-septembre 2026", loc="left")
    save(fig, "fig11_mission_13_semaines.png")

def fig_parcours_lecture():
    fig, ax = plt.subplots(figsize=(4.5, 1.9)); ax.set_xlim(0, 12.6); ax.set_ylim(0, 3.3); ax.axis("off")
    ess = {1, 2, 3, 7, 8, 9, 12}
    for i in range(12):
        c = i+1; x = 0.1 + i*1.04
        ax.add_patch(FancyBboxPatch((x, 1.5), 0.86, 0.9, boxstyle="round,pad=0.02,rounding_size=0.12", fc=NAVY if c in ess else "white", ec=TEAL, lw=1))
        ax.text(x+0.43, 1.95, str(c), ha="center", va="center", fontsize=9, color="white" if c in ess else TEAL, fontfamily="Montserrat", fontweight="bold")
    ax.add_patch(FancyBboxPatch((0.4, 0.45), 0.4, 0.4, boxstyle="round,pad=0.02", fc=NAVY, ec=TEAL)); ax.text(1.0, 0.65, "Parcours 1 : indispensables", va="center", fontsize=7.5, color=NAVY)
    ax.add_patch(FancyBboxPatch((6.6, 0.45), 0.4, 0.4, boxstyle="round,pad=0.02", fc="white", ec=TEAL)); ax.text(7.2, 0.65, "Parcours 2 : selon votre besoin", va="center", fontsize=7.5, color=NAVY)
    for lab, a, b in [("PARTIE I", 0, 2), ("PARTIE II", 2, 6), ("PARTIE III", 6, 9), ("PARTIE IV", 9, 12)]:
        ax.plot([0.15+a*1.04, b*1.04-0.08], [2.75, 2.75], color=TEAL, lw=1.2); ax.text((0.15+a*1.04+b*1.04)/2, 2.95, lab, ha="center", fontsize=6.6, color=TEAL, fontfamily="Montserrat", fontweight="bold")
    save(fig, "fig00_parcours_lecture.png")

if __name__ == "__main__":
    for f in [fig_parcours, fig_bridge, fig_ageing, fig_13w_base, fig_versions, fig_dashboard, fig_scenarios, fig_asbl, fig_ia_cycle, fig_separation, fig_c12, fig_parcours_lecture]:
        f(); print(f.__name__)
