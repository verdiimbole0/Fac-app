## Chapitre 1 — L'industrie minière à l'ère de l'intelligence artificielle

### A. Mise en situation professionnelle

Lundi, 7 h 30, bureaux de Mbiyo Copper Cobalt SA à Kolwezi. Aline Mujinga, directrice générale, ouvre sa messagerie. Le conseil d'administration lui demande, pour la réunion de jeudi, « une position claire sur l'intelligence artificielle ». Un administrateur a lu qu'une grande compagnie minière avait « réduit de moitié le temps de production de ses rapports grâce à l'IA » ; un autre s'inquiète des fuites de données ; un troisième veut savoir si l'IA peut « remplacer des postes ».

Dans le même temps, la réalité du terrain s'impose : le rapport mensuel de production a trois jours de retard, car les données de la mine, de l'usine et du laboratoire arrivent dans des formats différents ; le service HSE doit synthétiser 160 déclarations d'incident avant l'audit ; le service juridique attend l'analyse de vingt contrats de sous-traitance ; et le géologue principal n'a toujours pas rédigé la mise à jour annuelle des ressources.

Aline a besoin de comprendre trois choses avant jeudi : **où** l'intelligence artificielle peut réellement aider une entreprise comme MCC, **ce qu'elle ne doit pas faire**, et **comment** démarrer sans risque. C'est l'objet de ce premier chapitre.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Situer** les grandes étapes du cycle minier et les principaux documents produits à chaque étape.
2. **Distinguer** les différentes vagues technologiques de l'industrie minière (mécanisation, automatisation, données, IA prédictive, IA générative).
3. **Identifier**, dans votre propre fonction, au moins dix tâches documentaires susceptibles d'être assistées par Claude.
4. **Classer** ces tâches selon leur intérêt et leur niveau de risque.
5. **Produire** une première « carte des opportunités IA » de votre service, utilisable pour une discussion avec votre hiérarchie.

### C. Comprendre avant de pratiquer

#### C.1. Une industrie stratégique, sous pression

L'industrie minière fournit les matières premières de la transition énergétique. Les technologies bas carbone — éolien, solaire, batteries, réseaux électriques — consomment davantage de métaux que les technologies fossiles qu'elles remplacent ; une étude de la Banque mondiale a montré qu'un avenir bas carbone serait « très intensif en minéraux » et que, même avec un recyclage accru, l'extraction minière resterait nécessaire [@WB-MCA-2020]. L'Agence internationale de l'énergie suit, dans ses perspectives annuelles sur les minéraux critiques, la forte concentration géographique de la production et du raffinage de ces substances [@IEA-GCMO2025].

La République démocratique du Congo occupe une place centrale dans ce paysage. Selon l'Institut d'études géologiques des États-Unis (USGS), le pays était en 2025 la première source mondiale de cobalt extrait, avec environ 73 % de la production mondiale (estimation de 230 000 tonnes sur environ 310 000 tonnes), et le deuxième producteur minier de cuivre après le Chili, avec environ 3,2 millions de tonnes sur 23 millions [@USGS-MCS2026, fiches « Cobalt » et « Copper »].

![Figure 1.1 — Production minière de cuivre et de cobalt en 2025 (estimations). La RDC est le deuxième producteur minier de cuivre et le premier producteur de cobalt. Données : U.S. Geological Survey (2026). Graphique réalisé pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig01_3_rdc_cuivre_cobalt.png){width=100%}

Cette position s'accompagne de fortes exigences : transparence des revenus (la RDC est pays de mise en œuvre de l'Initiative pour la transparence dans les industries extractives [@EITI-RDC]), devoir de diligence sur les chaînes d'approvisionnement [@OECD-DDG], sécurité des travailleurs [@ILO-C176], gestion des résidus [@GISTM-2020], attentes croissantes des investisseurs et des communautés. Chacune de ces exigences se traduit par **davantage de documents, de données, de contrôles et de rapports**.

