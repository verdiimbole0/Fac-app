# Module 6 : Identifier les opportunités d'IA et choisir les bonnes priorités

## 6.1 Mise en situation

À l'issue du diagnostic, l'équipe de direction d'Horizons Partagés dispose d'une liste de vingt-trois idées : un assistant pour répondre aux questions des agents sur les procédures, la rédaction automatique des procès-verbaux, l'extraction des données des factures, un tableau de bord budgétaire, la prévision de trésorerie, la traduction des supports, un tri automatique des candidatures, un chatbot pour les bénéficiaires… Chaque responsable défend la sienne. Le budget, lui, permet d'en lancer deux.

Comment choisir sans céder à l'idée la plus séduisante ou à la personne la plus convaincante ?

## 6.2 Problématique

Les organisations qui échouent avec l'IA ont souvent commencé par un projet trop ambitieux, mal défini, sur des données insuffisantes ou à risque élevé. À l'inverse, celles qui réussissent commencent par des cas d'usage précis, à valeur visible, réalisables avec leurs moyens, et dont les risques sont maîtrisables. Le choix des priorités est donc une décision décisive, et elle peut se faire avec méthode.

## 6.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. formuler un problème sous forme de cas d'usage précis et mesurable ;
2. définir les résultats attendus et les indicateurs associés ;
3. distinguer automatisation classique et IA ;
4. évaluer la faisabilité, les coûts, les bénéfices et les risques d'un cas d'usage ;
5. utiliser une matrice de sélection pondérée pour prioriser ;
6. rédiger une fiche d'opportunité.

## 6.4 Notions et définitions

- **Cas d'usage** : description d'une utilisation précise d'une technologie, pour un acteur donné, dans un processus donné, en vue d'un résultat mesurable. Exemple : « Le comptable dispose d'une proposition d'imputation pour chaque facture fournisseur reçue, afin de réduire le temps de saisie de 40 % sans augmenter le taux d'erreur. »
- **Résultat attendu** : changement concret visé (temps, qualité, délai, accessibilité, satisfaction).
- **Indicateur** : mesure qui permet de vérifier l'atteinte du résultat.
- **Faisabilité** : capacité réelle à mettre en œuvre le cas d'usage avec les données, compétences, outils et budget disponibles.
- **Coût total de possession** : ensemble des coûts sur la durée : acquisition, paramétrage, formation, abonnements, maintenance, temps de contrôle.
- **Gain rapide** : cas d'usage à forte valeur et à forte faisabilité, réalisable en quelques semaines.

## 6.5 Explications détaillées

### Étape 1 : Partir des problèmes, pas des outils

Chaque idée doit être reformulée en problème. « Un chatbot pour les bénéficiaires » n'est pas un problème. « Les bénéficiaires attendent en moyenne quatre jours une réponse à des questions simples sur les horaires et les documents à apporter » en est un. Cette reformulation fait souvent apparaître des solutions plus simples (une affiche, un message vocal enregistré, une FAQ imprimée).

**Gabarit de formulation :**

> Pour **[ACTEUR]**, dans le processus **[PROCESSUS]**, le problème est **[PROBLÈME OBSERVÉ, CHIFFRÉ SI POSSIBLE]**, ce qui entraîne **[CONSÉQUENCE]**. Nous voulons **[RÉSULTAT ATTENDU]**, mesuré par **[INDICATEUR]**.

### Étape 2 : Définir les résultats attendus

Un résultat attendu doit être **observable**. Évitez « améliorer l'efficacité ». Préférez « ramener le délai de production du procès-verbal de dix à trois jours » ou « réduire de moitié le nombre d'imputations corrigées lors de la revue mensuelle ». Notez la **valeur de départ** (issue du diagnostic) et la **valeur cible**.

### Étape 3 : Automatisation classique ou IA ?

