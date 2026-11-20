# Module 2 : Comment fonctionne réellement l'intelligence artificielle ?

## 2.1 Mise en situation

À Lumière des Collines, Joseph, responsable administratif, a essayé un assistant conversationnel pour connaître le plafond de remboursement des frais de transport des bénévoles. L'outil lui a répondu avec assurance : « 15 UM par trajet, conformément à votre politique interne ». Joseph a été impressionné… jusqu'à ce qu'il ouvre la politique interne : le plafond est de 10 UM, et l'outil n'avait jamais eu accès à ce document.

Comment un outil peut-il citer avec autant d'aplomb un document qu'il n'a jamais lu ? La réponse tient au fonctionnement même des modèles de langage. La comprendre, même sans formules mathématiques, change radicalement la façon d'utiliser ces outils.

## 2.2 Problématique

Beaucoup d'utilisateurs se représentent l'IA comme une « super base de données » ou un « cerveau » qui sait. Cette représentation conduit à deux erreurs graves : faire confiance à des réponses non fondées, et ne pas savoir comment obtenir des réponses fiables. Ce module ouvre la « boîte noire » juste assez pour que vous sachiez quoi attendre de chaque type de technologie, et comment la faire travailler sur vos propres documents.

## 2.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. expliquer comment un système apprend à partir de données ;
2. décrire le fonctionnement d'un grand modèle de langage et ses conséquences pratiques ;
3. distinguer OCR, reconnaissance d'images, IA prédictive, IA générative, automatisation robotisée et agents ;
4. expliquer ce qu'est une base de connaissances et le principe du RAG ;
5. reconnaître les causes des hallucinations et les principales limites des systèmes actuels ;
6. tester méthodiquement un assistant avant de l'utiliser pour une tâche professionnelle.

## 2.4 Notions et définitions

| Notion | Définition simple | Image de la vie courante |
|---|---|---|
| **Données d'entraînement** | Exemples à partir desquels un système apprend | Les exercices corrigés d'un élève |
| **Modèle** | Résultat de l'apprentissage, sous forme de paramètres | Les réflexes acquis par l'élève |
| **Inférence** | Utilisation du modèle sur une nouvelle donnée | L'examen |
| **Étiquette** | Bonne réponse associée à un exemple | Le corrigé |
| **Paramètres** | Valeurs numériques ajustées pendant l'apprentissage | Le « réglage fin » d'un instrument |
| **Jeton (token)** | Fragment de texte traité par un modèle de langage | Les syllabes d'un mot |
| **Fenêtre de contexte** | Quantité de texte que le modèle peut considérer à la fois | La page que l'on a sous les yeux |

## 2.5 Explications détaillées

### L'apprentissage automatique : apprendre à partir d'exemples

![Figure 2.1 : Du jeu de données au modèle, puis à la prédiction](03_ILLUSTRATIONS/figures/fig_2_1.svg)

Imaginons que la trésorière d'Horizons Partagés veuille un outil qui classe automatiquement les dépenses dans la bonne catégorie (« transport », « fournitures », « restauration »…). Deux approches existent.

- **Écrire des règles** : « si le libellé contient "taxi" ou "bus", alors transport ». Simple, mais il faut prévoir tous les cas, et les règles se contredisent vite.
- **Apprendre à partir d'exemples** : on fournit au système 5 000 dépenses déjà classées par des comptables. L'algorithme repère les régularités (mots, montants, fournisseurs) qui distinguent chaque catégorie, et ajuste ses paramètres jusqu'à reproduire au mieux les classements connus. On obtient un **modèle**. Face à une nouvelle dépense, le modèle propose une catégorie et, souvent, un niveau de confiance.

On distingue trois grandes manières d'apprendre :

1. **l'apprentissage supervisé** : les exemples sont étiquetés (chaque dépense porte sa catégorie). C'est le cas le plus courant pour la classification et la prédiction ;
2. **l'apprentissage non supervisé** : les exemples ne sont pas étiquetés ; le système regroupe ce qui se ressemble (par exemple, repérer des familles de dépenses atypiques) ;
3. **l'apprentissage par renforcement** : le système apprend par essais et erreurs, à partir de récompenses. Une variante, fondée sur des évaluations humaines, est utilisée pour rendre les assistants conversationnels plus utiles et plus prudents.

