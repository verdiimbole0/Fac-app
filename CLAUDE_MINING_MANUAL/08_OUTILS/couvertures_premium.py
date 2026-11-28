# -*- coding: utf-8 -*-
"""Couvertures des tomes II (orange) et III (bleu marine), 1re et 4e, format 15,5 × 23,5 cm.
Même système typographique que le tome I (capitales espacées en Garamond, bandeau auteur),
avec une illustration technique propre à chaque tome :
- tome II : coupe géologique schématique d'une fosse à ciel ouvert (gradins, rampe, couches, corps minéralisé, sondages) ;
- tome III : plan de fosse en courbes de niveau sur quadrillage topographique, rose des vents et échelle (esprit « bleu d'ingénieur »).
Unités : millimètres (0 à 155 en largeur, 0 à 235 en hauteur)."""
import textwrap
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Rectangle, Polygon, FancyBboxPatch, Circle, PathPatch
from matplotlib.path import Path as MPath
from matplotlib.textpath import TextToPath

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "02_ILLUSTRATIONS" / "COUVERTURES"
FD = "/usr/share/fonts/opentype/ebgaramond/"
REG = FontProperties(fname=FD + "EBGaramond12-Regular.otf")
ITA = FontProperties(fname=FD + "EBGaramond12-Italic.otf")
_BOLD = ROOT / "08_OUTILS" / "polices" / "EBGaramond12-Bold.ttf"
BOLD = FontProperties(fname=str(_BOLD)) if _BOLD.exists() else REG
PT = 25.4 / 72  # 1 point en mm
SOUS_TITRE = "Maîtriser Claude et l'intelligence artificielle générative dans les métiers et les processus miniers"
AUTEUR = "Verdi Imbole"
_T2P = TextToPath()

# ---------------------------------------------------------------- outils communs
def toile():
    fig = plt.figure(figsize=(15.5 / 2.54, 23.5 / 2.54)); ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 155); ax.set_ylim(0, 235); ax.axis("off")
    return fig, ax

def fond(ax, haut, bas, vignette=0.18, grain=0.035, seed=1):
    """Dégradé vertical, vignettage doux et grain de papier."""
    h, w = 940, 620
    a, b = np.array(to_rgb(haut)), np.array(to_rgb(bas))
    v = np.linspace(0, 1, h)[:, None, None] ** 1.15
    img = a * (1 - v) + b * v
    img = np.repeat(img, w, axis=1)
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt(((xx - w / 2) / (w * 0.62)) ** 2 + ((yy - h * 0.42) / (h * 0.62)) ** 2)
    img = img * (1 - vignette * np.clip(d - 0.35, 0, 1)[..., None])
    rng = np.random.default_rng(seed)
    img = img + (rng.standard_normal((h, w))[..., None] * grain)
    ax.imshow(np.clip(img, 0, 1), extent=(0, 155, 0, 235), aspect="auto", zorder=0, interpolation="bilinear")

def largeur(s, size, font=REG):
    p = font.copy(); p.set_size(size)
    return _T2P.get_text_width_height_descent(s, p, ismath=False)[0] * PT

def trace(ax, x, y, s, size, font=REG, color="k", track=0.0, ha="center", z=8, alpha=1.0):
    """Texte avec interlettrage réel (track en fraction de la taille du corps)."""
    if not track:
        ax.text(x, y, s, fontproperties=font, size=size, color=color, ha=ha, va="center", zorder=z, alpha=alpha); return
    ws = [largeur(ch, size, font) if ch != " " else size * 0.28 * PT for ch in s]
    t = track * size * PT
    total = sum(ws) + t * (len(s) - 1)
    x0 = x - total / 2 if ha == "center" else (x - total if ha == "right" else x)
    for ch, w in zip(s, ws):
        if ch != " ":
            ax.text(x0, y, ch, fontproperties=font, size=size, color=color, ha="left", va="center", zorder=z, alpha=alpha)
        x0 += w + t
    return total

def paragraphe(ax, x, y, txt, size, wrap, font=REG, color="k", interligne=1.32, ha="left", alpha=1.0, z=8):
    for l in textwrap.wrap(txt, wrap):
        ax.text(x, y, l, fontproperties=font, size=size, color=color, ha=ha, va="center", zorder=z, alpha=alpha)
        y -= size * PT * interligne * 1.0
    return y

def losange(ax, x, y, r, color, z=8):
    ax.add_patch(Polygon([(x - r, y), (x, y + r * 0.8), (x + r, y), (x, y - r * 0.8)], closed=True, fc=color, ec="none", zorder=z))

