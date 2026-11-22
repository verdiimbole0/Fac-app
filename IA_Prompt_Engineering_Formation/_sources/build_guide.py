# -*- coding: utf-8 -*-
"""Guide du formateur (PDF) + fichier texte des prompts de démonstration."""
import json
from docparts import *

NOTES = json.load(open(os.path.join(BUILD, "notes.json"), encoding="utf-8"))
doc = Doc("Guide du formateur — IA & Prompt Engineering appliqués aux entreprises")
B = []; br = '<div class="page-break"></div>'

def fmt(m):
    mm = int(m); ss = int(round((m - mm) * 60))
    return f"{mm}:{ss:02d}"

# ------------------------------------------------------------------ 1
B.append(section_title(doc, "Votre rôle et l'esprit de la formation", first=True, kicker="Avant tout"))
B.append(P("Ce guide vous permet d'animer la formation <strong>« IA & Prompt Engineering appliqués aux entreprises »</strong> sans avoir à improviser. Il complète les notes du présentateur intégrées au fichier PowerPoint (affichez-les en <strong>mode Présentateur</strong>) et les reprend ici sous une forme imprimable.",
 "Votre public est hétérogène : des personnes qui n'ont jamais utilisé d'IA, d'autres qui l'utilisent sans méthode, quelques utilisateurs avancés. Votre mission n'est pas d'impressionner, mais de <strong>rassurer, clarifier et faire pratiquer</strong>."))
B.append('<div class="grid g2">' + "".join(f'<div class="card"><h4 style="margin-top:0">{icon(ic, TEAL, 14)} {esc(t)}</h4><p>{esc(d)}</p></div>' for ic, t, d in [
    ("users", "Partir de leur réalité", "Chaque notion commence par une situation de travail que le public connaît (emails, comptes rendus, rapports), jamais par la technologie."),
    ("message-circle", "Faire participer", "Une question, un vote ou un mini-défi toutes les 3 à 4 minutes. Les quiz rythment la session."),
    ("compass", "Ancrer trois repères", "Le stagiaire surdoué, la méthode PILOTE, la règle Vrai ? Juste ? Signable ? Faites-les répéter."),
    ("clock", "Tenir le temps", "60 minutes, c'est court. Utilisez le conducteur minuté et le « parking » pour les questions hors sujet."),
    ("shield-check", "Rester honnête", "Pas de promesses de gains chiffrés universels, pas de prédictions alarmistes. L'IA est un outil puissant et faillible."),
    ("heart", "Valoriser", "Dédramatisez les erreurs aux quiz ; félicitez les essais. Un participant en confiance pratiquera après la session.")]) + '</div>')
B.append(box("key", P("Trois messages doivent rester après la session : <strong>1)</strong> l'IA compose des réponses plausibles, pas vérifiées ; <strong>2)</strong> la qualité de la réponse dépend de la qualité de la demande (PILOTE) ; <strong>3)</strong> l'IA prépare, l'humain vérifie et décide.")))

# ------------------------------------------------------------------ 2
B.append(section_title(doc, "Préparer la session", kicker="Logistique"))
B.append(table(["Quand ?", "À faire"], [
    ["J-7", "Confirmer la salle, le vidéoprojecteur et l'accès Internet. Demander la liste des participants et leurs fonctions pour adapter les exemples du chapitre 2. Vérifier quel assistant IA est autorisé dans l'entreprise cliente (Copilot, ChatGPT, Gemini…)."],
    ["J-2", "Répéter la présentation en entier avec un chronomètre. Faire une fois la démonstration du chapitre 4 dans l'outil choisi et conserver des captures d'écran de vos résultats (plan B supplémentaire)."],
    ["J-1", "Imprimer ou envoyer : syllabus et kit (un par participant), ce guide (pour vous). Copier le fichier « Prompts_Demonstration.txt » sur l'ordinateur de présentation."],
    ["H-30", "Installer le matériel. Ouvrir le PowerPoint en mode Présentateur. Ouvrir l'assistant IA dans un onglet, connecté, avec une conversation vierge. Tester le son et l'affichage du navigateur (zoom à 125 % pour la lisibilité)."],
    ["H-5", "Accueillir les participants. Préparer des feuilles et stylos pour les quiz et le plan d'action. Afficher la diapositive de couverture."]], ["12%", "88%"]))
