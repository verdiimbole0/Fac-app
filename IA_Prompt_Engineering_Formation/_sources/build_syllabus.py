# -*- coding: utf-8 -*-
"""Syllabus / guide pédagogique complet (PDF)."""
from docparts import *
from kitdata import PROMPT_GROUPS, ERRORS

doc = Doc("Syllabus — IA & Prompt Engineering appliqués aux entreprises")
B = []  # corps
br = '<div class="page-break"></div>'

# ------------------------------------------------------------------ INTRO
B.append(section_title(doc, "Message d'introduction", first=True, kicker="Bienvenue"))
B.append(P(
 "Vous tenez entre les mains le document de référence de la formation <strong>« IA & Prompt Engineering appliqués aux entreprises »</strong>. "
 "Pendant la session, le diaporama vous a montré l'essentiel. Ce syllabus va plus loin : il explique, détaille, illustre et vous donne de quoi pratiquer seul, à votre rythme.",
 "Peut-être pensiez-vous que l'intelligence artificielle était réservée aux informaticiens. Peut-être l'avez-vous déjà essayée, avec des résultats décevants ou au contraire bluffants, sans bien comprendre pourquoi. "
 "Dans tous les cas, ce document a été conçu pour vous permettre de passer d'une <strong>utilisation au hasard</strong> à une <strong>utilisation maîtrisée</strong> : savoir ce que l'IA fait réellement, quand l'utiliser, comment lui parler et comment vérifier ce qu'elle produit.",
 "Relisez-le dans quelques jours, puis dans quelques semaines. Chaque chapitre se termine par un quiz corrigé, et vous trouverez à la fin un glossaire, une fiche de révision express et un plan d'action personnel. "
 "Le <strong>Kit IA du professionnel moderne</strong>, remis avec ce syllabus, complète l'ensemble avec une sélection d'outils, plus de vingt prompts prêts à l'emploi et un défi pratique de 7 jours."))
B.append(box("tip", P("Ne cherchez pas à tout retenir. Retenez <strong>une image</strong> (le stagiaire surdoué), <strong>une méthode</strong> (PILOTE) et <strong>une règle</strong> (Vrai ? Juste ? Signable ?). Le reste viendra avec la pratique."), "Le conseil du formateur"))
B.append(f'<h3>Comment utiliser ce document</h3>')
B.append(table(["Repère", "Signification"], [
    [f'{icon("badge-check", TEAL, 13)} À retenir', "L'idée essentielle à mémoriser."],
    [f'{icon("briefcase", NAVY, 13)} Exemple concret', "Une situation d'entreprise pour illustrer la notion."],
    [f'{icon("triangle-alert", RED, 13)} Erreur à éviter', "Le piège le plus fréquent sur ce point."],
    [f'{icon("lightbulb", GOLD, 13)} Conseil du formateur', "Une astuce issue de l'expérience terrain."],
    [f'{icon("notebook-pen", TEAL, 13)} À vous de jouer', "Un exercice court à faire seul ou en équipe."],
    ['<span style="background:#0E2449;color:#fff;padding:1pt 5pt;border-radius:3pt;font-size:8pt;">PROMPT</span>', "Un prompt à copier-coller ; les éléments entre [CROCHETS] sont à remplacer."]], ["32%", "68%"]))
B.append(br)

B.append(section_title(doc, "Présentation de la formation", kicker="Le cadre"))
B.append(P("Cette formation d'une heure est une initiation <strong>pratique</strong> à l'intelligence artificielle générative et au Prompt Engineering, c'est-à-dire l'art de formuler des demandes efficaces à une IA. "
           "Elle ne demande aucune compétence technique. Elle part des tâches que vous réalisez chaque jour (écrire, résumer, organiser, analyser, préparer) et montre comment l'IA peut vous aider à les accomplir plus vite et mieux, sans renoncer à votre jugement."))
B.append('<div class="grid g2">')
B.append('<div class="card"><h4>' + icon("users", TEAL, 15) + ' À qui s\'adresse cette formation ?</h4>' + UL([
    "Salariés de tous services, assistants et responsables administratifs", "Comptables, contrôleurs de gestion, financiers", "Commerciaux, chargés de relation client, marketeurs",
    "Responsables RH, managers, dirigeants, entrepreneurs", "Consultants, étudiants, toute personne qui découvre l'IA"]) + '</div>')
B.append('<div class="card"><h4>' + icon("circle-check", TEAL, 15) + ' Prérequis</h4>' + UL([
    "Aucune connaissance en informatique ou en IA", "Savoir utiliser un navigateur web et une messagerie", "Facultatif : un compte gratuit sur un assistant IA (ChatGPT, Claude, Gemini, Copilot ou Le Chat) pour pratiquer après la session",
    "Une curiosité et l'envie d'essayer"]) + '</div></div>')
B.append("<h3>Objectifs généraux</h3>" + UL([
    "Comprendre ce qu'est l'IA générative, ce qu'elle sait faire et ses limites.",
    "Identifier des usages concrets et pertinents de l'IA dans son propre métier.",
    "Savoir formuler des demandes efficaces et améliorer les réponses par itération.",
    "Utiliser l'IA de manière responsable : vérification, confidentialité, jugement humain."]))
B.append("<h3>Objectifs spécifiques et compétences visées</h3>")
B.append(table(["Compétence", "À l'issue de la formation, le participant est capable de…", "Chapitre"], [
    ["Comprendre", "Expliquer avec ses mots le fonctionnement d'un modèle de langage et la notion d'hallucination", "1"],
    ["Choisir", "Distinguer les situations où utiliser un moteur de recherche, un assistant IA ou un outil spécialisé", "1, 2"],
    ["Identifier", "Repérer au moins trois tâches de son métier où l'IA apporte un gain réel", "2"],
    ["Formuler", "Rédiger un prompt structuré avec la méthode PILOTE et doser son niveau de détail", "3"],
    ["Itérer", "Améliorer une réponse par des relances ciblées dans une même conversation", "3, 4"],
    ["Produire", "Mener une tâche complète (notes → compte rendu → plan d'action → email) avec l'IA", "4"],
    ["Vérifier", "Contrôler une réponse avec la règle Vrai ? Juste ? Signable ?", "4, 5"],
    ["Protéger", "Classer une information selon le feu tricolore des données et l'anonymiser", "5"]], ["16%", "70%", "14%"]))
B.append("<h3>Résultats attendus</h3>" + P("À la fin de la session, chaque participant repart avec : une compréhension claire et démystifiée de l'IA ; une méthode de formulation réutilisable dans tous les métiers ; l'expérience d'un cas pratique complet ; des réflexes de sécurité ; un plan d'action personnel de trois tâches ; un kit d'outils et de prompts pour passer à l'action dès le lendemain."))
B.append(br)

B.append(section_title(doc, "Vue d'ensemble du parcours", kicker="Le programme"))
cards = ""
for ch, (t, m, d) in zip(CHAPTERS, TIMING[1:6]):
    cards += (f'<div class="card" style="display:flex;gap:10pt;align-items:flex-start;">{badge(ch["icon"], TEAL if ch["n"]%2 else NAVY, "FFFFFF", 34)}'
              f'<div><div class="kicker">Chapitre {ch["n"]} · {m} min</div><h4 style="margin:2pt 0 3pt 0;">{esc(ch["title"])}</h4><p>{esc(ch["message"])}</p></div></div>')
