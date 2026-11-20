# Module 5 : Diagnostiquer les dysfonctionnements et cartographier les processus

## 5.1 Mise en situation

À Horizons Partagés, le bailleur principal a adressé un courrier sévère : les rapports financiers arrivent avec trois semaines de retard, et lors du dernier audit, 11 pièces justificatives sur 60 sélectionnées n'ont pas été retrouvées dans les délais. La direction a une réponse toute prête : « Il nous faut un logiciel avec de l'IA. »

Avant d'acheter quoi que ce soit, le responsable financier, Ibrahim, propose de comprendre d'abord pourquoi les rapports sont en retard et pourquoi les pièces se perdent. Deux semaines plus tard, le diagnostic montre que la moitié du problème vient… d'une signature : le directeur, souvent en déplacement, signe les demandes de paiement avec cinq à douze jours de retard. Aucun logiciel n'aurait résolu ce problème seul.

## 5.2 Problématique

On confond souvent le **symptôme** (« les rapports sont en retard »), le **problème** (« la clôture mensuelle n'est jamais terminée à temps ») et ses **causes profondes** (« les pièces arrivent tard du terrain », « une seule personne sait faire », « les validations attendent »). Introduire l'IA sur un symptôme sans traiter les causes produit au mieux un gain marginal, au pire une automatisation du dysfonctionnement.

## 5.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. conduire un diagnostic organisationnel, administratif, financier, comptable et opérationnel ;
2. distinguer symptômes, problèmes et causes profondes ;
3. identifier les tâches répétitives à fort potentiel d'amélioration ;
4. cartographier un processus « tel quel » et repérer ses points de blocage ;
5. repérer les faiblesses du contrôle interne à l'aide d'un référentiel reconnu ;
6. transformer des notes d'entretien en carte de processus avec l'aide de l'IA.

## 5.4 Notions et définitions

- **Diagnostic** : analyse structurée de la situation d'une organisation, fondée sur des faits (documents, données, entretiens, observations).
- **Symptôme** : manifestation visible d'un dysfonctionnement.
- **Cause profonde (cause racine)** : cause qui, si elle était supprimée, empêcherait le problème de se reproduire.
- **Processus « tel quel » (*as-is*)** : description du processus tel qu'il se déroule réellement, et non tel qu'il est prévu dans les procédures.
- **Processus cible (*to-be*)** : processus amélioré que l'on souhaite mettre en place.
- **Point de blocage** : étape où le flux ralentit, s'arrête ou génère des erreurs.
- **Contrôle interne** : dispositifs qui donnent une assurance raisonnable sur l'atteinte des objectifs, la fiabilité de l'information et la conformité. Le référentiel COSO (2013) l'organise en cinq composantes (environnement de contrôle, évaluation des risques, activités de contrôle, information et communication, pilotage) déclinées en dix-sept principes.

## 5.5 Explications détaillées

### Les cinq angles du diagnostic

| Diagnostic | Questions clés | Sources de faits |
|---|---|---|
| **Organisationnel** | Les rôles sont-ils clairs ? Qui décide quoi ? Les délégations sont-elles écrites ? | Statuts, organigramme, délégations de pouvoir, fiches de poste |
| **Administratif** | Les documents sont-ils retrouvables ? Les procédures sont-elles écrites et appliquées ? | Plan de classement, manuels, échantillon de dossiers |
| **Financier** | Le budget est-il suivi ? La trésorerie est-elle anticipée ? Les rapports sont-ils à l'heure ? | Budgets, suivis, plans de trésorerie, rapports aux bailleurs |
| **Comptable** | Les écritures sont-elles complètes, justifiées et à jour ? Les rapprochements sont-ils faits ? | Grand livre, rapprochements bancaires, échantillon de pièces |
| **Opérationnel** | Les activités sont-elles suivies ? Les données de terrain sont-elles fiables et à temps ? | Bases de suivi, rapports d'activité, visites de terrain |

Un diagnostic utile combine **trois types de preuves** : ce que disent les personnes (entretiens), ce que montrent les documents, et ce que l'on observe (suivre une facture du début à la fin, par exemple).

### Des symptômes aux causes profondes

![Figure 5.2 : Arbre des causes : retards de reporting financier](03_ILLUSTRATIONS/figures/fig_5_2.svg)

Deux techniques simples suffisent la plupart du temps.

**Les « 5 pourquoi ».** On pose la question « pourquoi ? » jusqu'à atteindre une cause sur laquelle on peut agir.

1. Pourquoi les rapports financiers sont-ils en retard ? : Parce que la clôture mensuelle n'est pas terminée.
2. Pourquoi ? : Parce que des dépenses ne sont pas encore saisies.
3. Pourquoi ? : Parce que les demandes de paiement attendent la signature du directeur.
4. Pourquoi ? : Parce qu'il est le seul habilité à signer, quel que soit le montant.
5. Pourquoi ? : Parce que la délégation de signature n'a jamais été formalisée.

La cause profonde est organisationnelle : **absence de délégation de signature par seuil.** La solution relève du conseil d'administration, pas d'un logiciel. Une fois cette cause traitée, un workflow de validation électronique (module 12) devient pertinent.

**Le diagramme causes-effet** (ou « en arête de poisson ») classe les causes par familles (méthodes, outils, personnes, données, environnement) et évite de s'arrêter à une seule explication.

### Repérer les tâches répétitives

Une tâche est un bon candidat à l'amélioration lorsqu'elle est :

- **fréquente** (quotidienne, hebdomadaire, mensuelle) ;
- **chronophage** au total ;
- **standardisable** (mêmes étapes à chaque fois) ;
- **source d'erreurs** (ressaisie, copier-coller) ;
- **peu valorisante** pour les personnes qui l'exécutent.

Une méthode simple consiste à faire tenir à chaque personne, pendant deux semaines, un **journal des tâches** : tâche, durée, fréquence, outils, irritants. Les résultats agrégés révèlent les gisements.

### Cartographier un processus

![Figure 5.1 : Cartographie « tel quel » du circuit des dépenses](03_ILLUSTRATIONS/figures/fig_5_1.svg)

La cartographie en **couloirs** (une ligne par acteur) est la plus lisible. Pour la construire :

1. **Délimiter** le processus : événement déclencheur (« un besoin de dépense apparaît ») et résultat final (« la dépense est payée, enregistrée et archivée »).
2. **Lister les acteurs** : chaque acteur a son couloir.
3. **Décrire les étapes réelles** dans l'ordre, en interrogeant les personnes qui les exécutent, pas seulement les responsables.
4. **Noter pour chaque étape** : durée, outil, document, règle, contrôle.
5. **Marquer les points de blocage** : attentes, ressaisies, allers-retours, pertes d'information.
6. **Faire valider** la carte par les acteurs.

### Repérer les faiblesses du contrôle interne

Lors de la cartographie, posez systématiquement les questions suivantes, inspirées des composantes du COSO :

| Composante | Question de diagnostic | Exemple de faiblesse |
|---|---|---|
| Environnement de contrôle | Les responsabilités et délégations sont-elles définies ? | Aucune délégation de signature écrite |
| Évaluation des risques | Les risques de ce processus ont-ils été identifiés ? | Aucun registre des risques |
| Activités de contrôle | Existe-t-il des autorisations, une séparation des tâches, des rapprochements ? | La même personne commande, réceptionne et paie |
| Information et communication | L'information est-elle fiable, à jour et accessible aux bonnes personnes ? | Budget suivi dans des fichiers personnels non partagés |
| Pilotage | Les contrôles sont-ils eux-mêmes vérifiés ? | Rapprochements bancaires non revus |

> **🔎 À retenir** : Un diagnostic n'est pas un audit à charge. Son but est de comprendre pour améliorer. Présentez-le ainsi aux équipes : vous obtiendrez des informations plus sincères.

## 5.6 Application professionnelle : diagnostic du circuit des dépenses d'Horizons Partagés

**A. Contexte.** Fondation de 60 salariés, 4 bureaux, 5 bailleurs ; comptabilité sur logiciel au siège ; pièces collectées sur papier dans les bureaux de terrain.

**B. Problème observé.** Retards de reporting financier et pièces introuvables.

**C. Symptômes.** Rapports remis avec trois semaines de retard ; 11 pièces sur 60 non retrouvées lors de l'audit ; heures supplémentaires de la comptable en fin de mois.

**D. Causes profondes** (après entretiens et « 5 pourquoi ») : absence de délégation de signature ; formulaires papier incomplets ; ressaisie manuelle au siège ; classement non normalisé ; une seule comptable formée.

**E. Processus actuel.** Voir figure 5.1 : fiche papier → vérification budgétaire sur un fichier personnel → signature du directeur → ressaisie → classement en classeur.

**F. Points de faiblesse.** Quatre points de blocage (fiche incomplète, attente de signature, ressaisie, classement) ; faiblesse de séparation des tâches au bureau de terrain n° 3 (la même personne demande et réceptionne).

**G. Résultat recherché.** Rapports remis dans les délais contractuels ; 100 % des pièces retrouvables en moins de cinq minutes ; délai moyen de traitement d'une dépense ramené à cinq jours ouvrables.

**H. Pertinence de l'IA.** Partielle : l'extraction de données des pièces et le classement peuvent être assistés (module 12) ; mais les deux causes principales, délégation de signature et formulaires incomplets, sont organisationnelles.

**I. Alternatives sans IA.** Délégation de signature par seuils adoptée par le CA ; formulaire numérique avec champs obligatoires ; plan de classement et règle de nommage (module 7) ; calendrier de clôture.

**J. Solution recommandée.** Séquence en trois temps : (1) mesures organisationnelles sans IA ; (2) formulaire numérique et workflow de validation ; (3) extraction assistée des pièces et contrôles automatiques.

**K. Niveau.** Débutant pour l'étape 1, Intermédiaire pour les étapes 2 et 3.

**L. Outils nécessaires.** Traitement de texte (délégations), formulaire numérique, espace documentaire partagé ; puis outil d'extraction de documents.

**M. Étapes détaillées.** Semaine 1 : collecte documentaire et journal des tâches. Semaine 2 : entretiens et suivi de trois dépenses réelles de bout en bout. Semaine 3 : cartographie, arbre des causes, restitution.

**N. Prompt.** Fiche P5.1 ci-dessous, pour transformer les notes d'entretien en carte de processus.

**O. Exemple de résultat.** Carte « tel quel » (figure 5.1) et arbre des causes (figure 5.2).

**P. Vérification.** Chaque étape de la carte est confirmée par au moins deux acteurs et par le suivi d'une dépense réelle.

**Q. Contrôles humains.** Validation de la carte par les acteurs ; validation des recommandations par la direction ; adoption de la délégation par le CA.

**R. Risques.** Diagnostic perçu comme une recherche de coupables ; carte idéalisée ; recommandations ignorées faute de responsable.

**S. Coûts.** Essentiellement du temps interne (environ 40 heures réparties) ; aucun coût logiciel à ce stade.

**T. Indicateurs.** Délai moyen de traitement d'une dépense ; taux de pièces retrouvées en moins de cinq minutes ; nombre de jours de retard des rapports.

**U. Amélioration continue.** Nouvelle mesure des indicateurs trois mois après la mise en œuvre ; mise à jour de la carte à chaque changement de procédure.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Journal des tâches papier ou tableur, entretiens, carte dessinée sur papier puis mise au propre avec un assistant | Papier, tableur, assistant | Temps | Dépend de la rigueur de la collecte |
| Intermédiaire | Formulaire en ligne pour le journal des tâches ; outil de diagramme ; synthèse assistée des entretiens | Formulaire, outil de diagramme, suite bureautique avec IA | Abonnements modestes | Confidentialité des entretiens |
| Avancé | Analyse des journaux d'événements des logiciels (dates de création, de validation, de paiement) pour mesurer les délais réels (« fouille de processus ») | Outil d'analyse de processus, extraction de données ERP | Licences, compétences | Exige des données horodatées fiables |

## 5.7 Prompt prêt à l'emploi

### Fiche P5.1 : Transformer des notes d'entretien en carte de processus

**A. Titre.** Du récit à la carte de processus en couloirs.

**B. Objectif.** Structurer des notes d'entretien en une liste d'étapes par acteur, avec durées, documents, contrôles et points de blocage, prête à être dessinée et validée.

**C. Contexte d'utilisation.** Diagnostic de processus ; après une série d'entretiens.

**D. Données nécessaires.** Notes d'entretien **anonymisées** (fonctions plutôt que noms) ; délimitation du processus.

**E. Prompt complet.**

```text
Contexte : je réalise le diagnostic du processus « [NOM DU PROCESSUS] »
dans une ASBL. Déclencheur : [ÉVÉNEMENT]. Résultat final : [RÉSULTAT].
Tâche : à partir des notes d'entretien ci-dessous, reconstitue le
processus tel qu'il se déroule réellement.
Données : <notes>[NOTES ANONYMISÉES, une section par entretien,
avec la fonction de la personne]</notes>
Résultat attendu :
1. Un tableau « N° | Étape | Acteur (fonction) | Durée ou délai
   mentionné | Outil/document | Contrôle existant | Problème signalé
   | Source (entretien n°) ».
2. La liste des points de blocage, classés par gravité supposée.
3. Les contradictions entre entretiens (même étape décrite
   différemment).
4. Les questions à poser pour compléter la carte.
5. Les faiblesses potentielles de contrôle interne (séparation des
   tâches, autorisations, rapprochements, traçabilité).
Limites : ne comble pas les manques par des suppositions ; écris
« non précisé ». Distingue clairement ce qui est rapporté de ce que
tu déduis.
```

**F. Instructions d'utilisation.** Remplacez les noms par des fonctions avant de coller les notes. Numérotez les entretiens. Utilisez le tableau obtenu pour dessiner la carte dans un outil de diagramme ou sur papier.

**G. Résultat attendu.** Un tableau d'étapes traçables jusqu'aux entretiens, des points de blocage, des contradictions, des questions complémentaires.

**H. Exemple d'application (illustratif).** À partir de six entretiens, l'assistant relève une contradiction utile : la coordinatrice affirme que le budget est vérifié « avant toute demande », tandis que l'assistante du bureau de terrain indique que « la vérification est faite après signature, quand on a le temps ». Le suivi d'une dépense réelle confirme la seconde version.

**I. Méthode de vérification.** Pour chaque étape, retrouvez l'entretien source ; suivez au moins une transaction réelle de bout en bout ; faites valider la carte par les acteurs en réunion.

**J. Précautions.** Les notes d'entretien contiennent souvent des jugements sur des collègues : supprimez-les ou neutralisez-les avant traitement. Classification orange au minimum (module 8).

**K. Amélioration.** Si le tableau mélange plusieurs variantes du processus (par exemple, achats inférieurs ou supérieurs à un seuil), demandez : « Sépare le processus en variantes selon [CRITÈRE] et produis un tableau par variante. »

## 5.8 Résultats attendus

Un rapport de diagnostic de 5 à 10 pages comprenant : carte « tel quel », arbre des causes, liste des tâches répétitives, faiblesses de contrôle interne, et recommandations classées en « organisationnelles », « outils simples » et « IA envisageable ».

## 5.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Les conclusions d'un diagnostic engagent des personnes et des services. Elles sont validées par la direction, présentées aux équipes concernées, et ne citent jamais de personne nommément comme cause d'un dysfonctionnement.

## 5.10 Risques et erreurs à éviter

- Cartographier la procédure écrite plutôt que la pratique réelle.
- S'arrêter au premier « pourquoi ».
- Présenter le diagnostic comme une évaluation individuelle.
- Recommander l'IA par principe, alors que la cause est organisationnelle.
- Négliger de mesurer la situation de départ (sans mesure initiale, pas de preuve d'amélioration).

## 5.11 Exercice pratique

**Consigne (90 minutes).** Choisissez un processus de votre organisation (paiement d'un fournisseur, remboursement d'un bénévole, inscription d'un bénéficiaire). (1) Délimitez-le. (2) Interrogez deux personnes qui l'exécutent. (3) Appliquez la fiche P5.1. (4) Dessinez la carte en couloirs. (5) Identifiez trois points de blocage et leur cause profonde avec les « 5 pourquoi ». (6) Classez chaque piste de solution en « organisationnelle », « outil simple » ou « IA envisageable ».

**Éléments de correction.** Une bonne réponse : délimite clairement début et fin ; distingue au moins trois acteurs ; signale au moins une différence entre procédure écrite et pratique ; aboutit à au moins une cause profonde organisationnelle ; propose au moins une solution sans IA.

## 5.12 Synthèse

- Un diagnostic combine entretiens, documents et observation.
- Il faut remonter des symptômes aux causes profondes (« 5 pourquoi », diagramme causes-effet).
- La cartographie « tel quel » en couloirs révèle les points de blocage réels.
- Les cinq composantes du COSO offrent une grille simple pour repérer les faiblesses de contrôle interne.
- Beaucoup de causes sont organisationnelles : elles se traitent avant ou à côté de l'IA.

## 5.13 QCM : Module 5

**Q1.** (une seule réponse) « Les rapports financiers arrivent en retard » est :

a) un symptôme.
b) une cause profonde.
c) une solution.
d) un indicateur de performance.

