#!/usr/bin/env python3
"""Génère les schémas originaux de l'ouvrage (SVG) + versions PNG pour le DOCX.
Tous les schémas sont des créations originales (aucune source externe)."""
import pathlib, math, cairosvg

OUT = pathlib.Path(__file__).resolve().parent.parent / "03_ILLUSTRATIONS" / "schemas"
OUT.mkdir(parents=True, exist_ok=True)
VC, BORD = "#8DBB9A", "#7B1E30"
NAVY, NAVY2, GOLD, GOLDL, GRAY, LINE, INK, MUTED = "#0A1E3F", "#14305C", "#2D5A3B", "#E6EFE8", "#F2F4F7", "#D9DEE6", "#1D2433", "#5A6476"
RED, ORANGE, YEL, GREEN = "#7B1E30", "#C9687A", "#E3B6BE", "#2D5A3B"
FIGS = {}

def fig(fn):
    FIGS[fn.__name__] = fn
    return fn

def svg(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{NAVY}"/></marker>
<marker id="arg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{GOLD}"/></marker></defs>
<rect width="{w}" height="{h}" fill="white"/>{body}</svg>'''

def T(x, y, s, size=13, color=INK, weight=400, anchor="middle", fam="Source Sans 3", italic=False, ls=0):
    lines = s.split("\n")
    out = []
    for i, l in enumerate(lines):
        dy = (i - (len(lines) - 1) / 2) * size * 1.18
        st = ' font-style="italic"' if italic else ""
        l = l.replace("&", "&amp;").replace("<", "&lt;")
        out.append(f'<text x="{x}" y="{y+dy+size*0.35:.1f}" font-family="{fam}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}" letter-spacing="{ls}"{st}>{l}</text>')
    return "".join(out)

def M(x, y, s, size=12, color=NAVY, weight=700, anchor="middle", ls=0.5):
    return T(x, y, s, size, color, weight, anchor, "Montserrat", ls=ls)

def R(x, y, w, h, fill=GRAY, stroke="none", sw=1, rx=7):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def A(x1, y1, x2, y2, color=NAVY, sw=1.8, dash=None, marker="ar"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{d} marker-end="url(#{marker})"/>'

def L(x1, y1, x2, y2, color=LINE, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{d}/>'

def sq(x, y, n, s=26, fill=BORD, color="white"):
    return R(x, y, s, s, fill, rx=4) + M(x + s / 2, y + s / 2, str(n), 13, color, 800, ls=0)

def card(x, y, w, h, title, text, n=None, head=NAVY, tsize=12.5):
    b = R(x, y, w, h, GRAY) + R(x, y, w, 34, head)
    b += M(x + (w / 2 if n is None else w / 2 + 12), y + 17, title, 11.5, "white", 700)
    if n is not None:
        b += sq(x, y, n, 34)
    b += T(x + w / 2, y + 34 + (h - 34) / 2, text, tsize, INK)
    return b

# ------------------------------------------------------------------ CH1
@fig
def fig01_types_archives():
    w, h = 900, 430
    b = R(360, 170, 180, 90, NAVY) + M(450, 205, "UNE ARCHIVE", 15, "white", 800) + T(450, 232, "se caractérise par…", 12.5, "#C9D3E3", italic=True)
    items = [
        (40, 30, "SUPPORT", "Physique (papier, photo, plan)\nNumérique natif\nNumérisé"),
        (620, 30, "STATUT", "Publique\nPrivée (entreprise, ASBL,\nfamille, personne)"),
        (40, 290, "FONCTION", "Administrative · Comptable\nJuridique · RH\nTechnique · Programmes"),
        (620, 290, "ÂGE ET UTILITÉ", "Courante\nIntermédiaire\nDéfinitive"),
    ]
    for i, (x, y, t, s) in enumerate(items, 1):
        b += R(x, y, 240, 110, GRAY) + R(x, y, 6, 110, GOLD) + M(x + 125, y + 22, t, 12.5, NAVY, 800, ls=1.5) + T(x + 125, y + 68, s, 13)
        cx, cy = (x + 240, y + 55) if x < 400 else (x, y + 55)
        b += L(cx, cy, 450 + (-90 if x < 400 else 90), 215 + (-45 if y < 200 else 45), GOLD, 1.6)
    b += R(330, 330, 240, 64, "white", GOLD, 1.2) + T(450, 362, "Ces critères se combinent :\nun contrat peut être numérique,\nprivé, juridique et courant.", 11.5, MUTED, italic=True)
    return svg(w, h, b)

@fig
def fig02_missions_archiviste():
    w, h = 900, 330
    ms = [("CONSEILLER", "les services sur\nla création des\ndocuments"), ("COLLECTER", "les documents\nqui ne servent plus\nau quotidien"),
          ("CLASSER\nET DÉCRIRE", "pour rendre les\ndocuments\nretrouvables"), ("CONSERVER", "dans des conditions\nqui garantissent\nleur intégrité"),
          ("COMMUNIQUER", "aux personnes\nautorisées, en\nsécurité"), ("ÉVALUER", "pour décider du\nsort final avec\nla direction")]
    bw = 136
    body = ""
    for i, (t, s) in enumerate(ms):
        x = 15 + i * (bw + 10)
        body += R(x, 40, bw, 250, GRAY) + R(x, 40, bw, 92, NAVY) + sq(x + bw / 2 - 15, 26, i + 1, 30)
        body += M(x + bw / 2, 94, t, 11.5, "white", 800, ls=0.8) + T(x + bw / 2, 205, s, 13)
        if i < 5:
            body += A(x + bw + 1, 165, x + bw + 9, 165, GOLD, 2, marker="arg")
    return svg(w, h, body)


# ------------------------------------------------------------------ Parcours / Horizon
@fig
def fig00_horizon():
    w, h = 900, 360
    b = R(330, 10, 240, 50, NAVY) + M(450, 35, "ORGANISATION HORIZON", 12.5, "white", 800, ls=1)
    b += T(450, 74, "ASBL fictive · 42 salariés · siège + 2 antennes", 12, MUTED, italic=True)
    sv = [("DIR", "Direction\ngénérale"), ("FIN", "Administration\net Finances"), ("RHU", "Ressources\nhumaines"),
          ("PRG", "Programmes\net Projets"), ("LOG", "Logistique\net Achats"), ("COM", "Communication\net Partenariats")]
    for i, (c, n) in enumerate(sv):
        x = 20 + i * 145
        b += L(450, 60, x + 65, 100, LINE, 1.2) + R(x, 100, 130, 82, GRAY) + R(x, 100, 130, 26, GOLD) + M(x + 65, 113, c, 12, "white", 800) + T(x + 65, 154, n, 12.5)
    b += M(450, 210, "PLAN DE CLASSEMENT FONCTIONNEL", 11, BORD, 800, ls=1.5)
    fn = ["01 Gouvernance", "02 Finances", "03 Ressources\nhumaines", "04 Programmes", "05 Partenariats", "06 Logistique", "07 Communication"]
    for i, f in enumerate(fn):
        x = 20 + i * 124.5
        b += R(x, 230, 116, 70, NAVY) + T(x + 58, 265, f, 12, "white", 600)
    b += T(450, 330, "Les services produisent, les fonctions organisent : un même service peut alimenter plusieurs rubriques.", 12, MUTED, italic=True)
    return svg(w, h, b)

# ------------------------------------------------------------------ CH2
@fig
def fig03_cycle_vie():
    """Roue de processus façon plaquette : arcs gris, pictogrammes, légendes en renvoi."""
    w, h = 900, 600
    cx, cy, R = 450, 305, 185
    ARC = "#C3CCDC"
    icons = [
        '<rect x="-20" y="-16" width="40" height="30" rx="2"/><path d="M-20 -16 L0 2 L20 -16"/><path d="M8 6 h18 M17 -3 v18" stroke="#2D5A3B"/>',
        '<rect x="-17" y="-22" width="30" height="42" rx="2"/><path d="M-10 -12h16M-10 -4h16M-10 4h10"/><path d="M10 18 l14 -22 l5 3 l-14 22 z" stroke="#2D5A3B"/>',
        '<path d="M-22 -8 h36 l-8 -8 M22 8 h-36 l8 8"/><circle cx="0" cy="0" r="3" fill="#2D5A3B" stroke="#2D5A3B"/>',
        '<rect x="-22" y="-8" width="44" height="28" rx="2"/><path d="M-24 -16 h48 v8 h-48 z M-7 4 h14" /><rect x="-9" y="0" width="18" height="9" stroke="#2D5A3B"/>',
        '<path d="M-14 -22 h28 M-14 22 h28 M-11 -22 c0 14 22 14 22 22 s-22 8 -22 22 M11 -22 c0 14 -22 14 -22 22 s22 8 22 22" transform="scale(1 0.98)"/><path d="M-5 16 h10" stroke="#2D5A3B"/>',
    ]
    steps = [("1. Création ou réception", "Le document entre dans\nla sphère de l'organisation"),
             ("2. Enregistrement", "Il reçoit date, numéro\net dossier (capture)"),
             ("3. Utilisation et circulation", "Traité, validé, transmis :\nun seul détenteur de l'original"),
             ("4. Conservation", "Rangé dans son dossier,\naux conditions adaptées"),
             ("5. Sort final", "Conservation, tri ou\ndestruction autorisée")]
    b = ""
    # cercle central
    b += f'<circle cx="{cx}" cy="{cy}" r="88" fill="{NAVY}"/>' + M(cx, cy - 22, "CYCLE DE VIE", 13, "white", 800, ls=1.5) + M(cx, cy - 2, "DU DOCUMENT", 13, "white", 800, ls=1.5)
    b += f'<line x1="{cx-28}" y1="{cy+16}" x2="{cx+28}" y2="{cy+16}" stroke="{GOLD}" stroke-width="2.4"/>' + T(cx, cy + 40, "traçabilité\nà chaque étape", 12, "#C9D3E3", italic=True)
    for i in range(5):
        ang = math.radians(-90 + i * 72)
        x, y = cx + R * math.cos(ang), cy + R * math.sin(ang)
        # arc gris ouvert vers l'extérieur (comme les « C » de la plaquette)
        r2 = 54; C = 2 * math.pi * r2
        rot = math.degrees(ang) + 0.36 * 180
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r2}" fill="none" stroke="{ARC}" stroke-width="20" stroke-dasharray="{0.64*C:.1f} {0.36*C:.1f}" transform="rotate({rot:.1f} {x:.1f} {y:.1f})"/>'
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="42" fill="white"/>'
        b += f'<g transform="translate({x:.1f} {y:.1f})" fill="none" stroke="{NAVY}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">{icons[i]}</g>'
        # renvoi et légende
        t, d = steps[i]
        lx = x + (95 if math.cos(ang) > 0.2 else -95 if math.cos(ang) < -0.2 else 0)
        ly = y + (-82 if i == 0 else 92 if math.sin(ang) > 0.5 else 0)
        if i == 0:
            b += M(x + 150, y - 30, t, 12.5, NAVY, 800, anchor="start", ls=0) + T(x + 150, y - 4, d, 12, INK, anchor="start")
            b += L(x + 66, y - 30, x + 142, y - 30, "#9AA2B1", 1.2) + f'<circle cx="{x+142}" cy="{y-30:.1f}" r="2.5" fill="{GOLD}"/>'
        else:
            right = math.cos(ang) > 0
            ex = x + (92 if right else -92)
            tx = ex + (14 if right else -14)
            anchor = "start" if right else "end"
            b += L(x + (66 if right else -66), y, ex, y, "#9AA2B1", 1.2) + f'<circle cx="{ex}" cy="{y:.1f}" r="2.5" fill="{GOLD}"/>'
            b += M(tx, y - 14, t, 12.5, NAVY, 800, anchor=anchor, ls=0) + T(tx, y + 14, d, 12, INK, anchor=anchor)
    return svg(w, h, b)

@fig
def fig04_trois_ages():
    w, h = 900, 330
    ages = [("1er ÂGE", "ARCHIVES COURANTES", "Usage quotidien\nDans les services", "Service producteur", NAVY2),
            ("2e ÂGE", "ARCHIVES INTERMÉDIAIRES", "Usage occasionnel\nLocal de préarchivage", "Archiviste + service", NAVY),
            ("3e ÂGE", "ARCHIVES DÉFINITIVES", "Intérêt historique\nou probant durable", "Archiviste", "#071530")]
    b = ""
    for i, (a, t, d, resp, col) in enumerate(ages):
        x = 20 + i * 290
        b += f'<path d="M{x} 40 H{x+250} L{x+275} 95 L{x+250} 150 H{x} L{x+25} 95 Z" fill="{col}"/>' if i else f'<path d="M{x} 40 H{x+250} L{x+275} 95 L{x+250} 150 H{x} Z" fill="{col}"/>'
        b += M(x + 140, 75, a, 12, VC, 800, ls=2) + M(x + 140, 105, t, 12, "white", 700)
        b += R(x + 10, 170, 250, 90, GRAY) + T(x + 135, 200, d, 13) + T(x + 135, 245, "Responsable : " + resp, 12, MUTED, italic=True)
    b += A(40, 295, 860, 295, GOLD, 2, marker="arg") + M(150, 312, "CRÉATION", 10, MUTED, 700, ls=1) + M(440, 312, "FIN DE LA DUA", 10, MUTED, 700, ls=1) + M(760, 312, "SANS LIMITE", 10, MUTED, 700, ls=1)
    b += L(310, 285, 310, 305, GOLD, 2) + L(600, 285, 600, 305, GOLD, 2) + T(455, 282, "tri et sort final", 11, GOLD, italic=True)
    return svg(w, h, b)

@fig
def fig05_modeles_gestion():
    w, h = 900, 300
    b = ""
    titles = [("CENTRALISÉE", "Un service d'archives\nunique gère tout", "+ cohérence  / – lenteur"),
              ("DÉCENTRALISÉE", "Chaque service gère\nses propres archives", "+ proximité  / – hétérogénéité"),
              ("MIXTE", "Courant dans les services,\nintermédiaire et définitif\ncentralisés", "+ équilibre recommandé")]
    for i, (t, d, p) in enumerate(titles):
        x = 15 + i * 295
        hl = i == 2
        b += R(x, 10, 275, 280, GOLDL if hl else GRAY) + R(x, 10, 275, 36, GOLD if hl else NAVY) + M(x + 137, 28, t, 12.5, "white", 800, ls=1)
        cx = x + 137
        if i == 0:
            b += R(cx - 40, 70, 80, 40, NAVY) + M(cx, 90, "ARCHIVES", 9.5, "white", 800)
            for k in range(4):
                sx = x + 25 + k * 62
                b += R(sx, 160, 50, 30, "white", NAVY, 1.2) + M(sx + 25, 175, "S" + str(k + 1), 10) + A(sx + 25, 158, cx, 112)
        elif i == 1:
            for k in range(4):
                sx = x + 25 + k * 62
                b += R(sx, 75, 50, 30, "white", NAVY, 1.2) + M(sx + 25, 90, "S" + str(k + 1), 10) + R(sx + 5, 150, 40, 40, NAVY2) + M(sx + 25, 170, "A", 10, "white") + A(sx + 25, 107, sx + 25, 148)
        else:
            for k in range(4):
                sx = x + 25 + k * 62
                b += R(sx, 65, 50, 30, "white", NAVY, 1.2) + M(sx + 25, 80, "S" + str(k + 1), 10) + T(sx + 25, 108, "courant", 9.5, MUTED, italic=True) + A(sx + 25, 118, cx, 148)
            b += R(cx - 55, 150, 110, 40, NAVY) + M(cx, 170, "CENTRAL", 9.5, "white", 800)
        b += T(cx, 228, d, 12.5) + M(cx, 272, p, 10, GOLD if hl else NAVY2, 700, ls=0)
    return svg(w, h, b)

@fig
def fig06_circuit_facture():
    w, h = 900, 250
    st = [("RÉCEPTION", "Accueil\nregistre + tampon"), ("SERVICE FAIT", "LOG\nrapprochement"), ("VALIDATION", "PRG\nvisa budgétaire"),
          ("COMPTABILISATION", "FIN\nn° de pièce"), ("PAIEMENT", "RAF\n« Payé le »"), ("CLASSEMENT", "FIN\nHOR/02.03")]
    b = ""
    for i, (t, d) in enumerate(st):
        x = 10 + i * 148
        b += R(x, 50, 128, 120, GRAY) + R(x, 50, 128, 34, NAVY) + M(x + 64, 67, t, 9.6, "white", 800, ls=0.2) + sq(x + 51, 30, i + 1, 26) + T(x + 64, 128, d, 12.5)
        if i < 5:
            b += A(x + 129, 110, x + 146, 110, GOLD, 2.2, marker="arg")
    b += R(10, 195, 880, 40, GOLDL) + T(450, 215, "Un seul détenteur de l'original à chaque étape · une trace datée à chaque passage · aucun paiement sur simple copie", 12.5, NAVY, 600)
    return svg(w, h, b)

# ------------------------------------------------------------------ CH3
@fig
def fig07_methodes_classement():
    w, h = 900, 330
    ms = [("ALPHABÉTIQUE", "A … Z", "Personnel, fournisseurs,\nadhérents"), ("NUMÉRIQUE", "001 … 999", "Factures, commandes,\nprojets"),
          ("CHRONOLOGIQUE", "2024 … 2026", "Courrier, PV,\nrelevés bancaires"), ("GÉOGRAPHIQUE", "Site · Région", "Organisations\nmultisites"),
          ("THÉMATIQUE", "Sujet", "Documentation,\ndossiers de référence"), ("FONCTIONNEL", "Fonction › activité", "Plan de classement\nde l'organisation")]
    b = ""
    for i, (t, sym, u) in enumerate(ms):
        x = 15 + (i % 3) * 295; y = 10 + (i // 3) * 160
        hl = i == 5
        b += R(x, y, 275, 145, GOLDL if hl else GRAY) + R(x, y, 8, 145, GOLD)
        b += M(x + 140, y + 28, t, 12.5, NAVY, 800, ls=1) + M(x + 140, y + 62, sym, 15, GOLD if not hl else NAVY2, 300, ls=0) + T(x + 140, y + 108, u, 12.5)
        if hl:
            b += R(x + 175, y + 125, 95, 18, NAVY) + M(x + 222, y + 134, "RECOMMANDÉ", 8.5, "white", 800, ls=0.8)
    return svg(w, h, b)

# ------------------------------------------------------------------ CH4
@fig
def fig08_anatomie_cote():
    w, h = 900, 270
    segs = [("HOR", "Organisation", "Préfixe de\nl'organisme", 130), ("02.03", "Rubrique", "Code du plan\nde classement", 170), ("2026", "Année", "Année d'ouverture\ndu dossier", 150), ("0157", "N° d'ordre", "Numéro continu dans\nla rubrique et l'année", 170)]
    x = 70; b = ""
    for i, (v, l, d, wd) in enumerate(segs):
        b += R(x, 30, wd, 70, NAVY if i % 2 == 0 else NAVY2) + M(x + wd / 2, 65, v, 24, "white", 300, ls=1)
        b += L(x + wd / 2, 100, x + wd / 2, 125, GOLD, 2) + M(x + wd / 2, 140, l.upper(), 10.5, GOLD, 800, ls=1) + T(x + wd / 2, 178, d, 12)
        if i < 3:
            b += M(x + wd + 11, 65, "/", 26, GOLD, 300)
        x += wd + 22
    b += R(70, 215, 760, 42, GRAY) + T(450, 236, "Localisation séparée : A-02-3-045 = local A · travée 02 · tablette 3 · boîte 045", 13, NAVY, 600)
    return svg(w, h, b)

# ------------------------------------------------------------------ CH5
@fig
def fig09_facteurs_degradation():
    w, h = 900, 300
    fs = [("HUMIDITÉ", "Moisissures, gondolage,\nencres qui coulent", "HR modérée et stable"), ("CHALEUR", "Acidification accélérée,\ncondensation", "Fraîcheur stable"),
          ("LUMIÈRE", "Jaunissement, encres\npâlies (cumulatif)", "Obscurité, filtres UV"), ("POUSSIÈRE", "Abrasion, acidité,\nnourrit les nuisibles", "Boîtes fermées, aspiration"),
          ("NUISIBLES", "Papier rongé, galeries,\ndéjections", "Propreté, pièges"), ("SINISTRES", "Eau, feu, vol,\nmanipulations", "Prévention, plan d'urgence")]
    b = ""
    for i, (t, e, p) in enumerate(fs):
        x = 10 + i * 148
        b += R(x, 10, 136, 280, GRAY) + R(x, 10, 136, 40, NAVY) + M(x + 68, 30, t, 10.5, "white", 800, ls=0.5)
        b += M(x + 68, 72, "EFFETS", 9, GOLD, 800, ls=1.5) + T(x + 68, 115, e, 11.8)
        b += L(x + 18, 160, x + 118, 160, LINE, 1) + M(x + 68, 182, "PRÉVENTION", 9, GOLD, 800, ls=1.5) + T(x + 68, 222, p, 12, NAVY, 600)
    return svg(w, h, b)

@fig
def fig10_local_comparatif():
    w, h = 900, 380
    b = ""
    for side in (0, 1):
        x0 = 10 + side * 450
        b += R(x0, 10, 430, 360, "#F5E6E9" if side == 0 else "#E6EFE8")
        b += R(x0, 10, 430, 38, RED if side == 0 else GREEN) + M(x0 + 215, 29, "À RISQUE" if side == 0 else "BONNES PRATIQUES", 12.5, "white", 800, ls=1.5)
        # sol + rayonnage
        b += L(x0 + 20, 300, x0 + 410, 300, INK, 2)
        if side == 0:
            b += f'<path d="M{x0+300} 60 v30 h40" stroke="{MUTED}" stroke-width="6" fill="none"/>' + f'<path d="M{x0+330} 96 q4 10 0 14 q-4 -4 0 -14z" fill="#4A90C2"/>'
            for k in range(4):
                b += R(x0 + 40 + k * 55, 258 - (k % 2) * 8, 48, 42 + (k % 2) * 8, "#D3D9E3", "#8E99AD", 1)
            b += R(x0 + 40, 296, 230, 6, "#4A90C2")
            b += R(x0 + 330, 160, 60, 80, "#F2F4F7", MUTED, 1) + T(x0 + 360, 200, "soleil", 11, MUTED, italic=True)
            for k in range(6):
                b += f'<circle cx="{x0+70+k*35}" cy="{200+(k%3)*12}" r="4" fill="#6B7486" opacity=".7"/>'
            notes = ["Cartons au sol, déformés", "Canalisation au-dessus", "Fenêtre plein soleil", "Taches de moisissure"]
        else:
            for lv in range(3):
                y = 280 - lv * 70
                b += R(x0 + 40, y, 250, 4, NAVY)
                for k in range(5):
                    b += R(x0 + 46 + k * 49, y - 46, 44, 46, "#E3E8EF", NAVY, 1) + R(x0 + 58 + k * 49, y - 34, 20, 8, GOLD)
            b += L(x0 + 40, 280, x0 + 40, 300, NAVY, 3) + L(x0 + 290, 280, x0 + 290, 300, NAVY, 3)
            b += R(x0 + 330, 110, 60, 80, "#0E234A") + T(x0 + 360, 150, "volet\nfermé", 11, "white", italic=True)
            b += R(x0 + 330, 215, 50, 40, "white", NAVY, 1.2) + M(x0 + 355, 235, "HR 50%", 8.5, NAVY, 700)
            notes = ["Rayonnages métalliques surélevés", "Boîtes de conservation cotées", "Obscurité, fenêtre occultée", "Climat mesuré et stable"]
        for k, n in enumerate(notes):
            b += T(x0 + 215, 318 + k * 13, ("× " if side == 0 else "• ") + n, 11.5, RED if side == 0 else GREEN, 600)
    return svg(w, h + 20, b.replace('height="360"', 'height="380"'))

# ------------------------------------------------------------------ CH6
@fig
def fig11_sort_final():
    w, h = 900, 300
    b = ""
    steps = [("SÉRIE", "issue du plan\nde classement"), ("VALEURS", "administrative\njuridique\nfinancière\nhistorique"), ("DUA", "durée + point\nde départ")]
    for i, (t, d) in enumerate(steps):
        x = 10 + i * 175
        b += R(x, 70, 150, 160, GRAY) + R(x, 70, 150, 36, NAVY) + M(x + 75, 88, t, 12, "white", 800, ls=1) + T(x + 75, 168, d, 12.5)
        b += A(x + 152, 150, x + 172, 150, GOLD, 2.2, marker="arg")
    b += R(535, 110, 90, 80, GOLD) + M(580, 140, "ÉCHÉANCE", 9.5, "white", 800) + T(580, 165, "gel ?\nlitige · audit", 10.5, "white", italic=True)
    outs = [("C", "CONSERVATION", "archives définitives", NAVY), ("T", "TRI", "échantillon conservé", NAVY2), ("D", "DESTRUCTION", "autorisée + PV", "#6B7486")]
    for i, (l, t, d, c) in enumerate(outs):
        y = 25 + i * 90
        b += A(627, 150, 680, y + 35, NAVY, 1.6)
        b += R(685, y, 205, 70, c) + R(685, y, 50, 70, BORD) + M(710, y + 35, l, 24, "white", 800) + M(812, y + 24, t, 11, "white", 800, ls=0.5) + T(812, y + 48, d, 12, "#E3E8EF", italic=True)
    return svg(w, h, b)

# ------------------------------------------------------------------ CH7
@fig
def fig12_stockage_ged_sae():
    w, h = 900, 280
    cols = [("STOCKAGE", "« Où est le fichier ? »", ["Disque, serveur, cloud", "Toutes versions", "Contrôles faibles"], 0.35),
            ("GED", "« Quelle version, qui travaille ? »", ["Documents vivants", "Versions, workflows", "Droits d'accès"], 0.65),
            ("ARCHIVAGE (SAE)", "« Est-ce intact et probant ? »", ["Documents figés, PDF/A", "Empreintes, journaux", "Durées et sort final"], 1)]
    b = ""
    for i, (t, q, items, lvl) in enumerate(cols):
        x = 15 + i * 295
        hh = 120 + lvl * 120
        y = 260 - hh
        b += R(x, y, 275, hh, NAVY if i == 2 else (NAVY2 if i == 1 else "#3A4E73"))
        b += M(x + 137, y + 24, t, 12.5, VC, 800, ls=1) + T(x + 137, y + 50, q, 12, "white", italic=True)
        for k, it in enumerate(items):
            b += T(x + 137, y + 82 + k * 22, it, 12.5, "white")
        if i < 2:
            b += A(x + 277, 200, x + 293, 200, GOLD, 2.2, marker="arg")
    b += T(450, 275, "Niveau d'exigence croissant : intégrité, authenticité, traçabilité, conservation", 11.5, MUTED, italic=True)
    return svg(w, h + 10, b)

@fig
def fig13_chaine_numerisation():
    w, h = 900, 200
    st = [("PRÉPARER", "trier, dégrafer,\ncompter"), ("NUMÉRISER", "paramètres\ndéfinis"), ("OCR", "couche texte"), ("CONTRÔLER", "pages, lisibilité,\nqualité"),
          ("DÉCRIRE", "nommage,\nmétadonnées"), ("ARCHIVER", "PDF/A, empreinte,\nSAE"), ("RÉINTÉGRER", "originaux\nreclassés")]
    b = ""
    for i, (t, d) in enumerate(st):
        x = 8 + i * 127
        b += R(x, 40, 112, 130, GRAY) + R(x, 40, 112, 32, NAVY) + M(x + 56, 56, t, 9.6, "white", 800, ls=0.2) + sq(x + 43, 18, i + 1, 24) + T(x + 56, 122, d, 12)
        if i < 6:
            b += A(x + 113, 105, x + 125, 105, GOLD, 2, marker="arg")
    return svg(w, h, b)

# ------------------------------------------------------------------ CH8
@fig
def fig14_exigences_securite():
    w, h = 900, 250
    ex = [("C", "CONFIDENTIALITÉ", "accès aux seules\npersonnes autorisées"), ("I", "INTÉGRITÉ", "complet et\nnon altéré"), ("D", "DISPONIBILITÉ", "accessible\nquand nécessaire"),
          ("A", "AUTHENTICITÉ", "auteur et date\nvérifiables"), ("T", "TRAÇABILITÉ", "chaque action\ndatée et attribuée")]
    b = R(10, 205, 880, 34, NAVY) + M(450, 222, "LA VALEUR DE PREUVE DES ARCHIVES", 12, VC, 800, ls=2)
    for i, (l, t, d) in enumerate(ex):
        x = 10 + i * 178
        col = NAVY2 if i < 3 else BORD
        b += R(x + 4, 10, 162, 190, GRAY) + f'<circle cx="{x+85}" cy="52" r="32" fill="{col}"/>' + M(x + 85, 52, l, 22, "white", 800)
        b += M(x + 85, 110, t, 10.5, NAVY, 800, ls=0.5) + T(x + 85, 152, d, 12.5)
    b += T(270, 4 + 0, "", 1)
    return svg(w, h, b)

@fig
def fig15_matrice_risques():
    w, h = 760, 560
    ox, oy, c = 120, 30, 100
    cols = {1: "#E6EFE8", 2: "#CFE2D4", 3: "#F1E4E0", 4: "#E3B6BE", 5: "#C9687A"}
    b = ""
    for p in range(1, 6):
        for i in range(1, 6):
            sc = p * i
            lvl = 1 if sc <= 4 else 2 if sc <= 6 else 3 if sc <= 10 else 4 if sc <= 15 else 5
            x = ox + (i - 1) * c; y = oy + (5 - p) * c
            b += R(x, y, c - 3, c - 3, cols[lvl]) + T(x + 14, y + 14, str(sc), 10, MUTED)
    risks = [("R1", 4, 5), ("R2", 4, 4), ("R3", 3, 5), ("R4", 3, 4), ("R5", 2, 5), ("R6", 2, 4)]
    for r, p, i in risks:
        x = ox + (i - 1) * c + c / 2 - 1; y = oy + (5 - p) * c + c / 2 - 1
        off = -18 if r in ("R2",) else 0
        b += f'<circle cx="{x}" cy="{y}" r="22" fill="{NAVY}"/>' + M(x, y, r, 12, "white", 800)
    b += M(ox + 250, oy + 525, "IMPACT  (1 = mineur  ·  5 = critique)", 11, NAVY, 700, ls=1)
    b += f'<g transform="translate(55 {oy+250}) rotate(-90)">' + M(0, 0, "PROBABILITÉ  (1 = rare  ·  5 = quasi certaine)", 11, NAVY, 700, ls=1) + "</g>"
    for k in range(1, 6):
        b += M(ox + (k - 1) * c + 48, oy + 505, str(k), 11, MUTED, 700) + M(ox - 18, oy + (5 - k) * c + 48, str(k), 11, MUTED, 700)
    return svg(w, h, b)

# ------------------------------------------------------------------ CH9
@fig
def fig16_ia_validation():
    w, h = 900, 270
    b = ""
    left = [("DOCUMENTS", "scans, fichiers,\ncourriels"), ("IA", "OCR · classement\nextraction · résumé")]
    for i, (t, d) in enumerate(left):
        x = 10 + i * 200
        b += R(x, 70, 170, 120, GRAY) + R(x, 70, 170, 34, NAVY2 if i else NAVY) + M(x + 85, 87, t, 12, "white", 800, ls=1) + T(x + 85, 148, d, 12.5)
    b += A(182, 130, 208, 130, GOLD, 2.2, marker="arg") + A(382, 130, 418, 130, GOLD, 2.2, marker="arg")
    b += R(420, 40, 210, 180, GOLD) + M(525, 70, "VALIDATION", 13, "white", 800, ls=1.5) + M(525, 90, "HUMAINE", 13, "white", 800, ls=1.5)
    b += T(525, 155, "contrôle proportionné\nà l'enjeu · confiance\nfaible = revue\nsystématique", 12, "white")
    outs = [("ACCEPTÉ", "classé, indexé,\ntracé", NAVY), ("CORRIGÉ", "règles et descriptions\najustées", NAVY2)]
    for i, (t, d, c) in enumerate(outs):
        y = 30 + i * 120
        b += A(632, 130, 688, y + 45, NAVY, 1.6) + R(690, y, 200, 90, c) + M(790, y + 25, t, 12, VC, 800, ls=1) + T(790, y + 60, d, 12, "white")
    b += f'<path d="M790 240 Q 525 290 300 192" fill="none" stroke="{GOLD}" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#arg)"/>' + T(560, 258, "amélioration continue", 11, GOLD, italic=True)
    return svg(w, h + 10, b)

# ------------------------------------------------------------------ CH10
@fig
def fig17_demarche_service():
    w, h = 900, 190
    st = ["DIAGNOSTIQUER", "DÉCIDER", "ORGANISER", "OUTILLER", "FORMER", "CONTRÔLER", "AMÉLIORER"]
    sub = ["inventaire,\nrapport", "politique,\nmoyens", "rôles,\ncorrespondants", "plan, tableau,\nregistres", "équipes,\nnouveaux", "indicateurs,\nrécolement", "revue\nannuelle"]
    b = ""
    for i, t in enumerate(st):
        x = 8 + i * 127
        b += f'<path d="M{x} 20 h108 l14 32 l-14 32 h-108 l14 -32z" fill="{NAVY if i%2==0 else NAVY2}"/>' if i else f'<path d="M{x} 20 h108 l14 32 l-14 32 h-108z" fill="{NAVY}"/>'
        b += M(x + 63, 52, t, 9.4, "white", 800, ls=0.2) + sq(x + 52, 98, i + 1, 22) + T(x + 63, 152, sub[i], 12)
    b += f'<path d="M820 175 Q 450 200 70 175" fill="none" stroke="{GOLD}" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#arg)"/>'
    return svg(w, h + 10, b)

@fig
def fig18_feuille_route_30j():
    w, h = 900, 290
    ph = [("COMPRENDRE", 1, 5), ("INVENTORIER", 6, 12), ("SÉCURISER", 13, 18), ("ANALYSER ET PROPOSER", 19, 25), ("DÉCIDER ET LANCER", 26, 30)]
    ox, dw = 200, 22
    b = ""
    for d in range(1, 31):
        x = ox + (d - 1) * dw
        if d in (1, 5, 10, 15, 20, 25, 30):
            b += T(x + dw / 2, 20, f"J{d}", 12, MUTED, 600) + L(x + dw / 2, 30, x + dw / 2, 260, LINE, 0.8, "2 3")
    for i, (t, a, z) in enumerate(ph):
        y = 45 + i * 44
        x = ox + (a - 1) * dw
        b += M(190, y + 15, t, 10, NAVY, 800, anchor="end", ls=0.3)
        b += R(x, y, (z - a + 1) * dw - 2, 30, NAVY if i % 2 == 0 else NAVY2) + R(x, y, 6, 30, GOLD)
    jal = [(5, "Lettre de mission"), (12, "Fiches de diagnostic"), (18, "Mesures d'urgence"), (25, "Rapport"), (30, "Plan validé")]
    for i, (d, t) in enumerate(jal):
        x = ox + d * dw - 2; y = 45 + i * 44 + 15
        b += f'<path d="M{x} {y-9} l9 9 l-9 9 l-9 -9z" fill="{GOLD}"/>'
    b += T(ox, 278, "Jalons : lettre de mission (J5) · diagnostic (J12) · urgences traitées (J18) · rapport (J25) · plan d'action validé (J30)", 11.5, MUTED, anchor="start", italic=True)
    return svg(w, h, b)

def main(only=None):
    for name, fn in FIGS.items():
        if name.startswith("_") or (only and name not in only):
            continue
        s = fn()
        (OUT / f"{name}.svg").write_text(s)
        cairosvg.svg2png(bytestring=s.encode(), write_to=str(OUT / f"{name}.png"), output_width=1800)
        print("ok", name)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:] or None)