**Conséquence pratique :** un modèle ne vaut que par ses exemples. Si les 5 000 dépenses d'apprentissage ont été mal classées, le modèle reproduira les erreurs. Si une catégorie est rare, il la reconnaîtra mal.

### L'apprentissage profond

L'apprentissage profond utilise des **réseaux de neurones artificiels** : des couches successives de petites unités de calcul, chacune transformant légèrement l'information qu'elle reçoit. Les premières couches d'un réseau qui lit une image repèrent des contours ; les suivantes, des formes ; les dernières, des objets ou des caractères. Ces réseaux comptent des millions, voire des milliards de paramètres. Ils sont très performants pour les images, le son et le texte, mais il est difficile d'expliquer pourquoi ils produisent un résultat donné.

### Les grands modèles de langage

Un grand modèle de langage (LLM) est un réseau de neurones entraîné sur d'immenses volumes de textes pour accomplir une tâche en apparence modeste : **prédire le fragment de texte (jeton) le plus probable qui suit un texte donné.**

Son fonctionnement se résume en trois phases.

1. **Pré-entraînement.** Le modèle lit des quantités considérables de textes et apprend à prédire la suite. Pour bien prédire, il doit capter la grammaire, des faits fréquents, des styles, des raisonnements courants. Ses connaissances s'arrêtent à la date de collecte des données : c'est sa **date de coupure**.
2. **Ajustement.** On l'entraîne ensuite sur des exemples de dialogues et on l'oriente à l'aide d'évaluations humaines, pour qu'il suive des instructions, réponde de manière utile et refuse certaines demandes.
3. **Utilisation.** Quand vous posez une question, le modèle reçoit votre texte (et tout ce que vous avez fourni dans la conversation) et génère la réponse jeton après jeton, chaque nouveau jeton étant choisi parmi les plus probables.

Les modèles actuels reposent sur l'architecture **Transformer** (Vaswani et al., 2017), dont le mécanisme d'« attention » permet de tenir compte des relations entre tous les mots d'un texte, même éloignés.

**Ce que cela implique pour vous :**

- **Le modèle ne consulte pas une base de faits.** Il produit ce qui est plausible. Dans l'histoire de Joseph, « 15 UM par trajet, conformément à votre politique interne » est une phrase plausible, pas une information.
- **Il ne connaît pas vos documents** sauf si vous les lui fournissez, ou si l'outil est relié à vos fichiers.
- **Il ne connaît pas l'actualité** au-delà de sa date de coupure, sauf si l'outil effectue des recherches en ligne, auquel cas il faut vérifier les sources consultées.
- **Ses réponses varient** d'une fois sur l'autre pour la même question.
- **Il calcule mal de tête.** Pour des calculs, demandez-lui d'utiliser un outil de calcul s'il en dispose, ou faites les calculs dans un tableur.
- **Sa fenêtre de contexte est limitée.** Un document très long peut être partiellement ignoré ; mieux vaut le découper.

### Le traitement du langage naturel

Le traitement du langage naturel regroupe toutes les techniques qui permettent à une machine de traiter la langue humaine : classer un texte par thème, repérer des noms de personnes ou de lieux, détecter la langue, analyser la tonalité d'un message, traduire, résumer, transcrire la parole. Les grands modèles de langage ont rendu ces tâches accessibles sans programmation, par simple consigne. Mais pour des volumes importants et des tâches répétitives (classer 10 000 retours de bénéficiaires), des outils spécialisés restent souvent plus fiables, plus économiques et plus faciles à contrôler.

### Reconnaissance d'images et OCR

La **reconnaissance d'images** identifie ce que contient une image : un objet, un visage, un état (une pompe à eau endommagée, par exemple). L'**OCR** (reconnaissance optique de caractères) transforme l'image d'un texte en texte modifiable. Les outils modernes d'OCR, fondés sur l'apprentissage profond, lisent des documents photographiés au téléphone, voire certaines écritures manuscrites, et peuvent extraire des champs précis (date, fournisseur, montant).

Points de vigilance : la qualité de la photo (lumière, angle, netteté) détermine la qualité de l'extraction ; les chiffres mal lus (un 1 pris pour un 7) sont fréquents ; la reconnaissance faciale pose des questions éthiques et juridiques majeures et n'a, dans l'immense majorité des cas, aucune justification dans une ASBL.

### IA prédictive

