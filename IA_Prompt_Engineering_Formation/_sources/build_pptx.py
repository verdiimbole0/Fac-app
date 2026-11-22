# -*- coding: utf-8 -*-
"""Génère le PowerPoint de la formation avec notes du présentateur.
Usage : python3 build_pptx.py  ->  ../01_PowerPoint/IA_Prompt_Engineering_Formation.pptx + build/notes.json"""
import json, os
from pptlib import *

D = Deck()
NOTES = []   # (num, titre, chapitre, minutes, notes) pour le guide formateur
CUR_CH = ["Introduction"]

def N(s, title, minutes, intro, explain, example=None, question=None, points=None, transition=None):
    parts = [f"⏱ TEMPS RECOMMANDÉ : {fmt_min(minutes)}", "", f"INTRODUIRE : {intro}", "", f"EXPLIQUER : {explain}"]
    if example: parts += ["", f"EXEMPLE À RACONTER : {example}"]
    if question: parts += ["", f"QUESTION AU PUBLIC : {question}"]
    if points: parts += ["", "À NE PAS OUBLIER : " + " | ".join(points)]
    if transition: parts += ["", f"TRANSITION : {transition}"]
    D.set_notes(s, "\n".join(parts))
    NOTES.append(dict(num=D.count, title=title, chapter=CUR_CH[0], minutes=minutes, intro=intro, explain=explain,
                      example=example, question=question, points=points, transition=transition))

def fmt_min(m):
    mm = int(m); ss = int(round((m - mm) * 60))
    return f"{mm} min {ss:02d} s" if mm else f"{ss} s"

# =====================================================================================
# INTRODUCTION
# =====================================================================================
s = D.new(NAVY)
D.rect(s, 0, 0, 0.25, 7.5, fill=GOLD)
for i, (d, c) in enumerate([(7.6, NAVY2), (5.6, "17366A"), (3.6, "1D4278")]):
    D.circle(s, 9.6 - d / 2 + 1.5, 3.75 - d / 2, d, fill=c)
D.icon_badge(s, "sparkles", 10.35, 3.0, 1.5, bg=TEAL, ratio=0.5)
D.text(s, 0.95, 0.9, 6, 0.4, "FORMATION PROFESSIONNELLE  ·  60 MINUTES", size=12, color=GOLD, bold=True, font=TITLE_FONT)
D.text(s, 0.95, 1.6, 8.3, 2.6, [[("IA & Prompt Engineering", {})], [("appliqués aux entreprises", {"color": GOLD})]],
       size=44, color=WHITE, bold=True, font=TITLE_FONT, spacing=1.0, para_space=2)
D.rect(s, 0.95, 3.85, 1.4, 0.06, fill=GOLD)
D.text(s, 0.95, 4.15, 7.6, 1.0, SUBTITLE, size=17, color="C9D3E6", spacing=1.15)
for i, (ic, t) in enumerate([("brain", "Comprendre"), ("compass", "Formuler"), ("users", "Pratiquer"), ("shield-check", "Sécuriser")]):
    x = 0.95 + i * 1.9
    D.icon(s, ic, x, 5.55, 0.38, GOLD)
    D.text(s, x + 0.48, 5.58, 1.4, 0.35, t, size=12, color=WHITE, bold=True, font=TITLE_FONT)
D.text(s, 0.95, 6.75, 8, 0.35, "Support du formateur  ·  Syllabus et Kit IA remis aux participants", size=10.5, color="8EA0C2")
N(s, "Couverture", 0.5,
  "Accueillez les participants pendant que cette diapositive est projetée. Souriez, présentez-vous en une phrase (nom, rôle, pourquoi l'IA vous passionne).",
  "Annoncez la promesse : « En une heure, vous allez passer de la curiosité à une vraie capacité d'utilisation. Pas de jargon, pas de code : des méthodes et des exemples tirés de votre quotidien. »",
  points=["Vérifiez avant de commencer : vidéoprojecteur, son, connexion Internet et assistant IA ouvert dans un onglet (pour la démo du chapitre 4)", "Le kit et le syllabus seront remis à la fin : inutile de tout noter"],
  transition="« Commençons par une petite question… »")

# ---------- accroche
s = D.new(WHITE); D.header(s, "Pour commencer", "Combien de temps avez-vous passé cette semaine à…")
items = [("mail", "Rédiger et relire des emails"), ("search", "Chercher une information"), ("file-text", "Lire, résumer des documents"), ("presentation", "Préparer réunions et rapports")]
for i, (ic, t) in enumerate(items):
    x = 0.6 + i * 3.1
    D.rrect(s, x, 2.0, 2.85, 2.6, fill=LIGHT)
    D.icon_badge(s, ic, x + 0.95, 2.35, 0.95, bg=NAVY)
    D.text(s, x + 0.2, 3.5, 2.45, 0.9, t, size=16, color=NAVY, bold=True, font=TITLE_FONT, align="c", anchor="t")
D.rrect(s, 0.6, 5.0, 12.13, 1.55, fill=NAVY)
D.icon(s, "hourglass", 1.0, 5.4, 0.75, GOLD)
D.text(s, 2.05, 5.2, 10.4, 1.2, [[("Et si une partie de ce temps vous était rendue ?", {"bold": True, "size": 22, "font": TITLE_FONT, "color": WHITE})],
                                  [("Pas en travaillant plus vite… mais en travaillant autrement, avec un assistant que vous savez piloter.", {"color": "C9D3E6", "size": 15})]], anchor="m")
D.footer(s)
N(s, "Accroche", 1.5,
  "Posez la question à voix haute et demandez à main levée : « Qui a passé plus d'une heure cette semaine à écrire des emails ? Plus de deux heures ? »",
  "Faites réagir 1 ou 2 personnes. L'objectif est de partir de LEUR réalité, pas de la technologie. Puis lisez la phrase du bas.",
  example="« La semaine dernière, une assistante de direction m'a dit passer près d'une journée par semaine à rédiger des comptes rendus. C'est exactement le type de tâche que nous allons transformer aujourd'hui. »",
  question="Combien de temps avez-vous passé cette semaine à rédiger des emails ?",
  points=["Ne promettez pas de gain chiffré universel : parlez de « temps rendu » pour des tâches précises"],
  transition="« Voici précisément ce que vous saurez faire dans une heure. »")

# ---------- objectifs
s = D.new(WHITE); D.header(s, "Objectifs de la formation", "Dans une heure, vous saurez…")
objs = ["Expliquer simplement ce qu'est l'IA générative et pourquoi elle peut se tromper",
        "Repérer dans votre métier les tâches où l'IA vous fait gagner du temps",
        "Rédiger des prompts efficaces avec la méthode PILOTE",
        "Mener une vraie conversation de travail avec l'IA, jusqu'à un résultat utilisable",
        "Protéger les données et vérifier une réponse avant de l'utiliser"]
for i, o in enumerate(objs):
    y = 1.95 + i * 0.88
    D.circle(s, 0.65, y, 0.6, fill=NAVY if i != 2 else TEAL, text=str(i + 1), size=18)
    D.text(s, 1.45, y + 0.02, 6.6, 0.6, o, size=16, color=INK, anchor="m")
D.rrect(s, 8.55, 1.95, 4.18, 4.45, fill=LIGHT)
D.text(s, 8.85, 2.15, 3.7, 0.4, "VOUS REPARTEZ AVEC", size=12, color=GOLD, bold=True, font=TITLE_FONT)
for i, (ic, t, d) in enumerate([("book-open", "Le syllabus complet", "Cours détaillé, quiz, glossaire"),
                                ("briefcase", "Le Kit IA du professionnel", "Outils, prompts prêts à l'emploi"),
                                ("flag", "Le défi IA de 7 jours", "Pour ancrer de nouvelles habitudes")]):
    y = 2.7 + i * 1.18
    D.icon_badge(s, ic, 8.85, y, 0.75, bg=TEAL)
    D.text(s, 9.8, y - 0.02, 2.85, 0.9, [[(t, {"bold": True, "color": NAVY, "font": TITLE_FONT, "size": 14})], [(d, {"size": 12, "color": MUTED})]], anchor="m")
D.footer(s)
N(s, "Objectifs", 1,
  "« Voici notre contrat pour l'heure qui vient. »",
  "Lisez rapidement les 5 objectifs (un par chapitre). Insistez sur le n°3, la méthode PILOTE, qui est le cœur de la formation. Montrez le cadre de droite : ils repartent avec trois ressources.",
  points=["Rassurez les débutants : aucun prérequis technique", "Dites aux utilisateurs avancés qu'ils repartiront avec une méthode et des réflexes qu'ils n'ont probablement pas encore systématisés"],
  transition="« Et voici comment nous allons organiser ces 60 minutes. »")

# ---------- programme
s = D.new(WHITE); D.header(s, "Programme", "60 minutes, 5 chapitres, 5 quiz")
x0, wtot = 0.6, 12.13
cols = [GOLD, NAVY, NAVY2, TEAL, NAVY, NAVY2, GOLD]
labels = ["Accueil", "1. Comprendre l'IA", "2. L'IA en entreprise", "3. La méthode PILOTE", "4. Atelier pratique", "5. Risques & réflexes", "Plan d'action"]
x = x0
for i, (t, m, d) in enumerate(TIMING):
    w = wtot * m / 60
    D.rect(s, x + 0.03, 2.3, w - 0.06, 0.75, fill=cols[i])
    D.text(s, x, 2.3, w, 0.75, f"{m} min", size=13 if w > 0.9 else 11, color=WHITE, bold=True, font=TITLE_FONT, align="c", anchor="m")
    D.text(s, x + 0.04, 3.2, w - 0.08, 0.8, labels[i], size=11.5 if w > 1.2 else 10, color=NAVY, bold=True, font=TITLE_FONT, align="c")
    x += w
for i, (ic, t, d) in enumerate([("brain", "Comprendre", "Démystifier sans jargon"), ("compass", "Méthode", "Formuler avec PILOTE"),
                                ("users", "Pratique", "Un cas réel, de A à Z"), ("circle-check", "Vérification", "Un quiz après chaque chapitre")]):
    x = 0.6 + i * 3.1
    D.rrect(s, x, 4.45, 2.85, 2.05, fill=LIGHT)
    D.icon(s, ic, x + 0.25, 4.7, 0.5, TEAL)
    D.text(s, x + 0.25, 5.3, 2.4, 1.1, [[(t, {"bold": True, "size": 15, "color": NAVY, "font": TITLE_FONT})], [(d, {"size": 12.5, "color": MUTED})]])
D.footer(s)
N(s, "Programme", 1,
  "« Le programme est rythmé : chaque chapitre se termine par un mini-quiz de trois questions. »",
  "Montrez la frise : le chapitre 3 (méthode) et le chapitre 4 (atelier) occupent près de la moitié du temps, car c'est là que se construit la compétence. Précisez que les quiz sont anonymes et ludiques : chacun répond mentalement ou sur papier.",
  points=["Annoncez que les questions de fond pourront être posées à la fin (ou notées sur un « parking » pour tenir le temps)"],
  transition="« Commençons par le commencement : qu'est-ce que l'IA, vraiment ? »")

# =====================================================================================
def chapter_cover(ch, minutes):
    CUR_CH[0] = f"Chapitre {ch['n']}"
    s = D.new(NAVY)
    D.rect(s, 0, 0, 13.333, 0.12, fill=GOLD)
    D.circle(s, 8.9, 1.25, 5.0, fill=NAVY2)
    D.icon_badge(s, ch["icon"], 10.15, 2.5, 2.5, bg=TEAL, ratio=0.5)
    D.text(s, 0.9, 0.8, 4, 1.9, f"0{ch['n']}", size=110, color=GOLD, bold=True, font=TITLE_FONT, spacing=0.9)
    D.text(s, 0.95, 2.75, 7, 0.4, f"CHAPITRE {ch['n']}", size=13, color=GOLD, bold=True, font=TITLE_FONT)
    D.text(s, 0.95, 3.15, 7.6, 1.6, ch["title"], size=32, color=WHITE, bold=True, font=TITLE_FONT, spacing=1.0)
    D.rect(s, 0.95, 4.85, 1.2, 0.05, fill=GOLD)
    D.text(s, 0.95, 5.05, 7.3, 1.1, ch["objective"], size=15, color="C9D3E6", spacing=1.15)
    D.icon(s, "clock", 0.95, 6.45, 0.32, GOLD)
    D.text(s, 1.38, 6.43, 4, 0.4, f"{minutes} minutes, quiz inclus", size=12.5, color=GOLD, bold=True, font=TITLE_FONT)
    return s

