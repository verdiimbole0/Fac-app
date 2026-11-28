## Chapitre 2. Comprendre les fondamentaux de l'intelligence artificielle

### A. Mise en situation professionnelle

Réunion du comité de direction de MCC. Le directeur des opérations présente le projet de maintenance prédictive des camions : « L'IA va prévoir les pannes trois jours à l'avance. » Le directeur financier enchaîne : « Justement, j'ai utilisé l'IA hier pour rédiger la note sur les redevances. » La responsable environnement ajoute : « Et le fournisseur du système de tri du minerai dit aussi que sa machine utilise de l'IA. »

Trois personnes, trois « IA » très différentes. Autour de la table, personne ne sait vraiment si ces outils ont quelque chose en commun, ni pourquoi l'un peut se tromper sur un calcul simple tandis que l'autre détecte une vibration anormale invisible à l'œil humain. Kevin Mutombo, le référent IA, est chargé de clarifier le vocabulaire avant la prochaine réunion.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Définir** avec vos propres mots l'intelligence artificielle, l'apprentissage automatique, l'apprentissage profond, le traitement du langage naturel et l'IA générative.
2. **Expliquer** la relation d'emboîtement entre ces notions.
3. **Distinguer** une IA prédictive d'une IA générative à partir d'un exemple minier.
4. **Décrire** simplement ce qu'est un réseau de neurones et ce que signifie « entraîner » un modèle.
5. **Associer** à chaque famille d'IA des usages pertinents dans une entreprise minière.

### C. Comprendre avant de pratiquer

#### C.1. L'intelligence artificielle : une définition pratique

L'**intelligence artificielle (IA)** désigne l'ensemble des techniques qui permettent à un système informatique de réaliser des tâches que l'on associe habituellement à l'intelligence humaine : reconnaître une image, comprendre une phrase, prévoir un événement, proposer une décision, rédiger un texte.

Le cadre de gestion des risques de l'IA publié par l'institut américain des normes et de la technologie (NIST) définit un système d'IA comme un système fondé sur des machines qui, pour des objectifs donnés, peut produire des résultats tels que des prédictions, des recommandations ou des décisions influençant des environnements réels ou virtuels [@NIST-RMF]. Cette définition a un mérite : elle insiste sur les **résultats** et sur leur **influence**, donc sur la responsabilité de ceux qui les utilisent.

Historiquement, deux grandes approches se sont succédé :

- **Les systèmes à règles** : un expert écrit les règles (« si la teneur est inférieure à 0,8 % Cu, le bloc est classé stérile »). Le système est transparent, mais rigide : il ne sait faire que ce qu'on lui a explicitement appris.
- **Les systèmes qui apprennent** : au lieu d'écrire les règles, on fournit des exemples, et le système **apprend** les régularités. C'est l'apprentissage automatique.

#### C.2. L'apprentissage automatique (machine learning)

L'**apprentissage automatique** est une branche de l'IA dans laquelle un modèle apprend à partir de données. Prenons un exemple minier.

> *Analogie.* Un géologue expérimenté reconnaît une roche minéralisée au premier coup d'œil, parce qu'il en a vu des milliers. Personne ne lui a donné une règle écrite pour chaque cas : il a appris par l'exemple. L'apprentissage automatique fonctionne de manière comparable, mais avec des données chiffrées et des calculs statistiques.

On distingue trois grandes familles :

| Famille | Principe | Exemple minier |
|---|---|---|
| Apprentissage supervisé | Le modèle apprend à partir d'exemples dont on connaît la bonne réponse | Prédire la récupération métallurgique à partir des caractéristiques du minerai et des résultats passés |
| Apprentissage non supervisé | Le modèle cherche des regroupements dans des données sans étiquette | Regrouper des échantillons géochimiques en familles de signatures |
| Apprentissage par renforcement | Le modèle apprend par essais et erreurs, en recevant des récompenses | Optimiser la répartition des camions entre les pelles |

Un modèle d'apprentissage automatique est **entraîné** sur des données passées, puis **utilisé** sur des données nouvelles. Sa qualité dépend fortement de la qualité, de la quantité et de la représentativité des données d'entraînement.

::: attention
Un modèle entraîné sur les données de la fosse Mbiyo Nord peut donner de mauvais résultats sur la fosse Mbiyo Sud si la minéralogie y est différente. Un modèle n'est fiable que dans le domaine où il a été entraîné et validé.
:::

#### C.3. L'apprentissage profond et les réseaux de neurones

L'**apprentissage profond (deep learning)** est une sous-famille de l'apprentissage automatique qui utilise des **réseaux de neurones artificiels** comportant de nombreuses couches.