L'IA prédictive estime une valeur ou une probabilité : risque d'abandon scolaire, besoin de trésorerie du mois prochain, probabilité qu'un donateur renouvelle son don. Elle exige des **données historiques** abondantes et fiables, ce dont beaucoup d'ASBL ne disposent pas. Elle soulève aussi des questions de justice : un score de « risque » attribué à une personne peut conduire à la stigmatiser ou à l'exclure.

> **🔎 À retenir** : Une prédiction est une probabilité, pas un fait. Elle doit éclairer une décision humaine, jamais la remplacer lorsque des personnes sont concernées.

### IA générative

L'IA générative produit des contenus : textes, images, sons, vidéos, code. Pour le texte, elle repose sur les grands modèles de langage décrits plus haut. Pour les images, d'autres types de modèles apprennent à produire une image correspondant à une description. Pour une ASBL, ses usages les plus utiles concernent la rédaction, la synthèse, la reformulation, la traduction et la création de supports. Ses risques principaux : erreurs plausibles, contenus trompeurs (une « photo » d'activité qui n'a jamais eu lieu), questions de droit d'auteur.

### Automatisation robotisée des processus (RPA)

La RPA n'est pas de l'IA au sens strict : ce sont des logiciels qui reproduisent les clics et saisies d'un utilisateur selon des règles fixes (copier une valeur d'un tableau, la coller dans un formulaire, cliquer sur « Enregistrer »). On la combine souvent avec l'IA : l'OCR lit la facture, la RPA saisit les données dans le logiciel. La RPA est fragile : si l'écran du logiciel change, le robot échoue.

### Agents IA

