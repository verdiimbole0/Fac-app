## Chapitre 19. Claude appliqué à l'ingénierie et à la planification minière

### A. Mise en situation professionnelle

Sarah Mwamba, ingénieure planification de MCC, doit expliquer au comité de direction pourquoi le minerai traité au premier semestre 2026 est inférieur au budget, et proposer un plan de rattrapage pour le second semestre. Elle dispose des données journalières de production, du plan budgétaire, des rapports mensuels et des comptes rendus de réunions. Le logiciel de planification minière produit les plans ; mais l'analyse des écarts, la rédaction des hypothèses, la comparaison des scénarios et la préparation de la présentation lui prennent l'essentiel de son temps.

![Figure 19.1. Une grande mine de cuivre à ciel ouvert : les gradins, les rampes et le fond de fosse illustrent l'ampleur des choix de planification. Titre original : « Bingham Canyon Open Pit Copper Mine 2012-09-17 21-25-59 ». Auteur : Jet6581. Source : Wikimedia Commons, [https://commons.wikimedia.org/wiki/File:Bingham_Canyon_Open_Pit_Copper_Mine_2012-09-17_21-25-59.jpg](https://commons.wikimedia.org/wiki/File:Bingham_Canyon_Open_Pit_Copper_Mine_2012-09-17_21-25-59.jpg) (consulté le 16/11/2026). Licence : [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.fr) ; image redimensionnée pour l'édition. Photographie d'illustration, sans lien avec l'entreprise fictive MCC.](02_ILLUSTRATIONS/PHOTOGRAPHIES/photo_fosse_bingham_canyon.jpg){width=85%}

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Analyser** les écarts entre plan et réalisé à partir de données de production, avec calculs vérifiables.
2. **Documenter** les hypothèses d'un plan minier de façon claire et traçable.
3. **Comparer** des scénarios simples (tonnages, découverture, disponibilité) par calcul programmé.
4. **Contrôler** la cohérence d'une étude technique (hypothèses, unités, références croisées).
5. **Préparer** une présentation de plan pour une direction non spécialiste.

### C. Comprendre avant de pratiquer : Profil du métier

*Tableau 19.1. Profil de l'ingénieur de planification minière.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Plans à long, moyen et court terme ; séquencement ; dimensionnement de la flotte ; contribution aux études et aux réserves |
| Tâches quotidiennes | Mise à jour des modèles, plans hebdomadaires, suivi plan/réalisé, réunions avec la production, la géologie, la géotechnique, l'usine |
| Difficultés | Données multiples ; hypothèses changeantes ; justification des écarts ; communication aux non-spécialistes |
| Documents | Plans miniers, études (préliminaire, préfaisabilité, faisabilité), rapports mensuels, notes d'hypothèses, comptes rendus |
| Données | Modèle de blocs, réserves, productivité de la flotte, disponibilités, temps de cycle, découverture, contraintes géotechniques |
| Livrables | Plans, notes d'hypothèses, rapports plan/réalisé, scénarios, présentations |
| Assistables par Claude | Analyse plan/réalisé (code) ; rédaction des notes ; contrôle de cohérence des études ; calculs de scénarios simples ; présentations |
| Limites | Optimisation de fosse et ordonnancement (logiciels spécialisés) ; angles de talus et contraintes géotechniques (géotechniciens) ; décision sur le plan |

::: attention
Les angles de talus, la largeur des rampes et des banquettes et toute contrainte de stabilité sont fixés par les études géotechniques et validés par des spécialistes. Claude ne les propose pas, ne les modifie pas et ne les « optimise » pas.
:::

### D. Démonstration guidée : Cas d'usage

#### Cas d'usage 19.1. Analyse des écarts plan / réalisé du semestre

**1. Problème.** Le minerai traité au S1 2026 est inférieur au budget de 200 kt/mois ; la direction veut comprendre pourquoi et ce qui est rattrapable.

**2. Méthode habituelle.** Tableaux croisés manuels, graphiques, commentaires rédigés le dernier jour.

