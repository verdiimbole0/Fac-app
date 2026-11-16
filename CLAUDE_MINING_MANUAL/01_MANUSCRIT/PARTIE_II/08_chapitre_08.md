## Chapitre 8 — Comprendre les modèles et choisir le bon outil pour chaque tâche

### A. Mise en situation professionnelle

Kevin Mutombo, référent IA de MCC, reçoit deux demandes le même jour. Nadine Kapinga, contrôleuse de gestion, se plaint : « Claude met trop de temps à classer mes 2 000 lignes de commandes par catégorie de dépense. » Patrick Ilunga, géologue principal, se plaint de l'inverse : « Pour l'analyse de cohérence de notre rapport de ressources, les réponses sont trop superficielles. »

Après vérification, Nadine utilisait le modèle le plus puissant, avec un effort élevé, pour une tâche de classement simple et répétitive ; Patrick utilisait un modèle rapide, avec un effort faible, pour une analyse complexe. Ni l'un ni l'autre n'avait fait un mauvais usage de Claude : ils n'avaient simplement pas choisi **le bon modèle pour la bonne tâche**.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Comparer** les modèles Claude selon leurs critères de choix : qualité, vitesse, coût, disponibilité selon l'offre.
2. **Choisir** un modèle adapté à une tâche minière donnée, à l'aide d'un arbre de décision.
3. **Estimer** l'ordre de grandeur du coût d'une tâche via l'API.
4. **Choisir** entre l'application, Cowork, Claude Code et l'API selon la nature du travail.
5. **Tester** objectivement deux configurations sur un même cas.

### C. Comprendre avant de pratiquer

#### C.1. Les critères de choix

Choisir un modèle revient à arbitrer entre quatre critères :

| Critère | Question à se poser |
|---|---|
| **Qualité** | La tâche exige-t-elle un raisonnement approfondi, une grande finesse d'analyse, une grande fiabilité ? |
| **Vitesse** | Ai-je besoin d'une réponse quasi immédiate, ou puis-je attendre ? |
| **Coût / consommation** | La tâche est-elle répétée des centaines de fois ? Mon offre limite-t-elle l'usage des modèles les plus puissants ? |
| **Disponibilité** | Le modèle est-il disponible dans mon offre et autorisé par mon organisation ? |

La documentation d'Anthropic propose une page dédiée au choix du modèle, qui recommande de définir d'abord ses critères puis de tester [@ANT-MODELS]. Elle indique qu'en cas de doute, Claude Opus 5.5 est le point de départ conseillé pour la plupart des usages, Claude Fable 5.2 étant réservé aux raisonnements les plus exigeants et aux travaux agentiques longs, Claude Sonnet 5.5 offrant la meilleure combinaison vitesse-intelligence et Claude Haiku 5.5 visant les tâches à fort volume [@ANT-MODELS].

#### C.2. L'arbre de décision

![Figure 8.1 — Arbre de décision pour choisir un modèle. Les niveaux d'effort indiqués sont des points de départ, à ajuster selon les résultats. Illustration réalisée pour cet ouvrage, d'après la documentation Anthropic (consultée le 16/11/2026).](02_ILLUSTRATIONS/SCHEMAS/fig08_1_arbre_choix_modele.png){width=100%}

