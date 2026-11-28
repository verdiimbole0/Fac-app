# -*- coding: utf-8 -*-
"""Couvertures (1re et 4e) des trois tomes, format 15,5 × 23,5 cm.
Même maquette pour les trois tomes ; seuls changent la couleur d'accent (cuivre, malachite, cobalt),
la position des courbes de niveau et les textes.
Sorties : 02_ILLUSTRATIONS/COUVERTURES/tome{N}_couverture_avant.(pdf|png), tome{N}_couverture_arriere.(pdf|png)"""
import textwrap
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
REG = FontProperties(fname=FD + "EBGaramond12-Regular.otf")
ITA = FontProperties(fname=FD + "EBGaramond12-Italic.otf")
FOND, CREME = "#1C1D1F", "#EFE7D8"
SOUS_TITRE = "Maîtriser Claude et l'intelligence artificielle générative dans les métiers et les processus miniers"
AUTEUR = "Verdi Imbole"
BIO = ("Auteur indépendant, auditeur financier et freelance, Verdi Imbole accompagne les ASBL et les entreprises "
       "dans la mise en place des outils d'intelligence artificielle, l'amélioration de la gouvernance et des pratiques "
       "comptables, le renforcement du contrôle interne et l'optimisation des processus administratifs et financiers.")

TOMES = {
    1: dict(romain="I", titre="Comprendre et maîtriser Claude", accent="#B07A45", sombre="#7A5634",
            fosse=dict(cx=77.5, cy=42, rx=92, ry=44, seed=11),
            citation="« On ne maîtrise pas l'intelligence artificielle simplement parce qu'on sait lui poser des questions. "
                     "On la maîtrise lorsqu'on est capable de l'intégrer dans ses méthodes de travail, d'évaluer ses résultats "
                     "et de créer de la valeur professionnelle avec elle. »",
            texte="Dans une mine, l'information est partout : journaux de sondage, bilans métallurgiques, ordres de travail, "
                  "déclarations d'incident, registres de plaintes, contrats, déclarations fiscales. Ce premier tome donne les "
                  "bases indispensables pour faire de l'intelligence artificielle générative un véritable outil de travail, "
                  "rigoureux, vérifiable et sûr, sans jamais lui déléguer ce qui relève de l'expertise et de la responsabilité humaines.",
            points=["Comprendre le fonctionnement des grands modèles de langage, leurs forces et leurs limites",
                    "Découvrir Claude et l'écosystème Anthropic",
                    "Choisir le bon modèle et les bons réglages",
                    "Formuler des instructions professionnelles avec la méthode CADRE",
                    "Travailler sur des documents, rechercher et vérifier des sources",
                    "Organiser ses dossiers avec les projets et connecter Claude à son environnement"],
            chiffres="Parties I et II · chapitres 1 à 16 · 160 questions corrigées · 60 prompts commentés"),
    2: dict(romain="II", titre="Claude dans les métiers et les processus miniers", accent="#6A9E86", sombre="#4A6E5D",
            fosse=dict(cx=112, cy=42, rx=88, ry=44, seed=23),
            citation="« Dans une mine, les processus sont interdépendants, et la meilleure idée d'usage vient souvent d'un autre service. »",
            texte="Ce tome est le cœur opérationnel de l'ouvrage. Chaque chapitre est consacré à un métier ou à un processus "
                  "de l'entreprise minière : il commence par un profil du métier, puis développe des cas d'usage concrets, "
                  "tirés du quotidien de Mbiyo Copper Cobalt SA, avec la méthode, le prompt, le contrôle qualité et le livrable final.",
            colonnes=[["Géologie et exploration", "Ressources et réserves", "Ingénierie et planification",
                       "Forage, minage et extraction", "Traitement et métallurgie", "Maintenance des équipements",
                       "Hygiène, sécurité, environnement", "Eau, résidus et fermeture"],
                      ["Relations communautaires", "Achats et logistique", "Droit minier et conformité",
                       "Finance, fiscalité, gestion", "Audit et contrôle interne", "Ressources humaines",
                       "Management et reporting", "ESG et traçabilité"]],
            chiffres="Partie III · chapitres 17 à 32 · 160 questions corrigées · 49 prompts commentés · bibliothèque de 124 prompts par métier"),
    3: dict(romain="III", titre="Méthodes, gouvernance et mise en pratique", accent="#6F8FC4", sombre="#4C6390",
            fosse=dict(cx=44, cy=42, rx=90, ry=44, seed=37),
            citation="« Utiliser Claude ponctuellement fait gagner du temps. Construire des méthodes transforme durablement "
                     "la manière de travailler d'une équipe. »",
            texte="Une entreprise minière manipule des informations stratégiques, des données personnelles, des informations "
                  "sensibles pour les marchés et les communautés, et prend chaque jour des décisions qui engagent la vie de ses "
                  "travailleurs. L'intelligence artificielle ne peut y être déployée sans règles. Ce dernier tome apprend à "
                  "construire des méthodes, à les encadrer et à les mettre à l'épreuve.",
            points=["Analyser des données et construire des tableaux de bord",
                    "Produire des livrables professionnels avec Claude",
                    "Créer des assistants spécialisés et des workflows contrôlés",
                    "Protéger les données et maîtriser les risques liés à l'IA",
                    "Déployer une politique d'utilisation de l'IA dans l'entreprise",
                    "Ateliers pratiques, évaluation des compétences et projet final"],
            chiffres="Parties IV à VI · chapitres 33 à 43 · 110 questions corrigées · ateliers, grille d'évaluation et projet final"),
}