def filet_orne(ax, xc, y, demi, color, lw=0.7, r=1.1, z=8):
    ax.plot([xc - demi, xc - r * 2.2], [y, y], color=color, lw=lw, zorder=z, solid_capstyle="butt")
    ax.plot([xc + r * 2.2, xc + demi], [y, y], color=color, lw=lw, zorder=z, solid_capstyle="butt")
    losange(ax, xc, y, r, color, z)

def pilule(ax, xc, y, txt, size, fc, tc, ec=None, track=0.32, pad=4.2, h=7.2):
    w = largeur(txt, size, BOLD) + track * size * PT * (len(txt) - 1) + 2 * pad
    ax.add_patch(FancyBboxPatch((xc - w / 2, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={h/2}",
                                fc=fc, ec=ec or fc, lw=0.7, zorder=7))
    trace(ax, xc, y + 0.15, txt, size, BOLD, tc, track)

def equilibre(txt, seuil=30):
    """Coupe un titre en deux lignes de longueurs voisines (pas de mot isolé)."""
    if len(txt) <= seuil: return [txt]
    m = txt.split(" ")
    k = min(range(1, len(m)), key=lambda i: abs(len(" ".join(m[:i])) - len(" ".join(m[i:]))))
    return [" ".join(m[:k]), " ".join(m[k:])]

def etiquette(ax, x, y, txt, size, fc, tc, ha="left", alpha=0.88, z=7.6, track=0.28):
    """Petite étiquette sur fond plein, lisible sur un dessin chargé."""
    w = largeur(txt, size) + track * size * PT * (len(txt) - 1); h = size * PT * 1.55
    x0 = x if ha == "left" else x - w
    ax.add_patch(FancyBboxPatch((x0 - 1.1, y - h / 2), w + 2.2, h, boxstyle="round,pad=0,rounding_size=0.8",
                                fc=fc, ec="none", alpha=alpha, zorder=z))
    trace(ax, x0, y + 0.1, txt, size, REG, tc, track, ha="left", z=z + 0.1)

def bloc_titre(ax, P, romain, titre_tome, y_haut=219):
    """Hiérarchie commune aux trois tomes : mention, titre, filet orné, sous-titre, pastille de tome, titre du tome."""
    trace(ax, 77.5, y_haut, "GUIDE PROFESSIONNEL", 7.4, REG, P["mention"], 0.42)
    trace(ax, 77.5, y_haut - 26, "LA MINE", 37, REG, P["titre"], 0.14)
    trace(ax, 77.5, y_haut - 49, "AUGMENTÉE", 37, REG, P["titre"], 0.14)
    filet_orne(ax, 77.5, y_haut - 63, 19, P["filet"], lw=0.75, r=1.15)
    y = y_haut - 73
    for l in textwrap.wrap(SOUS_TITRE, 42):
        ax.text(77.5, y, l, fontproperties=ITA, size=12.6, color=P["sous_titre"], ha="center", va="center", zorder=8); y -= 6.4
    y -= 5
    pilule(ax, 77.5, y, f"TOME {romain}", 8.4, P["pilule_fond"], P["pilule_texte"], P.get("pilule_bord"))
    y -= 9
    for l in equilibre(titre_tome.upper()):
        trace(ax, 77.5, y, l, 8.2, REG, P["tome"], 0.16); y -= 4.8
    return y

def bandeau_auteur(ax, P, h=17):
    ax.add_patch(Rectangle((0, 0), 155, h, fc=P["bandeau"], ec="none", zorder=9))
    ax.plot([0, 155], [h, h], color=P["bandeau_filet"], lw=0.8, zorder=10)
    trace(ax, 77.5, h / 2 + 0.3, AUTEUR.upper(), 10.5, REG, P["auteur"], 0.5, z=11)

def enregistrer(fig, nom):
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"{nom}.{ext}", dpi=300)
    plt.close(fig)

# ---------------------------------------------------------------- TOME II : orange, coupe géologique
O = dict(haut="#EE8436", bas="#C24F17", encre="#21150E", creme="#FFF3E2", sable="#FBD9B4",
         terre=["#B9501B", "#AA4717", "#C25A22", "#9D3F13", "#B04C1C", "#8F3711"], minerai="#21150E")
PO = dict(mention="#FFF3E2", titre="#21150E", filet="#21150E", sous_titre="#2A1A10", pilule_fond="#21150E",
          pilule_texte="#FFF3E2", tome="#FFF3E2", bandeau="#21150E", bandeau_filet="#FBD9B4", auteur="#FFF3E2")

def surface(x, base):
    return base + 1.3 * np.sin(x / 17.0) + 0.7 * np.sin(x / 6.5 + 1.2)