*Tableau 8.1 — Exemples de choix pour des tâches de MCC (recommandations de l'auteur, à tester).*

| Tâche | Modèle de départ | Pourquoi |
|---|---|---|
| Classer 2 000 lignes de commandes par catégorie | Haiku 5.5 ou Sonnet 5.5 | Tâche simple, répétitive, volumineuse |
| Reformuler un courriel, résumer une note de 5 pages | Sonnet 5.5 | Rapide et largement suffisant |
| Rédiger un rapport d'incident à partir de déclarations | Opus 5.5 | Qualité rédactionnelle et rigueur factuelle |
| Analyser la cohérence d'un rapport de ressources de 200 pages | Opus 5.5 (effort élevé) ou Fable 5.2 | Raisonnement long, croisement d'informations |
| Comparer un contrat de 80 pages au modèle standard de l'entreprise | Opus 5.5 | Finesse juridique, longueur |
| Étude multi-documents complexe sur plusieurs heures (agentique) | Fable 5.2 | Travail autonome long |

#### C.3. Le choix dans l'application selon l'offre

Dans l'application, les modèles proposés dépendent de votre offre. Au 16 novembre 2026, la page des offres indiquait par exemple que l'offre gratuite donne accès aux modèles Sonnet et Haiku ; que les offres payantes ajoutent Opus ; que Fable est accessible sur Pro au moyen de crédits d'utilisation, et inclus sur Max et Ultra dans la limite de la moitié de l'utilisation hebdomadaire [@ANT-PLANS]. Certaines fonctions imposent leur propre modèle : la recherche approfondie (Research) s'exécute sur Claude Opus 5.5, avec repli sur Claude Opus 4.8, quel que soit le modèle choisi dans la conversation [@ANT-HC-RESEARCH].

::: terrain
Le centre d'aide signale aussi que Claude peut **changer de modèle** au cours d'une conversation dans certaines situations (par exemple en cas d'indisponibilité). Si la qualité d'une réponse vous surprend, vérifiez le modèle affiché.
:::

#### C.4. Choisir la bonne « porte d'entrée »

Le choix ne porte pas seulement sur le modèle, mais aussi sur l'outil :

| Votre besoin | Outil adapté |
|---|---|
| Question, rédaction, analyse d'un document, échange interactif | Application Claude (conversation) |
| Dossier récurrent avec documents de référence | Application Claude + Projet (chapitre 15) |
| Tâche longue en plusieurs étapes sur des fichiers, à reprendre plus tard | Cowork |
| Traitement automatisé de données, scripts, outils internes | Claude Code (profils techniques) |
| Intégration dans une application de l'entreprise, traitement en masse | API (développeurs) |

#### C.5. Estimer un coût via l'API

Pour l'API, la facturation se fait au **nombre de tokens** en entrée (ce que vous envoyez) et en sortie (ce que Claude produit), avec des prix différents selon le modèle [@ANT-PRICING; @ANT-MODELS]. La documentation précise en outre que les requêtes par lots (*Batch API*) bénéficient d'une réduction de 50 % et que la relecture de contenu mis en cache coûte une fraction du prix d'entrée de base [@ANT-MODELS].

**Exemple de calcul (ordre de grandeur, prix au 16/11/2026) :** résumer un rapport de 50 pages (environ 25 000 mots, soit environ 45 000 tokens, sur la base d'environ 1,8 token par mot) en une synthèse de 2 000 mots (environ 3 600 tokens) avec Claude Opus 5.5 :

- entrée : 45 000 tokens × 4 USD / 1 000 000 = 0,18 USD ;
- sortie : 3 600 tokens × 20 USD / 1 000 000 ≈ 0,07 USD ;
- **total ≈ 0,25 USD**, hors tokens de réflexion (qui comptent comme des tokens de sortie).

Le même traitement répété sur 5 000 documents coûterait environ 1 250 USD avec Opus 5.5, environ 625 USD avec Sonnet 5.5, et sensiblement moins avec Haiku 5.5 — d'où l'intérêt de tester un modèle plus léger pour les traitements de masse.

::: attention
Ces calculs sont des **ordres de grandeur**. Le nombre réel de tokens dépend de la langue, des tableaux, de la réflexion du modèle et des outils utilisés. Pour un budget, mesurez sur un échantillon réel.
:::

### D. Démonstration guidée — Le test A/B de Nadine

Kevin propose à Nadine une méthode simple pour choisir objectivement.

1. **Constituer un échantillon** : 50 lignes de commandes, dont elle connaît la bonne catégorie.
2. **Rédiger un seul prompt**, identique pour tous les essais (prompt 8.1).
3. **Tester deux configurations** : Haiku 5.5 et Opus 5.5.
4. **Mesurer** : taux de bonnes réponses, temps de réponse, cas d'erreur.
5. **Décider** : si le modèle léger atteint une qualité suffisante (par exemple au moins 95 % de bonnes réponses, avec des erreurs faciles à repérer), il est retenu pour le traitement de masse ; les cas ambigus sont signalés pour revue humaine.

Résultat (fictif) : Haiku 5.5 classe correctement 48 lignes sur 50, Opus 5.5 49 sur 50 ; les erreurs portent sur deux libellés réellement ambigus. Nadine retient Haiku 5.5 avec une consigne de signalement des cas ambigus.

### E. Prompts commentés

**Prompt 8.1 — Classement à fort volume**

```text
Classe chaque ligne de commande ci-dessous dans UNE des catégories suivantes :
Réactifs | Pièces de rechange | Pneumatiques | Explosifs | Transport | Services | Autre.

Règles :
- Réponds uniquement par un tableau à 3 colonnes : bc | catégorie | confiance (haute/basse).
- Mets « basse » si le libellé est ambigu ; ne devine pas.
- N'ajoute aucun commentaire.

Lignes :
[coller les lignes : bc;article;fournisseur]
```

*Commentaire.* Pour un modèle léger et un fort volume, un format de sortie strict et une liste fermée de catégories sont essentiels. La colonne « confiance » permet de router les cas douteux vers un humain.

**Prompt 8.2 — Analyse exigeante**

```text
Tu es un géologue senior chargé de relire un rapport de ressources minérales
avant sa validation par la personne compétente.

À partir du rapport joint :
1. Vérifie la cohérence entre les tableaux de ressources, le texte et les annexes
   (tonnages, teneurs, catégories, teneur de coupure, date d'effet).
2. Liste toutes les incohérences, avec page et citation exacte.
3. Liste les informations attendues par un code de déclaration de type JORC
   qui semblent absentes ou insuffisantes.
Ne valide pas le rapport : ton rôle est de préparer la revue de la personne compétente.
```

*Commentaire.* Une tâche longue, croisée et exigeante justifie un modèle puissant et un effort élevé (chapitre 9).

### F. Exercices pratiques

**Exercice 8.1 (guidé) — Test A/B**

Avec le fichier `MCC_bons_de_commande.csv`, extrayez 30 lignes. Classez-les vous-même, puis testez deux modèles avec le prompt 8.1. Calculez le taux de bonnes réponses et notez le temps de réponse.

**Exercice 8.2 (guidé) — Estimation de coût**

Estimez le coût API du résumé mensuel des 160 incidents HSE de MCC (environ 120 mots par incident ; synthèse de 1 500 mots) avec Opus 5.5 et avec Sonnet 5.5.

**Exercice 8.3 (autonome) — Votre matrice modèle / tâche**

Pour dix tâches de votre métier, indiquez le modèle de départ, l'outil (conversation, projet, Cowork, Code, API) et la justification.

### G. Livrable professionnel

**Matrice de choix modèle / tâche** de votre service, avec, pour chaque tâche : modèle de départ, outil, niveau d'effort de départ, résultat du test éventuel, date de révision.

### H. Vérification des résultats

::: controle
- Le choix du modèle a été justifié par un critère explicite (qualité, vitesse, coût, disponibilité).
- Pour les traitements répétés, un test sur échantillon a été réalisé avec une grille de résultats.
- Les estimations de coût indiquent leurs hypothèses (mots, tokens, prix, date).
- La disponibilité du modèle dans l'offre de l'entreprise a été vérifiée.
:::

::: setrompe
Interrogé sur « le meilleur modèle Claude », un assistant peut citer de mémoire une gamme ancienne. Le nom d'un modèle n'est fiable que s'il figure dans la documentation officielle à jour ou dans le sélecteur de modèle de votre application.
:::

### I. Limites et précautions

- Un modèle plus puissant **réduit** le risque d'erreur sur les tâches complexes, mais ne le supprime pas.
- Les prix et quotas évoluent : ne figez pas une décision budgétaire sur un tarif ancien.
- Ne changez pas de modèle au milieu d'un processus validé sans refaire les tests.

### J. Boîte à outils

**Règle des trois questions pour choisir un modèle**

1. La tâche est-elle **simple et répétitive** ? → modèle léger.
2. La tâche est-elle **courante et interactive** ? → modèle équilibré.
3. La tâche est-elle **complexe, longue ou à fort enjeu** ? → modèle puissant, effort plus élevé, vérification renforcée.

**Gabarit de test A/B**

| Échantillon | Configuration A | Configuration B | Critère | Résultat A | Résultat B | Décision |
|---|---|---|---|---|---|---|
| 50 lignes | Haiku 5.5 / effort low | Opus 5.5 / effort medium | % correct | | | |

### K. Quiz

1. **(QCM)** Pour classer 5 000 libellés simples, quel modèle testez-vous en premier ? a) Fable 5.2 ; b) Haiku 5.5 ; c) aucun ; d) le plus cher par principe.
2. **(Vrai ou faux)** La recherche approfondie s'exécute toujours sur le modèle sélectionné dans la conversation.
3. **(Compréhension)** Quels sont les quatre critères de choix d'un modèle ?
4. **(Calcul)** Combien coûte approximativement l'envoi de 100 000 tokens en entrée à Claude Sonnet 5.5 (2 USD par million de tokens) ?
5. **(QCM)** Quel outil choisir pour intégrer Claude dans le portail HSE interne de l'entreprise ? a) l'application mobile ; b) l'API ; c) un compte gratuit ; d) la mémoire.
6. **(Mise en situation)** Les analyses de Patrick sont superficielles. Proposez deux ajustements.
7. **(Vrai ou faux)** Les requêtes par lots via l'API bénéficient d'une réduction de prix selon la documentation consultée.
8. **(Analyse critique)** Pourquoi faut-il refaire des tests quand on change de modèle dans un processus validé ?
9. **(Compréhension)** À quoi sert la colonne « confiance » du prompt 8.1 ?
10. **(Application)** Quel outil de l'écosystème convient à une tâche longue en plusieurs étapes sur des fichiers, que vous souhaitez pouvoir reprendre ?

<div class="carnet" titre="Chapitre 8 — Comprendre les modèles et choisir le bon outil pour chaque tâche"></div>
