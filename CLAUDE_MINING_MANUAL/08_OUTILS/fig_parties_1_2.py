# -*- coding: utf-8 -*-
"""Figures des parties I et II. Toutes : « Illustration réalisée pour cet ouvrage »."""
import math
import numpy as np
from fig_lib import *

def f01_1():
    fig, ax = canvas(11, 5.8, 110, 58)
    title(ax, "La chaîne de valeur minière et les points d'appui de l'IA générative", fs=13)
    etapes = [("Exploration", "cartes,\nsondages,\nrapports"),
              ("Études", "ressources,\nréserves,\nfaisabilité"),
              ("Construction", "contrats,\nplannings,\navancement"),
              ("Extraction", "forage-minage,\nchargement,\ntransport"),
              ("Traitement", "usine,\nlaboratoire,\nbilans"),
              ("Vente &\nexport", "contrats,\nlogistique,\nexpéditions"),
              ("Fermeture", "réhabilitation,\nsuivi post-\nfermeture")]
    x0, w, gap = 2, 13.6, 2.0
    for i, (e, d) in enumerate(etapes):
        x = x0 + i * (w + gap)
        box(ax, x, 33, w, 9, e, fc=NAVY, ec=NAVY, color="white", bold=True, fs=9.5)
        box(ax, x, 20, w, 11, d, fc=GREY, ec="#B8C2CC", fs=8, color=INK)
        if i < len(etapes) - 1:
            arrow(ax, (x + w, 37.5), (x + w + gap, 37.5), color=GOLD, lw=2)
    box(ax, 2, 4, 106, 13, "", fc=LIGHTTURQ, ec=TURQ)
    ax.text(55, 14.2, "Fonctions transversales assistées par Claude", ha="center", fontsize=10, fontweight="bold", color=TURQ)
    ax.text(55, 8.5, "HSE  •  Environnement & eau  •  Relations communautaires  •  Achats & logistique  •  Juridique & conformité\n"
            "Finance, fiscalité & contrôle de gestion  •  Audit  •  RH & compétences  •  Gouvernance, ESG & reporting",
            ha="center", va="center", fontsize=8.6, color=INK, linespacing=1.6)
    ax.text(55, 49.5, "Chaque étape produit et consomme des documents : c'est là que l'IA générative apporte le plus de valeur.",
            ha="center", fontsize=8.8, color=MID, style="italic")
    return save(fig, "fig01_1_chaine_valeur")

def f01_2():
    fig, ax = canvas(10, 7, 100, 70)
    ax.add_patch(Rectangle((0, 0), 100, 70, fc="#F3F1E7", ec="none", zorder=0))
    title(ax, "Plan schématique du site de Mbiyo Copper Cobalt SA (fictif)", y=67)
    # rivière
    xs = np.linspace(0, 100, 200); ys = 12 + 4 * np.sin(xs / 9)
    ax.plot(xs, ys, color="#6FA8DC", lw=6, solid_capstyle="round", zorder=1)
    ax.text(88, 8, "Rivière Mbiyo", color="#2F6FA8", fontsize=8.5, style="italic")
    # permis
    ax.add_patch(Rectangle((8, 18), 84, 44, fc="none", ec=RED, lw=1.6, ls="--", zorder=1))
    ax.text(9, 60, "Limite du permis PE-MCC-001 (fictif)", color=RED, fontsize=8)
    # fosses
    for (cx, cy, rw, rh, lab) in [(30, 46, 18, 11, "Fosse\nMbiyo Nord"), (55, 48, 14, 9, "Fosse\nMbiyo Sud")]:
        for k, c in enumerate(["#C9B79C", "#B49F80", "#9C8665", "#83704F"]):
            ax.add_patch(Ellipse((cx, cy), rw - k * 3.5, rh - k * 2.2, fc=c, ec="#6E5B3E", lw=0.6, zorder=2))
        ax.text(cx, cy, lab, ha="center", va="center", fontsize=7.5, color="white", fontweight="bold", zorder=3)
    box(ax, 15, 27, 13, 7, "Verses à\nstériles", fc="#CFC6B5", ec="#8C7B60", fs=7.5)
    box(ax, 66, 32, 15, 8, "Usine SX-EW\n+ précip. Co", fc=LIGHTNAVY, ec=NAVY, fs=7.5, bold=True)
    box(ax, 66, 22, 15, 6, "Atelier maintenance\nmagasin", fc=GREY, ec=MID, fs=7)
    box(ax, 40, 22, 18, 9, "Parc à résidus\nKilima", fc="#E3D7B8", ec="#9C8665", fs=7.5)
    box(ax, 83, 44, 9, 6, "Bureaux\nlabo", fc=GREY, ec=MID, fs=7)
    # villages
    for (x, y, n) in [(4, 50, "Kasongo-\nMbiyo"), (95, 26, "Lupanda"), (48, 3.2, "Mwinda")]:
        ax.add_patch(Circle((x, y), 2.2, fc=GOLD, ec=NAVY, lw=1, zorder=3))
        ax.text(x, y - 6.5 if y > 10 else y + 3.0, n, ha="center", fontsize=7.5, color=NAVY, fontweight="bold")
    # route
    ax.plot([92, 100], [36, 36], color="#555", lw=2.5); ax.plot([81, 92], [36, 36], color="#555", lw=2.5)
    ax.text(93, 37.5, "Route vers\nKolwezi (45 km)", fontsize=7, color="#333")
    arrow(ax, (47, 40), (66, 36), color=MID, lw=1.2, ls="--")
    ax.text(52, 38.5, "minerai", fontsize=7, color=MID, rotation=-10)
    # échelle et nord
    ax.plot([8, 18], [3, 3], color=INK, lw=2); ax.text(13, 4.2, "≈ 2 km", ha="center", fontsize=7)
    arrow(ax, (96, 56), (96, 63), color=INK, lw=1.5); ax.text(96, 64.5, "N", ha="center", fontsize=9, fontweight="bold")
    note(ax, "Plan non à l'échelle, entièrement fictif — sert de repère pour les exercices de l'ouvrage.", y=0.8)
    return save(fig, "fig01_2_plan_site_mcc")

