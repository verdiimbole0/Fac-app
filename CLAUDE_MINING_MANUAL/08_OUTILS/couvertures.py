# -*- coding: utf-8 -*-
"""Couvertures (1re et 4e) des trois tomes, format 15,5 × 23,5 cm.
Tome I : fond anthracite et cuivre. Tome II : orange pastel et blanc. Tome III : bleu pastel et or sable.
Les trois partagent la fosse en courbes de niveau, la typographie et la hiérarchie des textes.
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
    2: dict(romain="II", titre="Claude dans les métiers et les processus miniers", accent="#C8693A", sombre="#E9A273",
            clair=dict(fond="#FFFFFF", encre="#3A2A22", accent="#C8693A", pastel="#F6B98A", motif="metiers",
                       bandes=["#FFFFFF", "#FEF3EA", "#FCE4D1", "#F9D2B4", "#F6BE95", "#F2AA79", "#EC9762"],
                       panneau="#FEF3EA", bande="#FCE4D1", trait="#FFFFFF"),
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
    3: dict(romain="III", titre="Méthodes, gouvernance et mise en pratique", accent="#B08A3E", sombre="#D9BC82",
            clair=dict(fond="#FFFFFF", encre="#1D3354", accent="#B08A3E", pastel="#A9CBE8", motif="quadrillage",
                       bandes=["#FFFFFF", "#F1F7FC", "#E0EDF8", "#CCE0F2", "#B6D2EC", "#9EC2E4", "#86B1DA"],
                       panneau="#EEF5FB", bande="#DDEBF7", trait="#FFFFFF"),
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

def theme(c):
    """Thème sombre par défaut (tomes I et III) ; le tome II a un thème clair (blanc, orange et bleu pastel)."""
    th = dict(fond=FOND, texte=CREME, doux=c["accent"], lignes=CREME, fort=c["accent"], remplissage=None,
              bande=FOND, bande_texte=CREME, panneau=None)
    th.update(c.get("theme", {}))
    return th

def lavis(ax, th, y0, y1, haut):
    """Lavis vertical très léger : la couleur `haut` se fond dans le fond de page."""
    from matplotlib.colors import to_rgb
    a, b = np.array(to_rgb(th["fond"])), np.array(to_rgb(haut))
    g = np.linspace(0, 1, 256) ** 1.6
    img = (a[None, :] * (1 - g[:, None]) + b[None, :] * g[:, None])[::-1][:, None, :]
    ax.imshow(img, extent=(0, 155, y0, y1), aspect="auto", zorder=0.5, interpolation="bicubic")

def toile(fond=FOND):
    fig = plt.figure(figsize=(15.5 / 2.54, 23.5 / 2.54)); ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 155); ax.set_ylim(0, 235); ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 155, 235, fc=fond, ec="none", zorder=0))
    return fig, ax

def degrade(couleurs, u):
    """Couleur interpolée le long d'une suite de couleurs (u entre 0 et 1)."""
    from matplotlib.colors import to_rgb
    pts = [np.array(to_rgb(c)) for c in couleurs]
    x = u * (len(pts) - 1); i = min(int(x), len(pts) - 2); f = x - i
    return tuple(pts[i] * (1 - f) + pts[i + 1] * f)

def fosse(ax, accent, cx, cy, rx, ry, seed, n=24, lw=0.55, alpha=1.0, clip=None, th=None):
    """Courbes de niveau d'une fosse à ciel ouvert : gradins concentriques irréguliers et rampe en spirale.
    Avec un thème à remplissage, chaque gradin est teinté : plus la fosse est profonde, plus le bleu s'affirme."""
    th = th or dict(lignes=CREME, fort=accent, remplissage=None)
    rng = np.random.default_rng(seed); t = np.linspace(0, 2 * np.pi, 600)
    ph = rng.uniform(0, 2 * np.pi, 4)
    for i in range(n):
        k = 1 - i / (n + 2)
        r = 1 + 0.07 * np.sin(2 * t + ph[0]) + 0.045 * np.sin(3 * t + ph[1]) * k + 0.02 * np.sin(7 * t + ph[2])
        x = cx + rx * k * r * np.cos(t); y = cy + ry * k * r * np.sin(t) - (1 - k) * 6
        fort = i % 4 == 0
        if th.get("remplissage"):
            poly, = ax.fill(x, y, color=degrade(th["remplissage"], i / (n - 1)), alpha=alpha, lw=0, zorder=1.5)
            if clip is not None: poly.set_clip_path(clip)
            a = alpha * (0.95 if fort else 0.55 + 0.35 * (1 - k))
        else:
            a = alpha * (0.85 if fort else 0.30 + 0.35 * (1 - k))
        line, = ax.plot(x, y, color=th["fort"] if fort else th["lignes"], lw=lw * (1.5 if fort else 1),
                        alpha=a, zorder=2)
        if clip is not None: line.set_clip_path(clip)
    s = np.linspace(0, 1, 400); ang = -0.6 + 5.2 * np.pi * s; k = 1 - 0.92 * s
    line, = ax.plot(cx + rx * k * np.cos(ang), cy + ry * k * np.sin(ang) - 0.92 * s * 6, color=th["fort"],
                    lw=lw * 1.1, alpha=alpha * 0.9, ls=(0, (6, 3)), zorder=3)
    if clip is not None: line.set_clip_path(clip)

