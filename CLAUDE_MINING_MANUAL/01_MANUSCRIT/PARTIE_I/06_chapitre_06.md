## Chapitre 6 — Pourquoi l'expertise humaine demeure indispensable

### A. Mise en situation professionnelle

Albert Kalenga, superintendant forage-minage de MCC, reçoit un message d'un jeune ingénieur : « J'ai demandé à Claude d'optimiser la maille de forage du prochain tir sur le gradin 1380 ; il propose d'élargir la maille de 15 %, ce qui ferait économiser de l'explosif. On applique ? »

Albert répond par une question : « As-tu vérifié la fracturation observée sur le gradin, la distance aux installations, les vibrations mesurées au dernier tir près du village de Kasongo-Mbiyo, et l'avis du boutefeu ? » Le jeune ingénieur n'avait rien vérifié. La proposition de Claude n'était pas absurde en soi ; elle était simplement **incomplète** — car Claude ne connaissait ni le terrain, ni les mesures, ni les contraintes locales.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Expliquer** pourquoi l'expertise humaine reste indispensable dans un environnement minier assisté par l'IA.
2. **Identifier** les décisions qui ne peuvent jamais être déléguées à un système d'IA.
3. **Appliquer** la boucle « humain dans la boucle » à une tâche de votre métier.
4. **Répartir** les rôles entre Claude et l'expert sur un livrable donné.
5. **Prévenir** la perte de compétences liée à une dépendance excessive à l'outil.

### C. Comprendre avant de pratiquer

#### C.1. Ce que l'expert apporte et que Claude n'a pas

| L'expert apporte… | Pourquoi Claude ne peut pas le remplacer |
|---|---|
| La connaissance du **terrain** | Claude ne voit, n'entend, ne mesure rien par lui-même ; il ne connaît que ce qu'on lui fournit |
| Le **contexte local** | Historique du site, relations avec les communautés, pratiques de l'administration locale |
| Le **jugement** sur la pertinence et le risque | Claude ne porte pas les conséquences ; il ne « sait » pas ce qui compte le plus |
| La **responsabilité** professionnelle et juridique | Seule une personne qualifiée peut signer, attester, engager l'entreprise |
| L'**éthique** et la relation humaine | Annoncer une mauvaise nouvelle, conduire un dialogue communautaire, accompagner un collègue blessé |
| La **capacité à détecter** l'anomalie | Reconnaître qu'un résultat « ne colle pas » avec l'expérience du terrain |

#### C.2. La responsabilité ne se délègue pas

Plusieurs cadres du secteur minier reposent explicitement sur des personnes qualifiées et responsables :

- Les codes de déclaration des ressources et réserves, comme le code JORC, exigent que les estimations publiées soient fondées sur les travaux d'une **personne compétente**, membre d'une organisation professionnelle reconnue et disposant d'une expérience pertinente [@JORC-2012].
- La Convention n° 176 de l'OIT sur la sécurité et la santé dans les mines fait peser sur l'employeur l'obligation d'évaluer et de maîtriser les risques, et reconnaît aux travailleurs des droits, dont celui de se retirer d'une situation de danger grave [@ILO-C176]. Le recueil de directives pratiques de l'OIT sur les mines à ciel ouvert détaille ces responsabilités [@ILO-OPENCAST].
- La gestion des **contrôles critiques** promue par l'ICMM repose sur l'identification, la vérification et la responsabilité clairement attribuée des contrôles qui préviennent les événements graves [@ICMM-CCM].

Un outil d'IA peut **aider** ces personnes à préparer, documenter et vérifier leur travail. Il ne peut pas **être** ces personnes.

#### C.3. Les décisions jamais déléguées

::: attention
**Décisions hors du champ de délégation à l'IA (règle de l'ouvrage et de la charte de MCC) :**

- conception, validation et autorisation des **tirs** ; manipulation et gestion des **explosifs** ;
- décisions relatives à la **stabilité des ouvrages** : talus de fosse, verses, digues et parcs à résidus, galeries souterraines ;
- conduite des **interventions d'urgence** et des évacuations ;
- autorisation des **travaux dangereux** (consignation, espaces confinés, travail en hauteur) ;
- **décisions individuelles** engageant la carrière ou la santé d'une personne (sanction, aptitude médicale, licenciement) ;
- **attestations et signatures** réglementaires (déclarations de ressources, rapports réglementaires, états financiers certifiés).

Claude peut aider à **documenter**, **préparer**, **relire** ou **former** sur ces sujets. Il ne décide pas.
:::

#### C.4. La boucle « humain dans la boucle »