def f02_1():
    fig, ax = canvas(9, 6.2, 90, 62)
    title(ax, "Des concepts emboîtés", y=59.5)
    cercles = [(45, 29, 42, 27, LIGHTNAVY, NAVY, "Intelligence artificielle", "systèmes qui réalisent des tâches\nassociées à l'intelligence humaine"),
               (45, 25, 33, 21, "#C8D6E8", NAVY, "Apprentissage automatique", "apprend des règles à partir de données"),
               (45, 21, 24, 15, LIGHTTURQ, TURQ, "Apprentissage profond", "réseaux de neurones à nombreuses couches"),
               (45, 17, 15, 9, GOLD, "#8A6D12", "IA générative\n(LLM : Claude)", "")]
    for (cx, cy, rx, ry, fc, ec, lab, d) in cercles:
        ax.add_patch(Ellipse((cx, cy), 2 * rx, 2 * ry, fc=fc, ec=ec, lw=1.6))
    ax.text(45, 53, "Intelligence artificielle", ha="center", fontsize=11, fontweight="bold", color=NAVY)
    ax.text(45, 50, "systèmes réalisant des tâches associées à l'intelligence humaine", ha="center", fontsize=8, color=INK)
    ax.text(45, 43.5, "Apprentissage automatique (machine learning)", ha="center", fontsize=10, fontweight="bold", color=NAVY)
    ax.text(45, 40.7, "apprend des régularités à partir de données", ha="center", fontsize=8)
    ax.text(45, 33.6, "Apprentissage profond (deep learning)", ha="center", fontsize=9.5, fontweight="bold", color=TURQ)
    ax.text(45, 31, "réseaux de neurones à nombreuses couches", ha="center", fontsize=8)
    ax.text(45, 17, "IA générative\nLLM (ex. : Claude)", ha="center", va="center", fontsize=9.5, fontweight="bold", color=NAVY)
    note(ax, "Illustration réalisée pour cet ouvrage.", y=0.5)
    return save(fig, "fig02_1_emboitement")

def f02_2():
    fig, ax = canvas(11, 5.6, 110, 56)
    title(ax, "IA « classique » (prédictive) et IA générative : deux familles complémentaires", y=53.5, fs=12)
    for x0, head, col, lines, ex in [
        (2, "IA prédictive / analytique", NAVY,
         ["Entrée : données structurées (capteurs,", "tableaux, historiques)", "Sortie : un nombre, une classe, une alerte",
          "Entraînée pour UNE tâche précise", "Évaluée par des métriques (erreur, précision)"],
         "Ex. mine : prédire la panne d'un camion\nà partir des vibrations ; estimer la teneur\npar krigeage ; tri optique du minerai"),
        (57, "IA générative (LLM)", TURQ,
         ["Entrée : langage, documents, images", "Sortie : du texte, du code, des tableaux,", "des documents nouveaux",
          "Polyvalente : rédiger, résumer, analyser,", "traduire, raisonner, programmer"],
         "Ex. mine : rédiger un rapport d'incident,\nrésumer une étude d'impact, comparer\ndeux contrats, expliquer un écart budgétaire")]:
        box(ax, x0, 40, 51, 8, head, fc=col, ec=col, color="white", bold=True, fs=11)
        for i, l in enumerate(lines):
            ax.text(x0 + 2.5, 35 - i * 3.6, "• " + l if not l.startswith(("tableaux", "des doc", "traduire")) else "   " + l,
                    fontsize=8.8, color=INK, va="center")
        box(ax, x0, 3, 51, 12, ex, fc=LIGHTTURQ if col == TURQ else LIGHTNAVY, ec=col, fs=8.4)
    ax.text(55, 30, "≠", fontsize=30, ha="center", va="center", color=GOLD, fontweight="bold")
    return save(fig, "fig02_2_classique_vs_generative")

def f02_3():
    fig, ax = canvas(10, 5.4, 100, 54)
    title(ax, "Un réseau de neurones, vu de très loin", y=51.5)
    layers = [3, 5, 5, 2]; xs = [15, 38, 61, 84]
    names = ["Couche d'entrée\n(données)", "Couches cachées\n(représentations)", "", "Couche de sortie\n(prédiction)"]
    pos = []
    for li, (n, x) in enumerate(zip(layers, xs)):
        ys = np.linspace(12, 40, n) if n > 1 else [26]
        pos.append([(x, y) for y in ys])
    for a, b in zip(pos[:-1], pos[1:]):
        for p in a:
            for q in b:
                ax.plot([p[0], q[0]], [p[1], q[1]], color="#B8C2CC", lw=0.7, zorder=1)
    cols = [GOLD, NAVY, NAVY, TURQ]
    for li, layer in enumerate(pos):
        for (x, y) in layer:
            ax.add_patch(Circle((x, y), 2.1, fc=cols[li], ec="white", lw=1.5, zorder=3))
    ax.text(15, 5.5, names[0], ha="center", fontsize=8.5); ax.text(49.5, 5.5, names[1], ha="center", fontsize=8.5)
    ax.text(84, 5.5, names[3], ha="center", fontsize=8.5)
    ax.text(26.5, 45, "chaque lien porte un « poids »\najusté pendant l'entraînement", ha="center", fontsize=8, color=MID, style="italic")
    note(ax, "Les grands modèles de langage comptent des milliards de poids. Illustration réalisée pour cet ouvrage.", y=0.8)
    return save(fig, "fig02_3_reseau_neurones")

def f03_1():
    fig, ax = canvas(11, 3.8, 110, 38)
    title(ax, "Le texte est découpé en tokens avant d'être traité", y=35.5, fs=12)
    toks = ["Le", " minerai", " oxyd", "é", " de", " Mbi", "yo", " titre", " 2", ",", "4", " %", " Cu", "."]
    x = 3
    for i, t in enumerate(toks):
        w = max(4.5, len(t) * 1.55 + 2.2)
        box(ax, x, 18, w, 8, t.replace(" ", "␣"), fc=[LIGHTNAVY, LIGHTTURQ, LIGHTGOLD][i % 3], ec=MID, fs=9, rounding=1)
        ax.text(x + w / 2, 14.5, str(1000 + 37 * i + (i * i) % 17), ha="center", fontsize=6.8, color=MID)
        x += w + 0.8
    ax.text(3, 11, "▲ identifiants numériques (valeurs illustratives)", fontsize=7.5, color=MID)
    ax.text(55, 5, "Découpage illustratif : le découpage réel dépend du « tokenizer » de chaque modèle. Les mots rares, les noms propres\n"
            "et les nombres sont souvent fragmentés — une des raisons pour lesquelles un LLM peut mal compter ou mal recopier un chiffre.",
            ha="center", fontsize=8, color=INK)
    return save(fig, "fig03_1_tokens")

def f03_2():
    fig, ax = plt.subplots(figsize=(9, 4.2))
    mots = ["camion", "convoyeur", "pelle", "train", "hélicoptère", "dromadaire"]
    p = [0.58, 0.24, 0.09, 0.06, 0.02, 0.01]
    cols = [TURQ] + [NAVY] * 4 + [RED]
    ax.barh(mots[::-1], p[::-1], color=cols[::-1], height=0.6)
    for i, v in enumerate(p[::-1]):
        ax.text(v + 0.01, i, f"{v:.0%}", va="center", fontsize=9)
    ax.set_xlim(0, 0.7); ax.set_xlabel("Probabilité estimée du token suivant (valeurs illustratives)")
    ax.set_title("« Le minerai est transporté jusqu'à l'usine par … »", fontsize=11.5, color=NAVY)
    style_axes(ax, grid=False)
    fig.text(0.5, -0.04, "Le modèle ne « sait » pas : il calcule une distribution de probabilités, puis choisit un token. "
             "Illustration réalisée pour cet ouvrage.", ha="center", fontsize=8, style="italic", color=MID)
    return save(fig, "fig03_2_probabilites", "GRAPHIQUES")

