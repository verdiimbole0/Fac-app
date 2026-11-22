# -*- coding: utf-8 -*-
"""Contenu pédagogique partagé — Formation « IA & Prompt Engineering appliqués aux entreprises ».
Source unique utilisée par le PowerPoint, le syllabus, le kit bonus et le guide du formateur."""

TITLE = "IA & Prompt Engineering appliqués aux entreprises"
SUBTITLE = "De la curiosité à la maîtrise : utiliser l'IA générative avec méthode, efficacité et discernement"
VERIF_DATE = "novembre 2026"

NAVY = "0A1E3F"; GOLD = "C7A34F"; WHITE = "FFFFFF"; LIGHT = "F3F5F8"; TEAL = "1B9E8F"
NAVY2 = "132C56"; INK = "1F2A3D"; MUTED = "5B6678"; RED = "C0504D"; ORANGE = "E39B2D"; GREEN = "1B9E8F"

# ------------------------------------------------------------------ PROGRAMME
TIMING = [
    ("Accueil et accroche", 4, "Créer l'envie, poser les objectifs et le programme"),
    ("Chapitre 1 — Comprendre l'IA sans être technicien", 9, "Contenu 6½ min · quiz + corrigé 2½ min"),
    ("Chapitre 2 — L'IA dans l'entreprise", 9, "Contenu 6½ min · quiz + corrigé 2½ min"),
    ("Chapitre 3 — Le Prompt Engineering : la méthode PILOTE", 14, "Contenu 11½ min · quiz + corrigé 2½ min"),
    ("Chapitre 4 — Atelier : l'IA comme collègue", 12, "Démonstration 9½ min · quiz + corrigé 2½ min"),
    ("Chapitre 5 — Risques, réflexes et responsabilité", 8, "Contenu 5½ min · quiz + corrigé 2½ min"),
    ("Conclusion et plan d'action", 4, "Récapitulatif, plan d'action, ouverture"),
]
assert sum(t[1] for t in TIMING) == 60

CHAPTERS = [
    dict(n=1, title="Comprendre l'IA sans être technicien", short="Comprendre l'IA", icon="brain",
         objective="Comprendre ce qu'est l'IA générative, comment elle produit ses réponses, ce qu'elle sait faire et pourquoi elle peut se tromper.",
         message="Une IA générative ne « sait » pas : elle prédit la suite la plus probable d'un texte. C'est puissant, mais cela exige votre vérification.",
         transition="Maintenant que vous savez comment elle fonctionne, voyons ce qu'elle peut faire concrètement dans votre métier."),
    dict(n=2, title="Découvrir le potentiel de l'IA dans l'entreprise", short="L'IA dans l'entreprise", icon="building-2",
         objective="Identifier des usages concrets de l'IA dans chaque fonction de l'entreprise et comprendre la répartition des rôles entre l'humain et l'IA.",
         message="L'IA n'est pas réservée aux informaticiens : elle produit un premier jet ; vous cadrez, vous vérifiez, vous décidez.",
         transition="Tout le monde a accès aux mêmes outils. Ce qui fait la différence, c'est la qualité de la demande. C'est l'objet du chapitre 3."),
    dict(n=3, title="Le Prompt Engineering : bien donner des instructions", short="La méthode PILOTE", icon="compass",
         objective="Savoir formuler une demande efficace grâce à la méthode PILOTE et améliorer une réponse par itérations successives.",
         message="La qualité de la réponse dépend de la qualité de la demande. Vous êtes le PILOTE, l'IA est votre copilote.",
         transition="Passons de la théorie à la pratique : nous allons traiter ensemble une situation de travail réelle, du début à la fin."),
    dict(n=4, title="Atelier pratique : utiliser l'IA comme un collègue", short="Atelier pratique", icon="users",
         objective="Traiter un cas complet (réunion → compte rendu → plan d'action → email de suivi) en dialoguant avec l'IA et en contrôlant le résultat.",
         message="On ne « tape pas une question » : on mène une conversation de travail, en plusieurs tours, jusqu'à un résultat vérifié.",
         transition="Vous avez vu la puissance de l'outil. Voyons maintenant comment l'utiliser de manière responsable et sûre."),
    dict(n=5, title="Utiliser l'IA intelligemment : risques, réflexes et plan d'action", short="Risques & réflexes", icon="shield-check",
         objective="Reconnaître les risques (hallucinations, confidentialité, droits, biais, dépendance) et appliquer des réflexes simples de vérification et de protection.",
         message="Avant d'utiliser une réponse : est-elle VRAIE, JUSTE pour mon contexte, et suis-je prêt à la SIGNER ?",
         transition="Il ne reste qu'une étape : transformer ce que vous avez appris en actions concrètes dès demain."),
]