def espace(txt):
    """Capitales espacées (interlettrage large)."""
    return "   ".join(" ".join(m) for m in txt.split(" "))

def texte(ax, x, y, s, size, font=REG, color=CREME, ha="center", **kw):
    ax.text(x, y, s, fontproperties=font, size=size, color=color, ha=ha, va="center", zorder=6, **kw)

def avant(n, c):
    th = theme(c); T = th["texte"]
    fig, ax = toile(th["fond"])
    if c.get("theme"): lavis(ax, th, 118, 235, th.get("ciel", "#E4EEF9"))
    fosse(ax, c["accent"], th=th, **c["fosse"])
    if c.get("theme"):   # double filet fin : orange pastel à l'extérieur, bleu pastel à l'intérieur
        ax.add_patch(Rectangle((4, 4), 147, 227, fc="none", ec=th["fort"], lw=0.9, zorder=4))
        ax.add_patch(Rectangle((6, 6), 143, 223, fc="none", ec=th["lignes"], lw=0.45, zorder=4))
    else:
        ax.add_patch(Rectangle((0, 0), 155, 235, fc="none", ec=c["sombre"], lw=0.8, zorder=4))
    texte(ax, 77.5, 216, espace("GUIDE PROFESSIONNEL"), 8.5, color=c["accent"])
    texte(ax, 77.5, 200, espace(f"TOME {c['romain']}"), 11, color=c["accent"])
    texte(ax, 77.5, 178, espace("LA MINE"), 31, color=T)
    texte(ax, 77.5, 156, espace("AUGMENTÉE"), 31, color=T)
    if c.get("theme"):
        ax.plot([58, 76], [142, 142], color=th["fort"], lw=1.6, zorder=5, solid_capstyle="round")
        ax.plot([79, 97], [142, 142], color=th["lignes"], lw=1.6, zorder=5, solid_capstyle="round")
    else:
        ax.plot([60, 95], [142, 142], color=c["accent"], lw=0.9, zorder=5)
    lignes = textwrap.wrap(SOUS_TITRE, 44)
    for i, l in enumerate(lignes):
        texte(ax, 77.5, 131 - i * 7.2, l, 12.5, font=ITA, color=T)
    y = 131 - len(lignes) * 7.2 - 4
    tt = c["titre"].upper()
    for i, l in enumerate(textwrap.wrap(tt, 44 if len(tt) <= 44 else len(tt) // 2 + 3)):
        texte(ax, 77.5, y - i * 6, l, 9.5, color=th["doux"])
    ax.add_patch(Rectangle((0, 0), 155, 17, fc=th["bande"], ec="none", zorder=4.5))
    ax.plot([0, 155], [17, 17], color=c["sombre"] if not c.get("theme") else th["fort"], lw=0.6, zorder=4.6)
    texte(ax, 77.5, 9, espace(AUTEUR.upper()), 8.5, color=th["bande_texte"])
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"tome{n}_couverture_avant.{ext}", dpi=300, facecolor=th["fond"])
    plt.close(fig)

def arriere(n, c):
    th = theme(c); T = th["texte"]; clair = bool(c.get("theme"))
    fig, ax = toile(th["fond"])
    clip = Rectangle((0, 0), 155, 235, transform=ax.transData)
    if clair: lavis(ax, th, 150, 235, "#EAF1FA")
    fosse(ax, c["accent"], *((160, 236, 62, 42) if clair else (150, 228, 70, 48)), seed=c["fosse"]["seed"] + 1, n=16,
          alpha=0.5 if clair else 0.35, clip=clip, th=th)
    if clair:
        ax.add_patch(Rectangle((4, 4), 147, 227, fc="none", ec=th["fort"], lw=0.9, zorder=4))
        ax.add_patch(Rectangle((6, 6), 143, 223, fc="none", ec=th["lignes"], lw=0.45, zorder=4))
    else:
        ax.add_patch(Rectangle((0, 0), 155, 235, fc="none", ec=c["sombre"], lw=0.8, zorder=4))
    texte(ax, 17, 214, espace(f"TOME {c['romain']}"), 8, color=c["accent"], ha="left")
    y = 202
    if clair: ax.plot([13, 13], [y + 3, y - 5.9 * len(textwrap.wrap(c["citation"], 58)) + 3], color=th["fort"], lw=1.6, zorder=5)
    for l in textwrap.wrap(c["citation"], 58):
        texte(ax, 17, y, l, 10.5, font=ITA, ha="left", color=T); y -= 5.9
    y -= 4
    for l in textwrap.wrap(c["texte"], 70):
        texte(ax, 17, y, l, 9, ha="left", color=T); y -= 4.8
    y -= 5
    texte(ax, 17, y, espace("DANS CE TOME"), 8, color=c["accent"], ha="left"); y -= 7.5
    if "points" in c:
        for p_ in c["points"]:
            texte(ax, 17, y, "•", 9.4, color=c["accent"], ha="left")
            for l in textwrap.wrap(p_, 68):
                texte(ax, 22, y, l, 9, ha="left", color=T); y -= 4.7
            y -= 1.3
    else:
        hauts = []
        if clair:   # panneau bleu pastel derrière la liste des métiers
            hlist = 5.4 * max(len(col) for col in c["colonnes"]) + 4
            from matplotlib.patches import FancyBboxPatch
            ax.add_patch(FancyBboxPatch((13, y - hlist + 3.5), 129, hlist, boxstyle="round,pad=0,rounding_size=2.5",
                                        fc=th["panneau"], ec=th["lignes"], lw=0.5, zorder=4.8))
        for j, col in enumerate(c["colonnes"]):
            yy = y
            for p_ in col:
                texte(ax, 17 + j * 62, yy, "•", 9.2, color=c["accent"], ha="left")
                texte(ax, 22 + j * 62, yy, p_, 9.2, ha="left", color=T); yy -= 5.4
            hauts.append(yy)
        y = min(hauts) - 1
    y -= 3
    for l in textwrap.wrap(c["chiffres"], 74):
        texte(ax, 17, y, l, 8.6, font=ITA, color=th["doux"] if clair else c["accent"], ha="left"); y -= 4.6
    # bloc auteur (pas d'ISBN, pas d'éditeur)
    if clair:
        ax.add_patch(Rectangle((6, 6), 143, 40, fc=th["bande"], ec="none", alpha=0.55, zorder=4.2))
        ax.plot([6, 149], [46, 46], color=th["fort"], lw=0.9, zorder=5)
    else:
        ax.plot([17, 138], [40, 40], color=c["sombre"], lw=0.6, zorder=5)
    texte(ax, 17, 34, espace(AUTEUR.upper()), 8, color=T if clair else c["accent"], ha="left")
    yy = 28
    for l in textwrap.wrap(BIO, 88):
        texte(ax, 17, yy, l, 7.8, ha="left", alpha=0.9 if clair else 0.85, color=T); yy -= 3.9
    texte(ax, 17, 11 if clair else 8, "Mines · Intelligence artificielle · Management", 7.5, ha="left", alpha=0.75, color=T)
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"tome{n}_couverture_arriere.{ext}", dpi=300, facecolor=th["fond"])
    plt.close(fig)