L'expression **humain dans la boucle** (*human in the loop*) désigne une organisation du travail dans laquelle un humain intervient à des étapes définies d'un processus assisté par l'IA : pour cadrer la tâche, vérifier les résultats, corriger et valider.

![Figure 6.1 — La boucle « humain dans la boucle ». Les étapes de cadrage, de vérification et de validation restent humaines ; Claude intervient dans la production et la correction. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig06_1_humain_boucle.png){width=78%}

Le cadre de gestion des risques de l'IA du NIST insiste lui aussi sur la définition claire des rôles et responsabilités humains dans l'utilisation des systèmes d'IA, au titre de sa fonction de gouvernance [@NIST-RMF].

#### C.5. Une répartition des rôles

![Figure 6.2 — Qui fait quoi ? Claude excelle dans la structuration et la production ; l'expert reste indispensable pour le jugement, la vérification et la responsabilité ; ensemble, ils produisent plus vite des livrables plus complets. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig06_2_partage_roles.png){width=100%}

#### C.6. Le risque de déqualification

L'usage intensif d'un assistant peut **éroder les compétences** : un jeune professionnel qui ne rédige jamais seul un rapport d'incident aura du mal à juger la qualité d'un rapport produit par Claude. Or c'est précisément ce jugement qui rend l'outil sûr.

::: terrain
À MCC, la charte IA prévoit que les **nouveaux arrivants** rédigent eux-mêmes leurs trois premiers rapports de chaque type, corrigés par un tuteur, avant d'utiliser Claude pour ce type de document. L'objectif : savoir faire avant de faire faire.
:::

### D. Démonstration guidée — Reprendre la proposition de maille de forage

Albert reprend la situation avec le jeune ingénieur, en appliquant la boucle.

1. **Cadrer** : la question n'est pas « optimise la maille », mais « aide-moi à préparer l'analyse d'une modification de maille, que je soumettrai au superintendant et au boutefeu ».
2. **Produire** : Claude liste les paramètres à considérer (fracturation, hauteur de gradin, diamètre, explosif, granulométrie visée, vibrations et projections, distance aux enjeux, résultats des tirs précédents) et propose un tableau de comparaison des options **à compléter avec les données du site**.
3. **Vérifier** : l'ingénieur complète le tableau avec les mesures réelles (vibrations du dernier tir, observations du gradin). Il constate que les vibrations mesurées près du village étaient déjà proches du seuil interne.
4. **Corriger** : il demande à Claude d'ajouter à l'analyse les risques pour les riverains et les mesures de suivi.
5. **Valider** : la décision appartient au superintendant et au boutefeu, conformément aux procédures de tir. Ils décident de ne pas élargir la maille sur ce secteur, mais de tester l'option sur un gradin éloigné, avec mesures de vibrations.

Claude a été utile : il a structuré l'analyse et évité des oublis. Il n'a pas décidé.

### E. Prompts commentés

**Prompt 6.1 — Préparer une analyse sans déléguer la décision**

```text
Je suis ingénieur forage-minage dans une mine de cuivre à ciel ouvert.
Je dois préparer, pour mon superintendant et le boutefeu, l'analyse d'une éventuelle
modification de la maille de forage sur un gradin. La décision leur appartient.

Aide-moi à :
1. lister les paramètres techniques et les contraintes à examiner ;
2. construire un tableau de comparaison « maille actuelle / maille proposée »
   avec des cases vides à compléter par les données du site ;
3. identifier les risques (sécurité, vibrations, projections, riverains, granulométrie) ;
4. lister les données à collecter avant toute décision.
Ne recommande pas de valeur de maille et ne te prononce pas sur la décision.
```

*Commentaire.* La consigne finale empêche Claude de franchir la frontière entre aide à l'analyse et décision. Le prompt positionne explicitement les décideurs humains.

**Prompt 6.2 — Contre-expertise d'un raisonnement**

```text
Voici mon raisonnement et ma conclusion provisoire : [texte].
Joue le rôle d'un relecteur expérimenté et sceptique. Identifie :
- les hypothèses non vérifiées ;
- les données manquantes ;
- les risques que je n'ai pas considérés ;
- les questions qu'un auditeur poserait.
Ne réécris pas ma conclusion ; aide-moi à la mettre à l'épreuve.
```

*Commentaire.* Ici, Claude renforce le jugement de l'expert au lieu de s'y substituer : c'est l'un des usages les plus précieux et les moins risqués.

### F. Exercices pratiques

**Exercice 6.1 (guidé) — Les lignes rouges de votre métier**

Listez cinq décisions de votre métier qui ne doivent jamais être déléguées à une IA. Pour chacune, indiquez ce que Claude peut néanmoins faire pour aider (préparer, documenter, relire, former).

**Exercice 6.2 (guidé) — Appliquer la boucle**

Choisissez une tâche de votre métier (par exemple : rédiger un rapport mensuel). Décrivez les cinq étapes de la boucle : ce que fait l'humain, ce que fait Claude, le contrôle prévu à chaque étape et la personne qui valide.

**Exercice 6.3 (autonome) — Le plan anti-déqualification**

Pour votre équipe, proposez trois règles qui garantissent que les compétences de base sont maintenues malgré l'usage de Claude.

### G. Livrable professionnel

**Fiche RACI d'un processus assisté par Claude** (Responsable, Approbateur, Consulté, Informé) — exemple pour le rapport mensuel HSE de MCC :

| Étape | Claude | Technicien HSE | Responsable HSE | Directeur des opérations |
|---|---|---|---|---|
| Collecte des données | — | R | A | — |
| Calcul des indicateurs | Assiste (code) | R | A | — |
| Commentaire des tendances | Premier jet | R | A | I |
| Identification des actions | Suggestions | C | R/A | C |
| Validation et diffusion | — | — | R | A |

### H. Vérification des résultats

::: controle
- Pour chaque livrable assisté par Claude, une personne nommée est responsable de la validation.
- Les décisions listées comme « jamais déléguées » n'apparaissent dans aucun processus automatisé.
- Les données de terrain utilisées dans l'analyse ont été collectées et contrôlées par des humains.
- La trace de la validation (nom, date, version) est conservée.
:::

::: setrompe
Interrogé sur la stabilité d'un talus à partir d'une simple photographie, un assistant d'IA peut produire une appréciation rassurante et bien argumentée. Aucune photographie ne remplace l'inspection d'un géotechnicien, les mesures d'auscultation (prismes, piézomètres, radars) et les analyses de stabilité. **Ne demandez pas** à Claude d'évaluer la stabilité d'un ouvrage : demandez-lui de vous aider à préparer la liste des observations à faire ou à rédiger le compte rendu d'inspection.
:::

### I. Limites et précautions

- La boucle humaine n'a de valeur que si la vérification est **réelle** : une validation « au clic », sans relecture, est une illusion de contrôle.
- La pression du temps pousse à réduire les contrôles : prévoyez-les dans les processus, pas seulement dans les bonnes intentions.
- Le partage des rôles doit être formalisé dans les procédures et connu de tous, y compris des sous-traitants.

### J. Boîte à outils

**Les trois questions avant de valider un livrable assisté**

1. Puis-je justifier chaque fait et chaque chiffre par une source que j'ai vérifiée ?
2. Le livrable tient-il compte de ce que je sais du terrain et que Claude ignore ?
3. Suis-je prêt à signer ce document comme s'il était entièrement de ma main ?

**Prompt réutilisable 6.3 — Délimiter le rôle de Claude**

```text
Ton rôle dans cette tâche est limité à : [préparer / structurer / relire / proposer des options].
La décision finale appartient à [fonction]. Ne formule aucune recommandation
de décision et signale toute question qui nécessite un avis d'expert ou une mesure de terrain.
```

### K. Quiz

1. **(Vrai ou faux)** Un système d'IA peut être désigné comme personne compétente au sens du code JORC.
2. **(QCM)** Lequel de ces sujets est hors du champ de délégation à l'IA ? a) la mise en forme d'un rapport ; b) la validation d'un plan de tir ; c) la traduction d'un courrier ; d) la préparation d'un quiz de formation.
3. **(Compréhension)** Que signifie « humain dans la boucle » ?
4. **(Mise en situation)** Un collègue valide les rapports de Claude sans les lire « parce qu'ils sont toujours bons ». Quel est le risque ?
5. **(QCM)** Quelle organisation promeut la gestion des contrôles critiques pour prévenir les événements graves ? a) ICMM ; b) FIFA ; c) OPEP ; d) UIT.
6. **(Application)** Citez deux manières dont Claude peut aider un responsable géotechnique sans évaluer lui-même la stabilité d'une digue.
7. **(Vrai ou faux)** La Convention n° 176 de l'OIT reconnaît le droit des travailleurs de se retirer d'une situation de danger grave.
8. **(Analyse critique)** Pourquoi le risque de déqualification menace-t-il, à terme, la sécurité de l'utilisation de l'IA elle-même ?
9. **(Compréhension)** Dans la boucle de la figure 6.1, quelles étapes sont humaines ?
10. **(Application)** Rédigez la phrase qui délimite le rôle de Claude dans un prompt de préparation d'une enquête d'incident.

<div class="carnet" titre="Chapitre 6 — Pourquoi l'expertise humaine demeure indispensable"></div>