B.append(f'<div class="grid" style="grid-template-columns:1fr;gap:6pt;">{cards}</div>')
B.append(doc.mark("Programme chronométré de 60 minutes", 2) + "<h3>Programme chronométré de 60 minutes</h3>")
rows, t0 = [], 0
detail = {
 0: "Accroche (temps passé sur les emails), objectifs, programme",
 1: "Les mots justes · l'autocomplétion géante · le stagiaire surdoué · moteur de recherche vs assistant · forces et limites · quiz",
 2: "Les 6 super-pouvoirs · exemples par fonction · 3 situations Avant/Après · la règle d'or · quiz",
 3: "Vote A/B · 4 erreurs · méthode PILOTE · prompt simple ou structuré · 3 démonstrations · comparaison · itération · quiz",
 4: "Scénario Nova Distribution · démarche en 8 étapes · 1re demande · prompt PILOTE · résultat · email de suivi · vérification · quiz",
 5: "Hallucinations · feu tricolore des données · droits, biais, dépendance · Vrai ? Juste ? Signable ? · 10 réflexes · quiz",
 6: "Récapitulatif en 5 phrases · plan d'action personnel · ouverture · remerciements"}
for i, (t, m, d) in enumerate(TIMING):
    rows.append([f"{t0:02d}:00 – {t0+m:02d}:00", f"<b>{esc(t)}</b>", f"{m} min", esc(detail[i])]); t0 += m
rows.append(["", "<b>Total</b>", "<b>60 min</b>", "Dont 5 quiz de 3 questions avec corrigés expliqués (≈ 2 min 30 chacun)"])
B.append(table(["Horaire", "Séquence", "Durée", "Contenu"], rows, ["15%", "28%", "9%", "48%"]))
B.append(box("tip", P("La durée de 60 minutes inclut les interactions et les quiz. Le chapitre 3 (méthode) et le chapitre 4 (atelier) représentent près de la moitié du temps : c'est là que se construit la compétence.")))

# ------------------------------------------------------------------ CHAPITRE 1
ch = CHAPTERS[0]
B.append(chapter_opener(doc, ch, 9, ["Les mots justes : IA, IA générative, modèle de langage", "Comment fonctionne un assistant IA", "L'analogie du stagiaire surdoué", "Dialoguer avec une IA", "Ce qu'elle sait faire, ce qu'elle ne sait pas faire", "Moteur de recherche ou assistant IA ?"]))
B.append('<h3 style="margin-top:0"><span class="num">1.1</span>Qu\'est-ce que l\'intelligence artificielle ?</h3>')
B.append(P("L'<strong>intelligence artificielle (IA)</strong> désigne l'ensemble des techniques qui permettent à une machine de réaliser des tâches qui demandent habituellement l'intelligence humaine : reconnaître une image, comprendre une phrase, prédire un comportement, prendre une décision simple, produire un texte.",
 "Vous l'utilisez déjà depuis des années, souvent sans le savoir : le filtre anti-spam de votre messagerie, le GPS qui vous fait éviter un bouchon, les recommandations de films ou de produits, la reconnaissance faciale de votre téléphone. Ces IA « classiques » <strong>reconnaissent, classent et prédisent</strong>.",
 "La plupart reposent sur l'<strong>apprentissage automatique</strong> (<em>machine learning</em>) : plutôt que de programmer chaque règle à la main, on montre à la machine une grande quantité d'exemples et elle apprend à en dégager des régularités."))
B.append('<h3><span class="num">1.2</span>Qu\'est-ce que l\'IA générative ?</h3>')
B.append(P("L'<strong>IA générative</strong> est une branche de l'IA capable de <strong>produire un contenu nouveau</strong> — un texte, une image, un son, une vidéo, du code — à partir d'une demande formulée en langage courant. C'est elle qui a popularisé l'IA auprès du grand public à partir de fin 2022.",
 "Pour le texte, elle repose sur des <strong>modèles de langage</strong> (en anglais <em>Large Language Models</em>, LLM). Ce sont eux qui font fonctionner ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google), Copilot (Microsoft) ou Le Chat (Mistral AI)."))
B.append(table(["", "IA « classique »", "IA générative"], [
    ["Ce qu'elle fait", "Reconnaît, classe, prédit", "Produit un contenu nouveau"],
    ["Exemple personnel", "Filtre anti-spam, GPS", "Rédiger un message d'anniversaire original"],
    ["Exemple professionnel", "Détection de fraude, prévision des ventes", "Rédiger un compte rendu, résumer un rapport"],
    ["Comment on l'utilise", "Souvent invisible, intégrée aux logiciels", "On lui parle : on lui donne des instructions (prompts)"]], ["24%", "38%", "38%"]))
B.append('<h3><span class="num">1.3</span>Comment fonctionne un assistant IA ? L\'autocomplétion géante</h3>')
B.append(P("Vous connaissez la saisie prédictive de votre téléphone, qui propose le mot suivant pendant que vous tapez un message. Un modèle de langage fonctionne sur un principe comparable, à une échelle gigantesque et avec une sophistication bien plus grande.",
 "<strong>1. L'entraînement.</strong> Le modèle a été entraîné sur d'immenses volumes de textes. Il en a retenu, sous forme statistique, la manière dont les mots, les idées et les raisonnements s'enchaînent habituellement.",
 "<strong>2. La prédiction.</strong> Quand vous lui écrivez, il compose sa réponse <strong>morceau de mot après morceau de mot</strong> (ces morceaux s'appellent des <em>tokens</em>), en choisissant à chaque fois une suite plausible compte tenu de tout ce qui précède.",
 "<strong>3. Votre prompt est le début du texte.</strong> Tout ce que vous écrivez oriente la suite. Plus votre demande est précise, plus la suite la plus probable correspond à ce que vous voulez. C'est le fondement même du Prompt Engineering."))
B.append(box("ex", P("Complétez : « Je vous remercie pour votre… ». Vous avez probablement pensé « confiance », « message » ou « patience ». Vous venez de faire, en miniature, ce que fait le modèle : choisir la suite la plus probable. Ajoutez du contexte — « Suite à votre commande, je vous remercie pour votre… » — et la probabilité de « commande » ou « confiance » change. Le contexte guide la prédiction.")))
B.append(box("key", P("Une IA générative ne cherche pas la réponse dans une base de données : <strong>elle la compose</strong>. C'est pour cela qu'elle rédige si bien… et c'est aussi pour cela qu'elle peut se tromper avec aplomb : elle vise une réponse <strong>plausible</strong>, pas une réponse <strong>vérifiée</strong>.")))
B.append(P("Les modèles actuels sont bien plus que de simples prédicteurs de mots : ils ont été affinés pour suivre des instructions, raisonner par étapes, utiliser des outils (recherche web, calcul, lecture de fichiers). Mais le principe de prédiction reste au cœur de leur fonctionnement, et il explique la plupart de leurs forces comme de leurs faiblesses. "
 "Il faut aussi éviter l'excès inverse : <strong>l'IA ne pense pas et ne comprend pas comme un être humain</strong>. Elle n'a ni intentions, ni expérience du monde, ni conscience de ce qui est vrai."))
B.append('<h3><span class="num">1.4</span>L\'analogie à retenir : le stagiaire surdoué</h3>')
B.append(P("Imaginez un nouveau stagiaire. Il a lu une bibliothèque entière, écrit vite et bien dans toutes les langues, ne se fatigue jamais. Mais il est arrivé ce matin : il ne connaît ni votre entreprise, ni vos clients, ni vos règles. Et il a un petit défaut : plutôt que d'avouer qu'il ne sait pas, il préfère proposer une réponse qui a l'air juste."))
B.append(table(["Le stagiaire surdoué…", "Conséquence pour vous"], [
    ["A une culture immense", "Il peut vous aider sur presque tous les sujets : rédaction, synthèse, explication, idées."],
    ["Écrit vite, dans le ton demandé", "Il vous fait gagner le temps du premier jet."],
    ["Ne connaît pas votre contexte", "Vous devez le briefer : situation, destinataire, objectif, contraintes (chapitre 3)."],
    ["N'aime pas dire « je ne sais pas »", "Vous devez vérifier ce qu'il produit, surtout les faits et les chiffres (chapitre 5)."]], ["40%", "60%"]))