# ---------------------------------------------------------------- maquette claire (tomes II et III)
from matplotlib.patches import FancyBboxPatch, Polygon
BOLD = FontProperties(fname=str(Path(__file__).resolve().parent / "polices" / "EBGaramond12-Bold.ttf"))

def anneau(cx, cy, rx, ry, k, ph, t):
    r = 1 + 0.07 * np.sin(2 * t + ph[0]) + 0.045 * np.sin(3 * t + ph[1]) * k + 0.02 * np.sin(7 * t + ph[2])
    return cx + rx * k * r * np.cos(t), cy + ry * k * r * np.sin(t) - (1 - k) * 7

def relief(ax, P, cx, cy, rx, ry, seed, n=22, clip=None, alpha=1.0, points=0):
    """Fosse en gradins : chaque gradin est une plage de couleur, son talus une ombre portée,
    son arête un filet blanc ; la rampe d'accès est tracée en tirets."""
    from matplotlib.colors import to_rgb
    rng = np.random.default_rng(seed); t = np.linspace(0, 2 * np.pi, 720); ph = rng.uniform(0, 2 * np.pi, 4)
    objets = []
    for i in range(n):
        k = 1 - i / (n + 1.5); u = i / (n - 1)
        x, y = anneau(cx, cy, rx, ry, k, ph, t)
        col = np.array(degrade(P["bandes"], u))
        objets += ax.fill(x, y - 1.3, color=tuple(col * 0.86), lw=0, alpha=alpha * 0.55, zorder=1.4)   # talus
        objets += ax.fill(x, y, color=tuple(col), lw=0, alpha=alpha, zorder=1.5)                   # gradin
        objets += ax.plot(x, y, color=P["trait"], lw=0.7 if i % 4 else 1.2, alpha=alpha * 0.95, zorder=1.6)
        if i % 4 == 0 and i:
            objets += ax.plot(x, y - 1.3, color=P["accent"], lw=0.35, alpha=alpha * 0.45, zorder=1.55)
    s_ = np.linspace(0, 1, 500); ang = -0.6 + 5.2 * np.pi * s_; k = 1 - 0.9 * s_
    objets += ax.plot(cx + rx * k * np.cos(ang), cy + ry * k * np.sin(ang) - 0.9 * s_ * 7, color=P["accent"],
                      lw=0.9, alpha=alpha * 0.9, ls=(0, (5, 2.5)), zorder=1.7)
    if points:   # un repère par métier, posé sur un même gradin
        kk = 1 - 7 / (n + 1.5); tp = np.linspace(0, 2 * np.pi, points, endpoint=False) + 0.2
        x, y = anneau(cx, cy, rx, ry, kk, ph, tp)
        objets += [ax.scatter(x, y, s=16, c=P["fond"], edgecolors=P["accent"], linewidths=0.9, zorder=1.8, alpha=alpha)]
    if clip is not None:
        for o in objets: o.set_clip_path(clip)