def thanks_slide(n, title_next):
    q = QUIZZES[n]
    s = D.new(NAVY)
    D.rect(s, 0, 7.38, 13.333, 0.12, fill=GOLD)
    D.icon_badge(s, "heart", 5.97, 1.1, 1.4, bg=GOLD, color=NAVY, ratio=0.5)
    D.text(s, 1.0, 2.75, 11.33, 1.0, q["thanks_title"], size=32, color=WHITE, bold=True, font=TITLE_FONT, align="c")
    D.text(s, 2.2, 4.0, 8.93, 1.4, q["thanks"], size=18, color="C9D3E6", align="c", spacing=1.2)
    D.rrect(s, 4.67, 5.65, 4.0, 0.7, fill=TEAL, radius=0.5)
    D.text(s, 4.67, 5.65, 4.0, 0.7, f"Quiz du chapitre {n} : 3 questions", size=14, color=WHITE, bold=True, font=TITLE_FONT, align="c", anchor="m")
    N(s, f"Remerciement chapitre {n}", 0.25,
      "Lisez le message avec chaleur, en regardant le public (pas l'écran).",
      "Ce moment marque une respiration : il clôt le chapitre et prépare le quiz. Demandez à chacun de prendre une feuille ou de compter sur ses doigts A, B, C, D.",
      transition="« Trois questions, une seule bonne réponse à chaque fois. C'est parti ! »")

def quiz_slide(n):
    q = QUIZZES[n]
    s = D.new(LIGHT)
    D.header(s, f"Quiz · Chapitre {n}", "À vous de jouer : une seule bonne réponse par question")
    for i, item in enumerate(q["questions"]):
        x = 0.6 + i * 4.1
        D.rrect(s, x, 1.95, 3.88, 4.85, fill=WHITE, line="DCE2EB", radius=0.04)
        D.circle(s, x + 0.25, 2.15, 0.62, fill=NAVY, text=f"Q{i+1}", size=15)
        D.text(s, x + 1.0, 2.1, 2.75, 1.25, item["q"], size=13, color=NAVY, bold=True, font=TITLE_FONT, anchor="m", spacing=1.0)
        for j, opt in enumerate(item["options"]):
            y = 3.5 + j * 0.8
            D.circle(s, x + 0.25, y + 0.08, 0.42, fill=WHITE, line=NAVY, text="ABCD"[j], color=NAVY, size=12)
            D.text(s, x + 0.82, y, 2.95, 0.72, opt, size=11.5, color=INK, anchor="m", spacing=1.0)
    D.footer(s)
    N(s, f"Quiz chapitre {n}", 1,
      "Laissez environ 45 secondes de réflexion silencieuse. Lisez les questions à voix haute si le public est nombreux ou si la salle est grande.",
      "Puis faites voter rapidement à main levée pour la question 1 (« Qui a répondu A ? B ? ») : cela crée de l'énergie. Ne donnez pas encore les réponses.",
      points=["Bonnes réponses (ne pas lire) : " + ", ".join(f"Q{k+1} = {'ABCD'[it['answer']]}" for k, it in enumerate(q["questions"]))],
      transition="« Voyons les réponses… et surtout pourquoi. »")

def answer_slide(n, transition):
    q = QUIZZES[n]
    s = D.new(WHITE)
    D.rect(s, 0, 0, 13.333, 1.55, fill=TEAL)
    D.icon(s, "circle-check", 0.6, 0.5, 0.6, WHITE)
    D.text(s, 1.4, 0.35, 11, 0.4, f"CORRIGÉ · CHAPITRE {n}", size=12, color="D7F2EE", bold=True, font=TITLE_FONT)
    D.text(s, 1.4, 0.68, 11.5, 0.6, "Les bonnes réponses, et pourquoi", size=26, color=WHITE, bold=True, font=TITLE_FONT)
    for i, item in enumerate(q["questions"]):
        x = 0.6 + i * 4.1
        D.rrect(s, x, 1.9, 3.88, 4.95, fill=LIGHT, radius=0.04)
        D.text(s, x + 0.25, 2.05, 3.4, 0.35, f"QUESTION {i+1}", size=11, color=MUTED, bold=True, font=TITLE_FONT)
        L = "ABCD"[item["answer"]]
        D.rrect(s, x + 0.2, 2.45, 3.48, 1.25, fill=TEAL, radius=0.1)
        D.circle(s, x + 0.35, 2.78, 0.6, fill=WHITE, text=L, color=TEAL, size=20)
        D.text(s, x + 1.08, 2.5, 2.5, 1.15, item["options"][item["answer"]], size=11.5, color=WHITE, bold=True, anchor="m", spacing=1.0)
        D.text(s, x + 0.25, 3.85, 3.4, 1.95, item["why"], size=11.5, color=INK, spacing=1.08)
        D.rect(s, x + 0.25, 5.85, 3.4, 0.85, fill="FBF5E6")
        D.rect(s, x + 0.25, 5.85, 0.06, 0.85, fill=GOLD)
        D.icon(s, "lightbulb", x + 0.42, 6.05, 0.4, GOLD)
        D.text(s, x + 0.92, 5.88, 2.68, 0.8, item["tip"], size=11, color=NAVY, bold=True, anchor="m", spacing=1.0)
    D.footer(s)
    N(s, f"Corrigé chapitre {n}", 1,
      "Révélez les réponses une par une en commentant l'explication, pas seulement la lettre.",
      "Pour chaque question : donnez la bonne réponse, expliquez en une phrase pourquoi, puis lisez l'astuce mémo en jaune. Si beaucoup se sont trompés sur une question, reprenez l'idée clé en 20 secondes.",
      points=["Valorisez les bonnes réponses et dédramatisez les erreurs : « c'est précisément pour cela que l'on fait le quiz »"],
      transition=transition)

# =====================================================================================
# CHAPITRE 1
# =====================================================================================
ch = CHAPTERS[0]
s = chapter_cover(ch, 9)
N(s, "Chapitre 1 — couverture", 0.25, "« Premier chapitre : comprendre l'IA sans être technicien. »",
  "Annoncez l'objectif du chapitre en une phrase. Rassurez : aucune formule, aucune ligne de code.",
  transition="« Commençons par mettre de l'ordre dans les mots. »")

s = D.new(WHITE); D.header(s, "Chapitre 1 · Les mots justes", "IA, IA générative, modèle de langage : de quoi parle-t-on ?")
# cercles imbriqués
cx, base = 3.55, 6.75
for d, c, lab, tc in [(5.0, LIGHT, "Intelligence artificielle", NAVY), (3.85, "DCE4F0", "Apprentissage automatique", NAVY),
                      (2.7, NAVY, "IA générative", WHITE), (1.55, TEAL, "Modèles de\nlangage", WHITE)]:
    D.circle(s, cx - d / 2, base - d, d, fill=c)
    D.text(s, cx - d / 2 + 0.1, base - d + (0.32 if d > 2 else 0.33), d - 0.2, 0.75, lab, size=12 if d > 2 else 11, color=tc, bold=True, font=TITLE_FONT, align="c", spacing=0.95)
cards = [("IA « classique »", "Elle reconnaît, classe, prédit.", "Filtre anti-spam, GPS qui évite les bouchons, recommandations de films.", NAVY, "cpu"),
         ("IA générative", "Elle produit un contenu nouveau.", "Rédiger un email, résumer un rapport, créer une image, traduire.", TEAL, "sparkles"),
         ("Modèle de langage", "Le « moteur » des assistants textuels.", "ChatGPT, Claude, Gemini, Copilot, Mistral… reposent sur ce type de modèle.", GOLD, "message-square")]
for i, (t, d1, ex, c, ic) in enumerate(cards):
    y = 1.85 + i * 1.6
    D.rrect(s, 6.6, y, 6.13, 1.42, fill=LIGHT)
    D.rect(s, 6.6, y, 0.08, 1.42, fill=c)
    D.icon(s, ic, 6.9, y + 0.25, 0.5, c)
    D.text(s, 7.6, y + 0.12, 5.0, 1.2, [[(t, {"bold": True, "font": TITLE_FONT, "size": 15, "color": NAVY}), ("  " + d1, {"size": 13, "color": INK, "bold": True})],
                                     [(ex, {"size": 12.5, "color": MUTED})]], anchor="m")
D.footer(s)
N(s, "Les mots justes", 1.25,
  "« On entend tous ces mots dans les médias. Mettons-les en ordre en 60 secondes. »",
  "Montrez les cercles : l'IA est la grande famille ; l'apprentissage automatique en est une partie (la machine apprend à partir d'exemples) ; l'IA générative est la branche qui PRODUIT du contenu ; les modèles de langage sont les moteurs des assistants comme ChatGPT, Claude, Gemini ou Copilot.",
  example="« Vous utilisez l'IA depuis des années sans le savoir : votre boîte mail trie les spams, votre GPS prédit les bouchons. La nouveauté depuis 2022, c'est une IA qui écrit, résume et dialogue. »",
  question="« Qui a déjà utilisé ChatGPT, Gemini, Claude ou Copilot au moins une fois ? »",
  transition="« Mais comment une machine peut-elle écrire un email ? La réponse est étonnamment simple. »")

s = D.new(WHITE); D.header(s, "Chapitre 1 · Comment ça marche ?", "Une autocomplétion… géante")
D.rrect(s, 0.6, 1.9, 6.1, 4.85, fill=LIGHT)
D.text(s, 0.9, 2.05, 5.6, 0.35, "LE MODÈLE CHOISIT LE MOT SUIVANT LE PLUS PROBABLE", size=11, color=GOLD, bold=True, font=TITLE_FONT)
D.rrect(s, 0.9, 2.5, 5.5, 0.8, fill=WHITE, line="D5DBE5")
D.text(s, 1.1, 2.5, 5.2, 0.8, [[("« Je vous remercie pour votre … »", {"size": 17, "bold": True, "color": NAVY})]], anchor="m")
for i, (w, p) in enumerate([("confiance", 42), ("message", 31), ("patience", 18), ("commande", 9)]):
    y = 3.6 + i * 0.62
    D.text(s, 0.95, y, 1.55, 0.45, w, size=14, color=INK, bold=(i == 0), anchor="m")
    D.rect(s, 2.55, y + 0.08, 3.6 * p / 42, 0.32, fill=TEAL if i == 0 else "AFC2DD")
    D.text(s, 2.6 + 3.6 * p / 42, y, 0.8, 0.45, f"{p} %", size=12, color=MUTED, bold=True, anchor="m")
D.text(s, 0.95, 6.15, 5.6, 0.5, "Probabilités illustratives. Le modèle répète l'opération mot après mot.", size=10.5, color=MUTED, italic=True)
steps = [("library", "1. Il a été entraîné", "sur d'immenses volumes de textes, pour apprendre comment les mots s'enchaînent."),
         ("sparkles", "2. Il prédit", "mot après mot la suite la plus probable de votre texte."),
         ("message-circle", "3. Votre prompt est le début du texte", "plus il est précis, plus la suite est pertinente.")]
for i, (ic, t, d) in enumerate(steps):
    y = 1.9 + i * 1.25
    D.icon_badge(s, ic, 7.15, y + 0.1, 0.8, bg=NAVY)
    D.text(s, 8.15, y, 4.6, 1.1, [[(t, {"bold": True, "font": TITLE_FONT, "size": 15, "color": NAVY})], [(d, {"size": 13, "color": INK})]], anchor="m")
D.rrect(s, 7.15, 5.75, 5.58, 1.0, fill=NAVY)
D.text(s, 7.4, 5.75, 5.2, 1.0, "Elle ne cherche pas la réponse dans une base : elle la compose.", size=15, color=WHITE, bold=True, font=TITLE_FONT, anchor="m")
D.footer(s)
N(s, "Comment ça marche", 1.5,
  "« Vous connaissez tous la saisie prédictive de votre téléphone, qui propose le mot suivant. »",
  "Un modèle de langage fonctionne sur un principe comparable, à une échelle gigantesque. Il a été entraîné sur d'immenses quantités de textes et a appris quelles suites de mots sont probables. Quand vous écrivez une demande, il compose la réponse mot après mot. C'est pour cela qu'il rédige si bien… et c'est aussi pour cela qu'il peut se tromper : il vise le plausible.",
  example="Lisez la phrase « Je vous remercie pour votre… » et demandez au public de compléter. Ils répondront « confiance » ou « message » : vous venez de faire exactement ce que fait le modèle !",
  question="« Comment compléteriez-vous cette phrase ? »",
  points=["Précisez que c'est une simplification honnête : les modèles actuels sont très sophistiqués, mais le principe de prédiction reste au cœur", "Ne dites pas que l'IA « pense » ou « comprend » comme un humain"],
  transition="« Pour retenir tout cela, j'utilise une image très simple. »")

s = D.new(WHITE); D.header(s, "Chapitre 1 · L'analogie à retenir", "L'IA, c'est votre nouveau stagiaire surdoué")
D.rrect(s, 0.6, 1.9, 4.0, 4.85, fill=NAVY)
D.icon_badge(s, "graduation-cap", 1.85, 2.3, 1.5, bg=TEAL, ratio=0.5)
D.text(s, 0.85, 4.0, 3.5, 2.5, [[("Brillant, rapide, infatigable…", {"bold": True, "size": 17, "color": WHITE, "font": TITLE_FONT})],
                                [("… mais il est arrivé ce matin et ne connaît rien de votre entreprise.", {"size": 14, "color": "C9D3E6"})]], align="c")