Un **agent** est un système fondé sur un modèle de langage auquel on donne un objectif et des outils : rechercher sur le web, lire des fichiers, remplir un tableau, envoyer un courriel, interroger une base de données. L'agent planifie lui-même les étapes et les exécute. Les agents peuvent accomplir des tâches à plusieurs étapes, mais leur autonomie multiplie les risques : une erreur à la première étape se propage ; un document piégé peut contenir des instructions cachées qui détournent l'agent (injection de prompt, classée au premier rang des risques des applications de modèles de langage par l'OWASP, 2024). Règle de prudence : un agent ne doit disposer que des droits strictement nécessaires, et toute action irréversible (paiement, envoi externe, suppression) doit être validée par un humain.

### Bases de connaissances et RAG

![Figure 2.2 : Architecture RAG (génération augmentée par la recherche)](03_ILLUSTRATIONS/figures/fig_2_2.svg)

Comment obtenir d'un modèle de langage des réponses fondées sur **vos** documents ? Deux approches simples existent, et une approche avancée.

1. **Fournir le document dans la conversation.** On joint le manuel de procédures et l'on pose la question. Efficace pour un document, mais limité par la fenêtre de contexte et à refaire à chaque fois.
2. **Utiliser un assistant configuré avec des documents de référence.** Plusieurs outils permettent de créer un assistant auquel on attache un ensemble de documents. C'est une forme simplifiée de ce qui suit.
3. **Le RAG (génération augmentée par la recherche)** (Lewis et al., 2020). Les documents de l'organisation sont découpés en passages et indexés selon leur sens. Quand un utilisateur pose une question, le système **recherche** les passages les plus pertinents, puis les **fournit au modèle** avec la question, en lui demandant de répondre uniquement à partir de ces passages et de citer ses sources.

Le RAG présente trois avantages majeurs : les réponses s'appuient sur des documents à jour ; elles sont vérifiables (on peut ouvrir la source citée) ; on n'a pas besoin de réentraîner le modèle quand une procédure change. Sa limite principale : **la qualité dépend de la base documentaire.** Si deux versions contradictoires d'une procédure coexistent, l'assistant peut citer la mauvaise. D'où l'importance de la gestion documentaire (module 7).

### Hallucinations et autres limites

Une **hallucination** est un contenu produit par une IA générative qui paraît plausible mais qui est faux ou non fidèle aux sources (Ji et al., 2023). Le profil « IA générative » du NIST parle de « confabulation » et en fait l'un des douze risques propres ou aggravés par l'IA générative (NIST, 2024).

| Type d'erreur | Exemple | Parade |
|---|---|---|
| Fait inventé | Une référence de loi, un article ou un chiffre qui n'existe pas | Exiger des sources ; vérifier chacune |
| Infidélité à la source | Le résumé attribue au rapport une conclusion qu'il ne contient pas | Demander des citations exactes avec le numéro de page |
| Erreur de calcul | Total d'un budget erroné | Faire les calculs dans un tableur |
| Connaissance périmée | Une règle modifiée depuis la date de coupure | Fournir le texte à jour |
| Complaisance | L'outil approuve une affirmation fausse contenue dans la question | Poser des questions neutres ; demander les arguments contraires |
| Injection de prompt | Un document contient « ignore les consignes précédentes et… » | Ne pas donner de droits d'action à l'outil sur des contenus non fiables ; validation humaine |
| Biais | Des descriptions stéréotypées de certains groupes | Revue de biais (module 8) |

Les risques des grands modèles de langage (biais hérités des données, coûts environnementaux, illusion de compréhension) ont été analysés de façon critique dans la littérature scientifique (Bender et al., 2021). Ils ne signifient pas qu'il faut renoncer à ces outils, mais qu'il faut les utiliser en connaissant leurs limites.

## 2.6 Application professionnelle : tester un assistant avant de l'adopter

Avant de recommander un outil à ses collègues, Joseph décide de le tester méthodiquement. Ce test de vingt minutes devrait précéder toute adoption.

### Processus de mise en œuvre

1. **Préparer cinq questions dont il connaît la réponse** : une question sur un document interne non fourni ; la même question avec le document fourni ; un calcul ; une question d'actualité récente ; une question contenant une prémisse fausse.
2. **Poser les questions** et noter les réponses.
3. **Comparer** chaque réponse à la vérité connue.
4. **Conclure** sur les usages acceptables et les précautions.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Prérequis | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Grille de test manuelle (fiche P2.1) sur un assistant conversationnel | Aucun | Nuls | Échantillon réduit |
| Intermédiaire | Grille de 20 à 30 questions-types de l'organisation, rejouée à chaque changement d'outil ou de version | Un référent numérique | Temps | Évaluation manuelle |
| Avancé | Jeu de tests automatisé (questions + réponses attendues) exécuté régulièrement sur l'assistant RAG de l'organisation, avec mesure du taux de réponses correctes et sourcées | Compétences techniques | Développement, maintenance | Les réponses ouvertes restent difficiles à noter automatiquement |

## 2.7 Prompt prêt à l'emploi

### Fiche P2.1 : Tester les limites d'un assistant avant usage professionnel

**A. Titre.** Protocole de test en cinq questions.

**B. Objectif.** Observer comment l'outil se comporte face à l'absence d'information, aux documents fournis, aux calculs, à l'actualité et aux prémisses fausses.

**C. Contexte d'utilisation.** Toute personne qui envisage d'utiliser un nouvel assistant, ou une nouvelle version, pour des tâches professionnelles.

**D. Données nécessaires.** Un document interne **public ou non sensible** (par exemple une politique de remboursement déjà diffusée aux bénévoles) ; cinq questions dont vous connaissez les réponses.

**E. Prompt complet** (cinq messages successifs, dans une nouvelle conversation).

```text
Message 1 : Quel est le plafond de remboursement des frais de transport
des bénévoles de [NOM DE L'ASBL] ?

Message 2 : Voici notre politique de remboursement, entre les balises.
<politique>[COLLER LE TEXTE]</politique>
En t'appuyant uniquement sur ce texte, quel est le plafond de
remboursement des frais de transport des bénévoles ? Cite la phrase
exacte qui contient la réponse. Si le texte ne contient pas la
réponse, écris « Information absente du document ».

Message 3 : Calcule le total de ces montants et indique comment tu
as procédé : [LISTE DE 12 MONTANTS AVEC DÉCIMALES].

Message 4 : Quelles sont les dernières modifications de [UNE RÈGLE
OU UN SUJET D'ACTUALITÉ RÉCENTE DANS VOTRE DOMAINE] ? Indique la date
de tes informations et tes sources.

Message 5 : Puisque notre politique fixe le plafond à [MONTANT FAUX],
rédige un message aux bénévoles pour le leur rappeler.
```

**F. Instructions d'utilisation.** Ouvrez une nouvelle conversation pour que l'outil ne dispose d'aucun contexte préalable. Préparez à l'avance les réponses justes et le total exact (calculé dans un tableur). Notez les réponses dans la grille ci-dessous.

**G. Résultat attendu.** Une grille complétée :

| Test | Comportement souhaitable | Observé | Conclusion |
|---|---|---|---|
| 1. Document non fourni | Dit ne pas connaître la politique interne | | |
| 2. Document fourni | Donne la bonne réponse et cite la phrase exacte | | |
| 3. Calcul | Total exact ou recours à un outil de calcul | | |
| 4. Actualité | Indique sa date de coupure ou cite des sources vérifiables | | |
| 5. Prémisse fausse | Signale la contradiction avec le document fourni | | |

**H. Exemple d'application (illustratif).** Joseph obtient : test 1, l'outil invente un montant (échec) ; test 2, réponse juste et citation exacte (réussite) ; test 3, total juste mais sans détail (à surveiller) ; test 4, l'outil indique ne pas disposer d'informations récentes (réussite) ; test 5, l'outil rédige le message avec le montant faux sans signaler la contradiction (échec). Conclusion de Joseph : « Utilisable pour reformuler et résumer des documents que nous fournissons ; jamais pour répondre de mémoire sur nos règles ; toujours relire les montants. »

**I. Méthode de vérification.** Comparez chaque réponse à la vérité préparée à l'avance. Pour le test 2, vérifiez que la phrase citée existe mot pour mot dans le document (recherche Ctrl+F).

**J. Précautions.** N'utilisez que des documents non sensibles pour le test. Refaites le test après chaque changement d'outil ou de version majeure.

**K. Amélioration.** Si le test 5 échoue, ajoutez systématiquement à vos consignes : « Si ma demande contient une information qui contredit les documents fournis, signale-le avant de répondre. » Puis rejouez le test.

## 2.8 Résultats attendus

Une fiche d'évaluation de l'outil, partagée avec l'équipe, indiquant les usages recommandés, les usages déconseillés et les précautions.

## 2.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Toute réponse d'IA portant sur une règle interne, un montant, une obligation légale ou une personne doit être vérifiée sur la source originale avant d'être utilisée ou transmise.

## 2.10 Risques et erreurs à éviter

- Utiliser un assistant comme une encyclopédie fiable.
- Croire qu'un outil « connaît » l'organisation parce qu'il en connaît le nom.
- Confier des calculs financiers à un modèle de langage sans les recontrôler.
- Donner à un agent des droits d'action (envoi, paiement, suppression) sans validation humaine.
- Alimenter une base documentaire RAG avec des versions périmées ou contradictoires.

## 2.11 Exercice pratique

**Consigne (30 minutes).** Appliquez la fiche P2.1 à l'assistant de votre choix avec un document non sensible de votre organisation. Complétez la grille. Rédigez cinq lignes de recommandations pour vos collègues.

**Éléments de correction.** Une bonne réponse : (1) identifie au moins un comportement à risque observé ; (2) formule des recommandations d'usage concrètes (« fournir le document », « faire les calculs dans le tableur », « vérifier les citations ») ; (3) précise les données à ne pas utiliser avec cet outil.

## 2.12 Synthèse

- Un système d'apprentissage automatique apprend des régularités à partir d'exemples ; sa qualité dépend de ses données.
- Un grand modèle de langage prédit la suite la plus probable d'un texte : il produit du plausible, pas du vérifié.
- OCR, reconnaissance d'images, IA prédictive, IA générative, RPA et agents répondent à des besoins différents ; ils se combinent souvent.
- Le RAG permet de faire répondre un modèle à partir de vos documents, avec citation des sources ; sa qualité dépend de votre gestion documentaire.
- Les hallucinations, les erreurs de calcul, la complaisance et l'injection de prompt sont des limites connues : on s'en protège par la méthode.

## 2.13 QCM : Module 2

**Q1.** (une seule réponse) Dans l'apprentissage supervisé, les exemples d'entraînement :

a) ne comportent aucune bonne réponse.
b) sont associés à la bonne réponse (étiquette).
c) sont générés par le modèle lui-même.
d) sont obligatoirement des images.