#### C.2. Une industrie qui vit de documents

On imagine souvent la mine comme un univers de machines. C'est vrai, mais c'est aussi un univers de documents. Le tableau 1.1 en donne un aperçu pour une entreprise comme MCC.

*Tableau 1.1 — Exemples de documents produits ou utilisés à chaque étape du cycle minier.*

| Étape | Documents typiques | Qui les produit ? |
|---|---|---|
| Exploration | Journaux de sondage, certificats d'analyse, cartes, rapports d'exploration | Géologues, laboratoires |
| Études | Estimation des ressources et réserves, études de faisabilité, étude d'impact environnemental et social (EIES) | Géologues, ingénieurs, consultants |
| Construction | Contrats d'ingénierie, plannings, rapports d'avancement, réceptions | Ingénieurs, chefs de projet, achats |
| Extraction | Plans de tir, rapports de poste, plans miniers, rapports de production | Ingénieurs, superviseurs |
| Traitement | Bilans métallurgiques, rapports de laboratoire, procédures d'usine | Métallurgistes, opérateurs |
| Maintenance | Ordres de travail, historiques d'équipement, plans de maintenance | Techniciens, planificateurs |
| HSE | Déclarations d'incident, analyses de risques, rapports d'enquête, audits | Équipe HSE, superviseurs |
| Environnement | Suivi de l'eau et de l'air, rapports réglementaires, plan de fermeture | Environnementalistes |
| Communautés | Registres de plaintes, comptes rendus de consultations, cahier des charges | Relations communautaires |
| Finance et fiscalité | Budgets, états financiers, déclarations de redevances, rapports ITIE | Finance, fiscalité |
| Juridique | Titres miniers, contrats, correspondances avec l'administration | Juristes |
| Gouvernance | Rapports au conseil, rapports de durabilité, tableaux de bord | Direction |

![Figure 1.2 — La chaîne de valeur minière et les points d'appui de l'IA générative. Chaque étape produit et consomme des documents ; les fonctions transversales accompagnent tout le cycle de vie. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig01_1_chaine_valeur.png){width=100%}

::: retenir
L'intelligence artificielle générative n'extrait pas de minerai. Elle aide à **lire, écrire, structurer, analyser et contrôler** l'information qui accompagne chaque tonne extraite. C'est là, d'abord, qu'elle crée de la valeur.
:::

#### C.3. Cinq vagues technologiques

L'industrie minière n'en est pas à sa première révolution technologique. Pour comprendre la place de Claude, il est utile de distinguer cinq vagues, qui se superposent plus qu'elles ne se remplacent (interprétation de l'auteur) :

1. **La mécanisation** : engins de grande capacité, foreuses, convoyeurs. Elle a transformé la productivité physique.
2. **L'automatisation** : contrôle-commande des usines, camions autonomes dans certaines grandes mines, foreuses télécommandées. Elle agit sur l'exécution des opérations.
3. **La numérisation et les données** : capteurs, systèmes de gestion de flotte, logiciels de modélisation géologique, progiciels de gestion intégrée (ERP), gestion de la maintenance assistée par ordinateur (GMAO). Elle produit des volumes considérables de données.
4. **L'IA prédictive** : modèles d'apprentissage automatique qui prédisent une panne, estiment une teneur, optimisent une recette de broyage. Elle exploite des **données structurées** pour produire un **chiffre** ou une **alerte**.
5. **L'IA générative** : modèles de langage comme Claude, capables de comprendre et de produire du texte, d'analyser des documents et des images, de rédiger du code. Elle agit sur le **travail intellectuel et documentaire**.

Un rapport du Forum intergouvernemental sur l'exploitation minière (IGF) souligne que la numérisation, les mégadonnées et l'automatisation transforment le secteur minier, avec des effets sur l'emploi local, l'approvisionnement local et les recettes publiques [@IGF-2019]. Ces effets concernent aussi l'IA générative : nous y reviendrons au chapitre 39.