def f03_3():
    fig, ax = canvas(10.5, 5.8, 105, 58)
    title(ax, "La fenêtre de contexte : la « mémoire de travail » d'une conversation", y=55.5, fs=12)
    box(ax, 4, 6, 70, 44, "", fc="white", ec=NAVY, lw=2)
    ax.text(39, 47.5, "Fenêtre de contexte (jusqu'à 1 million de tokens selon le modèle)", ha="center", fontsize=9, color=NAVY, fontweight="bold")
    blocs = [("Instructions système / instructions de projet", LIGHTNAVY, 6), ("Préférences et mémoire (si activées)", LIGHTNAVY, 4),
             ("Documents joints (PDF, Excel, rapports…)", LIGHTGOLD, 10), ("Historique de la conversation", GREY, 8),
             ("Votre nouvelle question", LIGHTTURQ, 4), ("Réponse en cours de génération", "#CDEBD9", 5)]
    y = 44
    for lab, c, h in blocs:
        y -= h + 0.6
        box(ax, 7, y, 64, h, lab, fc=c, ec=MID, fs=8.6, rounding=0.8)
    box(ax, 78, 30, 24, 16, "Ce qui est HORS\nde la fenêtre\nn'existe pas\npour le modèle", fc=LIGHTRED, ec=RED, fs=8.6, bold=True)
    box(ax, 78, 8, 24, 18, "Plus la fenêtre est\nchargée, plus le\nmodèle peut négliger\ndes détails : gardez\nle contexte pertinent", fc=GREY, ec=MID, fs=8)
    note(ax, "Valeur de 1 million de tokens : documentation Anthropic, Models overview (consultée le 16/11/2026). Illustration réalisée pour cet ouvrage.", y=2.5)
    return save(fig, "fig03_3_fenetre_contexte")

def f03_4():
    fig, ax = canvas(11.5, 4.4, 115, 44)
    title(ax, "Ce qui se passe entre votre question et la réponse", y=41.5, fs=12)
    steps = [("1. Votre instruction", "texte + fichiers", LIGHTTURQ),
             ("2. Tokenisation", "découpage en tokens", LIGHTNAVY),
             ("3. Réflexion (optionnelle)", "raisonnement interne\nselon l'effort", LIGHTGOLD),
             ("4. Calcul des probabilités", "token par token", LIGHTNAVY),
             ("5. Génération", "réponse assemblée\nprogressivement", LIGHTNAVY),
             ("6. Votre vérification", "relecture, contrôle,\nvalidation", "#CDEBD9")]
    x, w = 2, 16.6
    for i, (h, d, c) in enumerate(steps):
        box(ax, x, 14, w, 18, "", fc=c, ec=NAVY if i != 5 else GREEN)
        ax.text(x + w / 2, 27, h, ha="center", fontsize=8.6, fontweight="bold", color=NAVY)
        ax.text(x + w / 2, 20.5, d, ha="center", va="center", fontsize=8, color=INK)
        if i < 5: arrow(ax, (x + w, 23), (x + w + 2.2, 23), color=GOLD, lw=2)
        x += w + 2.2
    ax.text(57, 7, "Les étapes 2 à 5 sont automatiques. L'étape 6 est toujours la vôtre.", ha="center", fontsize=9.5, color=RED, fontweight="bold")
    return save(fig, "fig03_4_traitement_instruction")

def f04_1():
    fig, ax = canvas(11, 6.4, 110, 64)
    title(ax, "L'écosystème Claude (état au 16 novembre 2026)", y=61.5)
    box(ax, 40, 24, 30, 14, "Modèles Claude\nFable • Opus • Sonnet • Haiku", fc=NAVY, ec=NAVY, color="white", bold=True, fs=10.5)
    items = [(4, 46, "Applications Claude\nWeb • Bureau • Mobile", "conversations, Projects,\nArtifacts, Research, mémoire"),
             (40, 46, "Claude Cowork", "tâches longues, fichiers,\ntâches planifiées"),
             (76, 46, "Claude Code", "agent de développement\n(terminal, IDE, web)"),
             (4, 4, "Claude Platform (API)", "intégration dans les applications\nde l'entreprise, agents gérés"),
             (40, 4, "Plateformes cloud", "Amazon Bedrock, Google Cloud,\nMicrosoft Foundry"),
             (76, 4, "Extensions & outils", "connecteurs (MCP), Skills, plugins,\nClaude in Chrome, Microsoft 365")]
    for x, y, h, d in items:
        box(ax, x, y, 30, 14, "", fc=LIGHTTURQ if y > 30 else LIGHTNAVY, ec=TURQ if y > 30 else NAVY)
        ax.text(x + 15, y + 10, h, ha="center", va="center", fontsize=9.2, fontweight="bold", color=NAVY)
        ax.text(x + 15, y + 4.2, d, ha="center", va="center", fontsize=7.6, color=INK)
        arrow(ax, (x + 15, y if y > 30 else y + 14), (55, 38 if y > 30 else 24), color=GOLD, lw=1.3, style="<|-|>")
    note(ax, "Sources : Anthropic, Models overview ; Claude Help Center ; claude.com/pricing (consultés le 16/11/2026). Illustration réalisée pour cet ouvrage.", y=1)
    return save(fig, "fig04_1_ecosysteme")

def f04_2():
    fig, ax = plt.subplots(figsize=(9.5, 5))
    m = [("Claude Haiku 5.5", 0.10, 1, "le plus rapide ;\nvolume, extraction, tri"),
         ("Claude Sonnet 5.5", 2, 2, "meilleur équilibre\nvitesse / intelligence"),
         ("Claude Opus 5.5", 4, 3, "point de départ conseillé\npour la plupart des travaux"),
         ("Claude Fable 5.2", 8, 4, "raisonnement exigeant,\ntravaux longs et complexes")]
    cols = [TURQ, NAVY, GOLD, RED]
    for (n, p, lvl, d), c in zip(m, cols):
        ax.scatter(lvl, p, s=900, color=c, zorder=3, edgecolor="white", lw=2)
        ax.text(lvl, p + 0.75, n, ha="center", fontsize=9.5, fontweight="bold", color=NAVY)
        ax.text(lvl, p - 1.25, d, ha="center", va="top", fontsize=7.8, color=INK)
    ax.set_xticks([1, 2, 3, 4]); ax.set_xticklabels(["Latence la\nplus faible", "Rapide", "Modérée", "Modérée"])
    ax.set_xlim(0.4, 4.6); ax.set_ylim(-3.2, 10); ax.set_yticks([0, 2, 4, 6, 8, 10]); ax.set_xlabel("Latence comparative (selon la documentation)")
    ax.set_ylabel("Prix API en entrée (USD par million de tokens)")
    ax.set_title("Gamme de modèles Claude actuelle — positionnement", fontsize=12)
    style_axes(ax)
    fig.text(0.5, -0.05, "Données : Anthropic, Models overview, tableau « Latest models » (consulté le 16/11/2026). Haiku : « à partir de » 0,10 USD. "
             "Prix et gamme susceptibles d'évoluer.", ha="center", fontsize=7.6, style="italic", color=MID)
    return save(fig, "fig04_2_gamme_modeles", "GRAPHIQUES")

