## Chapitre 20. Claude appliqué au forage, au minage et aux opérations d'extraction

### A. Mise en situation professionnelle

Albert Kalenga, superintendant forage-minage de MCC, termine chaque poste de nuit par une heure de « paperasse » : rapport de poste, mise à jour du registre des tirs, réponses aux questions de la planification, préparation de la causerie du matin. Il pilote aussi un sujet délicat : les vibrations ressenties au village de Kasongo-Mbiyo après certains tirs, qui suscitent des plaintes. Il voudrait gagner du temps sur l'écrit pour en passer davantage sur le terrain, et mieux expliquer aux riverains ce que fait la mine.

![Figure 20.1. Chargement d'un camion de grande capacité par une pelle hydraulique. Titre original : « Belaz haul truck and a Hitachi mining excavator ». Auteur : Sandrerro. Source : Wikimedia Commons, [https://commons.wikimedia.org/wiki/File:Belaz_haul_truck_and_a_Hitachi_mining_excavator.jpg](https://commons.wikimedia.org/wiki/File:Belaz_haul_truck_and_a_Hitachi_mining_excavator.jpg) (consulté le 16/11/2026). Licence : [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.fr) ; image redimensionnée pour l'édition. Photographie d'illustration, sans lien avec l'entreprise fictive MCC.](02_ILLUSTRATIONS/PHOTOGRAPHIES/photo_pelle_camion.jpg){width=78%}

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Situer** précisément la frontière entre ce que Claude peut faire et ce qui relève exclusivement des personnes habilitées en forage-minage.
2. **Produire** des rapports de poste structurés à partir de notes brutes.
3. **Documenter** un retour d'expérience de tir à partir de données validées.
4. **Analyser** des données d'exploitation (temps de cycle, productivité) avec calculs traçables.
5. **Préparer** une communication claire et prudente à destination des riverains.

### C. Comprendre avant de pratiquer : Profil du métier

*Tableau 20.1. Profil des métiers du forage-minage et de l'extraction.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Exécution sûre des forages et des tirs ; chargement et transport ; productivité ; respect des procédures et de la réglementation sur les explosifs |
| Tâches quotidiennes | Supervision des postes, contrôle des trous, gestion des explosifs (personnes habilitées), sécurisation des zones, suivi de la flotte, rapports |
| Difficultés | Pression de production ; météo ; disponibilité des engins ; relations avec les riverains (vibrations, poussières) ; charge administrative |
| Documents | Plans de tir, registres des explosifs, rapports de poste, comptes rendus d'incident, mesures de vibrations, procédures |
| Données | Métrages forés, consommation d'explosif, granulométrie, vibrations et surpressions mesurées, temps de cycle, disponibilités |
| Livrables | Rapports de poste, registres, retours d'expérience, indicateurs de productivité, causeries |
| Assistables par Claude | Mise en forme des rapports ; synthèses de données validées ; retours d'expérience ; causeries ; communications aux riverains (à valider) ; analyse de données d'exploitation |
| Limites | Conception, validation et autorisation des tirs ; gestion des explosifs et des ratés ; distances de sécurité ; décisions d'évacuation |