# ------------------------------------------------------------------ MÉTHODE PILOTE
PILOTE = [
    ("P", "Persona", "Le rôle que l'IA doit adopter", "Agis comme un responsable RH expérimenté…", "user-check"),
    ("I", "Informations", "Le contexte utile : situation, public, données", "Nous sommes une PME de 40 salariés ; le destinataire est…", "layers"),
    ("L", "Livrable", "Ce que vous voulez obtenir et sous quel format", "Rédige un email de 150 mots max, avec objet et 3 puces…", "file-text"),
    ("O", "Objectif", "Pourquoi vous le demandez, le résultat visé", "…afin d'obtenir une réponse du client avant vendredi.", "target"),
    ("T", "Ton", "Le style et le niveau de langage", "Ton courtois, direct, sans jargon.", "message-circle"),
    ("E", "Exigences", "Contraintes et critères de qualité", "N'invente aucun chiffre ; signale ce qui manque ; pose-moi d'abord 2 questions si besoin.", "list-checks"),
]
PILOTE_MIN = "Le trio minimum : I + L + O (contexte, livrable, objectif). Ajoutez P, T et E quand l'enjeu augmente."

PILOTE_TEMPLATE = """[P] Agis comme [RÔLE / EXPERTISE].
[I] Contexte : [SITUATION, ENTREPRISE, PUBLIC, DONNÉES UTILES].
[L] Rédige / Produis : [LIVRABLE] au format [FORMAT : tableau, liste, email, X mots…].
[O] Objectif : [CE QUE CE LIVRABLE DOIT PERMETTRE D'OBTENIR].
[T] Ton : [FORMEL / CHALEUREUX / PÉDAGOGIQUE / DIRECT].
[E] Exigences : [CONTRAINTES, À ÉVITER, CRITÈRES DE QUALITÉ]. Si des informations manquent, pose-moi des questions avant de répondre."""

ITERATIONS = [
    ("Raccourcir / préciser", "« Réduis à 100 mots et garde uniquement les 3 points essentiels. »"),
    ("Changer de ton", "« Reformule sur un ton plus chaleureux, comme si tu parlais à un client fidèle. »"),
    ("Changer de format", "« Présente cela sous forme de tableau : action / responsable / échéance. »"),
    ("Faire critiquer", "« Relis ta réponse comme un directeur exigeant : quelles sont ses 3 faiblesses ? Corrige-les. »"),
    ("Faire poser des questions", "« Avant de répondre, pose-moi les questions dont tu as besoin pour bien faire. »"),
]

