## Chapitre 23 — Claude appliqué à l'hygiène, à la sécurité et à l'environnement au travail (HSE)

### A. Mise en situation professionnelle

Le 14 avril 2026, à 2 h 40, le camion CAM-07 glisse au freinage sur la rampe R3 de la fosse Mbiyo Nord et s'arrête contre le merlon de sécurité. Personne n'est blessé. Grace Nsimba, responsable HSE, dispose de la déclaration du conducteur, du rapport du superviseur et des observations de la maintenance. Elle doit transmettre un rapport préliminaire dans les 24 heures, lancer l'enquête, et — cette même semaine — finaliser le rapport HSE mensuel et préparer l'audit des contrôles critiques. Grace veut utiliser Claude pour gagner du temps sur l'écrit, mais une règle s'impose à elle : **aucune décision de sécurité ne sera déléguée**.

![Figure 23.1 — Accident type de la circulation minière : un camion de grande capacité a reculé sur un véhicule léger stationné. Photographie : NIOSH, « Haul truck backed over a parked vehicle », Wikimedia Commons, domaine public, https://commons.wikimedia.org/wiki/File:Haul_truck_backed_over_a_parked_vehicle.jpg (consulté le 16/11/2026). Photographie d'illustration, sans lien avec MCC.](02_ILLUSTRATIONS/PHOTOGRAPHIES/photo_niosh_camion_recul.jpg){width=72%}

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Rédiger** un rapport préliminaire d'incident à partir d'éléments bruts, sans invention ni conclusion prématurée.
2. **Produire** la synthèse mensuelle des indicateurs HSE avec des calculs conformes aux définitions de l'entreprise.
3. **Préparer** des supports de vérification des contrôles critiques.
4. **Concevoir** des causeries et des supports de formation à partir des incidents réels.
5. **Délimiter** strictement le rôle de Claude en matière de sécurité.

### C. Comprendre avant de pratiquer — Profil du métier

#### C.1. Le cadre

La Convention n° 176 de l'OIT impose à l'employeur d'évaluer et de maîtriser les risques et reconnaît aux travailleurs des droits, dont celui de se retirer d'une situation de danger grave [@ILO-C176] ; le recueil de directives de l'OIT sur les mines à ciel ouvert détaille les mesures pratiques, notamment pour la circulation des engins, les talus et les explosifs [@ILO-OPENCAST]. L'ICMM promeut la **gestion des contrôles critiques** : identifier, pour chaque événement indésirable majeur, les contrôles qui le préviennent ou en limitent les conséquences, définir leurs normes de performance, les vérifier et en rendre compte [@ICMM-CCM-2015; @ICMM-CCM].

*Tableau 23.1 — Profil de l'équipe HSE.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Prévention, conformité réglementaire, gestion des incidents, contrôles critiques, formation, culture sécurité, hygiène industrielle |
| Tâches quotidiennes | Inspections, causeries, analyses de risques, suivi des actions, enquêtes, reporting |
| Difficultés | Volume de déclarations ; qualité inégale des récits ; suivi des actions en retard ; nombreux sous-traitants ; reporting chronophage |
| Documents | Déclarations, rapports d'enquête, analyses de risques, permis de travail, procédures, rapports d'audit, statistiques |
| Données | Registre des incidents, heures travaillées, actions correctives, résultats d'inspections, mesures d'exposition |
| Livrables | Rapports d'incident, rapports mensuels, causeries, plans d'action, dossiers d'audit, supports de formation |
| Assistables par Claude | Mise en forme des déclarations ; premiers jets de rapports ; calcul des indicateurs (code) ; analyse de tendances ; causeries ; check-lists ; relecture d'analyses de risques |
| Limites | Classification de la gravité, détermination des causes, décisions d'arrêt ou de reprise, autorisations de travail, gestion des urgences |

::: attention
**Hors délégation, sans exception :** gestion des situations d'urgence et des évacuations ; autorisation des travaux dangereux ; décision d'arrêt ou de reprise d'une activité ; détermination finale des causes et des responsabilités ; classification réglementaire des accidents. Claude prépare, structure, relit — il ne décide pas.
:::

![Figure 23.2 — Rapport d'incident assisté : qui fait quoi ? Les étapes de déclaration, d'enquête et de validation restent humaines. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig23_3_workflow_incident.png){width=100%}

### D. Démonstration guidée — Cas d'usage

#### Cas d'usage 23.1 — Le rapport préliminaire de l'incident INC-2026-0412

**1. Problème.** Transmettre en 24 heures un rapport préliminaire factuel, complet et prudent.

**2. Méthode habituelle.** Rédaction sous pression, à partir de notes, avec un risque d'oublis et de jugements prématurés.

**3. Contribution de Claude.** Structuration des faits au format MCC, chronologie, identification des informations manquantes, liste des mesures immédiates déjà prises (selon les documents), questions pour l'enquête.

**4. Données.** `MCC_declarations_incident_INC-2026-0412` (déclaration du conducteur, rapport du superviseur, observations maintenance, informations manquantes). Le document ne contient pas de données nominatives autres que le superviseur ; le rapport sera anonymisé pour diffusion large.

**5. Procédure.** Joindre le document → prompt → relecture ligne à ligne → compléments → validation par Grace → transmission.

**6. Prompt.**

```text
[C] Je suis responsable HSE de MCC (mine Cu-Co à ciel ouvert). Je dois transmettre au directeur
des opérations, sous 24 heures, le rapport préliminaire de l'incident INC-2026-0412
(rampe R3, nuit du 14/04/2026).
[A] Rédige le rapport préliminaire.
[D] Document joint : éléments bruts (déclaration du conducteur, rapport du superviseur,
observations de la maintenance, informations manquantes).
[R] Uniquement les faits des documents ; aucune cause, aucune responsabilité, aucune
classification de gravité (décisions de l'équipe d'enquête et de la direction).
Toute information manquante : [à compléter]. Ton factuel, sans jugement. Aucun nom de conducteur.
[E] Rubriques MCC : 1. Identification ; 2. Description factuelle ; 3. Chronologie (tableau heure/fait/source) ;
4. Conséquences constatées ; 5. Mesures immédiates prises ; 6. Informations manquantes et questions
pour l'enquête ; 7. Prochaines étapes. Une page et demie maximum.
Termine par la liste de toutes les phrases qui ne sont pas directement issues des documents.
```

**7. Échanges successifs.** Grace demande : « Ajoute à la rubrique 6 les données du système de suivi embarqué à extraire et le témoignage à recueillir auprès du conducteur de la pelle PEL-02 » ; puis « Vérifie que chaque heure de la chronologie figure dans les documents. »

**8. Exemple de résultat (extrait).**

| Heure | Fait | Source |
|---|---|---|
| 23 h 30 (13/04) | Arrosage de la rampe effectué malgré la pluie annoncée | Rapport superviseur |
| ≈ 2 h 40 | Glissade du CAM-07 chargé au freinage avant le virage ; arrêt contre le merlon côté talus | Déclaration conducteur |
| 2 h 55 | Arrivée du superviseur ; merlon entamé sur ≈ 2 m | Rapport superviseur |
| 3 h 00 – 5 h 20 | Circulation arrêtée sur R3 | Rapport superviseur |
| 2 h 00 – 8 h 00 | Fuite constatée sur le flexible de freinage avant gauche | Observations maintenance |

Rubrique 6 (extrait) : hauteur réelle du merlon [à compléter] ; vitesse au moment du freinage (données embarquées) [à compléter] ; lien éventuel avec les interventions hydrauliques de mars (OT-25311, OT-25340) : à instruire par l'enquête.

**9. Contrôle qualité.** Chaque ligne relue contre les documents ; la liste finale « phrases non issues des documents » est examinée et purgée ; aucune cause suggérée.

**10. Erreurs possibles.** Formulation suggérant une cause (« en raison de la fuite… ») ; heure approximative présentée comme exacte ; oubli des mesures immédiates.

**11. Limites.** Le rapport préliminaire ne préjuge pas de l'enquête ; la classification et les déclarations réglementaires suivent la procédure officielle.

**12. Livrable.** Rapport préliminaire validé et signé par la responsable HSE, transmis dans le délai.

#### Cas d'usage 23.2 — La synthèse mensuelle des indicateurs HSE

**1. Problème.** Produire chaque mois les indicateurs (nombre d'événements par type et zone, taux de fréquence, actions en retard) et un commentaire de tendance.

**2. Méthode habituelle.** Tableur, calculs manuels, risque d'erreur de définition.

**3. Contribution de Claude.** Calculs par code selon les **définitions de l'entreprise**, graphiques, commentaire, liste des actions en retard.

**4. Données.** `MCC_incidents_HSE_2025_2026.csv` (160 événements du 4 janvier 2025 au 18 juin 2026), heures travaillées (fournies par les RH), définitions des indicateurs de MCC.

**5–6. Procédure et prompt.**

```text
Fichier joint : registre des incidents. Heures travaillées du mois : [valeur].
Définitions MCC (font foi) :
- Taux de fréquence (TF) = nombre d'accidents avec arrêt × 1 000 000 / heures travaillées.
- Ratio presque-accidents / événements avec blessure.
Avec l'exécution de code : indicateurs du mois et cumul annuel ; répartition par type et par zone ;
liste des événements dont le statut est « Actions en retard ».
Commentaire de 150 mots : tendances factuelles, sans attribution de cause.
```

**7. Échanges.** « Quelles zones ont le plus d'événements liés à la circulation ? » ; « Prépare 3 questions pour le comité HSE. »

**8. Exemple de résultat (données fictives, cumul de la période).** 160 événements : 46 presque-accidents, 36 événements environnementaux, 23 premiers soins, 20 accidents avec arrêt, 18 dommages matériels, 17 soins médicaux ; 26 événements avec actions en retard ; zones les plus représentées : route d'accès (23), fosse Nord (22) et magasin (22).

![Figure 23.3 — Registre HSE 2025-2026 : événements par type et par zone (données fictives MCC). Graphique réalisé pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig23_1_incidents_hse.png){width=100%}

**9. Contrôle.** Recalcul du TF à la main ; vérification que les heures travaillées sont celles validées par les RH.

**10. Erreurs possibles.** Définition d'indicateur différente de celle de l'entreprise ; double comptage d'événements ; confusion entre date de l'événement et date de déclaration.

**11. Limites.** Les indicateurs « retardés » (accidents) ne mesurent pas à eux seuls la maîtrise des risques ; ils doivent être complétés par des indicateurs de vérification des contrôles critiques.

**12. Livrable.** Rapport HSE mensuel validé.

#### Cas d'usage 23.3 — Vérification des contrôles critiques (condensé)

Pour l'événement majeur « collision ou sortie de route d'un engin sur rampe », l'équipe HSE a identifié des contrôles critiques (merlons conformes, état et arrosage maîtrisé des rampes, limitation de vitesse, freinage conforme, séparation engins-véhicules légers). Claude transforme les normes de performance de chaque contrôle en **check-lists de vérification de terrain**, prépare le tableau de suivi des vérifications et synthétise les résultats saisis par les vérificateurs. Les contrôles critiques eux-mêmes et leurs normes de performance sont définis par les experts, conformément à l'approche de l'ICMM [@ICMM-CCM-2015].

#### Cas d'usage 23.4 — Relecture d'une analyse de risques (condensé)

Claude relit une analyse de risques de poste (par exemple « remplacement d'un flexible hydraulique en atelier ») et signale les dangers fréquemment associés à ce type de tâche qui n'y figurent pas, les mesures de maîtrise imprécises et les incohérences de cotation. L'équipe décide de ce qu'il faut intégrer ; la cotation reste la sienne.

![Figure 23.4 — Chambre de refuge pour environnement souterrain : un exemple de contrôle critique en cas d'urgence. Photographie : LeaSubroca, « Emergency and rescue shelter for underground environment », Wikimedia Commons, licence CC BY-SA 4.0, https://commons.wikimedia.org/wiki/File:Emergency-and-rescue-shelter-for-underground-environment-mines-tunnels-subroca.png (consulté le 16/11/2026). Photographie d'illustration, sans lien avec MCC.](02_ILLUSTRATIONS/PHOTOGRAPHIES/photo_refuge_souterrain.jpg){width=70%}

### E. Prompts commentés

**Prompt 23.1 — Relecture d'une analyse de risques**

```text
Voici l'analyse de risques de la tâche « [tâche] » (jointe) et la procédure associée.
En tant que relecteur, signale :
1. les dangers couramment associés à ce type de tâche qui n'apparaissent pas ;
2. les mesures de maîtrise vagues (« faire attention ») à préciser ;
3. les incohérences de cotation entre lignes comparables.
Ne modifie aucune cotation ; présente tes remarques sous forme de questions pour l'équipe.
```

*Commentaire.* La formulation « sous forme de questions » maintient la responsabilité de l'équipe et favorise la discussion plutôt que l'acceptation passive.

### F. Exercices pratiques

**Exercice 23.1 (guidé).** Réalisez le cas 23.1 avec le document d'exercice. Faites relire votre rapport par un collègue : a-t-il trouvé une phrase qui suggère une cause ?

**Exercice 23.2 (guidé).** Réalisez le cas 23.2 en supposant 420 000 heures travaillées sur le mois et 2 accidents avec arrêt. Recalculez le TF à la main.

**Exercice 23.3 (autonome).** Pour un événement majeur de votre site, transformez les normes de performance de deux contrôles critiques en check-lists de vérification.

### G. Livrable professionnel

**Kit HSE assisté** : modèle de rapport préliminaire et prompt ; tableau de bord mensuel ; check-lists de vérification des contrôles critiques ; trois causeries ; procédure interne précisant ce que Claude ne fait pas.

### H. Vérification des résultats

::: controle
- Aucun rapport ne contient de cause, de responsabilité ou de gravité non validée par l'équipe compétente.
- Les indicateurs sont calculés selon les définitions officielles de l'entreprise et recalculés par sondage.
- Les données personnelles sont minimisées et anonymisées pour toute diffusion large.
- Les check-lists de contrôles critiques correspondent exactement aux normes de performance validées.
:::

::: setrompe
Dans un premier jet, Claude écrit : « L'incident est dû à la combinaison de la pluie et d'une défaillance hydraulique. » La phrase est plausible — et peut-être juste —, mais elle anticipe l'enquête et pourrait influencer les témoignages. **Contre-mesure** : règle explicite « aucune cause », et liste finale des phrases non issues des documents.
:::

### I. Limites et précautions

- En situation d'urgence, n'utilisez pas Claude : appliquez le plan d'urgence.
- Les déclarations d'incident contiennent des données personnelles et parfois médicales : classification « confidentiel » ou « restreint ».
- Les déclarations réglementaires aux autorités suivent les procédures officielles et sont signées par les personnes désignées.

### J. Boîte à outils

- Prompts des cas 23.1 (rapport préliminaire), 23.2 (indicateurs) et prompt 23.1 (relecture d'analyse de risques).
- Formule anti-conclusion : « Aucune cause, aucune responsabilité, aucune classification de gravité. »
- Modèle de rapport préliminaire (Annexe D).

### K. Quiz

1. **(Vrai ou faux)** Claude peut proposer la classification de gravité réglementaire d'un accident.
2. **(Calcul)** Avec 2 accidents avec arrêt et 420 000 heures travaillées, quel est le taux de fréquence ?
3. **(Compréhension)** Pourquoi un rapport préliminaire ne doit-il pas suggérer de cause ?
4. **(QCM)** Que sont les contrôles critiques selon l'approche de l'ICMM ? a) des indicateurs financiers ; b) les contrôles qui préviennent un événement majeur ou en limitent les conséquences ; c) des audits externes ; d) des logiciels.
5. **(Mise en situation)** Pendant une alerte d'urgence, un collègue veut demander à Claude la conduite à tenir. Que lui dites-vous ?
6. **(Vrai ou faux)** Les indicateurs d'accidents suffisent à mesurer la maîtrise des risques.
7. **(Application)** Dans les données d'exercice, combien d'événements ont des actions en retard ?
8. **(Compréhension)** Pourquoi présenter les remarques de relecture d'une analyse de risques sous forme de questions ?
9. **(Analyse critique)** Quel risque présente la diffusion large d'un rapport d'incident non anonymisé ?
10. **(QCM)** La Convention n° 176 de l'OIT porte sur : a) la fiscalité minière ; b) la sécurité et la santé dans les mines ; c) les résidus ; d) la transparence des revenus.

<div class="carnet" titre="Chapitre 23 — Claude appliqué à l'hygiène, à la sécurité et à l'environnement au travail"></div>