#### C.4. Ce que l'IA générative change concrètement

Pour un professionnel minier, l'IA générative change surtout la manière de réaliser six grandes familles de tâches :

| Famille de tâches | Exemple à MCC | Apport possible de Claude |
|---|---|---|
| Rédiger | Rapport d'incident, note au comité de direction, procédure | Premier jet structuré en quelques minutes |
| Synthétiser | Résumer une étude d'impact de 400 pages | Synthèse ciblée, avec citations des passages |
| Analyser | Comparer budget et réel, repérer des anomalies dans un fichier de sondages | Pistes d'analyse, calculs vérifiables, questions à poser |
| Transformer | Convertir des notes de terrain en tableau, traduire un contrat | Restructuration rapide de l'information |
| Contrôler | Vérifier qu'un rapport respecte une check-list | Relecture systématique, signalement des écarts |
| Apprendre | Comprendre une norme, préparer une formation | Explications adaptées au niveau du lecteur |

::: attention
Chacune de ces contributions doit être **vérifiée** par un professionnel compétent. Une synthèse peut omettre un point clé, un calcul peut être faux, une référence peut être inventée. Le chapitre 5 détaille ces risques.
:::

#### C.5. Les défis spécifiques du secteur minier

L'introduction de l'IA générative dans une entreprise minière soulève des défis particuliers :

