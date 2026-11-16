# -*- coding: utf-8 -*-
"""Couverture (1re) et quatrième de couverture — format 15,5 × 23,5 cm.
Sorties : 02_ILLUSTRATIONS/COUVERTURES/couverture_avant.(pdf|png), couverture_arriere.(pdf|png)"""
import math, textwrap
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "02_ILLUSTRATIONS" / "COUVERTURES"; OUT.mkdir(parents=True, exist_ok=True)
FD = "/usr/share/fonts/opentype/ebgaramond/"
F = lambda style: FontProperties(fname=FD + f"EBGaramond12-{style}.otf")
REG, ITA, BOLD = F("Regular"), F("Italic"), F("Bold")
W, H = 15.5 / 2.54, 23.5 / 2.54
FOND, CREME, CUIVRE, CUIVRE_P = "#1C1D1F", "#EFE7D8", "#B07A45", "#7A5634"
TITRE, SOUS_TITRE = "LA MINE AUGMENTÉE", "Maîtriser Claude et l'intelligence artificielle générative dans les métiers et les processus miniers"

def toile():
    fig = plt.figure(figsize=(W, H)); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 155); ax.set_ylim(0, 235); ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 155, 235, fc=FOND, ec="none", zorder=0))
    return fig, ax

def fosse(ax, cx, cy, rx, ry, n=22, seed=7, lw=0.55, alpha=1.0, clip=None):
    """Courbes de niveau d'une fosse à ciel ouvert : gradins concentriques irréguliers + rampe."""
    rng = np.random.default_rng(seed); t = np.linspace(0, 2 * np.pi, 600)
    ph = rng.uniform(0, 2 * np.pi, 4)
    for i in range(n):
        k = 1 - i / (n + 2)
        r = 1 + 0.07 * np.sin(2 * t + ph[0]) + 0.045 * np.sin(3 * t + ph[1]) * k + 0.02 * np.sin(7 * t + ph[2])
        x = cx + rx * k * r * np.cos(t); y = cy + ry * k * r * np.sin(t) - (1 - k) * 6
        c = CUIVRE if i % 4 == 0 else CREME
        a = alpha * (0.85 if i % 4 == 0 else 0.30 + 0.35 * (1 - k))
        line, = ax.plot(x, y, color=c, lw=lw * (1.4 if i % 4 == 0 else 1), alpha=a, zorder=2)
        if clip is not None: line.set_clip_path(clip)
    # rampe en spirale
    s = np.linspace(0, 1, 400); ang = -0.6 + 5.2 * np.pi * s; k = 1 - 0.92 * s
    x = cx + rx * k * np.cos(ang); y = cy + ry * k * np.sin(ang) - 0.92 * s * 6
    line, = ax.plot(x, y, color=CUIVRE, lw=lw * 1.1, alpha=alpha * 0.9, ls=(0, (6, 3)), zorder=3)
    if clip is not None: line.set_clip_path(clip)

def espace(ax, x, y, txt, size, font, color=CREME, track=0.0, ha="center"):
    """Texte avec interlettrage approximatif (espaces fines)."""
    if track: txt = (" " * int(track)).join(txt) if track >= 1 else txt
    ax.text(x, y, txt, fontproperties=font, size=size, color=color, ha=ha, va="center", zorder=5)

def avant():
    fig, ax = toile()
    fosse(ax, 77.5, 52, 92, 50, n=24, seed=11)
    ax.add_patch(Rectangle((0, 0), 155, 235, fc="none", ec=CUIVRE_P, lw=0.8, zorder=4))
    espace(ax, 77.5, 214, "G U I D E   P R O F E S S I O N N E L", 8.5, REG, color=CUIVRE)
    espace(ax, 77.5, 182, "L A   M I N E", 31, REG)
    espace(ax, 77.5, 160, "A U G M E N T É E", 31, REG)
    ax.plot([60, 95], [146, 146], color=CUIVRE, lw=0.9, zorder=5)
    for i, l in enumerate(textwrap.wrap(SOUS_TITRE, 44)):
        espace(ax, 77.5, 135 - i * 7.2, l, 12.5, ITA)
    ax.add_patch(Rectangle((0, 0), 155, 17, fc=FOND, ec="none", zorder=4))
    ax.plot([0, 155], [17, 17], color=CUIVRE_P, lw=0.6, zorder=4)
    espace(ax, 77.5, 9, "É D I T I O N   2 0 2 6", 7.5, REG, color=CUIVRE)
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"couverture_avant.{ext}", dpi=300, facecolor=FOND)
    plt.close(fig)

