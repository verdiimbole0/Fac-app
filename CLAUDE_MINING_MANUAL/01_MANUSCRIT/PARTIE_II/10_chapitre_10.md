## Chapitre 10 — L'art de bien communiquer avec Claude : la méthode CADRE

### A. Mise en situation professionnelle

Joseph Banza, responsable des relations communautaires de MCC, demande à Claude : « Écris une réponse à la plainte du village de Lupanda sur la poussière. » La réponse est polie, générique, et promet « des mesures immédiates d'arrosage renforcé et une indemnisation des personnes affectées ». Or MCC n'a décidé aucune indemnisation, et l'arrosage est déjà au maximum autorisé par le plan de gestion de l'eau. Envoyée telle quelle, cette lettre aurait créé un engagement que l'entreprise ne peut pas tenir et une crise de confiance avec le village.

Le problème ne vient pas de Claude, mais de la consigne : Claude ne savait rien de la situation réelle, des engagements existants, ni de ce qu'il ne fallait pas promettre. Ce chapitre vous donne une méthode pour ne plus jamais formuler une consigne de cette façon.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Expliquer** les cinq briques de la méthode CADRE : Contexte, Action, Données, Règles, Exigences de sortie.
2. **Diagnostiquer** les faiblesses d'une instruction vague.
3. **Transformer** une demande vague en instruction professionnelle structurée.
4. **Adapter** la méthode à plusieurs métiers miniers.
5. **Constituer** vos premiers modèles d'instructions réutilisables.

### C. Comprendre avant de pratiquer

#### C.1. Pourquoi une méthode ?

La documentation d'Anthropic propose une image utile : considérez Claude comme un collaborateur brillant mais **nouveau**, qui ne connaît ni vos normes ni vos méthodes de travail ; plus vous expliquez précisément ce que vous voulez, meilleur est le résultat. Elle suggère un test simple : montrez votre consigne à un collègue qui ne connaît pas le dossier ; s'il serait perdu, Claude le sera aussi [@ANT-PROMPT].

La même documentation recommande notamment d'être clair et direct, de donner le contexte et la raison des consignes, d'utiliser des exemples, de structurer les instructions (par exemple avec des balises), d'attribuer un rôle, de placer les longs documents en tête de l'instruction et de dire ce qu'il faut faire plutôt que ce qu'il ne faut pas faire [@ANT-PROMPT].

La **méthode CADRE** organise ces bonnes pratiques en cinq briques faciles à mémoriser et à vérifier.

::: attention
**CADRE est un cadre pédagogique proposé par cet ouvrage.** Ce n'est pas une méthode officielle d'Anthropic. Il s'appuie sur les recommandations publiques de la documentation d'Anthropic, réorganisées pour les professionnels du secteur minier.
:::

![Figure 10.1 — La méthode CADRE : Contexte, Action, Données, Règles, Exigences de sortie. Cadre pédagogique proposé par cet ouvrage. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig10_1_methode_cadre.png){width=100%}

#### C.2. C — Contexte

Le **contexte** répond à la question : *dans quelle situation se trouve-t-on ?* Il comprend :

- **qui vous êtes** (fonction, responsabilités) ;
- **l'organisation** (type de mine, substance, pays, taille) ;
- **la situation** (événement, projet, échéance) ;
- **le destinataire** du livrable et l'**usage** qui en sera fait ;
- **l'enjeu** (pourquoi c'est important).

*Exemple :* « Je suis responsable des relations communautaires d'une mine de cuivre-cobalt à ciel ouvert en RDC. Le village de Lupanda (environ 4 000 habitants, à 1,5 km de la route d'accès) a déposé une plainte écrite sur la poussière. La relation avec ce village est sensible depuis la réinstallation de 2020. »

::: terrain
Le contexte inclut aussi le **pourquoi** d'une consigne. « Évite les promesses » est moins efficace que « Évite toute promesse : l'entreprise n'a encore décidé aucune mesure et une promesse non tenue détériorerait gravement la confiance. » Expliquer la raison aide Claude à appliquer la règle avec discernement [@ANT-PROMPT].
:::