B.append(box("tip", P("Avant d'envoyer une demande à l'IA, demandez-vous : « Est-ce que je dirais cela de cette façon à un stagiaire arrivé ce matin ? » Si la réponse est non, ajoutez du contexte.")))
B.append('<h3><span class="num">1.5</span>Que signifie « dialoguer » avec une IA ?</h3>')
B.append(P("Un assistant IA fonctionne en <strong>conversation</strong>. Dans une même conversation, il « voit » tout ce qui a été échangé : vos messages, les documents fournis, ses propres réponses. C'est ce qu'on appelle la <strong>fenêtre de contexte</strong>. Elle est grande, mais limitée.",
 "Conséquences pratiques : vous pouvez <strong>corriger et préciser</strong> sans tout répéter (« plus court », « en tableau », « pour un client ») ; une <strong>nouvelle conversation repart de zéro</strong>, sauf si l'outil propose une mémoire ou des « projets » que vous avez configurés ; dans une très longue conversation, les éléments du début peuvent être moins bien pris en compte. Pour un nouveau sujet, ouvrez une nouvelle conversation."))
B.append('<h3><span class="num">1.6</span>Ce que l\'IA sait faire… et ce qu\'elle ne sait pas faire</h3>')
B.append('<div class="grid g2"><div class="card" style="border-top:3pt solid #' + TEAL + '"><h4 style="color:#' + TEAL + '">Elle sait très bien</h4>' + UL([
    "Rédiger, reformuler, adapter le ton", "Résumer de longs textes", "Traduire", "Structurer des idées, des plans, des tableaux", "Générer des idées en quantité", "Expliquer simplement un sujet complexe", "Analyser un texte ou des données que vous lui fournissez", "Jouer un rôle pour vous entraîner (client difficile, recruteur…)"]) +
    '</div><div class="card" style="border-top:3pt solid #' + RED + '"><h4 style="color:#' + RED + '">Elle ne sait pas</h4>' + UL([
    "Garantir l'exactitude de ses réponses", "Connaître vos données internes si vous ne les fournissez pas", "Être à jour sans accès à des sources récentes (ses connaissances s'arrêtent à la date de son entraînement)", "Faire des calculs complexes sans risque d'erreur (sauf outil de calcul intégré, et même alors : vérifiez)", "Exercer un jugement moral ou prendre une responsabilité", "Comprendre le monde comme un être humain"]) + '</div></div>')
B.append('<h3><span class="num">1.7</span>Pourquoi l\'IA peut-elle se tromper ?</h3>')
B.append(UL(["<strong>Elle vise le plausible.</strong> Une phrase peut être grammaticalement parfaite, cohérente… et fausse.",
             "<strong>Elle comble les vides.</strong> Si une information manque, elle peut en produire une qui « a l'air juste » : un nom, une date, une source. C'est l'<strong>hallucination</strong>.",
             "<strong>Ses connaissances sont datées.</strong> Sans recherche web, elle ignore les événements postérieurs à son entraînement.",
             "<strong>Elle hérite des biais de ses données.</strong> Stéréotypes, points de vue sur-représentés, angles morts.",
             "<strong>Elle dépend de votre demande.</strong> Une question ambiguë produit une réponse approximative."]))
B.append(box("warn", P("Croire qu'une réponse est exacte parce qu'elle est bien écrite et détaillée. La qualité de la forme ne garantit jamais la qualité du fond.")))
B.append('<h3><span class="num">1.8</span>Moteur de recherche ou assistant IA ?</h3>')
B.append(table(["", "Moteur de recherche", "Assistant IA"], [
    ["Ce qu'il fait", "Trouve des pages qui existent déjà", "Compose une réponse nouvelle"],
    ["Ce que vous obtenez", "Une liste de liens à lire", "Un texte structuré, prêt à retravailler"],
    ["Point fort", "Sources identifiées, informations récentes", "Synthèse, rédaction, reformulation, dialogue"],
    ["Point de vigilance", "C'est vous qui lisez, triez et synthétisez", "Peut se tromper ; pas toujours à jour sans accès web"],
    ["Idéal pour", "Vérifier un fait, trouver un site officiel, un horaire, un texte de loi", "Rédiger, résumer, structurer, réfléchir, s'entraîner"]], ["22%", "39%", "39%"]))
B.append(P("Aujourd'hui, la frontière s'estompe : de nombreux assistants peuvent effectuer une recherche web et citer leurs sources (ChatGPT, Gemini, Claude, Copilot, Le Chat), et des outils comme Perplexity sont spécialisés dans les réponses sourcées. "
           "Le bon réflexe reste le même : pour une information <strong>factuelle, récente ou chiffrée</strong>, on remonte à la source et on l'ouvre."))
B.append(box("ask", P("Pour chacune de ces demandes, choisiriez-vous un moteur de recherche ou un assistant IA ? 1) Connaître le taux de TVA applicable à un service. 2) Rédiger un courrier de relance aimable. 3) Résumer un article de 10 pages. 4) Trouver l'adresse d'un fournisseur.",
    "<em>Réponses : 1) source officielle (moteur de recherche ou assistant qui cite des sources officielles, puis vérification) ; 2) assistant IA ; 3) assistant IA ; 4) moteur de recherche.</em>")))
B.append(br + quiz_html(1, doc) + br + corr_html(1, doc))

# ------------------------------------------------------------------ CHAPITRE 2
ch = CHAPTERS[1]
B.append(chapter_opener(doc, ch, 9, ["Les 6 super-pouvoirs de l'IA au quotidien", "Des cas concrets dans 10 fonctions de l'entreprise", "Trois situations Avant / Après détaillées", "La règle d'or : l'IA prépare, l'humain décide"]))
B.append('<h3 style="margin-top:0"><span class="num">2.1</span>Les 6 super-pouvoirs utiles au quotidien</h3>')
B.append(P("Presque tous les usages professionnels de l'IA générative entrent dans six familles. Les connaître vous aide à repérer, dans votre propre travail, les tâches où elle peut intervenir."))
B.append(table(["Super-pouvoir", "Ce que l'IA fait", "Exemples"], [
    ["Rédiger", "Produit un premier jet dans le ton voulu", "Emails, courriers, posts, procédures, annonces"],
    ["Résumer", "Condense et hiérarchise l'information", "Rapports, réunions, longues chaînes d'emails"],
    ["Reformuler et traduire", "Adapte le style, simplifie, traduit", "Rendre un texte plus clair, plus diplomate, en anglais"],
    ["Structurer", "Organise des idées en plan, tableau, liste", "Plans de rapport, check-lists, plannings, tableaux d'actions"],
    ["Analyser", "Repère tendances, écarts, causes possibles", "Données fournies, résultats d'enquête, comparaison d'offres"],
    ["Imaginer", "Génère des idées et des scénarios", "Noms, campagnes, objections clients, solutions à un problème"]], ["20%", "38%", "42%"]))