# ------------------------------------------------------------------ DÉMOS CHAPITRE 3
DEMO3 = [
    dict(level="Prompt faible", color=RED,
         prompt="Écris un email pour un client.",
         answer="Objet : Votre demande\n\nBonjour,\n\nNous vous remercions pour votre message. Nous revenons vers vous rapidement concernant votre demande.\n\nCordialement,\nL'équipe",
         why="Aucun contexte, aucun objectif, aucun destinataire précis : l'IA produit un texte générique, inutilisable en l'état."),
    dict(level="Prompt amélioré", color=ORANGE,
         prompt="Écris un email à un client pour m'excuser d'un retard de livraison de sa commande de fournitures de bureau.",
         answer="Objet : Retard de livraison de votre commande\n\nBonjour Monsieur Martin,\n\nNous vous prions de nous excuser pour le retard de livraison de votre commande. Ce retard est dû à des difficultés logistiques. Votre commande vous sera livrée dans les meilleurs délais…",
         why="Le sujet est clair, mais l'IA invente des éléments (« Monsieur Martin », « difficultés logistiques ») et ne propose rien de concret."),
    dict(level="Prompt professionnel (PILOTE)", color=TEAL,
         prompt=("[P] Agis comme un responsable de la relation client d'une PME.\n"
                 "[I] Notre client, la société Alfa Conseil (contact : Mme Diallo), attend 40 cartons de papier commandés le 3 mars. La livraison prévue le 10 mars est décalée au 14 mars à cause d'une rupture chez notre transporteur.\n"
                 "[L] Rédige un email de 120 à 150 mots avec un objet clair.\n"
                 "[O] Objectif : conserver la confiance du client et lui proposer une solution.\n"
                 "[T] Ton : professionnel, empathique, sans excès d'excuses.\n"
                 "[E] Propose une livraison partielle de 10 cartons dès le 11 mars. N'invente aucune autre information."),
         answer=("Objet : Votre commande du 3 mars : nouvelle date et solution immédiate\n\n"
                 "Bonjour Madame Diallo,\n\nJe tiens à vous informer personnellement que la livraison de vos 40 cartons de papier, prévue le 10 mars, est reportée au 14 mars en raison d'une rupture chez notre transporteur. Je mesure la gêne que cela peut représenter.\n\n"
                 "Pour vous permettre de poursuivre votre activité sans interruption, nous pouvons vous livrer 10 cartons dès le 11 mars. Il vous suffit de me confirmer ce choix par retour d'email.\n\n"
                 "Je reste à votre disposition…"),
         why="Le contexte est fourni, l'objectif est explicite, une solution est proposée : le résultat est quasi prêt à l'envoi, après relecture."),
]

# ------------------------------------------------------------------ ATELIER CHAPITRE 4
NOTES_BRUTES = """Réunion 14/11 – lancement nouveau logiciel de facturation
Présents : Sarah (DAF), Karim (IT), Julie (resp. service client), Marc (commercial)
- Sarah : mise en service prévue le 6 janvier, pas plus tard (clôture annuelle)
- Karim : migration des données clients pas finie, besoin de 2 semaines de tests -> risque si on garde le 6/01
- Julie inquiète : équipe pas formée, risque d'appels clients
- Décidé : formation équipe service client semaine du 8 décembre
- Karim envoie le planning de migration vendredi
- Marc : faut-il prévenir les 20 plus gros clients du nouveau format de facture ? -> pas tranché
- Budget formation 3 500 € validé par Sarah
- Prochaine réunion le 28/11"""

PROMPT4_V1 = "Fais un compte rendu de cette réunion : [COLLER LES NOTES]"
ANSWER4_V1 = ("Compte rendu de réunion\n\nLa réunion a porté sur le lancement du nouveau logiciel de facturation. "
              "Plusieurs points ont été abordés, notamment la date de mise en service, la migration des données et la formation des équipes. "
              "Les participants ont échangé sur les risques et les prochaines étapes. Une prochaine réunion est prévue.")
MISSING4 = ["Pas de liste des décisions", "Pas de responsables ni d'échéances", "Le conflit de date (6 janvier vs tests) disparaît", "Le point non tranché n'apparaît pas", "Format inexploitable pour un suivi"]

PROMPT4_V2 = """[P] Agis comme un chef de projet rigoureux.
[I] Voici mes notes brutes d'une réunion de lancement d'un nouveau logiciel de facturation : [COLLER LES NOTES]
[L] Produis un compte rendu structuré : 1) contexte en 2 lignes, 2) décisions prises, 3) tableau des actions (action / responsable / échéance), 4) points non tranchés, 5) risques identifiés.
[O] Objectif : que chaque participant sache exactement ce qu'il doit faire.
[T] Ton : factuel et concis.
[E] N'invente rien : si un responsable ou une date manque, écris « À définir ». Signale toute contradiction."""

ANSWER4_V2 = dict(
    decisions=["Formation de l'équipe service client la semaine du 8 décembre", "Budget formation de 3 500 € validé (Sarah)", "Prochaine réunion le 28 novembre"],
    actions=[("Envoyer le planning de migration", "Karim", "Vendredi"),
             ("Organiser la formation service client", "Julie", "Sem. du 8 déc."),
             ("Prévenir les 20 plus gros clients", "Marc", "Avant le 6 janv.")],
    open_points=["Informer ou non les 20 plus gros clients du nouveau format de facture"],
    risks=["Date du 6 janvier incompatible avec 2 semaines de tests si la migration n'est pas terminée", "Équipe non formée → hausse des appels clients"])