B.append("<h4>Matériel nécessaire</h4>" + UL(["Ordinateur avec PowerPoint (ou LibreOffice Impress) et les polices Montserrat et Inter installées (fournies dans le dossier 06_Polices)", "Vidéoprojecteur ou grand écran, idéalement télécommande de présentation",
    "Connexion Internet et un compte sur un assistant IA (facultatif grâce au plan B)", "Syllabus et Kit IA pour chaque participant (papier ou PDF)", "Feuilles et stylos ; un tableau ou paperboard pour le « parking » à questions"]))
B.append(box("tip", P("Si les polices Montserrat et Inter ne sont pas installées sur l'ordinateur de présentation, PowerPoint les remplacera par des polices proches ; la mise en page peut alors légèrement bouger. Installez-les la veille (double-clic sur chaque fichier puis « Installer »).")))

# ------------------------------------------------------------------ 3
B.append(br + section_title(doc, "Conducteur minuté", first=True, kicker="60 minutes"))
rows, cum = [], 0.0
for n in NOTES:
    cum += n["minutes"]
    rows.append([str(n["num"]), esc(n["chapter"]), esc(n["title"]), fmt(n["minutes"]), f"<b>{fmt(cum)}</b>"])
B.append(P("Le temps cumulé vous indique où vous devez en être. Si vous avez plus de 2 minutes de retard à la fin d'un chapitre, appliquez les raccourcis proposés plus loin."))
B.append(table(["Diapo", "Partie", "Contenu", "Durée", "Cumul"], rows, ["9%", "17%", "50%", "11%", "13%"]))

# ------------------------------------------------------------------ 4
B.append(br + section_title(doc, "Notes du présentateur, diapositive par diapositive", first=True, kicker="Le déroulé"))
B.append(P("Ces notes sont identiques à celles du fichier PowerPoint. Elles indiquent ce que vous dites pour introduire chaque diapositive, ce que vous expliquez, l'exemple à raconter, la question à poser, les points à ne pas oublier et la transition."))
cur = None
for n in NOTES:
    if n["chapter"] != cur:
        cur = n["chapter"]
        B.append(f'{doc.mark(cur if cur not in ("Introduction","Conclusion") else ("Introduction (diapositives 1 à 4)" if cur=="Introduction" else "Conclusion (diapositives 57 à 60)"), 2)}<h3 style="color:#{TEAL}">{esc(cur)}</h3>')
    parts = [f'<p style="margin:2pt 0"><b>Introduire :</b> {esc(n["intro"])}</p>', f'<p style="margin:2pt 0"><b>Expliquer :</b> {esc(n["explain"])}</p>']
    if n.get("example"): parts.append(f'<p style="margin:2pt 0"><b style="color:#{NAVY}">Exemple :</b> {esc(n["example"])}</p>')
    if n.get("question"): parts.append(f'<p style="margin:2pt 0"><b style="color:#{TEAL}">Question au public :</b> {esc(n["question"])}</p>')
    if n.get("points"): parts.append(f'<p style="margin:2pt 0"><b style="color:#{RED}">À ne pas oublier :</b> {esc(" · ".join(n["points"]))}</p>')
    if n.get("transition"): parts.append(f'<p style="margin:2pt 0;color:#{MUTED}"><b>Transition :</b> <i>{esc(n["transition"])}</i></p>')
    B.append(f'<div class="avoid" style="border-left:3pt solid #{GOLD};padding:4pt 0 4pt 10pt;margin:8pt 0;font-size:8.8pt;">'
             f'<div style="display:flex;justify-content:space-between;align-items:center;"><span style="font-family:Montserrat;font-weight:700;color:#{NAVY};font-size:10pt;">Diapo {n["num"]} · {esc(n["title"])}</span>'
             f'<span class="chip" style="background:#{LIGHT};color:#{NAVY}">{icon("clock", NAVY, 10)} {fmt(n["minutes"])}</span></div>{"".join(parts)}</div>')