B.append('<h3><span class="num">2.2</span>Des cas concrets dans chaque fonction</h3>')
B.append(P("Pour chaque fonction, voici une tâche réelle, le problème initial, la façon dont l'IA intervient, le résultat possible et le point de vigilance."))
cases = [
 ("Administration", "Rédiger une procédure à partir de consignes orales.", "Les consignes sont dispersées et la procédure n'est jamais écrite.", "Vous dictez ou collez les consignes ; l'IA propose une procédure en étapes numérotées avec les points de contrôle.", "Une procédure claire, diffusable après validation.", "Faire valider par la personne qui réalise réellement la tâche."),
 ("Comptabilité & finance", "Commenter un écart budgétaire.", "Les chiffres sont là, mais le commentaire prend du temps.", "Vous fournissez budget et réalisé agrégés ; l'IA calcule les écarts et propose des hypothèses.", "Une note de 10 lignes pour la direction.", "Recalculer les écarts ; valider les causes réelles ; pas de données nominatives."),
 ("Ressources humaines", "Préparer un recrutement.", "Annonce à rédiger, questions d'entretien à structurer.", "L'IA rédige une fiche de poste inclusive et une grille d'entretien avec critères.", "Un processus plus structuré et plus équitable.", "La décision de recrutement reste humaine ; ne jamais soumettre de CV nominatifs à un outil non validé."),
 ("Marketing & communication", "Décliner un message sur plusieurs canaux.", "Le même message doit être adapté à LinkedIn, à la newsletter et au site.", "L'IA propose trois versions adaptées à chaque canal.", "Une communication cohérente et régulière.", "Vérifier les informations, respecter la charte et le ton de la marque."),
 ("Vente & relation client", "Préparer les réponses aux objections.", "Les commerciaux improvisent face aux mêmes objections.", "L'IA liste les objections probables et propose des réponses, puis joue le client.", "Des commerciaux mieux préparés.", "Ne pas promettre ce que l'offre ne permet pas."),
 ("Direction & management", "Préparer une décision.", "Trois rapports à lire avant le comité.", "L'IA produit une note de synthèse comparative d'une page.", "Une décision mieux préparée, plus vite.", "Lire les passages clés des originaux ; la décision reste celle du dirigeant."),
 ("Gestion de projet", "Suivre les actions d'un projet.", "Les comptes rendus ne débouchent pas sur des actions claires.", "L'IA transforme les notes en tableau « action / responsable / échéance ».", "Un suivi plus rigoureux.", "Vérifier que chaque action a bien été décidée (voir chapitre 4)."),
 ("Entrepreneuriat", "Tester une idée d'offre.", "Difficile de prendre du recul sur son propre projet.", "L'IA joue trois profils de clients types et formule leurs objections.", "Une offre affinée avant d'aller sur le terrain.", "Rien ne remplace de vrais échanges avec de vrais clients."),
 ("Recherche & analyse", "Comparer des fournisseurs.", "Les informations sont hétérogènes et difficiles à comparer.", "L'IA construit une grille de comparaison sur des critères définis.", "Un choix argumenté et traçable.", "Vérifier les informations factuelles auprès des fournisseurs."),
 ("Formation & apprentissage", "Monter en compétence sur un sujet nouveau.", "Manque de temps et de méthode pour apprendre.", "L'IA explique, donne des exemples de votre métier et vous interroge.", "Un apprentissage personnalisé et actif.", "Croiser avec des sources fiables pour les notions techniques ou réglementaires.")]
B.append(table(["Fonction", "Tâche · problème initial", "Intervention de l'IA → résultat", "Vigilance"],
               [[f"<b>{a}</b>", f"<b>{b}</b><br>{c}", f"{d}<br><span style='color:#{TEAL};font-weight:600'>→ {e}</span>", f]
                for a, b, c, d, e, f in cases], ["16%", "27%", "33%", "24%"]))
B.append('<h3><span class="num">2.3</span>Trois situations Avant / Après</h3>')
for ba in BEFORE_AFTER:
    B.append(f'<div class="avoid"><h4>{esc(ba["title"])}</h4><div class="grid g2" style="margin:4pt 0;">'
             f'<div class="card" style="border-top:3pt solid #{RED}"><div class="kicker" style="color:#{RED}">Avant</div>{UL([esc(x) for x in ba["before"]])}</div>'
             f'<div class="card" style="border-top:3pt solid #{TEAL};background:#E6F4F2"><div class="kicker" style="color:#{TEAL}">Après, avec l\'IA</div>{UL([esc(x) for x in ba["after"]])}</div></div>'
             f'{prompt(ba["prompt"], "Le prompt utilisé")}</div>')
B.append(P('<span class="small">* Durées purement illustratives : le gain réel varie selon la personne, la tâche et la qualité des données fournies. Il n\'existe pas de gain de temps « universel ».</span>'))
B.append('<h3><span class="num">2.4</span>La règle d\'or : l\'IA prépare, l\'humain décide</h3>')
B.append(table(["Étape", "Qui ?", "Ce qui se passe"], [
    ["1. Cadrer", "Vous", "Vous définissez le contexte, l'objectif, les données utiles, les contraintes."],
    ["2. Produire", "L'IA", "Elle propose un premier jet, des options, une structure."],
    ["3. Vérifier", "Vous", "Vous contrôlez les faits, les chiffres, la pertinence, le ton."],
    ["4. Décider", "Vous", "Vous ajustez, validez, assumez et diffusez."]], ["18%", "12%", "70%"]))
B.append(box("key", P("Trois étapes sur quatre restent humaines. L'IA accélère la production ; votre valeur se déplace vers le <strong>cadrage</strong>, le <strong>contrôle</strong> et la <strong>décision</strong>. Les décisions qui concernent des personnes (recrutement, évaluation, sanction) ou qui engagent l'entreprise ne doivent jamais être déléguées à une IA.")))
B.append(box("ask", P("Listez trois tâches que vous réalisez chaque semaine. Pour chacune, notez : le super-pouvoir concerné, le temps passé, et ce que vous pourriez fournir à l'IA comme contexte. Vous les reprendrez dans votre plan d'action personnel.")))
B.append(br + quiz_html(2, doc) + br + corr_html(2, doc))

# ------------------------------------------------------------------ CHAPITRE 3
ch = CHAPTERS[2]
B.append(chapter_opener(doc, ch, 14, ["Qu'est-ce qu'un prompt et pourquoi sa qualité compte", "Les 4 erreurs les plus fréquentes", "La méthode PILOTE, lettre par lettre", "Prompt simple ou prompt structuré ?", "Trois démonstrations commentées", "Techniques avancées et itération"]))
B.append('<h3 style="margin-top:0"><span class="num">3.1</span>Qu\'est-ce qu\'un prompt ?</h3>')
B.append(P("Un <strong>prompt</strong> est l'instruction, la question ou la demande que vous adressez à une IA. Le <strong>Prompt Engineering</strong> est simplement l'art de formuler ces demandes de manière claire et structurée pour obtenir des réponses utiles. Le mot impressionne ; la pratique est accessible à tous.",
 "Rappelez-vous le chapitre 1 : votre prompt est le début du texte que l'IA va prolonger. Une demande vague laisse à l'IA un immense champ de suites « plausibles » : elle choisit alors une réponse moyenne, générique. Une demande précise réduit ce champ et oriente la réponse vers ce dont <strong>vous</strong> avez besoin."))
B.append('<div class="grid g2"><div class="card"><div class="kicker" style="color:#' + NAVY + '">Prompt A</div><p style="font-weight:600;color:#' + NAVY + ';">« Fais-moi un résumé de ce rapport. »</p></div>'
         '<div class="card" style="background:#E6F4F2"><div class="kicker" style="color:#' + TEAL + '">Prompt B</div><p style="font-weight:600;color:#' + NAVY + ';">« Résume ce rapport de 12 pages en 5 puces pour mon directeur, qui doit décider vendredi s\'il valide le budget. Mets en avant les coûts et les risques. »</p></div></div>')
B.append(P("Le prompt B précise <strong>pour qui</strong> (le directeur), <strong>pour quoi</strong> (décider du budget), <strong>sous quelle forme</strong> (5 puces) et <strong>avec quelles priorités</strong> (coûts, risques). Il donnera systématiquement un meilleur résultat."))
B.append('<h3><span class="num">3.2</span>Les 4 erreurs les plus fréquentes</h3>')
B.append(table(["Erreur", "Exemple", "Ce que l'IA ne sait pas", "Correction"], [
    ["Trop vague", "« Parle-moi du marketing. »", "De quel marketing ? Pour quelle entreprise ? Avec quel but ?", "Précisez le sujet exact."],
    ["Sans contexte", "« Écris une offre commerciale. »", "Pour quel client, quel produit, quel prix, quelle situation ?", "Donnez les informations utiles."],
    ["Sans objectif", "« Résume ce texte. »", "Pour décider ? informer ? présenter ?", "Dites pourquoi vous le demandez."],
    ["Sans format", "« Donne-moi des idées. »", "Combien ? sous quelle forme ? quelle longueur ?", "Décrivez le livrable attendu."]], ["17%", "24%", "33%", "26%"]))