def f05_1():
    fig, ax = canvas(10.5, 5.6, 105, 56)
    title(ax, "Anatomie d'une hallucination", y=53.5)
    box(ax, 3, 30, 45, 17, "Question : « Quel article du Code minier fixe\nle taux de redevance du cobalt ? Cite-le. »", fc=LIGHTTURQ, ec=TURQ, fs=9)
    box(ax, 57, 26, 45, 25, "", fc=LIGHTRED, ec=RED)
    ax.text(79.5, 47, "Réponse plausible… mais à vérifier", ha="center", fontsize=9.5, fontweight="bold", color=RED)
    ax.text(79.5, 37.5, "« L'article 241 bis, alinéa 3, fixe le taux\nà X %. Source : Journal officiel n° 14/2019. »\n\n"
            "→ numéro d'article précis, référence\nofficielle, ton assuré… mais rien ne\ngarantit que ces éléments existent.", ha="center", va="center", fontsize=8.3)
    arrow(ax, (48, 38.5), (57, 38.5), color=MID, lw=2)
    signes = ["Précision excessive (numéros, dates, pages)", "Références impossibles à retrouver", "Ton très assuré sans source fournie",
              "Chiffres « ronds » ou trop parfaits", "Contradiction avec vos propres documents"]
    box(ax, 3, 3, 99, 20, "", fc=GREY, ec=MID)
    ax.text(5, 19.5, "Signaux d'alerte", fontsize=9.5, fontweight="bold", color=NAVY)
    for i, s in enumerate(signes):
        ax.text(6 + (i % 2) * 48, 14.5 - (i // 2) * 4.6, "⚠  " + s, fontsize=8.5, color=INK)
    return save(fig, "fig05_1_hallucination")

def f05_2():
    fig, ax = plt.subplots(figsize=(8.6, 6.4))
    ax.axhline(0.5, color=MID, lw=1); ax.axvline(0.5, color=MID, lw=1)
    quads = [(0.25, 0.75, "Usage encouragé\navec relecture", "#CDEBD9", "brouillons, résumés, mise en forme,\nreformulation, plans de rapports"),
             (0.75, 0.75, "Usage encadré\nvérification systématique", LIGHTGOLD, "analyses de données, synthèses\nréglementaires, calculs, traductions\ntechniques"),
             (0.25, 0.25, "Usage libre\n(faible enjeu)", LIGHTTURQ, "idées, brainstorming,\nentraînement, apprentissage"),
             (0.75, 0.25, "Claude ne décide pas\nexpertise humaine requise", LIGHTRED, "plans de tir, stabilité des talus\net digues, urgences, sécurité des\npersonnes, avis juridiques engageants")]
    for x, y, t, c, ex in quads:
        ax.add_patch(Rectangle((x - 0.25, y - 0.25), 0.5, 0.5, fc=c, ec="white", lw=2))
        ax.text(x, y + 0.09, t, ha="center", va="center", fontsize=10, fontweight="bold", color=NAVY)
        ax.text(x, y - 0.1, ex, ha="center", va="center", fontsize=8, color=INK)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_xticks([0.25, 0.75]); ax.set_xticklabels(["Conséquences d'une erreur : faibles", "Conséquences d'une erreur : graves"])
    ax.set_yticks([0.25, 0.75]); ax.set_yticklabels(["Difficile à\nvérifier", "Facile à\nvérifier"])
    ax.set_title("Matrice de décision : quand et comment utiliser Claude ?", fontsize=12)
    for s in ax.spines.values(): s.set_visible(False)
    fig.text(0.5, 0.01, "Lecture : le quadrant inférieur droit est hors du champ de délégation à l'IA. Illustration réalisée pour cet ouvrage.",
             ha="center", fontsize=7.8, style="italic", color=MID)
    return save(fig, "fig05_2_matrice_risque_verif")

def f06_1():
    fig, ax = canvas(9, 7, 90, 70)
    title(ax, "La boucle « humain dans la boucle »", y=67.5)
    etapes = [("1. Cadrer", "l'expert définit la tâche,\nles données, les règles"), ("2. Produire", "Claude propose\nun brouillon ou une analyse"),
              ("3. Vérifier", "l'expert contrôle faits,\ncalculs, sources, cohérence"), ("4. Corriger", "itérations ciblées,\ncompléments"),
              ("5. Valider et signer", "l'expert assume\nle livrable final")]
    cx, cy, r = 45, 34, 23
    for i, (h, d) in enumerate(etapes):
        a = math.pi / 2 - i * 2 * math.pi / 5
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        c = GREEN if i in (0, 2, 4) else TURQ
        box(ax, x - 12, y - 6, 24, 12, "", fc="white", ec=c, lw=2, zorder=3)
        ax.text(x, y + 2.3, h, ha="center", fontsize=9.3, fontweight="bold", color=c, zorder=5)
        ax.text(x, y - 2.4, d, ha="center", va="center", fontsize=7.4, color=INK, zorder=5)
        a2 = math.pi / 2 - (i + 1) * 2 * math.pi / 5
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        ax.add_patch(FancyArrowPatch((x, y), (x2, y2), arrowstyle="-|>", mutation_scale=16, color=GOLD, lw=2,
                     connectionstyle="arc3,rad=-0.18", shrinkA=48, shrinkB=48, zorder=1))
    ax.text(45, 34, "Responsabilité\nhumaine", ha="center", va="center", fontsize=11, fontweight="bold", color=NAVY)
    ax.text(10, 2.5, "■ étapes humaines", color=GREEN, fontsize=8.5); ax.text(48, 2.5, "■ étapes assistées par Claude", color=TURQ, fontsize=8.5)
    return save(fig, "fig06_1_humain_boucle")

def f06_2():
    fig, ax = canvas(11, 5.4, 110, 54)
    title(ax, "Qui fait quoi ? Répartition des rôles entre Claude et l'expert", y=51.5, fs=12)
    cols = [("Claude excelle à…", TURQ, ["structurer et rédiger", "résumer de longs documents", "comparer des versions",
                                          "proposer des hypothèses", "transformer des formats", "expliquer et vulgariser"]),
            ("L'expert reste indispensable pour…", NAVY, ["connaître le terrain et le contexte", "juger la pertinence et le risque",
                                                          "vérifier les données sources", "arbitrer entre options", "signer, engager sa responsabilité",
                                                          "décider en situation critique"]),
            ("Ensemble, ils permettent…", GOLD, ["des livrables plus rapides", "une meilleure couverture des risques", "plus de temps pour l'analyse",
                                                 "une documentation plus complète", "une montée en compétences", "une traçabilité renforcée"])]
    for i, (h, c, items) in enumerate(cols):
        x = 2 + i * 36
        box(ax, x, 38, 34, 8, h, fc=c, ec=c, color="white", bold=True, fs=9.8)
        for j, it in enumerate(items):
            ax.text(x + 2, 33 - j * 5, "✓ " + it, fontsize=8.8, color=INK, va="center")
    return save(fig, "fig06_2_partage_roles")

def f07_1():
    fig, ax = canvas(11, 6.6, 110, 66)
    ax.add_patch(Rectangle((1, 1), 108, 62, fc="#FBFAF7", ec="#9AA5B1", lw=1.5))
    ax.add_patch(Rectangle((1, 1), 22, 62, fc="#F0EEE8", ec="#9AA5B1", lw=1))
    for i, t in enumerate(["+ Nouvelle conversation", "Recherche", "Conversations", "Projets", "Artefacts", "Personnalisation"]):
        ax.text(4, 57 - i * 5, t, fontsize=8.5, color=INK, fontweight="bold" if i == 0 else "normal")
    ax.text(4, 20, "Conversations récentes", fontsize=7.5, color=MID)
    for i in range(4): box(ax, 3.5, 15 - i * 3.6, 17, 2.6, "", fc="#E4E1D9", ec="none", rounding=0.6)
    ax.text(4, 3.5, "Profil • Paramètres", fontsize=7.5, color=MID)
    ax.text(66, 50, "Comment puis-je vous aider aujourd'hui ?", ha="center", fontsize=13, color=INK)
    box(ax, 32, 22, 68, 16, "", fc="white", ec="#B8C2CC", lw=1.4, rounding=2)
    ax.text(35, 33.5, "Écrivez votre message…", fontsize=9.5, color=MID)
    ax.text(35, 25, "+", fontsize=13, color=INK); ax.text(40, 25.3, "outils : fichiers, recherche, connecteurs", fontsize=7.5, color=MID)
    box(ax, 77, 23.6, 15, 4, "Modèle ▾", fc=GREY, ec="#B8C2CC", fs=8, rounding=1)
    ax.add_patch(Circle((96, 25.6), 2.2, fc=ORANGE, ec="none")); ax.text(96, 25.6, "↑", ha="center", va="center", color="white", fontweight="bold")
    callouts = [((14, 59), (14, 66), "A. Nouvelle conversation"), ((8, 42), (-1, 70), ""), ((50, 24.5), (58, 11), "C. Ajouter fichiers, outils,\nrecherche, connecteurs"),
                ((84, 23.6), (84, 12), "D. Sélecteur de modèle\net options de réflexion"), ((66, 34), (66, 44.5), "")]
    ax.annotate("B. Barre latérale :\nconversations, projets,\nartefacts", xy=(21, 40), xytext=(30, 8), fontsize=8, color=RED, fontweight="bold", ha="left", arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.2))
    for p, q, t in callouts:
        if t:
            ax.annotate(t, xy=p, xytext=q, fontsize=8, color=RED, fontweight="bold", ha="center",
                        arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.2))
    ax.text(55, -2.5, "ILLUSTRATION SCHÉMATIQUE — ce n'est pas une capture d'écran. La disposition réelle de l'interface évolue ;\n"
            "les libellés exacts peuvent différer selon la version, l'offre et la langue.", ha="center", fontsize=8, color=RED, style="italic")
    ax.set_ylim(-5, 66)
    return save(fig, "fig07_1_interface_schematique", "CAPTURES_CLAUDE")