PROMPT4_V3 = "Rédige maintenant l'email de suivi à envoyer aux 4 participants : 120 mots maximum, objet clair, rappel des décisions et du tableau d'actions, et demande à chacun de confirmer ses actions avant le 21/11."
CATCHES4 = [
    ("Erreur détectée", "L'IA a attribué à Marc l'action « Prévenir les 20 plus gros clients » alors que ce point n'a PAS été tranché.", RED),
    ("Hypothèse à valider", "« Organiser la formation : Julie » n'est pas écrit dans les notes : l'IA l'a déduit. À confirmer.", ORANGE),
    ("Bien vu par l'IA", "Le risque sur la date du 6 janvier a été correctement mis en évidence.", TEAL),
]
WORKFLOW4 = [("Contexte", "Je rassemble les notes et l'objectif", "clipboard-list"),
             ("1re demande", "Je soumets une instruction simple", "send"),
             ("Observer", "Je lis le résultat calmement", "eye"),
             ("Diagnostiquer", "J'identifie ce qui manque", "scan-search"),
             ("Améliorer", "Je reformule avec PILOTE", "compass"),
             ("Préciser", "Je relance, je corrige, j'enrichis", "refresh-cw"),
             ("Exploiter", "J'obtiens un livrable utilisable", "file-text"),
             ("Vérifier", "Je contrôle avant de diffuser", "badge-check")]

# ------------------------------------------------------------------ CHAPITRE 5
TRAFFIC = [
    ("ROUGE — Jamais dans un outil public", RED, ["Données personnelles identifiantes (clients, salariés)", "Salaires, données de santé, évaluations", "Mots de passe, coordonnées bancaires", "Chiffres financiers non publiés, contrats, secrets d'affaires"]),
    ("ORANGE — Seulement après anonymisation, ou dans l'outil validé par l'entreprise", ORANGE, ["Comptes rendus internes", "Documents de travail", "Données chiffrées agrégées", "Échanges clients (noms remplacés)"]),
    ("VERT — Utilisable librement", GREEN, ["Informations publiques", "Modèles et textes génériques", "Idées, structures, plans", "Vos propres brouillons sans données sensibles"]),
]
VJS = [("VRAI ?", "Les faits sont-ils exacts ?", ["Vérifier chiffres, dates, noms, citations à la source d'origine", "Demander les sources… puis les ouvrir réellement", "Refaire les calculs importants"], "scan-search"),
       ("JUSTE ?", "Est-ce adapté à MON contexte ?", ["Correspond-il à mon entreprise, mon client, nos règles ?", "Rien d'essentiel n'a-t-il été oublié ou ajouté ?", "Le ton convient-il au destinataire ?"], "scale"),
       ("SIGNABLE ?", "Suis-je prêt à l'assumer ?", ["Je l'ai relu en entier", "Je peux expliquer chaque phrase", "Je respecte la confidentialité et les droits"], "pen-tool")]

REFLEXES = [
    ("Je donne du contexte", "Une IA ne connaît ni votre entreprise ni votre interlocuteur : décrivez la situation."),
    ("Je précise le livrable", "Format, longueur, structure : dites exactement ce que vous voulez recevoir."),
    ("Je dialogue, je n'abandonne pas", "La première réponse est un brouillon. Relancez, précisez, corrigez."),
    ("Je vérifie les faits", "Chiffres, dates, noms, citations, références : contrôlez à la source."),
    ("Je protège les données", "Appliquez le feu tricolore : rien de rouge dans un outil non validé."),
    ("J'anonymise par défaut", "Remplacez noms et montants sensibles par [CLIENT A], [MONTANT]."),
    ("Je garde la décision", "L'IA propose, vous décidez. Les décisions sur des personnes restent humaines."),
    ("Je relis avant d'envoyer", "Tout ce qui part sous votre nom doit être relu et assumé."),
    ("Je capitalise mes prompts", "Gardez vos meilleurs prompts dans un document : ils deviennent vos modèles."),
    ("Je reste curieux", "Testez un nouvel usage chaque semaine : la compétence vient de la pratique."),
]