def arriere():
    fig, ax = toile()
    from matplotlib.patches import Rectangle as R
    clip = R((0, 0), 155, 235, transform=ax.transData)
    fosse(ax, 150, 228, 70, 48, n=16, seed=4, alpha=0.35, clip=clip)
    ax.add_patch(Rectangle((0, 0), 155, 235, fc="none", ec=CUIVRE_P, lw=0.8, zorder=4))
    y = 200
    citation = ("« On ne maîtrise pas l'intelligence artificielle simplement parce qu'on sait lui poser des questions. "
                "On la maîtrise lorsqu'on est capable de l'intégrer dans ses méthodes de travail, d'évaluer ses résultats "
                "et de créer de la valeur professionnelle avec elle. »")
    for l in textwrap.wrap(citation, 52):
        ax.text(17, y, l, fontproperties=ITA, size=11, color=CREME, va="center"); y -= 6.3
    y -= 5
    corps = ("Dans une mine, l'information est partout : journaux de sondage, bilans métallurgiques, ordres de travail, "
             "déclarations d'incident, registres de plaintes, contrats, déclarations fiscales. Ce livre apprend aux professionnels "
             "du secteur à faire de l'intelligence artificielle générative un véritable outil de travail — rigoureux, vérifiable "
             "et sûr — sans jamais lui déléguer ce qui relève de l'expertise et de la responsabilité humaines.")
    for l in textwrap.wrap(corps, 62):
        ax.text(17, y, l, fontproperties=REG, size=9.6, color=CREME, va="center"); y -= 5.3
    y -= 6
    ax.text(17, y, "D A N S   C E   L I V R E", fontproperties=REG, size=8, color=CUIVRE, va="center"); y -= 8
    points = ["Comprendre le fonctionnement des grands modèles de langage, leurs forces et leurs limites",
              "Formuler des instructions professionnelles avec la méthode CADRE",
              "Analyser documents et données, vérifier chaque résultat",
              "Appliquer Claude à seize métiers et processus miniers, de l'exploration à la fermeture",
              "Protéger les données et maîtriser les risques de l'IA",
              "Concevoir ses propres méthodes de travail assistées"]
    for p_ in points:
        ls = textwrap.wrap(p_, 58)
        ax.text(17, y, "—", fontproperties=REG, size=9.6, color=CUIVRE, va="center")
        for l in ls:
            ax.text(23, y, l, fontproperties=REG, size=9.6, color=CREME, va="center"); y -= 5.1
        y -= 1.6
    y -= 4
    pub = "430 questions corrigées · 255 prompts commentés · 20 fichiers d’exercice · ateliers et projet final"
    for l in textwrap.wrap(pub, 70):
        ax.text(17, y, l, fontproperties=ITA, size=8.8, color=CUIVRE, va="center"); y -= 4.8
    ax.add_patch(Rectangle((103, 12), 38, 22, fc="#FFFFFF", ec="none", zorder=5))
    ax.text(122, 27, "ISBN", fontproperties=REG, size=7, color="#333333", ha="center", zorder=6)
    for i in range(28):
        ax.add_patch(Rectangle((107 + i * 1.08, 15), 0.45 if i % 3 else 0.8, 9, fc="#BBBBBB", ec="none", zorder=6))
    ax.text(17, 22, "Mines · Intelligence artificielle · Management", fontproperties=REG, size=8, color=CREME, va="center", alpha=0.8)
    ax.text(17, 15, "Emplacement réservé au code-barres ISBN et au prix", fontproperties=ITA, size=7, color=CREME, va="center", alpha=0.55)
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"couverture_arriere.{ext}", dpi=300, facecolor=FOND)
    plt.close(fig)

if __name__ == "__main__":
    avant(); arriere(); print("Couvertures produites dans", OUT)