def profil_fosse(xL, xR, yb, x_fond, base, n=7, rampe=3):
    """Parois en gradins (talus + risberme), rampe élargie sur la paroi droite."""
    gauche = [(xL, surface(xL, base))]
    x, y = xL, surface(xL, base); h = (y - yb) / n
    f = 2.4; b = ((x_fond[0] - xL) - n * f) / n
    for i in range(n):
        x += f; y -= h; gauche.append((x, y))
        x += b if i < n - 1 else (x_fond[0] - x); gauche.append((x, y))
    droite = [(xR, surface(xR, base))]
    x, y = xR, surface(xR, base); h = (y - yb) / n
    larg = [1.0] * n; larg[rampe] = 2.6
    unite = ((xR - x_fond[1]) - n * f) / sum(larg)
    for i in range(n):
        x -= f; y -= h; droite.append((x, y))
        x -= unite * larg[i] if i < n - 1 else (x - x_fond[1]); droite.append((x, y))
    return gauche, droite[::-1]

def coupe_geologique(ax, base=93, bas=17, petite=False):
    xL, xR, yb = 22.0, 134.0, 41.0
    gauche, droite = profil_fosse(xL, xR, yb, (64.0, 86.0), base)
    xs = np.linspace(0, 155, 400)
    sol_g = [(x, surface(x, base)) for x in xs if x <= xL]
    sol_d = [(x, surface(x, base)) for x in xs if x >= xR]
    terrain = [(0, bas)] + sol_g + gauche + droite + sol_d + [(155, bas)]
    tp = MPath(terrain + [terrain[0]], closed=True)
    clip = PathPatch(tp, transform=ax.transData, fc="none", ec="none"); ax.add_patch(clip)
    # couches : limites ondulées et pendage léger vers la droite
    rng = np.random.default_rng(5)
    limites = [base + 8, 86, 77, 67, 57, 47, 37, 27, bas - 2]
    ph = rng.uniform(0, 6.3, len(limites))
    def lim(i, x): return limites[i] - 0.055 * (x - 77) + 1.4 * np.sin(x / 21 + ph[i]) + 0.6 * np.sin(x / 8 + ph[i] * 2)
    for i in range(len(limites) - 1):
        haut = [(x, lim(i, x)) for x in xs]; basl = [(x, lim(i + 1, x)) for x in xs[::-1]]
        p = Polygon(haut + basl, closed=True, fc=O["terre"][i % len(O["terre"])], ec="none", zorder=2)
        ax.add_patch(p); p.set_clip_path(clip)
        # figurés géologiques conventionnels
        motif = i % 4
        y0, y1 = limites[i + 1], limites[i]
        if motif == 0:      # grès : pointillés
            px = rng.uniform(0, 155, 900); py = rng.uniform(y0 - 6, y1 + 6, 900)
            sel = (py < lim(i, px)) & (py > lim(i + 1, px))
            sc = ax.scatter(px[sel], py[sel], s=0.35, c=O["creme"], alpha=0.38, lw=0, zorder=3); sc.set_clip_path(clip)
        elif motif == 1:    # schistes : tirets parallèles
            for yy in np.arange(y0 - 4, y1 + 4, 2.2):
                for x0 in np.arange(-3 + (yy * 7) % 6, 155, 6.5):
                    xx = np.array([x0, x0 + 3.2]); yl = yy - 0.055 * (xx - 77)
                    if lim(i + 1, x0) + 0.6 < yl[0] < lim(i, x0) - 0.6:
                        l, = ax.plot(xx, yl, color=O["creme"], lw=0.35, alpha=0.32, zorder=3); l.set_clip_path(clip)
        elif motif == 2:    # calcaires : briques
            for k, yy in enumerate(np.arange(y0 - 4, y1 + 4, 2.6)):
                l, = ax.plot(xs, yy - 0.055 * (xs - 77), color=O["creme"], lw=0.3, alpha=0.22, zorder=3); l.set_clip_path(clip)
                for x0 in np.arange((k % 2) * 3, 155, 6):
                    l, = ax.plot([x0, x0], [yy - 0.055 * (x0 - 77), yy + 2.6 - 0.055 * (x0 - 77)], color=O["creme"], lw=0.3, alpha=0.22, zorder=3)
                    l.set_clip_path(clip)
        else:               # roche cristalline : croix
            px = rng.uniform(0, 155, 170); py = rng.uniform(y0 - 6, y1 + 6, 170)
            for a, b_ in zip(px, py):
                if lim(i + 1, a) + 0.8 < b_ < lim(i, a) - 0.8:
                    for dx, dy in ((0.7, 0.7), (0.7, -0.7)):
                        l, = ax.plot([a - dx, a + dx], [b_ - dy, b_ + dy], color=O["creme"], lw=0.35, alpha=0.3, zorder=3)
                        l.set_clip_path(clip)
        l, = ax.plot(xs, [lim(i + 1, x) for x in xs], color=O["encre"], lw=0.45, alpha=0.55, zorder=3.5); l.set_clip_path(clip)
    # corps minéralisé : lentille pentée sous le fond de fosse
    t = np.linspace(0, 2 * np.pi, 300); a, b, ang = 46, 7.5, np.radians(-13)
    ex = 92 + a * np.cos(t) * np.cos(ang) - b * np.sin(t) * np.sin(ang) * (1 + 0.25 * np.cos(3 * t))
    ey = 37 + a * np.cos(t) * np.sin(ang) + b * np.sin(t) * np.cos(ang) * (1 + 0.25 * np.cos(3 * t))
    p = Polygon(np.c_[ex, ey], closed=True, fc=O["minerai"], ec=O["sable"], lw=0.7, zorder=4); ax.add_patch(p); p.set_clip_path(clip)
    px = rng.uniform(40, 145, 1400); py = rng.uniform(18, 55, 1400)
    inside = MPath(np.c_[ex, ey]).contains_points(np.c_[px, py])
    sc = ax.scatter(px[inside], py[inside], s=rng.uniform(0.2, 1.6, inside.sum()), c=O["haut"], alpha=0.75, lw=0, zorder=4.2)
    sc.set_clip_path(clip)
    # faille normale
    fx = np.array([146, 124]); fy = np.array([bas, base + 2])
    l, = ax.plot(fx, fy, color=O["encre"], lw=0.9, ls=(0, (5, 2.2)), zorder=5); l.set_clip_path(clip)
    for yy, s in ((48, 1), (64, -1)):
        xx = fx[0] + (yy - fy[0]) * (fx[1] - fx[0]) / (fy[1] - fy[0])
        ax.annotate("", xy=(xx + 2.2, yy + 3.2 * s), xytext=(xx + 2.2, yy), zorder=5,
                    arrowprops=dict(arrowstyle="-|>", color=O["encre"], lw=0.6, mutation_scale=5))
    # fosse : parois et surface
    prof = gauche + droite
    ax.plot([p_[0] for p_ in prof], [p_[1] for p_ in prof], color=O["encre"], lw=1.05, zorder=6, solid_joinstyle="miter")
    ax.plot(xs, surface(xs, base), color=O["encre"], lw=0.9, zorder=6)
    # sondages carottés inclinés : collet, intervalles d'échantillonnage, fond de trou
    for x0, angd, lg in ((11, -62, 64), (146, -118, 66), (75, -90, 20)):
        y0 = surface(x0, base) if x0 != 75 else yb
        dx, dy = np.cos(np.radians(angd)), np.sin(np.radians(angd))
        ax.plot([x0, x0 + dx * lg], [y0, y0 + dy * lg], color=O["creme"], lw=0.8, zorder=6.5)
        for k in np.arange(4, lg, 3.2):
            cx, cy = x0 + dx * k, y0 + dy * k
            ax.plot([cx - dy * 0.9, cx + dy * 0.9], [cy + dx * 0.9, cy - dx * 0.9], color=O["creme"], lw=0.45, zorder=6.5)
        ax.add_patch(Circle((x0, y0), 0.9, fc=O["encre"], ec=O["creme"], lw=0.6, zorder=7))
        ex_, ey_ = x0 + dx * lg, y0 + dy * lg
        ax.plot([ex_ - dy * 1.6, ex_ + dy * 1.6], [ey_ + dx * 1.6, ey_ - dx * 1.6], color=O["creme"], lw=0.9, zorder=6.5)
    if petite: return
    # engin de transport sur la rampe et chevalement de sondage en surface
    rx, ry = 116.5, droite[7][1]
    ax.add_patch(Polygon([(rx - 4.6, ry + 0.9), (rx + 1.2, ry + 0.9), (rx + 2.4, ry + 4.2), (rx - 4.6, ry + 4.2)], fc=O["encre"], ec="none", zorder=7))
    ax.add_patch(Rectangle((rx + 1.6, ry + 0.9), 2.6, 2.4, fc=O["encre"], ec="none", zorder=7))
    for wx in (rx - 3.0, rx + 2.6):
        ax.add_patch(Circle((wx, ry + 0.9), 0.95, fc=O["sable"], ec=O["encre"], lw=0.5, zorder=7.2))
    xd = 11; yd = surface(xd, base)
    ax.plot([xd - 2.2, xd, xd + 2.2], [yd, yd + 7.5, yd], color=O["encre"], lw=0.8, zorder=7)
    ax.plot([xd - 1.4, xd + 1.4], [yd + 2.6, yd + 2.6], color=O["encre"], lw=0.6, zorder=7)
    # légendes techniques (petites capitales)
    def legende(xp, yp, xt, yt, txt, ha="left"):
        ax.plot([xp, xt], [yp, yt], color=O["creme"], lw=0.4, zorder=7.5)
        ax.add_patch(Circle((xp, yp), 0.45, fc=O["creme"], ec="none", zorder=7.6))
        etiquette(ax, xt + (0.6 if ha == "left" else -0.6), yt, txt, 5.3, O["encre"], O["creme"], ha=ha)
    g = gauche[4]; legende(g[0] + 1.2, g[1] + 0.3, 24, 49, "GRADINS", ha="right")
    d = droite[7]; legende(d[0] - 3, d[1] + 0.3, 126, 80.5, "RAMPE", ha="right")
    legende(112, 31.5, 120, 23.5, "CORPS MINÉRALISÉ")
    legende(16.5, 72, 4.5, 63, "SONDAGE")
    legende(137.5, 60, 145.5, 70, "FAILLE", ha="right")
    etiquette(ax, 5.5, bas + 3.6, "COUPE SCHÉMATIQUE · SANS ÉCHELLE", 4.6, O["encre"], O["sable"], alpha=0.7)