B.append(box("warn", P("Penser que l'IA va « deviner » ce que vous voulez. Face à une demande floue, elle ne demande généralement pas de précisions : elle suppose. Et ses suppositions sont rarement les vôtres.")))
B.append(doc.mark("La méthode PILOTE", 2) + '<h3><span class="num">3.3</span>La méthode PILOTE</h3>')
B.append(P("Pour ne plus oublier les éléments d'un bon prompt, retenez un mot : <strong>PILOTE</strong>. Vous êtes le pilote ; l'IA est votre copilote."))
B.append(pilote_cards())
pil_detail = [
 ("P", "Persona", "Le rôle que l'IA doit adopter. Il oriente le vocabulaire, le niveau d'expertise et le point de vue.", "Agis comme un responsable RH expérimenté dans une PME industrielle.", "Agis comme un expert.", "Choisissez un rôle précis et réaliste, en lien avec la tâche."),
 ("I", "Informations", "Le contexte : la situation, l'entreprise, le destinataire, les faits, les données, les documents.", "Nous sommes une PME de 40 salariés ; le destinataire est un client fidèle depuis 5 ans, mécontent d'un retard.", "(aucun contexte)", "C'est l'élément le plus important : sans contexte, l'IA invente ou reste générique."),
 ("L", "Livrable", "Ce que vous voulez obtenir et sous quelle forme : type de document, longueur, structure, format.", "Rédige un email de 150 mots maximum, avec un objet et 3 puces.", "Écris quelque chose.", "Décrivez le résultat comme si vous le commandiez à un prestataire."),
 ("O", "Objectif", "Pourquoi vous le demandez : le résultat visé chez le lecteur ou pour vous.", "Objectif : obtenir l'accord du client sur une nouvelle date avant vendredi.", "(objectif implicite)", "Un même texte n'est pas rédigé de la même façon pour informer, convaincre ou faire décider."),
 ("T", "Ton", "Le style et le niveau de langage.", "Ton courtois, direct, sans jargon technique.", "(ton par défaut)", "Pensez au destinataire : client, collègue, direction, grand public."),
 ("E", "Exigences", "Les contraintes, interdits et critères de qualité.", "N'invente aucun chiffre ; signale ce qui manque ; pose-moi 2 questions si besoin.", "(aucune limite)", "Les garde-fous réduisent fortement les inventions et les hors-sujets.")]
B.append(table(["Lettre", "Ce que c'est", "Bon exemple", "Conseil"],
               [[f'<span style="font-family:Montserrat;font-weight:800;font-size:15pt;color:#{GOLD}">{L}</span><br><b>{w}</b>', esc(d), f"<i>« {esc(g)} »</i>", esc(c)] for L, w, d, g, b, c in pil_detail],
               ["13%", "29%", "31%", "27%"]))
B.append(box("key", P(f"<strong>{esc(PILOTE_MIN)}</strong> L'ordre des lettres dans votre prompt n'a pas d'importance : ce qui compte, c'est que les informations soient présentes.")))
B.append('<h3><span class="num">3.4</span>Prompt simple ou prompt structuré ?</h3>')
B.append(P("La méthode PILOTE n'est pas un carcan. Il serait absurde d'écrire six rubriques pour traduire un mot. Dosez l'effort selon l'enjeu :"))
B.append(table(["Situation", "Exemples", "Niveau de prompt"], [
    ["Demande simple", "Traduire une phrase, trouver un synonyme, une idée rapide, une définition", "Une phrase suffit"],
    ["Tâche courante", "Email interne, résumé, liste d'idées, plan de document", "Trio I + L + O (contexte, livrable, objectif)"],
    ["Enjeu important", "Document client, note de direction, publication, contenu engageant", "PILOTE complet + relecture attentive"]], ["22%", "48%", "30%"]))
B.append(box("tip", P("Si vous ne savez pas quoi préciser, retournez la situation : terminez votre demande par <em>« Avant de répondre, pose-moi les questions dont tu as besoin pour bien faire. »</em> L'IA vous aide alors à construire le contexte.")))
B.append("<h4>Le modèle à réutiliser</h4>" + prompt(PILOTE_TEMPLATE, "Modèle PILOTE — à copier-coller"))
B.append(doc.mark("Trois démonstrations commentées", 2) + '<h3><span class="num">3.5</span>Trois démonstrations commentées</h3>')
B.append(P("Même besoin, trois manières de le formuler : informer une cliente d'un retard de livraison."))
for i, dm in enumerate(DEMO3):
    col = dm["color"]
    B.append(f'<h4 style="color:#{col if col != ORANGE else "B5761A"}">Démonstration {i+1} — {esc(dm["level"])}</h4>')
    B.append(prompt(dm["prompt"], "Prompt") + answer(dm["answer"]))
    B.append(P(f"<strong>Analyse :</strong> {esc(dm['why'])}"))
B.append(table(["Critère", "Faible", "Amélioré", "PILOTE"], [
    ["Contexte fourni", "Aucun", "Sujet seulement", "Client, dates, quantités, cause"],
    ["Objectif exprimé", "Non", "Non", "Garder la confiance, proposer une solution"],
    ["Format demandé", "Non", "Non", "120-150 mots, objet clair"],
    ["Garde-fous", "Non", "Non", "« N'invente aucune information »"],
    ["Informations inventées", "Possible", "Oui (nom, cause)", "Aucune"],
    ["Temps de retouche", "Tout réécrire", "Important", "Simple relecture"]], ["25%", "20%", "22%", "33%"]))
B.append(box("key", P("Rédiger un prompt PILOTE prend environ une minute de plus. Ce temps est récupéré, et au-delà, au moment de la retouche. Plus le contexte est riche, moins l'IA invente.")))
B.append('<h3><span class="num">3.6</span>Six techniques pour aller plus loin</h3>')
B.append(table(["Technique", "Quand l'utiliser", "Exemple de formulation"], [
    ["Donner un exemple", "Vous voulez un style ou un format précis", "« Voici un exemple de compte rendu que j'aime : […]. Utilise la même structure. »"],
    ["Fournir le document", "La réponse doit s'appuyer sur vos données", "« À partir uniquement du document joint, … »"],
    ["Faire poser des questions", "Vous ne savez pas tout préciser", "« Pose-moi d'abord 3 questions pour bien comprendre mon besoin. »"],
    ["Découper en étapes", "La tâche est complexe", "« Étape 1 : propose seulement le plan. Nous rédigerons ensuite partie par partie. »"],
    ["Demander des options", "Vous voulez choisir", "« Propose 3 versions : formelle, chaleureuse, très courte. »"],
    ["Faire critiquer", "Vous voulez améliorer la qualité", "« Relis ta réponse comme un directeur exigeant et corrige ses 3 faiblesses. »"]], ["22%", "30%", "48%"]))
B.append('<h3><span class="num">3.7</span>Itérer : la première réponse est un brouillon</h3>')
B.append(P("Les utilisateurs les plus efficaces ne sont pas ceux qui écrivent le prompt parfait du premier coup, mais ceux qui savent <strong>relancer</strong>. Dans une même conversation, l'IA garde le contexte : une phrase suffit pour ajuster."))
B.append(table(["Relance", "Formulation type"], [[esc(t), f"<i>{esc(q)}</i>"] for t, q in ITERATIONS], ["28%", "72%"]))
B.append(P("La méthode d'itération tient en trois verbes : <strong>Demander → Observer → Préciser</strong>. Observez ce qui ne va pas (trop long ? trop vague ? mauvais ton ? information inventée ?) et transformez chaque défaut en instruction."))
B.append(box("ask", P("Améliorez ce prompt faible avec la méthode PILOTE : <em>« Fais une annonce pour la réunion. »</em>",
   "<em>Proposition de correction :</em> « [P] Agis comme assistant de direction. [I] Réunion d'équipe mensuelle du service commercial (12 personnes), jeudi 14 h, salle B, pour présenter les résultats du trimestre et les objectifs du prochain. [L] Rédige un message d'invitation de 80 mots avec un objet. [O] Objectif : que chacun vienne en ayant préparé ses 2 principaux résultats. [T] Ton dynamique et cordial. [E] Termine par une demande de confirmation de présence avant mardi. »")))
