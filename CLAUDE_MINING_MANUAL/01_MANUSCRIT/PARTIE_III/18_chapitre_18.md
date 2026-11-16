## Chapitre 18 — Claude appliqué à l'échantillonnage, aux ressources et aux réserves minérales

### A. Mise en situation professionnelle

La mise à jour annuelle des ressources et réserves de MCC doit être publiée dans six semaines. Patrick Ilunga, géologue principal et « personne compétente » pour les ressources, découvre que la base de données de sondages contient des anomalies : une teneur en cuivre de 112 %, une valeur de cobalt dix fois supérieure aux valeurs voisines, un échantillon dupliqué, des intervalles qui se chevauchent. Le contrôle qualité des analyses (QA/QC) signale aussi un standard hors tolérance et un blanc contaminé. Avant toute estimation, il faut nettoyer, documenter et expliquer. Le rapport final devra respecter un code de déclaration reconnu, et c'est Patrick qui le signera.

![Figure 18.1 — Caisses de carottes de sondage rangées en carothèque. Titre original : « Drill core boxes Onkalo 1 ». Auteur : kallerna. Source : Wikimedia Commons, [https://commons.wikimedia.org/wiki/File:Drill_core_boxes_Onkalo_1.jpg](https://commons.wikimedia.org/wiki/File:Drill_core_boxes_Onkalo_1.jpg) (consulté le 16/11/2026). Licence : [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr) ; image redimensionnée pour l'édition. Photographie d'illustration, sans lien avec l'entreprise fictive MCC.](02_ILLUSTRATIONS/PHOTOGRAPHIES/photo_carottes_sondage.jpg){width=78%}

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Expliquer** les catégories de ressources et de réserves et le rôle de la personne compétente.
2. **Faire profiler** une base d'échantillonnage pour détecter les anomalies.
3. **Analyser** des données de contrôle qualité (standards, blancs, duplicatas) avec Claude.
4. **Vérifier** la cohérence interne d'un rapport de ressources et sa complétude au regard d'un code de déclaration.
5. **Rédiger** des sections méthodologiques claires et traçables.

### C. Comprendre avant de pratiquer — Profil du métier

#### C.1. Ressources, réserves et personne compétente

Les codes de déclaration — le code JORC en Australasie, et plus largement les codes alignés sur le gabarit international du CRIRSCO — distinguent [@JORC-2012; @CRIRSCO] :

- les **ressources minérales**, classées par niveau croissant de confiance géologique en **présumées**, **indiquées** et **mesurées** ;
- les **réserves de minerai** (ou réserves minérales), partie économiquement exploitable des ressources indiquées et mesurées après prise en compte des **facteurs modificateurs** (exploitation, métallurgie, économie, marché, juridique, environnement, social, gouvernance), classées en **probables** et **prouvées**.

Les déclarations publiques doivent être fondées sur les travaux d'une **personne compétente**, et le code JORC prévoit une liste de critères à documenter (sa « Table 1 ») couvrant l'échantillonnage, les données, l'estimation et les facteurs modificateurs [@JORC-2012].

*Tableau 18.1 — Profil des métiers « données géologiques et ressources ».*

| Dimension | Contenu |
|---|---|
| Responsabilités | Qualité des données, protocoles d'échantillonnage, QA/QC, estimation et classification, déclaration |
| Tâches quotidiennes | Validation de la base, suivi des laboratoires, contrôle des standards, préparation des données pour l'estimation, rédaction |
| Difficultés | Données historiques hétérogènes ; anomalies ; traçabilité des corrections ; rapports très longs et normés |
| Documents | Protocoles, certificats d'analyse, rapports QA/QC, rapports de ressources, Table 1, audits externes |
| Données | Analyses, densités, collets, levés de déviation, résultats des standards, blancs et duplicatas |
| Livrables | Base validée, rapport QA/QC, rapport de ressources et réserves, déclarations publiques |
| Assistables par Claude | Profilage et détection d'anomalies (par code) ; synthèse QA/QC ; contrôle de cohérence texte-tableaux ; vérification de complétude ; rédaction méthodologique |
| Limites | Estimation géostatistique (logiciels spécialisés), classification, jugement de la personne compétente, signature |

::: attention
La classification des ressources et la déclaration publique engagent la responsabilité professionnelle de la personne compétente — et, pour une société cotée, l'entreprise vis-à-vis des marchés. Claude ne classe pas, ne valide pas et ne signe pas.
:::

### D. Démonstration guidée — Cas d'usage

#### Cas d'usage 18.1 — Profiler et nettoyer la base d'échantillonnage

**1. Problème.** La base `MCC_sondages_analyses.csv` comporte des anomalies qui fausseraient l'estimation.

**2. Méthode habituelle.** Requêtes manuelles dans le logiciel de gestion de données, contrôles visuels ; anomalies parfois découvertes tardivement, pendant l'estimation.

**3. Contribution de Claude.** Profil complet par exécution de code ; tests systématiques (valeurs impossibles, aberrantes, manquantes, doublons, chevauchements, cohérence avec les collets) ; liste d'anomalies traçable ; graphiques.

**4. Données.** Fichiers d'analyses et de collets (fictifs, fournis) ; règles de validation de MCC.

**5. Procédure.** (a) Profil ; (b) tests de validation ; (c) revue humaine de chaque anomalie ; (d) correction **dans la base source** par le gestionnaire de données, avec justification ; (e) journal des corrections.

**6. Prompt.**

```text
Fichiers joints : MCC_sondages_analyses.csv et MCC_sondages_collets.csv
(séparateur ;, ligne 1 = bandeau à ignorer).

Avec l'exécution de code, applique les tests de validation suivants et liste chaque anomalie
(sondage, échantillon, valeur, test échoué) :
1. Cu_pct hors de [0 ; 60] ou Co_pct hors de [0 ; 5] (valeurs physiquement suspectes).
2. Valeurs manquantes.
3. Échantillons en double (même identifiant).
4. Intervalles qui se chevauchent ou laissent un vide dans un même sondage.
5. Profondeur maximale analysée supérieure à la profondeur du collet.
6. Valeurs aberrantes statistiques (au-delà de 4 écarts-types de la moyenne de la lithologie).
Produis aussi un histogramme des teneurs en Cu et un nuage Cu-Co.
Ne corrige rien : le tableau d'anomalies sera revu par le géologue.
Affiche le nombre total d'échantillons testés.
```

**7. Échanges successifs.** « Pour l'échantillon à 112 % de Cu, quelles hypothèses d'erreur sont plausibles (virgule, unité, transcription) ? Comment les vérifier sur le certificat d'analyse ? » ; « Rédige l'entrée du journal des corrections pour chaque anomalie, une fois ma décision indiquée. »

**8. Exemple de résultat.** Claude retrouve les anomalies insérées dans le jeu d'exercice : S10200 (Cu = 112 %), S10038 (Co ×10), S10053 (Cu manquant), S10081 (doublon), chevauchement sur MBN-002 (voir `ANOMALIES_ATTENDUES.md`).

![Figure 18.2 — Distribution des teneurs en cuivre et relation Cu-Co sur la base d'échantillonnage (fictive). Le graphique fait apparaître une valeur de cobalt aberrante ; la valeur de 112 % Cu, impossible, a été exclue. Graphique réalisé pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig18_1_teneurs_sondages.png){width=100%}

**9. Contrôle qualité.** Le géologue contrôle chaque anomalie sur le certificat d'analyse original ; il vérifie que le nombre d'échantillons testés correspond à la base.

**10. Erreurs possibles.** Seuils inadaptés (par exemple un seuil Co trop bas qui signale de vrais hauts teneurs) ; faux positifs de chevauchement dus à des arrondis.

**11. Limites.** Claude détecte des **incohérences de données**, pas des erreurs d'échantillonnage physique (contamination au forage, mauvaise récupération de carotte) : celles-ci relèvent des contrôles de terrain.

**12. Livrable.** Rapport de validation de la base : liste des anomalies, décisions, corrections, journal signé du gestionnaire de données.

#### Cas d'usage 18.2 — Synthèse QA/QC

**1. Problème.** Le rapport annuel doit démontrer la qualité des analyses : résultats des **matériaux de référence certifiés** (standards), des **blancs** et des **duplicatas**.

**2. Méthode habituelle.** Graphiques de contrôle dans un tableur, commentaires rédigés manuellement.

**3. Contribution de Claude.** Calcul des écarts normalisés, détection des valeurs hors tolérance, graphiques, rédaction du commentaire QA/QC.

**4. Données.** `MCC_qaqc_standards_blancs.csv` ; tolérances de l'exercice (± 3 écarts-types ; blancs < 0,05 % Cu).

**5–6. Procédure et prompt.**

```text
Fichier joint : MCC_qaqc_standards_blancs.csv.
Avec l'exécution de code :
1. Pour chaque standard certifié, calcule l'écart normalisé
   (mesuré − certifié) / (0,025 × certifié) et signale |écart| > 3.
2. Pour les blancs, signale toute valeur > 0,05 % Cu.
3. Produis une carte de contrôle (écarts normalisés) et un graphique des blancs.
4. Pour chaque anomalie, indique le lot d'analyses concerné.
5. Rédige un commentaire de 150 mots pour le rapport QA/QC, factuel, sans conclure
   sur l'acceptation ou le rejet des lots (décision du géologue).
```

**7. Échanges.** « Quels échantillons de production ont été analysés dans les lots LOT-04 et LOT-06 ? » (jointure avec la base) ; « Propose le texte de la demande de réanalyse au laboratoire. »

**8. Exemple de résultat.** Le standard Q018 (CRM-B, valeur certifiée 0,85 % Cu) est mesuré à 0,952 % Cu, soit un écart normalisé d'environ +4,8 : hors tolérance. Le blanc Q030 présente 0,15 % Cu : contamination possible. Les deux lots concernés (LOT-04, LOT-06) sont signalés pour décision.

![Figure 18.3 — Contrôle qualité des analyses : écarts normalisés des standards certifiés et teneurs des blancs (données fictives). Graphique réalisé pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig18_2_carte_controle_qaqc.png){width=100%}

**9. Contrôle.** Recalcul manuel des deux anomalies ; vérification des tolérances utilisées (celles du protocole du laboratoire et de MCC, pas des valeurs « par défaut »).

**10. Erreurs possibles.** Tolérances inventées si non fournies ; confusion entre standards ; blancs mal identifiés (une erreur de ce type a d'ailleurs été détectée et corrigée dans les données d'exercice pendant la préparation de cet ouvrage).

**11. Limites.** La décision d'accepter ou de rejeter un lot, et de faire réanalyser, appartient au géologue responsable.

**12. Livrable.** Section QA/QC du rapport annuel avec graphiques, tableau des anomalies et décisions.

#### Cas d'usage 18.3 — Contrôle de cohérence et de complétude d'un rapport de ressources (condensé)

Claude compare systématiquement les tableaux de ressources et réserves, le résumé, le texte et les annexes (tonnages, teneurs, métal contenu, catégories, coupure, date d'effet), recalcule le métal contenu (tonnage × teneur) et signale toute incohérence avec citation et page. Il vérifie ensuite, à partir de la liste de critères fournie par l'utilisateur (par exemple la Table 1 du code applicable), les rubriques absentes ou insuffisamment documentées. Exemple : dans le scénario, 51 Mt × 2,36 % Cu = 1,20 Mt de cuivre contenu ; si le résumé annonce 1,25 Mt, l'écart est signalé. **La personne compétente reste seule juge** de la complétude et de la conformité.

#### Cas d'usage 18.4 — Rédiger la section « échantillonnage et analyses » (condensé)

À partir du protocole interne, des fiches du laboratoire et de la synthèse QA/QC, Claude rédige une section méthodologique (type de sondage, diamètre, longueur des échantillons, préparation, méthode analytique, programme QA/QC, résultats), en signalant entre crochets les informations manquantes. Le géologue complète et valide.

### E. Prompts commentés

**Prompt 18.1 — Recalcul et cohérence d'un tableau de ressources**

```text
Tableau des ressources (extrait du projet de rapport) : <tableau> … </tableau>
Avec l'exécution de code : recalcule le métal contenu (Mt × teneur) par catégorie et le total,
vérifie que les totaux sont cohérents (tonnage total = somme ; teneur totale = moyenne pondérée),
et liste les écarts supérieurs à 0,5 %. N'arrondis qu'à la fin.
```

*Commentaire.* L'instruction « teneur totale = moyenne pondérée » évite l'erreur classique de la moyenne simple. Avec les ressources du scénario (18 Mt à 2,9 %, 42 Mt à 2,4 %, 25 Mt à 2,0 %), la teneur moyenne pondérée est de 2,39 % Cu, alors que la moyenne simple donnerait 2,43 %.

### F. Exercices pratiques

**Exercice 18.1 (guidé).** Réalisez le cas 18.1 avec les fichiers d'exercice. Comparez la liste d'anomalies avec `ANOMALIES_ATTENDUES.md`. Combien en avez-vous trouvé ? Lesquelles nécessitent un retour au certificat d'analyse ?

**Exercice 18.2 (guidé).** Réalisez le cas 18.2. Recalculez à la main l'écart normalisé de Q018.

**Exercice 18.3 (autonome).** Avec les tableaux de ressources et de réserves du scénario (fiche MCC), calculez le métal contenu (Cu et Co) par catégorie et rédigez un paragraphe de résumé. Vérifiez que la teneur totale des réserves (2,36 % Cu) est cohérente avec les catégories.

### G. Livrable professionnel

**Dossier de qualité des données** : rapport de validation de la base, journal des corrections, section QA/QC avec graphiques, contrôle de cohérence du projet de rapport de ressources — prêt pour la revue de la personne compétente.

### H. Vérification des résultats

::: controle
- Chaque anomalie a été vérifiée sur le document source (certificat, journal de sondage).
- Les corrections ont été faites dans la base source, pas dans un fichier de travail.
- Les tolérances QA/QC proviennent du protocole officiel.
- Tous les totaux et moyennes pondérées ont été recalculés par programme.
- Aucune classification n'a été proposée ou modifiée par Claude.
:::

::: setrompe
Claude « corrige » spontanément la teneur de 112 % en 1,12 % dans un tableau récapitulatif, en pensant bien faire. La correction est peut-être juste… ou pas (la vraie valeur pourrait être 11,2 % ou 0,112 %). **Contre-mesure** : interdire toute correction et exiger le retour au certificat d'analyse.
:::

### I. Limites et précautions

- L'estimation des ressources relève de méthodes géostatistiques et de logiciels spécialisés, mis en œuvre et validés par des spécialistes.
- Les informations de ressources et réserves sont sensibles (marchés, négociations, fiscalité).
- Un rapport « complet » sur le papier n'est pas pour autant un rapport « juste » : la complétude documentaire ne garantit pas la qualité technique.

### J. Boîte à outils

- Prompt du cas 18.1 (validation de base) ; prompt du cas 18.2 (QA/QC) ; prompt 18.1 (cohérence des tableaux).
- Liste des tests de validation d'une base d'échantillonnage (cas 18.1, points 1 à 6).
- Rappel : métal contenu = tonnage × teneur ; teneur d'un ensemble = moyenne pondérée par le tonnage.

### K. Quiz

1. **(QCM)** Dans l'ordre de confiance géologique croissante, les ressources sont : a) mesurées, indiquées, présumées ; b) présumées, indiquées, mesurées ; c) probables, prouvées ; d) possibles, probables.
2. **(Vrai ou faux)** Des réserves peuvent être déclarées à partir de ressources présumées.
3. **(Compréhension)** Que sont les « facteurs modificateurs » ?
4. **(Calcul)** Quel est le cuivre contenu dans les réserves prouvées du scénario (16 Mt à 2,7 % Cu) ?
5. **(Calcul)** Recalculez l'écart normalisé de Q018 (certifié 0,85 ; mesuré 0,952 ; écart-type = 2,5 % de la valeur certifiée).
6. **(Mise en situation)** Claude a corrigé une teneur dans un tableau sans vous le dire. Que faites-vous ?
7. **(QCM)** Qui décide d'accepter ou de rejeter un lot d'analyses ? a) Claude ; b) le laboratoire seul ; c) le géologue responsable selon le protocole ; d) le service achats.
8. **(Analyse critique)** Pourquoi un blanc contaminé est-il un signal important ?
9. **(Vrai ou faux)** La moyenne simple des teneurs de trois catégories de ressources donne la teneur totale.
10. **(Application)** Rédigez la règle qui interdit à Claude de corriger une valeur de la base.

<div class="carnet" titre="Chapitre 18 — Claude appliqué à l'échantillonnage, aux ressources et aux réserves minérales"></div>