![Figure 6.2 : Arbre de décision : faut-il de l'IA, une automatisation classique ou rien ?](03_ILLUSTRATIONS/figures/fig_6_2.svg)

| Critère | Automatisation classique | IA |
|---|---|---|
| Nature de la tâche | Règles stables et explicites | Langage, images, cas variables, jugement approximatif |
| Exemple | Envoyer un rappel 7 jours avant l'échéance d'un rapport | Résumer un rapport ; extraire les données d'une facture photographiée |
| Prévisibilité | Totale : même entrée, même sortie | Partielle : erreurs possibles, à contrôler |
| Explicabilité | Élevée | Variable, souvent faible |
| Coût de contrôle | Faible après test | Permanent (vérification humaine) |

**Règle d'or :** si une règle simple, une formule de tableur ou un modèle de document suffit, ce sont eux qu'il faut utiliser. L'IA se justifie quand la variabilité des entrées rend les règles impossibles à écrire.

### Étape 4 : Évaluer la faisabilité

Cinq questions :

1. **Données** : les données nécessaires existent-elles, sont-elles accessibles, de qualité suffisante et utilisables légalement ?
2. **Compétences** : qui mettra en place, qui utilisera, qui maintiendra ?
3. **Outils** : une solution existe-t-elle au niveau de maturité de l'organisation (débutant, intermédiaire, avancé) ?
4. **Intégration** : la solution s'insère-t-elle dans le processus existant sans créer de double saisie ?
5. **Acceptabilité** : les utilisateurs et les personnes concernées accepteront-ils la solution ?

### Étape 5 : Estimer coûts et bénéfices

Estimez les coûts sur **trois ans**, pas seulement l'année de lancement.

*Exemple (fictif) : extraction assistée des factures à Horizons Partagés :*

| Poste | Année 1 | Année 2 | Année 3 |
|---|---|---|---|
| Abonnement outil d'extraction | 1 800 UM | 1 800 UM | 1 800 UM |
| Paramétrage et intégration (prestataire) | 2 500 UM | Néant | Néant |
| Formation (temps interne valorisé) | 600 UM | 200 UM | 200 UM |
| Temps de contrôle humain | 1 200 UM | 1 200 UM | 1 200 UM |
| **Total des coûts** | **6 100 UM** | **3 200 UM** | **3 200 UM** |

Bénéfices estimés : la comptable traite environ 350 factures par mois ; la saisie manuelle prend en moyenne 6 minutes par facture, soit 35 heures par mois. Si l'outil ramène ce temps à 2,5 minutes (contrôle compris), le gain est d'environ 20 heures par mois, soit 240 heures par an. Valorisées à 15 UM de l'heure (coût complet fictif), cela représente 3 600 UM par an : à comparer aux 3 200 UM de coûts récurrents.

Conclusion : le gain financier direct est modeste. Le cas d'usage se justifie surtout par des **bénéfices qualitatifs** (réduction des erreurs, pièces retrouvables, clôture plus rapide, réduction de la dépendance à une personne) qui doivent être explicités et mesurés. Ce type d'analyse honnête évite les désillusions.

> **🔎 À retenir** : Le temps « gagné » n'est un bénéfice que s'il est réaffecté à quelque chose d'utile. Précisez à quoi il servira.

### Étape 6 : Évaluer les risques

Pour chaque cas d'usage, évaluez : la sensibilité des données (vert, orange, rouge ; voir le module 8) ; l'impact d'une erreur sur des personnes ou sur l'organisation ; le risque de biais ; la dépendance au fournisseur ; le risque d'image. Un cas d'usage qui implique des décisions sur des personnes vulnérables avec des données sensibles n'est jamais un « gain rapide ».

### Étape 7 : Prioriser avec la matrice de sélection

![Figure 6.1 : Matrice de priorisation valeur × faisabilité](03_ILLUSTRATIONS/figures/fig_6_1.svg)

La matrice de sélection (annexe 3) note chaque cas d'usage sur des critères pondérés :

| Critère | Poids | Échelle (1 à 5) |
|---|---|---|
| Contribution à la mission | 25 % | 1 = indirecte et faible · 5 = directe et forte |
| Gain de temps ou de qualité | 20 % | 1 = négligeable · 5 = majeur |
| Disponibilité et qualité des données | 15 % | 1 = inexistantes · 5 = prêtes |
| Faisabilité technique et compétences | 15 % | 1 = hors de portée · 5 = immédiate |
| Coût sur 3 ans (inversé) | 10 % | 1 = très élevé · 5 = très faible |
| Niveau de risque (inversé) | 15 % | 1 = risque élevé sur des personnes · 5 = risque faible |

*Application (fictive) à huit cas d'usage d'Horizons Partagés :*

| Cas d'usage | Mission | Gain | Données | Faisab. | Coût | Risque | **Score /5** |
|---|---|---|---|---|---|---|---|
| 1. Projet de PV et suivi des décisions | 3 | 4 | 5 | 5 | 5 | 4 | **4,15** |
| 2. Synthèse des rapports de terrain | 4 | 4 | 4 | 4 | 5 | 4 | **4,10** |
| 3. Extraction des données de factures | 3 | 4 | 4 | 4 | 3 | 4 | **3,65** |
| 4. Assistant procédures (RAG) | 4 | 4 | 2 | 2 | 2 | 3 | **3,05** |
| 5. Prévision de trésorerie | 3 | 3 | 2 | 2 | 3 | 4 | **2,85** |
| 6. Déclinaison de publications pour les réseaux | 2 | 3 | 5 | 5 | 5 | 4 | **3,70** |
| 7. Tri automatique des candidatures | 2 | 3 | 3 | 3 | 3 | 1 | **2,45** |
| 8. Traduction des supports | 4 | 3 | 4 | 4 | 4 | 3 | **3,65** |

*Détail du calcul pour le cas 1 :* 3 × 0,25 + 4 × 0,20 + 5 × 0,15 + 5 × 0,15 + 5 × 0,10 + 4 × 0,15 = 0,75 + 0,80 + 0,75 + 0,75 + 0,50 + 0,60 = **4,15**.

> **🔎 À retenir** : Faites toujours les calculs d'une matrice dans un tableur (formule `SOMMEPROD` entre la ligne des notes et la ligne des poids). Lors de la préparation de cet exemple, un premier calcul « de tête » comportait deux erreurs d'arrondi : c'est précisément le type d'erreur que le tableur évite.

**Lecture :** les cas 1 et 2 sont des gains rapides. Le cas 6 arrive en troisième position, mais avec une faible contribution à la mission : il peut être mené en parallèle à faible coût. Le cas 4 (assistant RAG) a une forte valeur mais une faible faisabilité : c'est un **projet structurant**, à préparer en commençant par la gestion documentaire. Le cas 7 est écarté en raison de son niveau de risque (décisions sur des personnes, risque de discrimination).

> **🔎 À retenir** : La matrice éclaire la décision ; elle ne la remplace pas. Un cas d'usage peut être retenu malgré un score moyen pour une raison stratégique explicite, ou écarté malgré un bon score pour une raison éthique. Consignez ces raisons.

## 6.6 Application professionnelle : sélectionner deux projets pilotes

**Processus de mise en œuvre :**

1. Recenser les idées (diagnostic, journal des tâches, suggestions des équipes).
2. Reformuler chaque idée avec le gabarit « problème → résultat → indicateur ».
3. Éliminer les idées qui relèvent d'une solution organisationnelle ou d'une automatisation classique (elles sont traitées à part, souvent plus vite).
4. Rédiger une fiche d'opportunité pour chaque cas d'usage restant (fiche P6.1, annexe 4).
5. Noter les cas d'usage dans la matrice, en atelier, avec trois à cinq personnes de fonctions différentes.
6. Débattre des résultats et retenir deux pilotes : idéalement un gain rapide et la préparation d'un projet structurant.
7. Présenter la sélection à la direction, puis au conseil si nécessaire.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Matrice papier ou tableur ; fiches d'opportunité rédigées avec un assistant | Tableur, assistant | Temps | Notation subjective : la faire en groupe |
| Intermédiaire | Formulaire de collecte des idées ; matrice partagée ; vote pondéré en atelier | Formulaire, tableur partagé | Faibles | Exige un animateur |
| Avancé | Portefeuille de projets numériques géré dans un outil de gestion de projets, avec revue trimestrielle et indicateurs de valeur | Outil de gestion de portefeuille | Licences | Lourd pour une petite structure |

## 6.7 Prompt prêt à l'emploi

### Fiche P6.1 : Rédiger une fiche d'opportunité

**A. Titre.** Fiche d'opportunité d'un cas d'usage d'IA.

**B. Objectif.** Transformer une idée en cas d'usage structuré, évaluable et comparable.

**C. Contexte d'utilisation.** Atelier de priorisation ; préparation d'un comité de direction.

**D. Données nécessaires.** Idée initiale ; constats du diagnostic (chiffres) ; processus concerné ; type de données ; moyens disponibles.

**E. Prompt complet.**

```text
Contexte : [NOM DE L'ASBL], [SECTEUR], [TAILLE]. Niveau de maturité
numérique : [débutant / intermédiaire / avancé]. Budget indicatif :
[MONTANT OU « très limité »].
Idée : [IDÉE]. Constats du diagnostic : [CONSTATS CHIFFRÉS].
Processus concerné : [PROCESSUS]. Données impliquées : [TYPES, sans
données réelles].
Tâche : rédige une fiche d'opportunité.
Résultat attendu (rubriques) :
1. Problème reformulé (gabarit : pour [acteur], dans [processus], le
   problème est…, ce qui entraîne… ).
2. Résultat attendu et 2 à 3 indicateurs avec valeur de départ
   (si connue) et cible proposée.
3. Solution sans IA possible (règle, modèle, réorganisation).
4. Solution avec IA : principe, niveau (débutant/intermédiaire/
   avancé), rôle de l'IA, rôle du logiciel, rôle humain.
5. Données nécessaires et classification probable (public, interne,
   confidentiel).
6. Risques principaux et contrôles humains indispensables.
7. Postes de coûts à estimer sur 3 ans (sans inventer de prix).
8. Questions à trancher avant décision.
Limites : n'invente ni prix ni fonctionnalités de produits nommés.
Indique « à estimer » lorsqu'une donnée chiffrée manque.
```

**F. Instructions d'utilisation.** Une fiche par idée. Complétez ensuite vous-même les coûts à partir de devis ou de pages tarifaires officielles.

**G. Résultat attendu.** Une fiche de une à deux pages, homogène avec les autres fiches, prête à être notée.

**H. Exemple d'application (illustratif).** Pour l'idée « chatbot pour les bénéficiaires », la fiche obtenue propose comme solution sans IA « un message vocal et une affiche listant les cinq questions les plus fréquentes », et relève comme risque principal « des réponses erronées sur l'éligibilité à des services de santé ». Le comité décide de commencer par la solution sans IA et de mesurer la baisse des appels.

**I. Méthode de vérification.** Vérifiez que les chiffres repris viennent du diagnostic ; que la solution sans IA a été sérieusement envisagée ; que les contrôles humains couvrent les décisions sensibles ; qu'aucun prix n'a été inventé.

**J. Précautions.** Ne pas soumettre de données réelles ; décrire les types de données.

**K. Amélioration.** Si la fiche est trop optimiste : « Joue le rôle d'un administrateur sceptique et liste les cinq meilleures objections à ce projet, puis propose une réponse à chacune. »

## 6.8 Résultats attendus

Une liste de cas d'usage reformulés, une fiche d'opportunité par cas, une matrice notée et commentée, une décision motivée sur deux projets pilotes.

## 6.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : La sélection des projets est une décision de direction, documentée, qui tient compte de considérations stratégiques et éthiques que la matrice ne capture pas entièrement. Les cas d'usage touchant des décisions sur des personnes sont soumis à un examen éthique préalable (module 8).

## 6.10 Risques et erreurs à éviter

- Choisir le projet le plus spectaculaire plutôt que le plus utile.
- Sous-estimer le temps de contrôle humain dans les coûts.
- Confondre gain de temps théorique et bénéfice réel.
- Laisser une seule personne noter la matrice.
- Négliger la solution sans IA.

## 6.11 Exercice pratique

**Consigne (90 minutes).** À partir de l'exercice du module 5 : (1) formulez trois cas d'usage avec le gabarit ; (2) rédigez la fiche P6.1 pour chacun ; (3) notez-les dans la matrice pondérée (dans un tableur) ; (4) expliquez en cinq lignes votre choix final, y compris une raison non capturée par la matrice.

**Éléments de correction.** Les cas d'usage sont précis et mesurables ; une solution sans IA est envisagée pour chacun ; les calculs de la matrice sont faits dans un tableur et vérifiables ; le choix final est argumenté et assume ses éventuels écarts avec le classement.

## 6.12 Synthèse

- Partir des problèmes, formuler des cas d'usage mesurables.
- Préférer l'automatisation classique quand des règles stables suffisent.
- Évaluer faisabilité, coûts sur trois ans, bénéfices réels et risques.
- Prioriser avec une matrice pondérée, notée en groupe, calculée dans un tableur.
- Commencer par un gain rapide et préparer un projet structurant.

## 6.13 QCM : Module 6

**Q1.** (une seule réponse) Lequel est un cas d'usage bien formulé ?

a) « Mettre de l'IA dans la comptabilité. »
b) « Le comptable dispose d'une proposition d'imputation pour chaque facture, afin de réduire de 40 % le temps de saisie sans augmenter le taux d'erreur. »
c) « Acheter un chatbot. »
d) « Être plus moderne. »