def cadre_carto(ax, P):
    """Cadre cartographique : filet fin et graduation alternée, comme sur une carte topographique."""
    m, e = 5.5, 1.5
    ax.add_patch(Rectangle((m, m), 155 - 2 * m, 235 - 2 * m, fc="none", ec=P["encre"], lw=0.45, zorder=7))
    ax.add_patch(Rectangle((m + e, m + e), 155 - 2 * (m + e), 235 - 2 * (m + e), fc="none", ec=P["encre"], lw=0.3, zorder=7))
    pas = 10
    for x0 in np.arange(m, 155 - m, pas):
        if int((x0 - m) / pas) % 2 == 0:
            for y0 in (m, 235 - m - e):
                ax.add_patch(Rectangle((x0, y0), min(pas, 155 - m - x0), e, fc=P["accent"], ec="none", alpha=0.85, zorder=7))
    for y0 in np.arange(m, 235 - m, pas):
        if int((y0 - m) / pas) % 2 == 0:
            for x0 in (m, 155 - m - e):
                ax.add_patch(Rectangle((x0, y0), e, min(pas, 235 - m - y0), fc=P["accent"], ec="none", alpha=0.85, zorder=7))

def nord(ax, P, x, y, h=9):
    ax.add_patch(Polygon([(x, y + h), (x - 2.2, y), (x, y + 2), (x + 2.2, y)], closed=True, fc=P["encre"], ec="none", zorder=6))
    ax.add_patch(Polygon([(x, y + h), (x + 2.2, y), (x, y + 2)], closed=True, fc=P["fond"], ec=P["encre"], lw=0.4, zorder=6))
    texte(ax, x, y + h + 3.2, "N", 7.5, font=BOLD, color=P["encre"])

def fondu(ax, blanc, teinte, y0, y1):
    """Teinte pastel en bas de page qui se fond progressivement dans le blanc, sans arête visible."""
    from matplotlib.colors import to_rgb
    a, b = np.array(to_rgb(teinte)), np.array(to_rgb(blanc))
    g = (np.linspace(0, 1, 400) ** 1.3)[:, None]
    img = (a * (1 - g) + b * g)[::-1][:, None, :]
    ax.imshow(img, extent=(0, 155, y0, y1), aspect="auto", zorder=0.5, interpolation="bicubic")