def f08_1():
    fig, ax = canvas(11, 6.6, 110, 66)
    title(ax, "Arbre de décision : quel modèle pour quelle tâche ?", y=63.5)
    box(ax, 38, 50, 34, 8, "Quelle est votre tâche ?", fc=NAVY, ec=NAVY, color="white", bold=True, fs=10)
    q = [(4, 34, "Gros volume, tâche simple,\nrépétitive (tri, extraction,\nclassement de 500 fiches)"),
         (30, 34, "Travail courant : rédiger,\nrésumer, analyser un\ndocument, échanger vite"),
         (56, 34, "Analyse approfondie, dossier\ncomplexe, rapport important,\ndonnées croisées"),
         (82, 34, "Raisonnement très exigeant,\ntâche longue et autonome,\nproblème inédit")]
    r = [("Haiku 5.5", TURQ), ("Sonnet 5.5", NAVY), ("Opus 5.5", GOLD), ("Fable 5.2", RED)]
    eff = ["effort : low / medium", "effort : medium / high", "effort : medium → high", "effort : high (xhigh si mesuré)"]
    for (x, y, t), (m, c), e in zip(q, r, eff):
        box(ax, x, y, 24, 11, t, fc=GREY, ec=MID, fs=7.8)
        arrow(ax, (55, 50), (x + 12, y + 11), color=MID, lw=1.2)
        box(ax, x, 18, 24, 9, m, fc=c, ec=c, color="white", bold=True, fs=11)
        arrow(ax, (x + 12, y), (x + 12, 27), color=c, lw=1.6)
        ax.text(x + 12, 14.5, e, ha="center", fontsize=7.8, color=INK)
    box(ax, 4, 2, 102, 8, "En cas de doute : commencez par Opus 5.5 (recommandation de la documentation Anthropic),\npuis ajustez selon la qualité, la vitesse et le coût. Le choix dépend aussi de votre offre.", fc=LIGHTGOLD, ec=GOLD, fs=8)
    return save(fig, "fig08_1_arbre_choix_modele")

def f09_1():
    fig, ax = canvas(11, 4.4, 110, 44)
    title(ax, "Le paramètre d'effort : du plus économe au plus approfondi", y=41.5, fs=12)
    lv = [("low", "tâches simples,\nrapides, à fort volume"), ("medium", "équilibre vitesse,\ncoût, performance"),
          ("high", "raisonnement complexe,\nanalyses exigeantes"), ("xhigh", "travaux agentiques\nlongs (> 30 min)"), ("max", "capacité maximale,\nsans contrainte de coût")]
    cmap = ["#9ED9D3", "#5CBFB4", TURQ, "#0F7F78", NAVY]
    for i, ((n, d), c) in enumerate(zip(lv, cmap)):
        x = 3 + i * 21
        ax.add_patch(Polygon([(x, 18), (x + 19, 18), (x + 21, 25), (x + 19, 32), (x, 32), (x + 2, 25)], fc=c, ec="white"))
        ax.text(x + 10.5, 25, n, ha="center", va="center", fontsize=12, fontweight="bold", color="white")
        ax.text(x + 10.5, 11, d, ha="center", va="center", fontsize=8.2, color=INK)
    ax.text(3, 36, "◄ plus rapide, moins de tokens", fontsize=8.5, color=MID); ax.text(107, 36, "plus de réflexion, plus de tokens ►", fontsize=8.5, color=MID, ha="right")
    note(ax, "Valeur par défaut via l'API : medium sur Opus 5.5 et Haiku 5.5 ; high sur Fable 5.2 et Sonnet 5.5. Source : Anthropic, Effort (consulté le 16/11/2026).", y=2.5)
    return save(fig, "fig09_1_niveaux_effort")

