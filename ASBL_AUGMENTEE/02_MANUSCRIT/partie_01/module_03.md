# Module 3 : Apprendre à utiliser et maîtriser les outils d'IA

## 3.1 Mise en situation

Grace est chargée de suivi-évaluation à Horizons Partagés. Elle utilise un assistant conversationnel depuis quelques mois, mais les résultats sont inégaux : « Parfois c'est bluffant, parfois c'est à côté de la plaque. » En regardant son historique, on comprend vite pourquoi. Ses demandes ressemblent à : « Résume ce rapport », « Fais un tableau », « Traduis en anglais ». L'outil devine alors le public, la longueur, le niveau de détail, le ton… et devine souvent mal.

Son collègue Daniel, lui, obtient des résultats réguliers. Sa méthode n'a rien de magique : il donne le contexte, précise la tâche, délimite les données, décrit le résultat attendu et fixe des limites. Puis il vérifie systématiquement.

## 3.2 Problématique

L'efficacité d'un outil d'IA dépend largement de la qualité de la consigne et de la rigueur de la vérification. Or la plupart des utilisateurs n'ont jamais été formés à ces deux compétences. Résultat : des pertes de temps, des déceptions, et parfois des erreurs qui passent inaperçues.

## 3.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. choisir le bon type d'outil selon la tâche (assistant, recherche, analyse de fichiers, tableur, traduction, présentation, image, automatisation) ;
2. rédiger des consignes efficaces avec la méthode CADRE ;
3. améliorer une consigne par itérations ;
4. vérifier une réponse avec la boucle « 6 V » ;
5. réaliser des exercices progressifs, du débutant au confirmé.

## 3.4 Notions et définitions

- **Prompt** : consigne rédigée en langage naturel et adressée à un outil d'IA.
- **Consigne système / instructions personnalisées** : instructions permanentes que l'on peut donner à certains outils (par exemple « Réponds toujours en français, de façon concise »).
- **Itération** : amélioration d'une réponse par des consignes successives dans la même conversation.
- **Exemple guidé (*few-shot*)** : un ou plusieurs exemples du résultat souhaité, fournis dans la consigne pour montrer le format attendu.
- **Délimiteurs** : balises (par exemple `<rapport>…</rapport>`) ou guillemets qui séparent clairement les instructions des données.

## 3.5 Explications détaillées

### Panorama des usages et des outils

| Usage | Type d'outil | Bon usage | Piège principal |
|---|---|---|---|
| Dialoguer, rédiger, reformuler | Assistant conversationnel | Brouillons, reformulations, plans, idées | Faits inventés |
| Recherche « intelligente » | Moteur de recherche avec synthèse par IA | Première exploration d'un sujet, avec liens vers les sources | Sources de qualité inégale, synthèse infidèle |
| Analyse de fichiers | Assistant acceptant des documents (PDF, texte, tableurs) | Résumer, comparer, extraire des informations | Passages ignorés si le document est long ; données sensibles |
| Tableurs et données | Assistant intégré au tableur, ou assistant capable d'exécuter des calculs | Formules, nettoyage, tableaux croisés, graphiques | Calculs « de tête » faux ; formules mal comprises |
| Traduction | Traducteurs automatiques, assistants | Premiers jets, compréhension | Contresens, ton inadapté, termes techniques |
| Présentations | Assistants intégrés aux logiciels de présentation | Structure, plan, première mise en page | Contenu générique ; images inappropriées |
| Création d'images | Générateurs d'images | Illustrations, pictogrammes, visuels de sensibilisation | Images trompeuses, stéréotypes, droits |
| Transcription | Outils de transcription audio | Comptes rendus, entretiens | Consentement ; erreurs sur les noms propres |
| Automatisation | Plateformes d'automatisation sans code | Enchaîner des actions entre applications | Erreurs reproduites à grande échelle |