- **La sécurité des personnes** : de nombreuses décisions minières engagent directement la vie humaine (tirs, stabilité des talus et des digues, interventions d'urgence). Ces décisions relèvent de personnes qualifiées et de procédures établies ; elles ne se délèguent pas à une IA.
- **La confidentialité** : données géologiques, réserves, contrats, informations fiscales et données personnelles sont sensibles, parfois réglementées ou boursièrement privilégiées.
- **La qualité des données** : un modèle ne corrige pas des données de terrain incomplètes ou erronées ; il peut même masquer leurs défauts sous une rédaction impeccable.
- **La connectivité** : les sites miniers sont souvent isolés ; l'accès à Internet peut être limité ou coûteux.
- **Les compétences** : l'outil n'apporte de valeur qu'entre les mains de professionnels formés à l'utiliser et à en contrôler les résultats.
- **L'acceptabilité sociale** : les communautés, les syndicats et les autorités sont attentifs aux effets de la technologie sur l'emploi et sur la transparence.

### D. Démonstration guidée — Cartographier les tâches documentaires d'un service

Grace Nsimba, responsable HSE de MCC, veut savoir où Claude pourrait aider son équipe. Plutôt que de partir de l'outil (« que peut faire Claude ? »), elle part de son travail (« que fait mon équipe chaque semaine ? »). C'est la démarche que nous vous recommandons.

**Étape 1 — Lister les tâches récurrentes.** Grace dresse, avec deux collaborateurs, la liste des tâches de l'équipe sur un mois type : rédaction des rapports d'incident, synthèse mensuelle des indicateurs, préparation des causeries sécurité, mise à jour des analyses de risques, suivi des actions correctives, préparation des audits, formation des nouveaux arrivants, veille réglementaire.

**Étape 2 — Estimer le temps passé.** Pour chaque tâche, l'équipe estime le nombre d'heures par mois. Ces estimations n'ont pas besoin d'être précises : un ordre de grandeur suffit.

**Étape 3 — Qualifier chaque tâche.** Pour chaque tâche, Grace répond à quatre questions :

- La tâche consiste-t-elle surtout à **lire, écrire, structurer ou comparer** de l'information ?
- Les données nécessaires sont-elles **disponibles sous forme numérique** ?
- Quelles seraient les **conséquences d'une erreur** ?
- Le résultat est-il **facile à vérifier** par un expert ?

**Étape 4 — Demander à Claude de structurer et de compléter l'analyse.** Grace ouvre une nouvelle conversation dans Claude et lui fournit sa liste (sans aucune donnée confidentielle), avec la consigne présentée dans la section E.

**Étape 5 — Relire, corriger et prioriser.** Claude propose une matrice et des idées. Grace corrige les estimations irréalistes, supprime les usages inadaptés (par exemple, Claude avait suggéré de « déterminer automatiquement la gravité potentielle des incidents » ; Grace décide que la classification restera faite par un humain, Claude proposant seulement une pré-classification argumentée) et retient trois cas d'usage pilotes.

::: application
À l'issue de l'exercice, l'équipe HSE de MCC retient trois pilotes : (1) premier jet des rapports d'incident à partir des déclarations brutes ; (2) synthèse mensuelle des indicateurs avec commentaire des tendances ; (3) préparation des causeries sécurité hebdomadaires à partir des incidents récents. Ces trois cas sont développés au chapitre 23.
:::

### E. Prompts commentés

**Prompt 1.1 — Cartographie des tâches d'un service**

```text
Je suis responsable HSE dans une entreprise minière à ciel ouvert (cuivre-cobalt,
2 350 personnes, sous-traitants compris). Je veux identifier où un assistant d'IA
générative pourrait aider mon équipe de 6 personnes.

Voici la liste de nos tâches récurrentes, avec une estimation du temps mensuel :
- Rédaction des rapports d'incident : 40 h
- Synthèse mensuelle des indicateurs HSE : 16 h
- Préparation des causeries sécurité : 12 h
- Mise à jour des analyses de risques : 24 h
- Suivi des actions correctives : 20 h
- Préparation des audits internes et externes : 18 h
- Formation des nouveaux arrivants : 30 h
- Veille réglementaire : 8 h

Pour chaque tâche :
1. Indique ce qu'un assistant comme toi pourrait concrètement faire.
2. Indique ce qui doit absolument rester sous la responsabilité d'un humain.
3. Évalue l'intérêt (faible / moyen / fort) et le niveau de risque (faible / moyen / élevé).
4. Précise les données ou documents dont tu aurais besoin.

Présente le résultat sous forme de tableau, puis propose 3 cas d'usage pilotes
à fort intérêt et faible risque, en justifiant ton choix en 3 lignes chacun.
Ne propose aucune délégation de décision de sécurité.
```

**Pourquoi ce prompt fonctionne :**

| Élément du prompt | Rôle |
|---|---|
| « Je suis responsable HSE dans une entreprise minière… » | Donne le **contexte** : Claude adapte ses propositions au secteur et à la fonction. |
| La liste des tâches avec les heures | Fournit des **données** concrètes au lieu de demander des généralités. |
| Les quatre questions numérotées | Précisent l'**action** attendue et garantissent une analyse complète. |
| « Présente le résultat sous forme de tableau… » | Fixe les **exigences de sortie**. |
| « Ne propose aucune délégation de décision de sécurité » | Pose une **règle** explicite, conforme à la politique de l'entreprise. |

Vous reconnaîtrez là les cinq briques de la méthode **CADRE** (Contexte, Action, Données, Règles, Exigences de sortie), que nous développerons au chapitre 10.

**Prompt 1.2 — Préparer une note de position pour la direction**

```text
Je suis directrice générale d'une société minière (cuivre-cobalt, RDC, 2 350 personnes).
Mon conseil d'administration me demande une position sur l'IA générative.

Rédige une note de 2 pages maximum, destinée à des administrateurs non spécialistes,
structurée ainsi :
1. Ce que l'IA générative peut apporter à une entreprise minière (exemples concrets).
2. Ce qu'elle ne doit pas faire (décisions de sécurité, décisions engageantes).
3. Les principaux risques (confidentialité, erreurs, dépendance, image).
4. Une démarche de démarrage prudente en 3 étapes sur 6 mois.
5. Les décisions attendues du conseil.

Règles : ton factuel et mesuré ; aucun chiffre de gain de productivité sans source ;
si tu cites une étude ou une norme, indique clairement que la référence doit être
vérifiée avant diffusion.
```

**Commentaire.** La consigne « aucun chiffre de gain de productivité sans source » est essentielle : sans elle, un modèle de langage peut produire des pourcentages plausibles mais non fondés. La dernière règle prépare la vérification des références, que nous traiterons au chapitre 14.

::: erreur
Demander « Qu'est-ce que l'IA peut faire pour une mine ? » produit une liste générique, valable pour n'importe quelle entreprise. Partez **toujours** de vos tâches réelles, de vos documents et de vos contraintes.
:::

### F. Exercices pratiques

**Exercice 1.1 (guidé) — Inventaire de vos tâches documentaires**

1. Sur une feuille ou dans un tableur, listez 10 à 15 tâches que vous réalisez au moins une fois par mois.
2. Pour chacune, estimez le temps mensuel et indiquez si elle consiste principalement à lire, écrire, structurer, comparer, calculer ou décider.
3. Utilisez le prompt 1.1 en l'adaptant à votre fonction.
4. Comparez la réponse de Claude à votre propre jugement : sur quelles tâches êtes-vous d'accord ? Sur lesquelles Claude a-t-il été trop optimiste ou trop prudent ?

*Critère de réussite :* vous disposez d'un tableau de 10 tâches au moins, chacune qualifiée (intérêt, risque, données nécessaires), relu et corrigé par vous.

**Exercice 1.2 (autonome) — La carte des opportunités de MCC**

Choisissez un département de MCC (maintenance, finance, environnement ou relations communautaires). À partir de la fiche de l'entreprise (Avant-propos) et de votre connaissance du métier, construisez la carte des opportunités IA du département : 8 tâches, classées dans la matrice intérêt / risque, avec 2 pilotes recommandés et 2 usages à exclure explicitement.

::: defi
Trouvez, dans votre fonction, une tâche que vous jugiez « impossible à assister par une IA » et demandez-vous pourquoi. Est-ce parce qu'elle exige une présence physique ? Une décision engageante ? Des données inaccessibles ? Ce raisonnement vous servira tout au long du manuel.
:::

### G. Livrable professionnel

À la fin de ce chapitre, vous devez être capable de produire une **carte des opportunités IA** de votre service, d'une page, comprenant :

*Tableau 1.2 — Modèle de carte des opportunités IA (extrait, service HSE de MCC, fictif).*

| Tâche | Temps/mois | Apport possible de Claude | Reste humain | Intérêt | Risque | Décision |
|---|---|---|---|---|---|---|
| Rapports d'incident | 40 h | Premier jet structuré à partir des déclarations | Faits, causes, classification, signature | Fort | Moyen | Pilote 1 |
| Synthèse mensuelle des indicateurs | 16 h | Calculs, graphiques, commentaire des tendances | Validation des chiffres, interprétation | Fort | Faible | Pilote 2 |
| Causeries sécurité | 12 h | Supports adaptés à partir d'incidents réels | Choix du thème, animation | Moyen | Faible | Pilote 3 |
| Analyses de risques | 24 h | Relecture, suggestions de dangers oubliés | Évaluation, mesures de maîtrise | Moyen | Élevé | Plus tard, avec garde-fous |
| Décision d'arrêt d'un chantier | — | Aucun | Totalité | — | Critique | Exclu |

### H. Vérification des résultats

Avant de présenter votre carte des opportunités, vérifiez :

::: controle
- Chaque tâche est **réelle** et correspond à votre activité (pas une idée générique proposée par Claude).
- Les **estimations de temps** proviennent de vous ou de votre équipe, pas de Claude.
- Aucune **décision critique** pour la sécurité n'est classée comme « déléguée ».
- Les **données nécessaires** sont identifiées et leur niveau de confidentialité est connu.
- Les gains annoncés sont formulés comme des **hypothèses à mesurer**, pas comme des certitudes.
:::

### I. Limites et précautions

- **Ne surestimez pas les gains.** Les premiers usages demandent un temps d'apprentissage. Mesurez avant et après sur un échantillon de tâches.
- **Ne partagez pas d'informations confidentielles** pour réaliser cette cartographie : la liste des tâches et les volumes horaires suffisent.
- **Méfiez-vous des chiffres « tout faits »** : si Claude affirme qu'une entreprise a « gagné 40 % de productivité », exigez la source et vérifiez-la.
- **Associez vos équipes** : une carte construite sans ceux qui réalisent les tâches sera inexacte et mal acceptée.

### J. Boîte à outils

**Fiche pratique 1.1 — Les quatre questions pour qualifier une tâche**

1. Est-ce surtout une tâche d'information (lire, écrire, structurer, comparer) ?
2. Les données sont-elles numériques et accessibles en respectant la confidentialité ?
3. Quelles sont les conséquences d'une erreur (faibles, moyennes, graves, critiques) ?
4. Un expert peut-il vérifier le résultat facilement ?

**Prompt réutilisable 1.3 — Analyse d'une tâche unique**

```text
Je suis [fonction] dans une entreprise minière [type de mine, substance, pays].
Je réalise la tâche suivante : [description], environ [fréquence et durée].
Les données utilisées sont : [documents, fichiers].
Le résultat est transmis à : [destinataire] pour [usage].

Analyse comment un assistant d'IA pourrait m'aider sur cette tâche :
étapes assistables, étapes à garder sous contrôle humain, risques, contrôles qualité
à prévoir, et un premier prompt que je pourrais tester. Sois concret et prudent.
```

**Check-list 1.1 — Démarrer sans risque**

- [ ] J'ai lu la charte IA de mon entreprise (ou j'ai demandé s'il en existe une).
- [ ] Je connais le niveau de confidentialité des documents que je compte utiliser.
- [ ] J'ai choisi un premier cas d'usage à faible risque et facile à vérifier.
- [ ] J'ai noté le temps actuel de la tâche pour pouvoir comparer.
- [ ] Je sais qui relira et validera les résultats.

### K. Quiz

1. **(QCM)** Selon l'USGS, quelle part approximative de la production minière mondiale de cobalt la RDC représentait-elle en 2025 ? a) 25 % ; b) 50 % ; c) 73 % ; d) 95 %.
2. **(Vrai ou faux)** L'IA générative est surtout utile pour piloter directement les équipements de la mine.
3. **(QCM)** Laquelle de ces tâches relève de l'IA prédictive plutôt que de l'IA générative ? a) Rédiger un rapport d'incident ; b) Prédire la panne d'un camion à partir de ses vibrations ; c) Résumer une étude d'impact ; d) Traduire un contrat.
4. **(Compréhension)** Citez trois familles de documents produits pendant la phase d'exploitation d'une mine.
5. **(Vrai ou faux)** Pour identifier les usages de Claude dans un service, il est préférable de partir de la liste des fonctionnalités de l'outil.
6. **(Mise en situation)** Un collègue propose de demander à Claude de « décider si le chantier doit être arrêté » lorsque la pluie dépasse un certain seuil. Que lui répondez-vous ?
7. **(QCM)** Quelle question n'appartient pas aux « quatre questions » pour qualifier une tâche ? a) La tâche est-elle surtout informationnelle ? b) Les données sont-elles numériques ? c) La tâche est-elle appréciée par l'équipe ? d) Le résultat est-il facile à vérifier ?
8. **(Analyse critique)** Claude vous indique qu'« une étude a démontré une réduction de 50 % du temps de rédaction des rapports miniers ». Quelle est la bonne réaction ?
9. **(Application)** Classez dans la matrice intérêt / risque la tâche « répondre automatiquement aux plaintes des communautés sans relecture ». Justifiez.
10. **(Compréhension)** Pourquoi la qualité des données de terrain reste-t-elle un enjeu majeur, même avec une IA performante ?

<div class="carnet" titre="Chapitre 1 — L'industrie minière à l'ère de l'intelligence artificielle"></div>