def legende_geologique(ax, x, y):
    """Légende des figurés de la coupe, comme sur une carte géologique."""
    trace(ax, x, y + 9, "LÉGENDE DE LA COUPE", 6, BOLD, O["encre"], 0.4, ha="left")
    items = [("Grès", 0), ("Schistes", 1), ("Calcaires", 2), ("Socle", 3), ("Minerai", 4)]
    rng = np.random.default_rng(9)
    for k, (nom, m) in enumerate(items):
        x0 = x + k * 25; w, h = 9, 6
        ax.add_patch(Rectangle((x0, y - h / 2), w, h, fc=O["terre"][k % 4] if m < 4 else O["minerai"], ec=O["encre"], lw=0.6, zorder=6))
        if m == 0:
            ax.scatter(rng.uniform(x0 + 0.5, x0 + w - 0.5, 40), rng.uniform(y - h / 2 + 0.5, y + h / 2 - 0.5, 40), s=0.5, c=O["creme"], lw=0, zorder=7)
        elif m == 1:
            for yy in np.arange(y - 2, y + 2.5, 1.6):
                for xx in (x0 + 0.8, x0 + 5): ax.plot([xx, xx + 3], [yy, yy], color=O["creme"], lw=0.4, zorder=7)
        elif m == 2:
            for j, yy in enumerate(np.arange(y - h / 2 + 1.5, y + h / 2, 1.5)):
                ax.plot([x0, x0 + w], [yy, yy], color=O["creme"], lw=0.35, alpha=0.7, zorder=7)
                for xx in np.arange(x0 + 1.5 + (j % 2) * 1.5, x0 + w, 3):
                    ax.plot([xx, xx], [yy - 1.5, yy], color=O["creme"], lw=0.35, alpha=0.7, zorder=7)
        elif m == 3:
            for xx, yy in ((x0 + 2.5, y + 1), (x0 + 6.5, y - 1.2), (x0 + 4.5, y + 1.8)):
                ax.plot([xx - 0.7, xx + 0.7], [yy - 0.7, yy + 0.7], color=O["creme"], lw=0.4, zorder=7)
                ax.plot([xx - 0.7, xx + 0.7], [yy + 0.7, yy - 0.7], color=O["creme"], lw=0.4, zorder=7)
        else:
            ax.scatter(rng.uniform(x0 + 0.5, x0 + w - 0.5, 30), rng.uniform(y - h / 2 + 0.5, y + h / 2 - 0.5, 30), s=rng.uniform(0.3, 2, 30), c=O["haut"], lw=0, zorder=7)
        ax.text(x0 + w + 1.8, y, nom, fontproperties=REG, size=7.4, color=O["encre"], ha="left", va="center", zorder=7)