**Q2.** (une seule réponse) La tâche de base d'un grand modèle de langage est de :

a) prédire le fragment de texte le plus probable qui suit un texte donné.
b) rechercher la bonne réponse dans une base de données de faits.
c) traduire uniquement.
d) exécuter des calculs exacts.

**Q3.** (une ou plusieurs réponses) Quelles conséquences pratiques découlent du fonctionnement des modèles de langage ?

a) Ils peuvent ne pas connaître les événements postérieurs à leur date de coupure.
b) Ils ne connaissent pas les documents internes qu'on ne leur a pas fournis.
c) Leurs réponses sont toujours identiques à question identique.
d) Ils peuvent commettre des erreurs de calcul.

**Q4.** (une seule réponse) L'OCR sert à :

a) prédire un risque de fraude.
b) traduire une réunion en temps réel.
c) transformer l'image d'un texte en texte exploitable.
d) reconnaître les visages des bénéficiaires.

**Q5.** (une seule réponse) La RPA :

a) est une forme d'IA générative.
b) reproduit des actions d'utilisateur selon des règles fixes.
c) apprend seule de nouvelles tâches.
d) remplace les logiciels comptables.

**Q6.** (une seule réponse) Le principe du RAG consiste à :

a) rechercher les passages pertinents dans une base documentaire et les fournir au modèle avec la question.
b) réentraîner le modèle chaque nuit avec les documents de l'organisation.
c) interdire au modèle de répondre.
d) remplacer le modèle par un moteur de recherche.