def quadrillage(ax, P, y_max):
    """Quadrillage d'arpentage dont l'intensité décroît vers le haut."""
    from matplotlib.colors import to_rgba
    def a_(y): return max(0.0, 1 - y / y_max) ** 0.8
    for x in np.arange(15, 155, 15):
        ys = np.linspace(0, y_max, 40)
        for y_a, y_b in zip(ys[:-1], ys[1:]):
            ax.plot([x, x], [y_a, y_b], color=P["accent"], lw=0.25, alpha=0.4 * a_(y_a), zorder=1.9)
    for y in np.arange(10, y_max, 15):
        ax.plot([0, 155], [y, y], color=P["accent"], lw=0.25, alpha=0.4 * a_(y), zorder=1.9)
    for x in np.arange(15, 155, 15):
        for y in np.arange(10, y_max, 15):
            ax.plot([x - 0.9, x + 0.9], [y, y], color=P["accent"], lw=0.5, alpha=0.9 * a_(y), zorder=1.95)
            ax.plot([x, x], [y - 0.9, y + 0.9], color=P["accent"], lw=0.5, alpha=0.9 * a_(y), zorder=1.95)

def _quadrillage_ancien(ax, P, y_max):
    for x in np.arange(15, 155, 15):
        ax.plot([x, x], [0, y_max], color=P["accent"], lw=0.25, alpha=0.35, zorder=1.9)
    for y in np.arange(10, y_max, 15):
        ax.plot([0, 155], [y, y], color=P["accent"], lw=0.25, alpha=0.35, zorder=1.9)
    for x in np.arange(15, 155, 15):          # croisillons d'arpentage
        for y in np.arange(10, y_max, 15):
            ax.plot([x - 0.9, x + 0.9], [y, y], color=P["accent"], lw=0.5, alpha=0.8, zorder=1.95)
            ax.plot([x, x], [y - 0.9, y + 0.9], color=P["accent"], lw=0.5, alpha=0.8, zorder=1.95)

def pastille(ax, x, y, txt, P, w=26, h=7.5):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={h / 2}",
                                fc=P["pastel"], ec="none", zorder=6))
    texte(ax, x, y + 0.2, espace(txt), 9.5, font=BOLD, color=P["encre"])