# ------------------------------------------------------------------ 5
B.append(br + section_title(doc, "Kit de démonstration du chapitre 4", first=True, kicker="En direct"))
B.append(P("La démonstration fonctionne dans n'importe quel assistant IA (ChatGPT, Claude, Gemini, Copilot, Le Chat). Les textes ci-dessous sont aussi dans le fichier <strong>Prompts_Demonstration.txt</strong> pour un copier-coller rapide. Restez <strong>dans la même conversation</strong> du début à la fin."))
B.append(box("warn", P("Les réponses d'une IA varient d'un essai à l'autre. Ne promettez jamais un résultat identique à celui des diapositives. Si l'IA ne commet pas l'erreur sur Marc, montrez la diapositive 44 : « Voici ce qui s'est produit lors d'un autre essai, et c'est fréquent. »"), "Point d'attention"))
B.append("<h4>Les notes brutes à coller</h4>" + f'<div class="answer" style="background:#FFFDF6;border-color:#E8DDBE;">{esc(NOTES_BRUTES)}</div>')
for lab, p in [("Étape 2 — première demande", PROMPT4_V1.replace("[COLLER LES NOTES]", "(coller les notes)")), ("Étape 5 — prompt PILOTE", PROMPT4_V2), ("Relance — email de suivi", PROMPT4_V3),
               ("Étape 8 — relance de correction (si nécessaire)", "Vérifie ton compte rendu ligne à ligne par rapport à mes notes : signale toute action, décision ou responsable qui n'y figure pas explicitement, puis corrige.")]:
    B.append(prompt(p, lab))
B.append("<h4>Démonstrations du chapitre 3 (facultatif, si vous avez de l'avance)</h4>")
for dm in DEMO3:
    B.append(prompt(dm["prompt"], dm["level"]))
B.append(doc.mark("Plan B : sans connexion ou sans outil", 2) + "<h3>Plan B : sans connexion ou sans outil</h3>")
B.append(table(["Situation", "Que faire ?"], [
    ["Pas d'Internet / outil bloqué", "Déroulez simplement les diapositives 38 à 44 : elles contiennent les prompts et les résultats. Faites deviner au public la réponse de l'IA avant de l'afficher : l'interaction reste intacte."],
    ["L'outil est lent", "Lancez la requête, puis commentez la diapositive suivante pendant la génération ; revenez à l'outil ensuite."],
    ["Réponse très différente", "Utilisez-la comme matière : « Voyons ce qui manque » (étape 4). La démarche reste la même."],
    ["L'IA refuse ou plante", "« Cela arrive : c'est aussi pour cela qu'on garde la main. » Passez aux diapositives."],
    ["Retard de plus de 3 minutes", "Ne faites pas la démonstration en direct : diapositives uniquement."]], ["28%", "72%"]))

# ------------------------------------------------------------------ 6
B.append(br + section_title(doc, "Animer les quiz", first=True, kicker="Rythme"))
B.append(P("Chaque chapitre se termine par une séquence de trois diapositives : <strong>remerciement</strong> (15 s), <strong>questions</strong> (1 min), <strong>corrigé</strong> (1 min). Laissez réfléchir en silence, faites voter à main levée sur au moins une question, puis expliquez le corrigé : l'explication compte plus que la lettre."))
B.append(UL(["<b>Variante ludique :</b> faites lever 1, 2, 3 ou 4 doigts pour A, B, C ou D.", "<b>Grand groupe :</b> utilisez un outil de vote en ligne si l'entreprise en dispose ; sinon, main levée.",
             "<b>En distanciel :</b> les participants répondent dans la discussion (« Q1 : B »).", "<b>Erreurs fréquentes :</b> reprenez l'idée clé en 20 secondes, sans insister sur la personne."]))