> **📶 Faible connectivité** : Les assistants en ligne exigent une connexion. Préparez vos consignes et documents hors ligne, regroupez vos demandes en une seule session de connexion, et privilégiez les outils capables de travailler sur des fichiers que vous enregistrez ensuite localement. Certains modèles plus petits peuvent fonctionner sur un ordinateur sans connexion (niveau Avancé, module 9), au prix de performances moindres.

### La méthode CADRE

![Figure 3.1 : Anatomie d'un prompt efficace : la méthode CADRE](03_ILLUSTRATIONS/figures/fig_3_1.svg)

Une bonne consigne répond à cinq questions. Retenez l'acronyme **CADRE** :

- **C : Contexte** : qui je suis, pour qui je travaille, dans quelle situation.
- **A : Action** : ce que l'outil doit faire, avec un verbe précis (résumer, comparer, extraire, rédiger, classer, vérifier, reformuler).
- **D : Données** : ce que je fournis, clairement délimité, et la consigne de ne s'appuyer que sur ces données lorsque c'est nécessaire.
- **R : Résultat attendu** : format, longueur, structure, ton, langue, public.
- **E : Exigences et limites** : ce qu'il ne faut pas faire ; comment signaler un doute ou une information manquante.

Comparons deux consignes pour la même tâche.

*Consigne faible* : « Résume ce rapport. »

*Consigne CADRE* :

```text
[C] Je suis chargée de suivi-évaluation dans une ASBL de santé
communautaire. Ce résumé est destiné à notre directrice, qui doit
décider en 5 minutes s'il faut prolonger l'activité de dépistage.
[A] Résume le rapport ci-dessous en mettant en évidence les résultats
obtenus par rapport aux objectifs, les difficultés et les décisions
à prendre.
[D] Utilise uniquement le texte entre les balises <rapport>.
<rapport>[TEXTE]</rapport>
[R] 250 mots maximum ; 3 rubriques avec titres : « Résultats »,
« Difficultés », « Décisions à prendre » ; puis un tableau
« Indicateur | Cible | Réalisé | Écart ».
[E] N'invente aucun chiffre. Si une cible ou un résultat manque,
écris « non renseigné ». Signale toute incohérence entre deux
chiffres du rapport.
```

La seconde consigne est plus longue à écrire, une minute de plus, mais elle produit un résultat directement exploitable, vérifiable, et réutilisable comme modèle.

### Techniques complémentaires

1. **Donner un exemple du format souhaité.** « Voici un exemple de ligne attendue : `2026-03-14 | Atelier hygiène | Village A | 32 participants`. »
2. **Demander des étapes.** Pour une analyse, demandez d'abord la liste des points relevés, puis la conclusion : cela rend le raisonnement vérifiable.
3. **Demander des citations.** « Pour chaque affirmation, cite le passage du document et sa page. »
4. **Autoriser l'ignorance.** « Si tu ne sais pas, dis-le. » Cette simple phrase réduit les inventions.
5. **Découper les gros travaux.** Un rapport de 80 pages se traite chapitre par chapitre.
6. **Itérer.** Plutôt que de recommencer, corrigez : « Raccourcis la deuxième partie de moitié », « Remplace les termes techniques par des mots simples ».
7. **Réutiliser.** Enregistrez vos meilleures consignes dans une bibliothèque partagée (annexe 18).

### La boucle de vérification « 6 V »

![Figure 3.2 : La boucle de vérification d'une réponse d'IA](03_ILLUSTRATIONS/figures/fig_3_2.svg)

1. **Formuler** avec CADRE.
2. **Lire la réponse en entier**, pas seulement le début.
3. **Vérifier les faits, chiffres, noms, dates**, un par un.
4. **Confronter aux sources originales** (le document fourni, le texte officiel, le tableur).
5. **Corriger ou reformuler** la consigne si nécessaire.
6. **Valider et documenter** : qui a vérifié, quand, avec quelle source, en particulier pour les documents externes.

Le niveau de vérification doit être proportionné à l'enjeu : un brouillon de message interne demande une relecture ; un rapport financier à un bailleur, une vérification ligne par ligne.

## 3.6 Application professionnelle : trois usages quotidiens maîtrisés

Les trois fiches suivantes couvrent les usages les plus fréquents : synthèse de document, analyse de données en tableur, traduction contrôlée.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Prérequis | Coûts | Limites |
|---|---|---|---|---|---|
| Débutant | Consignes CADRE dans un assistant conversationnel ; documents non sensibles ; vérification manuelle | Assistant conversationnel, tableur, traitement de texte | Formation de 2 heures | Nuls à faibles | Offres gratuites : limites d'usage, conditions de confidentialité souvent inadaptées aux données internes |
| Intermédiaire | Assistant intégré à la suite bureautique professionnelle ; bibliothèque partagée de consignes ; documents internes autorisés selon la classification | Suite bureautique avec IA, espace documentaire partagé | Référent numérique, règles d'usage | Abonnements par utilisateur | Vérifier le contrat (non-utilisation des données pour l'entraînement, localisation) |
| Avancé | Assistants configurés par métier, reliés à la base documentaire (RAG), consignes standardisées et journalisées | Plateforme d'IA d'entreprise, API | Compétences techniques, gouvernance | Licences, intégration, maintenance | Complexité, dépendance au fournisseur |