**Q2.** (une seule réponse) Envoyer un rappel automatique sept jours avant l'échéance d'un rapport relève plutôt :

a) de l'automatisation classique.
b) de l'IA générative.
c) de l'IA prédictive.
d) d'un agent IA.

**Q3.** (une ou plusieurs réponses) Quels postes appartiennent au coût total de possession ?

a) Les abonnements.
b) La formation.
c) Le temps de contrôle humain.
d) La maintenance.

**Q4.** (une seule réponse) Dans la matrice, un cas d'usage à forte valeur mais à faible faisabilité est :

a) un gain rapide.
b) à écarter systématiquement.
c) un projet structurant à préparer.
d) une petite amélioration.

**Q5.** (une seule réponse) Avec les poids du module (25/20/15/15/10/15 %), un cas noté 4, 4, 4, 4, 4, 4 obtient :

a) 3,5
b) 4,0
c) 4,5
d) 24

**Q6.** (une ou plusieurs réponses) Pourquoi le tri automatique des candidatures a-t-il été écarté dans l'exemple ?

a) Il implique des décisions sur des personnes.
b) Il présente un risque de discrimination.
c) Il est techniquement impossible.
d) Son score de risque était très défavorable.

**Q7.** (mise en situation, une seule réponse) Le calcul d'un projet montre un gain financier direct faible, mais une forte réduction des erreurs et des pièces perdues. Que faites-vous ?