B.append(doc.mark("Grille des réponses", 2) + "<h3>Grille des réponses</h3>")
B.append(table(["Chapitre", "Q1", "Q2", "Q3", "Idée clé à rappeler"], [
    [f"<b>{n}</b>"] + [f'<b style="color:#{TEAL}">{"ABCD"[q["answer"]]}</b>' for q in QUIZZES[n]["questions"]] + [esc(CHAPTERS[n - 1]["message"])] for n in range(1, 6)], ["12%", "7%", "7%", "7%", "67%"]))

# ------------------------------------------------------------------ 7
B.append(section_title(doc, "Répondre aux questions difficiles", kicker="FAQ du formateur"))
faq = [
 ("« L'IA va-t-elle remplacer mon emploi ? »", "Restez factuel et nuancé : l'IA transforme surtout des tâches (rédaction, synthèse, recherche) plutôt que des métiers entiers ; elle déplace la valeur vers le cadrage, la vérification, la relation et la décision. Ceux qui savent l'utiliser avec méthode renforcent leur position. Évitez les prédictions chiffrées."),
 ("« Quel outil dois-je utiliser ? »", "D'abord celui que votre entreprise autorise (souvent Copilot avec un compte professionnel, ou une version entreprise d'un autre assistant). La méthode PILOTE fonctionne avec tous. Le Kit IA présente 18 outils par besoin."),
 ("« C'est gratuit ? »", "La plupart des assistants proposent une version gratuite limitée et des offres payantes (environ 20 $ par mois pour un usage individuel avancé, davantage pour les offres entreprise). Les tarifs évoluent : renvoyez vers le kit et les pages officielles."),
 ("« Mes données sont-elles en sécurité ? »", "Cela dépend de l'outil, de la version et des paramètres. Les offres professionnelles prévoient en général des engagements contractuels plus protecteurs. Règle simple : feu tricolore, anonymisation, outils validés. Pour les questions juridiques précises, renvoyez vers le DPO ou le service juridique."),
 ("« L'IA m'a donné une réponse fausse, donc elle est nulle ? »", "C'est exactement le chapitre 1 : elle vise le plausible. Elle reste extraordinairement utile pour rédiger, structurer, reformuler, à condition de vérifier les faits."),
 ("« Faut-il dire que j'ai utilisé l'IA ? »", "Suivez la politique de votre entreprise et le contexte (client, publication, document officiel). Dans tous les cas, vous restez l'auteur responsable du contenu diffusé."),
 ("« Peut-on lui faire confiance pour des calculs ? »", "Les assistants récents utilisent souvent des outils de calcul, mais il faut toujours vérifier les chiffres importants, idéalement dans un tableur."),
 ("Question très technique ou hors sujet", "Notez-la sur le « parking » et proposez d'y répondre après la session. Protégez le temps du groupe.")]
for q, a in faq:
    B.append(f'<div class="avoid" style="margin:7pt 0;"><h4 style="margin-bottom:2pt;color:#{TEAL}">{esc(q)}</h4><p>{esc(a)}</p></div>')

# ------------------------------------------------------------------ 8
B.append(br + section_title(doc, "Adapter la formation", first=True, kicker="Variantes"))
B.append(table(["Situation", "Adaptation recommandée"], [
    ["Public de débutants complets", "Ralentissez au chapitre 1 (+2 min) ; au chapitre 3, ne présentez en détail que 2 démonstrations sur 3 (la faible et la PILOTE)."],
    ["Public déjà utilisateur", "Passez plus vite sur le chapitre 1 ; insistez sur les techniques avancées (syllabus 3.6), l'itération et la vérification."],
    ["Public d'une seule fonction (ex. RH)", "Remplacez les exemples du chapitre 2 par les cas de cette fonction (syllabus 2.2) et adaptez l'atelier (ex. : préparer un entretien)."],
    ["Dirigeants", "Insistez sur la règle d'or, la confidentialité, la charte d'usage et la montée en compétence des équipes."],
    ["Distanciel", "Partagez votre écran ; remplacez les votes à main levée par la discussion ; prévoyez une pause active de 30 secondes au milieu."],
    ["Groupe de plus de 30 personnes", "Faites voter uniquement à main levée, sans recueillir d'interventions orales sur chaque question."],
    ["Version 90 minutes", "Ajoutez 20 minutes de pratique individuelle après le chapitre 4 (chacun applique PILOTE à une de ses tâches) et 10 minutes de questions."]], ["30%", "70%"]))