# ------------------------------------------------------------------ QUIZ
QUIZZES = {
 1: dict(thanks_title="Merci pour cette première exploration !",
         thanks="Vous venez de lever le voile sur ce qui se passe « derrière l'écran ». Prenons deux minutes pour vérifier que les idées clés sont bien ancrées.",
         questions=[
    dict(q="Qu'est-ce qui distingue l'IA générative des autres formes d'IA ?",
         options=["Elle stocke les données de l'entreprise de façon sécurisée", "Elle produit du contenu nouveau (texte, image, son…) à partir d'une demande", "Elle garantit des réponses exactes, comme une encyclopédie", "Elle ne sait faire que des calculs mathématiques"],
         answer=1, why="L'IA générative crée un contenu nouveau (un texte, une image…) en réponse à une demande formulée en langage courant. Elle ne garantit pas l'exactitude.",
         tip="« Générative » = qui génère, qui produit."),
    dict(q="Pourquoi un assistant IA peut-il affirmer une information fausse avec beaucoup d'assurance ?",
         options=["Parce qu'il ment volontairement pour satisfaire l'utilisateur", "Parce que l'utilisateur a mal configuré son ordinateur", "Parce qu'il produit la suite de mots la plus probable, sans vérifier si elle est vraie", "Parce qu'il est obligatoirement connecté à des sites peu fiables"],
         answer=2, why="Le modèle prédit des mots plausibles. Une phrase peut être parfaitement plausible… et fausse. Il n'y a ni intention de mentir, ni vérification automatique.",
         tip="Plausible ne veut pas dire vrai."),
    dict(q="Vous avez besoin du taux de change euro/dollar d'aujourd'hui pour un devis. Quel est le meilleur réflexe ?",
         options=["Demander à n'importe quel assistant IA et reprendre le chiffre tel quel", "Demander à l'IA d'estimer un taux « raisonnable »", "Renoncer : aucun outil numérique ne peut aider", "Utiliser une source à jour (outil avec recherche web ou site officiel) et contrôler la source citée"],
         answer=3, why="Une information récente et chiffrée exige une source à jour. Un assistant sans accès web s'appuie sur des données d'entraînement datées ; même avec recherche web, on ouvre la source.",
         tip="Information récente ou chiffrée = source vérifiable."),
 ]),
 2: dict(thanks_title="Merci pour votre attention !",
         thanks="Vous avez sans doute déjà repéré une ou deux tâches de votre quotidien qui pourraient changer. Vérifions maintenant que la logique « humain + IA » est claire.",
         questions=[
    dict(q="Parmi ces tâches, laquelle ne doit PAS être confiée entièrement à une IA ?",
         options=["Proposer trois plans possibles pour un rapport", "Décider seule du licenciement d'un collaborateur", "Résumer un compte rendu de cinq pages", "Reformuler un email jugé trop sec"],
         answer=1, why="Les décisions qui touchent des personnes, engagent l'entreprise ou demandent un jugement éthique restent humaines. L'IA peut aider à préparer, jamais décider à votre place.",
         tip="L'IA prépare, l'humain décide."),
    dict(q="Dans le cycle de travail présenté (Cadrer → Produire → Vérifier → Décider), qui est responsable du résultat final ?",
         options=["L'IA, puisqu'elle a rédigé le texte", "L'éditeur du logiciel d'IA", "La personne qui utilise l'IA et diffuse le résultat", "Personne : c'est un contenu automatique"],
         answer=2, why="Ce que vous envoyez, publiez ou présentez engage votre responsabilité et celle de votre entreprise, quel que soit l'outil utilisé pour le préparer.",
         tip="Votre nom, votre responsabilité."),
    dict(q="Un commercial doit répondre à une réclamation client délicate. Quelle utilisation de l'IA est la plus pertinente ?",
         options=["Copier tout l'historique du client, coordonnées bancaires comprises, pour être précis", "Laisser l'IA décider seule du geste commercial à accorder", "Envoyer la réponse générée sans la relire pour gagner du temps", "Décrire la situation sans données sensibles, demander un brouillon empathique, puis l'ajuster et vérifier les engagements"],
         answer=3, why="C'est l'usage idéal : contexte utile mais anonymisé, brouillon de qualité, puis contrôle humain des promesses faites au client.",
         tip="Contexte utile, données protégées, relecture obligatoire."),
 ]),
 3: dict(thanks_title="Bravo, vous avez la méthode !",
         thanks="Vous venez d'acquérir la compétence qui fait la plus grande différence dans l'usage de l'IA. Voyons si le PILOTE est bien aux commandes !",
         questions=[
    dict(q="Dans la méthode PILOTE, que signifie la lettre « O » ?",
         options=["Objectif : le résultat que vous voulez atteindre", "Organisation : le plan du document", "Orthographe : le niveau de langue", "Option : les variantes proposées"],
         answer=0, why="L'Objectif explique POURQUOI vous faites la demande. Il permet à l'IA d'orienter sa réponse vers le résultat utile (convaincre, informer, décider…).",
         tip="P-I-L-O-T-E : Persona, Informations, Livrable, Objectif, Ton, Exigences."),
    dict(q="Le prompt « Fais-moi un résumé » donne un résultat décevant. Quel ajout améliore le plus la réponse ?",
         options=["Ajouter « s'il te plaît » et « merci »", "Écrire la demande en majuscules", "Préciser pour qui, dans quel but et sous quel format (ex. : 5 puces pour mon directeur, pour décider vendredi)", "Répéter trois fois la même demande"],
         answer=2, why="Le destinataire, l'objectif et le format transforment un résumé générique en un livrable utile. La politesse ne nuit pas, mais elle n'apporte pas d'information.",
         tip="Pour qui ? Pour quoi ? Sous quelle forme ?"),
    dict(q="La première réponse est correcte, mais trop longue et trop formelle. Quelle est la meilleure réaction ?",
         options=["Conclure que l'IA ne fonctionne pas", "Relancer dans la même conversation : « Réduis à 120 mots, ton plus chaleureux, garde les 3 points clés »", "Ouvrir une nouvelle conversation et reposer la même question", "Tout réécrire soi-même depuis le début"],
         answer=1, why="L'IA garde le contexte de la conversation : une relance précise est le moyen le plus rapide d'obtenir le bon résultat. C'est l'itération.",
         tip="La 1re réponse est un brouillon : on itère."),
 ]),
 4: dict(thanks_title="Merci d'avoir joué le jeu de l'atelier !",
         thanks="Vous avez vu une vraie conversation de travail, avec ses réussites… et ses pièges. Assurons-nous que la démarche est bien acquise.",
         questions=[
    dict(q="Avant de demander un compte rendu à l'IA, quelle est l'étape la plus importante ?",
         options=["Choisir la police et la mise en page du document", "Demander le résultat le plus long possible", "Fournir les notes brutes et le contexte de la réunion", "Traduire les notes en anglais"],
         answer=2, why="Sans matière première (notes, participants, enjeux), l'IA ne peut que produire un texte générique ou inventer. Le contexte est le carburant.",
         tip="Pas de contexte, pas de qualité."),
    dict(q="Dans la démonstration, l'IA attribue à Marc l'information des 20 plus gros clients, alors que ce point n'a pas été tranché. Que retenir ?",
         options=["Qu'il faut toujours comparer le résultat aux notes d'origine avant de le diffuser", "Que l'IA est inutilisable pour les comptes rendus", "Que Marc doit forcément s'en charger", "Qu'il s'agit d'un bug rare qui ne se reproduira pas"],
         answer=0, why="Les IA « comblent les vides » de façon plausible. Ce type d'erreur est fréquent : la vérification ligne à ligne contre la source est indispensable.",
         tip="Ce qui n'est pas dans la source ne doit pas apparaître dans le résultat."),
    dict(q="Quel enchaînement reflète la bonne méthode de travail avec l'IA ?",
         options=["Prompt → envoi immédiat du résultat", "Vérification → prompt → envoi", "Contexte → demande → observation → amélioration → vérification → utilisation", "Utilisation → vérification éventuelle plus tard"],
         answer=2, why="C'est le cycle vu en atelier : on prépare, on demande, on observe, on améliore, on vérifie, puis seulement on utilise.",
         tip="On ne diffuse jamais un premier jet."),
 ]),
 5: dict(thanks_title="Merci, vous voilà utilisateur averti !",
         thanks="Utiliser l'IA, c'est bien ; l'utiliser avec discernement, c'est ce qui fait les vrais professionnels. Dernier quiz : à vous de jouer !",
         questions=[
    dict(q="Qu'appelle-t-on une « hallucination » d'IA ?",
         options=["Un bug d'affichage de l'application", "Un refus de l'IA de répondre", "Une réponse inventée mais présentée de façon crédible", "Un virus informatique transmis par l'IA"],
         answer=2, why="L'IA peut inventer une source, un chiffre, une loi ou une citation avec un ton parfaitement assuré. D'où la nécessité de vérifier.",
         tip="Une référence citée par l'IA = une référence à ouvrir."),
    dict(q="Selon le feu tricolore des données, quelle information est classée ROUGE (jamais dans un outil public) ?",
         options=["Un communiqué de presse déjà publié", "La liste nominative des salaires de l'équipe", "Un modèle de lettre de relance générique", "Un article de blog public sur votre secteur"],
         answer=1, why="Les données personnelles et sensibles (salaires nominatifs, santé, coordonnées bancaires…) ne doivent jamais être saisies dans un outil non validé par l'entreprise.",
         tip="Si sa fuite poserait problème, c'est rouge."),
    dict(q="Dans la règle « Vrai – Juste – Signable », que signifie « Juste » ?",
         options=["Que la réponse est adaptée à votre contexte, à votre destinataire et à vos règles internes", "Que l'orthographe est parfaite", "Que la réponse est courte", "Que la réponse a été produite rapidement"],
         answer=0, why="Une réponse peut être vraie en général mais inadaptée à votre situation. « Juste » vérifie la pertinence pour VOTRE contexte.",
         tip="Vrai = les faits. Juste = le contexte. Signable = l'engagement."),
 ]),
}