a) Abandonner le projet.
b) Gonfler les gains de temps pour justifier le projet.
c) Lancer le projet sans analyse.
d) Expliciter et mesurer les bénéfices qualitatifs dans la décision.

**Q8.** (mise en situation, une seule réponse) Une responsable propose « un chatbot pour les bénéficiaires ». Première étape ?

a) Choisir un fournisseur.
b) Lancer un appel d'offres.
c) Reformuler le besoin en problème mesurable et envisager des solutions sans IA.
d) Rédiger les réponses du chatbot.

**Q9.** (une seule réponse) Le temps gagné grâce à une solution est un bénéfice réel lorsque :

a) il est calculé par le fournisseur.
b) il est réaffecté à une activité utile, identifiée.
c) il dépasse dix heures par mois.
d) il est mentionné dans le rapport annuel.

**Q10.** (une ou plusieurs réponses) Une bonne pratique de notation de la matrice consiste à :

a) noter en groupe, avec des fonctions différentes.
b) calculer les scores dans un tableur.
c) consigner les raisons d'un choix qui s'écarte du classement.
d) laisser l'outil d'IA décider seul.

## 6.14 Corrigé détaillé : Module 6

**Q1 : b.** Il précise l'acteur, le processus, le résultat et l'indicateur.

**Q2 : a.** C'est une règle stable : un rappel programmé suffit.

**Q3 : a, b, c, d.** Tous ces postes doivent être estimés sur la durée.

**Q4 : c.** Il faut préparer ses conditions (données, compétences) avant de le lancer.

**Q5 : b.** 4 × (0,25 + 0,20 + 0,15 + 0,15 + 0,10 + 0,15) = 4 × 1 = 4,0.

**Q6 : a, b, d.** Il n'est pas techniquement impossible (c) ; il est écarté pour des raisons de risque et d'éthique.

**Q7 : d.** Les bénéfices qualitatifs sont réels mais doivent être explicités et mesurés. Gonfler les gains (b) serait malhonnête.

**Q8 : c.** On part toujours du problème ; une solution simple peut suffire.

**Q9 : b.** Le temps gagné n'a de valeur que s'il est réinvesti.

**Q10 : a, b, c.** La décision reste humaine (d est faux). L'exemple du module montre d'ailleurs qu'une erreur de calcul manuel est vite arrivée.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.