**Q2.** (une seule réponse) La carte « tel quel » doit décrire :

a) le processus prévu par le manuel de procédures.
b) le processus idéal.
c) le processus du principal bailleur.
d) le processus tel qu'il se déroule réellement.

**Q3.** (une ou plusieurs réponses) Quelles sources de preuves combine un bon diagnostic ?

a) Entretiens.
b) Documents.
c) Observation de transactions réelles.
d) Impressions générales de la direction, sans vérification.

**Q4.** (une seule réponse) Selon le COSO (2013), le contrôle interne comporte :

a) trois composantes et dix principes.
b) cinq composantes et dix-sept principes.
c) sept composantes et vingt principes.
d) une seule composante : l'audit.

**Q5.** (une ou plusieurs réponses) Quelles caractéristiques font d'une tâche un bon candidat à l'amélioration ?

a) Fréquente.
b) Standardisable.
c) Source d'erreurs de ressaisie.
d) Impliquant un jugement éthique complexe à chaque occurrence.

**Q6.** (une seule réponse) Dans l'exemple d'Horizons Partagés, la cause profonde principale des retards était :

a) l'absence d'IA.
b) la lenteur d'internet.
c) le nombre de bailleurs.
d) l'absence de délégation de signature formalisée.

**Q7.** (mise en situation, une seule réponse) Au bureau de terrain, la même personne commande, réceptionne et paie les fournitures. Quelle composante du contrôle interne est principalement concernée ?

