## Chapitre 3. Comprendre les grands modèles de langage

### A. Mise en situation professionnelle

Ruth Mbuyi, comptable principale de MCC, a demandé à Claude de calculer le total d'une colonne de 180 montants copiés depuis un export comptable. Le résultat semblait juste… mais différait de 312 USD du total calculé par le tableur. Le même jour, son collègue Olivier Kanku a obtenu de Claude une excellente analyse d'un article de loi fiscale, nuancée et bien structurée.

Comment un même outil peut-il exceller dans l'analyse d'un texte juridique et commettre une erreur sur une simple addition ? Pour le comprendre, et pour savoir quand faire confiance, il faut ouvrir le capot des **grands modèles de langage**.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Expliquer** ce qu'est un token et pourquoi cette notion compte pour l'usage quotidien.
2. **Décrire** le principe de prédiction du token suivant et ses conséquences (fluidité, erreurs plausibles).
3. **Expliquer** le rôle de la fenêtre de contexte et ses implications pratiques.
4. **Distinguer** les phases d'entraînement d'un modèle et la notion de date limite des connaissances.
5. **Identifier** les capacités multimodales et les outils qui complètent le modèle (recherche Web, exécution de code).
6. **Adapter** votre manière de travailler à ces caractéristiques (calculs, documents longs, faits récents).

### C. Comprendre avant de pratiquer

#### C.1. Les tokens : l'unité de base

Un modèle de langage ne lit pas des mots comme nous. Il découpe le texte en **tokens** : des fragments de texte (un mot entier, une partie de mot, un signe de ponctuation, un chiffre). Chaque token est converti en identifiant numérique, puis en une représentation mathématique que le modèle peut traiter.

![Figure 3.1. Le texte est découpé en tokens avant d'être traité. Découpage illustratif : le découpage réel dépend de l'outil de découpage (« tokenizer ») propre à chaque modèle. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig03_1_tokens.png){width=100%}

Pourquoi est-ce important pour vous ?

- **Les capacités se mesurent en tokens** : la taille des documents que Claude peut traiter, la longueur maximale de ses réponses et le coût d'utilisation de l'API sont exprimés en tokens. La documentation d'Anthropic indique qu'un million de tokens correspond à environ 555 000 mots (ou 2,5 millions de caractères) avec le découpage des modèles actuels [@ANT-MODELS].
- **Les nombres sont souvent fragmentés** : « 2 351 847 » peut être découpé en plusieurs tokens. C'est l'une des raisons pour lesquelles un modèle de langage, sans outil de calcul, peut commettre des erreurs de calcul ou de recopie de chiffres.
- **Les noms propres rares** (« Kasongo-Mbiyo », « hétérogénite ») sont découpés en morceaux, ce qui peut favoriser des fautes de recopie.

#### C.2. Prédire le token suivant

Le principe fondamental d'un grand modèle de langage est simple à énoncer : **à partir d'un texte, il calcule la probabilité de chaque token possible pour la suite, puis en choisit un**. Il recommence ensuite avec le texte prolongé, token après token, jusqu'à produire une réponse complète.

![Figure 3.2. Prédire la suite. Le modèle calcule une distribution de probabilités sur les tokens possibles. Valeurs illustratives. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig03_2_probabilites.png){width=85%}

Ce principe explique à la fois les forces et les faiblesses des modèles :

| Caractéristique | Conséquence pratique |
|---|---|
| Le modèle a « vu » d'immenses quantités de textes | Il maîtrise les styles, les structures de documents, de nombreux domaines techniques |
| Il produit ce qui est **probable**, pas ce qui est **vrai** | Il peut produire une affirmation fausse mais vraisemblable (hallucination) |
| Il génère token par token | Il peut perdre le fil d'un calcul long s'il ne s'appuie pas sur un outil ou une méthode explicite |
| La génération comporte une part de variabilité | La même question peut donner des réponses légèrement différentes |

::: retenir
Un modèle de langage n'est **pas une base de données** qui « retrouve » des faits enregistrés. C'est un système qui **génère** du texte plausible à partir de régularités apprises. La plausibilité n'est pas une preuve.
:::

Cette description reste une simplification. Les recherches en interprétabilité menées par Anthropic montrent que le fonctionnement interne est plus riche qu'une simple prédiction « mot à mot » : par exemple, lorsqu'il écrit un poème rimé, un modèle peut anticiper la rime avant d'écrire la ligne qui y mène [@ANT-TRACING]. Mais pour l'utilisateur, la conséquence pratique demeure : il faut vérifier.