B.append("<h4>Raccourcis si vous êtes en retard</h4>" + UL([
    "Chapitre 2 : ne présentez qu'une situation Avant/Après sur trois (2 min gagnées).",
    "Chapitre 3 : regroupez les démonstrations 1 et 2 (1 min gagnée).",
    "Chapitre 4 : pas de démonstration en direct, diapositives uniquement (2 à 3 min gagnées).",
    "Chapitre 5 : diapositive des 10 réflexes en 20 secondes (renvoyer au kit).",
    "Ne supprimez jamais : la méthode PILOTE, l'étape 8 de vérification, le feu tricolore et le plan d'action."]))

# ------------------------------------------------------------------ 9
B.append(section_title(doc, "Après la formation", kicker="Suivi"))
B.append(UL(["Envoyez le jour même le syllabus et le kit en PDF, avec un message rappelant le défi de 7 jours.",
             "Proposez un court retour d'expérience une à deux semaines plus tard (30 minutes) : chacun partage une réussite et un prompt.",
             "Invitez l'équipe à constituer une bibliothèque de prompts partagée.",
             "Recueillez l'évaluation à chaud : utilité perçue, clarté, envie d'aller plus loin. Améliorez la session suivante en conséquence."]))
B.append(box("tip", P("La meilleure preuve de réussite n'est pas la note de satisfaction, mais le nombre de participants qui utilisent la méthode PILOTE une semaine plus tard. Posez la question lors du retour d'expérience.")))

def body(toc): return '<h2 class="first">Sommaire</h2>' + toc + br + "".join(B)
cov = cover("Guide du formateur", 'Guide du formateur <span style="color:#' + GOLD + '">IA &amp; Prompt Engineering</span>',
            "Préparer, animer et chronométrer la formation de 60 minutes, diapositive par diapositive.",
            [("clock", "Conducteur minuté sur 60 minutes"), ("presentation", "Notes détaillées pour les 60 diapositives"), ("sparkles", "Kit de démonstration et plan B"), ("message-circle", "FAQ et adaptations du public")], ic="presentation")
build(doc, cov, body, os.path.join(HERE, "..", "04_Formateur", "Guide_Formateur.pdf"), "GUIDE DU FORMATEUR · IA &amp; PROMPT ENGINEERING")

# fichier texte des prompts
txt = ["PROMPTS DE DÉMONSTRATION — Formation IA & Prompt Engineering", "=" * 64, "", "Restez dans la même conversation du début à la fin de l'atelier.", "",
       "---- NOTES BRUTES (à coller après le prompt de l'étape 2 ou à la place de [COLLER LES NOTES]) ----", NOTES_BRUTES, "",
       "---- ÉTAPE 2 : PREMIÈRE DEMANDE ----", "Fais un compte rendu de cette réunion :", NOTES_BRUTES, "",
       "---- ÉTAPE 5 : PROMPT PILOTE ----", PROMPT4_V2.replace("[COLLER LES NOTES]", "\n" + NOTES_BRUTES), "",
       "---- RELANCE : EMAIL DE SUIVI ----", PROMPT4_V3, "",
       "---- ÉTAPE 8 : RELANCE DE CORRECTION ----", "Vérifie ton compte rendu ligne à ligne par rapport à mes notes : signale toute action, décision ou responsable qui n'y figure pas explicitement, puis corrige.", "",
       "---- CHAPITRE 3 (facultatif) ----"] + sum([[f"[{d['level']}]", d["prompt"], ""] for d in DEMO3], [])
open(os.path.join(HERE, "..", "04_Formateur", "Prompts_Demonstration.txt"), "w", encoding="utf-8").write("\n".join(txt))