# ------------------------------------------------------------------ CAS ENTREPRISE (chap. 2)
FUNCTIONS = [
    ("Administration", "clipboard-list", "Rédiger notes, courriers, procédures", "Transformer des consignes orales en procédure claire en 5 étapes"),
    ("Comptabilité & finance", "calculator", "Expliquer des écarts, préparer des commentaires", "Rédiger le commentaire d'un écart budgétaire à partir de chiffres fournis"),
    ("Ressources humaines", "users", "Fiches de poste, onboarding, questions d'entretien", "Créer une fiche de poste et une grille d'entretien structurée"),
    ("Marketing & communication", "megaphone", "Posts, newsletters, idées de campagne", "Décliner un message en 3 posts adaptés à LinkedIn, Facebook, email"),
    ("Vente & relation client", "handshake", "Emails, offres, réponses aux objections", "Préparer les réponses aux 5 objections les plus fréquentes"),
    ("Direction & management", "landmark", "Synthèses, décisions, communication interne", "Résumer 3 rapports en une note de décision d'une page"),
    ("Gestion de projet", "kanban", "Plannings, comptes rendus, risques", "Transformer un compte rendu en tableau d'actions"),
    ("Entrepreneuriat", "rocket", "Business plan, offre, prospection", "Tester une idée d'offre face à 3 profils de clients types"),
    ("Recherche & analyse", "scan-search", "Synthèses, comparaisons, veille", "Comparer 3 fournisseurs selon des critères définis"),
    ("Formation & apprentissage", "graduation-cap", "Expliquer, créer des quiz, s'entraîner", "Apprendre une notion nouvelle avec exemples et auto-évaluation"),
]