B.append(br + quiz_html(3, doc) + br + corr_html(3, doc))

# ------------------------------------------------------------------ CHAPITRE 4
ch = CHAPTERS[3]
B.append(chapter_opener(doc, ch, 12, ["Le scénario : Nova Distribution", "La démarche en 8 étapes", "Les prompts de l'atelier et les résultats obtenus", "La vérification avant diffusion", "Adapter l'atelier à votre propre situation"]))
B.append('<h3 style="margin-top:0"><span class="num">4.1</span>Le scénario</h3>')
B.append(P("<strong>Nova Distribution</strong> est une PME (fictive) de 60 salariés. Vous sortez d'une réunion de lancement d'un nouveau logiciel de facturation, avec quatre participants : Sarah (directrice administrative et financière), Karim (informatique), Julie (responsable du service client) et Marc (commercial). "
           "Vous devez diffuser aujourd'hui un compte rendu, les décisions prises, un plan d'action et un email de suivi. Voici vos notes, telles que vous les avez prises :"))
B.append(f'<div class="answer" style="background:#FFFDF6;border-color:#E8DDBE;"><span class="pl" style="color:#9C7C2C">Vos notes brutes</span>{esc(NOTES_BRUTES)}</div>')
B.append(box("key", P("Ces notes ne contiennent aucune donnée sensible (pas de données personnelles de clients, pas de chiffres confidentiels) : elles peuvent être utilisées dans un assistant IA. Dans votre entreprise, appliquez toujours le feu tricolore du chapitre 5 avant de coller un contenu.")))
B.append('<h3><span class="num">4.2</span>La démarche en 8 étapes</h3>')
B.append(table(["", "Étape", "Ce que vous faites"], [[str(i + 1), f"<b>{esc(t)}</b>", esc(d)] for i, (t, d, ic) in enumerate(WORKFLOW4)], ["6%", "24%", "70%"]))
B.append('<h3><span class="num">4.3</span>Étapes 1 à 3 : la première demande</h3>')
B.append(prompt(PROMPT4_V1, "Première demande") + answer(ANSWER4_V1))
B.append(P("La réponse est correcte en apparence et bien écrite… mais inutilisable. <strong>Ce qui manque :</strong>"))
B.append(UL([esc(m) for m in MISSING4]))
B.append('<h3><span class="num">4.4</span>Étapes 4 et 5 : diagnostiquer et reformuler avec PILOTE</h3>')
B.append(P("Chaque manque devient une instruction. Pas de décisions ? On demande une rubrique « décisions ». Pas de responsables ? On demande un tableau d'actions. Risque d'invention ? On l'interdit explicitement."))
B.append(prompt(PROMPT4_V2, "Prompt PILOTE"))
B.append('<h3><span class="num">4.5</span>Étapes 6 et 7 : le résultat</h3>')
res = ("Compte rendu — Lancement du logiciel de facturation (14/11)\n\nContexte : réunion de lancement du nouveau logiciel de facturation ; la mise en service est visée pour le 6 janvier.\n\nDécisions prises :\n"
       + "\n".join("• " + d for d in ANSWER4_V2["decisions"]) + "\n\nActions :\n"
       + "\n".join(f"• {a} — {r} — {e}" for a, r, e in ANSWER4_V2["actions"]) + "\n\nPoints non tranchés :\n• " + ANSWER4_V2["open_points"][0]
       + "\n\nRisques et contradiction :\n" + "\n".join("• " + r for r in ANSWER4_V2["risks"]))
B.append(answer(res, "Résultat obtenu (exemple)"))
B.append(P("Le résultat est structuré et actionnable. L'exigence « signale toute contradiction » a fonctionné : le conflit entre la date du 6 janvier et les deux semaines de tests est mis en évidence. Mais avant de diffuser… on enchaîne d'abord sur l'email."))
B.append(prompt(PROMPT4_V3, "Relance : l'email de suivi"))
B.append(answer("Objet : Logiciel de facturation – décisions et actions (réunion du 14/11)\n\nBonjour à tous,\nMerci pour vos contributions. Décisions : formation du service client la semaine du 8 décembre ; budget de 3 500 € validé.\nActions : Karim – planning de migration (vendredi) · Julie – organisation de la formation · Marc – information des 20 plus gros clients.\nPoint de vigilance : la date du 6 janvier dépend de la fin de la migration.\nMerci de confirmer vos actions avant le 21/11. Prochaine réunion : 28/11."))
B.append(doc.mark("Étape 8 : vérifier avant de diffuser", 2) + '<h3><span class="num">4.6</span>Étape 8 : vérifier avant de diffuser</h3>')
B.append(P("On compare le résultat, ligne à ligne, avec les notes d'origine :"))
for t, d, c in CATCHES4:
    kind = {RED: "warn", ORANGE: "tip", TEAL: "key"}[c]
    B.append(box(kind, P(esc(d)), t))
B.append(prompt("Le point sur les 20 clients n'est pas tranché : retire l'action de Marc, place-le dans les points ouverts avec « Responsable : à définir ». Confirme aussi que l'organisation de la formation par Julie est une proposition à valider. Mets à jour le compte rendu et l'email.", "Relance de correction"))
B.append("<h4>La check-list avant envoi</h4>" + UL(["Les noms et les rôles sont corrects", "Les dates et échéances correspondent aux notes", "Les montants et chiffres sont exacts", "Chaque décision figure bien dans les notes d'origine", "Les points non tranchés sont signalés comme tels", "Le ton est adapté aux destinataires"]))
B.append(box("key", P("L'IA a réalisé l'essentiel du travail de mise en forme en quelques minutes. La vérification est <strong>votre valeur ajoutée</strong> : c'est elle qui évite qu'un collègue reçoive une mission que personne ne lui a confiée.")))
B.append('<h3><span class="num">4.7</span>Si la technologie fait défaut</h3>')
B.append(P("Cet atelier fonctionne aussi sans connexion : les prompts et les résultats sont reproduits dans le diaporama et dans ce syllabus. Les réponses d'une IA varient d'un essai à l'autre : si vous reproduisez l'atelier, vous n'obtiendrez pas exactement le même texte, mais la démarche et les enseignements restent identiques."))
B.append(box("ask", P("Reprenez les notes de votre dernière réunion (en retirant toute donnée sensible). Appliquez le prompt PILOTE de l'étape 5, puis la check-list de l'étape 8. Combien d'éléments avez-vous dû corriger ?")))
B.append(br + quiz_html(4, doc) + br + corr_html(4, doc))

# ------------------------------------------------------------------ CHAPITRE 5
ch = CHAPTERS[4]
B.append(chapter_opener(doc, ch, 8, ["Les hallucinations et les erreurs factuelles", "Vérifier une information : la méthode en 5 gestes", "Confidentialité : le feu tricolore des données", "Droits d'auteur, biais, dépendance", "La règle Vrai ? Juste ? Signable ?", "Bonnes pratiques en entreprise"]))
B.append('<h3 style="margin-top:0"><span class="num">5.1</span>Les hallucinations et les erreurs factuelles</h3>')
B.append(P("Une <strong>hallucination</strong> est une réponse inventée mais présentée de façon crédible : une étude qui n'existe pas, un chiffre faux, une citation jamais prononcée, un article de loi erroné, une biographie approximative. Elle découle directement du fonctionnement vu au chapitre 1 : le modèle produit du plausible."))
B.append(prompt("Donne-moi une statistique récente et sa source sur l'usage de l'IA dans les PME européennes.", "Demande") +
         answer("Selon l'étude 2024 de l'Observatoire européen des PME numériques, 73,4 % des PME européennes utilisent quotidiennement l'IA générative, avec un gain moyen de 11,2 heures par salarié et par semaine.", "Réponse — exemple fictif d'hallucination"))