a) Pilotage.
b) Information et communication.
c) Activités de contrôle (séparation des tâches).
d) Aucune.

**Q8.** (mise en situation, une seule réponse) Deux entretiens décrivent différemment la même étape. Que faites-vous ?

a) Retenir la version du responsable hiérarchique.
b) Suivre une transaction réelle pour établir les faits.
c) Retenir la version la plus récente.
d) Supprimer l'étape de la carte.

**Q9.** (une seule réponse) Pourquoi mesurer la situation de départ ?

a) Pour pouvoir démontrer l'effet des améliorations.
b) Pour sanctionner les retards.
c) Parce que le bailleur l'exige toujours.
d) Ce n'est pas nécessaire.

**Q10.** (une ou plusieurs réponses) Avant de soumettre des notes d'entretien à un assistant d'IA, il faut :

a) remplacer les noms par des fonctions.
b) neutraliser les jugements sur des collègues.
c) vérifier que l'outil est autorisé pour ce niveau de confidentialité.
d) ajouter les coordonnées des personnes interrogées.

## 5.14 Corrigé détaillé : Module 5

**Q1 : a.** C'est la manifestation visible ; les causes sont à rechercher en amont.

**Q2 : d.** La carte doit refléter la pratique réelle, souvent différente de la procédure écrite.

**Q3 : a, b, c.** Les impressions non vérifiées (d) ne constituent pas des preuves.

**Q4 : b.** Cinq composantes (environnement de contrôle, évaluation des risques, activités de contrôle, information et communication, pilotage) et dix-sept principes.

**Q5 : a, b, c.** Une tâche exigeant un jugement éthique complexe (d) est mal adaptée à l'automatisation.

**Q6 : d.** La cause était organisationnelle ; un logiciel seul ne l'aurait pas résolue.

**Q7 : c.** Le cumul de fonctions incompatibles est une faiblesse des activités de contrôle.

**Q8 : b.** Les faits priment : on vérifie par l'observation d'une transaction réelle.

**Q9 : a.** Sans mesure initiale, impossible de prouver un progrès.

**Q10 : a, b, c.** Ajouter les coordonnées (d) contredit le principe de minimisation des données.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Committee of Sponsoring Organizations of the Treadway Commission (COSO). (2013). *Internal Control : Integrated Framework*.