BEFORE_AFTER = [
    dict(title="Administration — le rapport mensuel d'activité", icon="file-text",
         before=["Page blanche, données éparpillées", "Structure réinventée chaque mois", "Environ 45 min de rédaction*"],
         after=["Vous fournissez les chiffres clés et les faits marquants", "L'IA propose une structure et un premier jet", "Vous complétez, vérifiez les chiffres : environ 15 min*"],
         prompt="À partir de ces éléments [COLLER], rédige le rapport mensuel d'activité en 4 sections : faits marquants, indicateurs, difficultés, actions du mois prochain. 1 page maximum."),
    dict(title="Vente — la réclamation client délicate", icon="handshake",
         before=["Client mécontent, email sous le coup de l'émotion", "Risque de ton défensif", "Plusieurs versions réécrites"],
         after=["Situation décrite sans données sensibles", "Brouillon empathique, structuré, avec solution", "Vous validez le geste commercial et les engagements"],
         prompt="Un client [TYPE] se plaint de [PROBLÈME]. Rédige une réponse empathique en 3 paragraphes : reconnaissance, explication factuelle, solution proposée : [SOLUTION]. Ton : calme et professionnel."),
    dict(title="Finance — expliquer un écart budgétaire", icon="calculator",
         before=["Tableau de chiffres difficile à commenter", "Note de synthèse longue à formuler", "Message peu lisible pour la direction"],
         after=["Vous fournissez les chiffres agrégés (sans données sensibles)", "L'IA propose des hypothèses d'explication et une note claire", "Vous validez les causes réelles et recalculez les écarts"],
         prompt="Voici le budget et le réalisé par poste [COLLER]. Calcule les écarts, classe-les par importance et propose une note de 10 lignes pour la direction. Indique clairement ce qui est une hypothèse."),
]