#### C.3. A — Action

L'**action** répond à la question : *que doit faire Claude exactement ?* Elle commence par un **verbe précis** :

| Verbe vague | Verbes précis |
|---|---|
| « Fais quelque chose sur… » | Rédiger, résumer, extraire, comparer, classer, calculer, vérifier, critiquer, traduire, reformuler, structurer, lister, expliquer |
| « Regarde ce document » | Identifier les obligations contractuelles ; lister les incohérences ; extraire les valeurs du tableau 4 |

Précisez aussi le **périmètre** (ce qui est inclus, ce qui ne l'est pas) et, si nécessaire, les **étapes**.

*Exemple :* « Rédige un projet de réponse écrite au chef du village, qui accuse réception de la plainte, présente les mesures déjà en place et propose une réunion. »

#### C.4. D — Données

Les **données** répondent à la question : *sur quoi Claude doit-il s'appuyer ?* Documents joints, extraits copiés, chiffres, exemples, résultats de mesures, modèles de documents. Sans données, Claude comble les vides avec des généralités — ou des inventions.

Bonnes pratiques :

- placez les **documents longs en tête** de l'instruction, avant la question (la documentation d'Anthropic indique que cela améliore les résultats, en particulier avec plusieurs documents) [@ANT-PROMPT] ;
- **délimitez** chaque source avec des balises (`<plainte>…</plainte>`, `<mesures_en_place>…</mesures_en_place>`) ;
- fournissez un **exemple** du résultat attendu si vous en avez un ;
- vérifiez le **niveau de confidentialité** de chaque donnée avant de la transmettre (chapitre 37).

#### C.5. R — Règles

Les **règles** répondent à la question : *quelles contraintes respecter ?*

- **Règles de vérité** : n'inventer aucun fait ; signaler les informations manquantes ; distinguer faits et hypothèses ; citer les sources.
- **Règles métier** : normes, procédures, référentiels (par exemple, « respecte le format du registre des plaintes de MCC »).
- **Règles de prudence** : ne pas promettre, ne pas conclure sur les causes avant enquête, ne pas formuler d'avis juridique engageant.
- **Règles de ton et d'éthique** : respect, langage non discriminant, absence de jargon pour un public non spécialiste.
- **Limites de rôle** : ce que Claude ne doit pas décider (chapitre 6).