## 3.7 Prompts prêts à l'emploi

### Fiche P3.1 : Synthèse fidèle d'un document

**A. Titre.** Synthèse décisionnelle d'un rapport.

**B. Objectif.** Obtenir une synthèse courte, fidèle et vérifiable d'un document long, orientée vers une décision.

**C. Contexte d'utilisation.** Direction, coordination, S&E, gouvernance ; avant une réunion ou une décision.

**D. Données nécessaires.** Le document (texte ou fichier) ; le public et la décision visée.

**E. Prompt complet.**

```text
Contexte : je travaille pour [NOM DE L'ASBL], [SECTEUR]. Cette synthèse
est destinée à [PUBLIC] qui doit décider de [DÉCISION].
Tâche : résume le document fourni.
Données : appuie-toi exclusivement sur le document entre les balises.
<document>[TEXTE OU FICHIER JOINT]</document>
Résultat attendu :
1. L'essentiel en 3 phrases.
2. Les points clés (5 puces maximum), chacun suivi entre parenthèses
   du numéro de page ou de section d'où il provient.
3. Les chiffres importants dans un tableau « Donnée | Valeur | Page ».
4. Les questions que le document laisse sans réponse.
Limites : n'ajoute aucune information extérieure au document. Si un
élément est ambigu, signale-le au lieu de l'interpréter. 300 mots
maximum hors tableau.
```

**F. Instructions d'utilisation.** Joignez le fichier ou collez le texte entre les balises. Pour un document de plus de 30 pages, traitez-le par parties et demandez ensuite une synthèse des synthèses.

**G. Résultat attendu.** Trois phrases, cinq puces référencées, un tableau de chiffres avec numéros de page, une liste de questions ouvertes.

**H. Exemple d'application (illustratif).** Grace synthétise un rapport d'évaluation à mi-parcours de 45 pages pour la directrice, qui doit décider de prolonger ou non le dépistage mobile. La synthèse obtenue signale notamment, comme question ouverte : « le rapport ne précise pas le coût par personne dépistée ».

**I. Méthode de vérification.** Ouvrez le document à chaque page citée et vérifiez trois points clés au minimum et **tous** les chiffres. Si une page citée ne contient pas l'information, considérez toute la synthèse comme suspecte.

**J. Précautions.** Respectez la classification du document (module 8). Un rapport contenant des données individuelles de bénéficiaires ne doit pas être soumis à un outil non validé.

**K. Amélioration.** *V1* : « Résume ce rapport. » → réponse générique, sans référence, impossible à vérifier. *V2* : la fiche ci-dessus. *Si la synthèse reste trop longue* : « Réduis à 150 mots en gardant uniquement ce qui influence la décision. »

### Fiche P3.2 : Analyser un tableau de données sans se tromper dans les calculs

**A. Titre.** Analyse assistée d'un tableau de suivi.