![Figure 20.2. Cycle forage-minage : ce que Claude peut faire, et ce qu'il ne fait jamais. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig20_2_forage_minage_frontiere.png){width=100%}

::: attention
**Ligne rouge.** La conception, la validation et l'autorisation des tirs, la manipulation et le stockage des explosifs, le traitement des ratés et la fixation des distances de sécurité relèvent exclusivement des personnes habilitées et des procédures de l'entreprise, conformément à la réglementation applicable. Le recueil de l'OIT sur les mines à ciel ouvert consacre des développements détaillés à l'utilisation des explosifs [@ILO-OPENCAST]. Ne demandez jamais à Claude de calculer une charge, un retard ou une distance de sécurité destinés à être appliqués.
:::

### D. Démonstration guidée : Cas d'usage

#### Cas d'usage 20.1. Le rapport de poste à partir de notes brutes

**1. Problème.** Les superviseurs rédigent leur rapport en fin de poste, fatigués ; les rapports sont hétérogènes et incomplets.

**2. Méthode habituelle.** Formulaire papier ou tableur rempli de mémoire.

**3. Contribution de Claude.** À partir de notes dictées ou tapées pendant le poste, production d'un rapport au format MCC, avec rubriques obligatoires, et liste des informations manquantes.

**4. Données.** Notes du superviseur ; modèle de rapport ; extraction du système de gestion de flotte (si disponible).

**5. Procédure.** Notes au fil du poste (application mobile ou carnet) → prompt de mise en forme → relecture et complément → signature.

**6. Prompt.**

```text
Tu mets en forme le rapport de poste d'un superviseur de mine à ciel ouvert (MCC).
Notes brutes du poste de nuit du [date] : <notes> … </notes>

Rubriques obligatoires : SÉCURITÉ (événements, presque-accidents, constats) ;
PRODUCTION (métrage foré, tirs réalisés selon le registre, tonnages chargés) ;
ÉQUIPEMENTS (pannes, arrêts, interventions) ; ENVIRONNEMENT (poussières, eau, déversements) ;
CONSIGNES pour le poste suivant ; POINTS À REMONTER.
Règles : reprends uniquement les informations des notes ; n'invente aucun chiffre ;
écris « non renseigné » pour toute rubrique vide ; place en tête tout événement de sécurité.
Style télégraphique, une page maximum.
```

**7. Échanges successifs.** « Compare avec le rapport du poste précédent et liste les problèmes récurrents » ; « Prépare le message de passation pour le superviseur du poste de jour (5 lignes). »

**8. Exemple de résultat (extrait, fictif).** « SÉCURITÉ : presque-accident 02 h 40 rampe R3 : camion CAM-07 glissade au freinage, arrêt contre le merlon, pas de blessé ; rampe fermée 03 h 00-05 h 20. PRODUCTION : métrage foré : non renseigné… »

**9. Contrôle.** Le superviseur relit chaque ligne, complète les chiffres depuis les systèmes officiels et signe.

**10. Erreurs possibles.** Chiffre de note mal interprété (« 3 tirs » au lieu de « 3 trous ») ; événement de sécurité relégué dans une autre rubrique.

**11. Limites.** Le rapport fait foi après signature du superviseur ; les registres réglementaires (explosifs) restent tenus selon la procédure officielle.

**12. Livrable.** Rapport de poste signé, archivé dans le système de l'entreprise.

#### Cas d'usage 20.2. Retour d'expérience sur les tirs et vibrations

**1. Problème.** Les plaintes du village de Kasongo-Mbiyo (fissures, tremblements) se multiplient ; Albert doit analyser les mesures de vibrations et préparer un retour d'expérience pour l'équipe de conception des tirs.

**2. Méthode habituelle.** Fichiers de mesures consultés au cas par cas ; analyse rarement consolidée.

**3. Contribution de Claude.** Consolidation des mesures **validées** et des caractéristiques des tirs, statistiques et graphiques par programme, croisement avec le registre des plaintes, rédaction d'un retour d'expérience factuel **sans recommandation de paramètres de tir**.

**4. Données.** Mesures de vibrations et de surpressions (sismographes), extraits du registre des tirs (date, localisation, distance au village), registre des plaintes.

**5–6. Procédure et prompt.**

```text
Données jointes : mesures de vibrations validées (date, station, vitesse particulaire,
fréquence, surpression), registre des tirs (date, gradin, distance à la station),
extraits du registre des plaintes (catégorie Bruit/Vibrations).
Avec l'exécution de code :
1. Tableau de synthèse des mesures par tir et par station.
2. Comparaison avec le seuil interne de MCC [valeur fournie par le service HSE].
3. Graphique des mesures en fonction de la distance.
4. Correspondance dans le temps entre tirs et plaintes (dates).
Rédige ensuite un retour d'expérience factuel de 1 page pour l'équipe de conception des tirs.
Règle absolue : ne propose aucune modification de charge, de maille, de séquence
ou de retard ; ces décisions appartiennent aux personnes habilitées.
```

**7. Échanges.** « Prépare la liste des données supplémentaires qui aideraient l'équipe à analyser les cas au-dessus du seuil. »

**8. Exemple de résultat.** Synthèse montrant que les mesures proches du seuil interne correspondent à des tirs sur les gradins les plus proches du village, et que trois plaintes suivent des tirs de ce secteur ; aucune recommandation technique.

**9. Contrôle.** Vérification des mesures avec les fichiers bruts des sismographes ; validation du rapport par le responsable forage-minage.

**10. Erreurs possibles.** Unités confondues (mm/s, in/s) ; mesures non validées incluses ; corrélation présentée comme causalité.

**11. Limites.** L'analyse vibratoire de référence (lois d'atténuation, conception des tirs) relève de spécialistes.

**12. Livrable.** Retour d'expérience daté, intégré au dossier de conception des tirs.

#### Cas d'usage 20.3. Fiche d'information pour les riverains (condensé)

À partir des faits validés, Claude rédige une fiche simple pour les habitants : horaires habituels des tirs, signaux d'alerte sonores, consignes, mesures de suivi des vibrations, comment déposer une plainte. La fiche est relue par le responsable forage-minage (exactitude technique) et par le responsable des relations communautaires (ton, traduction, diffusion). Règle : aucune promesse, aucun chiffre non validé.

