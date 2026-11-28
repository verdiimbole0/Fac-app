\newpage

\sommaire

## Avant-propos {.unnumbered}

### Pourquoi ce manuel ? {.unnumbered}

Dans une mine, l'information est partout : journaux de sondage, rapports de tir, bilans métallurgiques, ordres de travail, déclarations d'incident, registres de plaintes, contrats, déclarations fiscales, rapports de durabilité. Les professionnels du secteur passent une part considérable de leur temps à lire, rédiger, contrôler, comparer et transmettre ces documents. C'est précisément sur ce terrain que l'intelligence artificielle générative, et Claude en particulier, peut apporter une aide concrète.

Encore faut-il savoir s'en servir. Poser une question à Claude est à la portée de tous. L'intégrer intelligemment dans une méthode de travail, contrôler ce qu'il produit, protéger les informations de l'entreprise et créer une valeur professionnelle mesurable demandent une véritable compétence. Ce livre a été conçu pour vous aider à acquérir cette compétence.

> « On ne maîtrise pas l'intelligence artificielle simplement parce qu'on sait lui poser des questions. On la maîtrise lorsqu'on est capable de l'intégrer intelligemment dans ses méthodes de travail, d'évaluer ses résultats et de créer de la valeur professionnelle avec elle. »

### À qui s'adresse-t-il ? {.unnumbered}

Ce manuel s'adresse à tous les professionnels de l'industrie minière, quel que soit leur niveau en informatique : géologues et géoscientifiques, ingénieurs des mines, de planification et de production, techniciens, métallurgistes, responsables de maintenance, responsables HSE, spécialistes de l'environnement, responsables des relations communautaires, acheteurs et logisticiens, comptables, financiers et fiscalistes, auditeurs, juristes et responsables conformité, responsables des ressources humaines, managers et directeurs, consultants, ainsi qu'aux étudiants des filières minières, techniques, économiques et financières.

**Aucun prérequis en programmation n'est nécessaire.** Les quelques passages techniques (paramètres de l'API, Claude Code) sont signalés et peuvent être survolés par les lecteurs non techniciens.

### Comment est-il organisé ? {.unnumbered}

Le manuel suit une progression en six parties, réparties en trois tomes :

| Partie | Objectif | Chapitres | Tome |
|---|---|---|---|
| I. Comprendre l'IA et découvrir Claude | Acquérir les bases : ce qu'est un modèle de langage, ce que Claude sait faire et ne sait pas faire | 1 à 6 | 1 |
| II. Maîtriser Claude de A à Z | Prendre en main l'outil : modèles, paramètres, méthode CADRE, documents, recherche, projets, connecteurs | 7 à 16 | 1 |
| III. Claude dans les métiers miniers | Appliquer Claude, métier par métier, sur des cas d'usage réels et détaillés | 17 à 32 | 2 |
| IV. Construire des méthodes de travail | Analyser des données, produire des livrables, créer des assistants et des workflows | 33 à 36 | 3 |
| V. Éthique, sécurité et gouvernance | Protéger les données, maîtriser les risques, déployer une politique IA | 37 à 40 | 3 |
| VI. Ateliers, évaluation et projet final | S'entraîner, s'évaluer et concevoir son propre système de travail | 41 à 43 | 3 |

Les **annexes** (A à M) rassemblent les outils de référence : glossaire, bibliothèque de prompts, modèles de documents, check-lists, charte IA, classification des données, programme de 30 jours, grille d'évaluation, études de cas corrigées et bibliographie vérifiée. Le glossaire (Annexe A) et la bibliographie (Annexe I) figurent dans chaque tome ; les Annexes C, E et H se trouvent dans le tome 1 ; les Annexes B et D dans le tome 2 ; les Annexes F, G, J, K, L et M dans le tome 3.

### Comment chaque chapitre est-il construit ? {.unnumbered}

Chaque chapitre suit la même architecture pédagogique, pour que vous trouviez rapidement ce que vous cherchez :

1. **Mise en situation professionnelle** : un problème réel, tiré du quotidien d'une entreprise minière.
2. **Objectifs d'apprentissage** : ce que vous saurez faire à la fin du chapitre.
3. **Comprendre avant de pratiquer** : les notions, expliquées simplement.
4. **Démonstration guidée** : la méthode, étape par étape.
5. **Prompts commentés** : des instructions complètes, et pourquoi elles sont formulées ainsi.
6. **Exercices pratiques** : au moins un exercice guidé et un exercice autonome.
7. **Livrable professionnel** : le résultat que vous devez être capable de produire.
8. **Vérification des résultats** : comment contrôler ce que Claude produit.
9. **Limites et précautions** : les risques et les situations où Claude ne doit pas être utilisé seul.
10. **Boîte à outils** : prompts réutilisables, check-lists, fiches pratiques.
11. **Quiz** : pour vérifier vos acquis (corrigés expliqués à la fin de chaque partie).
12. **Mon carnet d'application et de réflexion** : vos pages personnelles.

### Les encadrés {.unnumbered}

Huit types d'encadrés jalonnent l'ouvrage :