def tome2_avant(c):
    fig, ax = toile(); fond(ax, O["haut"], O["bas"], seed=2)
    # courbes de niveau très discrètes dans le ciel (rappel du tome I)
    t = np.linspace(0, 2 * np.pi, 400)
    for k in range(1, 14):
        r = 1 + 0.06 * np.sin(2 * t + 1) + 0.03 * np.sin(5 * t)
        ax.plot(150 + 9 * k * r * np.cos(t), 232 + 7 * k * r * np.sin(t), color=O["creme"], lw=0.4, alpha=0.11, zorder=1)
    bloc_titre(ax, PO, c["romain"], c["titre"])
    coupe_geologique(ax)
    bandeau_auteur(ax, PO)
    enregistrer(fig, "tome2_couverture_avant")

def tome2_arriere(c):
    fig, ax = toile(); fond(ax, O["haut"], O["bas"], seed=3)
    trace(ax, 17, 219, f"TOME {c['romain']}", 8, BOLD, O["encre"], 0.45, ha="left")
    ax.plot([17, 50], [214.5, 214.5], color=O["encre"], lw=0.6)
    ax.text(14, 205, "«", fontproperties=ITA, size=44, color=O["creme"], ha="left", va="center", alpha=0.9)
    y = paragraphe(ax, 27, 204, c["citation"].strip("« »"), 13, 50, ITA, O["encre"], 1.3)
    y = paragraphe(ax, 17, y - 4, c["texte"], 9.4, 74, REG, O["encre"], 1.42)
    # panneau « Dans ce tome » : métiers numérotés
    y -= 3; h = 61
    ax.add_patch(FancyBboxPatch((13, y - h), 129, h, boxstyle="round,pad=0,rounding_size=2.2", fc=O["encre"], ec="none", zorder=5))
    trace(ax, 20, y - 6.5, "DANS CE TOME", 7.6, BOLD, O["sable"], 0.42, ha="left")
    yy0 = y - 14
    for j, col in enumerate(c["colonnes"]):
        yy = yy0
        for k, m in enumerate(col):
            n = 17 + j * 8 + k
            ax.text(20 + j * 62, yy, f"{n}", fontproperties=REG, size=8.2, color=O["haut"], ha="left", va="center", zorder=6)
            ax.text(27 + j * 62, yy, m, fontproperties=REG, size=8.8, color=O["creme"], ha="left", va="center", zorder=6)
            yy -= 5.6
    y = y - h - 6
    y = paragraphe(ax, 17, y, c["chiffres"], 8.6, 80, ITA, O["encre"], 1.35)
    legende_geologique(ax, 17, 52)
    # bandeau auteur
    ax.add_patch(Rectangle((0, 0), 155, 40, fc=O["encre"], ec="none", zorder=5))
    ax.plot([0, 155], [40, 40], color=O["sable"], lw=0.8, zorder=6)
    trace(ax, 17, 32, AUTEUR.upper(), 9, REG, O["creme"], 0.48, ha="left", z=7)
    paragraphe(ax, 17, 25, c["bio"], 7.7, 92, REG, O["sable"], 1.35, z=7)
    trace(ax, 17, 6.5, "MINES · INTELLIGENCE ARTIFICIELLE · MANAGEMENT", 5.6, REG, O["haut"], 0.32, ha="left", z=7)
    enregistrer(fig, "tome2_couverture_arriere")