Formulez de préférence les règles **positivement** (« écris en paragraphes continus ») plutôt que négativement (« n'utilise pas de listes »), comme le recommande la documentation [@ANT-PROMPT] — sauf pour les interdits de sécurité, qui doivent rester explicites.

#### C.6. E — Exigences de sortie

Les **exigences de sortie** répondent à la question : *à quoi le résultat doit-il ressembler ?*

- **format** : courrier, tableau, liste, note, fichier Word, Excel ;
- **structure** : rubriques imposées, ordre ;
- **longueur** : nombre de mots, de lignes, de pages ;
- **ton et langue** : formel, pédagogique, français simple, traduction en swahili ;
- **éléments obligatoires** : sources, niveau de confiance, questions ouvertes, prochaines étapes.

#### C.7. Avant / après : l'exemple de Joseph

![Figure 10.2 — D'une demande vague à une instruction CADRE (exemple HSE). La version structurée produit un brouillon factuel, traçable, conforme au modèle, avec ses lacunes signalées. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig10_2_avant_apres.png){width=100%}

**Version vague :**

```text
Écris une réponse à la plainte du village de Lupanda sur la poussière.
```

**Version CADRE :**

```text
[C — CONTEXTE]
Je suis responsable des relations communautaires de Mbiyo Copper Cobalt SA,
mine de cuivre-cobalt à ciel ouvert en RDC. Le village de Lupanda (≈ 4 000 habitants)
se trouve à 1,5 km de la route d'accès à la mine. La relation est sensible depuis
une réinstallation en 2020. Le chef du village a déposé la plainte écrite ci-dessous.

[A — ACTION]
Rédige un projet de réponse écrite au chef du village qui :
1. accuse réception de la plainte et reconnaît la gêne exprimée ;
2. présente les mesures déjà en place (liste ci-dessous), sans en ajouter ;
3. propose une réunion d'échange au village dans les deux semaines ;
4. explique la suite de la procédure de traitement des plaintes.

[D — DONNÉES]
<plainte>
[texte de la plainte PL-0042 du registre]
</plainte>
<mesures_en_place>
- Arrosage de la route 4 fois par jour en saison sèche (maximum autorisé par le plan de gestion de l'eau).
- Limitation de vitesse à 30 km/h à la traversée du village, contrôlée par radar.
- Suivi mensuel des poussières à la station située à l'entrée du village.
</mesures_en_place>

[R — RÈGLES]
- Ne promets aucune mesure nouvelle ni indemnisation : aucune décision n'a été prise,
  et une promesse non tenue détériorerait gravement la confiance.
- N'emploie aucun chiffre qui ne figure pas dans les données.
- Ton respectueux, simple, sans jargon technique ni juridique.
- Si une information utile manque, indique-la entre crochets [à compléter].

[E — EXIGENCES DE SORTIE]
- Courrier d'une page maximum, en français.
- Formules de politesse adaptées à un chef coutumier.
- Après le courrier, liste séparément les points que je dois vérifier avant envoi.
```

Le résultat est un courrier sobre, qui reconnaît le problème sans rien promettre de nouveau, propose un dialogue et laisse à Joseph la liste de ses vérifications. Il reste à le relire, l'adapter et le faire valider selon la procédure de MCC.

#### C.8. Les erreurs de formulation les plus fréquentes

*Tableau 10.1 — Diagnostic des instructions faibles.*

| Erreur | Exemple | Effet | Correction CADRE |
|---|---|---|---|
| Pas de contexte | « Analyse ce tableau » | Analyse générique | C : qui, pourquoi, pour qui |
| Verbe flou | « Regarde ce contrat » | Résumé au lieu d'une analyse de risques | A : « identifie les clauses de pénalité » |
| Données absentes | « Rédige le rapport d'incident » | Faits inventés | D : déclarations, constats, chronologie |
| Pas de règle de vérité | — | Chiffres plausibles mais faux | R : « n'invente rien, signale les manques » |
| Pas de format | « Fais-moi un point » | Texte trop long ou mal structuré | E : « tableau de 5 lignes » |
| Plusieurs tâches mêlées | « Résume, critique, traduis et fais une présentation » | Résultat moyen partout | Découper (chapitre 11) |
| Question orientée | « Pourquoi le conducteur est-il fautif ? » | Réponse complaisante | Formulation neutre |

### D. Démonstration guidée — CADRE appliqué à quatre métiers

#### D.1. Géologie — Synthèse d'une campagne de sondages

```text
[C] Je suis géologue principal d'une mine de cuivre-cobalt (gisement stratiforme
de type Copperbelt). Je prépare la note trimestrielle d'exploration pour le directeur
technique, qui n'est pas géologue.
[A] Rédige la synthèse des résultats de la campagne de sondages du trimestre :
principaux résultats, intersections significatives, implications pour la suite.
[D] <resultats> tableau des intersections significatives (joint) </resultats>
    <programme> programme initial de la campagne (joint) </programme>
[R] Utilise uniquement les données fournies ; n'extrapole aucune ressource
    (ce n'est pas une estimation de ressources) ; signale les sondages non encore analysés.
[E] Une page ; un paragraphe d'introduction ; un tableau des 5 meilleures intersections
    (sondage, de-à, longueur, Cu %, Co %) ; 3 recommandations ; vocabulaire accessible.
```

#### D.2. Finance — Commentaire d'écart budgétaire

```text
[C] Je suis contrôleuse de gestion d'une mine (MCC). Le comité de direction
de lundi examine les coûts du premier semestre 2026.
[A] Analyse les écarts entre budget et réel par centre de coût et rédige
le commentaire de gestion.
[D] Fichier joint MCC_budget_reel_S1_2026.xlsx (onglets « Budget vs réel » et « Hypothèses »).
[R] Tous les calculs avec l'exécution de code ; aucune cause d'écart affirmée sans
    lien avec les données ; distingue « cause établie » et « piste à vérifier ».
[E] Tableau des 5 écarts les plus importants (MUSD et %) ; commentaire de 200 mots ;
    3 questions à poser aux responsables de centres de coût.
```

#### D.3. Maintenance — Analyse d'un historique

```text
[C] Je suis responsable maintenance d'une mine à ciel ouvert (12 camions de 90 t).
Le camion CAM-07 semble avoir des pannes hydrauliques répétées.
[A] Analyse l'historique des ordres de travail du CAM-07 et identifie les schémas de défaillance.
[D] Fichier joint MCC_maintenance_ordres_travail.csv.
[R] Calculs par programme ; ne conclus pas sur la cause racine (une analyse
    de défaillance sur site est nécessaire) ; signale les données incohérentes.
[E] Tableau chronologique des interventions hydrauliques ; temps d'arrêt cumulé ;
    coût cumulé ; liste d'hypothèses à vérifier par l'équipe ; 1 graphique.
```

#### D.4. HSE — Causerie sécurité

```text
[C] Je suis responsable HSE. Chaque lundi, les superviseurs animent une causerie
de 10 minutes avec leurs équipes (conducteurs d'engins, francophones, niveau
d'instruction variable).
[A] Prépare la causerie de la semaine sur la circulation sur les rampes par temps de pluie.
[D] Résumé anonymisé de deux presque-accidents récents (ci-dessous).
[R] Messages simples et concrets ; pas de culpabilisation ; ne cite aucun nom ;
    reste cohérent avec les règles de circulation du site (rappelées ci-dessous).
[E] Fiche d'une page : 3 messages clés, 2 questions à poser à l'équipe,
    1 engagement collectif ; version en français simple.
```

### E. Prompts commentés

**Prompt 10.1 — Le diagnostic CADRE de votre propre instruction**

```text
Voici une instruction que je compte te donner : [coller l'instruction].
Avant de l'exécuter, évalue-la selon cinq critères : Contexte, Action, Données,
Règles, Exigences de sortie. Pour chaque critère, indique ce qui manque ou est ambigu,
puis propose une version améliorée de l'instruction. N'exécute pas encore la tâche.
```

*Commentaire.* Claude devient ici un coach de formulation. C'est une excellente façon de progresser rapidement : comparez sa version améliorée à la vôtre et retenez ce qui manquait.

**Prompt 10.2 — Demander les questions avant d'agir**

```text
Je veux [objectif]. Avant de commencer, pose-moi les questions dont tu as besoin
pour faire un travail de qualité (5 maximum, les plus importantes d'abord).
Attends mes réponses avant de rédiger.
```

*Commentaire.* Lorsque vous ne savez pas exactement quel contexte fournir, laissez Claude vous le demander. Vous construisez ainsi le « C » et le « D » en dialoguant.

**Prompt 10.3 — Gabarit CADRE vierge**

```text
[C — CONTEXTE] Je suis [fonction] chez [entreprise / type de mine / pays].
Situation : [description]. Destinataire et usage : [qui, pour quoi faire].
[A — ACTION] [Verbe précis] + [objet] + [périmètre] (+ étapes si nécessaire).
[D — DONNÉES] <source_1> … </source_1> <source_2> … </source_2>
[R — RÈGLES] Vérité : … Métier : … Prudence : … Ton : … Rôle : …
[E — EXIGENCES DE SORTIE] Format : … Structure : … Longueur : … Éléments obligatoires : …
```

### F. Exercices pratiques

**Exercice 10.1 (guidé) — Diagnostiquer et réécrire**

Réécrivez avec CADRE les trois instructions suivantes, puis comparez les résultats obtenus :

1. « Fais un résumé de l'étude d'impact. »
2. « Calcule les indicateurs HSE du mois. »
3. « Rédige un mail au fournisseur d'acide pour se plaindre. »

**Exercice 10.2 (guidé) — Le courrier au fournisseur**

À partir du fichier `MCC_contrat_fourniture_acide_extrait.pdf` et de la situation suivante (livraisons de mars : 5 100 t), rédigez avec CADRE l'instruction qui produira un projet de courrier de réclamation au fournisseur, conforme au contrat. *Indice : relisez les articles 3 et 9 ; quelles règles fixerez-vous sur les montants ?*

**Exercice 10.3 (autonome) — Votre bibliothèque CADRE**

Rédigez cinq instructions CADRE pour les tâches les plus fréquentes de votre métier. Testez-les, améliorez-les, et enregistrez la meilleure version de chacune.

::: defi
Prenez votre dernière conversation avec Claude dont le résultat vous a déçu. Identifiez quelle brique CADRE manquait. Refaites l'essai.
:::

### G. Livrable professionnel

**Bibliothèque personnelle de 5 instructions CADRE** testées, chacune accompagnée : du cas d'usage, de la version de l'instruction, du modèle utilisé, du résultat obtenu (bon / à améliorer), des contrôles à effectuer. Cette bibliothèque sera enrichie au chapitre 11 et dans la partie III. L'Annexe C propose des modèles avancés.

### H. Vérification des résultats

::: controle
**Check-list CADRE avant d'envoyer une instruction importante**

- **C** : un collègue extérieur comprendrait-il la situation ?
- **A** : le verbe est-il précis ? le périmètre est-il clair ?
- **D** : les sources nécessaires sont-elles fournies, délimitées et autorisées ?
- **R** : la règle de vérité (« n'invente rien, signale les manques ») est-elle présente ? les limites de rôle sont-elles posées ?
- **E** : le format, la longueur et les éléments obligatoires sont-ils précisés ?
:::

::: setrompe
Même avec une instruction CADRE, Claude peut ajouter une « mesure » non fournie en croyant bien faire (par exemple « nous installerons des panneaux de signalisation supplémentaires »). **Contre-mesure** : demander, en fin de réponse, la liste de tout élément qui ne provient pas des données fournies — et relire.
:::

### I. Limites et précautions

- CADRE améliore fortement la qualité, mais ne dispense jamais de la vérification.
- Une instruction trop longue et contradictoire peut dégrader le résultat : chaque règle doit être utile.
- Les données fournies dans le « D » doivent respecter la classification de l'entreprise.

### J. Boîte à outils

**Mémo CADRE (à imprimer)**

| Brique | Question | Mots-clés |
|---|---|---|
| C — Contexte | Quelle situation ? | Je suis… / Notre mine… / Destinataire… / Enjeu… |
| A — Action | Quoi faire ? | Rédige / Extrais / Compare / Calcule / Vérifie… |
| D — Données | Sur quoi ? | `<document>` / fichiers joints / exemples |
| R — Règles | Quelles limites ? | N'invente rien / Signale / Cite / Ne décide pas |
| E — Exigences | Quel résultat ? | Format / Structure / Longueur / Ton |

### K. Quiz

1. **(QCM)** Que signifie le « D » de CADRE ? a) Décision ; b) Données ; c) Délai ; d) Diagnostic.
2. **(Vrai ou faux)** CADRE est la méthode officielle d'Anthropic.
3. **(Compréhension)** Pourquoi est-il utile d'expliquer la raison d'une règle dans l'instruction ?
4. **(QCM)** Où la documentation d'Anthropic recommande-t-elle de placer les documents longs ? a) à la fin ; b) en tête, avant la question ; c) dans un autre message ; d) nulle part.
5. **(Application)** Transformez en action précise : « Regarde ce contrat. »
6. **(Mise en situation)** Claude a promis une indemnisation dans un projet de courrier. Quelle brique CADRE était insuffisante ?
7. **(Vrai ou faux)** Les règles doivent de préférence être formulées positivement, sauf les interdits de sécurité.
8. **(Compréhension)** Citez trois éléments possibles des « exigences de sortie ».
9. **(Analyse critique)** Pourquoi la question « Pourquoi le conducteur est-il fautif ? » est-elle mal formulée ?
10. **(Application)** Rédigez la règle de vérité que vous ajouterez systématiquement à vos instructions sensibles.

<div class="carnet" titre="Chapitre 10 — L'art de bien communiquer avec Claude : la méthode CADRE"></div>