def f09_2():
    fig, ax = canvas(11, 6, 110, 60)
    title(ax, "Anatomie d'une requête à l'API Messages", y=57.5)
    code = ('{\n  "model": "claude-opus-5-5",\n  "max_tokens": 4096,\n  "system": "Tu es analyste HSE chez MCC…",\n'
            '  "messages": [\n    {"role": "user", "content": "Analyse ce rapport…"}\n  ],\n  "output_config": {"effort": "medium"},\n'
            '  "thinking": {"type": "adaptive"},\n  "stop_sequences": ["###FIN"]\n}')
    box(ax, 3, 6, 50, 46, "", fc="#1B263B", ec="#1B263B", rounding=1.5)
    ax.text(6, 49, code, fontsize=8.6, color="#E8EEF5", family="monospace", va="top", linespacing=1.55)
    exp = [("model", "quel modèle répond"), ("max_tokens", "plafond de longueur de la sortie\n(réflexion comprise)"),
           ("system", "rôle, règles et contexte permanents"), ("messages", "la conversation (tours user / assistant)"),
           ("output_config.effort", "intensité de travail : low → max"), ("thinking", "mode de réflexion (adaptatif)"),
           ("stop_sequences", "chaînes qui arrêtent la génération")]
    for i, (k, v) in enumerate(exp):
        y = 48 - i * 6.3
        ax.text(58, y, k, fontsize=9, fontweight="bold", color=TURQ, family="monospace")
        ax.text(80, y, v, fontsize=8.2, color=INK, va="center" if "\n" in v else "baseline")
    note(ax, "Exemple simplifié. Paramètres d'après la référence de l'API Messages (Anthropic, consultée le 16/11/2026). Illustration réalisée pour cet ouvrage.", y=2)
    return save(fig, "fig09_2_requete_api")

def f10_1():
    fig, ax = canvas(11.5, 5.6, 115, 56)
    title(ax, "La méthode CADRE : cinq briques pour une instruction professionnelle", y=53.5, fs=12.5)
    L = [("C", "Contexte", "Qui êtes-vous ? Quelle\nentreprise, quel projet,\nquelle situation ?", NAVY),
         ("A", "Action", "Que doit faire Claude\nexactement ? Un verbe\nprécis, un objectif", TURQ),
         ("D", "Données", "Sur quoi travailler ?\nDocuments, chiffres,\nextraits, exemples", GOLD),
         ("R", "Règles", "Contraintes, normes,\ninterdits, sources\nautorisées, prudence", RED),
         ("E", "Exigences\nde sortie", "Format, longueur,\nstructure, ton,\ndestinataire", GREEN)]
    for i, (l, n, d, c) in enumerate(L):
        x = 3 + i * 22.5
        ax.add_patch(Circle((x + 10, 38), 7, fc=c, ec="white", lw=2))
        ax.text(x + 10, 38, l, ha="center", va="center", fontsize=24, fontweight="bold", color="white")
        ax.text(x + 10, 26.5, n, ha="center", va="center", fontsize=10.5, fontweight="bold", color=c)
        box(ax, x, 5, 20, 16, d, fc=GREY, ec=c, fs=8.3)
    note(ax, "Cadre pédagogique proposé par cet ouvrage — ce n'est pas une méthode officielle d'Anthropic.", y=1.5, fs=8)
    return save(fig, "fig10_1_methode_cadre")

def f10_2():
    fig, ax = canvas(11, 6.4, 110, 64)
    title(ax, "D'une demande vague à une instruction CADRE", y=61.5)
    box(ax, 2, 40, 38, 15, "« Fais-moi un rapport\nsur l'incident d'hier. »", fc=LIGHTRED, ec=RED, fs=10.5)
    ax.text(21, 36, "Résultat : générique, incomplet,\nfaits inventés pour combler les vides", ha="center", fontsize=8, color=RED, va="top")
    arrow(ax, (40, 47.5), (48, 47.5), color=GOLD, lw=3)
    parts = [("C", NAVY, "Je suis responsable HSE chez MCC (mine à ciel ouvert, Cu-Co, RDC)."),
             ("A", TURQ, "Rédige le rapport préliminaire d'incident à soumettre au directeur des opérations."),
             ("D", GOLD, "Données : déclaration du conducteur, rapport du superviseur, photos décrites ci-dessous."),
             ("R", RED, "N'invente aucun fait ; signale « [à confirmer] » toute information manquante ;\nne conclus pas sur les causes profondes avant l'enquête."),
             ("E", GREEN, "Format : modèle MCC (6 rubriques), 1 page, ton factuel, liste des actions immédiates.")]
    for i, (l, c, t) in enumerate(parts):
        y = 54 - i * 10.5
        ax.add_patch(Circle((52, y), 3.3, fc=c, ec="none")); ax.text(52, y, l, ha="center", va="center", color="white", fontweight="bold", fontsize=12)
        ax.text(57, y, t, va="center", fontsize=8.2, color=INK)
    box(ax, 2, 4, 38, 22, "Résultat : un brouillon structuré,\nfactuel, traçable, conforme au\nmodèle, avec ses lacunes\nexplicitement signalées", fc="#CDEBD9", ec=GREEN, fs=9)
    return save(fig, "fig10_2_avant_apres")

def f11_1():
    fig, ax = canvas(11.5, 4.6, 115, 46)
    title(ax, "Le chaînage de prompts : découper une tâche complexe", y=43.5, fs=12)
    s = [("Prompt 1\nExtraire", "faits et chiffres\ndu rapport (citations)"), ("Prompt 2\nVérifier", "contrôler cohérence\net unités"),
         ("Prompt 3\nAnalyser", "écarts, causes\npossibles, risques"), ("Prompt 4\nRédiger", "note de synthèse\nau format MCC"),
         ("Prompt 5\nCritiquer", "relire selon\nune check-list")]
    for i, (h, d) in enumerate(s):
        x = 3 + i * 22.5
        box(ax, x, 22, 19, 13, h, fc=NAVY if i % 2 == 0 else TURQ, ec="white", color="white", bold=True, fs=9.5)
        ax.text(x + 9.5, 15.5, d, ha="center", va="center", fontsize=8, color=INK)
        if i < 4: arrow(ax, (x + 19, 28.5), (x + 22.5, 28.5), color=GOLD, lw=2.2)
        ax.add_patch(Circle((x + 9.5, 7), 2, fc=GREEN, ec="none")); ax.text(x + 9.5, 7, "✓", ha="center", va="center", color="white", fontsize=9)
    ax.text(57, 2.5, "✓ = point de contrôle humain possible entre deux étapes", ha="center", fontsize=8.5, color=GREEN)
    return save(fig, "fig11_1_chainage")