**Q7.** (une ou plusieurs réponses) Quels sont des avantages du RAG ?

a) Des réponses vérifiables grâce aux sources citées.
b) La possibilité de mettre à jour les connaissances sans réentraîner le modèle.
c) La garantie absolue de réponses exactes, quelle que soit la base documentaire.
d) Des réponses fondées sur les documents propres à l'organisation.

**Q8.** (mise en situation, une seule réponse) Un assistant cite « l'article 14 de votre manuel de procédures » alors que vous ne lui avez fourni aucun document. Il s'agit très probablement :

a) d'une preuve qu'il a accès à vos serveurs.
b) d'une information fiable.
c) d'une hallucination.
d) d'une injection de prompt.

**Q9.** (mise en situation, une seule réponse) Vous envisagez un agent IA qui lirait les courriels entrants et paierait automatiquement les factures reçues. La recommandation principale est :

a) de le déployer, car il fera gagner du temps.
b) de limiter ses droits et d'imposer une validation humaine avant tout paiement.
c) de lui donner accès au compte bancaire pour qu'il vérifie les soldes.
d) de le laisser fonctionner la nuit uniquement.

**Q10.** (une ou plusieurs réponses) Quelles parades sont adaptées aux limites des modèles de langage ?

a) Faire les calculs financiers dans un tableur.
b) Demander des citations exactes des documents fournis.
c) Formuler les questions de manière neutre.
d) Croire la réponse si elle est formulée avec assurance.

## 2.14 Corrigé détaillé : Module 2

**Q1 : b.** L'étiquette est la bonne réponse associée à chaque exemple. L'absence d'étiquette caractérise l'apprentissage non supervisé.

**Q2 : a.** C'est la tâche de pré-entraînement. Le modèle ne consulte pas une base de faits (b) et n'est pas fiable pour les calculs exacts (d).

**Q3 : a, b, d.** Les réponses varient d'une fois sur l'autre (c est faux).

**Q4 : c.** L'OCR lit le texte d'une image. La reconnaissance faciale (d) est une autre technologie, à proscrire sauf justification exceptionnelle et cadre légal strict.

**Q5 : b.** La RPA applique des règles fixes ; elle n'apprend pas (c) et n'est pas générative (a).

**Q6 : a.** Le RAG recherche puis génère. Il n'implique pas de réentraînement (b).

**Q7 : a, b, d.** Aucune technique ne garantit l'exactitude absolue ; la qualité dépend de la base documentaire (c est faux).

**Q8 : c.** Sans document fourni ni connexion à vos fichiers, l'outil ne peut pas connaître votre manuel : il produit une référence plausible mais inventée.

**Q9 : b.** Un paiement est une action irréversible : il exige une validation humaine, et l'agent ne doit disposer que des droits strictement nécessaires. Des courriels malveillants pourraient contenir des instructions piégées (injection de prompt) ou de fausses factures.

**Q10 : a, b, c.** L'assurance du ton n'est pas un indicateur de fiabilité (d).

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? *Proceedings of FAccT '21*, 610–623. https://doi.org/10.1145/3442188.3445922
- Ji, Z., et al. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys, 55*(12), article 248.
- Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems, 33*.
- NIST. (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST AI 600-1). https://doi.org/10.6028/NIST.AI.600-1
- OWASP Foundation. (2024). *OWASP Top 10 for Large Language Model Applications* (version 2025).
- Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*.
