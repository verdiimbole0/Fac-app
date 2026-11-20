#!/usr/bin/env python3
"""Génère les figures originales (SVG) de l'ouvrage ASBL AUGMENTÉE.

Toutes les figures sont des créations originales. Palette éditoriale :
bleu marine #102849, or doux #C7A34F, gris clair #EAF0F5, vert pétrole #167D73, blanc.
Usage : python3 figures.py <dossier_sortie>
"""
import os, sys, csv
from xml.sax.saxutils import escape

NAVY, GOLD, LIGHT, TEAL, WHITE = "#241A6B", "#7B6CF0", "#F1EFFB", "#3F5BD8", "#FFFFFF"
GREY, LGOLD, LTEAL, RED, LRED, AMBER = "#6E6A85", "#E9E5FD", "#E1E9FB", "#C0392B", "#F8DEDB", "#E0A526"
FONT = "'Inter', Arial, sans-serif"
TFONT = "'Outfit', 'Inter', Arial, sans-serif"

FIGS = []  # (id, titre, alt)


class SVG:
    def __init__(self, w, h, title, desc):
        self.w, self.h, self.items = w, h, []
        self.title, self.desc = title, desc

    def add(self, s):
        self.items.append(s)

    def rect(self, x, y, w, h, fill=LIGHT, stroke=NAVY, sw=1.2, rx=10, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def text(self, x, y, s, size=13, color=NAVY, weight="normal", anchor="middle", lh=1.25, italic=False, family=None):
        lines = s.split("\n")
        st = ' font-style="italic"' if italic else ""
        y0 = y - (len(lines) - 1) * size * lh / 2
        for i, ln in enumerate(lines):
            self.add(f'<text x="{x}" y="{y0 + i*size*lh:.1f}" font-family="{family or FONT}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" dominant-baseline="middle"{st}>{escape(ln)}</text>')

    def box(self, x, y, w, h, s, fill=LIGHT, color=NAVY, size=13, weight="normal", stroke=NAVY, rx=8, dash=None):
        self.rect(x, y, w, h, fill, stroke, rx=rx, dash=dash)
        self.text(x + w/2, y + h/2, s, size, color, weight)

    def arrow(self, x1, y1, x2, y2, color=NAVY, sw=1.6, dash=None, label=None, lsize=11):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" marker-end="url(#ah{color[1:]})"{d}/>')
        if label:
            self.text((x1+x2)/2, (y1+y2)/2 - 9, label, lsize, GREY)

    def path(self, d, color=NAVY, sw=1.6, arrow=True, dash=None):
        m = f' marker-end="url(#ah{color[1:]})"' if arrow else ""
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"{m}{ds}/>')

    def circle(self, cx, cy, r, fill, stroke=NAVY, sw=1.2):
        self.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def header(self, s, sub=None):
        self.add(f'<rect x="24" y="12" width="44" height="5" rx="2.5" fill="{GOLD}"/>')
        self.text(24, 34, s, 18, NAVY, "800", "start", family=TFONT)
        if sub:
            self.text(24, 52, sub, 12, GREY, "normal", "start", italic=True)

    def render(self):
        markers = "".join(
            f'<marker id="ah{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
            for c in (NAVY, TEAL, GOLD, GREY, RED))
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" role="img" aria-labelledby="t d">'
                f'<title id="t">{escape(self.title)}</title><desc id="d">{escape(self.desc)}</desc>'
                f'<defs>{markers}</defs><rect width="100%" height="100%" fill="{WHITE}"/>' + "".join(self.items) + "</svg>")


def fig(fid, title, alt, w=900, h=520):
    def deco(fn):
        def run(out):
            s = SVG(w, h, title, alt)
            fn(s)
            with open(os.path.join(out, f"fig_{fid.replace('.', '_')}.svg"), "w", encoding="utf-8") as f:
                f.write(s.render())
        FIGS.append((fid, title, alt, run))
        return run
    return deco


# ---------------------------------------------------------------- Liminaires
@fig("0.1", "Carte des parcours de lecture",
     "Socle commun (modules 1 à 6, 8, 19, 20) puis parcours spécialisés par métier vers les modules 10 à 18, et laboratoire final (modules 21 et 22).", 900, 600)
def f01(s):
    s.header("Carte des parcours de lecture", "Le socle commun d'abord, puis votre métier, puis le laboratoire")
    s.box(30, 80, 840, 120, "", LIGHT)
    s.text(450, 98, "SOCLE COMMUN : à lire par tous", 14, NAVY, "bold")
    items = [("M1–M3", "Fondamentaux\nde l'IA"), ("M4–M6", "Comprendre et\ndiagnostiquer l'ASBL"),
             ("M8", "Éthique et\nsécurité"), ("M7, M9", "Données et outils\n(recommandé)"), ("M19–M20", "Déployer et\npérenniser")]
    for i, (a, b) in enumerate(items):
        x = 50 + i*165
        s.box(x, 115, 150, 72, f"{a}\n{b}", WHITE, NAVY, 12)
    roles = [("Dirigeants, CA", "M10"), ("Comptables,\ntrésoriers", "M12"), ("Auditeurs,\ncontrôleurs", "M13"),
             ("Chefs de projet,\nS&E", "M11"), ("RH, bénévolat", "M14"), ("Financements", "M15"),
             ("Logistique,\nachats", "M16"), ("Communication", "M17"), ("Agents de\nterrain", "M18")]
    s.text(450, 228, "PARCOURS SPÉCIALISÉS : choisissez votre métier", 14, TEAL, "bold")
    for i, (r, m) in enumerate(roles):
        x = 30 + i*94
        s.arrow(450, 205, x+43, 250, GREY, 1)
        s.box(x, 252, 86, 62, r, LTEAL, NAVY, 10.5)
        s.box(x+13, 330, 60, 34, m, TEAL, WHITE, 13, "bold", TEAL)
        s.arrow(x+43, 314, x+43, 330, TEAL, 1.2)
        s.arrow(x+43, 364, 450, 420, GREY, 1)
    s.box(250, 420, 400, 70, "LABORATOIRE : M21 : 10 études de cas\nM22 : votre plan de transformation à 90 jours", LGOLD, NAVY, 13, "bold", GOLD)
    s.text(450, 525, "Transformer toute l'organisation ? Lisez les 22 modules dans l'ordre.", 13, GREY, italic=True)
    s.text(450, 550, "Les dirigeants complètent M10 par M5, M6, M20 et M22.", 12, GREY, italic=True)


# ---------------------------------------------------------------- Module 1
@fig("1.1", "Repères historiques de l'intelligence artificielle",
     "Frise chronologique : 1950 article de Turing ; 1956 conférence de Dartmouth ; années 1980 systèmes experts ; 1997 victoire d'un ordinateur aux échecs ; 2012 essor de l'apprentissage profond ; 2017 architecture Transformer ; fin 2022 diffusion grand public des assistants conversationnels ; depuis 2024 encadrement réglementaire.", 920, 380)
def f11(s):
    s.header("Repères historiques de l'IA", "Des promesses, des hivers, puis une accélération récente")
    s.add(f'<line x1="40" y1="200" x2="880" y2="200" stroke="{NAVY}" stroke-width="3"/>')
    ev = [("1950", "Turing pose la\nquestion « une machine\npeut-elle penser ? »"), ("1956", "Conférence de\nDartmouth : naissance\ndu terme « IA »"),
          ("1980s", "Systèmes experts\nà base de règles"), ("1997", "Un ordinateur bat\nle champion du\nmonde d'échecs"),
          ("2012", "Essor de\nl'apprentissage\nprofond (images)"), ("2017", "Architecture\nTransformer"),
          ("Fin 2022", "Assistants\nconversationnels\ngrand public"), ("2024+", "Cadres et lois :\nAI Act, normes,\nconventions")]
    for i, (d, t) in enumerate(ev):
        x = 70 + i*110
        up = i % 2 == 0
        s.circle(x, 200, 9, GOLD if i >= 5 else TEAL, WHITE, 2)
        s.text(x, 228 if up else 172, d, 13, NAVY, "bold")
        s.box(x-52, 250 if up else 70, 104, 76, t, LIGHT if i < 5 else LGOLD, NAVY, 10.5)
    s.text(460, 360, "Les « hivers de l'IA » (années 1970 et fin des années 1980) rappellent que les promesses excessives sont suivies de désillusions.", 11.5, GREY, italic=True)


@fig("1.2", "Les grandes familles d'intelligence artificielle",
     "Schéma emboîté : l'IA englobe les systèmes à règles et l'apprentissage automatique ; l'apprentissage automatique englobe l'apprentissage profond ; l'apprentissage profond englobe l'IA générative et les grands modèles de langage.", 900, 480)
def f12(s):
    s.header("Les grandes familles d'IA", "Des ensembles emboîtés, pas des technologies concurrentes")
    s.rect(40, 70, 820, 390, LIGHT, NAVY, 1.5, 18)
    s.text(70, 95, "Intelligence artificielle : tout système qui produit des prédictions, contenus, recommandations ou décisions", 12.5, NAVY, "bold", "start")
    s.box(60, 120, 200, 320, "Systèmes à règles\n(« si… alors… »)\n\nEx. : contrôle\nautomatique d'un\nplafond de dépense", WHITE, NAVY, 12)
    s.rect(280, 115, 560, 330, LTEAL, TEAL, 1.5, 16)
    s.text(300, 138, "Apprentissage automatique : apprend à partir d'exemples", 12.5, TEAL, "bold", "start")
    s.text(300, 160, "Ex. : prévoir un risque d'abandon scolaire", 11.5, GREY, "normal", "start")
    s.rect(300, 180, 520, 250, WHITE, NAVY, 1.2, 14)
    s.text(320, 202, "Apprentissage profond : réseaux de neurones à nombreuses couches", 12.5, NAVY, "bold", "start")
    s.text(320, 224, "Ex. : reconnaissance d'images, OCR moderne, voix", 11.5, GREY, "normal", "start")
    s.rect(320, 250, 480, 165, LGOLD, GOLD, 1.5, 12)
    s.text(340, 272, "IA générative : produit du texte, des images, du son", 12.5, NAVY, "bold", "start")
    s.box(340, 295, 210, 105, "Grands modèles\nde langage (LLM)\nAssistants\nconversationnels", WHITE, NAVY, 12)
    s.box(570, 295, 210, 105, "Modèles d'images,\nde voix, de vidéo", WHITE, NAVY, 12)


# ---------------------------------------------------------------- Module 2
@fig("2.1", "Du jeu de données au modèle, puis à la prédiction",
     "Phase d'entraînement : données d'exemples, algorithme d'apprentissage, modèle. Phase d'utilisation : nouvelle donnée, modèle, prédiction, puis vérification humaine qui alimente l'amélioration.", 900, 400)
def f21(s):
    s.header("Comment un système apprend", "Deux temps : l'entraînement, puis l'utilisation")
    s.text(220, 85, "1. ENTRAÎNEMENT", 13, TEAL, "bold")
    s.box(40, 105, 140, 80, "Données\nd'exemples\n(étiquetées ou non)", LIGHT)
    s.box(230, 105, 140, 80, "Algorithme\nd'apprentissage", LTEAL)
    s.box(420, 105, 140, 80, "Modèle\n(paramètres\najustés)", LGOLD, NAVY, 13, "bold", GOLD)
    s.arrow(180, 145, 230, 145); s.arrow(370, 145, 420, 145)
    s.text(660, 85, "2. UTILISATION (inférence)", 13, TEAL, "bold")
    s.box(40, 255, 140, 80, "Nouvelle donnée\n(ex. : une facture\njamais vue)", LIGHT)
    s.box(420, 255, 140, 80, "Modèle", LGOLD, NAVY, 13, "bold", GOLD)
    s.box(610, 255, 120, 80, "Prédiction\n+ niveau de\nconfiance", WHITE)
    s.box(770, 255, 110, 80, "Vérification\nhumaine", TEAL, WHITE, 12.5, "bold", TEAL)
    s.arrow(180, 295, 420, 295); s.arrow(490, 185, 490, 255, GOLD, 1.6, "5,4")
    s.arrow(560, 295, 610, 295); s.arrow(730, 295, 770, 295)
    s.path("M825,335 C825,380 110,380 110,190", TEAL, 1.4, True, "6,4")
    s.text(470, 372, "Corrections et nouveaux exemples → amélioration du système", 11.5, TEAL, italic=True)


@fig("2.2", "Architecture RAG (génération augmentée par la recherche)",
     "La question de l'utilisateur déclenche une recherche dans la base documentaire de l'ASBL ; les passages pertinents sont transmis au modèle de langage avec la question ; la réponse cite ses sources et est vérifiée.", 900, 460)
def f22(s):
    s.header("Le RAG : répondre à partir de VOS documents", "Le modèle ne « sait » pas vos procédures : on les lui fournit au moment de la question")
    s.box(30, 110, 150, 70, "Question :\n« Plafond d'une\navance de mission ? »", LIGHT, NAVY, 11.5)
    s.box(240, 90, 180, 110, "Moteur de recherche\nsémantique\n(index des passages)", LTEAL)
    s.box(240, 260, 180, 130, "Base documentaire\nde l'ASBL\nManuel de procédures\nPolitiques, conventions\n(versions validées)", LGOLD, NAVY, 11.5, "normal", GOLD)
    s.box(480, 90, 180, 110, "Question\n+ 3 passages\npertinents\n(avec références)", WHITE)
    s.box(720, 90, 150, 110, "Modèle de\nlangage (LLM)", NAVY, WHITE, 13, "bold")
    s.box(700, 270, 190, 110, "Réponse sourcée :\n« 300 UM : Manuel\nfinancier §4.2 (v3) »\n+ vérification humaine", LTEAL, NAVY, 11.5)
    s.arrow(180, 145, 240, 145); s.arrow(330, 260, 330, 200, GOLD, 1.6, None, None)
    s.text(380, 230, "extraits", 11, GREY)
    s.arrow(420, 145, 480, 145); s.arrow(660, 145, 720, 145); s.arrow(795, 200, 795, 270)
    s.text(450, 425, "Avantage : réponses fondées sur des documents à jour et vérifiables. Limite : la qualité dépend de la base (doublons, versions périmées).", 11.5, GREY, italic=True)


# ---------------------------------------------------------------- Module 3
@fig("3.1", "Anatomie d'un prompt efficace : la méthode CADRE",
     "Cinq blocs : Contexte, Action, Données, Résultat attendu, Exigences et limites. Chaque bloc est illustré par un exemple relatif à un rapport d'activité.", 900, 470)
def f31(s):
    s.header("Méthode CADRE", "Cinq blocs pour écrire une consigne claire, vérifiable et réutilisable")
    rows = [("C", "Contexte", "Qui je suis, pour qui, dans quelle situation", "« Je suis chargée de suivi-évaluation d'une ASBL de santé communautaire… »"),
            ("A", "Action", "Ce que l'IA doit faire, avec un verbe précis", "« Rédige une synthèse de 300 mots du rapport trimestriel… »"),
            ("D", "Données", "Les éléments fournis et leur délimitation", "« … à partir UNIQUEMENT du texte entre les balises <rapport>. »"),
            ("R", "Résultat attendu", "Format, longueur, structure, ton, langue", "« Format : 3 titres, un tableau des indicateurs, ton factuel. »"),
            ("E", "Exigences et limites", "Ce qu'il ne faut pas faire ; comment signaler un doute", "« N'invente aucun chiffre ; écris [À VÉRIFIER] si une donnée manque. »")]
    for i, (l, n, d, ex) in enumerate(rows):
        y = 75 + i*76
        s.box(30, y, 60, 62, l, NAVY if i % 2 == 0 else TEAL, WHITE, 26, "bold", NAVY if i % 2 == 0 else TEAL)
        s.box(100, y, 230, 62, f"{n}\n{d}", LIGHT, NAVY, 11.5)
        s.box(340, y, 530, 62, ex, WHITE, GREY, 11.5, "normal", GREY, dash="4,3")


@fig("3.2", "La boucle de vérification d'une réponse d'IA",
     "Cycle en six étapes : formuler, lire la réponse, vérifier les faits et chiffres, confronter aux sources, corriger ou reformuler, valider et documenter.", 760, 520)
def f32(s):
    import math
    s.header("Ne jamais copier-coller sans vérifier", "La boucle « 6 V »")
    st = ["1. Formuler\n(CADRE)", "2. Lire la réponse\nen entier", "3. Vérifier faits,\nchiffres, noms", "4. Confronter aux\nsources originales", "5. Corriger ou\nreformuler", "6. Valider et\ndocumenter"]
    cx, cy, r = 380, 290, 170
    pts = []
    for i, t in enumerate(st):
        a = -math.pi/2 + i*2*math.pi/6
        x, y = cx + r*math.cos(a), cy + r*math.sin(a)
        pts.append((x, y))
    for i in range(6):
        x1, y1 = pts[i]; x2, y2 = pts[(i+1) % 6]
        s.arrow(x1 + (x2-x1)*0.28, y1 + (y2-y1)*0.28, x1 + (x2-x1)*0.72, y1 + (y2-y1)*0.72, TEAL, 2)
    for i, (x, y) in enumerate(pts):
        s.box(x-75, y-30, 150, 60, st[i], GOLD if i == 5 else LIGHT, NAVY, 12, "bold" if i == 5 else "normal", GOLD if i == 5 else NAVY)
    s.box(cx-80, cy-28, 160, 56, "Responsabilité\nhumaine", NAVY, WHITE, 13, "bold")


# ---------------------------------------------------------------- Module 4
@fig("4.1", "Organigramme type d'une ASBL de taille moyenne",
     "Assemblée générale, conseil d'administration, direction exécutive, puis quatre pôles : programmes, finances et administration, ressources humaines, communication et partenariats ; audit interne rattaché au conseil.", 900, 470)
def f41(s):
    s.header("Organigramme type (Fondation Horizons Partagés)", "Les intitulés varient selon les statuts et le droit applicable")
    s.box(350, 70, 200, 46, "Assemblée générale", LGOLD, NAVY, 13, "bold", GOLD)
    s.box(350, 140, 200, 46, "Conseil d'administration", NAVY, WHITE, 13, "bold")
    s.box(640, 140, 200, 46, "Audit interne / comité\nd'audit (selon taille)", WHITE, NAVY, 11.5, dash="5,3")
    s.box(350, 215, 200, 46, "Direction exécutive", TEAL, WHITE, 13, "bold", TEAL)
    s.arrow(450, 116, 450, 140); s.arrow(450, 186, 450, 215); s.arrow(550, 163, 640, 163, GREY, 1.2, "4,3")
    poles = [("Programmes\net projets", "Chefs de projet\nS&E · Terrain"), ("Finances et\nadministration", "Comptabilité\nTrésorerie · Achats"),
             ("Ressources\nhumaines", "Recrutement · Paie\nBénévolat"), ("Communication et\npartenariats", "Bailleurs · Plaidoyer\nNumérique")]
    for i, (p, d) in enumerate(poles):
        x = 40 + i*215
        s.path(f"M450,261 L450,285 L{x+95},285 L{x+95},305", NAVY, 1.2)
        s.box(x, 305, 190, 56, p, LIGHT, NAVY, 12.5, "bold")
        s.box(x, 375, 190, 60, d, WHITE, GREY, 11.5, stroke=GREY)


@fig("4.2", "Les cycles de fonctionnement d'une ASBL",
     "Quatre cycles concentriques qui s'entrecroisent : cycle stratégique pluriannuel, cycle budgétaire annuel, cycle de projet, cycle mensuel de clôture et de reporting.", 900, 420)
def f42(s):
    s.header("Quatre cycles qui s'emboîtent", "Chaque cycle produit des documents, des décisions et des échéances")
    cyc = [("Stratégique (3–5 ans)", "Vision → plan stratégique →\névaluation → révision", LGOLD),
           ("Budgétaire (annuel)", "Préparation → vote → exécution\n→ suivi → clôture → audit", LIGHT),
           ("Projet (6 mois – 5 ans)", "Identification → formulation →\nmise en œuvre → évaluation", LTEAL),
           ("Opérationnel (mensuel)", "Pièces → saisie → rapprochements\n→ tableaux de bord → reporting", WHITE)]
    for i, (t, d, c) in enumerate(cyc):
        x = 30 + i*215
        s.box(x, 90, 200, 50, t, NAVY, WHITE, 13, "bold")
        s.box(x, 150, 200, 110, d, c, NAVY, 12)
    s.box(30, 290, 845, 90, "Point clé pour l'IA : chaque cycle comporte des tâches répétitives (collecte, consolidation, mise en forme)\net des décisions (arbitrages, validations). L'IA peut alléger les premières ; les secondes restent humaines.", LIGHT, NAVY, 12.5)


# ---------------------------------------------------------------- Module 5
@fig("5.1", "Cartographie « tel quel » du circuit des dépenses",
     "Diagramme en couloirs : demandeur, coordination, comptabilité, direction. Les étapes sont reliées par des flèches ; quatre points de blocage sont signalés en rouge : formulaires papier incomplets, attente de signature, ressaisie manuelle, classement non retrouvable.", 940, 470)
def f51(s):
    s.header("Processus « tel quel » : circuit des dépenses", "Fondation Horizons Partagés : points de blocage en rouge")
    lanes = ["Demandeur", "Coordination", "Comptabilité", "Direction"]
    for i, l in enumerate(lanes):
        y = 70 + i*95
        s.rect(20, y, 900, 90, LIGHT if i % 2 == 0 else WHITE, GREY, 0.8, 0)
        s.text(70, y+45, l, 12.5, NAVY, "bold")
    s.add(f'<line x1="120" y1="70" x2="120" y2="450" stroke="{GREY}" stroke-width="0.8"/>')
    B = [(140, 85, "Remplit fiche\npapier"), (300, 180, "Vérifie budget\n(Excel perso)"), (460, 370, "Signe\n(si présente)"),
         (620, 275, "Ressaisit dans\nle logiciel"), (780, 275, "Classe la pièce\n(classeur)")]
    for x, y, t in B:
        s.box(x, y, 130, 60, t, WHITE, NAVY, 11.5)
    s.arrow(205, 145, 300, 200); s.arrow(430, 220, 460, 380); s.arrow(590, 390, 640, 335); s.arrow(750, 305, 780, 305)
    for (x, y, n) in [(260, 95, "1"), (450, 345, "2"), (600, 255, "3"), (900, 255, "4")]:
        s.circle(x, y, 13, RED, WHITE, 2); s.text(x, y, n, 12, WHITE, "bold")
    s.text(520, 462, "① Fiche incomplète · ② Attente de signature (5 à 12 jours) · ③ Ressaisie et erreurs · ④ Pièce introuvable lors de l'audit", 11, RED)


@fig("5.2", "Arbre des causes : retards de reporting financier",
     "Le problème central « rapports financiers remis en retard » est relié à quatre familles de causes : méthodes, outils, personnes, données ; chacune détaillée en causes racines.", 900, 460)
def f52(s):
    s.header("Remonter aux causes profondes", "Diagramme causes-effet appliqué au reporting financier")
    s.box(660, 200, 220, 80, "PROBLÈME :\nrapports financiers\nremis avec 3 semaines\nde retard", RED, WHITE, 12.5, "bold", RED)
    s.add(f'<line x1="60" y1="240" x2="660" y2="240" stroke="{NAVY}" stroke-width="3"/>')
    fam = [("MÉTHODES", ["Pas de calendrier de clôture", "Codes budgétaires différents\nselon bailleurs"], 130, True),
           ("OUTILS", ["Tableurs non reliés", "Pas de modèle de rapport"], 400, True),
           ("PERSONNES", ["Une seule comptable", "Pas de suppléance formée"], 130, False),
           ("DONNÉES", ["Pièces arrivent tard du terrain", "Imputations à corriger"], 400, False)]
    for n, cs, x, up in fam:
        yb = 80 if up else 400
        s.box(x, yb-20 if up else yb-10, 140, 34, n, NAVY, WHITE, 12.5, "bold")
        s.arrow(x+70, yb+14 if up else yb-10, x+150, 236 if up else 244, NAVY, 1.4)
        for j, c in enumerate(cs):
            yy = (125 + j*45) if up else (300 + j*45)
            s.box(x+150, yy-17, 190, 36, c, LIGHT, NAVY, 10.5)


# ---------------------------------------------------------------- Module 6
@fig("6.1", "Matrice de priorisation valeur × faisabilité",
     "Graphique à quatre quadrants : gains rapides (forte valeur, forte faisabilité), projets structurants (forte valeur, faible faisabilité), petites améliorations, à écarter. Huit cas d'usage positionnés.", 820, 560)
def f61(s):
    s.header("Prioriser les cas d'usage", "Valeur pour la mission × faisabilité (données, coût, compétences, risques)")
    x0, y0, W, H = 110, 80, 640, 420
    s.rect(x0, y0, W/2, H/2, LGOLD, GREY, 0.8, 0); s.rect(x0+W/2, y0, W/2, H/2, LTEAL, GREY, 0.8, 0)
    s.rect(x0, y0+H/2, W/2, H/2, LRED, GREY, 0.8, 0); s.rect(x0+W/2, y0+H/2, W/2, H/2, LIGHT, GREY, 0.8, 0)
    s.text(x0+W*0.25, y0+18, "PROJETS STRUCTURANTS", 12, NAVY, "bold"); s.text(x0+W*0.75, y0+18, "GAINS RAPIDES", 12, TEAL, "bold")
    s.text(x0+W*0.25, y0+H-14, "À ÉCARTER / REPORTER", 12, RED, "bold"); s.text(x0+W*0.75, y0+H-14, "PETITES AMÉLIORATIONS", 12, GREY, "bold")
    s.arrow(x0, y0+H, x0+W+10, y0+H); s.arrow(x0, y0+H, x0, y0-10)
    s.text(x0+W/2, y0+H+28, "Faisabilité →", 13, NAVY, "bold")
    s.add(f'<text x="60" y="{y0+H/2}" font-family="{FONT}" font-size="13" font-weight="bold" fill="{NAVY}" text-anchor="middle" transform="rotate(-90 60 {y0+H/2})">Valeur pour la mission →</text>')
    pts = [(0.82, 0.80, "1 PV de réunion"), (0.75, 0.66, "2 Synthèse rapports"), (0.62, 0.86, "3 Extraction factures"),
           (0.30, 0.82, "4 Assistant procédures (RAG)"), (0.22, 0.62, "5 Prévision trésorerie"), (0.85, 0.30, "6 Posts réseaux"),
           (0.18, 0.22, "7 Tri automatique candidats"), (0.60, 0.40, "8 Traduction")]
    for fx, fy, t in pts:
        x, y = x0 + fx*W, y0 + (1-fy)*H
        s.circle(x, y, 7, NAVY, WHITE, 2)
        s.text(x+10, y, t, 11.5, NAVY, "normal", "start")


@fig("6.2", "Arbre de décision : faut-il de l'IA, une automatisation classique ou rien ?",
     "Questions successives : le problème est-il d'abord organisationnel ? La tâche suit-elle des règles stables ? Implique-t-elle du langage, des images ou des données variables ? Une erreur est-elle grave ? Les données sont-elles disponibles et autorisées ?", 900, 560)
def f62(s):
    s.header("IA, automatisation classique… ou rien ?", "Commencer par le problème, pas par l'outil")
    q = [(300, 70, "Q1. Le problème vient-il d'abord\nd'une règle, d'un rôle ou d'une\nhabitude mal définie ?"),
         (300, 175, "Q2. La tâche suit-elle des règles\nstables et explicites ?"),
         (300, 280, "Q3. Implique-t-elle du langage,\ndes images ou des cas variables ?"),
         (300, 385, "Q4. Les données nécessaires sont-\nelles disponibles, propres et\nautorisées ?")]
    for x, y, t in q:
        s.box(x, y, 280, 75, t, LIGHT, NAVY, 11.5)
    r = [(650, 70, "Réorganiser d'abord\n(procédure, rôles)", LGOLD), (650, 175, "Automatisation classique\n(formule, règle, workflow)", LTEAL),
         (650, 280, "Outil simple / statu quo\n(gain trop faible)", WHITE), (650, 385, "Préparer les données\n(module 7) avant l'IA", LGOLD)]
    for x, y, t, c in r:
        s.box(x, y, 220, 75, t, c, NAVY, 11.5)
    for i in range(4):
        y = q[i][1] + 37
        s.arrow(580, y, 650, y, NAVY, 1.4, label="Oui" if i != 2 else "Non")
    for i in range(3):
        s.arrow(440, q[i][1]+75, 440, q[i+1][1], NAVY, 1.4)
        s.text(458, q[i][1]+88, "Non" if i != 2 else "Oui", 11, GREY)
    s.box(300, 490, 280, 55, "Solution d'IA envisageable\n→ évaluer le risque d'erreur (module 8)", NAVY, WHITE, 12, "bold")
    s.arrow(440, 460, 440, 490); s.text(458, 475, "Oui", 11, GREY)


# ---------------------------------------------------------------- Module 7
@fig("7.1", "Le cycle de vie des données",
     "Six étapes : collecter, stocker, traiter, utiliser, partager, archiver ou détruire. Au centre : qualité, sécurité et responsabilité.", 760, 500)
def f71(s):
    import math
    s.header("Cycle de vie des données", "Chaque étape a un responsable, une règle et un risque")
    st = ["Collecter\n(minimum utile)", "Stocker\n(lieu sûr, accès)", "Traiter\n(nettoyer, coder)", "Utiliser\n(analyse, IA)", "Partager\n(qui, pourquoi)", "Archiver\nou détruire"]
    cx, cy, r = 380, 280, 165
    for i, t in enumerate(st):
        a = -math.pi/2 + i*2*math.pi/6
        x, y = cx + r*math.cos(a), cy + r*math.sin(a)
        b = -math.pi/2 + (i+0.5)*2*math.pi/6
        s.box(x-70, y-30, 140, 60, t, LTEAL if i % 2 else LIGHT, NAVY, 12)
        s.circle(cx + (r)*math.cos(b), cy + (r)*math.sin(b), 5, GOLD, GOLD)
    s.box(cx-85, cy-40, 170, 80, "Qualité\nSécurité\nResponsabilité", NAVY, WHITE, 13, "bold")


@fig("7.2", "Exemple d'arborescence documentaire et de règle de nommage",
     "Arborescence en cinq dossiers racines (gouvernance, finances, programmes, RH, communication) avec sous-dossiers par année et par projet, et règle de nommage AAAA-MM-JJ_TYPE_OBJET_vN.", 900, 470)
def f72(s):
    s.header("Un plan de classement simple et partagé", "La même logique pour le serveur, le cloud et les classeurs papier")
    tree = ["01_GOUVERNANCE/ → Statuts · CA · AG · Politiques",
            "02_FINANCES/ → 2026/ → 01_Pieces · 02_Banque · 03_Budget · 04_Rapports",
            "03_PROGRAMMES/ → PRJ-SANTE-07/ → Convention · Rapports · Donnees_S&E",
            "04_RH/ (accès restreint) → Contrats · Recrutement · Formation",
            "05_COMMUNICATION/ → Charte · Photos (avec consentements) · Publications",
            "99_ARCHIVES/ → selon durées de conservation légales"]
    for i, t in enumerate(tree):
        s.box(40, 75 + i*50, 560, 40, t, LIGHT if i % 2 == 0 else WHITE, NAVY, 12)
    s.box(630, 75, 240, 290, "RÈGLE DE NOMMAGE\n\nAAAA-MM-JJ_TYPE_OBJET_vN\n\nEx. :\n2026-03-15_FACT_\nFournisseurX_Riz_v1.pdf\n\n2026-04-02_PV_CA_v2.docx\n\nPas d'accents, pas\nd'espaces, version finale\n= « VALIDE »", LGOLD, NAVY, 12, stroke=GOLD)
    s.text(450, 420, "Une IA ne retrouve bien que ce qu'un humain aurait pu retrouver : le classement précède l'automatisation.", 12, GREY, italic=True)


# ---------------------------------------------------------------- Module 8
@fig("8.1", "Le feu tricolore de classification des données",
     "Trois catégories : vert (public, utilisable avec un outil grand public), orange (interne, utilisable avec un outil professionnel encadré, après minimisation), rouge (confidentiel ou sensible : interdit dans les outils non validés, anonymisation et validation obligatoires).", 900, 440)
def f81(s):
    s.header("Feu tricolore des données", "Avant chaque usage d'une IA : quelle couleur ?")
    cat = [("VERT : Public", "Rapport annuel publié, article\nde site web, appel à projets public", "Outils grand public autorisés.\nVérifier les sorties.", "#2E9E5B", "#DDF2E5"),
           ("ORANGE : Interne", "Budget non publié, procédures,\nPV de CA, données agrégées", "Outil professionnel encadré\n(contrat, pas d'entraînement\nsur vos données). Minimiser.", AMBER, LGOLD),
           ("ROUGE : Confidentiel / sensible", "Données nominatives de\nbénéficiaires, santé, enfants,\nsalaires, dossiers disciplinaires,\nRIB, signalements", "Interdit dans tout outil non\nvalidé. Anonymiser, base légale,\nvalidation du responsable.", RED, LRED)]
    for i, (t, ex, r, c, lc) in enumerate(cat):
        x = 30 + i*285
        s.circle(x+135, 110, 30, c, WHITE, 3)
        s.box(x, 155, 270, 40, t, c, WHITE, 13, "bold", c)
        s.box(x, 200, 270, 100, "Exemples :\n" + ex, lc, NAVY, 11.5, stroke=c)
        s.box(x, 310, 270, 90, r, WHITE, NAVY, 11.5, stroke=c)


@fig("8.2", "Trois modes de supervision humaine",
     "Humain dans la boucle : l'IA propose, l'humain décide à chaque fois. Humain sur la boucle : l'IA agit, l'humain surveille et peut interrompre. Humain aux commandes : l'humain fixe les règles et audite. Plus la décision est sensible, plus on va vers la gauche.", 900, 400)
def f82(s):
    s.header("Quel niveau de supervision humaine ?", "Plus l'impact sur les personnes est fort, plus l'humain intervient tôt")
    m = [("Humain DANS la boucle", "L'IA propose,\nl'humain valide chaque cas.\n\nEx. : imputation comptable,\nrecrutement, aide sociale", TEAL),
         ("Humain SUR la boucle", "L'IA exécute,\nl'humain surveille et\npeut interrompre.\n\nEx. : tri des courriels,\nclassement documentaire", GOLD),
         ("Humain AUX COMMANDES", "L'humain fixe les règles,\nles seuils et audite\npériodiquement.\n\nEx. : traduction de supports\npublics non sensibles", NAVY)]
    for i, (t, d, c) in enumerate(m):
        x = 40 + i*280
        s.box(x, 80, 260, 44, t, c, WHITE, 13.5, "bold", c)
        s.box(x, 130, 260, 170, d, LIGHT, NAVY, 12)
    s.arrow(820, 340, 80, 340, RED, 2.5)
    s.text(450, 362, "Impact croissant sur les droits, l'argent ou la sécurité des personnes", 12, RED, "bold")


# ---------------------------------------------------------------- Module 9
@fig("9.1", "Trois niveaux d'implémentation",
     "Escalier à trois marches : Débutant (assistant conversationnel, tableur, formulaires, procédures assistées), Intermédiaire (no-code, intégrations, gestion documentaire, assistants sur documents), Avancé (API, bases de données, ERP, RAG, agents, supervision).", 900, 460)
def f91(s):
    s.header("Trois niveaux d'implémentation", "On peut commencer petit : et monter d'une marche quand les bases sont solides")
    lv = [("NIVEAU 1 : DÉBUTANT", "Assistant conversationnel · tableur\nformulaires numériques · modèles\nprocédures manuelles assistées\n\nCompétences : bureautique\nCoûts : faibles, souvent gratuits\n(limites des offres gratuites)", LTEAL),
          ("NIVEAU 2 : INTERMÉDIAIRE", "Logiciels métier · no-code/low-code\nautomatisations entre applications\ngestion documentaire · tableaux de bord\nassistants sur documents internes\n\nCompétences : « référent numérique »\nCoûts : abonnements, paramétrage", LGOLD),
          ("NIVEAU 3 : AVANCÉ", "API · bases de données · ERP\nRAG · agents IA · hébergement\ngestion des accès · supervision\n\nCompétences : spécialistes\nCoûts : développement, hébergement,\nmaintenance, sécurité", LIGHT)]
    for i, (t, d, c) in enumerate(lv):
        x, y = 30 + i*285, 340 - i*120
        s.box(x, y, 270, 40, t, [TEAL, GOLD, NAVY][i], WHITE, 13, "bold", [TEAL, GOLD, NAVY][i])
        s.box(x, y+44, 270, 150 + i*0 , d, c, NAVY, 11)


# ---------------------------------------------------------------- Module 10
@fig("10.1", "De la réunion au suivi des décisions",
     "Flux : préparation de l'ordre du jour, réunion enregistrée avec consentement, transcription, projet de procès-verbal par l'IA, relecture par le secrétaire, adoption, registre des décisions, rappels automatiques, tableau de suivi présenté à la réunion suivante.", 940, 420)
def f101(s):
    s.header("Gouvernance : de la réunion au suivi des décisions", "En vert pétrole : étapes assistées par l'IA ; en bleu : étapes humaines")
    st = [("Ordre du jour\n+ documents", 0), ("Réunion\n(enregistrement\nconsenti)", 1), ("Transcription\nautomatique", 0), ("Projet de PV\n+ décisions\nextraites", 0),
          ("Relecture par\nle secrétaire\net le président", 1), ("Adoption\ndu PV", 1)]
    for i, (t, h) in enumerate(st):
        x = 20 + i*153
        s.box(x, 100, 138, 80, t, NAVY if h else TEAL, WHITE, 11.5, "bold" if h else "normal", NAVY if h else TEAL)
        if i < 5:
            s.arrow(x+138, 140, x+153, 140)
    s.box(560, 260, 180, 80, "Registre des décisions\n(qui, quoi, quand)", LGOLD, NAVY, 12, stroke=GOLD)
    s.box(310, 260, 180, 80, "Rappels automatiques\naux responsables", LTEAL, NAVY, 12, stroke=TEAL)
    s.box(60, 260, 180, 80, "Tableau de suivi\nà la réunion suivante", LIGHT, NAVY, 12)
    s.arrow(840, 180, 650, 260); s.arrow(560, 300, 490, 300); s.arrow(310, 300, 240, 300)
    s.path("M150,260 C150,215 90,215 90,182", GREY, 1.3, True, "5,4")
    s.text(470, 395, "Le PV n'a de valeur qu'une fois relu et adopté par l'organe compétent : l'IA ne produit qu'un projet.", 12, GREY, italic=True)


# ---------------------------------------------------------------- Module 11
@fig("11.1", "De l'arbre à problèmes à l'arbre à objectifs",
     "À gauche, un arbre à problèmes : problème central « taux élevé de maladies diarrhéiques chez les enfants de moins de 5 ans », causes en bas, effets en haut. À droite, l'arbre à objectifs obtenu en reformulant chaque problème en situation positive.", 940, 500)
def f111(s):
    s.header("Arbre à problèmes → arbre à objectifs", "Chaque cause devient un moyen ; chaque effet devient une fin")
    def tree(x0, title, top, mid, bots, c):
        s.text(x0+210, 75, title, 14, NAVY, "bold")
        s.box(x0+60, 95, 300, 50, top, LIGHT, NAVY, 11.5)
        s.box(x0+60, 200, 300, 60, mid, c, WHITE, 12, "bold", c)
        for i, b in enumerate(bots):
            s.box(x0 + i*145, 330, 135, 75, b, WHITE, NAVY, 11)
            s.arrow(x0 + i*145 + 67, 330, x0+210, 260, GREY, 1.2)
        s.arrow(x0+210, 200, x0+210, 145, GREY, 1.2)
    tree(20, "Arbre à problèmes", "EFFETS : absentéisme scolaire,\ndépenses de santé des ménages", "PROBLÈME CENTRAL :\nmaladies diarrhéiques fréquentes\nchez les moins de 5 ans",
         ["Eau de boisson\nnon traitée", "Peu de latrines\nfonctionnelles", "Lavage des\nmains rare"], RED)
    tree(500, "Arbre à objectifs", "FINS : assiduité scolaire accrue,\ndépenses de santé réduites", "OBJECTIF :\nincidence des diarrhées\nréduite chez les moins de 5 ans",
         ["Eau traitée\nà domicile", "Latrines\nfonctionnelles", "Lavage des mains\naux moments clés"], TEAL)
    s.arrow(450, 230, 510, 230, GOLD, 3)
    s.text(470, 470, "L'IA peut proposer des causes à discuter ; seuls les acteurs de terrain et la communauté valident l'arbre.", 12, GREY, italic=True)


@fig("11.2", "Chaîne de résultats et indicateurs",
     "Intrants, activités, extrants, résultats intermédiaires, impact ; sous chaque maillon un exemple d'indicateur et la source de vérification.", 940, 360)
def f112(s):
    s.header("Chaîne de résultats", "Chaque maillon a ses indicateurs et ses sources de vérification")
    c = [("Intrants", "Budget, staff,\nkits de traitement", "Dépenses vs budget"), ("Activités", "Séances de\nsensibilisation", "Nb séances tenues"),
         ("Extrants", "Ménages formés,\nkits distribués", "Nb ménages formés"), ("Résultats", "Pratiques adoptées", "% ménages traitant\nl'eau (enquête)"),
         ("Impact", "Santé des enfants", "Incidence des\ndiarrhées (centre\nde santé)")]
    for i, (t, e, ind) in enumerate(c):
        x = 25 + i*183
        s.box(x, 80, 165, 44, t, [LIGHT, LIGHT, LTEAL, LGOLD, NAVY][i], WHITE if i == 4 else NAVY, 14, "bold")
        s.box(x, 135, 165, 70, e, WHITE, NAVY, 11.5)
        s.box(x, 220, 165, 80, "Indicateur :\n" + ind, LIGHT, TEAL, 11, stroke=TEAL)
        if i < 4:
            s.arrow(x+165, 102, x+183, 102)
    s.text(470, 330, "Plus on avance vers la droite, moins le résultat dépend du seul projet : l'attribution devient prudente.", 11.5, GREY, italic=True)


# ---------------------------------------------------------------- Module 12
@fig("12.1", "Traitement d'une facture en 14 étapes : qui fait quoi ?",
     "Diagramme en trois couloirs : IA, logiciel comptable, professionnel. Les 14 étapes de la réception à l'archivage sont réparties ; les étapes de validation (vérification du compte, approbation, validation de l'écriture) sont humaines.", 960, 480)
def f121(s):
    s.header("Une facture, 14 étapes, trois acteurs", "IA = proposer et signaler · Logiciel = enregistrer et tracer · Humain = vérifier et décider")
    steps = [(1, 2, "Réception"), (2, 2, "Numérisation /\nphotographie"), (3, 0, "Extraction\ndes champs"), (4, 2, "Contrôle des\ndonnées extraites"),
             (5, 0, "Nature de la\ndépense"), (6, 0, "Imputation\nproposée"), (7, 2, "Vérification\ndu compte"), (8, 1, "Rapprochement\navec le budget"),
             (9, 0, "Détection\nd'anomalies"), (10, 2, "Approbation\n(personne habilitée)"), (11, 2, "Validation de\nl'écriture"), (12, 1, "Mise à jour\ntableaux de bord"),
             (13, 1, "Archivage +\npiste d'audit"), (14, 2, "Traitement des\nerreurs / exceptions")]
    cols = [(LTEAL, NAVY, TEAL), (LGOLD, NAVY, GOLD), (NAVY, WHITE, NAVY)]
    for k, (n, lane, t) in enumerate(steps):
        row, col = k // 7, k % 7
        if row == 1: col = 6 - col
        x = 25 + col*133; y = 90 + row*170
        f, c, st = cols[lane]
        s.box(x, y, 118, 92, f"{n}\n{t}", f, c, 11.5, "bold" if lane == 2 else "normal", st)
        if k < 13 and k != 6:
            if row == 0: s.arrow(x+118, y+46, x+133, y+46)
            else: s.arrow(x, y+46, x-15, y+46)
    s.arrow(25+6*133+59, 182, 25+6*133+59, 260)
    for i, (lbl, (f, c, st)) in enumerate(zip(["IA : propose et signale", "Logiciel : enregistre et trace", "Humain : vérifie et décide"], cols)):
        s.rect(120 + i*250, 405, 22, 16, f, st, 1, 3); s.text(150 + i*250, 413, lbl, 12.5, NAVY, "normal", "start")
    s.text(480, 455, "Les étapes 4, 7, 10 et 11 sont des points de contrôle humain obligatoires.", 12, RED, "bold")


@fig("12.2", "Tableau de bord fictif : exécution budgétaire par ligne",
     "Histogramme horizontal comparant budget et réalisé pour six lignes budgétaires d'un projet, avec taux d'exécution ; deux lignes dépassent 100 % (déplacements 118 %, communication 104 %) et une est sous-exécutée (formation 41 %). Données fictives.", 900, 470)
def f122(s):
    s.header("Tableau de bord budgétaire : programme PRG-SANTE (données fictives)", "Budget annuel vs réalisé au 30 septembre, en milliers d'UM")
    data = [("Personnel", 420, 318), ("Déplacements", 60, 71), ("Formation", 85, 35), ("Équipements", 140, 126), ("Communication", 25, 26), ("Frais de structure", 70, 52)]
    mx = 450; x0 = 200; W = 520
    for i, (n, b, r) in enumerate(data):
        y = 90 + i*58
        s.text(x0-12, y+18, n, 12.5, NAVY, "normal", "end")
        s.rect(x0, y, W*b/mx, 16, LIGHT, GREY, 0.6, 2)
        rate = r/b
        col = RED if rate > 1 else (AMBER if rate < 0.5 else TEAL)
        s.rect(x0, y+19, W*r/mx, 16, col, col, 0.6, 2)
        s.text(x0 + W*max(b, r)/mx + 8, y+18, f"{b} / {r}  ({rate:.0%})".replace("%", " %"), 11.5, col, "bold", "start")
    s.rect(x0, 445, 14, 10, LIGHT, GREY, 0.6, 1); s.text(x0+20, 450, "Budget", 11, GREY, anchor="start")
    s.rect(x0+90, 445, 14, 10, TEAL, TEAL, 0.6, 1); s.text(x0+110, 450, "Réalisé (normal)", 11, GREY, anchor="start")
    s.rect(x0+230, 445, 14, 10, RED, RED, 0.6, 1); s.text(x0+250, 450, "Dépassement", 11, GREY, anchor="start")
    s.rect(x0+350, 445, 14, 10, AMBER, AMBER, 0.6, 1); s.text(x0+370, 450, "Sous-exécution < 50 %", 11, GREY, anchor="start")


# ---------------------------------------------------------------- Module 13
@fig("13.1", "Entonnoir des tests analytiques assistés",
     "Du fichier complet de 40 dépenses à neuf tests automatiques, 22 opérations signalées, 8 opérations prioritaires examinées par l'auditeur, puis 3 constats et une faiblesse de contrôle donnant lieu à recommandations.", 900, 470)
def f131(s):
    s.header("De la population aux constats", "L'IA trie et signale ; l'auditeur examine et conclut")
    lv = [("Population : 40 dépenses, 31 890,50 UM (1er trimestre)", 820), ("9 tests automatiques : doublons · fournisseurs hors base · pièces ·\nauto-approbation · fractionnement · montants ronds · week-end · seuils · libellés", 700),
          ("22 opérations signalées (dont de nombreux faux positifs)", 580), ("8 opérations prioritaires examinées : pièces + entretiens", 440), ("3 constats + 1 faiblesse de contrôle\n→ recommandations", 300)]
    for i, (t, w) in enumerate(lv):
        y = 75 + i*76
        c = [LIGHT, LTEAL, LGOLD, LIGHT, NAVY][i]
        s.box(450 - w/2, y, w, 62, t, c, WHITE if i == 4 else NAVY, 12.5, "bold" if i in (0, 4) else "normal")


@fig("13.2", "Carte thermique des risques",
     "Matrice 5 × 5 probabilité × impact avec cinq risques positionnés : paiements en double, avances non justifiées, fractionnement des achats, fuite de données via IA, dépendance à un fournisseur.", 820, 540)
def f132(s):
    s.header("Cartographie des risques (exemple)", "Probabilité × impact, échelle de 1 à 5 : avant mesures de maîtrise")
    x0, y0, c = 140, 80, 82
    for i in range(5):
        for j in range(5):
            sc = (i+1)*(j+1)
            col = LTEAL if sc <= 4 else (LGOLD if sc <= 9 else (("#F0C9A0") if sc <= 14 else LRED))
            s.rect(x0 + i*c, y0 + (4-j)*c, c, c, col, WHITE, 2, 0)
    for k in range(5):
        s.text(x0 + k*c + c/2, y0 + 5*c + 16, str(k+1), 12, GREY)
        s.text(x0 - 14, y0 + (4-k)*c + c/2, str(k+1), 12, GREY)
    s.text(x0 + 2.5*c, y0 + 5*c + 40, "Probabilité →", 13, NAVY, "bold")
    s.add(f'<text x="90" y="{y0+2.5*c}" font-family="{FONT}" font-size="13" font-weight="bold" fill="{NAVY}" text-anchor="middle" transform="rotate(-90 90 {y0+2.5*c})">Impact →</text>')
    R = [(3, 4, "R1"), (4, 3, "R2"), (2, 4, "R3"), (3, 5, "R4"), (2, 3, "R5")]
    for p, im, t in R:
        s.circle(x0 + (p-1)*c + c/2, y0 + (5-im)*c + c/2, 16, NAVY, WHITE, 2)
        s.text(x0 + (p-1)*c + c/2, y0 + (5-im)*c + c/2, t, 11.5, WHITE, "bold")
    leg = ["R1 Paiements en double", "R2 Avances non justifiées", "R3 Fractionnement des achats", "R4 Fuite de données via IA", "R5 Dépendance fournisseur"]
    for i, l in enumerate(leg):
        s.text(570, 120 + i*28, l, 12, NAVY, "normal", "start")


# ---------------------------------------------------------------- Module 14
@fig("14.1", "Recrutement assisté : où l'IA aide, où l'humain décide",
     "Étapes : besoin, fiche de poste (IA assiste), annonce (IA assiste), réception des candidatures (logiciel), présélection selon grille humaine, entretiens, décision et retour aux candidats. Le tri automatique sans contrôle humain est barré.", 940, 380)
def f141(s):
    s.header("Recrutement : l'IA prépare, l'humain évalue et décide", "Aucune décision sur une personne n'est déléguée à une machine")
    st = [("Besoin\nvalidé", 1), ("Fiche de\nposte", 0), ("Annonce\ninclusive", 0), ("Réception\ncandidatures", 2), ("Présélection\nsur grille", 1), ("Entretiens\nstructurés", 1), ("Décision +\nretours", 1)]
    for i, (t, h) in enumerate(st):
        x = 20 + i*131
        c = NAVY if h == 1 else (TEAL if h == 0 else GOLD)
        s.box(x, 110, 118, 70, t, c, WHITE, 12, "bold", c)
        if i < 6:
            s.arrow(x+118, 145, x+131, 145)
    s.box(330, 230, 300, 64, "Classement automatique des candidats\npar une IA sans contrôle humain", LRED, RED, 12, "bold", RED)
    s.add(f'<line x1="335" y1="235" x2="625" y2="290" stroke="{RED}" stroke-width="3"/>')
    s.text(170, 330, "Bleu : décision humaine · Vert pétrole : rédaction assistée · Or : logiciel", 11.5, GREY, anchor="start")


# ---------------------------------------------------------------- Module 15
@fig("15.1", "Entonnoir des opportunités de financement",
     "Veille (40 appels repérés), filtre d'éligibilité (12), adéquation stratégique (5), décision go/no-go (3), soumission (2), financement obtenu (taux variable).", 900, 460)
def f151(s):
    s.header("De la veille à la soumission", "L'IA élargit la veille et accélère l'analyse ; la direction décide du go / no-go")
    lv = [("Veille : 40 appels repérés", 820, "IA : résumés, critères extraits"), ("Éligibilité vérifiée : 12", 660, "Humain : confirmation sur textes officiels"),
          ("Adéquation stratégique : 5", 500, "Grille de décision"), ("Go / No-go : 3", 360, "Direction"), ("Dossiers soumis : 2", 240, "IA : brouillons · Humain : contenu")]
    for i, (t, w, n) in enumerate(lv):
        y = 75 + i*72
        s.box(450 - w/2, y, w, 52, t, [LIGHT, LTEAL, LGOLD, NAVY, TEAL][i], WHITE if i >= 3 else NAVY, 13, "bold")
        s.text(450 + w/2 + 10 if i >= 2 else 870, y+26, n if i >= 2 else "", 11, GREY, anchor="start")
    s.text(450, 440, "Chiffres illustratifs (fictifs).", 11, GREY, italic=True)


# ---------------------------------------------------------------- Module 16
@fig("16.1", "Circuit achats et logistique",
     "Demande d'achat, vérification budgétaire, consultation, tableau comparatif des offres, décision du comité, bon de commande, réception et rapprochement à trois voies (commande, bon de livraison, facture), stock et inventaire, immobilisations.", 940, 420)
def f161(s):
    s.header("Circuit achats : de la demande à l'inventaire", "Séparation des tâches : demander ≠ choisir ≠ réceptionner ≠ payer")
    st = ["Demande\nd'achat", "Contrôle\nbudgétaire", "Consultation\n(≥ 3 offres\nselon seuil)", "Tableau\ncomparatif", "Décision\n(comité)", "Bon de\ncommande", "Réception\n+ rapprochement\n3 voies", "Stock /\ninventaire /\nimmobilisations"]
    ai = {3, 6}
    for i, t in enumerate(st):
        x = 18 + i*115
        c = TEAL if i in ai else (NAVY if i == 4 else LIGHT)
        s.box(x, 110, 104, 90, t, c, WHITE if i in ai or i == 4 else NAVY, 11.5, "bold" if i == 4 else "normal", c if i in ai or i == 4 else NAVY)
        if i < 7:
            s.arrow(x+104, 155, x+115, 155)
    s.box(120, 260, 700, 90, "Où l'IA aide : extraire les offres reçues (PDF, photos) dans un tableau normalisé ; signaler les écarts\nentre commande, bon de livraison et facture ; proposer des alertes de réapprovisionnement.\nOù elle n'intervient pas : le choix du fournisseur et la réception physique.", LGOLD, NAVY, 12, stroke=GOLD)


# ---------------------------------------------------------------- Module 17
@fig("17.1", "La chaîne éditoriale assistée",
     "Faits vérifiés du programme, messages clés validés, calendrier éditorial, production de déclinaisons par l'IA, relecture humaine (exactitude, consentement, dignité), publication, mesure et ajustement.", 940, 360)
def f171(s):
    s.header("Communication : une chaîne éditoriale assistée", "La matière première, ce sont des faits vérifiés et des consentements")
    st = [("Faits vérifiés\ndu programme", LIGHT), ("Messages\nclés validés", LIGHT), ("Calendrier\néditorial", LTEAL), ("Déclinaisons\nproduites par l'IA", LTEAL),
          ("Relecture :\nexactitude, dignité,\nconsentement", NAVY), ("Publication", LIGHT), ("Mesure et\najustement", LGOLD)]
    for i, (t, c) in enumerate(st):
        x = 18 + i*131
        s.box(x, 110, 118, 90, t, c, WHITE if c == NAVY else NAVY, 11.5, "bold" if c == NAVY else "normal")
        if i < 6:
            s.arrow(x+118, 155, x+131, 155)
    s.path("M836,200 C836,290 77,290 77,202", GREY, 1.3, True, "5,4")
    s.text(470, 315, "Les résultats de la mesure alimentent le calendrier suivant.", 11.5, GREY, italic=True)


# ---------------------------------------------------------------- Module 18
@fig("18.1", "La boucle de redevabilité envers les communautés",
     "Canaux multiples (ligne téléphonique, boîte à suggestions, messagerie, agents), enregistrement, classification assistée, traitement prioritaire des cas sensibles par une personne référente, réponse à la personne, analyse des tendances, ajustement du programme, retour à la communauté.", 900, 520)
def f181(s):
    import math
    s.header("Retours, plaintes et réclamations : boucler la boucle", "Les cas sensibles sortent immédiatement du circuit automatisé")
    st = ["Canaux multiples\n(voix, papier,\nmessagerie, agents)", "Enregistrement\n(minimisation)", "Classification\nassistée par l'IA\n+ langue détectée", "Traitement par\nle service concerné", "Réponse à la\npersonne (délai)", "Analyse des\ntendances", "Ajustement du\nprogramme", "Retour collectif\nà la communauté"]
    cx, cy, r = 450, 300, 190
    pts = []
    for i, t in enumerate(st):
        a = -math.pi/2 + i*2*math.pi/8
        pts.append((cx + r*1.3*math.cos(a), cy + r*0.95*math.sin(a)))
    for i in range(8):
        x1, y1 = pts[i]; x2, y2 = pts[(i+1) % 8]
        s.arrow(x1 + (x2-x1)*0.3, y1 + (y2-y1)*0.3, x1 + (x2-x1)*0.7, y1 + (y2-y1)*0.7, TEAL, 1.8)
    for i, (x, y) in enumerate(pts):
        s.box(x-72, y-30, 144, 60, st[i], LTEAL if i == 2 else LIGHT, NAVY, 10.5)
    s.box(cx-110, cy-38, 220, 76, "Cas sensibles (abus,\nexploitation, sécurité) :\nréférent·e humain·e\nimmédiatement", RED, WHITE, 11.5, "bold", RED)


# ---------------------------------------------------------------- Module 19
@fig("19.1", "Cycle de vie d'un projet IA dans une ASBL",
     "Douze étapes : problème, diagnostic, cahier des charges, processus cible, sélection, budget, conception, intégration, tests, pilote, formation et déploiement, documentation ; avec deux portes de décision (go/no-go après cadrage et après pilote).", 960, 430)
def f191(s):
    s.header("Du problème à la solution en production", "Deux portes de décision : après le cadrage et après le pilote")
    st = ["Problème", "Diagnostic", "Cahier des\ncharges", "Processus\ncible", "Sélection\nsolution", "Budget", "Conception", "Intégration", "Tests", "Pilote", "Formation +\ndéploiement", "Documentation"]
    for i, t in enumerate(st):
        row = i // 6; col = i % 6 if row == 0 else 5 - (i % 6)
        x = 30 + col*155; y = 90 + row*170
        s.box(x, y, 125, 64, f"{i+1}. {t}", LIGHT if i < 6 else LTEAL, NAVY, 12)
        if i < 11 and i != 5:
            if row == 0:
                s.arrow(x+125, y+32, x+155, y+32)
            else:
                s.arrow(x, y+32, x-30, y+32)
    s.arrow(30+5*155+62, 154, 30+5*155+62, 260)
    s.box(820, 178, 120, 40, "GO / NO-GO", GOLD, NAVY, 12, "bold", GOLD)
    s.box(250, 345, 130, 40, "GO / NO-GO", GOLD, NAVY, 12, "bold", GOLD)
    s.text(480, 410, "Un « non » après le pilote est un résultat utile : il évite d'industrialiser une mauvaise solution.", 11.5, GREY, italic=True)


# ---------------------------------------------------------------- Module 20
@fig("20.1", "Gouvernance de l'IA dans l'ASBL",
     "Conseil d'administration (politique IA, appétence au risque), direction (arbitrages, budget), comité ou référent IA (registre des outils, validation des usages, incidents), utilisateurs formés, avec audit périodique et amélioration continue.", 900, 470)
def f201(s):
    s.header("Une gouvernance de l'IA proportionnée", "Pour une petite ASBL, le « comité » peut être une personne référente et un administrateur")
    lv = [("Conseil d'administration", "Adopte la politique d'utilisation de l'IA · fixe les limites · reçoit un bilan annuel", NAVY, WHITE),
          ("Direction exécutive", "Arbitre les priorités · alloue le budget · répond des incidents graves", TEAL, WHITE),
          ("Référent·e / comité IA", "Tient le registre des outils · valide les nouveaux usages · gère incidents et formation", LGOLD, NAVY),
          ("Utilisateurs formés", "Appliquent la politique · vérifient les sorties · signalent les problèmes", LIGHT, NAVY)]
    for i, (t, d, c, tc) in enumerate(lv):
        y = 80 + i*88
        s.box(60, y, 220, 70, t, c, tc, 13, "bold", NAVY if c != GOLD else GOLD)
        s.box(300, y, 440, 70, d, WHITE, NAVY, 12)
        if i < 3:
            s.arrow(170, y+70, 170, y+88)
    s.box(770, 80, 100, 334, "Audit\npériodique\n\n+\n\nAmélio-\nration\ncontinue", LTEAL, NAVY, 12, "bold", TEAL)


@fig("20.2", "Facteurs d'adoption d'un nouvel outil",
     "Quatre déterminants inspirés des modèles d'acceptation de la technologie : utilité perçue (performance attendue), facilité d'utilisation (effort attendu), influence sociale, conditions facilitantes ; et les actions correspondantes.", 900, 420)
def f202(s):
    s.header("Pourquoi les équipes adoptent (ou non) un outil", "Lecture pratique des modèles d'acceptation de la technologie (Davis, 1989 ; Venkatesh et al., 2003)")
    f = [("Utilité perçue", "« Cela m'aide-t-il\nvraiment ? »", "Démontrer sur une tâche\nréelle de la personne"),
         ("Facilité perçue", "« Est-ce simple\npour moi ? »", "Modèles prêts à l'emploi,\nformation courte, aide"),
         ("Influence sociale", "« Mes collègues et\nma hiérarchie l'utilisent-ils ? »", "Ambassadeurs, exemple\nde la direction"),
         ("Conditions facilitantes", "« Ai-je le matériel,\nle temps, le droit ? »", "Équipement, temps dédié,\nrègles claires")]
    for i, (t, q, a) in enumerate(f):
        x = 25 + i*218
        s.box(x, 85, 200, 46, t, [NAVY, TEAL, GOLD, NAVY][i], WHITE, 13.5, "bold", [NAVY, TEAL, GOLD, NAVY][i])
        s.box(x, 140, 200, 80, q, LIGHT, NAVY, 12)
        s.box(x, 235, 200, 80, "Action :\n" + a, WHITE, TEAL, 12, stroke=TEAL)
    s.box(250, 345, 400, 50, "Intention d'utiliser → usage réel → habitudes", LGOLD, NAVY, 13, "bold", GOLD)


# ---------------------------------------------------------------- Module 21
@fig("21.1", "Les dix études de cas et leurs modules de référence",
     "Tableau visuel reliant chacune des dix études de cas aux modules mobilisés.", 900, 520)
def f211(s):
    s.header("Dix cas, dix problèmes réels", "Chaque cas mobilise plusieurs modules")
    cases = [("1 Comptabilité désorganisée", "M7 · M12"), ("2 Retards de reporting", "M5 · M12 · M15"), ("3 Risques de détournement", "M13 · M16"),
             ("4 Dépendance financière", "M15 · M17"), ("5 Perte de documents", "M7 · M10"), ("6 Mauvais suivi de projets", "M11"),
             ("7 Bénévoles mal gérés", "M14"), ("8 Bénéficiaires non suivis", "M18 · M8"), ("9 Administration manuelle", "M9 · M10 · M19"),
             ("10 Politique d'IA responsable", "M8 · M20")]
    for i, (c, m) in enumerate(cases):
        col, row = i % 2, i // 2
        x, y = 40 + col*420, 75 + row*85
        s.box(x, y, 280, 62, c, LIGHT if (i // 2) % 2 == 0 else WHITE, NAVY, 13, "bold")
        s.box(x+290, y, 110, 62, m, TEAL, WHITE, 12.5, "bold", TEAL)


# ---------------------------------------------------------------- Module 22
@fig("22.1", "Plan de transformation sur 90 jours",
     "Diagramme de Gantt sur 13 semaines : diagnostic (semaines 1–3), politique d'IA et règles de données (2–5), formation socle (3–6), deux cas d'usage pilotes (5–10), évaluation (10–11), décision et feuille de route annuelle (12–13).", 940, 440)
def f221(s):
    s.header("Plan à 90 jours : Lumière des Collines", "Commencer petit, mesurer, décider")
    x0, W = 260, 650
    for w in range(13):
        x = x0 + w*W/13
        s.rect(x, 70, W/13, 330, LIGHT if w % 2 == 0 else WHITE, WHITE, 0, 0)
        s.text(x + W/26, 85, f"S{w+1}", 11, GREY)
    tasks = [("Diagnostic et inventaire", 1, 3, NAVY), ("Politique IA + règles données", 2, 5, NAVY), ("Formation socle (M1–M3, M8)", 3, 6, TEAL),
             ("Pilote A : PV et suivi décisions", 5, 10, GOLD), ("Pilote B : suivi des élèves (tableur)", 5, 10, GOLD), ("Mesure des indicateurs", 6, 11, TEAL),
             ("Évaluation des pilotes", 10, 11, NAVY), ("Décision + feuille de route 12 mois", 12, 13, RED)]
    for i, (t, a, b, c) in enumerate(tasks):
        y = 105 + i*37
        s.text(x0 - 10, y+12, t, 12, NAVY, "normal", "end")
        s.rect(x0 + (a-1)*W/13 + 2, y, (b-a+1)*W/13 - 4, 24, c, c, 0, 5)
    s.text(470, 420, "Jalons : S3 diagnostic validé · S5 politique adoptée · S11 bilan des pilotes · S13 décision du conseil.", 11.5, GREY, italic=True)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(out, exist_ok=True)
    for fid, title, alt, run in FIGS:
        run(out)
    with open(os.path.join(out, "..", "credits", "registre_credits_figures.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["figure", "fichier", "titre", "texte_alternatif", "auteur", "nature", "licence", "date", "modifications"])
        for fid, title, alt, _ in FIGS:
            w.writerow([fid, f"fig_{fid.replace('.', '_')}.svg", title, alt, "Verdi Imbole (création originale, génération assistée)",
                        "Schéma original SVG", "© 2026 Verdi Imbole – tous droits réservés", "2026-11-20", "Néant"])
    print(f"{len(FIGS)} figures générées")


if __name__ == "__main__":
    main()