# ---------------------------------------------------------------- TOME III : bleu marine, plan de fosse
M = dict(haut="#17305A", bas="#0A1830", trait="#CFE0F5", or_="#D9AE5A", creme="#F4EEDF", nuit="#081326")
PM = dict(mention="#D9AE5A", titre="#F4EEDF", filet="#D9AE5A", sous_titre="#DCE6F2", pilule_fond="#0A1830",
          pilule_texte="#D9AE5A", pilule_bord="#D9AE5A", tome="#D9AE5A", bandeau="#081326", bandeau_filet="#D9AE5A", auteur="#F4EEDF")

def quadrillage(ax, y0=0, y1=235, fort=0.11, faible=0.045):
    for x in np.arange(0, 156, 5):
        ax.plot([x, x], [y0, y1], color=M["trait"], lw=0.25 if x % 25 else 0.4, alpha=faible if x % 25 else fort, zorder=1)
    for y in np.arange(0, 236, 5):
        ax.plot([0, 155], [y, y], color=M["trait"], lw=0.25 if y % 25 else 0.4, alpha=faible if y % 25 else fort, zorder=1)

def cadre_coordonnees(ax, m=6.5):
    ax.add_patch(Rectangle((m, m), 155 - 2 * m, 235 - 2 * m, fc="none", ec=M["trait"], lw=0.5, alpha=0.45, zorder=2))
    for x in np.arange(25, 155, 25):
        for yb, s in ((m, 1), (235 - m, -1)):
            ax.plot([x, x], [yb, yb + 2.2 * s], color=M["trait"], lw=0.5, alpha=0.6, zorder=2)
    for y in np.arange(25, 235, 25):
        for xb, s in ((m, 1), (155 - m, -1)):
            ax.plot([xb, xb + 2.2 * s], [y, y], color=M["trait"], lw=0.5, alpha=0.6, zorder=2)