**B. Objectif.** Obtenir des formules de tableur fiables et une lecture des tendances, en laissant les calculs au tableur.

**C. Contexte d'utilisation.** S&E, finances, logistique ; données agrégées ou anonymisées.

**D. Données nécessaires.** La description des colonnes ; un extrait de 10 lignes **anonymisées** ; la question d'analyse.

**E. Prompt complet.**

```text
Contexte : j'utilise un tableur ([NOM DU LOGICIEL] en français) pour
suivre [OBJET]. Les colonnes sont : [A : …, B : …, C : …].
Voici un extrait anonymisé de 10 lignes :
<extrait>[LIGNES]</extrait>
Tâche :
1. Propose les formules exactes pour calculer [INDICATEURS SOUHAITÉS],
   en indiquant dans quelle cellule les placer.
2. Explique chaque formule en une phrase simple.
3. Propose un tableau croisé dynamique ou un graphique adapté.
4. Liste les contrôles de cohérence à effectuer sur les données
   (doublons, valeurs manquantes, valeurs aberrantes).
Limites : ne calcule pas toi-même les résultats sur l'extrait ;
je les calculerai dans le tableur. Utilise le séparateur
d'arguments « ; ».
```

**F. Instructions d'utilisation.** Remplacez noms et identifiants par des codes avant de coller l'extrait. Copiez les formules dans le tableur ; testez-les sur deux ou trois lignes dont vous connaissez le résultat.

**G. Résultat attendu.** Une liste de formules prêtes à coller, leurs explications, une proposition de visualisation et une liste de contrôles.

**H. Exemple d'application (illustratif).** Lumière des Collines suit l'assiduité de 120 élèves (colonnes : code élève, classe, mois, jours présents, jours prévus). L'assistant propose par exemple la formule `=SOMME.SI.ENS(D:D;B:B;"CM1";C:C;"mars")/SOMME.SI.ENS(E:E;B:B;"CM1";C:C;"mars")` pour le taux d'assiduité d'une classe sur un mois, ainsi qu'un contrôle des lignes où les jours présents dépassent les jours prévus.

**I. Méthode de vérification.** Calculez manuellement un résultat sur un petit sous-ensemble et comparez. Vérifiez que les plages de cellules correspondent bien à vos colonnes. Contrôlez les noms de fonctions selon la langue de votre logiciel.

**J. Précautions.** Jamais de données nominatives d'élèves ou de bénéficiaires dans un outil non validé. Le code élève doit être non signifiant (pas d'initiales + date de naissance).

**K. Amélioration.** Si les formules ne fonctionnent pas, transmettez le message d'erreur exact et la version de votre logiciel : « La formule renvoie #NOM?. J'utilise [LOGICIEL ET VERSION] en français. »

### Fiche P3.3 : Traduction contrôlée d'un support destiné aux communautés

**A. Titre.** Traduction adaptée et contrôlée.

**B. Objectif.** Produire un premier jet de traduction compréhensible par le public visé, et identifier les passages à faire valider par un locuteur natif.

**C. Contexte d'utilisation.** Communication, programmes, terrain.

**D. Données nécessaires.** Le texte source ; la langue cible ; le public (niveau de lecture, contexte culturel) ; un glossaire des termes clés si disponible.

**E. Prompt complet.**

```text
Contexte : ce texte est un support de sensibilisation de [NOM DE
L'ASBL] destiné à [PUBLIC : âge, niveau de lecture, contexte].
Tâche : traduis-le du [LANGUE SOURCE] vers le [LANGUE CIBLE].
Données : <texte>[TEXTE]</texte>
Glossaire imposé : [TERME SOURCE = TERME CIBLE ; …]
Résultat attendu :
1. La traduction, avec des phrases courtes et un vocabulaire courant.
2. Un tableau des passages délicats : « Passage | Difficulté
   (terme technique, expression culturelle, ambiguïté) | Choix
   effectué | Alternative ».
Limites : ne modifie pas le sens des messages de santé ou de sécurité.
Si un terme n'a pas d'équivalent clair, conserve le terme d'origine
et signale-le.
```