def f11_2():
    fig, ax = canvas(10, 5.2, 100, 52)
    title(ax, "Montrer plutôt que décrire : l'apprentissage par exemples", y=49.5, fs=12)
    box(ax, 3, 28, 42, 14, "Exemple 1 (entrée → sortie attendue)\n« Fuite hydraulique camion C-07 »\n→ Catégorie : Environnement / Gravité : 2", fc=LIGHTNAVY, ec=NAVY, fs=8)
    box(ax, 3, 11, 42, 14, "Exemple 2\n« Chute de plain-pied atelier »\n→ Catégorie : Sécurité / Gravité : 1", fc=LIGHTNAVY, ec=NAVY, fs=8)
    box(ax, 55, 19, 42, 15, "Nouvelle entrée\n« Projection d'acide, cellule EW »\n→ Claude reproduit le format\net la logique de classement", fc=LIGHTTURQ, ec=TURQ, fs=8.3)
    arrow(ax, (45, 35), (55, 28), color=GOLD, lw=2); arrow(ax, (45, 18), (55, 24), color=GOLD, lw=2)
    note(ax, "2 à 5 exemples variés et représentatifs suffisent souvent. Illustration réalisée pour cet ouvrage.", y=3)
    return save(fig, "fig11_2_exemples")

def f12_1():
    fig, ax = plt.subplots(figsize=(9, 4.4))
    x = np.arange(1, 41)
    q = 0.95 - 0.35 / (1 + np.exp(-(x - 24) / 4))
    ax.plot(x, q, color=NAVY, lw=2.5, label="Conversation unique qui s'allonge")
    q2 = np.where(x < 20, q, 0.93 - 0.002 * (x - 20))
    ax.plot(x, q2, color=TURQ, lw=2.5, ls="--", label="Nouvelle conversation + résumé au tour 20")
    ax.axvline(20, color=GOLD, lw=1.2, ls=":"); ax.text(20.5, 0.63, "résumé\ntransféré", fontsize=8, color=GOLD)
    ax.set_ylim(0.5, 1); ax.set_xlabel("Nombre d'échanges dans la conversation"); ax.set_ylabel("Pertinence perçue (schématique)")
    ax.set_yticks([]); ax.legend(frameon=False, fontsize=8.5, loc="lower left")
    ax.set_title("Conversations longues : pourquoi repartir sur une base propre", fontsize=11.5)
    style_axes(ax, grid=False)
    fig.text(0.5, -0.04, "Courbes schématiques (non mesurées) illustrant un principe d'usage. Illustration réalisée pour cet ouvrage.",
             ha="center", fontsize=7.8, style="italic", color=MID)
    return save(fig, "fig12_1_contexte_conversation", "GRAPHIQUES")

def f13_1():
    fig, ax = canvas(11.5, 4.8, 115, 48)
    title(ax, "Circuit de travail sur un document", y=45.5, fs=12)
    s = [("Préparer", "vérifier la classification,\nretirer les données\nsensibles, nommer"), ("Joindre", "PDF, Word, Excel, CSV,\nimages (selon limites\nde l'offre)"),
         ("Interroger", "questions précises,\ndemande de citations\net de pages"), ("Extraire", "tableaux, chiffres,\nobligations, dates"),
         ("Vérifier", "retour au document\nsource, recalcul,\néchantillonnage"), ("Produire", "livrable final\nvalidé et archivé")]
    for i, (h, d) in enumerate(s):
        x = 2 + i * 19
        c = GREEN if i in (0, 4) else NAVY
        box(ax, x, 26, 16.5, 9, h, fc=c, ec=c, color="white", bold=True, fs=10)
        ax.text(x + 8.25, 16, d, ha="center", va="center", fontsize=7.8, color=INK)
        if i < 5: arrow(ax, (x + 16.5, 30.5), (x + 19, 30.5), color=GOLD, lw=2)
    note(ax, "Limites des fichiers : voir Anthropic, Upload files to Claude (consulté le 16/11/2026). Illustration réalisée pour cet ouvrage.", y=4)
    return save(fig, "fig13_1_circuit_documentaire")

def f14_1():
    fig, ax = canvas(10, 6.4, 100, 64)
    title(ax, "Hiérarchie de fiabilité des sources (à adapter au sujet)", y=61.5, fs=12)
    niveaux = [("Textes officiels, normes,\ndonnées primaires de l'entreprise", GREEN),
               ("Rapports institutionnels (OIT, OCDE, Banque\nmondiale, USGS, ICMM, ITIE…)", TURQ),
               ("Publications scientifiques évaluées par les pairs", NAVY),
               ("Presse spécialisée, cabinets, associations professionnelles", GOLD),
               ("Blogs, forums, réseaux sociaux, contenus non signés", ORANGE),
               ("Réponse de Claude sans source", RED)]
    n = len(niveaux)
    for i, (t, c) in enumerate(niveaux):
        y = 50 - i * 8.2; half = 12 + i * 6.5
        ax.add_patch(Polygon([(50 - half, y), (50 + half, y), (50 + half + 3.2, y - 7.2), (50 - half - 3.2, y - 7.2)], fc=c, ec="white", lw=1.5))
        ax.text(50, y - 3.6, t, ha="center", va="center", fontsize=8.1, color="white", fontweight="bold")
    ax.text(97, 50, "plus\nfiable", ha="right", fontsize=8, color=GREEN); ax.text(97, 5, "à vérifier\nsystémati-\nquement", ha="right", fontsize=8, color=RED)
    note(ax, "Une réponse de Claude n'est pas une source : c'est un point de départ à vérifier. Illustration réalisée pour cet ouvrage.", y=1.2)
    return save(fig, "fig14_1_pyramide_sources")