#### C.3. Comment un modèle est-il construit ?

La construction d'un grand modèle de langage comporte, de manière simplifiée, deux grandes phases :

1. **Le pré-entraînement** : le modèle apprend à prédire la suite de textes sur un très grand corpus. Il acquiert ainsi la langue, des connaissances générales et des capacités de raisonnement.
2. **L'ajustement** : le modèle est ensuite entraîné à se comporter en assistant utile, honnête et inoffensif, notamment à partir de retours humains et, chez Anthropic, de principes écrits. Cette méthode, dite d'**IA constitutionnelle**, a été décrite dans un article de recherche de 2022 [@BAI-2022] ; Anthropic publie par ailleurs la « constitution » qui décrit les valeurs et le comportement visés pour Claude [@ANT-CONSTIT].

Conséquence importante : les connaissances d'un modèle s'arrêtent à une **date limite d'entraînement**. Pour les modèles Claude actuels, la documentation indique une date limite de connaissances fiables de juin 2026 [@ANT-MODELS]. Tout ce qui s'est passé après (nouveau décret, nouveau prix des métaux, nouvelle norme) est inconnu du modèle, sauf si vous le lui fournissez ou s'il utilise un outil de recherche Web.

#### C.4. La fenêtre de contexte : la mémoire de travail

La **fenêtre de contexte** est la quantité maximale de texte (en tokens) que le modèle peut prendre en compte en une fois : vos instructions, les documents joints, l'historique de la conversation et la réponse en cours. Les modèles Claude actuels disposent d'une fenêtre d'un million de tokens et peuvent produire jusqu'à 128 000 tokens en sortie via l'API [@ANT-MODELS; @ANT-CTX].

![Figure 3.3. La fenêtre de contexte. Tout ce qui est utile à la réponse doit s'y trouver ; ce qui est hors de la fenêtre n'existe pas pour le modèle. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig03_3_fenetre_contexte.png){width=95%}

Trois conséquences pratiques :

- **Le modèle ne se souvient pas spontanément** de vos conversations précédentes. Ce qu'il « sait » de votre situation est ce qui figure dans la fenêtre, ou ce que les fonctions de mémoire et de projets y ajoutent (chapitres 12 et 15).
- **Une fenêtre très grande ne garantit pas une attention parfaite** : plus elle est chargée d'informations peu pertinentes, plus le risque est grand qu'un détail important soit négligé. Fournissez des documents ciblés.
- **Les longues conversations s'alourdissent** : il est souvent préférable de repartir d'une nouvelle conversation avec un résumé (chapitre 12).

#### C.5. Réflexion, effort et outils

Les modèles Claude actuels peuvent **réfléchir avant de répondre** : ils produisent un raisonnement interne avant la réponse finale. La documentation décrit une réflexion **adaptative**, dans laquelle le modèle décide quand et combien réfléchir, en fonction d'un paramètre appelé **effort** [@ANT-THINK; @ANT-EFFORT]. Plus l'effort est élevé, plus le modèle consacre de calcul à la tâche, au prix d'une réponse plus lente et plus coûteuse. Ce réglage est détaillé au chapitre 9.

Le modèle peut aussi utiliser des **outils** : rechercher sur le Web, exécuter du code pour faire des calculs exacts ou analyser un fichier, interroger des applications connectées [@ANT-TOOLS]. C'est un point essentiel pour les calculs : lorsque Claude exécute un programme pour additionner une colonne, le résultat est calculé, et non « prédit ».