def toile():
    fig = plt.figure(figsize=(15.5 / 2.54, 23.5 / 2.54)); ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 155); ax.set_ylim(0, 235); ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 155, 235, fc=FOND, ec="none", zorder=0))
    return fig, ax

def fosse(ax, accent, cx, cy, rx, ry, seed, n=24, lw=0.55, alpha=1.0, clip=None):
    """Courbes de niveau d'une fosse à ciel ouvert : gradins concentriques irréguliers et rampe en spirale."""
    rng = np.random.default_rng(seed); t = np.linspace(0, 2 * np.pi, 600)
    ph = rng.uniform(0, 2 * np.pi, 4)
    for i in range(n):
        k = 1 - i / (n + 2)
        r = 1 + 0.07 * np.sin(2 * t + ph[0]) + 0.045 * np.sin(3 * t + ph[1]) * k + 0.02 * np.sin(7 * t + ph[2])
        x = cx + rx * k * r * np.cos(t); y = cy + ry * k * r * np.sin(t) - (1 - k) * 6
        fort = i % 4 == 0
        line, = ax.plot(x, y, color=accent if fort else CREME, lw=lw * (1.4 if fort else 1),
                        alpha=alpha * (0.85 if fort else 0.30 + 0.35 * (1 - k)), zorder=2)
        if clip is not None: line.set_clip_path(clip)
    s = np.linspace(0, 1, 400); ang = -0.6 + 5.2 * np.pi * s; k = 1 - 0.92 * s
    line, = ax.plot(cx + rx * k * np.cos(ang), cy + ry * k * np.sin(ang) - 0.92 * s * 6, color=accent,
                    lw=lw * 1.1, alpha=alpha * 0.9, ls=(0, (6, 3)), zorder=3)
    if clip is not None: line.set_clip_path(clip)

def espace(txt):
    """Capitales espacées (interlettrage large)."""
    return "   ".join(" ".join(m) for m in txt.split(" "))

def texte(ax, x, y, s, size, font=REG, color=CREME, ha="center", **kw):
    ax.text(x, y, s, fontproperties=font, size=size, color=color, ha=ha, va="center", zorder=6, **kw)