Un **réseau de neurones artificiel** est un modèle mathématique composé d'unités de calcul (les « neurones ») organisées en couches. Chaque neurone reçoit des valeurs, les combine selon des **poids** (des coefficients numériques) et transmet un résultat à la couche suivante. Pendant l'**entraînement**, ces poids sont ajustés progressivement pour réduire l'écart entre la réponse du modèle et la réponse attendue.

![Figure 2.1. Un réseau de neurones, vu de très loin. Les données entrent à gauche, traversent des couches cachées qui construisent des représentations de plus en plus abstraites, et produisent une sortie à droite. Chaque lien porte un poids ajusté pendant l'entraînement. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig02_3_reseau_neurones.png){width=85%}

L'apprentissage profond a permis des progrès spectaculaires dans la reconnaissance d'images (détection automatique d'équipements de protection individuelle sur une vidéo, analyse de photographies de carottes de sondage), la reconnaissance vocale et, surtout, le traitement du langage.

#### C.4. Le traitement automatique du langage naturel

Le **traitement automatique du langage naturel (TALN)** regroupe les techniques qui permettent aux machines de traiter le langage humain : classer des textes, extraire des informations, traduire, résumer, répondre à des questions.

Pendant longtemps, ces techniques ont été spécialisées : un modèle pour la traduction, un autre pour la classification des courriels, un autre pour l'extraction d'entités nommées. En 2017, une architecture de réseau de neurones appelée **Transformer** a été présentée par des chercheurs dans l'article « Attention Is All You Need » [@VASWANI-2017]. Elle repose sur un mécanisme dit d'**attention**, qui permet au modèle de prendre en compte les relations entre tous les mots d'un texte, même éloignés. Cette architecture est à l'origine des grands modèles de langage actuels, dont Claude.

#### C.5. L'IA générative

L'**IA générative** désigne les systèmes capables de **produire de nouveaux contenus** (texte, images, code, sons) à partir d'une instruction. Les **grands modèles de langage** (en anglais *Large Language Models*, LLM) en sont la forme la plus répandue pour le travail de bureau : ils sont entraînés sur de très grandes quantités de textes et apprennent à prédire la suite la plus probable d'un texte. Le chapitre 3 explique en détail ce mécanisme.

![Figure 2.2. Des concepts emboîtés. L'IA générative et les grands modèles de langage sont un cas particulier de l'apprentissage profond, lui-même branche de l'apprentissage automatique, lui-même branche de l'intelligence artificielle. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig02_1_emboitement.png){width=72%}

#### C.6. IA prédictive et IA générative : deux familles complémentaires

La distinction la plus utile pour un professionnel minier oppose l'**IA prédictive** (ou analytique) et l'**IA générative**.

![Figure 2.3. IA prédictive et IA générative. La première produit un chiffre, une classe ou une alerte à partir de données structurées ; la seconde produit du texte, des tableaux ou du code à partir d'instructions en langage naturel. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig02_2_classique_vs_generative.png){width=100%}

*Tableau 2.1. Comparaison des deux familles.*

| Critère | IA prédictive | IA générative (LLM) |
|---|---|---|
| Entrée | Données structurées (capteurs, tableaux) | Texte, documents, images, instructions |
| Sortie | Nombre, catégorie, probabilité, alerte | Texte, tableau, code, document |
| Spécialisation | Une tâche précise | Polyvalente |
| Construction | Entraînée sur les données de l'entreprise | Modèle généraliste utilisé tel quel, guidé par des instructions |
| Évaluation | Métriques statistiques (erreur, précision) | Jugement d'expert, vérification des faits |
| Exemple à MCC | Prédire la panne du camion CAM-07 | Rédiger le rapport sur l'incident du CAM-07 |
| Erreur typique | Fausse alerte, panne non détectée | Affirmation fausse mais plausible, calcul erroné |

Les deux familles se complètent. À MCC, le système de maintenance prédictive signale une anomalie de pression hydraulique sur le camion CAM-07 ; Claude aide ensuite le planificateur à rédiger l'ordre de travail, à retrouver l'historique des interventions et à préparer la note de synthèse pour le responsable maintenance.

::: retenir
- L'**IA prédictive** répond à la question « que va-t-il se passer ? » à partir de données chiffrées.
- L'**IA générative** répond à la question « comment le dire, le structurer, l'analyser ? » à partir de langage et de documents.
- Claude appartient à la seconde famille. Il n'est pas conçu pour remplacer vos logiciels de modélisation géologique, de planification minière ou de contrôle-commande.
:::

#### C.7. Quelques termes à connaître

| Terme | Définition simple |
|---|---|
| Modèle | Programme mathématique entraîné qui transforme une entrée en sortie |
| Entraînement | Phase pendant laquelle le modèle ajuste ses paramètres à partir de données |
| Paramètres (poids) | Coefficients numériques internes du modèle ; les grands modèles en comptent des milliards |
| Inférence | Utilisation du modèle entraîné pour produire une réponse |
| Données d'entraînement | Données utilisées pour apprendre |
| Biais | Déformation systématique des résultats, souvent héritée des données |
| Surapprentissage | Le modèle « récite » ses données d'entraînement et généralise mal |
| Prompt | Instruction donnée à un modèle génératif |

### D. Démonstration guidée : Faire expliquer un concept par Claude, puis le contrôler

Kevin Mutombo prépare une fiche d'une page pour le comité de direction. Il utilise Claude comme tuteur, en procédant en quatre temps.

**Étape 1. Demander une explication adaptée au public.** Kevin précise que les lecteurs sont des directeurs non spécialistes et qu'il veut des exemples miniers (prompt 2.1).

**Étape 2. Demander une auto-vérification.** Il demande ensuite à Claude de relire son explication et de signaler les simplifications qui pourraient induire en erreur (prompt 2.2). Claude signale notamment que l'expression « l'IA apprend comme un humain » est une analogie trompeuse si elle est prise au pied de la lettre.

**Étape 3. Confronter à une source de référence.** Kevin compare la définition proposée à celle du NIST [@NIST-RMF] et ajuste sa fiche.

**Étape 4. Tester la compréhension.** Il demande à Claude cinq questions de quiz pour vérifier que les directeurs ont compris. Il les utilisera en fin de réunion.

### E. Prompts commentés

**Prompt 2.1. Explication adaptée à un public**

```text
Explique la différence entre IA prédictive et IA générative à des directeurs
d'une entreprise minière (cuivre-cobalt) qui ne sont pas spécialistes du numérique.

Contraintes :
- 300 mots maximum ;
- deux exemples miniers concrets pour chaque famille ;
- une analogie simple, en précisant ses limites ;
- termine par trois questions que la direction devrait poser à un fournisseur
  qui prétend vendre une « solution d'IA ».
Évite le jargon ; si tu emploies un terme technique, définis-le en une phrase.
```

*Commentaire.* Le public est précisé (directeurs non spécialistes), la longueur est limitée, les exemples sont imposés dans le domaine minier. La demande de préciser « les limites de l'analogie » évite qu'une image simplificatrice soit prise pour une vérité.

**Prompt 2.2. Auto-critique**

```text
Relis l'explication que tu viens de produire, comme le ferait un spécialiste
de l'apprentissage automatique exigeant. Liste :
1. les simplifications qui pourraient induire un lecteur en erreur ;
2. les affirmations qui mériteraient une source ;
3. une version corrigée des passages concernés.
```

*Commentaire.* Demander à Claude de critiquer sa propre réponse améliore souvent la précision. Cela ne remplace pas une vérification indépendante, mais c'est un premier filtre utile.

**Prompt 2.3. Qualifier une « solution d'IA » proposée par un fournisseur**

```text
Un fournisseur propose à notre mine un système de « tri du minerai par IA ».
Voici sa brochure commerciale : [coller le texte].

Aide-moi à préparer la réunion :
1. De quelle famille d'IA s'agit-il probablement (prédictive, générative, autre) ?
2. Quelles données le système utilise-t-il et sur quelles données a-t-il été entraîné ?
3. Quelles questions poser sur ses performances, sa validation et ses limites ?
4. Quelles affirmations de la brochure sont invérifiables en l'état ?
Ne suppose rien qui ne soit pas écrit dans la brochure ; signale ce qui manque.
```

### F. Exercices pratiques

**Exercice 2.1 (guidé) : Classer des cas d'usage**

Classez les dix cas suivants en IA prédictive, IA générative ou autre technologie (automatisme, logiciel classique) :

1. Prévoir la teneur d'un bloc à partir des sondages voisins.
2. Rédiger le résumé non technique d'une étude d'impact.
3. Détecter le non-port du casque sur les images d'une caméra.
4. Traduire en anglais un contrat de vente de cathodes.
5. Arrêter automatiquement un convoyeur quand un capteur détecte un bourrage.
6. Proposer cinq questions pour une causerie sécurité sur la conduite de nuit.
7. Estimer la durée de vie restante d'un roulement à partir des vibrations.
8. Résumer 95 plaintes communautaires par thème.
9. Calculer la paie selon le barème de la convention collective.
10. Générer un premier jet de procédure de consignation à partir de notes.

*Corrigé indicatif :* prédictive : 1, 3, 7 (3 relève de la vision par ordinateur, une branche de l'apprentissage profond) ; générative : 2, 4, 6, 8, 10 ; autre : 5 (automatisme), 9 (logiciel de paie à règles).

**Exercice 2.2 (autonome) : La fiche « IA expliquée à mon équipe »**

Rédigez, avec l'aide de Claude, une fiche d'une page qui explique à votre équipe les notions de ce chapitre, avec deux exemples tirés de votre métier. Faites-la relire par un collègue non spécialiste : comprend-il la différence entre IA prédictive et IA générative ?

### G. Livrable professionnel

**Fiche « L'IA expliquée à mon équipe »** (1 page) comprenant : une définition de l'IA, le schéma d'emboîtement, le tableau prédictive / générative adapté à votre métier, trois précautions d'usage et une source de référence citée.

### H. Vérification des résultats

::: controle
- Les définitions sont-elles cohérentes avec une source de référence (par exemple le NIST) ?
- Les exemples sont-ils techniquement plausibles dans votre contexte ?
- Les analogies sont-elles accompagnées de leurs limites ?
- Aucune promesse de performance chiffrée n'apparaît sans source.
:::

::: setrompe
Interrogé sur l'origine des modèles de langage, un assistant d'IA peut attribuer une publication à de mauvais auteurs ou à une mauvaise année, avec une grande assurance. Vérifiez systématiquement les références bibliographiques : titre, auteurs, année, éditeur et lien doivent être retrouvés dans une source fiable. C'est ce qui a été fait pour chaque référence de ce livre.
:::

### I. Limites et précautions

- Les catégories présentées sont des **simplifications pédagogiques** : certains systèmes combinent plusieurs familles d'IA.
- Le mot « IA » est souvent utilisé à des fins commerciales. Exigez toujours une description précise de la technologie, des données utilisées et des performances mesurées.
- Comprendre les principes ne dispense pas de faire appel à des spécialistes pour **concevoir** ou **valider** un modèle prédictif utilisé dans des décisions d'exploitation.

### J. Boîte à outils

**Fiche pratique 2.1 : Les cinq questions à poser à tout fournisseur de « solution IA »**

1. Quelle famille d'IA utilisez-vous, et pour quelle tâche précise ?
2. Sur quelles données le modèle a-t-il été entraîné ? Sont-elles comparables aux nôtres ?
3. Comment les performances ont-elles été mesurées, sur quelles données de test ?
4. Que se passe-t-il quand le modèle se trompe ? Qui est alerté, qui décide ?
5. Où sont stockées nos données, et sont-elles utilisées pour entraîner vos modèles ?

**Prompt réutilisable 2.4 : Tuteur personnel**

```text
Tu es mon tuteur pour comprendre [notion]. Je suis [fonction] dans le secteur minier,
sans formation en informatique. Explique la notion en trois niveaux :
(1) en une phrase ; (2) en un paragraphe avec un exemple minier ;
(3) en détail, avec les limites et les idées reçues à éviter.
Pose-moi ensuite deux questions pour vérifier ma compréhension.
```

### K. Quiz

1. **(QCM)** L'apprentissage profond est : a) une alternative à l'apprentissage automatique ; b) une sous-famille de l'apprentissage automatique ; c) un synonyme d'IA générative ; d) une technique de forage.
2. **(Vrai ou faux)** Un système à règles apprend automatiquement à partir des données.
3. **(QCM)** Quelle architecture, présentée en 2017, est à l'origine des grands modèles de langage actuels ? a) le perceptron ; b) le Transformer ; c) le krigeage ; d) l'arbre de décision.
4. **(Compréhension)** Qu'est-ce qu'un « poids » dans un réseau de neurones ?
5. **(Application)** Donnez un exemple minier d'apprentissage supervisé et précisez la « bonne réponse » connue utilisée pour l'entraînement.
6. **(Vrai ou faux)** Claude est conçu pour remplacer le logiciel de modélisation géologique de la mine.
7. **(Mise en situation)** Un modèle prédictif de récupération entraîné sur le minerai oxydé est appliqué au minerai sulfuré de « Mbiyo Profond ». Quel risque identifiez-vous ?
8. **(QCM)** Quelle sortie est typique d'une IA générative ? a) une probabilité de panne ; b) une alerte de vibration ; c) un projet de procédure rédigé ; d) une classe « minerai / stérile ».
9. **(Analyse critique)** Pourquoi la définition du NIST insiste-t-elle sur l'« influence » des résultats d'un système d'IA ?
10. **(Compréhension)** Citez deux erreurs typiques d'une IA générative et une erreur typique d'une IA prédictive.

<div class="carnet" titre="Chapitre 2. Comprendre les fondamentaux de l'intelligence artificielle"></div>