def avant_clair(n, c):
    P = c["clair"]; E = P["encre"]
    fig, ax = toile(P["fond"])
    clip = Rectangle((5.5, 5.5), 144, 224, transform=ax.transData)
    fondu(ax, P["fond"], P["panneau"], 0, 125)
    if P["motif"] == "quadrillage": quadrillage(ax, P, 125)
    cx, cy = (96, 40) if n == 2 else (60, 40)
    relief(ax, P, cx, cy, 98, 58, seed=c["fosse"]["seed"], clip=clip, points=16 if P["motif"] == "metiers" else 0)
    nord(ax, P, 138 if n == 2 else 140, 82)
    cadre_carto(ax, P)
    texte(ax, 77.5, 216, espace("GUIDE PROFESSIONNEL"), 8.2, color=P["accent"])
    pastille(ax, 77.5, 203, f"TOME {c['romain']}", P)
    texte(ax, 77.5, 181, espace("LA MINE"), 33, color=E)
    texte(ax, 77.5, 158, espace("AUGMENTÉE"), 33, color=E)
    ax.plot([62, 74], [145, 145], color=P["accent"], lw=1.2, zorder=6, solid_capstyle="round")
    ax.add_patch(Polygon([(77.5, 147), (79.5, 145), (77.5, 143), (75.5, 145)], closed=True, fc=P["accent"], ec="none", zorder=6))
    ax.plot([81, 93], [145, 145], color=P["accent"], lw=1.2, zorder=6, solid_capstyle="round")
    lignes = textwrap.wrap(SOUS_TITRE, 44)
    for i, l in enumerate(lignes):
        texte(ax, 77.5, 134 - i * 7, l, 12.5, font=ITA, color=E)
    y = 134 - len(lignes) * 7 - 4.5
    tt = c["titre"].upper()
    for i, l in enumerate(textwrap.wrap(tt, 44 if len(tt) <= 44 else len(tt) // 2 + 3)):
        texte(ax, 77.5, y - i * 6, l, 9.8, font=BOLD, color=P["accent"])
    ax.add_patch(FancyBboxPatch((44, 10.5), 67, 9, boxstyle="round,pad=0,rounding_size=1.2", fc=P["fond"], ec=P["accent"], lw=0.6, zorder=6))
    texte(ax, 77.5, 15.2, espace(AUTEUR.upper()), 8.8, font=BOLD, color=E)
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"tome{n}_couverture_avant.{ext}", dpi=300, facecolor=P["fond"])
    plt.close(fig)

def arriere_clair(n, c):
    P = c["clair"]; E = P["encre"]
    fig, ax = toile(P["fond"])
    clip = Rectangle((5.5, 5.5), 144, 224, transform=ax.transData)
    relief(ax, P, 150, 232, 72, 46, seed=c["fosse"]["seed"] + 1, n=16, clip=clip, alpha=0.75)
    cadre_carto(ax, P)
    pastille(ax, 30, 214, f"TOME {c['romain']}", P, w=28)
    y = 199
    cit = textwrap.wrap(c["citation"].replace("« ", "«\u00a0").replace(" »", "\u00a0»"), 42 if n == 3 else 44)
    ax.plot([14, 14], [y + 3.4, y - 7.4 * len(cit) + 3.8], color=P["accent"], lw=2, zorder=6, solid_capstyle="round")
    for l in cit:
        texte(ax, 19, y, l, 13.5, font=ITA, ha="left", color=E); y -= 7.4
    y -= 5
    for l in textwrap.wrap(c["texte"], 68):
        texte(ax, 14, y, l, 9.9, ha="left", color=E); y -= 5.3
    y -= 7
    texte(ax, 14, y, espace("DANS CE TOME"), 8.2, font=BOLD, color=P["accent"], ha="left"); y -= 4
    if "colonnes" in c:
        haut = 6.2 * max(len(col) for col in c["colonnes"]) + 7
        ax.add_patch(FancyBboxPatch((12, y - haut), 131, haut, boxstyle="round,pad=0,rounding_size=2.5",
                                    fc=P["panneau"], ec=P["pastel"], lw=0.7, zorder=4.8))
        y -= 5.5; hauts = []
        for j, col in enumerate(c["colonnes"]):
            yy = y
            for k_, p_ in enumerate(col):
                num = j * len(col) + k_ + 17
                texte(ax, 17 + j * 64, yy, str(num), 8, font=BOLD, color=P["accent"], ha="left")
                texte(ax, 24 + j * 64, yy, p_, 9.6, ha="left", color=E); yy -= 6.2
            hauts.append(yy)
        y = min(hauts) - 2
    else:
        y -= 4
        for k_, p_ in enumerate(c["points"]):
            ax.add_patch(Rectangle((14.2, y - 1.2), 2.4, 2.4, fc=P["pastel"], ec=P["accent"], lw=0.5, zorder=6))
            for l in textwrap.wrap(p_, 64):
                texte(ax, 20.5, y, l, 10, ha="left", color=E); y -= 5.3
            y -= 2
    y -= 3
    y -= 2
    for l in textwrap.wrap(c["chiffres"], 72):
        texte(ax, 14, y, l, 9.2, font=ITA, color=P["accent"], ha="left"); y -= 4.9
    # bloc auteur sur bande pastel
    ax.add_patch(Rectangle((7, 7), 141, 41, fc=P["bande"], ec="none", zorder=4.2))
    ax.plot([7, 148], [48, 48], color=P["accent"], lw=0.9, zorder=5)
    texte(ax, 14, 40, espace(AUTEUR.upper()), 8.6, font=BOLD, color=E, ha="left")
    yy = 33.5
    for l in textwrap.wrap(BIO, 86):
        texte(ax, 14, yy, l, 7.9, ha="left", color=E); yy -= 4
    texte(ax, 14, 12.5, "Mines · Intelligence artificielle · Management", 7.5, ha="left", color=P["accent"])
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"tome{n}_couverture_arriere.{ext}", dpi=300, facecolor=P["fond"])
    plt.close(fig)

if __name__ == "__main__":
    for n, c in TOMES.items():
        if "clair" in c: avant_clair(n, c); arriere_clair(n, c)
        else: avant(n, c); arriere(n, c)
    print("Couvertures produites dans", OUT)