**F. Instructions d'utilisation.** Établissez le glossaire avec l'équipe de terrain. Si la langue cible est peu représentée sur internet, attendez-vous à une qualité plus faible.

**G. Résultat attendu.** Une traduction lisible et un tableau des difficultés à arbitrer.

**H. Exemple d'application (illustratif).** Horizons Partagés traduit une affiche sur le traitement de l'eau à domicile. Le tableau signale que l'expression « eau potable » a deux traductions possibles dans la langue cible, l'une signifiant « eau claire », ce qui pourrait induire en erreur.

**I. Méthode de vérification.** Faites relire par au moins un locuteur natif issu du public visé ; pour les messages de santé, par un professionnel de santé. Technique de la **rétro-traduction** : faites retraduire le texte vers la langue d'origine par une autre personne ou un autre outil et comparez le sens.

**J. Précautions.** Une traduction automatique non relue ne doit jamais être diffusée pour un message de santé, de sécurité ou de droits.

**K. Amélioration.** Si le registre est trop soutenu : « Réécris pour un public qui lit difficilement : phrases de 12 mots maximum, un message par phrase. »

## 3.8 Exercices progressifs

**Niveau 1 : Découverte (20 minutes).** Rédigez avec CADRE une consigne demandant un message de remerciement à des bénévoles après une journée de collecte. Comparez le résultat avec celui d'une consigne d'une seule ligne.

**Niveau 2 : Pratique (40 minutes).** Prenez un rapport public de votre organisation. Appliquez la fiche P3.1. Vérifiez chaque chiffre. Notez le temps passé à vérifier.

**Niveau 3 : Maîtrise (60 minutes).** Construisez une bibliothèque de trois consignes pour votre métier, testez chacune trois fois, notez la stabilité des résultats, et rédigez pour chacune la méthode de vérification.

**Éléments de correction.** Le niveau 1 doit faire apparaître des différences nettes (ton, longueur, personnalisation). Le niveau 2 révèle généralement au moins une imprécision à corriger : c'est l'objectif de l'exercice. Le niveau 3 est réussi si chaque consigne comporte les cinq blocs CADRE, une méthode de vérification et une indication des données à ne pas utiliser.

## 3.9 Résultats attendus

Une pratique plus régulière et plus sûre ; une bibliothèque de consignes partagée ; une habitude de vérification proportionnée à l'enjeu.

## 3.10 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Tout document produit avec l'IA et destiné à l'extérieur (bailleur, autorités, partenaires, communautés, public) est relu et validé par une personne habilitée, qui en assume le contenu.

## 3.11 Risques et erreurs à éviter

- Recopier une réponse sans l'avoir lue entièrement.
- Mélanger instructions et données sans délimiteurs (risque de confusion et d'injection).
- Demander des calculs à un modèle de langage au lieu d'un tableur.
- Publier des images générées présentées comme des photos réelles d'activités.
- Oublier que l'historique des conversations peut être conservé par le fournisseur.

## 3.12 Synthèse

- Le bon outil dépend de la tâche ; l'assistant conversationnel n'est pas universel.
- La méthode CADRE (Contexte, Action, Données, Résultat attendu, Exigences) rend les résultats plus pertinents et vérifiables.
- On améliore une réponse par itérations ciblées.
- La boucle « 6 V » garantit une vérification proportionnée à l'enjeu.
- Les meilleures consignes se partagent et se capitalisent.

## 3.13 QCM : Module 3

**Q1.** (une seule réponse) Dans la méthode CADRE, la lettre D désigne :

a) la date de la demande.
b) la durée de la réponse.
c) les données fournies et leur délimitation.
d) le destinataire.

**Q2.** (une seule réponse) Pour calculer le total d'un budget de 80 lignes, il est préférable :

a) de demander le total à l'assistant conversationnel.
b) de faire le calcul dans un tableur, éventuellement avec une formule proposée par l'IA.
c) d'estimer le total à vue.
d) de demander le total à deux assistants et de faire la moyenne.