def plan_fosse(ax, cx=77.5, cy=55, R=38, petite=False):
    # rose des vents / cercle gradué
    t = np.linspace(0, 2 * np.pi, 720)
    for rr, lw, a in ((R, 0.7, 0.75), (R + 3.2, 0.4, 0.45)):
        ax.plot(cx + rr * np.cos(t), cy + rr * np.sin(t), color=M["or_"], lw=lw, alpha=a, zorder=3)
    for k in range(72):
        ang = np.radians(k * 5); L = 3.2 if k % 6 == 0 else 1.5
        ax.plot([cx + R * np.cos(ang), cx + (R + L) * np.cos(ang)], [cy + R * np.sin(ang), cy + (R + L) * np.sin(ang)],
                color=M["or_"], lw=0.5 if k % 6 else 0.8, alpha=0.8, zorder=3)
    if not petite:
        for lab, ang in (("N", 90), ("E", 0), ("S", 270), ("O", 180)):
            a = np.radians(ang); trace(ax, cx + (R + 7.2) * np.cos(a), cy + (R + 7.2) * np.sin(a), lab, 7.5, BOLD, M["or_"], 0)
    # fosse en courbes de niveau, teintes de plus en plus profondes
    rng = np.random.default_rng(37); ph = rng.uniform(0, 6.3, 4)
    n = 17
    for i in range(n):
        k = 1 - i / (n + 1.5)
        r = 1 + 0.08 * np.sin(2 * t + ph[0]) + 0.05 * np.sin(3 * t + ph[1]) * k + 0.018 * np.sin(8 * t + ph[2])
        x = cx + (R - 6) * k * r * np.cos(t) * 1.06; y = cy + (R - 6) * k * r * np.sin(t) * 0.86 - (1 - k) * 4
        teinte = np.array(to_rgb(M["haut"])) * (1 - i / n) + np.array(to_rgb(M["nuit"])) * (i / n)
        ax.fill(x, y, color=teinte, lw=0, zorder=3.5 + i * 0.01)
        fort = i % 4 == 0
        ax.plot(x, y, color=M["or_"] if fort else M["trait"], lw=0.8 if fort else 0.45, alpha=0.95 if fort else 0.6, zorder=4 + i * 0.01)
        if fort and not petite and i < n - 2:
            j = 470 + i * 9
            cote = f"{1320 - i * 10:,}".replace(",", " ")
            ax.text(x[j], y[j], cote, fontproperties=REG, size=4.6, color=M["or_"], ha="center", va="center", zorder=5,
                    bbox=dict(boxstyle="round,pad=0.12", fc=teinte, ec="none"))
    # rampe en spirale
    s = np.linspace(0, 1, 500); ang = 0.4 + 4.6 * np.pi * s; k = 1 - 0.9 * s
    ax.plot(cx + (R - 6) * k * np.cos(ang) * 1.06, cy + (R - 6) * k * np.sin(ang) * 0.86 - 0.9 * s * 4,
            color=M["creme"], lw=0.7, ls=(0, (4, 2)), alpha=0.85, zorder=5)
    if petite: return
    # points topographiques et ligne de coupe
    for (px, py, lab) in ((cx - 30, cy + 18, "P1"), (cx + 33, cy + 12, "P2"), (cx + 6, cy - 31, "P3")):
        ax.add_patch(Polygon([(px - 1.3, py - 0.9), (px + 1.3, py - 0.9), (px, py + 1.3)], fc=M["creme"], ec="none", zorder=6))
        trace(ax, px + 2.2, py + 1.6, lab, 5, REG, M["creme"], 0.1, ha="left", z=6)
    ax.plot([cx - R + 2, cx + R - 2], [cy - 9, cy + 9], color=M["or_"], lw=0.6, ls=(0, (6, 1.5, 1, 1.5)), zorder=5.5)
    for (px, py, lab) in ((cx - R + 2, cy - 9, "A"), (cx + R - 2, cy + 9, "B")):
        ax.add_patch(Circle((px, py), 2.2, fc=M["nuit"], ec=M["or_"], lw=0.6, zorder=6))
        trace(ax, px, py, lab, 6, BOLD, M["or_"], 0, z=6.5)
    # flèche du nord et échelle graphique
    nx, ny = 139, 92
    ax.add_patch(Polygon([(nx, ny + 6), (nx - 2, ny - 1.5), (nx, ny), ], fc=M["creme"], ec="none", zorder=6))
    ax.add_patch(Polygon([(nx, ny + 6), (nx + 2, ny - 1.5), (nx, ny)], fc="none", ec=M["creme"], lw=0.5, zorder=6))
    trace(ax, nx, ny + 9, "N", 6.5, BOLD, M["creme"], 0)
    ex, ey = 121, 70
    for i in range(4):
        ax.add_patch(Rectangle((ex + i * 6, ey), 6, 1.4, fc=M["creme"] if i % 2 == 0 else "none", ec=M["creme"], lw=0.4, zorder=6))
    for i, v in enumerate(("0", "50", "100", "150", "200 m")):
        ax.text(ex + i * 6, ey + 3.4, v, fontproperties=REG, size=4.6, color=M["creme"], ha="center", va="center", zorder=6)
    trace(ax, 145, ey - 4.5, "PLAN DE FOSSE", 4.8, REG, M["trait"], 0.3, ha="right", z=6, alpha=0.85)
    trace(ax, 145, ey - 8.3, "ÉQUIDISTANCE 10 M", 4.8, REG, M["trait"], 0.3, ha="right", z=6, alpha=0.85)