def f15_1():
    fig, ax = canvas(11, 6, 110, 60)
    title(ax, "Organiser son travail : conversations, projets et artefacts", y=57.5, fs=12)
    box(ax, 3, 6, 62, 46, "", fc=LIGHTNAVY, ec=NAVY, lw=2)
    ax.text(34, 48.5, "PROJET « Rapports mensuels HSE — MCC »", ha="center", fontsize=10, fontweight="bold", color=NAVY)
    box(ax, 6, 34, 27, 11, "Instructions du projet\n(rôle, format, règles)", fc="white", ec=NAVY, fs=8.3)
    box(ax, 36, 34, 26, 11, "Connaissances du projet\n(procédures, modèles,\nindicateurs 2025)", fc="white", ec=NAVY, fs=8.3)
    for i, t in enumerate(["Conversation : rapport de janvier", "Conversation : rapport de février", "Conversation : analyse trimestrielle"]):
        box(ax, 6, 25 - i * 6.5, 56, 5, t, fc=GREY, ec=MID, fs=8.3, rounding=0.8)
    box(ax, 74, 30, 33, 18, "ARTEFACT\ntableau de bord HSE,\ndocument, présentation\n(modifiable, partageable)", fc=LIGHTGOLD, ec=GOLD, fs=8.6, bold=True)
    box(ax, 74, 6, 33, 18, "Conversation hors projet\n(question ponctuelle,\nsans contexte permanent)", fc="white", ec=MID, fs=8.6)
    arrow(ax, (62, 22), (74, 36), color=GOLD, lw=2)
    ax.text(68, 31, "produit", fontsize=8, color=GOLD, rotation=45)
    note(ax, "D'après Anthropic, What are projects? et What are artifacts…? (consultés le 16/11/2026). Illustration réalisée pour cet ouvrage.", y=2)
    return save(fig, "fig15_1_projets_artefacts")

def f16_1():
    fig, ax = canvas(11.5, 5.8, 115, 58)
    title(ax, "Le Model Context Protocol (MCP) : une « prise universelle » pour connecter Claude", y=55.5, fs=12)
    box(ax, 3, 18, 26, 22, "Application hôte\n(Claude Desktop,\nClaude.ai, Claude Code)\n\ncontient des\nclients MCP", fc=NAVY, ec=NAVY, color="white", fs=8.8, bold=True)
    serv = [("Serveur MCP\n« documents »", "GED / SharePoint\n(procédures, rapports)"), ("Serveur MCP\n« base de données »", "historique production,\nmaintenance (lecture)"),
            ("Serveur MCP\n« messagerie / agenda »", "courriels, réunions"), ("Serveur MCP\n« outil métier »", "ERP, GMAO, LIMS…")]
    for i, (s, d) in enumerate(serv):
        y = 42 - i * 11
        box(ax, 46, y, 25, 9, s, fc=LIGHTTURQ, ec=TURQ, fs=8, bold=True)
        box(ax, 84, y, 28, 9, d, fc=GREY, ec=MID, fs=8)
        arrow(ax, (29, 29), (46, y + 4.5), color=GOLD, lw=1.5, style="<|-|>")
        arrow(ax, (71, y + 4.5), (84, y + 4.5), color=MID, lw=1.3, style="<|-|>")
    ax.text(37, 47, "protocole\nstandard", ha="center", fontsize=8, color=GOLD, fontweight="bold")
    note(ax, "« Considérez MCP comme un port USB-C pour les applications d'IA » (modelcontextprotocol.io, consulté le 16/11/2026, traduction). Illustration réalisée pour cet ouvrage.", y=2.5)
    return save(fig, "fig16_1_mcp")

def f16_2():
    fig, ax = canvas(11, 6, 110, 60)
    title(ax, "Quel outil de l'écosystème pour quel besoin ?", y=57.5, fs=12)
    rows = [("Connecteurs", "Donner à Claude l'accès à vos outils et données (Drive, messagerie, GED, ERP…)", TURQ),
            ("Skills", "Lui apprendre une procédure maison, réutilisable (modèle de rapport, méthode d'analyse)", GOLD),
            ("Projects", "Regrouper instructions et documents de référence d'un dossier récurrent", NAVY),
            ("Cowork", "Lui confier une tâche longue en plusieurs étapes sur des fichiers, avec suivi", PURPLE),
            ("Claude Code", "Automatiser, programmer, traiter des données par scripts (équipes techniques)", GREEN),
            ("API", "Intégrer Claude dans une application de l'entreprise (développeurs)", RED)]
    for i, (n, d, c) in enumerate(rows):
        y = 47 - i * 8
        box(ax, 3, y, 22, 6.4, n, fc=c, ec=c, color="white", bold=True, fs=9.5)
        box(ax, 27, y, 80, 6.4, d, fc=GREY, ec="#D5DBE3", fs=8.6, ha="left")
    note(ax, "Disponibilité selon l'offre et la configuration de l'organisation. Sources : Claude Help Center (consulté le 16/11/2026).", y=1.5)
    return save(fig, "fig16_2_carte_outils")

ALL = [f01_1, f01_2, f02_1, f02_2, f02_3, f03_1, f03_2, f03_3, f03_4, f04_1, f04_2, f05_1, f05_2, f06_1, f06_2,
       f07_1, f08_1, f09_1, f09_2, f10_1, f10_2, f11_1, f11_2, f12_1, f13_1, f14_1, f15_1, f16_1, f16_2]

if __name__ == "__main__":
    for f in ALL:
        print(f())

def f01_3():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.6), gridspec_kw=dict(width_ratios=[1.25, 1]))
    pays = ["Chili", "Congo (RDC)", "Pérou", "Chine", "Russie", "Zambie", "Autres"]
    val = [5.3, 3.2, 2.7, 1.8, 1.3, 0.94, 23 - (5.3 + 3.2 + 2.7 + 1.8 + 1.3 + 0.94)]
    cols = [NAVY, GOLD, NAVY, NAVY, NAVY, NAVY, "#B8C2CC"]
    a1.barh(pays[::-1], val[::-1], color=cols[::-1], height=0.62)
    for i, v in enumerate(val[::-1]): a1.text(v + 0.1, i, f"{v:.1f}".replace(".", ","), va="center", fontsize=8.5)
    a1.set_title("Production minière de cuivre, 2025 (estimation)\nen millions de tonnes de cuivre contenu", fontsize=10)
    a1.set_xlim(0, 8.5); style_axes(a1, grid=False); a1.tick_params(labelsize=8.5)
    a2.pie([230, 44, 310 - 274], labels=["Congo (RDC)\n230 000 t", "Indonésie\n44 000 t", "Autres pays\n36 000 t"],
           colors=[GOLD, NAVY, "#B8C2CC"], startangle=90, counterclock=False, wedgeprops=dict(width=0.42, edgecolor="white"),
           textprops=dict(fontsize=8.5))
    a2.text(0, 0, "≈ 73 %\nRDC", ha="center", va="center", fontsize=12, fontweight="bold", color=NAVY)
    a2.set_title("Production minière de cobalt, 2025 (estimation)\ntotal mondial ≈ 310 000 t", fontsize=10)
    fig.text(0.5, -0.03, "Source des données : U.S. Geological Survey (2026), Mineral Commodity Summaries 2026, fiches « Copper » et « Cobalt ». "
             "Graphique réalisé pour cet ouvrage.", ha="center", fontsize=7.8, style="italic", color=MID)
    fig.tight_layout()
    return save(fig, "fig01_3_rdc_cuivre_cobalt", "GRAPHIQUES")

ALL.append(f01_3)