**Q3.** (une ou plusieurs réponses) Quelles pratiques réduisent le risque d'informations inventées ?

a) Fournir le document et demander de s'y limiter.
b) Autoriser l'outil à dire qu'il ne sait pas.
c) Demander des citations avec numéros de page.
d) Demander une réponse plus longue.

**Q4.** (une seule réponse) Les délimiteurs (balises) servent principalement à :

a) embellir la consigne.
b) accélérer l'outil.
c) chiffrer les données.
d) séparer clairement les instructions des données.

**Q5.** (une seule réponse) La rétro-traduction consiste à :

a) traduire deux fois dans la même langue.
b) supprimer les termes techniques.
c) retraduire le texte traduit vers la langue d'origine pour comparer le sens.
d) faire traduire par l'auteur du texte.

**Q6.** (une ou plusieurs réponses) Dans la boucle « 6 V », quelles étapes figurent ?

a) Lire la réponse en entier.
b) Confronter aux sources originales.
c) Publier immédiatement.
d) Valider et documenter.

**Q7.** (mise en situation, une seule réponse) L'assistant propose une formule de tableur qui renvoie une erreur. La meilleure réaction est :

a) transmettre le message d'erreur exact et la version du logiciel, puis tester la nouvelle formule sur des lignes connues.
b) abandonner le tableur.
c) recopier les résultats calculés par l'assistant.
d) changer d'outil d'IA sans rien préciser.

**Q8.** (mise en situation, une seule réponse) Une collègue veut diffuser aux familles une traduction automatique d'un message sur la vaccination, sans relecture, « car c'est urgent ». Vous recommandez :

a) de diffuser, l'urgence prime.
b) de diffuser en ajoutant « traduction automatique ».
c) de renoncer à traduire.
d) une relecture rapide par un locuteur natif et un professionnel de santé avant diffusion.

**Q9.** (une seule réponse) Pour un document de 80 pages, la stratégie la plus fiable est :

a) de tout coller en une fois et de demander un résumé.
b) de ne lire que l'introduction.
c) de le traiter par parties, puis de faire une synthèse des synthèses.
d) de demander à l'outil de deviner le contenu à partir du titre.

**Q10.** (une ou plusieurs réponses) Une bibliothèque partagée de consignes doit comporter, pour chaque consigne :

a) la méthode de vérification.
b) les données à ne pas utiliser.
c) le nom de la personne qui l'a écrite, à l'exclusion de toute autre information.
d) un exemple d'utilisation.

## 3.14 Corrigé détaillé : Module 3

**Q1 : c.** D = Données : ce qui est fourni, délimité, avec éventuellement la consigne de s'y limiter.

**Q2 : b.** Les modèles de langage ne sont pas fiables pour les calculs exacts ; le tableur l'est. L'IA peut aider à écrire la formule.

**Q3 : a, b, c.** Une réponse plus longue (d) n'est pas plus fiable, souvent l'inverse.

**Q4 : d.** Les délimiteurs évitent que l'outil confonde vos instructions et le contenu à traiter, et limitent l'effet d'instructions cachées dans les données.

**Q5 : c.** La rétro-traduction permet de repérer les glissements de sens.

**Q6 : a, b, d.** La publication immédiate (c) contredit le principe même de la boucle.

**Q7 : a.** Le message d'erreur et la version du logiciel permettent une correction précise ; le test sur des lignes connues valide la formule.

**Q8 : d.** Un message de santé mal traduit peut mettre des personnes en danger. Une relecture rapide mais qualifiée est compatible avec l'urgence.

**Q9 : c.** Le découpage limite les passages ignorés et rend chaque synthèse vérifiable.

**Q10 : a, b, d.** Le nom de l'auteur peut être utile, mais la réponse c, par sa formulation exclusive, est fausse.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285. (Fondement de la progression par exemples guidés et exercices gradués.)
- Ji, Z., et al. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys, 55*(12), article 248.