::: terrain
Pour tout calcul qui compte, demandez explicitement à Claude d'**utiliser l'exécution de code** (ou l'analyse de données) et de **montrer la formule**. Pour une addition de 180 montants, Ruth Mbuyi aurait obtenu un total exact en joignant le fichier et en demandant : « Calcule le total avec un programme et affiche le nombre de lignes prises en compte. »
:::

#### C.6. La multimodalité

Un modèle **multimodal** traite plusieurs types de données. Les modèles Claude actuels acceptent du texte et des images en entrée et produisent du texte en sortie [@ANT-MODELS]. Concrètement, Claude peut analyser une photographie d'affleurement, un graphique de production, un plan scanné, une capture d'écran de tableau de bord ou un PDF contenant des figures [@ANT-VISION; @ANT-PDF]. Il peut aussi **créer** des fichiers (tableurs, documents, présentations, graphiques) grâce à l'exécution de code et aux artefacts (chapitres 13 et 15).

::: attention
L'analyse d'image a des limites : une photographie floue, une échelle absente ou un plan de faible résolution peuvent conduire à des interprétations erronées. Une photo ne remplace jamais une observation de terrain ni une mesure.
:::

![Figure 3.4. Ce qui se passe entre votre question et la réponse. Les étapes 2 à 5 sont automatiques ; l'étape 6, la vérification, vous revient toujours. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig03_4_traitement_instruction.png){width=100%}

### D. Démonstration guidée : Mettre en évidence les forces et les faiblesses

Ruth reproduit l'expérience en quatre temps pour former son équipe.

1. **Test de calcul « de tête »** : elle colle 30 montants dans la conversation et demande le total sans autre consigne. Elle compare avec le tableur.
2. **Test de calcul « outillé »** : elle joint le fichier CSV et demande à Claude de calculer le total **par programme**, en indiquant le nombre de lignes et les éventuelles valeurs non numériques. Le résultat est exact, et Claude signale deux cellules contenant du texte.
3. **Test de connaissance récente** : elle demande le taux d'une redevance « en vigueur aujourd'hui ». Claude répond avec prudence, rappelle sa date limite de connaissances et recommande de vérifier le texte officiel.
4. **Test d'analyse textuelle** : elle fournit un article du contrat de fourniture d'acide (fichier d'exercice) et demande une explication de la formule de révision du prix. L'explication est claire et exacte.

Conclusion pour l'équipe : **Claude est très performant sur le langage ; pour les calculs, il faut lui faire utiliser un outil ; pour les faits récents, il faut lui fournir la source.**

### E. Prompts commentés

**Prompt 3.1. Calcul fiable sur un fichier**

```text
Voici le fichier joint [MCC_bons_de_commande.csv] (séparateur point-virgule ;
la première ligne est un bandeau à ignorer).

Avec l'exécution de code :
1. Calcule le montant total des commandes par fournisseur.
2. Indique le nombre de lignes lues, le nombre de lignes ignorées et pourquoi.
3. Affiche le code utilisé.
Ne fais aucun calcul « de tête » : tous les chiffres doivent provenir du programme.
```

*Commentaire.* Les consignes 2 et 3 rendent le calcul **auditable** : vous pouvez vérifier que toutes les lignes ont été prises en compte et relire le code.

**Prompt 3.2. Tester les connaissances du modèle sur un sujet évolutif**

```text
Avant de répondre, indique ta date limite de connaissances et si la question
porte sur une information susceptible d'avoir changé depuis.
Question : [question sur un taux, un prix, une réglementation].
Si l'information peut avoir évolué, dis-le clairement et indique quelle source
officielle je dois consulter pour la vérifier.
```

**Prompt 3.3. Faire analyser une image**

```text
Voici la photographie d'un front de taille de la fosse Mbiyo Nord.
Décris ce que tu observes (couleurs, structures, éléments visibles) en distinguant
clairement ce qui est observable sur l'image et ce qui serait une interprétation.
Indique les informations manquantes (échelle, orientation, contexte) qui limitent
l'interprétation. Ne conclus pas sur la teneur.
```

### F. Exercices pratiques

**Exercice 3.1 (guidé) : Les deux additions**

Avec le fichier `MCC_production_journaliere_S1_2026.csv`, demandez à Claude : (a) le total de la colonne `cathode_Cu_t` pour janvier, sans outil, en collant les valeurs ; (b) le même total en joignant le fichier et en exigeant l'exécution de code. Comparez avec votre tableur. Notez le nombre de lignes et les éventuelles anomalies signalées.

**Exercice 3.2 (guidé) : Mesurer la taille d'un document**

Estimez le nombre de tokens d'un de vos rapports habituels (rappel : environ 555 000 mots pour un million de tokens avec les modèles actuels, soit un ordre de grandeur de 1,8 token par mot). Combien de rapports de ce type tiendraient dans la fenêtre de contexte ? Pourquoi n'est-il pas forcément judicieux de tous les joindre ?

**Exercice 3.3 (autonome) : L'IA expliquée en cinq minutes**

Préparez une présentation orale de cinq minutes pour une causerie avec votre équipe : tokens, prédiction, fenêtre de contexte, date limite de connaissances, outils. Utilisez un exemple tiré de votre métier pour chaque notion.

### G. Livrable professionnel

**Fiche réflexe « Comment Claude fonctionne : ce que cela change pour moi »** (une page), contenant pour chaque notion du chapitre la règle pratique associée. Exemple :

| Notion | Ce que cela implique | Ma règle pratique |
|---|---|---|
| Prédiction du token suivant | Réponses plausibles, pas forcément vraies | Je vérifie les faits importants |
| Tokens et chiffres | Erreurs possibles sur les nombres | Calculs avec exécution de code, toujours |
| Date limite des connaissances | Ignorance des faits récents | Je fournis la source officielle à jour |
| Fenêtre de contexte | Ne connaît que ce qui y figure | Je donne le contexte utile, pas tout |
| Multimodalité | Lit images et PDF | J'indique l'échelle et le contexte |

### H. Vérification des résultats

::: controle
- Tout chiffre issu d'un calcul a-t-il été produit par un outil (code, tableur) et recoupé ?
- Les informations susceptibles d'avoir changé depuis la date limite de connaissances ont-elles été vérifiées dans une source officielle à jour ?
- Les noms propres, références et nombres recopiés par Claude correspondent-ils exactement aux documents sources ?
:::

::: setrompe
Vous demandez la teneur moyenne pondérée de cinq passes de sondage. Claude fait une moyenne simple au lieu d'une moyenne pondérée par la longueur des passes, et présente le résultat avec deux décimales. Le résultat paraît précis, mais il est faux. **Contre-mesure** : précisez la méthode (« moyenne pondérée par la longueur ») et exigez la formule et le calcul par programme.
:::

### I. Limites et précautions

- La description de ce chapitre est simplifiée ; elle suffit à un usage professionnel éclairé, pas à la conception de modèles.
- Les capacités (taille de contexte, longueur de sortie, formats acceptés) **évoluent** et dépendent du produit utilisé (application, API, offre) : vérifiez la documentation officielle.
- La variabilité des réponses impose, pour les tâches critiques, de **standardiser les prompts** et de **contrôler systématiquement** les résultats.

### J. Boîte à outils

**Les cinq réflexes « fonctionnement »**

1. **Calcul** → exécution de code + formule affichée.
2. **Fait récent** → source officielle fournie ou recherche Web avec citations.
3. **Document long** → extraits ciblés + demande de citations exactes.
4. **Chiffres recopiés** → contrôle par échantillonnage.
5. **Image** → contexte, échelle et prudence d'interprétation.

**Prompt réutilisable 3.4 : Réponse ancrée dans un document**

```text
Réponds uniquement à partir du document joint. Pour chaque affirmation,
cite le passage exact entre guillemets et indique la page ou la section.
Si le document ne contient pas l'information, écris : « Information absente du document. »
Question : [votre question]
```

### K. Quiz

1. **(QCM)** Un token est : a) un mot de passe ; b) un fragment de texte traité par le modèle ; c) une unité de coût fixe par question ; d) un fichier joint.
2. **(Vrai ou faux)** Un grand modèle de langage retrouve les faits dans une base de données interne, comme un moteur de recherche.
3. **(Compréhension)** Pourquoi un modèle de langage peut-il se tromper sur une addition alors qu'il analyse correctement un texte juridique ?
4. **(QCM)** Selon la documentation d'Anthropic consultée pour ce livre, quelle est la fenêtre de contexte des modèles Claude actuels ? a) 8 000 tokens ; b) 100 000 tokens ; c) 1 million de tokens ; d) illimitée.
5. **(Vrai ou faux)** Claude connaît automatiquement le décret publié la semaine dernière par le ministère des Mines.
6. **(Mise en situation)** Vous devez calculer la teneur moyenne pondérée de 40 passes. Rédigez la consigne que vous donnez à Claude.
7. **(QCM)** La méthode d'entraînement par principes écrits décrite par Anthropic s'appelle : a) apprentissage par renforcement profond ; b) IA constitutionnelle ; c) krigeage ordinaire ; d) réseau adverse.
8. **(Analyse critique)** « Plus la fenêtre de contexte est grande, plus il faut y mettre de documents. » Discutez cette affirmation.
9. **(Compréhension)** Qu'est-ce que la multimodalité ? Donnez deux exemples d'usage minier.
10. **(Application)** Citez deux moyens de rendre auditable un calcul réalisé avec Claude.

<div class="carnet" titre="Chapitre 3. Comprendre les grands modèles de langage"></div>