**3. Contribution de Claude.** Profil des données, agrégation mensuelle, décomposition des écarts (jours de forte pluie, arrêts de l'usine, teneur, récupération), graphiques, projet de commentaire.

**4. Données.** `MCC_production_journaliere_S1_2026.xlsx` ; budget mensuel (200 kt de minerai traité ; teneur 2,36 % ; récupération 88 %).

**5. Procédure.** Profil et anomalies → corrections validées → agrégation → décomposition → commentaire → présentation.

**6. Prompt.**

```text
[C] Je suis ingénieure planification chez MCC (mine Cu-Co à ciel ouvert). Je présente
lundi au comité de direction l'analyse des écarts du premier semestre 2026.
[A] Analyse les écarts entre le réalisé et le budget pour le minerai traité, la teneur,
la récupération et la production de cathode, mois par mois.
[D] Fichier joint MCC_production_journaliere_S1_2026.xlsx. Budget mensuel : 200 kt de
minerai traité ; teneur 2,36 % Cu ; récupération 88 % ; cathode = traité × teneur × récupération.
[R] Commence par le profil des données et signale les anomalies sans les corriger.
Calculs par exécution de code uniquement. Pour l'explication des écarts, utilise seulement
les variables du fichier (pluie, arrêts) et distingue corrélation et cause.
[E] Tableau mensuel (budget, réel, écart, %) ; graphique ; décomposition de l'écart de cathode
en effet tonnage, effet teneur, effet récupération ; commentaire de 200 mots ; 3 questions
à poser aux équipes.
```

**7. Échanges successifs.** Après le profil, Sarah indique ses décisions sur les anomalies (récupération de 121,4 % le 15/02 : à exclure ; journée du 11/04 manquante : à compléter par les données du système de l'usine ; cathode ×10 le 01/06 : corriger par division par 10 après vérification). Puis : « Montre la relation entre les jours de forte pluie et le minerai extrait » ; « Combien faudrait-il traiter par jour au S2 pour atteindre l'objectif annuel de 2,4 Mt ? »

**8. Exemple de résultat (fictif).**

![Figure 19.2. Minerai traité par mois au premier semestre 2026, comparé au budget de 200 kt. Les mois de saison des pluies sont pénalisés. Données fictives MCC. Graphique réalisé pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig19_2_minerai_traite_mensuel.png){width=88%}

Commentaire produit (extrait, à valider) : « Le minerai traité est inférieur au budget au premier semestre, principalement de janvier à avril. Ces mois coïncident avec une fréquence élevée de jours de forte pluie dans les données ; l'extraction y est en moyenne plus faible les jours de pluie. Cette association ne suffit pas à établir la cause : l'effet de l'état des rampes et de la disponibilité de la flotte doit être vérifié avec la production. »

**9. Contrôle qualité.** Totaux mensuels recalculés dans le tableur ; vérification que les anomalies ont été traitées selon les décisions de Sarah ; décomposition des écarts contrôlée (la somme des effets doit égaler l'écart total).

**10. Erreurs possibles.** Agrégation incluant la valeur aberrante ; confusion minerai extrait / minerai traité ; causalité affirmée à partir d'une simple corrélation.

**11. Limites.** Les causes opérationnelles réelles (état des rampes, organisation des postes) ne figurent pas dans le fichier ; elles relèvent des échanges avec la production.

**12. Livrable.** Note d'analyse plan/réalisé de 3 pages et 5 diapositives pour le comité, validées par Sarah.

#### Cas d'usage 19.2. Note d'hypothèses du plan trimestriel

**1. Problème.** Les hypothèses du plan (productivités, disponibilités, temps de cycle, découverture, teneurs) sont dispersées dans des fichiers et des courriels ; certaines ont changé sans être documentées.

**2. Méthode habituelle.** Note rédigée en fin de processus, souvent incomplète.

**3. Contribution de Claude.** Collecte structurée (à partir des documents fournis), tableau des hypothèses avec source et date, détection des incohérences, rédaction de la note.

**4. Données.** Comptes rendus, extraits du modèle de planification, courriels de validation.

**5–6. Procédure et prompt.**

```text
À partir des documents joints (comptes rendus, extraits de plan, courriels), établis
le tableau des hypothèses du plan T1 2027 : paramètre | valeur | unité | source (document, date) |
statut (validée / proposée / contradictoire).
Si un paramètre a plusieurs valeurs, liste-les toutes et marque « contradictoire ».
Puis rédige la note d'hypothèses (2 pages) en utilisant uniquement les valeurs « validées »,
et liste à la fin les paramètres à arbitrer.
```

**7. Échanges.** « Pour les paramètres contradictoires, prépare la question à poser à chaque responsable. »

**8. Exemple de résultat.** Tableau de 24 hypothèses, dont 3 contradictoires (disponibilité de la flotte : 85 % dans le plan, 81 % réalisé en mars ; rapport de découverture : 6,0 et 6,5) : à arbitrer par Sarah.

**9. Contrôle.** Chaque valeur « validée » est rattachée à un document de validation.

**10. Erreurs possibles.** Valeur ancienne prise pour la valeur courante ; unité confondue (t/h et t/poste).

**11. Limites.** Claude ne choisit pas entre deux valeurs contradictoires.

**12. Livrable.** Note d'hypothèses versionnée, annexée au plan.

#### Cas d'usage 19.3. Scénarios simples de rattrapage (condensé)

Par exécution de code, Claude calcule l'effet de quelques leviers sur la production du second semestre : disponibilité de la flotte (81 % → 85 %), nombre de jours de pluie, teneur d'alimentation, récupération. Il présente un tableau de scénarios avec les formules. Ces calculs simplifiés aident à **structurer la discussion** ; ils ne remplacent pas la replanification dans le logiciel minier, qui intègre les contraintes de séquence, de géotechnique et de flotte.

#### Cas d'usage 19.4. Revue de cohérence d'une étude technique (condensé)

Pour l'étude « Mbiyo Profond », Claude contrôle la cohérence entre chapitres : mêmes hypothèses de prix, de taux de change, de récupération et de coûts ; unités ; références à des tableaux et figures existants ; cohérence entre le résumé et le corps. Il produit un tableau d'incohérences (page, citation, nature). L'ingénieur responsable arbitre.

### E. Prompts commentés

**Prompt 19.1. Décomposition d'un écart de production**

```text
Avec l'exécution de code, décompose l'écart de production de cathode du mois [M]
entre budget et réel en trois effets successifs :
effet tonnage = (T_réel − T_budget) × teneur_budget × récupération_budget ;
effet teneur = T_réel × (teneur_réelle − teneur_budget) × récupération_budget ;
effet récupération = T_réel × teneur_réelle × (récup_réelle − récup_budget).
Vérifie que la somme des trois effets est égale à l'écart total et affiche le contrôle.
```

*Commentaire.* En fournissant la formule, vous évitez que Claude choisisse une méthode de décomposition différente de celle de votre entreprise ; le contrôle de somme rend le calcul auditable.

### F. Exercices pratiques

**Exercice 19.1 (guidé).** Réalisez le cas 19.1 avec le fichier d'exercice. Vérifiez à la main le total de minerai traité d'un mois.

**Exercice 19.2 (guidé).** Avec les données du rapport de mars (189 kt ; 2,41 % ; 87,9 % ; budget 200 kt ; 2,36 % ; 88 %), appliquez le prompt 19.1 et vérifiez que la somme des effets égale l'écart total.

**Exercice 19.3 (autonome).** Rédigez la note d'hypothèses d'un plan de votre site (ou du scénario MCC) selon le cas 19.2.

### G. Livrable professionnel

**Dossier de revue de planification** : analyse plan/réalisé, décomposition des écarts, note d'hypothèses, tableau de scénarios, présentation au comité.

### H. Vérification des résultats

::: controle
- Les anomalies de données ont été traitées par une décision humaine documentée.
- La somme des effets de la décomposition est égale à l'écart total.
- Les hypothèses utilisées sont rattachées à une source validée et datée.
- Aucune contrainte géotechnique n'a été proposée ou modifiée par Claude.
- Les affirmations de cause sont étayées par des faits vérifiés auprès de la production.
:::

::: setrompe
Claude calcule une « disponibilité moyenne de la flotte » en faisant la moyenne des pourcentages mensuels, alors que la méthode de MCC pondère par les heures calendaires. L'écart est faible mais réel. **Contre-mesure** : fournir la définition de l'indicateur, comme pour le taux de fréquence en HSE.
:::

### I. Limites et précautions

- Les décisions de plan relèvent de l'ingénieur et de la direction, avec les logiciels et méthodes de la profession.
- Les scénarios simplifiés ne doivent pas être présentés comme des plans.
- Les données de production et les plans peuvent être confidentiels ou sensibles.

### J. Boîte à outils

- Prompts des cas 19.1, 19.2 et prompt 19.1 (décomposition des écarts).
- Gabarit de tableau d'hypothèses : paramètre | valeur | unité | source | date | statut | responsable.
- Check-list « présentation au comité » : messages clés ; chiffres vérifiés ; causes distinguées des corrélations ; décisions demandées.

### K. Quiz

1. **(Vrai ou faux)** Claude peut optimiser l'angle des talus de la fosse pour réduire la découverture.
2. **(Calcul)** Pour 189 kt à 2,41 % et 87,9 % de récupération, quelle est la production théorique de cathode ?
3. **(Compréhension)** Pourquoi faut-il distinguer corrélation et cause dans l'analyse des jours de pluie ?
4. **(QCM)** Que faire lorsqu'un paramètre de plan a deux valeurs dans les documents ? a) prendre la plus récente sans le dire ; b) demander à Claude de choisir ; c) signaler « contradictoire » et faire arbitrer ; d) faire la moyenne.
5. **(Application)** Quel contrôle simple garantit la cohérence d'une décomposition d'écart en effets ?
6. **(Mise en situation)** La direction vous demande d'utiliser le tableau de scénarios de Claude comme plan officiel. Que répondez-vous ?
7. **(Vrai ou faux)** Une note d'hypothèses doit rattacher chaque valeur à une source et une date.
8. **(Compréhension)** Pourquoi fournir la définition des indicateurs à Claude ?
9. **(Calcul)** Pour atteindre 2,4 Mt en 2026 après un S1 à 1,14 Mt, combien faut-il traiter par jour au S2 (184 jours) ?
10. **(Analyse critique)** Quels risques présente une présentation au comité préparée par Claude et non relue ?

<div class="carnet" titre="Chapitre 19. Claude appliqué à l'ingénierie et à la planification minière"></div>