B.append(P("Tout semble crédible : un organisme au nom sérieux, des chiffres précis à la décimale. Pourtant, dans cet exemple construit pour la formation, l'organisme et les chiffres sont inventés."))
B.append('<div class="grid g2"><div class="card"><h4 style="color:#' + RED + '">Les signaux d\'alerte</h4>' + UL(["Chiffres très précis sans lien vérifiable", "Source, auteur ou étude introuvable", "Citations « parfaites », références juridiques", "Ton très assuré sur un sujet pointu", "Informations récentes sans recherche web"]) + '</div>'
         '<div class="card"><h4 style="color:#' + TEAL + '">Les zones à risque</h4>' + UL(["Chiffres, statistiques, montants", "Dates et événements récents", "Textes juridiques, normes, réglementations", "Noms de personnes, biographies", "Références bibliographiques et liens"]) + '</div></div>')
B.append("<h4>Vérifier une information : la méthode en 5 gestes</h4>" + OL([
    "<strong>Isoler les affirmations vérifiables</strong> : chiffres, dates, noms, citations, références.",
    "<strong>Demander la source</strong> à l'IA (« Pour chaque chiffre, indique ta source et sa date »).",
    "<strong>Ouvrir la source</strong> et vérifier qu'elle existe et qu'elle dit bien ce qui lui est attribué.",
    "<strong>Croiser</strong> avec une seconde source fiable (site officiel, organisme reconnu, document interne).",
    "<strong>Refaire les calculs</strong> importants vous-même ou dans un tableur."]))
B.append(box("warn", P("Considérer qu'une source citée par l'IA est forcément exacte. Même les outils avec recherche web peuvent attribuer à une source ce qu'elle ne dit pas, ou citer un lien qui ne fonctionne pas. Une source introuvable rend l'information inutilisable.")))
B.append(doc.mark("Confidentialité : le feu tricolore des données", 2) + '<h3><span class="num">5.2</span>Confidentialité : le feu tricolore des données</h3>')
B.append(P("Tout ce que vous saisissez dans un outil d'IA quitte votre poste de travail. Selon l'outil, la version (gratuite ou professionnelle) et vos paramètres, ces contenus peuvent être conservés, consultés pour la modération ou utilisés pour améliorer les modèles. Les versions professionnelles souscrites par les entreprises offrent généralement des engagements contractuels plus protecteurs. <strong>La règle : connaître la politique de votre entreprise et classer l'information avant de la saisir.</strong>"))
for (t, c, ex), kind in zip(TRAFFIC, ["warn", "tip", "key"]):
    B.append(box(kind, UL([esc(e) for e in ex]), t))
B.append("<h4>Anonymiser : un exemple</h4>")
B.append('<div class="grid g2">' + f'<div>{answer("Mme Sophie Lambert (Lambert Immobilier, 12 rue des Lilas, Lyon) conteste notre facture n° 2024-118 de 14 860 € et menace de résilier son contrat.", "Avant : à ne pas saisir")}</div>'
         f'<div>{answer("[CLIENTE A], gérante d une agence immobilière, conteste une facture de [MONTANT] et menace de résilier son contrat.", "Après : utilisable")}</div></div>')
B.append(P("Vous gardez l'essentiel pour obtenir une réponse utile (la situation, l'enjeu), sans exposer les données personnelles ni les montants. Vous réintégrez les vraies informations après coup, dans votre messagerie."))
B.append('<h3><span class="num">5.3</span>Droits d\'auteur, biais et dépendance</h3>')
B.append(table(["Risque", "De quoi s'agit-il ?", "Le bon réflexe"], [
    ["Droits d'auteur", "Les contenus générés peuvent ressembler à des œuvres protégées ; les conditions d'utilisation varient selon les outils, notamment pour les images.", "Ne pas demander de reproduire des textes, images ou marques protégés ; vérifier les conditions d'usage commercial ; respecter la politique interne (mention de l'IA, validation)."],
    ["Biais", "L'IA reproduit des stéréotypes présents dans ses données (genre, origine, âge, culture).", "Relire avec un œil critique ; demander une formulation inclusive ; croiser les points de vue ; ne jamais laisser l'IA trier des candidats."],
    ["Dépendance", "À force de déléguer, on risque de perdre des compétences (rédaction, analyse, esprit critique).", "Réfléchir d'abord, puis comparer avec l'IA ; l'utiliser comme partenaire d'entraînement ; garder la maîtrise des sujets clés."],
    ["Jugement humain", "L'IA n'a ni responsabilité, ni éthique, ni connaissance fine de votre contexte.", "Garder la décision, surtout quand elle touche des personnes ou engage l'entreprise."]], ["16%", "40%", "44%"]))
B.append(box("ex", P("Le RGPD encadre l'utilisation des données personnelles, y compris lorsqu'elles sont traitées avec une IA. Le règlement européen sur l'intelligence artificielle (AI Act) encadre progressivement les usages, avec des obligations qui varient selon le niveau de risque des systèmes. Ces cadres évoluent : référez-vous à la politique de votre entreprise, à votre délégué à la protection des données (DPO) ou à votre service juridique."), "Le cadre réglementaire, en bref"))
B.append(doc.mark("La règle Vrai ? Juste ? Signable ?", 2) + '<h3><span class="num">5.4</span>La règle à retenir : Vrai ? Juste ? Signable ?</h3>')
B.append(P("Avant d'utiliser une réponse de l'IA, posez-vous trois questions :"))
B.append('<div class="grid g3">' + "".join(
    f'<div class="card" style="border-top:4pt solid #{c}"><div style="font-family:Montserrat;font-weight:800;font-size:15pt;color:#{c if c != GOLD else "9C7C2C"}">{esc(t)}</div><p style="font-weight:600;margin:3pt 0 5pt 0;">{esc(sub)}</p>{UL([esc(x) for x in lst])}</div>'
    for (t, sub, lst, ic), c in zip(VJS, [NAVY, TEAL, GOLD])) + '</div>')
B.append(box("key", P("<strong>Vrai</strong> = les faits. <strong>Juste</strong> = le contexte. <strong>Signable</strong> = l'engagement. Dans l'atelier du chapitre 4, l'erreur sur Marc était un problème de « Juste » : l'information était plausible, mais ne correspondait pas à la réalité de la réunion.")))
B.append('<h3><span class="num">5.5</span>Bonnes pratiques en entreprise</h3>')
B.append(UL(["Utiliser en priorité les outils <strong>validés</strong> par l'entreprise et connectés avec un compte professionnel.",
             "Vérifier les <strong>paramètres de confidentialité</strong> (historique, utilisation des données pour l'entraînement).",
             "Mettre en place une <strong>charte d'usage</strong> simple : outils autorisés, données interdites, relecture obligatoire.",
             "Partager les <strong>bons prompts</strong> en équipe et capitaliser les retours d'expérience.",
             "Être <strong>transparent</strong> sur l'usage de l'IA lorsque la politique interne ou le contexte l'exigent.",
             "Former régulièrement les équipes : les outils évoluent vite, les réflexes doivent suivre."]))
B.append(br + quiz_html(5, doc) + br + corr_html(5, doc))

# ------------------------------------------------------------------ ANNEXES
B.append(br + section_title(doc, "Bibliothèque de prompts essentiels", first=True, kicker="Boîte à outils"))
B.append(P("Une sélection de douze prompts couvrant les besoins les plus fréquents. Remplacez les éléments entre [CROCHETS]. La bibliothèque complète (25 prompts commentés) se trouve dans le <strong>Kit IA du professionnel moderne</strong>."))
picks = []
for g, ic, items in PROMPT_GROUPS:
    for it in items[:2]: picks.append((g, it))
for g, it in picks[:12]:
    B.append(f'<div class="avoid"><h4>{esc(it["name"])} <span class="chip" style="background:#E6F4F2;color:#{TEAL}">{esc(g)}</span></h4>'
             f'<p class="small" style="margin:0 0 2pt 0;"><b>Quand l\'utiliser :</b> {esc(it["when"])}</p>{prompt(it["prompt"], "Prompt")}</div>')