def legende_carto(ax, x, y):
    trace(ax, x, y + 9, "LÉGENDE DU PLAN", 6, BOLD, M["or_"], 0.4, ha="left")
    pas = 31
    ax.plot([x, x + 8], [y, y], color=M["or_"], lw=0.9); ax.text(x + 10, y, "Courbe maîtresse", fontproperties=REG, size=7.4, color=M["creme"], va="center")
    x1 = x + pas + 4
    ax.plot([x1, x1 + 8], [y, y], color=M["creme"], lw=0.8, ls=(0, (4, 2))); ax.text(x1 + 10, y, "Rampe", fontproperties=REG, size=7.4, color=M["creme"], va="center")
    x2 = x1 + 24
    ax.add_patch(Polygon([(x2 + 2.7, y - 0.9), (x2 + 5.3, y - 0.9), (x2 + 4, y + 1.3)], fc=M["creme"], ec="none"))
    ax.text(x2 + 8, y, "Point topographique", fontproperties=REG, size=7.4, color=M["creme"], va="center")
    x3 = x2 + 38
    ax.plot([x3, x3 + 8], [y, y], color=M["or_"], lw=0.6, ls=(0, (6, 1.5, 1, 1.5))); ax.text(x3 + 10, y, "Ligne de coupe", fontproperties=REG, size=7.4, color=M["creme"], va="center")

def tome3_avant(c):
    fig, ax = toile(); fond(ax, M["haut"], M["bas"], vignette=0.22, grain=0.03, seed=4)
    quadrillage(ax); cadre_coordonnees(ax)
    bloc_titre(ax, PM, c["romain"], c["titre"])
    plan_fosse(ax)
    bandeau_auteur(ax, PM)
    enregistrer(fig, "tome3_couverture_avant")

def tome3_arriere(c):
    fig, ax = toile(); fond(ax, M["haut"], M["bas"], vignette=0.22, grain=0.03, seed=5)
    quadrillage(ax, fort=0.07, faible=0.03); cadre_coordonnees(ax)
    trace(ax, 17, 219, f"TOME {c['romain']}", 8, BOLD, M["or_"], 0.45, ha="left")
    ax.plot([17, 50], [214.5, 214.5], color=M["or_"], lw=0.6)
    ax.text(14, 205, "«", fontproperties=ITA, size=44, color=M["or_"], ha="left", va="center")
    y = paragraphe(ax, 27, 204, c["citation"].strip("« »"), 13, 50, ITA, M["creme"], 1.3)
    y = paragraphe(ax, 17, y - 4, c["texte"], 9.4, 74, REG, "#DCE6F2", 1.42)
    y -= 4
    trace(ax, 17, y, "DANS CE TOME", 7.6, BOLD, M["or_"], 0.42, ha="left"); y -= 8
    for k, p_ in enumerate(c["points"]):
        ax.add_patch(Rectangle((17, y - 1.6), 3.2, 3.2, fc="none", ec=M["or_"], lw=0.6, zorder=6))
        trace(ax, 18.6, y, str(k + 1), 5.6, BOLD, M["or_"], 0, z=7)
        ax.text(24, y, p_, fontproperties=REG, size=9, color=M["creme"], ha="left", va="center", zorder=6)
        y -= 6
    y -= 2
    y = paragraphe(ax, 17, y, c["chiffres"], 8.6, 80, ITA, M["or_"], 1.35)
    legende_carto(ax, 17, 52)
    ax.add_patch(Rectangle((0, 0), 155, 40, fc=M["nuit"], ec="none", zorder=5))
    ax.plot([0, 155], [40, 40], color=M["or_"], lw=0.8, zorder=6)
    trace(ax, 17, 32, AUTEUR.upper(), 9, REG, M["creme"], 0.48, ha="left", z=7)
    paragraphe(ax, 17, 25, c["bio"], 7.7, 92, REG, "#C9D6E6", 1.35, z=7)
    trace(ax, 17, 6.5, "MINES · INTELLIGENCE ARTIFICIELLE · MANAGEMENT", 5.6, REG, M["or_"], 0.32, ha="left", z=7)
    enregistrer(fig, "tome3_couverture_arriere")

def produire(tomes, bio):
    c2 = dict(tomes[2], bio=bio); c3 = dict(tomes[3], bio=bio)
    tome2_avant(c2); tome2_arriere(c2); tome3_avant(c3); tome3_arriere(c3)

if __name__ == "__main__":
    import couvertures as cv
    produire(cv.TOMES, cv.BIO); print("Tomes II et III produits dans", OUT)