traits = [("book-open", "Il a « tout lu »", "Une bibliothèque immense : il rédige, résume et explique sur presque tous les sujets.", TEAL),
          ("languages", "Il écrit vite, dans toutes les langues", "Un brouillon en quelques secondes, dans le ton demandé.", TEAL),
          ("building-2", "Il ne connaît pas votre contexte", "Vos clients, vos règles, vos chiffres : il faut les lui donner.", GOLD),
          ("circle-help", "Il n'aime pas dire « je ne sais pas »", "Il peut combler les vides avec une réponse plausible… mais fausse.", RED)]
for i, (ic, t, d, c) in enumerate(traits):
    x = 4.9 + (i % 2) * 3.95; y = 1.9 + (i // 2) * 1.95
    D.rrect(s, x, y, 3.8, 1.8, fill=LIGHT)
    D.icon(s, ic, x + 0.25, y + 0.25, 0.5, c)
    D.text(s, x + 0.25, y + 0.8, 3.4, 1.0, [[(t, {"bold": True, "size": 13.5, "color": NAVY, "font": TITLE_FONT})], [(d, {"size": 11.5, "color": INK})]], spacing=1.02)
D.rrect(s, 4.9, 5.9, 7.83, 0.85, fill="FBF5E6")
D.text(s, 5.15, 5.9, 7.4, 0.85, [[("Conséquence : ", {"bold": True, "color": GOLD}), ("briefez-le comme un nouveau collaborateur… et relisez toujours son travail.", {"bold": True, "color": NAVY})]], size=15, anchor="m")
D.footer(s)
N(s, "L'analogie du stagiaire", 1.25,
  "« Si vous ne deviez retenir qu'une image de ce chapitre, ce serait celle-ci. »",
  "Le stagiaire surdoué a deux qualités et deux défauts. Qualités : il a une culture immense et il écrit vite. Défauts : il ne connaît pas votre contexte et il préfère proposer une réponse plutôt que d'avouer qu'il ne sait pas. Tout le reste de la formation découle de cette image : on le briefe bien (chapitre 3), on travaille avec lui (chapitre 4), on vérifie (chapitre 5).",
  example="« Vous ne diriez jamais à un stagiaire arrivé le matin même : “Fais-moi le rapport.” Vous lui expliqueriez quel rapport, pour qui, avec quelles données. C'est exactement pareil avec l'IA. »",
  question="« Que diriez-vous à un stagiaire pour qu'il vous rende un bon compte rendu ? »",
  transition="« Mais au fait, pourquoi ne pas simplement utiliser Google ? »")

s = D.new(WHITE); D.header(s, "Chapitre 1 · Bien choisir son outil", "Moteur de recherche ou assistant IA ?")
rows = [("Ce qu'il fait", "Trouve des pages qui existent déjà", "Compose une réponse nouvelle"),
        ("Ce que vous obtenez", "Une liste de liens à lire", "Un texte structuré, prêt à retravailler"),
        ("Point fort", "Sources identifiées, informations récentes", "Synthèse, rédaction, reformulation, dialogue"),
        ("Point de vigilance", "C'est vous qui lisez, triez et synthétisez", "Peut se tromper ; pas toujours à jour sans accès web"),
        ("Idéal pour", "Vérifier un fait, trouver un site officiel", "Rédiger, résumer, structurer, réfléchir")]
D.rect(s, 3.3, 1.85, 4.6, 0.7, fill=NAVY); D.rect(s, 8.08, 1.85, 4.65, 0.7, fill=TEAL)
D.icon(s, "search", 3.55, 2.0, 0.4, WHITE); D.text(s, 4.1, 1.85, 3.7, 0.7, "Moteur de recherche", size=15, color=WHITE, bold=True, font=TITLE_FONT, anchor="m")
D.icon(s, "sparkles", 8.33, 2.0, 0.4, WHITE); D.text(s, 8.88, 1.85, 3.7, 0.7, "Assistant IA", size=15, color=WHITE, bold=True, font=TITLE_FONT, anchor="m")
for i, (a, b, c) in enumerate(rows):
    y = 2.65 + i * 0.72
    fill = LIGHT if i % 2 == 0 else WHITE
    D.rect(s, 0.6, y, 12.13, 0.66, fill=fill)
    D.text(s, 0.8, y, 2.4, 0.66, a, size=13, color=NAVY, bold=True, font=TITLE_FONT, anchor="m")
    D.text(s, 3.5, y, 4.3, 0.66, b, size=12.5, color=INK, anchor="m")
    D.text(s, 8.28, y, 4.35, 0.66, c, size=12.5, color=INK, anchor="m")
D.rrect(s, 0.6, 6.35, 12.13, 0.5, fill="E6F4F2")
D.text(s, 0.85, 6.35, 11.7, 0.5, [[("Bon à savoir : ", {"bold": True, "color": TEAL}), ("de nombreux assistants combinent désormais les deux (recherche web + sources citées). Ouvrez toujours les sources.", {"color": NAVY})]], size=12.5, anchor="m")
D.footer(s)
N(s, "Moteur de recherche vs assistant", 1,
  "« Beaucoup de gens utilisent ChatGPT comme Google… et sont déçus. Voici pourquoi. »",
  "Un moteur de recherche TROUVE des documents existants ; un assistant IA COMPOSE une réponse. Les deux sont complémentaires. Pour un fait récent, un chiffre, un texte de loi : partez d'une source (ou d'un assistant qui cite ses sources, et ouvrez-les). Pour rédiger, synthétiser, structurer : l'assistant est imbattable.",
  example="« Pour connaître les horaires d'ouverture d'une administration, Google. Pour rédiger la lettre que vous allez lui envoyer, l'assistant IA. »",
  question="« Pour vérifier le montant actuel d'une aide publique, lequel utiliseriez-vous ? »",
  transition="« Résumons ce que l'IA sait faire… et ce qu'elle ne sait pas faire. »")

s = D.new(WHITE); D.header(s, "Chapitre 1 · Forces et limites", "Ce qu'elle fait très bien… et ce qu'elle ne fait pas")
can = ["Rédiger et reformuler", "Résumer de longs textes", "Traduire et adapter le ton", "Structurer des idées, des plans", "Générer des idées en quantité", "Expliquer simplement un sujet complexe", "Analyser un texte ou un tableau fourni"]
cant = ["Garantir l'exactitude de ses réponses", "Connaître vos données internes si vous ne les fournissez pas", "Être à jour sans accès à des sources récentes", "Remplacer votre jugement et votre responsabilité", "Comprendre le monde comme un être humain"]
for col, (lst, c, ic, t) in enumerate([(can, TEAL, "circle-check", "ELLE SAIT FAIRE"), (cant, RED, "circle-x", "ELLE NE SAIT PAS FAIRE")]):
    x = 0.6 + col * 6.2
    D.rrect(s, x, 1.85, 5.93, 4.05, fill=LIGHT)
    D.rect(s, x, 1.85, 5.93, 0.08, fill=c)
    D.text(s, x + 0.3, 2.05, 5, 0.4, t, size=13, color=c, bold=True, font=TITLE_FONT)
    for i, it in enumerate(lst):
        y = 2.55 + i * 0.47
        D.icon(s, ic, x + 0.3, y + 0.06, 0.3, c)
        D.text(s, x + 0.75, y, 5.0, 0.44, it, size=13.5, color=INK, anchor="m")
D.rrect(s, 0.6, 6.05, 12.13, 0.8, fill=NAVY)
D.icon(s, "triangle-alert", 0.9, 6.22, 0.45, GOLD)
D.text(s, 1.55, 6.05, 11, 0.8, [[("Pourquoi se trompe-t-elle ? ", {"bold": True, "color": GOLD}), ("Parce qu'elle vise une réponse plausible, pas une réponse vérifiée.", {"color": WHITE, "bold": True})]], size=15, anchor="m")
D.footer(s)
N(s, "Forces et limites", 1.5,
  "« Pour bien utiliser un outil, il faut connaître son mode d'emploi… et ses limites. »",
  "Colonne de gauche : tout ce qui touche au langage (rédiger, résumer, reformuler, structurer). Colonne de droite : tout ce qui touche à la vérité, à l'actualité, à vos données internes et à la responsabilité. La phrase du bas fait le lien avec la mécanique vue précédemment : elle prédit du plausible.",
  example="« Demandez-lui une biographie d'une personne peu connue : elle peut inventer un diplôme ou une date avec un aplomb total. C'est ce qu'on appelle une hallucination ; nous y reviendrons au chapitre 5. »",
  points=["Les calculs : les assistants récents utilisent souvent des outils de calcul intégrés, mais il faut quand même vérifier les chiffres importants"],
  transition="« Bravo, vous en savez déjà plus que la majorité des utilisateurs. Un petit mot avant le quiz. »")

thanks_slide(1, "")
quiz_slide(1)
answer_slide(1, CHAPTERS[0]["transition"])

# =====================================================================================
# CHAPITRE 2
# =====================================================================================
ch = CHAPTERS[1]
s = chapter_cover(ch, 9)
N(s, "Chapitre 2 — couverture", 0.25, "« L'IA n'est pas réservée aux informaticiens. Voyons ce qu'elle change dans chaque métier. »",
  "Annoncez que le chapitre est concret : des cas par fonction et des situations Avant/Après.",
  transition="« Commençons par les grandes familles d'usages. »")

s = D.new(WHITE); D.header(s, "Chapitre 2 · Les usages", "Les 6 super-pouvoirs utiles au quotidien")
powers = [("pen-tool", "Rédiger", "Emails, courriers, posts, procédures"), ("file-text", "Résumer", "Rapports, réunions, longs documents"),
          ("languages", "Reformuler & traduire", "Adapter le ton, simplifier, traduire"), ("layers", "Structurer", "Plans, tableaux, check-lists, plannings"),
          ("chart-column", "Analyser", "Données fournies, écarts, comparaisons"), ("lightbulb", "Imaginer", "Idées, scénarios, objections, noms")]
for i, (ic, t, d) in enumerate(powers):
    x = 0.6 + (i % 3) * 4.1; y = 1.85 + (i // 3) * 2.05
    D.rrect(s, x, y, 3.88, 1.85, fill=LIGHT)
    D.icon_badge(s, ic, x + 0.3, y + 0.42, 1.0, bg=TEAL if i % 2 == 0 else NAVY)
    D.text(s, x + 1.5, y + 0.25, 2.3, 1.4, [[(t, {"bold": True, "size": 16, "font": TITLE_FONT, "color": NAVY})], [(d, {"size": 12.5, "color": MUTED})]], anchor="m")
D.rrect(s, 0.6, 6.0, 12.13, 0.85, fill="FBF5E6")
D.icon(s, "hand", 0.9, 6.15, 0.5, GOLD) if os.path.exists(os.path.join(ICON_DIR, "hand.svg")) else None
D.text(s, 1.6, 6.0, 11, 0.85, [[("Question : ", {"bold": True, "color": GOLD}), ("si vous pouviez déléguer UNE tâche répétitive dès demain, laquelle choisiriez-vous ?", {"bold": True, "color": NAVY})]], size=15, anchor="m")
D.footer(s)
N(s, "Les 6 super-pouvoirs", 1,
  "« Presque tout ce que l'IA fait en entreprise entre dans six familles. »",
  "Parcourez rapidement les six cartes, avec un exemple chacune. Puis posez la question du bas et recueillez 2 ou 3 réponses : notez-les mentalement, vous pourrez les reprendre dans l'atelier ou la conclusion.",
  question="Si vous pouviez déléguer une tâche répétitive dès demain, laquelle choisiriez-vous ?",
  transition="« Voyons maintenant, fonction par fonction, à quoi cela ressemble. »")

s = D.new(WHITE); D.header(s, "Chapitre 2 · Pour chaque métier", "Un exemple concret dans chaque fonction de l'entreprise")
for i, (f, ic, gen, ex) in enumerate(FUNCTIONS):
    x = 0.6 + (i % 5) * 2.45; y = 1.85 + (i // 5) * 2.5
    D.rrect(s, x, y, 2.3, 2.35, fill=LIGHT)
    D.icon(s, ic, x + 0.2, y + 0.2, 0.45, TEAL)
    D.text(s, x + 0.2, y + 0.72, 1.95, 0.55, f, size=12, color=NAVY, bold=True, font=TITLE_FONT, spacing=0.95)
    D.text(s, x + 0.2, y + 1.3, 1.95, 1.0, ex, size=10.5, color=INK, spacing=1.0)
D.footer(s)
N(s, "Exemples par fonction", 1.5,
  "« Cherchez votre métier dans ces dix cartes. »",
  "Ne lisez pas les dix cartes. Choisissez-en 3 en fonction du public présent (demandez qui est en RH, en finance, en vente…) et développez l'exemple. Le syllabus détaille chaque fonction avec le problème initial, l'intervention de l'IA et le résultat.",
  question="« Qui travaille en RH ? En comptabilité ? En vente ? » (adaptez vos exemples aux réponses)",
  points=["Message clé : il y a un usage pertinent dans TOUS les métiers"],
  transition="« Rendons cela encore plus concret avec trois situations Avant / Après. »")

for k, ba in enumerate(BEFORE_AFTER):
    s = D.new(WHITE); D.header(s, f"Chapitre 2 · Avant / Après  {k+1}/3", ba["title"])
    D.rrect(s, 0.6, 1.85, 5.6, 3.25, fill=LIGHT)
    D.text(s, 0.9, 2.0, 3, 0.4, "AVANT", size=14, color=RED, bold=True, font=TITLE_FONT)
    for i, b in enumerate(ba["before"]):
        D.icon(s, "circle-x", 0.9, 2.55 + i * 0.78 + 0.05, 0.32, RED)
        D.text(s, 1.35, 2.55 + i * 0.78, 4.7, 0.7, b, size=14, color=INK, anchor="m")
    D.arrow(s, 6.35, 3.15, 0.6, 0.6, fill=GOLD)
    D.rrect(s, 7.1, 1.85, 5.63, 3.25, fill="E6F4F2")
    D.text(s, 7.4, 2.0, 3, 0.4, "APRÈS, AVEC L'IA", size=14, color=TEAL, bold=True, font=TITLE_FONT)
    for i, a in enumerate(ba["after"]):
        D.icon(s, "circle-check", 7.4, 2.55 + i * 0.78 + 0.05, 0.32, TEAL)
        D.text(s, 7.85, 2.55 + i * 0.78, 4.75, 0.7, a, size=14, color=INK, anchor="m")
    D.rrect(s, 0.6, 5.3, 12.13, 1.2, fill=NAVY)
    D.text(s, 0.9, 5.38, 3, 0.35, "LE PROMPT UTILISÉ", size=10.5, color=GOLD, bold=True, font=TITLE_FONT)
    D.text(s, 0.9, 5.7, 11.6, 0.75, ba["prompt"], size=12.5, color=WHITE, spacing=1.05)
    D.text(s, 0.6, 6.58, 12, 0.35, "* Durées purement illustratives : le gain réel varie selon la personne, la tâche et la qualité des données fournies.", size=10, color=MUTED, italic=True)
    D.footer(s)
    tr = ["« Deuxième situation, côté vente. »", "« Dernière situation, côté finance. »", "« Ces trois exemples ont un point commun. Lequel ? »"][k]
    ex = ["« Imaginez Nadia, assistante de direction : chaque mois, elle compile le rapport d'activité. Avec l'IA, elle garde la main sur les chiffres et le fond, mais ne part plus d'une page blanche. »",
          "« Thomas, commercial, reçoit un email furieux. Plutôt que de répondre à chaud, il décrit la situation à l'IA, obtient un brouillon calme et structuré, puis décide lui-même du geste commercial. »",
          "« Léa, contrôleuse de gestion, doit expliquer un dépassement de budget. L'IA calcule les écarts et propose des pistes ; Léa valide les causes réelles, car elle seule les connaît. »"][k]
    N(s, f"Avant/Après {k+1}", 1,
      "Racontez la situation comme une petite histoire, avec un prénom.",
      "Lisez la colonne AVANT (le problème), puis la colonne APRÈS (ce que fait l'IA, ce que fait l'humain). Montrez le prompt en bas : il est disponible dans le kit. Soulignez la note sur les durées : ce sont des ordres de grandeur illustratifs, pas des promesses.",
      example=ex,
      question="« Qui a déjà vécu cette situation ? »" if k == 0 else None,
      points=["Dans chaque cas, l'humain vérifie et décide : c'est le message du slide suivant"],
      transition=tr)

s = D.new(WHITE); D.header(s, "Chapitre 2 · La règle d'or", "L'IA prépare, l'humain décide")
steps = [("target", "1. Vous cadrez", "Contexte, objectif, données utiles", NAVY, "VOUS"),
         ("sparkles", "2. L'IA produit", "Premier jet, options, structure", TEAL, "L'IA"),
         ("scan-search", "3. Vous vérifiez", "Faits, chiffres, pertinence, ton", NAVY, "VOUS"),
         ("badge-check", "4. Vous décidez", "Vous ajustez, validez et assumez", GOLD, "VOUS")]
for i, (ic, t, d, c, who) in enumerate(steps):
    x = 0.6 + i * 3.1
    D.rrect(s, x, 2.05, 2.75, 2.9, fill=c)
    D.icon(s, ic, x + 1.04, 2.35, 0.65, WHITE)
    D.text(s, x + 0.15, 3.15, 2.45, 1.6, [[(t, {"bold": True, "size": 15, "font": TITLE_FONT, "color": WHITE})], [(d, {"size": 12, "color": WHITE})]], align="c")
    if i < 3: D.arrow(s, x + 2.8, 3.3, 0.27, 0.4, fill=GOLD)
    D.rrect(s, x + 0.65, 5.15, 1.45, 0.48, fill=LIGHT, radius=0.5)
    D.text(s, x + 0.65, 5.15, 1.45, 0.48, who, size=12, color=c if c != GOLD else "9C7C2C", bold=True, font=TITLE_FONT, align="c", anchor="m")
D.rrect(s, 0.6, 5.95, 12.13, 0.9, fill=LIGHT)
D.text(s, 0.9, 5.95, 11.6, 0.9, [[("3 étapes sur 4 restent humaines. ", {"bold": True, "color": NAVY}), ("L'IA accélère la production ; votre valeur se déplace vers le cadrage, le contrôle et la décision.", {"color": INK})]], size=15, anchor="m")
D.footer(s)
N(s, "La règle d'or", 1,
  "« Les trois exemples avaient un point commun : regardez qui fait quoi. »",
  "Sur les quatre étapes, une seule est confiée à l'IA. Le cadrage, la vérification et la décision restent humains. C'est ce qui protège la qualité, et c'est ce qui valorise votre expertise : l'IA ne remplace pas votre connaissance du terrain, elle la rend plus productive.",
  points=["Les décisions concernant des personnes (recrutement, sanction, évaluation) ne doivent jamais être déléguées à une IA"],
  transition="« Avant de passer à la méthode, petite pause quiz. »")

thanks_slide(2, ""); quiz_slide(2); answer_slide(2, CHAPTERS[1]["transition"])

# =====================================================================================
# CHAPITRE 3
# =====================================================================================
ch = CHAPTERS[2]
s = chapter_cover(ch, 14)
N(s, "Chapitre 3 — couverture", 0.25, "« Voici le chapitre le plus important de la formation. »",
  "Annoncez : « Dans 14 minutes, vous saurez écrire des demandes que la plupart des utilisateurs n'écrivent jamais. »",
  transition="« Commençons par un petit vote. »")

s = D.new(WHITE); D.header(s, "Chapitre 3 · Le prompt", "Votez : lequel donnera le meilleur résultat ?")
D.text(s, 0.6, 1.8, 12.1, 0.55, [[("Un prompt ", {"bold": True, "color": TEAL}), ("est l'instruction que vous donnez à l'IA. La qualité de la réponse dépend directement de la qualité de la demande.", {"color": INK})]], size=15)
for i, (lab, txt, c) in enumerate([("A", "Fais-moi un résumé de ce rapport.", NAVY),
                                   ("B", "Résume ce rapport de 12 pages en 5 puces pour mon directeur, qui doit décider vendredi s'il valide le budget. Mets en avant les coûts et les risques.", TEAL)]):
    x = 0.6 + i * 6.2
    D.rrect(s, x, 2.6, 5.93, 3.0, fill=LIGHT)
    D.circle(s, x + 0.3, 2.85, 0.8, fill=c, text=lab, size=26)
    D.text(s, x + 0.3, 3.85, 5.3, 1.6, f"« {txt} »", size=15.5, color=NAVY, bold=True, spacing=1.1)
D.rrect(s, 0.6, 5.85, 12.13, 1.0, fill=NAVY)
D.text(s, 0.9, 5.85, 11.6, 1.0, [[("B gagne, toujours. ", {"bold": True, "color": GOLD}), ("Il dit à l'IA pour qui, pour quoi et sous quelle forme. C'est tout le secret du Prompt Engineering.", {"color": WHITE, "bold": True})]], size=15, anchor="m")
N(s, "Qu'est-ce qu'un prompt + vote", 1.5,
  "Masquez le bandeau du bas si possible (ou ne le commentez pas tout de suite). Faites voter à main levée : A ou B ?",
  "Tout le monde votera B. Demandez alors : « Pourquoi ? Qu'a B de plus que A ? » Faites lister par le public : le destinataire (directeur), l'objectif (décider du budget), le format (5 puces), les priorités (coûts et risques). Vous venez de faire découvrir la méthode par le public lui-même.",
  question="À votre avis, lequel de ces deux prompts donnera le meilleur résultat ? Pourquoi ?",
  points=["Insistez : « Prompt Engineering » fait peur, mais ce n'est rien d'autre que l'art de bien formuler une demande"],
  transition="« Si tout le monde sait que B est meilleur… pourquoi écrit-on presque toujours A ? Voyons les 4 erreurs classiques. »")
D.footer(s)

s = D.new(WHITE); D.header(s, "Chapitre 3 · Les pièges", "Les 4 erreurs les plus fréquentes")
errs = [("Trop vague", "« Parle-moi du marketing. »", "De quel marketing ? Pour quelle entreprise ? Avec quel but ?", "Précisez le sujet exact."),
        ("Sans contexte", "« Écris une offre commerciale. »", "Pour quel client, quel produit, quel prix, quelle situation ?", "Donnez les informations utiles."),
        ("Sans objectif", "« Résume ce texte. »", "Pour décider ? Pour informer ? Pour présenter ?", "Dites pourquoi vous le demandez."),
        ("Sans format", "« Donne-moi des idées. »", "Combien ? Sous quelle forme ? Quelle longueur ?", "Décrivez le livrable attendu.")]
for i, (t, ex, pb, fix) in enumerate(errs):
    x = 0.6 + (i % 2) * 6.2; y = 1.85 + (i // 2) * 2.5
    D.rrect(s, x, y, 5.93, 2.3, fill=LIGHT)
    D.circle(s, x + 0.25, y + 0.25, 0.55, fill=RED, text=str(i + 1), size=16)
    D.text(s, x + 1.0, y + 0.22, 4.7, 0.6, [[(t, {"bold": True, "size": 16, "font": TITLE_FONT, "color": NAVY}), ("   " + ex, {"size": 13, "italic": True, "color": MUTED})]], anchor="m")
    D.text(s, x + 1.0, y + 0.9, 4.7, 0.55, pb, size=13, color=INK)
    D.icon(s, "circle-check", x + 1.0, y + 1.62, 0.32, TEAL)
    D.text(s, x + 1.42, y + 1.55, 4.3, 0.48, fix, size=13.5, color=TEAL, bold=True, anchor="m")
D.footer(s)
N(s, "Les 4 erreurs", 1.25,
  "« Voici les quatre erreurs que je vois le plus souvent, chez les débutants comme chez les utilisateurs réguliers. »",
  "Pour chaque erreur : lisez l'exemple, puis la question que l'IA « se pose » (la ligne du milieu), puis la correction en vert. Faites remarquer que face à une demande floue, l'IA ne vous demande généralement pas de précisions : elle devine. Et elle devine de façon moyenne, générique.",
  question="« Laquelle de ces erreurs faites-vous le plus souvent ? » (réponse honnête à main levée, avec humour)",
  transition="« Pour ne plus jamais oublier ces éléments, je vous propose une méthode en six lettres. »")

s = D.new(WHITE); D.header(s, "Chapitre 3 · La méthode", "La méthode PILOTE : 6 lettres pour des prompts efficaces")
for i, (L, w, d, ex, ic) in enumerate(PILOTE):
    x = 0.6 + i * 2.04
    D.rrect(s, x, 1.85, 1.92, 3.85, fill=NAVY if i % 2 == 0 else NAVY2)
    D.text(s, x, 1.9, 1.92, 1.1, L, size=54, color=GOLD, bold=True, font=TITLE_FONT, align="c", anchor="m")
    D.text(s, x + 0.1, 3.0, 1.72, 0.4, w, size=14, color=WHITE, bold=True, font=TITLE_FONT, align="c")
    D.text(s, x + 0.12, 3.45, 1.68, 1.0, d, size=11, color="C9D3E6", align="c", spacing=1.0)
    D.icon(s, ic, x + 0.73, 4.85, 0.45, TEAL)
D.rrect(s, 0.6, 5.9, 7.4, 0.95, fill=TEAL)
D.text(s, 0.85, 5.9, 7.0, 0.95, "Vous êtes le PILOTE. L'IA est votre copilote.", size=18, color=WHITE, bold=True, font=TITLE_FONT, anchor="m")
D.rrect(s, 8.2, 5.9, 4.53, 0.95, fill="FBF5E6")
D.text(s, 8.4, 5.9, 4.2, 0.95, [[("Le minimum vital : ", {"bold": True, "color": "9C7C2C"}), ("I + L + O", {"bold": True, "color": NAVY}), (". Ajoutez P, T, E quand l'enjeu monte.", {"color": INK})]], size=12.5, anchor="m")
D.footer(s)
N(s, "La méthode PILOTE", 1.5,
  "« Six lettres, un mot facile à retenir : PILOTE. Parce que c'est vous qui pilotez. »",
  "P = Persona : le rôle que l'IA doit jouer (juriste, commercial, formateur…). I = Informations : le contexte, les données. L = Livrable : ce que vous voulez recevoir, et sous quelle forme. O = Objectif : pourquoi, à quoi cela doit servir. T = Ton : le style. E = Exigences : les contraintes et critères de qualité (n'invente rien, 150 mots max, pose-moi des questions…). Insistez sur le minimum vital : pour une demande courante, I + L + O suffisent souvent.",
  example="Faites répéter le mot au public : « Comment s'appelle la méthode ? » — « PILOTE ! » Cela ancre la mémoire.",
  points=["Ne transformez pas PILOTE en carcan : pour traduire un mot ou trouver un synonyme, une phrase suffit", "L'ordre des lettres n'est pas obligatoire dans le prompt"],
  transition="« Concrètement, quand utiliser un prompt simple et quand sortir la méthode complète ? »")

s = D.new(WHITE); D.header(s, "Chapitre 3 · Doser l'effort", "Prompt simple ou prompt structuré ?")
levels = [("Demande simple", "Traduire une phrase, trouver un synonyme, une idée rapide", "Une phrase suffit", "« Traduis en anglais : … »", "AFC2DD"),
          ("Tâche courante", "Email interne, résumé, liste d'idées, plan", "I + L + O", "Contexte, livrable, objectif", TEAL),
          ("Enjeu important", "Client, direction, publication, document engageant", "PILOTE complet", "Les 6 éléments + relecture", NAVY)]
for i, (t, d, how, ex, c) in enumerate(levels):
    y = 1.9 + i * 1.12
    D.rect(s, 0.6, y, 0.35 + i * 0.0, 1.0, fill=c)
    D.rrect(s, 1.05, y, 5.45, 1.0, fill=LIGHT)
    D.text(s, 1.25, y, 5.2, 1.0, [[(t, {"bold": True, "font": TITLE_FONT, "size": 14, "color": NAVY})], [(d, {"size": 11.5, "color": MUTED})]], anchor="m")
    D.rrect(s, 1.05 + 5.55, y, 0.0 + 0.01, 1.0, fill=LIGHT) if False else None
D.text(s, 0.6, 5.35, 6, 0.4, "RÈGLE PRATIQUE", size=11, color=GOLD, bold=True, font=TITLE_FONT)
D.text(s, 0.6, 5.7, 5.9, 1.2, "Plus l'enjeu est élevé, plus vous détaillez. Et si vous hésitez : « Pose-moi les questions nécessaires avant de répondre. »", size=13.5, color=INK, spacing=1.1)
for i, (t, d, how, ex, c) in enumerate(levels):
    y = 1.9 + i * 1.12
    D.rrect(s, 6.6, y + 0.2, 1.3, 0.6, fill=c, radius=0.5)
    D.text(s, 6.6, y + 0.2, 1.3, 0.6, ["1 phrase", "I + L + O", "PILOTE"][i], size=11, color=WHITE if c != "AFC2DD" else NAVY, bold=True, font=TITLE_FONT, align="c", anchor="m")
D.rrect(s, 8.15, 1.9, 4.58, 4.95, fill=NAVY)
D.text(s, 8.4, 2.05, 4.1, 0.4, "LE MODÈLE À RÉUTILISER", size=11, color=GOLD, bold=True, font=TITLE_FONT)
tpl = [("P", "Agis comme [RÔLE]."), ("I", "Contexte : [SITUATION, DONNÉES]."), ("L", "Produis : [LIVRABLE + FORMAT]."),
       ("O", "Objectif : [À QUOI ÇA SERT]."), ("T", "Ton : [STYLE]."), ("E", "Exigences : [CONTRAINTES]. Pose-moi des questions si besoin.")]
for i, (L, t) in enumerate(tpl):
    y = 2.55 + i * 0.7
    D.circle(s, 8.4, y + 0.05, 0.45, fill=GOLD, text=L, color=NAVY, size=13)
    D.text(s, 9.0, y - 0.02, 3.6, 0.65, t, size=12, color=WHITE, anchor="m", spacing=1.0)
D.footer(s)
N(s, "Prompt simple ou structuré", 1,
  "« Attention : je ne vous demande pas d'écrire un roman à chaque fois. »",
  "Trois niveaux : demande simple (une phrase), tâche courante (contexte + livrable + objectif), enjeu important (PILOTE complet). À droite, le modèle à réutiliser : il est dans votre kit, vous pourrez le copier-coller. Donnez l'astuce : si vous ne savez pas quoi préciser, demandez à l'IA de vous poser des questions d'abord.",
  points=["Le modèle PILOTE est imprimé dans le Kit IA (Partie 3 : le prompt universel)"],
  transition="« Passons à la démonstration : trois prompts pour le même besoin. »")

for k, dm in enumerate(DEMO3):
    s = D.new(WHITE); D.header(s, f"Chapitre 3 · Démonstration {k+1}/3", f"{dm['level']}")
    D.chat_window(s, 0.6, 1.8, 8.0, 5.05)
    nlines = dm["prompt"].count("\n") + 1
    ph = 0.65 if nlines == 1 else 1.95
    D.bubble_user(s, 2.2 if nlines == 1 else 1.0, 2.4, 6.2 if nlines == 1 else 7.4, ph, dm["prompt"], size=11.5 if nlines == 1 else 9.5)
    ay = 2.4 + ph + 0.18
    D.bubble_ai(s, 0.8, ay, 7.6, 6.7 - ay, dm["answer"].replace("\n\n", "\n"), size=10.5 if k < 2 else 9.5)
    D.rrect(s, 8.85, 1.8, 3.88, 5.05, fill=LIGHT)
    D.rect(s, 8.85, 1.8, 3.88, 0.09, fill=dm["color"])
    D.text(s, 9.1, 2.05, 3.4, 0.4, "NIVEAU DE QUALITÉ", size=11, color=MUTED, bold=True, font=TITLE_FONT)
    for j in range(3):
        D.icon(s, "star", 9.1 + j * 0.55, 2.5, 0.45, GOLD if j <= k else "C9D1DE")
    D.text(s, 9.1, 3.2, 3.4, 0.4, "CE QUI SE PASSE", size=11, color=MUTED, bold=True, font=TITLE_FONT)
    D.text(s, 9.1, 3.6, 3.45, 2.2, dm["why"], size=13, color=INK, spacing=1.1)
    tag = ["Inutilisable", "À retravailler", "Prêt après relecture"][k]
    D.rrect(s, 9.1, 6.0, 3.4, 0.6, fill=dm["color"], radius=0.5)
    D.text(s, 9.1, 6.0, 3.4, 0.6, tag, size=13, color=WHITE, bold=True, font=TITLE_FONT, align="c", anchor="m")
    D.footer(s)
    exps = ["Lisez le prompt « Écris un email pour un client. » Demandez : « Que va répondre l'IA ? » Puis montrez la réponse : polie, vide, inutilisable. Ce n'est pas la faute de l'IA : elle n'avait rien à quoi se raccrocher.",
            "Le sujet est maintenant clair, la réponse est meilleure… mais regardez : l'IA a inventé un nom de client (« Monsieur Martin ») et une cause (« difficultés logistiques »). Elle comble les vides. Et elle ne propose aucune solution, parce qu'on ne lui a pas dit quel était l'objectif.",
            "Montrez les lettres P-I-L-O-T-E dans le prompt. Le résultat est précis, empathique, propose une solution concrète, et n'invente rien car on le lui a interdit (Exigences). Il reste à relire, mais on gagne un temps considérable. Précisez : « Rédiger ce prompt prend environ une minute de plus. C'est l'investissement le plus rentable de votre journée. »"]
    N(s, f"Démo prompt {k+1}", [1.25, 1, 1.5][k],
      ["« Premier essai, comme le font 80 % des utilisateurs. »", "« On améliore un peu… »", "« Et maintenant, la version PILOTE. »"][k],
      exps[k],
      question=["« À votre avis, que va répondre l'IA ? »", "« Qu'est-ce que l'IA a inventé ici ? »", "« Retrouvez les 6 lettres de PILOTE dans ce prompt. »"][k],
      points=["Si vous avez le temps et la connexion, tapez ce prompt en direct dans l'assistant : les réponses varieront légèrement, c'est normal"] if k == 2 else None,
      transition=["« Améliorons la demande. »", "« Passons au niveau professionnel. »", "« Comparons les trois versions côte à côte. »"][k])

s = D.new(WHITE); D.header(s, "Chapitre 3 · Comparaison", "Ce qui change vraiment d'un prompt à l'autre")
hdr = [("", None), ("Faible", RED), ("Amélioré", ORANGE), ("PILOTE", TEAL)]
rows = [("Contexte fourni", "Aucun", "Sujet seulement", "Client, dates, quantités, cause"),
        ("Objectif exprimé", "Non", "Non", "Garder la confiance, proposer une solution"),
        ("Format demandé", "Non", "Non", "120-150 mots, objet clair"),
        ("Garde-fous", "Non", "Non", "« N'invente aucune information »"),
        ("Informations inventées", "Possible", "Oui (nom, cause)", "Aucune"),
        ("Temps de retouche", "Tout réécrire", "Important", "Simple relecture")]
widths = [3.2, 2.6, 2.6, 3.73]; xs = [0.6]
for w in widths[:-1]: xs.append(xs[-1] + w)
for j, (h, c) in enumerate(hdr):
    if c: D.rect(s, xs[j] + 0.04, 1.85, widths[j] - 0.08, 0.6, fill=c); D.text(s, xs[j], 1.85, widths[j], 0.6, h, size=14, color=WHITE, bold=True, font=TITLE_FONT, align="c", anchor="m")
for i, r in enumerate(rows):
    y = 2.55 + i * 0.68
    D.rect(s, 0.6, y, 12.13, 0.62, fill=LIGHT if i % 2 == 0 else WHITE)
    for j, cell in enumerate(r):
        D.text(s, xs[j] + 0.15, y, widths[j] - 0.3, 0.62, cell, size=12.5 if j else 13, color=NAVY if j == 0 else (TEAL if j == 3 else INK), bold=(j == 0 or j == 3), font=TITLE_FONT if j == 0 else BODY_FONT, anchor="m", align="l" if j == 0 else "c")
D.footer(s)
N(s, "Comparatif des 3 prompts", 1,
  "« Résumons ce qui a fait la différence. »",
  "Parcourez la grille ligne par ligne. Insistez sur deux lignes : « Informations inventées » (plus le contexte est pauvre, plus l'IA invente) et « Temps de retouche » (le temps investi dans le prompt est récupéré, et au-delà, dans la retouche).",
  transition="« Dernier point essentiel : la première réponse n'est jamais la dernière. »")

s = D.new(WHITE); D.header(s, "Chapitre 3 · Itérer", "La 1re réponse est un brouillon : relancez !")
icons = ["scissors" if os.path.exists(os.path.join(ICON_DIR, "scissors.svg")) else "filter", "message-circle", "table", "scan-search", "circle-help"]
for i, ((t, q), ic) in enumerate(zip(ITERATIONS, icons)):
    y = 1.85 + i * 0.86
    D.rrect(s, 0.6, y, 8.1, 0.76, fill=LIGHT)
    D.icon(s, ic, 0.82, y + 0.17, 0.42, TEAL)
    D.text(s, 1.45, y, 2.3, 0.76, t, size=13, color=NAVY, bold=True, font=TITLE_FONT, anchor="m")
    D.text(s, 3.8, y, 4.8, 0.76, q, size=11.5, color=INK, anchor="m", italic=True, spacing=1.0)
D.rrect(s, 8.95, 1.85, 3.78, 4.18, fill=NAVY)
D.icon(s, "refresh-cw", 9.25, 2.15, 0.6, GOLD)
D.text(s, 9.25, 2.95, 3.25, 3.0, [[("Restez dans la même conversation", {"bold": True, "size": 16, "font": TITLE_FONT, "color": WHITE})],
                                  [("L'IA garde en mémoire ce qui précède : inutile de tout réexpliquer. Ouvrez une nouvelle conversation seulement pour changer de sujet.", {"size": 12.5, "color": "C9D3E6"})]], spacing=1.1)
D.rrect(s, 8.95, 6.15, 3.78, 0.7, fill=GOLD)
D.text(s, 8.95, 6.15, 3.78, 0.7, "Demander > Observer > Préciser", size=12.5, color=NAVY, bold=True, font=TITLE_FONT, align="c", anchor="m")
D.footer(s)
N(s, "Itérer", 1.5,
  "« Les meilleurs utilisateurs ne sont pas ceux qui écrivent le prompt parfait du premier coup. Ce sont ceux qui savent relancer. »",
  "Présentez les cinq relances : raccourcir, changer de ton, changer de format, faire critiquer, faire poser des questions. La relance « fais critiquer » est souvent une révélation : l'IA identifie elle-même les faiblesses de son texte et les corrige. Encadré de droite : rester dans la même conversation pour garder le contexte.",
  example="« Une responsable marketing m'a dit : “Je pensais que l'IA écrivait mal. En fait, je m'arrêtais à la première réponse.” »",
  question="« Laquelle de ces relances allez-vous essayer en premier ? »",
  transition="« Vous avez maintenant la méthode. Vérifions-le ! »")

thanks_slide(3, ""); quiz_slide(3); answer_slide(3, CHAPTERS[2]["transition"])

# =====================================================================================
# CHAPITRE 4
# =====================================================================================
ch = CHAPTERS[3]
s = chapter_cover(ch, 12)
N(s, "Chapitre 4 — couverture", 0.25, "« Place à la pratique. Nous allons traiter ensemble une vraie situation de travail. »",
  "Si vous faites la démonstration en direct, ouvrez maintenant l'assistant IA dans un onglet et gardez les prompts du Guide du formateur à portée de main (fichier texte prêt à copier). Sinon, les diapositives suivantes montrent tous les résultats : la démonstration fonctionne sans connexion.",
  points=["PLAN B : si Internet ou l'outil ne fonctionne pas, déroulez simplement les diapositives : elles contiennent les prompts et les résultats"],
  transition="« Voici la situation. »")

s = D.new(WHITE); D.header(s, "Chapitre 4 · Le scénario", "Vous sortez d'une réunion… et vous avez 15 minutes")
D.rrect(s, 0.6, 1.85, 5.4, 5.0, fill=NAVY)
D.icon(s, "building-2", 0.9, 2.1, 0.55, GOLD)
D.text(s, 0.9, 2.75, 4.85, 1.8, [[("Nova Distribution", {"bold": True, "size": 18, "font": TITLE_FONT, "color": WHITE})],
                                 [("PME de 60 salariés. Réunion de lancement d'un nouveau logiciel de facturation. Vous devez diffuser le compte rendu et le plan d'action aujourd'hui.", {"size": 13, "color": "C9D3E6"})]], spacing=1.1)
D.text(s, 0.9, 4.65, 4.8, 0.4, "VOTRE MISSION AVEC L'IA", size=11, color=GOLD, bold=True, font=TITLE_FONT)
for i, m in enumerate(["Un compte rendu clair", "Les décisions prises", "Un plan d'action (qui, quoi, quand)", "L'email de suivi aux participants"]):
    D.icon(s, "circle-check", 0.9, 5.08 + i * 0.42, 0.28, TEAL)
    D.text(s, 1.3, 5.03 + i * 0.42, 4.5, 0.38, m, size=12.5, color=WHITE, anchor="m")
D.rect(s, 6.25, 1.85, 6.48, 5.0, fill="FFFDF6", line="E8DDBE")
D.text(s, 6.5, 1.98, 6, 0.35, "VOS NOTES BRUTES (telles quelles)", size=10.5, color="9C7C2C", bold=True, font=TITLE_FONT)
D.text(s, 6.5, 2.35, 6.1, 4.4, NOTES_BRUTES, size=11, color=INK, spacing=1.12, font="Inter")
D.footer(s)
N(s, "Le scénario", 1,
  "« Situation universelle : vous sortez d'une réunion, vous avez pris des notes en vrac, et il faut diffuser un compte rendu propre. »",
  "Lisez le cadre de gauche (contexte et mission), puis montrez les notes brutes à droite : abréviations, flèches, points non tranchés. C'est volontairement réaliste. Précisez : ces notes ne contiennent aucune donnée sensible, on peut donc les utiliser dans un outil d'IA (rappel du chapitre 5 à venir).",
  question="« Combien de temps vous faudrait-il pour transformer ces notes en compte rendu propre ? »",
  transition="« Voici la démarche que nous allons suivre, en 8 étapes. »")

s = D.new(WHITE); D.header(s, "Chapitre 4 · La démarche", "Travailler avec l'IA en 8 étapes")
for i, (t, d, ic) in enumerate(WORKFLOW4):
    x = 0.6 + (i % 4) * 3.1; y = 1.95 + (i // 4) * 2.45
    D.rrect(s, x, y, 2.85, 2.15, fill=LIGHT if i not in (4, 7) else ("E6F4F2" if i == 4 else "FBF5E6"))
    D.circle(s, x + 0.2, y + 0.2, 0.55, fill=NAVY if i not in (4, 7) else (TEAL if i == 4 else GOLD), text=str(i + 1), size=15)
    D.icon(s, ic, x + 2.1, y + 0.25, 0.48, TEAL)
    D.text(s, x + 0.2, y + 0.95, 2.5, 1.1, [[(t, {"bold": True, "size": 15, "font": TITLE_FONT, "color": NAVY})], [(d, {"size": 12, "color": INK})]])
    if i % 4 != 3:
        D.arrow(s, x + 2.88, y + 0.92, 0.19, 0.3, fill=GOLD)
D.footer(s)
N(s, "La démarche en 8 étapes", 1,
  "« Voici la feuille de route. Elle s'applique à presque toutes les tâches. »",
  "Parcourez rapidement les 8 étapes. Faites remarquer les deux étapes colorées : l'étape 5 (Améliorer avec PILOTE) et l'étape 8 (Vérifier). Ce sont celles que les débutants sautent, et ce sont celles qui font la qualité.",
  transition="« Étapes 1 à 3 : on commence comme tout le monde. »")

s = D.new(WHITE); D.header(s, "Chapitre 4 · Étapes 1 à 3", "Première demande… premier constat")
D.chat_window(s, 0.6, 1.8, 7.7, 5.05)
D.bubble_user(s, 2.0, 2.45, 6.1, 0.65, PROMPT4_V1, size=12)
D.bubble_ai(s, 0.8, 3.3, 7.3, 2.6, ANSWER4_V1, size=12)
D.rrect(s, 8.55, 1.8, 4.18, 5.05, fill=LIGHT)
D.rect(s, 8.55, 1.8, 4.18, 0.09, fill=RED)
D.text(s, 8.8, 2.0, 3.7, 0.4, "CE QUI MANQUE", size=12, color=RED, bold=True, font=TITLE_FONT)
for i, m in enumerate(MISSING4):
    D.icon(s, "circle-x", 8.8, 2.6 + i * 0.75 + 0.06, 0.32, RED)
    D.text(s, 9.25, 2.55 + i * 0.75, 3.35, 0.7, m, size=13, color=INK, anchor="m", spacing=1.0)
D.footer(s)
N(s, "Étapes 1-3 : première demande", 1.5,
  "EN DIRECT (optionnel) : collez le prompt « Fais un compte rendu de cette réunion » suivi des notes (disponibles dans le Guide du formateur). Sinon, montrez la diapositive.",
  "Lisez la réponse : elle est correcte en apparence, bien écrite… et inutilisable. Demandez au public ce qui manque AVANT d'afficher la colonne de droite si vous le pouvez. Faites ressortir : pas de décisions, pas de responsables, pas d'échéances, le conflit de date a disparu.",
  question="« Pourriez-vous envoyer ce compte rendu tel quel ? Qu'est-ce qui vous manque ? »",
  points=["Les réponses en direct varieront : c'est normal, l'important est le diagnostic"],
  transition="« Étapes 4 et 5 : on diagnostique et on reformule avec PILOTE. »")

s = D.new(WHITE); D.header(s, "Chapitre 4 · Étapes 4 et 5", "On reformule la demande avec PILOTE")
D.chat_window(s, 0.6, 1.8, 8.6, 5.05)
D.bubble_user(s, 0.85, 2.45, 8.1, 4.2, PROMPT4_V2, size=12)
lines = ["P — rôle : chef de projet rigoureux", "I — les notes brutes", "L — 5 rubriques, dont un tableau d'actions", "O — chacun sait quoi faire", "T — factuel et concis", "E — « N'invente rien », « À définir », signaler les contradictions"]
D.rrect(s, 9.45, 1.8, 3.28, 5.05, fill=LIGHT)
D.text(s, 9.65, 2.0, 3, 0.4, "DÉCODAGE", size=12, color=GOLD, bold=True, font=TITLE_FONT)
for i, l in enumerate(lines):
    D.circle(s, 9.65, 2.55 + i * 0.7, 0.42, fill=NAVY, text=l[0], size=12)
    D.text(s, 10.17, 2.48 + i * 0.7, 2.5, 0.6, l[4:], size=11, color=INK, anchor="m", spacing=1.0)
D.footer(s)
N(s, "Étapes 4-5 : prompt PILOTE", 1.5,
  "EN DIRECT (optionnel) : dans la même conversation, collez le prompt PILOTE fourni dans le Guide du formateur.",
  "Montrez comment chaque manque identifié à l'étape précédente devient une instruction : pas de décisions → rubrique « décisions » ; pas de responsables → tableau d'actions ; risque d'invention → « N'invente rien, écris À définir ». Le prompt est plus long, mais il ne fait que traduire nos besoins.",
  points=["Mettez en avant l'exigence « signale toute contradiction » : c'est elle qui fera ressortir le problème de date"],
  transition="« Voyons le résultat. »")

s = D.new(WHITE); D.header(s, "Chapitre 4 · Étapes 6 et 7", "Le résultat : un compte rendu exploitable")
D.rrect(s, 0.6, 1.8, 12.13, 5.05, fill=WHITE, line="D5DBE5")
D.icon_badge(s, "sparkles", 0.85, 2.0, 0.42, bg=TEAL)
D.text(s, 1.4, 2.0, 8, 0.42, "Compte rendu — Lancement du logiciel de facturation (14/11)", size=14, color=NAVY, bold=True, font=TITLE_FONT, anchor="m")
D.text(s, 0.85, 2.6, 5.6, 0.35, "DÉCISIONS PRISES", size=11, color=TEAL, bold=True, font=TITLE_FONT)
for i, d in enumerate(ANSWER4_V2["decisions"]):
    D.text(s, 0.85, 2.95 + i * 0.4, 5.6, 0.38, "•  " + d, size=12, color=INK)
D.text(s, 6.75, 2.6, 5.8, 0.35, "TABLEAU DES ACTIONS", size=11, color=TEAL, bold=True, font=TITLE_FONT)
cw = [2.9, 1.2, 1.6]; cx = [6.75, 9.65, 10.85]
for j, h in enumerate(["Action", "Responsable", "Échéance"]):
    D.rect(s, cx[j], 2.95, cw[j] - 0.04, 0.38, fill=NAVY)
    D.text(s, cx[j] + 0.08, 2.95, cw[j] - 0.15, 0.38, h, size=10.5, color=WHITE, bold=True, anchor="m")
for i, row in enumerate(ANSWER4_V2["actions"]):
    for j, c in enumerate(row):
        D.rect(s, cx[j], 3.37 + i * 0.44, cw[j] - 0.04, 0.4, fill=LIGHT)
        D.text(s, cx[j] + 0.08, 3.37 + i * 0.44, cw[j] - 0.15, 0.4, c, size=10.5, color=INK, anchor="m")
D.text(s, 0.85, 4.45, 5.6, 0.35, "POINT NON TRANCHÉ", size=11, color=ORANGE, bold=True, font=TITLE_FONT)
D.text(s, 0.85, 4.8, 5.6, 0.6, "•  " + ANSWER4_V2["open_points"][0], size=12, color=INK)
D.text(s, 6.75, 4.85, 5.8, 0.35, "RISQUES ET CONTRADICTION SIGNALÉS", size=11, color=RED, bold=True, font=TITLE_FONT)
for i, r in enumerate(ANSWER4_V2["risks"]):
    D.text(s, 6.75, 5.2 + i * 0.55, 5.8, 0.55, "•  " + r, size=11.5, color=INK, spacing=1.0)
D.rrect(s, 0.85, 5.65, 5.6, 0.95, fill="E6F4F2")
D.text(s, 1.05, 5.65, 5.3, 0.95, "Structuré, actionnable, avec la contradiction de dates mise en évidence. Mais… est-il juste ?", size=12.5, color=NAVY, bold=True, anchor="m")
D.footer(s)
N(s, "Étapes 6-7 : le résultat", 1.5,
  "« Comparez avec la première version : on change de monde. »",
  "Montrez les rubriques : décisions, tableau d'actions, point non tranché, risques. Faites remarquer que l'IA a bien signalé la contradiction entre la date du 6 janvier et les deux semaines de tests : c'est l'exigence « signale toute contradiction » qui a fonctionné. Terminez par la question en bas à gauche : « Est-il juste ? » et laissez planer le doute. Ne révélez pas encore l'erreur.",
  question="« Quelqu'un voit-il un problème dans ce compte rendu ? » (laisser chercher 15 secondes)",
  transition="« Avant de vérifier, on va même lui demander l'email de suivi. »")

s = D.new(WHITE); D.header(s, "Chapitre 4 · Relance", "On enchaîne : l'email de suivi en une phrase")
D.chat_window(s, 0.6, 1.8, 12.13, 5.05)
D.bubble_user(s, 3.2, 2.42, 9.3, 0.95, PROMPT4_V3, size=11.5)
EMAIL = ("Objet : Logiciel de facturation – décisions et actions (réunion du 14/11)\n"
         "Bonjour à tous, merci pour vos contributions. Décisions : formation du service client la semaine du 8 décembre ; budget de 3 500 € validé.\n"
         "Actions : Karim – planning de migration (vendredi) · Julie – organisation de la formation · Marc – information des 20 plus gros clients.\n"
         "Point de vigilance : la date du 6 janvier dépend de la fin de la migration. Merci de confirmer vos actions avant le 21/11. Prochaine réunion : 28/11.")
D.bubble_ai(s, 0.8, 3.55, 11.75, 2.55, EMAIL, size=11.5)
D.rrect(s, 0.85, 6.22, 11.6, 0.5, fill="FBF5E6")
D.text(s, 1.05, 6.22, 11.3, 0.5, "L'IA a gardé tout le contexte : une seule phrase suffit pour obtenir l'email. Gain de temps maximal… si le contenu est exact.", size=12, color=NAVY, bold=True, anchor="m")
D.footer(s)
N(s, "Relance : email de suivi", 1.25,
  "EN DIRECT (optionnel) : tapez la relance dans la même conversation.",
  "Montrez qu'une simple phrase suffit, puisque l'IA a gardé le contexte. L'email est clair, court, avec une date de confirmation. Puis dites : « On l'envoie ? »… Attendez une réaction. Quelqu'un remarquera peut-être la ligne « Marc – information des 20 plus gros clients ».",
  question="« On l'envoie tel quel ? »",
  transition="« Pas si vite : étape 8, la vérification. »")

s = D.new(WHITE); D.header(s, "Chapitre 4 · Étape 8", "Vérifier avant de diffuser : ce que la relecture révèle")
for i, (t, d, c) in enumerate(CATCHES4):
    y = 1.85 + i * 1.3
    D.rrect(s, 0.6, y, 7.6, 1.15, fill=LIGHT)
    D.rect(s, 0.6, y, 0.1, 1.15, fill=c)
    D.icon(s, ["triangle-alert", "circle-help", "circle-check"][i], 0.9, y + 0.33, 0.48, c)
    D.text(s, 1.6, y + 0.05, 6.45, 1.05, [[(t, {"bold": True, "font": TITLE_FONT, "size": 14, "color": c if c != ORANGE else "B5761A"})], [(d, {"size": 12.5, "color": INK})]], anchor="m", spacing=1.02)
D.rrect(s, 0.6, 5.85, 7.6, 1.0, fill=NAVY)
D.text(s, 0.85, 5.85, 7.2, 1.0, [[("Relance de correction : ", {"bold": True, "color": GOLD}), ("« Le point sur les 20 clients n'est pas tranché : retire l'action de Marc, place-le dans les points ouverts avec “Responsable : à définir”. »", {"color": WHITE})]], size=12, anchor="m")
D.rrect(s, 8.45, 1.85, 4.28, 5.0, fill="FBF5E6")
D.text(s, 8.7, 2.05, 3.8, 0.4, "CHECK-LIST AVANT ENVOI", size=12, color="9C7C2C", bold=True, font=TITLE_FONT)
for i, c in enumerate(["Noms et rôles", "Dates et échéances", "Montants et chiffres", "Décisions = notes d'origine", "Points non tranchés bien signalés", "Ton adapté aux destinataires"]):
    D.icon(s, "square-check" if os.path.exists(os.path.join(ICON_DIR, "square-check.svg")) else "circle-check", 8.7, 2.62 + i * 0.66, 0.36, GOLD)
    D.text(s, 9.2, 2.56 + i * 0.66, 3.4, 0.5, c, size=13, color=NAVY, bold=True, anchor="m")
D.footer(s)
N(s, "Étape 8 : vérifier", 1.75,
  "« Reprenons le compte rendu, ligne à ligne, avec nos notes d'origine. »",
  "Révélez les trois constats. 1) L'erreur : l'IA a attribué à Marc une action alors que le point n'était PAS tranché. C'est typique : l'IA « complète » de façon plausible. Si vous envoyez cet email, Marc reçoit une mission que personne ne lui a confiée. 2) L'hypothèse : Julie organise la formation ? Logique, mais non décidé : à confirmer. 3) Le point positif : la contradiction de dates a bien été repérée. Montrez la relance de correction et la check-list.",
  example="« Imaginez la réunion suivante : “Marc, où en est l'information des clients ?” — “Quelle information ?” C'est exactement ce que la vérification évite. »",
  points=["Message clé : l'IA a fait 90 % du travail en 3 minutes ; les 10 % de vérification sont VOTRE valeur ajoutée", "La check-list de droite est reprise dans le syllabus"],
  transition="« Merci d'avoir joué le jeu. Petit quiz ! »")

thanks_slide(4, ""); quiz_slide(4); answer_slide(4, CHAPTERS[3]["transition"])

# =====================================================================================
# CHAPITRE 5
# =====================================================================================
ch = CHAPTERS[4]
s = chapter_cover(ch, 8)
N(s, "Chapitre 5 — couverture", 0.25, "« Dernier chapitre, et non des moindres : utiliser l'IA de façon responsable. »",
  "Annoncez trois sujets : les hallucinations, la protection des données, et une règle simple pour vérifier.",
  transition="« Commençons par le risque le plus connu. »")

s = D.new(WHITE); D.header(s, "Chapitre 5 · Hallucinations", "Quand l'IA invente avec aplomb")
D.chat_window(s, 0.6, 1.8, 7.2, 5.05)
D.bubble_user(s, 1.6, 2.42, 6.0, 0.95, "Donne-moi une statistique récente et sa source sur l'usage de l'IA dans les PME européennes.", size=11.5)
D.bubble_ai(s, 0.8, 3.55, 6.8, 1.85, "Selon l'étude 2024 de l'Observatoire européen des PME numériques, 73,4 % des PME européennes utilisent quotidiennement l'IA générative, avec un gain moyen de 11,2 heures par salarié et par semaine.", size=11.5)
D.rrect(s, 0.85, 5.6, 6.7, 1.05, fill="FBE9E7")
D.text(s, 1.05, 5.6, 6.4, 1.05, [[("Exemple fictif d'hallucination : ", {"bold": True, "color": RED}), ("l'organisme et les chiffres sont inventés, mais tout semble crédible.", {"color": INK})]], size=12, anchor="m")
D.rrect(s, 8.05, 1.8, 4.68, 5.05, fill=LIGHT)
D.text(s, 8.3, 2.0, 4.2, 0.4, "LES SIGNAUX D'ALERTE", size=12, color=RED, bold=True, font=TITLE_FONT)
for i, a in enumerate(["Chiffres très précis sans lien vérifiable", "Source, auteur ou étude introuvable", "Citations « parfaites », références juridiques", "Ton très assuré sur un sujet pointu"]):
    D.icon(s, "triangle-alert", 8.3, 2.55 + i * 0.62 + 0.05, 0.3, RED)
    D.text(s, 8.72, 2.5 + i * 0.62, 3.9, 0.58, a, size=12, color=INK, anchor="m", spacing=1.0)
D.text(s, 8.3, 5.1, 4.2, 0.4, "LE RÉFLEXE", size=12, color=TEAL, bold=True, font=TITLE_FONT)
D.text(s, 8.3, 5.45, 4.25, 1.3, "Exiger la source, l'ouvrir réellement, retrouver l'information à l'origine. Introuvable = inutilisable.", size=12.5, color=NAVY, bold=True, spacing=1.1)
D.footer(s)
N(s, "Hallucinations", 1.25,
  "« Lisez cette réponse. Vous la mettriez dans une présentation à votre direction ? »",
  "Laissez réagir, puis révélez : l'organisme n'existe pas, les chiffres sont inventés. C'est une hallucination : le modèle produit une réponse plausible, avec un niveau de détail qui inspire confiance. Le risque est maximal pour les chiffres, les sources, les références juridiques, les citations et les biographies. Le réflexe : demander la source, l'ouvrir, la vérifier.",
  example="Il existe des cas publics, très médiatisés, de professionnels ayant cité dans des documents officiels des références inventées par une IA. La leçon : la responsabilité reste toujours celle de l'humain qui signe.",
  question="« Avez-vous déjà eu un doute sur une réponse d'IA ? »",
  points=["Les outils avec recherche web réduisent le risque mais ne l'éliminent pas : une source citée peut ne pas dire ce que l'IA lui attribue"],
  transition="« Deuxième risque : ce que VOUS donnez à l'IA. »")

s = D.new(WHITE); D.header(s, "Chapitre 5 · Confidentialité", "Le feu tricolore des données")
for i, (t, c, ex) in enumerate(TRAFFIC):
    y = 1.85 + i * 1.5
    D.rrect(s, 0.6, y, 12.13, 1.35, fill=LIGHT)
    D.circle(s, 0.85, y + 0.25, 0.85, fill=c)
    D.icon(s, ["lock", "eye", "circle-check"][i], 1.05, y + 0.45, 0.45, WHITE)
    D.text(s, 1.95, y + 0.1, 4.3, 1.15, t, size=14, color=NAVY, bold=True, font=TITLE_FONT, anchor="m", spacing=1.0)
    for j, e in enumerate(ex):
        D.text(s, 6.4 + (j % 2) * 3.2, y + 0.18 + (j // 2) * 0.5, 3.15, 0.5, "•  " + e, size=11.5, color=INK, anchor="m", spacing=1.0)
D.rrect(s, 0.6, 6.4, 12.13, 0.48, fill="E6F4F2")
D.text(s, 0.85, 6.4, 11.7, 0.48, [[("Réflexe : ", {"bold": True, "color": TEAL}), ("utilisez les outils validés par votre entreprise, anonymisez ([CLIENT A], [MONTANT]) et vérifiez les paramètres de confidentialité.", {"color": NAVY})]], size=12, anchor="m")
D.footer(s)
N(s, "Feu tricolore des données", 1.25,
  "« Tout ce que vous tapez dans un outil d'IA sort de votre ordinateur. Où va-t-il ? Cela dépend de l'outil et de vos réglages. »",
  "Présentez les trois couleurs. ROUGE : jamais dans un outil public ou non validé (données personnelles, salaires, santé, coordonnées bancaires, chiffres non publiés, contrats). ORANGE : seulement après anonymisation, ou dans l'outil professionnel validé par l'entreprise. VERT : librement. Rappelez que les versions professionnelles des assistants offrent généralement des engagements contractuels de confidentialité plus forts que les versions grand public : vérifiez la politique de votre entreprise.",
  example="« Un collaborateur colle dans un outil grand public le tableau des salaires pour “faire une analyse rapide”. Même si l'intention est bonne, c'est une fuite potentielle de données personnelles. »",
  question="« Le compte rendu de notre atelier : rouge, orange ou vert ? » (réponse : vert ou orange selon les cas ; il ne contenait pas de données sensibles)",
  points=["Le RGPD s'applique aux données personnelles, y compris quand on utilise une IA", "Ne donnez pas de conseil juridique précis : renvoyez vers la politique interne et le DPO / référent"],
  transition="« Trois autres risques méritent votre attention. »")

s = D.new(WHITE); D.header(s, "Chapitre 5 · Autres vigilances", "Droits, biais, dépendance : trois réflexes")
cards = [("copyright", "Droits d'auteur", ["Ne faites pas reproduire des textes ou images protégés", "Vérifiez les conditions d'utilisation des contenus générés", "Respectez la politique interne sur la mention de l'IA"]),
         ("scale", "Biais", ["L'IA reflète les biais de ses données", "Exemple : une fiche de poste au masculin par défaut", "Demandez une relecture inclusive et croisez les sources"]),
         ("brain", "Dépendance", ["Gardez vos compétences : réfléchissez d'abord", "Faites votre propre plan, puis comparez", "L'IA est un partenaire d'entraînement, pas un cerveau de remplacement"])]
for i, (ic, t, lst) in enumerate(cards):
    x = 0.6 + i * 4.1
    D.rrect(s, x, 1.85, 3.88, 4.2, fill=LIGHT)
    D.icon_badge(s, ic, x + 0.3, 2.1, 0.85, bg=NAVY)
    D.text(s, x + 1.3, 2.1, 2.5, 0.85, t, size=17, color=NAVY, bold=True, font=TITLE_FONT, anchor="m")
    for j, l in enumerate(lst):
        D.icon(s, "arrow-right", x + 0.3, 3.25 + j * 0.9 + 0.06, 0.28, TEAL)
        D.text(s, x + 0.7, 3.2 + j * 0.9, 3.05, 0.85, l, size=12.5, color=INK, spacing=1.02)
D.rrect(s, 0.6, 6.2, 12.13, 0.68, fill=NAVY)
D.text(s, 0.85, 6.2, 11.7, 0.68, [[("Cadre légal : ", {"bold": True, "color": GOLD}), ("le RGPD protège les données personnelles et le règlement européen sur l'IA (AI Act) encadre progressivement les usages. Suivez la politique de votre entreprise.", {"color": WHITE})]], size=12, anchor="m")
D.footer(s)
N(s, "Droits, biais, dépendance", 1,
  "« Trois vigilances supplémentaires, en une minute. »",
  "Droits d'auteur : ne pas demander de reproduire des œuvres protégées, vérifier les conditions d'utilisation, notamment pour les images. Biais : l'IA reproduit des stéréotypes présents dans ses données d'entraînement ; on lui demande une relecture inclusive et on garde un œil critique. Dépendance : on garde ses compétences en réfléchissant d'abord, puis en comparant avec l'IA. Bandeau du bas : le cadre légal évolue, la politique de l'entreprise prime.",
  points=["Restez factuel et prudent sur le droit : ne pas affirmer de règles juridiques détaillées"],
  transition="« Et maintenant, la règle à retenir pour vérifier n'importe quelle réponse. »")

s = D.new(WHITE); D.header(s, "Chapitre 5 · La règle à retenir", "Avant d'utiliser une réponse : Vrai ? Juste ? Signable ?")
for i, (t, sub, lst, ic) in enumerate(VJS):
    x = 0.6 + i * 4.1
    c = [NAVY, TEAL, GOLD][i]
    D.rrect(s, x, 1.85, 3.88, 5.0, fill=LIGHT)
    D.rect(s, x, 1.85, 3.88, 1.55, fill=c)
    D.icon(s, ic, x + 0.3, 2.12, 0.6, WHITE)
    D.text(s, x + 1.05, 2.0, 2.7, 0.7, t, size=26, color=WHITE, bold=True, font=TITLE_FONT, anchor="m")
    D.text(s, x + 0.3, 2.82, 3.4, 0.5, sub, size=13, color=WHITE, bold=True)
    for j, l in enumerate(lst):
        D.circle(s, x + 0.3, 3.72 + j * 1.0, 0.36, fill=c, text=str(j + 1), size=11)
        D.text(s, x + 0.8, 3.62 + j * 1.0, 2.9, 0.95, l, size=12.5, color=INK, spacing=1.02)
D.footer(s)
N(s, "Vrai - Juste - Signable", 1.25,
  "« Si vous ne retenez qu'une règle de ce chapitre, retenez celle-ci : trois questions avant d'utiliser une réponse. »",
  "VRAI : les faits sont-ils exacts ? On vérifie chiffres, dates, noms, citations à la source, on refait les calculs importants. JUSTE : est-ce adapté à MON contexte, à mon client, à nos règles ? Rien d'oublié, rien d'ajouté ? SIGNABLE : suis-je prêt à l'assumer ? L'ai-je relu en entier, puis-je expliquer chaque phrase, ai-je respecté la confidentialité ? Faites le lien avec l'atelier : l'erreur sur Marc était un problème de « Juste ».",
  example="Faites répéter : « Vrai ? Juste ? Signable ? »",
  transition="« Pour terminer ce chapitre, voici les dix réflexes du professionnel qui utilise l'IA. »")

s = D.new(WHITE); D.header(s, "Chapitre 5 · Bonnes pratiques", "Les 10 réflexes du professionnel qui utilise l'IA")
for i, (t, d) in enumerate(REFLEXES):
    x = 0.6 + (i // 5) * 6.2; y = 1.85 + (i % 5) * 1.0
    D.circle(s, x, y + 0.12, 0.62, fill=NAVY if i % 2 == 0 else TEAL, text=str(i + 1), size=15)
    D.text(s, x + 0.8, y, 5.2, 0.9, [[(t, {"bold": True, "size": 14, "font": TITLE_FONT, "color": NAVY})], [(d, {"size": 11.5, "color": MUTED})]], anchor="m", spacing=1.0)
D.footer(s)
N(s, "Les 10 réflexes", 0.75,
  "« Voici la synthèse pratique, celle que vous pouvez afficher près de votre écran. »",
  "Ne lisez pas les dix : citez-en trois (contexte, vérification, protection des données) et indiquez qu'ils sont détaillés dans le Kit IA (Partie 4).",
  transition="« Dernier quiz de la formation ! »")

thanks_slide(5, ""); quiz_slide(5); answer_slide(5, CHAPTERS[4]["transition"])

# =====================================================================================
# CONCLUSION
# =====================================================================================
CUR_CH[0] = "Conclusion"
s = D.new(WHITE); D.header(s, "Conclusion", "Ce que vous retenez en 5 phrases")
for i, chp in enumerate(CHAPTERS):
    y = 1.85 + i * 0.98
    D.rrect(s, 0.6, y, 12.13, 0.86, fill=LIGHT)
    D.circle(s, 0.8, y + 0.13, 0.6, fill=[NAVY, NAVY2, TEAL, NAVY, NAVY2][i], text=f"0{i+1}", size=13)
    D.text(s, 1.6, y, 2.7, 0.86, chp["short"], size=13.5, color=NAVY, bold=True, font=TITLE_FONT, anchor="m")
    D.text(s, 4.35, y, 8.2, 0.86, chp["message"], size=12.5, color=INK, anchor="m", spacing=1.02)
D.footer(s)
N(s, "Récapitulatif", 1,
  "« Faisons le point : une phrase par chapitre. »",
  "Lisez les cinq messages clés lentement. Ils constituent la « fiche de révision express » du syllabus.",
  transition="« Maintenant, l'essentiel : que ferez-vous dès demain ? »")

s = D.new(WHITE); D.header(s, "Votre plan d'action", "Trois tâches, trois essais, dès cette semaine")
hd = ["Ma tâche à améliorer", "Temps actuel / fréquence", "Mon prompt PILOTE (idée)", "Premier essai le…"]
ws = [3.4, 2.4, 4.13, 2.2]; xs = [0.6]
for w in ws[:-1]: xs.append(xs[-1] + w)
for j, h in enumerate(hd):
    D.rect(s, xs[j] + 0.03, 1.85, ws[j] - 0.06, 0.6, fill=NAVY)
    D.text(s, xs[j] + 0.15, 1.85, ws[j] - 0.3, 0.6, h, size=12.5, color=WHITE, bold=True, font=TITLE_FONT, anchor="m")
ex = ["Ex. : compte rendu hebdomadaire", "1 h / semaine", "Chef de projet · notes · tableau d'actions…", "Lundi"]
for i in range(3):
    y = 2.55 + i * 0.95
    for j in range(4):
        D.rect(s, xs[j] + 0.03, y, ws[j] - 0.06, 0.85, fill=LIGHT)
    D.circle(s, xs[0] + 0.15, y + 0.2, 0.45, fill=TEAL, text=str(i + 1), size=13)
    if i == 0:
        for j in range(4):
            D.text(s, xs[j] + (0.75 if j == 0 else 0.15), y, ws[j] - (0.9 if j == 0 else 0.3), 0.85, ex[j], size=11.5, color=MUTED, italic=True, anchor="m")
D.rrect(s, 0.6, 5.55, 7.5, 1.3, fill="FBF5E6")
D.icon(s, "notebook-pen", 0.85, 5.85, 0.6, GOLD)
D.text(s, 1.65, 5.55, 6.3, 1.3, [[("1 minute, maintenant : ", {"bold": True, "color": "9C7C2C"}), ("notez une tâche dans votre syllabus (page « Plan d'action personnel »). Une seule suffit pour commencer.", {"color": NAVY})]], size=13.5, anchor="m")
D.rrect(s, 8.3, 5.55, 4.43, 1.3, fill=TEAL)
D.icon(s, "flag", 8.55, 5.85, 0.6, WHITE)
D.text(s, 9.35, 5.55, 3.25, 1.3, [[("Le défi IA de 7 jours", {"bold": True, "color": WHITE, "font": TITLE_FONT})], [("Un exercice de 10 minutes par jour, dans votre kit.", {"color": "E6F4F2", "size": 12})]], size=14, anchor="m")
D.footer(s)
N(s, "Plan d'action", 1.5,
  "« La formation ne vaut que par ce que vous en ferez la semaine prochaine. »",
  "Demandez à chacun de noter, MAINTENANT, une tâche (idéalement trois) dans le tableau du syllabus. Montrez l'exemple de la première ligne. Présentez le défi de 7 jours : un exercice court par jour, progressif, pour transformer la formation en habitude.",
  question="« Quelle est LA tâche que vous testerez en premier ? » (2 ou 3 volontaires)",
  points=["Laissez réellement 45 à 60 secondes d'écriture silencieuse : c'est le moment qui fait passer à l'action"],
  transition="« Et pour finir, un regard vers demain. »")

s = D.new(WHITE); D.header(s, "Ouverture", "Et demain ? Ce qui arrive déjà dans vos outils")
trends = [("layers", "Des assistants multimodaux", "Ils lisent vos documents, images, tableaux, et dialoguent à la voix."),
          ("bot", "Des agents qui enchaînent les tâches", "Rechercher, remplir, préparer… sous votre supervision."),
          ("presentation", "L'IA intégrée à vos logiciels", "Suite bureautique, messagerie, CRM : l'IA est là où vous travaillez."),
          ("workflow", "L'automatisation sans code", "Relier vos applications pour supprimer les tâches répétitives.")]
for i, (ic, t, d) in enumerate(trends):
    x = 0.6 + (i % 2) * 6.2; y = 1.85 + (i // 2) * 1.75
    D.rrect(s, x, y, 5.93, 1.6, fill=LIGHT)
    D.icon_badge(s, ic, x + 0.3, y + 0.35, 0.9, bg=TEAL if i in (0, 3) else NAVY)
    D.text(s, x + 1.45, y + 0.1, 4.3, 1.4, [[(t, {"bold": True, "size": 15, "font": TITLE_FONT, "color": NAVY})], [(d, {"size": 12.5, "color": INK})]], anchor="m")
D.rrect(s, 0.6, 5.5, 12.13, 1.35, fill=NAVY)
D.text(s, 0.9, 5.5, 11.6, 1.35, [[("Les outils changeront. La méthode restera : ", {"color": WHITE, "bold": True}), ("cadrer, dialoguer, vérifier, décider.", {"color": GOLD, "bold": True})]], size=19, font=TITLE_FONT, anchor="m", align="c")
D.footer(s)
N(s, "Ouverture", 1,
  "« Ce que vous avez appris aujourd'hui vous servira longtemps, même si les outils évoluent très vite. »",
  "Présentez les quatre tendances de façon réaliste, sans promesse spectaculaire : assistants multimodaux, agents, IA intégrée aux logiciels, automatisation sans code. Concluez sur la phrase du bas : la compétence durable, c'est la méthode.",
  points=["Évitez les prédictions chiffrées ou alarmistes sur l'emploi : restez factuel et encourageant"],
  transition="« Merci à vous. »")

s = D.new(NAVY)
D.rect(s, 0, 0, 13.333, 0.12, fill=GOLD)
D.circle(s, 9.3, 1.2, 5.1, fill=NAVY2)
D.icon_badge(s, "compass", 10.6, 2.5, 2.5, bg=TEAL, ratio=0.5)
D.text(s, 0.95, 1.3, 8, 1.4, "Merci !", size=66, color=WHITE, bold=True, font=TITLE_FONT)
D.text(s, 0.95, 2.75, 7.8, 0.8, "Vous êtes désormais le PILOTE.", size=26, color=GOLD, bold=True, font=TITLE_FONT)
D.text(s, 0.95, 3.55, 7.6, 0.9, "L'IA est un copilote formidable, à condition de savoir où vous allez.", size=17, color="C9D3E6")
for i, (ic, t) in enumerate([("book-open", "Le syllabus : tout le cours, les quiz et le glossaire"), ("briefcase", "Le Kit IA : outils, prompts prêts à l'emploi"), ("flag", "Le défi de 7 jours : commencez demain")]):
    D.icon(s, ic, 0.95, 4.75 + i * 0.6, 0.38, TEAL)
    D.text(s, 1.5, 4.72 + i * 0.6, 7, 0.45, t, size=14.5, color=WHITE, anchor="m")
D.rrect(s, 0.95, 6.55, 2.6, 0.55, fill=GOLD, radius=0.5)
D.text(s, 0.95, 6.55, 2.6, 0.55, "Vos questions ?", size=14, color=NAVY, bold=True, font=TITLE_FONT, align="c", anchor="m")
N(s, "Merci et questions", 0.5,
  "« Merci pour votre énergie et votre participation. »",
  "Remerciez chaleureusement, rappelez les trois ressources remises, et ouvrez les questions s'il reste du temps (sinon, proposez de répondre individuellement après la session).",
  points=["Distribuez ou envoyez le syllabus et le Kit IA", "Invitez à commencer le défi de 7 jours dès le lendemain"])

out = os.path.join(HERE, "..", "01_PowerPoint", "IA_Prompt_Engineering_Formation.pptx")
D.prs.save(out)
json.dump(NOTES, open(os.path.join(HERE, "build", "notes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("slides:", D.count, "minutes:", sum(n["minutes"] for n in NOTES))