B.append(br + section_title(doc, "Les bonnes pratiques", first=True, kicker="Synthèse"))
B.append(P("Les dix réflexes du professionnel qui utilise l'IA :"))
B.append(table(["", "Réflexe", "En pratique"], [[str(i + 1), f"<b>{esc(t)}</b>", esc(d)] for i, (t, d) in enumerate(REFLEXES)], ["6%", "30%", "64%"]))
B.append(section_title(doc, "Les erreurs à éviter", kicker="Synthèse"))
B.append(table(["", "Erreur", "Pourquoi et que faire"], [[str(i + 1), f"<b>{esc(t)}</b>", esc(d)] for i, (t, d) in enumerate(ERRORS)], ["6%", "34%", "60%"]))

B.append(br + section_title(doc, "Confidentialité et sécurité : la check-list", first=True, kicker="Synthèse"))
B.append(table(["Avant de saisir une information, je vérifie que…", "Oui"], [[x, "☐"] for x in [
    "J'utilise un outil autorisé par mon entreprise (de préférence avec mon compte professionnel)",
    "Le contenu ne contient aucune donnée personnelle identifiante (clients, salariés, candidats)",
    "Le contenu ne contient ni salaires, ni données de santé, ni coordonnées bancaires, ni mots de passe",
    "Les chiffres financiers non publiés et les secrets d'affaires sont retirés ou agrégés",
    "J'ai anonymisé les noms, adresses et montants précis ([CLIENT A], [MONTANT])",
    "Je connais les paramètres de confidentialité de l'outil (historique, entraînement)"]] +
    [["<b>Avant d'utiliser la réponse, je vérifie que…</b>", ""]] + [[x, "☐"] for x in [
    "Les faits, chiffres, dates et noms sont exacts (VRAI)", "La réponse est adaptée à mon contexte, mon destinataire et nos règles (JUSTE)",
    "Je l'ai relue en entière et je peux l'assumer (SIGNABLE)", "Je respecte les droits d'auteur et la politique interne sur l'usage de l'IA"]], ["88%", "12%"]))

B.append(br + section_title(doc, "Glossaire de l'IA", first=True, kicker="Référence"))
B.append(table(["Terme", "Définition"], [[f"<b>{esc(t)}</b>", esc(d)] for t, d in GLOSSARY], ["28%", "72%"]))

B.append(br + section_title(doc, "Fiche de révision express", first=True, kicker="Une page pour tout retenir"))
B.append('<div class="grid g2">')
for chp in CHAPTERS:
    B.append(f'<div class="card" style="border-left:4pt solid #{TEAL}"><div class="kicker">Chapitre {chp["n"]}</div><h4 style="margin:2pt 0 3pt 0;">{esc(chp["short"])}</h4><p>{esc(chp["message"])}</p></div>')
B.append(f'<div class="card navy" style="background:#{NAVY}"><div class="kicker">Les 3 choses à retenir</div><p style="color:#fff;font-size:9pt;margin-top:4pt;">'
         f'<b style="color:#{GOLD}">Une image :</b> le stagiaire surdoué.<br><b style="color:#{GOLD}">Une méthode :</b> PILOTE.<br><b style="color:#{GOLD}">Une règle :</b> Vrai ? Juste ? Signable ?</p></div></div>')
B.append("<h4>La méthode PILOTE</h4>" + pilote_cards())
B.append('<div class="grid g3">' + "".join(f'<div class="card"><h4 style="margin-top:0">{esc(t)}</h4><p>{esc(q)}</p></div>' for t, q in ITERATIONS[:3]) + '</div>')
B.append(box("key", P("Cadrer → Produire → Vérifier → Décider. L'IA prépare, l'humain décide. Rien de rouge dans un outil non validé.")))

B.append(br + section_title(doc, "Plan d'action personnel", first=True, kicker="À compléter"))
B.append(P("Identifiez trois tâches professionnelles que vous allez améliorer grâce à l'IA. Choisissez des tâches fréquentes, qui vous prennent du temps et dont vous maîtrisez bien le contenu (pour pouvoir vérifier le résultat)."))
for i in range(3):
    B.append(f'<div class="card avoid" style="margin:8pt 0;"><div style="display:flex;align-items:center;gap:8pt;">{badge("target", TEAL, "FFFFFF", 26)}<h4 style="margin:0">Tâche n° {i+1}</h4></div>'
             + "".join(f'<div style="display:flex;gap:8pt;align-items:flex-end;margin-top:6pt;"><span class="small" style="width:46mm;flex:none;">{lab}</span><div class="write" style="flex:1"></div></div>'
                       for lab in ["La tâche", "Temps actuel / fréquence", "Super-pouvoir concerné", "Mon prompt (idée PILOTE)", "Données à anonymiser ?", "Date du premier essai", "Résultat / temps gagné"]) + '</div>')
B.append(box("tip", P("Commencez par la tâche la plus simple. Un premier succès rapide vaut mieux qu'un projet ambitieux jamais lancé. Puis suivez le <strong>défi IA de 7 jours</strong> du kit.")))

B.append(br + section_title(doc, "Conclusion", first=True, kicker="Et maintenant ?"))
B.append(P("Il y a une heure, l'intelligence artificielle était peut-être pour vous une boîte noire, fascinante ou inquiétante. Vous savez maintenant qu'il s'agit d'un outil puissant, qui compose des réponses plausibles à partir de vos instructions, et qui a besoin de vous pour être utile : pour le cadrer, pour le guider, pour le vérifier.",
 "Vous disposez d'une méthode — <strong>PILOTE</strong> — qui fonctionne avec tous les assistants, aujourd'hui comme demain. Vous avez vu, avec l'atelier, qu'une conversation de travail bien menée transforme des notes en vrac en un plan d'action clair en quelques minutes, à condition de vérifier. Vous savez protéger les données et poser les trois questions qui comptent : <strong>Vrai ? Juste ? Signable ?</strong>",
 "Les outils vont continuer à évoluer très vite : assistants capables de lire vos documents et de dialoguer à la voix, agents capables d'enchaîner des tâches, IA intégrée à tous vos logiciels, automatisations sans code. Ces évolutions ne rendront pas votre méthode obsolète ; elles la rendront plus précieuse. "
 "<strong>Les outils changeront. La méthode restera : cadrer, dialoguer, vérifier, décider.</strong>",
 "La compétence en IA ne s'acquiert pas en lisant, mais en pratiquant. Choisissez une tâche, ouvrez un assistant, écrivez votre premier prompt PILOTE. Demain."))
B.append(f'<div style="margin-top:14pt;background:#{NAVY};border-radius:8pt;padding:16pt 18pt;color:#fff;text-align:center;">'
         f'<div style="font-family:Montserrat;font-weight:800;font-size:17pt;">Vous êtes désormais le PILOTE.</div>'
         f'<div style="color:#C9D3E6;margin-top:4pt;">L\'IA est un copilote formidable, à condition de savoir où vous allez.</div></div>')

def body(toc):
    return (section_title(doc, "Sommaire", first=True).replace(doc.toc[-1][0], "") if False else
            '<h2 class="first">Sommaire</h2>' + toc + br + "".join(B))

cov = cover("Syllabus · Guide pédagogique complet", 'IA &amp; Prompt Engineering <span style="color:#' + GOLD + '">appliqués aux entreprises</span>',
            SUBTITLE, [("book-open", "Le cours détaillé des 5 chapitres"), ("circle-check", "5 quiz et leurs corrigés expliqués"), ("compass", "La méthode PILOTE et l'atelier complet"),
                       ("notebook-pen", "Glossaire, fiche de révision et plan d'action")], ic="book-open")
build(doc, cov, body, os.path.join(HERE, "..", "02_Syllabus", "Syllabus_IA_Prompt_Engineering.pdf"), "SYLLABUS · IA &amp; PROMPT ENGINEERING APPLIQUÉS AUX ENTREPRISES")