#### Cas d'usage 20.4. Productivité de la flotte de transport (condensé)

À partir d'une extraction du système de gestion de flotte (temps de cycle, attentes à la pelle, files d'attente au concasseur), Claude calcule par programme les temps de cycle moyens, identifie les goulets d'étranglement et produit des graphiques. L'ingénieur de production interprète et décide (affectation des camions, organisation des postes).

### E. Prompts commentés

**Prompt 20.1. Causerie sécurité à partir d'un événement**

```text
Prépare une causerie de 10 minutes pour les conducteurs de camions à partir du presque-accident
anonymisé suivant : <evenement> … </evenement>.
Contenu : rappel des faits (sans nom), 3 messages clés sur la circulation sur rampe
par temps de pluie, conformes aux règles du site ci-dessous <regles> … </regles>,
2 questions pour faire parler l'équipe, 1 engagement collectif.
Langage simple ; pas de culpabilisation ; une page.
```

*Commentaire.* L'ancrage dans un événement réel rend la causerie concrète ; les règles du site fournies empêchent Claude d'inventer des consignes contraires à la procédure.

### F. Exercices pratiques

**Exercice 20.1 (guidé).** À partir du document `MCC_declarations_incident_INC-2026-0412`, produisez le rapport de poste du poste de nuit du 14 avril 2026 (cas 20.1). Quelles rubriques restent « non renseignées » ?

**Exercice 20.2 (guidé).** Préparez la causerie de l'événement de la rampe R3 avec le prompt 20.1.

**Exercice 20.3 (autonome).** Rédigez la fiche d'information riverains (cas 20.3) et la liste des validations nécessaires avant diffusion.

### G. Livrable professionnel

**Kit documentaire du superviseur** : modèle de rapport de poste et prompt associé ; modèle de retour d'expérience ; trois causeries ; fiche riverains validée.

### H. Vérification des résultats

::: controle
- Aucun paramètre de tir, de charge, de retard ou de distance de sécurité n'a été proposé par Claude ou repris d'une de ses réponses.
- Les chiffres des rapports proviennent des systèmes officiels.
- Les communications externes ont été validées par les responsables désignés.
- Les mesures utilisées sont des mesures validées, avec leurs unités.
:::

::: setrompe
Sollicité pour « réduire les vibrations au village », un assistant d'IA peut proposer spontanément des modifications de charge par retard ou de maille, avec des chiffres d'apparence technique. Ces propositions ne doivent jamais être appliquées : elles ignorent la géologie locale, les mesures, les équipements et la réglementation. Reformulez la demande vers l'analyse des données et la préparation de questions pour les spécialistes.
:::

### I. Limites et précautions

- Le domaine des explosifs est fortement réglementé ; seuls les documents et procédures officiels font foi.
- Les données de vibrations et les relations avec les riverains sont sensibles : diffusion contrôlée.
- La dictée sur mobile en zone de production ne doit jamais détourner l'attention d'une tâche de sécurité.

### J. Boîte à outils

- Prompt du cas 20.1 (rapport de poste), du cas 20.2 (retour d'expérience vibrations), prompt 20.1 (causerie).
- Formule à intégrer à tout prompt du domaine : « Ne propose aucun paramètre de tir ; ces décisions appartiennent aux personnes habilitées. »

### K. Quiz

1. **(Vrai ou faux)** Claude peut calculer la charge par trou d'un tir si on lui fournit la maille.
2. **(QCM)** Quelle tâche est appropriée pour Claude ? a) autoriser un tir ; b) mettre en forme un rapport de poste ; c) fixer la distance d'évacuation ; d) gérer un raté.
3. **(Compréhension)** Pourquoi placer les événements de sécurité en tête du rapport de poste ?
4. **(Mise en situation)** Claude propose de réduire la charge pour limiter les vibrations. Que faites-vous ?
5. **(Application)** Citez deux erreurs possibles lors de la consolidation de mesures de vibrations.
6. **(Vrai ou faux)** Une corrélation entre dates de tirs et dates de plaintes prouve que les tirs ont causé les fissures.
7. **(Compréhension)** Qui doit valider une fiche d'information pour les riverains ?
8. **(QCM)** Le rapport de poste fait foi : a) dès qu'il est produit par Claude ; b) après relecture et signature du superviseur ; c) jamais ; d) après publication.
9. **(Analyse critique)** Pourquoi la dictée sur mobile peut-elle poser un problème de sécurité ?
10. **(Application)** Rédigez la phrase de limitation de rôle d'un prompt d'analyse des tirs.

<div class="carnet" titre="Chapitre 20. Claude appliqué au forage, au minage et aux opérations d'extraction"></div>