def avant(n, c):
    fig, ax = toile()
    fosse(ax, c["accent"], **c["fosse"])
    ax.add_patch(Rectangle((0, 0), 155, 235, fc="none", ec=c["sombre"], lw=0.8, zorder=4))
    texte(ax, 77.5, 216, espace("GUIDE PROFESSIONNEL"), 8.5, color=c["accent"])
    texte(ax, 77.5, 200, espace(f"TOME {c['romain']}"), 11, color=c["accent"])
    texte(ax, 77.5, 178, espace("LA MINE"), 31)
    texte(ax, 77.5, 156, espace("AUGMENTÉE"), 31)
    ax.plot([60, 95], [142, 142], color=c["accent"], lw=0.9, zorder=5)
    lignes = textwrap.wrap(SOUS_TITRE, 44)
    for i, l in enumerate(lignes):
        texte(ax, 77.5, 131 - i * 7.2, l, 12.5, font=ITA)
    y = 131 - len(lignes) * 7.2 - 4
    for i, l in enumerate(textwrap.wrap(c["titre"].upper(), 44)):
        texte(ax, 77.5, y - i * 6, l, 9.5, color=c["accent"])
    ax.add_patch(Rectangle((0, 0), 155, 17, fc=FOND, ec="none", zorder=4))
    ax.plot([0, 155], [17, 17], color=c["sombre"], lw=0.6, zorder=4)
    texte(ax, 77.5, 9, espace(AUTEUR.upper()), 8.5)
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"tome{n}_couverture_avant.{ext}", dpi=300, facecolor=FOND)
    plt.close(fig)

def arriere(n, c):
    fig, ax = toile()
    clip = Rectangle((0, 0), 155, 235, transform=ax.transData)
    fosse(ax, c["accent"], 150, 228, 70, 48, seed=c["fosse"]["seed"] + 1, n=16, alpha=0.35, clip=clip)
    ax.add_patch(Rectangle((0, 0), 155, 235, fc="none", ec=c["sombre"], lw=0.8, zorder=4))
    texte(ax, 17, 214, espace(f"TOME {c['romain']}"), 8, color=c["accent"], ha="left")
    y = 202
    for l in textwrap.wrap(c["citation"], 58):
        texte(ax, 17, y, l, 10.5, font=ITA, ha="left"); y -= 5.9
    y -= 4
    for l in textwrap.wrap(c["texte"], 70):
        texte(ax, 17, y, l, 9, ha="left"); y -= 4.8
    y -= 5
    texte(ax, 17, y, espace("DANS CE TOME"), 8, color=c["accent"], ha="left"); y -= 7.5
    if "points" in c:
        for p_ in c["points"]:
            texte(ax, 17, y, "•", 9.4, color=c["accent"], ha="left")
            for l in textwrap.wrap(p_, 68):
                texte(ax, 22, y, l, 9, ha="left"); y -= 4.7
            y -= 1.3
    else:
        hauts = []
        for j, col in enumerate(c["colonnes"]):
            yy = y
            for p_ in col:
                texte(ax, 17 + j * 62, yy, "•", 9.2, color=c["accent"], ha="left")
                texte(ax, 22 + j * 62, yy, p_, 9.2, ha="left"); yy -= 5.4
            hauts.append(yy)
        y = min(hauts) - 1
    y -= 3
    for l in textwrap.wrap(c["chiffres"], 74):
        texte(ax, 17, y, l, 8.6, font=ITA, color=c["accent"], ha="left"); y -= 4.6
    # bloc auteur (pas d'ISBN, pas d'éditeur)
    ax.plot([17, 138], [40, 40], color=c["sombre"], lw=0.6, zorder=5)
    texte(ax, 17, 34, espace(AUTEUR.upper()), 8, color=c["accent"], ha="left")
    yy = 28
    for l in textwrap.wrap(BIO, 88):
        texte(ax, 17, yy, l, 7.8, ha="left", alpha=0.85); yy -= 3.9
    texte(ax, 17, 8, "Mines · Intelligence artificielle · Management", 7.5, ha="left", alpha=0.7)
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"tome{n}_couverture_arriere.{ext}", dpi=300, facecolor=FOND)
    plt.close(fig)

if __name__ == "__main__":
    for n, c in TOMES.items():
        avant(n, c); arriere(n, c)
    print("Couvertures produites dans", OUT)