# ------------------------------------------------------------------ GLOSSAIRE
GLOSSARY = [
    ("Intelligence artificielle (IA)", "Ensemble de techniques permettant à une machine de réaliser des tâches qui demandent habituellement l'intelligence humaine : reconnaître, prédire, classer, produire."),
    ("IA générative", "IA capable de produire un contenu nouveau (texte, image, son, vidéo, code) à partir d'une demande."),
    ("Modèle de langage (LLM)", "Programme entraîné sur d'immenses volumes de textes pour prédire la suite la plus probable d'un texte. C'est le « moteur » de ChatGPT, Claude, Gemini, Copilot, Mistral…"),
    ("Assistant IA / chatbot", "Interface conversationnelle qui permet de dialoguer avec un modèle de langage."),
    ("Prompt", "La demande, l'instruction ou la question que vous adressez à l'IA."),
    ("Prompt Engineering", "L'art de formuler des demandes claires et structurées pour obtenir des réponses utiles et fiables."),
    ("Contexte (fenêtre de contexte)", "Tout ce que l'IA « a sous les yeux » dans la conversation en cours : vos messages, les documents fournis, ses réponses précédentes. Sa taille est limitée."),
    ("Token", "Unité de texte (morceau de mot) que le modèle traite. Les limites d'usage et de longueur s'expriment souvent en tokens."),
    ("Hallucination", "Réponse inventée mais présentée comme exacte : fausse référence, chiffre erroné, citation inexistante."),
    ("Entraînement", "Phase durant laquelle le modèle apprend à partir de très grands volumes de données. Ses connaissances s'arrêtent à une date donnée."),
    ("Biais", "Déformation systématique des réponses, héritée des données d'entraînement (stéréotypes, sur-représentation de certains points de vue)."),
    ("Itération", "Le fait d'améliorer une réponse par relances successives dans la même conversation."),
    ("Multimodal", "Se dit d'une IA capable de traiter plusieurs types de contenus : texte, images, audio, documents, vidéo."),
    ("Agent IA", "Système d'IA capable d'enchaîner plusieurs actions de façon autonome (chercher, remplir, envoyer) pour atteindre un objectif, sous supervision."),
    ("Automatisation (no-code)", "Outils (Make, n8n, Zapier…) qui relient des applications entre elles pour exécuter des tâches répétitives automatiquement."),
    ("Données sensibles", "Informations dont la divulgation causerait un préjudice : données personnelles, santé, salaires, données financières non publiques, secrets d'affaires."),
    ("Anonymisation", "Remplacement des éléments identifiants (noms, adresses, montants précis) par des marqueurs neutres avant de soumettre un texte à l'IA."),
    ("Recherche augmentée (web / documents)", "Capacité d'un assistant à consulter des sources externes (web, vos fichiers) avant de répondre, et idéalement à les citer."),
]
