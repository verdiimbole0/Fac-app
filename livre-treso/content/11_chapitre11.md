@chapter 11|Excel, outils numériques et intelligence artificielle : moderniser sa gestion de trésorerie|Outils numériques et IA
Mai 2026. Le comptable de MAKAO passe chaque lundi trois heures à recopier des relevés, recalculer des totaux et mettre en forme le tableau de bord. Un stagiaire lui suggère : « Demandez à l'IA, elle fait tout en dix secondes. » Le comptable essaie : il colle un tableau dans un assistant conversationnel et écrit « analyse ma trésorerie ». Il obtient une page de conseils généraux… et un total des encaissements faux de 2 000 USD.
L'outil n'est pas en cause : la demande était vague et rien n'a été vérifié. Ce chapitre vous apprend à automatiser dans un tableur, puis à dialoguer avec un assistant d'IA comme avec un collaborateur compétent mais faillible.
:::objectifs
- Utiliser les fonctions de tableur indispensables à la trésorerie.
- Comprendre ce qu'est un assistant d'IA, ses possibilités et ses limites.
- Rédiger des prompts financiers précis et vérifier les résultats.
- Protéger les données confidentielles.
:::
## 11.1 Le tableur, socle de la gestion de trésorerie
Excel et Google Sheets suffisent pour tous les outils de ce livre. Les fonctions ci-dessous sont données dans leur version française (l'équivalent anglais entre parenthèses).
|{w:38,62}Fonction|Usage en trésorerie
|SOMME.SI.ENS (SUMIFS)|Totaliser les encaissements d'une semaine : `=SOMME.SI.ENS(Montant;Date;">="&D1;Date;"<="&D2)`
|NB.SI.ENS (COUNTIFS)|Repérer les doublons de factures (chapitre 7)
|SI (IF)|Classer une créance : `=SI(AUJOURDHUI()-Echeance>30;"31 j et +";"0-30 j")`
|AUJOURDHUI (TODAY)|Calculer les jours de retard
|RECHERCHEX (XLOOKUP) ou INDEX/EQUIV|Retrouver les conditions d'un client
|MIN (MIN)|Identifier le point bas d'une série de soldes
Ajoutez trois bonnes pratiques : des **tableaux structurés** (Insertion > Tableau) qui étendent automatiquement les formules, la **validation des données** (listes déroulantes de catégories) et la **mise en forme conditionnelle** (solde négatif en couleur). Une règle d'or : les données sont saisies une seule fois, dans un onglet de saisie ; tous les autres onglets calculent. Les fichiers Excel fournis avec ce livre suivent ce principe.
## 11.2 Ce qu'est (et n'est pas) un assistant d'IA
Un assistant conversationnel d'**intelligence artificielle générative** est un programme entraîné sur de très grandes quantités de textes pour produire une réponse plausible à une demande écrite, le **prompt**. Il sait reformuler, structurer, proposer des plans, rédiger des courriers, écrire des formules de tableur et commenter des chiffres. Mais il **prédit** du texte : il peut inventer une information avec assurance (on parle d'**hallucination**), se tromper dans un calcul, mal comprendre une colonne ou proposer une mesure inadaptée à votre contexte légal.
:::attention! Protection des données
N'envoyez jamais d'identifiants bancaires, de mots de passe ou de données personnelles à un outil non approuvé par votre organisation. Anonymisez : remplacez les noms de clients par des codes (C01, C02), arrondissez si nécessaire, retirez les numéros de compte. Vérifiez les conditions d'utilisation de l'outil et la politique interne. Le cadre du NIST (*AI Risk Management Framework* 1.0 et son profil consacré à l'IA générative, NIST AI 600-1, 2024) recense ces risques : confidentialité, informations erronées, dépendance excessive.
:::
@figure illustrations/fig09_cycle_ia.png|Le cycle de travail avec un assistant d'IA : la décision reste humaine.|68
## 11.3 Les bases du prompt engineering
Le **prompt engineering** est l'art de formuler une demande pour obtenir une réponse exploitable. Comparez « Analyse ma trésorerie » et la demande structurée suivante, qui comporte six éléments : **rôle et contexte** (qui vous êtes, quelle organisation), **tâche** (ce qu'il faut produire), **données** (collées ou jointes, anonymisées), **format** (tableau, colonnes, longueur), **contraintes** (hypothèses, devise, ce qu'il ne faut pas inventer) et **contrôle** (demander d'afficher les calculs et de signaler les incertitudes). Écrivez simplement, comme à un collègue : l'outil n'a pas besoin de jargon informatique.
## 11.4 Dix prompts professionnels prêts à l'emploi
Chaque prompt est présenté selon la même grille. Les données d'exemple sont celles de MAKAO, anonymisées. Les crochets [ ] sont à remplacer par vos informations.
:::prompt 1. Construire un budget de trésorerie
**Objectif** : obtenir un budget mensuel cohérent à partir d'hypothèses. **Données** : solde initial, ventes prévues, profil d'encaissement, dettes et charges datées.
`Tu es assistant d'un responsable financier de PME. Construis un budget de trésorerie mensuel de [janvier] à [juin] en [USD]. Solde initial : [15 000]. Ventes prévues : [95 000 ; 100 000 ; 105 000 ; 100 000 ; 105 000 ; 110 000]. Encaissement des ventes : [20 %] le mois même, [45 %] à M+1, [30 %] à M+2, [5 %] à M+3. Créances existantes : [liste mois/montant]. Décaissements : [liste avec mois et montant]. Présente un tableau : solde initial, encaissements par catégorie, décaissements par catégorie, solde final. Montre le calcul de chaque total. N'invente aucune donnée manquante : signale-la.`
**Exemple** : avec les données de MAKAO, la réponse doit retrouver un solde de -4 750 USD fin janvier. **Résultat attendu** : un tableau mensuel et la liste des hypothèses manquantes. **Vérification** : recalculer un mois à la main ; vérifier que chaque solde final devient le solde initial suivant. **Limites** : l'outil ne connaît ni vos contrats ni vos échéances fiscales ; les hypothèses restent les vôtres.
:::
:::prompt 2. Analyser les retards de paiement
**Objectif** : classer les créances et prioriser les relances. **Données** : liste des factures (code client, montant, échéance), date d'analyse.
`Voici la liste de nos factures clients impayées au [31/12/2025] (clients codés). Calcule pour chaque facture les jours de retard, classe-les en tranches (non échu, 1-30, 31-60, 61-90, plus de 90 jours), totalise par client et par tranche, puis propose un ordre de relance en expliquant tes critères (montant, ancienneté). Affiche les formules Excel qui reproduisent ton calcul. [tableau]`
**Exemple** : le client C01 (30 000 USD dont 3 000 à 31-60 jours) doit sortir parmi les priorités. **Résultat attendu** : une balance âgée et une liste de relance justifiée. **Vérification** : le total des tranches égale le total des factures (126 000 USD) ; contrôler deux lignes au hasard. **Limites** : l'IA ignore les litiges et l'historique de la relation : ajoutez-les vous-même.
:::
:::prompt! 3. Construire un calendrier d'encaissements
**Objectif** : transformer créances et ventes en encaissements datés par semaine. **Données** : créances avec date probable, ventes futures, profil d'encaissement.
`À partir des données ci-dessous, construis un calendrier hebdomadaire des encaissements sur 13 semaines à partir du [lundi 5 janvier 2026]. Hypothèse : les encaissements d'un mois arrivent en quatre parts égales les [5, 12, 19 et 26]. Donne un tableau semaine par semaine (dates de début et de fin, montant, origine) et le total général, qui doit être égal à la somme des données d'entrée sur la période.`
**Exemple** : semaine 1 de MAKAO après relances, 26 500 USD. **Résultat attendu** : 13 lignes datées. **Vérification** : total général cohérent ; aucune date en dehors de la semaine indiquée. **Limites** : les jours fériés et retards bancaires ne sont pas connus de l'outil.
:::
:::prompt 4. Préparer un calendrier de décaissements
**Objectif** : ordonner les paiements selon les priorités. **Données** : engagements (bénéficiaire codé, montant, échéance, nature), trésorerie disponible.
`Voici nos engagements à payer du [5] au [11 janvier] et notre trésorerie disponible de [41 500 USD] sur la semaine. Classe chaque engagement en obligatoire, négociable ou différable selon ces règles : [salaires, impôts, cotisations, loyer et banque obligatoires ; fournisseurs négociables ; investissements et remboursements d'associés différables]. Propose un plan de paiement qui ne dépasse pas la trésorerie disponible, avec les montants à négocier et une justification par ligne. Ne propose jamais de reporter une obligation légale.`
**Exemple** : l'IA doit aboutir à 41 500 USD de paiements au maximum, loyer inclus. **Résultat attendu** : un plan daté et justifié. **Vérification** : somme des paiements au plus égale au disponible ; obligations intégralement payées. **Limites** : la négociation réelle avec chaque fournisseur reste humaine.
:::
:::prompt 5. Analyser les écarts
**Objectif** : expliquer prévu et réalisé. **Données** : tableau prévu/réalisé par catégorie, informations connues sur les événements du mois.
`Voici notre prévu et notre réalisé de trésorerie de [janvier]. Calcule l'écart en valeur et en pourcentage par ligne. Classe chaque écart significatif (plus de [2 %] ou [1 000 USD]) en décalage, volume, anomalie ou imprévu, en t'appuyant uniquement sur les explications fournies : [Palmiers -6 000 reporté ; Clinique +2 000 anticipé ; facture payée deux fois 4 800 ; réparation 1 400]. Indique les écarts que tu ne peux pas expliquer.`
**Résultat attendu** : le tableau 3.4 et ses quatre explications. **Vérification** : écart total = somme des écarts par ligne ; aucune explication inventée. **Limites** : l'IA ne peut pas savoir pourquoi un écart s'est produit si vous ne le lui dites pas.
:::
:::prompt 6. Construire un tableau de bord
**Objectif** : produire la structure d'un tableau de bord d'une page. **Données** : trésorerie, prévisions, créances, dettes, charges fixes.
`À partir des données suivantes, calcule ces indicateurs : trésorerie disponible, couverture en mois de charges fixes, point bas prévisionnel, taux de réalisation des encaissements, DSO, DPO, créances échues de plus de 30 jours. Affiche chaque formule et son résultat. Propose ensuite une mise en page Excel (onglets, colonnes, graphiques recommandés) et des seuils d'alerte, en les présentant comme des propositions à valider.`
**Résultat attendu** : les indicateurs du tableau 8.1. **Vérification** : recalculer DSO et couverture ; vérifier les unités (jours, mois, USD). **Limites** : les seuils proposés doivent être adaptés à votre activité.
:::
:::prompt 7. Préparer un rapport de trésorerie
**Objectif** : rédiger le commentaire mensuel pour la direction ou la banque. **Données** : tableau de bord, causes des écarts, décisions prises.
`Rédige un commentaire de trésorerie de [10] lignes maximum pour la direction, en français simple, selon l'ordre : constat chiffré, causes, risque à venir, décisions avec dates et responsables. Utilise uniquement les chiffres fournis ; n'ajoute aucune donnée. [indicateurs et décisions]`
**Résultat attendu** : un texte proche de l'encadré du chapitre 8. **Vérification** : chaque chiffre du texte figure dans les données ; le ton est factuel. **Limites** : relisez les engagements pris au nom de l'organisation.
:::
:::prompt 8. Identifier les risques financiers
**Objectif** : dresser une liste structurée des risques. **Données** : description de l'activité, concentration clients, devises, financements.
`Voici la description de notre organisation [activité, part du premier client 24 %, devises USD et CDF, découvert de 20 000 USD, emprunt]. Identifie les principaux risques de trésorerie. Pour chacun : description, cause, impact possible en USD (en expliquant le calcul), probabilité estimée (faible, moyenne, forte) et mesure de réponse. Présente un tableau trié par impact.`
**Résultat attendu** : une matrice des risques à compléter. **Vérification** : les impacts reposent sur vos chiffres ; aucun risque majeur connu n'est oublié. **Limites** : l'estimation des probabilités relève de votre jugement.
:::
:::prompt 9. Vérifier la cohérence de données financières
**Objectif** : détecter erreurs et anomalies avant analyse. **Données** : export de paiements ou de factures.
`Contrôle ce tableau de paiements : signale les doublons (même fournisseur, même numéro de facture ou même montant à moins de [30] jours d'intervalle), les montants négatifs ou nuls, les dates hors période, les fournisseurs absents de la liste de référence et les paiements au-dessus de [2 000 USD] sans seconde validation. Donne la liste des lignes concernées et la formule Excel qui permettrait de refaire ce contrôle.`
**Exemple** : la facture MX-1187 payée le 12 et le 25 janvier doit apparaître. **Vérification** : retrouver chaque ligne signalée dans le fichier source. **Limites** : une ligne signalée est un soupçon, pas une preuve.
:::
:::prompt 10. Proposer des scénarios de trésorerie
**Objectif** : simuler l'effet d'un événement. **Données** : prévision de base, événement, hypothèses de chaque scénario.
`Notre prévision de base d'[avril] à [juin] est la suivante : [tableau]. Notre principal client ([24 %] des ventes) nous quitte au [1er avril]. Calcule trois scénarios avec ces hypothèses exactes : [optimiste, réaliste, pessimiste]. Pour chacun, donne le solde de fin de mois et indique le mois du solde le plus bas. Ne modifie aucune autre hypothèse. Propose ensuite cinq mesures d'urgence chiffrées, sans report d'obligations légales.`
**Résultat attendu** : un tableau comparable au tableau 9.2. **Vérification** : refaire un mois du scénario pessimiste dans Excel. **Limites** : le choix des mesures et leur acceptabilité sociale restent des décisions humaines.
:::
:::retenir Synthèse du chapitre
- Le tableur structuré (une saisie, des calculs) reste le socle ; l'IA accélère, elle ne remplace pas.
- Un bon prompt précise contexte, tâche, données, format, contraintes et contrôle.
- Tout résultat d'IA se vérifie : totaux, logique, sources, absence d'invention.
- Données anonymisées, outils approuvés, jamais d'identifiants bancaires.
:::
## QCM du chapitre 11
*Une seule réponse est attendue pour chaque question.*
Q1. Quelle formule totalise les montants de la colonne Montant pour les dates du 5 au 11 janvier (D1 et D2) ?
a) `=SOMME(Montant)`
b) `=SOMME.SI.ENS(Montant;Date;">="&D1;Date;"<="&D2)`
c) `=NB.SI(Date;D1)`
d) `=MIN(Montant)`
Q2. Qu'appelle-t-on une hallucination d'une IA générative ?
a) Une panne du logiciel
b) Une information inventée présentée comme exacte
c) Un refus de répondre
d) Une réponse trop longue
Q3. Quel prompt est le mieux construit ?
a) « Analyse ma trésorerie »
b) « Tu es expert, aide-moi »
c) Un prompt précisant contexte, tâche, données anonymisées, format, contraintes et demande d'afficher les calculs
d) Un prompt contenant les identifiants bancaires pour plus de précision
Q4. L'IA annonce un total d'encaissements de 108 000 USD ; votre fichier donne 106 000 USD. Que faire ?
a) Retenir le chiffre de l'IA
b) Faire la moyenne
c) Rechercher l'origine de l'écart dans les données et les calculs, et corriger
d) Ignorer, l'écart est faible
Q5. Quelle donnée ne doit jamais être transmise à un assistant d'IA non approuvé ?
a) Un profil d'encaissement en pourcentages
b) Des montants de créances anonymisés
c) Les identifiants de connexion à la banque en ligne
d) Une liste de catégories de dépenses
## Corrigé du QCM
**Q1 : b.** SOMME.SI.ENS additionne les montants qui respectent toutes les conditions de dates. NB.SI compte des lignes ; MIN donne le plus petit montant.
**Q2 : b.** Le modèle produit un texte plausible, pas nécessairement vrai : d'où l'obligation de vérifier.
**Q3 : c.** Elle contient les six éléments d'un prompt efficace. La réponse d est une faute grave de sécurité.
**Q4 : c.** Le fichier source vérifié fait foi ; l'écart signale une erreur à comprendre (donnée mal lue, ligne dupliquée).
**Q5 : c.** Les identifiants permettent d'agir sur le compte : ils ne quittent jamais les canaux sécurisés de la banque.
:::action
**Testez un prompt** de ce chapitre sur des données fictives ou anonymisées (par exemple le prompt 2 avec les factures de MAKAO). Vérifiez trois chiffres à la main, notez ce qu'il a fallu préciser et conservez la version améliorée.
:::