::: retenir
Les idées essentielles à mémoriser.
:::

::: terrain
L'expérience des praticiens : astuces, raccourcis, bonnes habitudes.
:::

::: attention
Un risque à connaître avant d'agir.
:::

::: erreur
Les pièges dans lesquels tombent la plupart des débutants.
:::

::: application
Une mise en œuvre concrète dans un métier minier.
:::

::: defi
Un exercice court pour vous mettre à l'épreuve.
:::

::: setrompe
Un exemple réaliste d'erreur de Claude, et comment la détecter.
:::

::: controle
Les points de contrôle à vérifier avant de valider un résultat.
:::

### Les prompts {.unnumbered}

Les instructions à donner à Claude (les **prompts**) sont présentées dans des blocs gris, en police à chasse fixe, prêtes à être copiées et adaptées. Les éléments entre crochets, par exemple `[nom du sondage]`, sont à remplacer par vos propres informations.

```text
Exemple de prompt : remplacez les éléments entre [crochets] par vos informations.
```

### Le fil conducteur : Mbiyo Copper Cobalt SA {.unnumbered}

Pour que les exemples soient concrets et cohérents d'un chapitre à l'autre, l'ouvrage suit une entreprise **fictive** : **Mbiyo Copper Cobalt SA (MCC)**, qui exploite un gisement de cuivre et de cobalt dans le Copperbelt congolais. Vous retrouverez ses équipes, ses données et ses documents tout au long du livre. Les fichiers d'exercice correspondants sont fournis dans le dossier `03_EXERCICES_ET_DONNEES`.

![Figure 0.1. Plan schématique du site de Mbiyo Copper Cobalt SA. Les deux fosses à ciel ouvert, l'usine hydrométallurgique, le parc à résidus Kilima, la rivière Mbiyo et les trois villages riverains servent de repères à de nombreux exercices. Entreprise et site fictifs. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig01_2_plan_site_mcc.png){width=92%}

| Élément | Données du scénario (fictives) |
|---|---|
| Activité | Mine à ciel ouvert (fosses Mbiyo Nord et Mbiyo Sud), usine de lixiviation et d'électrolyse (SX-EW), précipitation du cobalt |
| Production | ≈ 50 000 t/an de cuivre cathode ; ≈ 4 500 t/an de cobalt contenu dans l'hydroxyde |
| Minerai traité | 2,4 Mt/an ; teneur moyenne des réserves : 2,36 % Cu et 0,27 % Co |
| Réserves | 51 Mt (prouvées + probables) ; durée de vie prévue jusqu'en 2043 |
| Effectif | 2 350 personnes, dont 900 sous-traitants |
| Cycle de vie | Exploration 2014-2018 ; études 2017-2019 ; construction 2020-2022 ; production depuis octobre 2022 ; fermeture prévue 2044-2048 |
| Communautés | Villages de Kasongo-Mbiyo, Lupanda et Mwinda (≈ 14 000 habitants) |
| Programme IA | « MCC-IA 2026 » : pilote de 40 utilisateurs, charte IA adoptée en mars 2026 |

Les personnages que vous croiserez, Patrick Ilunga (géologue principal), Sarah Mwamba (ingénieure planification), Grace Nsimba (responsable HSE), Thomas Kayembe (directeur financier), Kevin Mutombo (référent IA) et leurs collègues, sont eux aussi fictifs.

### Comment tirer le meilleur parti de ce livre ? {.unnumbered}

::: terrain
**Lisez avec Claude ouvert à côté de vous.** Ce manuel est un livre de pratique. Chaque démonstration gagne à être reproduite immédiatement, avec les fichiers d'exercice puis avec vos propres documents (dans le respect des règles de confidentialité de votre entreprise, voir chapitre 37).
:::

- **Débutant complet** : suivez l'ordre des chapitres. Les parties I et II sont indispensables avant la partie III.
- **Utilisateur occasionnel de Claude** : survolez la partie I, lisez attentivement les chapitres 9 à 14, puis allez directement aux chapitres de votre métier.
- **Manager ou responsable de déploiement** : lisez les chapitres 1, 5, 6, puis les parties IV et V, et l'Annexe F (charte IA).
- **Formateur** : chaque chapitre peut servir de module de formation de 2 à 4 heures ; les quiz, ateliers (chapitre 41) et la grille d'évaluation (Annexe K) facilitent l'organisation de sessions.

Le **programme d'apprentissage sur 30 jours** (Annexe J) propose un rythme réaliste d'environ 45 minutes par jour.

### Une note sur l'actualité de l'ouvrage {.unnumbered}

Les outils d'intelligence artificielle évoluent plus vite que les livres. Nous avons donc fait un choix : expliquer d'abord les **principes durables** (comment fonctionne un modèle de langage, comment formuler une instruction, comment vérifier un résultat, comment protéger les données), puis décrire les **fonctionnalités actuelles** en les datant. Lorsque l'interface ou la gamme de modèles changera, les principes resteront valables ; seuls les détails pratiques devront être actualisés dans la documentation officielle d'Anthropic [@ANT-MODELS; @ANT-HC-RELEASE].
