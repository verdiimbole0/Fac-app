# Module 12 — Comptabilité, gestion financière et budgétaire

## 12.1 Mise en situation

Fin mars, à Horizons Partagés. Esther, l'unique comptable, a devant elle 340 pièces du mois : factures papier, photos de reçus envoyées par messagerie depuis les bureaux de terrain, relevés bancaires en PDF, états de caisse manuscrits. Elle doit tout saisir, imputer à l'un des cinq bailleurs et à la bonne ligne budgétaire, rapprocher la banque, mettre à jour le suivi budgétaire et préparer, pour le 15 avril, deux rapports financiers dans deux formats différents. L'auditeur arrive en juin.

Ibrahim, le responsable financier, a lu qu'« il existe des outils d'IA qui traitent les factures automatiquement ». Il se demande ce que cela veut dire concrètement, ce qu'il faut acheter, ce qui changera pour Esther, et surtout ce qui restera sous leur contrôle.

## 12.2 Problématique

La fonction financière d'une ASBL combine trois exigences : **exactitude** (chaque écriture est juste et justifiée), **traçabilité** (chaque montant peut être relié à une pièce et à une autorisation) et **redevabilité multiple** (bailleurs, organes de gouvernance, autorités, auditeurs, public). Elle est aussi l'une des plus chargées en tâches répétitives : réception, saisie, imputation, rapprochements, consolidation, mise en forme. L'IA peut alléger fortement ces tâches — à condition de ne jamais affaiblir le contrôle interne ni la piste d'audit.

## 12.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. organiser la fonction comptable et la gestion des pièces justificatives pour la rendre compatible avec l'automatisation ;
2. décrire, étape par étape, le traitement assisté d'une facture, de sa réception à l'archivage, en distinguant le rôle de l'IA, du logiciel et du professionnel ;
3. mettre en œuvre une extraction de données et une imputation assistées, avec leurs contrôles ;
4. réaliser et contrôler un rapprochement bancaire et un suivi de caisse ;
5. suivre un budget par projet et par bailleur, distinguer fonds affectés et non affectés, et analyser les écarts ;
6. préparer la trésorerie, le reporting et les audits ;
7. situer les référentiels comptables applicables.

## 12.4 Notions et définitions

- **Pièce justificative** : document qui prouve la réalité et le montant d'une opération (facture, reçu, contrat, bon de livraison, état de paie).
- **Imputation comptable** : affectation d'une opération à un compte du plan comptable.
- **Imputation analytique ou budgétaire** : affectation d'une opération à un projet, un bailleur, une ligne budgétaire, une activité.
- **Écriture comptable** : enregistrement d'une opération au débit et au crédit de comptes.
- **Rapprochement bancaire** : explication des écarts entre le solde comptable du compte bancaire et le solde du relevé.
- **Fonds affectés (ou restreints)** : ressources dont l'utilisation est limitée par le donateur à un objet, une période ou un projet.
- **Fonds non affectés** : ressources utilisables librement pour la mission (cotisations, dons non fléchés, certaines subventions de fonctionnement).
- **Piste d'audit** : capacité à remonter de chaque montant des états financiers jusqu'à la pièce et à l'autorisation, et inversement.
- **Seuil de confiance** : niveau de certitude au-dessous duquel une proposition de l'IA est automatiquement soumise à un examen renforcé.

> **⚖️ Adaptation réglementaire** — Il n'existe pas de référentiel comptable universel pour les organisations à but non lucratif. Selon les pays, s'appliquent un plan comptable national, un référentiel spécifique aux entités à but non lucratif ou aux associations, des règles particulières (par exemple, à titre d'illustration et à vérifier selon votre situation : le système comptable des entités à but non lucratif dans l'espace OHADA, le règlement de l'ANC applicable aux personnes morales de droit privé à but non lucratif en France, le *Charities SORP* au Royaume-Uni, les normes du FASB pour les *not-for-profit entities* aux États-Unis). En octobre 2025, un référentiel international volontaire dédié, l'*International Non-Profit Accounting Standard* (INPAS), a été lancé à l'issue du projet IFR4NPO ; il ne s'impose que s'il est adopté par une juridiction ou exigé par un bailleur. Les numéros de comptes cités dans ce module sont donc des **exemples** : utilisez votre plan comptable.

## 12.5 Explications détaillées

### Organisation comptable : les préalables à toute automatisation

Avant d'automatiser, quatre fondations doivent être en place :

1. **Un plan comptable et un plan analytique** stables : comptes, codes projets, codes bailleurs, lignes budgétaires, avec une **table de correspondance** entre les lignes du budget de chaque bailleur et vos comptes.
2. **Un manuel de procédures financières** à jour : seuils d'autorisation, circuit de validation, pièces exigées par type de dépense.
3. **Une séparation des tâches** : la personne qui saisit n'est pas celle qui approuve le paiement ; celle qui tient la caisse n'est pas celle qui la contrôle.
4. **Un plan de classement** des pièces (module 7), numérique et papier.

### Le traitement d'une facture en 14 étapes

![Figure 12.1 — Traitement d'une facture en 14 étapes : qui fait quoi ?](03_ILLUSTRATIONS/figures/fig_12_1.svg)

Suivons une facture réelle (fictive) d'un bout à l'autre.

*La pièce :* facture n° F-2026-0412 de « Papeterie du Centre », datée du 12 mars 2026, adressée à la Fondation Horizons Partagés : 40 rames de papier à 6,50 UM = 260 UM ; 20 cartouches d'encre à 22,00 UM = 440 UM ; **total 700 UM** (l'organisation n'est pas assujettie à une taxe sur la valeur ajoutée dans cet exemple). Référence du bon de commande : BC-2026-077. Matériel destiné aux sessions de formation des agents de santé du projet PRJ-SANTE-07.

**Étape 1 — Réception.** La facture arrive par courriel au bureau de terrain.
*Logiciel :* une adresse électronique dédiée (par exemple factures@…) centralise toutes les factures. *Humain :* les factures remises en main propre sont numérisées le jour même. *Règle :* aucune facture ne circule en dehors de ce canal.

**Étape 2 — Numérisation ou photographie.** Le PDF est conservé tel quel ; une facture papier est scannée ou photographiée avec une application de numérisation (document à plat, lumière suffisante, quatre coins visibles).
*Contrôle :* lisibilité de tous les montants avant envoi.

**Étape 3 — Extraction des informations.**
*IA :* un outil d'extraction (OCR et modèle d'extraction) lit la pièce et propose les champs : fournisseur, numéro, date, montant total, lignes (désignation, quantité, prix unitaire, montant), référence du bon de commande, coordonnées bancaires éventuelles. Il associe à chaque champ un niveau de confiance.
*Logiciel :* les champs extraits sont stockés dans un enregistrement relié à l'image de la pièce.

**Étape 4 — Contrôle des données extraites.**
*Logiciel :* contrôles automatiques simples — somme des lignes = total (260 + 440 = 700 ✓) ; date plausible ; fournisseur existant dans le fichier fournisseurs ; numéro de facture non déjà enregistré pour ce fournisseur.
*Humain :* l'assistante administrative compare les champs à faible confiance avec l'image (ici, le « 6,50 » a été lu « 6,60 » avec une confiance de 71 % : elle corrige). Toute modification des **coordonnées bancaires** d'un fournisseur est bloquée et transmise au responsable financier (risque de fraude au changement de RIB).

**Étape 5 — Identification de la nature de la dépense.**
*IA :* à partir des libellés (« rames de papier », « cartouches d'encre ») et de l'historique, le système propose la nature « fournitures de bureau et consommables de formation ».

**Étape 6 — Proposition d'imputation.**
*IA :* proposition d'imputation comptable (compte de charges « Fournitures de bureau » de votre plan comptable) et analytique (projet PRJ-SANTE-07, activité 1.1 « Sessions de formation », ligne budgétaire 2 « Activités »), en s'appuyant sur la référence du bon de commande BC-2026-077, qui portait déjà ces codes. Confiance : 94 %.

**Étape 7 — Vérification que le compte proposé est approprié.**
*Humain :* la comptable vérifie : la nature de la dépense correspond-elle au compte ? Le projet et la ligne correspondent-ils au bon de commande approuvé ? La dépense est-elle éligible selon la convention du bailleur (période, nature, plafond) ? *Règle :* toute proposition avec une confiance inférieure au seuil (par exemple 85 %) ou concernant un compte sensible (immobilisations, salaires, avances) est examinée ligne par ligne.

**Étape 8 — Rapprochement avec le budget concerné.**
*Logiciel :* le système calcule le disponible de la ligne : budget annuel de la ligne 2 du projet = 28 400 UM ; engagé et réalisé à date = 19 650 UM ; disponible avant cette facture = 8 750 UM ; après = 8 050 UM. Aucun dépassement.
*Logiciel :* rapprochement à trois voies — commande BC-2026-077 (700 UM), bon de livraison signé (40 rames et 20 cartouches reçues), facture (700 UM) : concordance.

**Étape 9 — Détection d'anomalies.**
*IA et règles :* le système signale : « Une facture du même fournisseur, d'un montant identique (700 UM), numéro F-2026-0411, a été enregistrée le 26 février. Doublon possible. »
*Humain :* la comptable vérifie : les deux factures correspondent à deux commandes distinctes (BC-2026-061 et BC-2026-077), deux livraisons signées. Ce n'est pas un doublon. Elle consigne l'explication dans le commentaire de l'alerte.

**Étape 10 — Soumission au responsable habilité.**
*Logiciel :* le workflow transmet automatiquement la dépense au responsable habilité selon le seuil (ici, moins de 1 000 UM : coordinatrice du projet) avec la pièce, la proposition d'imputation, le contrôle budgétaire et les alertes traitées.
*Humain :* la coordinatrice approuve dans l'outil. L'approbation est horodatée et nominative.

**Étape 11 — Validation et enregistrement de l'écriture.**
*Logiciel :* l'écriture est générée (débit du compte de charges « Fournitures de bureau » 700 UM ; crédit du compte fournisseur « Papeterie du Centre » 700 UM ; axes analytiques PRJ-SANTE-07 / 1.1 / ligne 2).
*Humain :* la comptable valide l'écriture. Une écriture n'est jamais comptabilisée sans validation humaine. Au paiement, une seconde écriture soldera le compte fournisseur par le compte bancaire, après approbation du paiement selon la procédure.

**Étape 12 — Actualisation des tableaux de bord et du suivi budgétaire.**
*Logiciel :* le tableau de bord du projet est mis à jour (exécution de la ligne 2 : 20 350 / 28 400, soit 71,7 %).

**Étape 13 — Conservation des pièces et de la piste d'audit.**
*Logiciel :* la pièce est archivée sous le nom `2026-03-12_FACT_PapeterieDuCentre_F-2026-0412.pdf`, liée à l'écriture, avec l'historique : qui a extrait, corrigé, proposé, approuvé, validé, et quand. La facture papier d'origine est classée selon les règles de conservation applicables.

**Étape 14 — Traitement des erreurs et cas exceptionnels.**
*Humain :* une procédure écrite couvre : pièce illisible (demande d'un duplicata) ; facture sans bon de commande (régularisation selon la procédure, signalement) ; dépense inéligible (réimputation sur fonds non affectés, après décision) ; avoir ou annulation ; facture en devise étrangère (taux de conversion selon la politique de l'organisation) ; erreur d'imputation découverte après clôture (écriture de correction documentée, jamais de suppression).

| Étape | IA | Logiciel | Professionnel |
|---|---|---|---|
| 1. Réception | — | Boîte dédiée | Numérise les pièces papier |
| 2. Numérisation | — | Application de numérisation | Vérifie la lisibilité |
| 3. Extraction | Lit et propose les champs, avec confiance | Stocke champs + image | — |
| 4. Contrôle des données | — | Contrôles arithmétiques et de cohérence | Corrige les champs à faible confiance ; bloque les changements de RIB |
| 5. Nature | Propose la nature | — | — |
| 6. Imputation | Propose comptes et axes | — | — |
| 7. Vérification du compte | — | — | **Vérifie et décide** |
| 8. Budget | — | Calcule le disponible ; rapprochement 3 voies | Examine les dépassements |
| 9. Anomalies | Signale doublons, inhabituels | Applique les règles | **Instruit et conclut** |
| 10. Approbation | — | Workflow | **Approuve** (personne habilitée) |
| 11. Écriture | — | Génère l'écriture | **Valide** |
| 12. Tableaux de bord | — | Met à jour | Analyse |
| 13. Archivage | Indexe | Archive et trace | Classe le papier |
| 14. Exceptions | — | — | **Traite selon procédure** |

> **🔎 À retenir** — L'IA **propose et signale** ; le logiciel **enregistre, calcule et trace** ; le professionnel **vérifie, décide et valide**. Ce partage des rôles est la condition d'une automatisation compatible avec l'audit.

### Caisse et banque

**La caisse** est le point le plus sensible du contrôle interne des petites structures. Règles : plafond d'encaisse ; pièces pour chaque sortie ; arrêté de caisse quotidien ou hebdomadaire signé par le caissier et contrôlé par une autre personne ; comptage inopiné. L'IA peut aider à **numériser et extraire** les reçus de caisse et à **signaler** des sorties inhabituelles (montants ronds répétés, sorties juste sous le seuil d'autorisation) ; elle ne remplace pas le comptage physique.

**Le rapprochement bancaire** est un contrôle clé. *Exemple (fictif) au 31 mars :*

| | Montant (UM) |
|---|---|
| Solde du relevé bancaire | 48 250 |
| − Chèque n° 1182 émis, non encore encaissé | − 1 500 |
| + Remise de dépôt du 31/03, non encore créditée | + 800 |
| **= Solde bancaire rapproché** | **47 550** |
| Solde comptable du compte banque | 46 980 |
| − Frais bancaires de mars, non comptabilisés | − 35 |
| + Virement reçu (cotisations), non comptabilisé | + 605 |
| **= Solde comptable rapproché** | **47 550** |
| **Écart résiduel** | **0** |

Les logiciels comptables et bancaires proposent souvent un **rapprochement automatique** (appariement des lignes du relevé et des écritures par montant, date et libellé). L'IA améliore l'appariement des libellés ambigus. Le comptable traite les lignes non appariées, et le rapprochement est **revu et signé** par une autre personne (responsable financier).

### Budget, financements affectés et non affectés, dépenses par projet

Une ASBL multi-bailleurs doit suivre ses dépenses selon **trois axes simultanés** : nature (plan comptable), projet/activité, et bailleur/ligne budgétaire du bailleur. Les **fonds affectés** ne peuvent financer que l'objet prévu ; les dépenses inéligibles doivent être couvertes par des **fonds non affectés**, qu'il faut donc préserver et suivre.

La **table de correspondance** est l'outil central : pour chaque bailleur, elle relie chaque ligne de son budget à vos comptes et codes analytiques. Elle permet de produire automatiquement le rapport de chaque bailleur dans son format à partir d'une seule comptabilité.

### Écarts budgétaires

![Figure 12.2 — Tableau de bord fictif : exécution budgétaire par ligne](03_ILLUSTRATIONS/figures/fig_12_2.svg)

Au 30 septembre (75 % de l'année écoulée), le tableau de bord du programme pluriannuel de santé communautaire (PRG-SANTE, qui regroupe plusieurs projets) fait apparaître (en milliers d'UM) :

| Ligne | Budget | Réalisé | Taux | Lecture |
|---|---|---|---|---|
| Personnel | 420 | 318 | 75,7 % | Conforme au prorata temporel |
| Déplacements | 60 | 71 | 118,3 % | **Dépassement** : à expliquer et à régulariser (réallocation autorisée ? fonds non affectés ?) |
| Formation | 85 | 35 | 41,2 % | **Sous-exécution** : retard d'activité ? risque de non-réalisation et de restitution des fonds |
| Équipements | 140 | 126 | 90,0 % | Avance sur le prorata : vérifier que les achats restants sont couverts |
| Communication | 25 | 26 | 104,0 % | Léger dépassement : vérifier le seuil de flexibilité de la convention |
| Frais de structure | 70 | 52 | 74,3 % | Conforme |

L'analyse des écarts combine **calcul** (fait par le tableur ou le logiciel) et **explication** (qui relève des équipes). L'IA est utile pour rédiger une première analyse à partir des taux calculés et des commentaires des responsables (fiche P12.3), et pour comparer les écarts aux règles de flexibilité budgétaire de la convention.

### Trésorerie

Le plan de trésorerie prévoit, mois par mois, les encaissements (tranches des bailleurs, dons, cotisations) et les décaissements (salaires, fournisseurs, activités). Les ASBL sont exposées aux **retards de versement** des bailleurs. Un tableau simple sur douze mois glissants, mis à jour chaque mois, suffit souvent. L'IA peut aider à construire le modèle et à rédiger des scénarios (« et si la deuxième tranche arrive avec trois mois de retard ? ») ; la prévision chiffrée repose sur vos données et vos calendriers contractuels.

### Reporting

Les rapports financiers aux bailleurs exigent : le bon format, la bonne période, le bon taux de change, les bonnes lignes, la réconciliation avec la comptabilité. L'automatisation consiste à produire les rapports **à partir de la comptabilité** via la table de correspondance, plutôt que de les ressaisir. L'IA peut rédiger la partie narrative du rapport financier (explication des écarts), à partir des chiffres validés.

### Préparation des audits

Une comptabilité dont chaque écriture est liée à sa pièce et à son approbation transforme la préparation de l'audit : la liste des pièces demandées par l'auditeur est extraite en quelques minutes. L'IA peut aider à préparer le dossier permanent (statuts, conventions, PV, procédures), à vérifier la complétude des pièces d'un échantillon et à rédiger des réponses aux observations, toujours relues par le responsable financier. Le module 13 approfondit l'audit.

## 12.6 Application métier : automatiser le traitement des pièces à Horizons Partagés

**A. Contexte.** 340 pièces par mois, une comptable, quatre bureaux, cinq bailleurs, logiciel comptable existant.
**B. Problème.** Saisie et imputation manuelles chronophages ; retards de reporting ; pièces difficiles à retrouver.
**C. Symptômes.** Environ 35 heures de saisie par mois ; rapports en retard de trois semaines ; 11 pièces sur 60 non retrouvées lors du dernier audit.
**D. Causes profondes.** Canaux de réception multiples ; ressaisie ; absence de lien pièce-écriture ; une seule personne formée.
**E. Processus actuel.** Voir module 5, figure 5.1.
**F. Points de faiblesse.** Ressaisie, classement papier, approbations hors système, aucune détection de doublons.
**G. Résultat recherché.** Temps de traitement par pièce divisé par deux ; 100 % des pièces liées aux écritures ; clôture mensuelle à J+10 ; zéro paiement en double.
**H. Pertinence de l'IA.** Forte pour l'extraction et la proposition d'imputation (documents variés, libellés libres) ; complémentaire de règles automatiques (contrôles arithmétiques, seuils, doublons).
**I. Alternatives sans IA.** Saisie directe dans un formulaire numérique par le demandeur ; centralisation des pièces ; classement normalisé — à mettre en place de toute façon.
**J. Solution recommandée.** Canal unique de réception + outil d'extraction de documents relié au logiciel comptable (ou fonction intégrée au logiciel) + workflow d'approbation + archivage lié.
**K. Niveau.** Intermédiaire.
**L. Outils nécessaires.** Logiciel comptable acceptant l'import ou disposant d'une fonction de capture de documents ; outil d'extraction (intégré ou externe, évalué selon le module 9) ; workflow d'approbation ; stockage documentaire.
**M. Étapes détaillées de mise en œuvre.**

1. Mettre à jour le manuel de procédures et la délégation de signature (module 5).
2. Finaliser le plan analytique et les tables de correspondance par bailleur.
3. Créer le canal unique de réception et la règle de nommage.
4. Sélectionner l'outil (module 9) ; vérifier le contrat (données orange, coordonnées bancaires sensibles).
5. Paramétrer : champs à extraire, contrôles automatiques, seuil de confiance, comptes sensibles, règles de doublons, circuit d'approbation par seuil.
6. Tester sur 100 pièces de l'année précédente déjà comptabilisées : comparer les propositions de l'IA aux imputations réelles et mesurer le taux d'exactitude.
7. Pilote de deux mois sur un bureau, en parallèle du processus actuel.
8. Ajuster les règles ; former les utilisateurs ; documenter.
9. Déploiement aux quatre bureaux.
10. Revue mensuelle des indicateurs et des corrections.

**N. Prompts et automatisation.** Fiches P12.1 à P12.3 ci-dessous (utilisables au niveau Débutant avec un assistant validé, ou comme spécifications pour paramétrer un outil).
**O. Exemple de résultat.** Voir le déroulé de la facture F-2026-0412 ci-dessus.
**P. Méthode de vérification.** Test initial sur 100 pièces connues ; pendant le pilote, contrôle de 100 % des propositions ; ensuite, contrôle de toutes les propositions sous le seuil de confiance et d'un échantillon aléatoire de 10 % des autres.
**Q. Contrôles humains.** Vérification des champs à faible confiance ; vérification du compte (étape 7) ; instruction des anomalies ; approbation par la personne habilitée ; validation des écritures ; revue mensuelle du rapprochement bancaire par le responsable financier.
**R. Risques et précautions.** Erreurs d'extraction ; imputation erronée sur un bailleur (dépense inéligible) ; biais d'automatisation (validation « en masse ») ; fraude par fausse facture ou faux changement de RIB ; données bancaires des fournisseurs exposées. Précautions : seuils, échantillonnage, blocage des modifications de RIB, outil validé.
**S. Coûts et maintenance.** Abonnement à l'outil d'extraction (selon volume), paramétrage, formation, temps de contrôle, mise à jour des tables de correspondance à chaque nouvelle convention.
**T. Indicateurs de performance.** Temps moyen de traitement par pièce ; taux de propositions d'imputation acceptées sans modification ; taux d'erreurs détectées en revue ; délai de clôture ; nombre de pièces non retrouvées lors de l'audit ; nombre d'alertes de doublons et taux de faux positifs.
**U. Amélioration continue.** Analyse mensuelle des corrections pour améliorer les règles et les données d'historique ; revue annuelle du paramétrage avec l'auditeur.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Prérequis | Coûts | Limites |
|---|---|---|---|---|---|
| **Débutant** | Pièces centralisées et nommées ; tableur de saisie avec listes déroulantes (comptes, projets, lignes) ; assistant autorisé pour extraire les champs d'une pièce **sans données personnelles** et proposer une imputation à partir du plan fourni ; contrôle humain systématique | Tableur, application de numérisation, assistant validé | Plan comptable et analytique ; formation | Faibles | Pièce par pièce ; pas d'intégration ; vigilance sur les données (coordonnées bancaires, noms de personnes physiques) |
| **Intermédiaire** | Fonction de capture intégrée au logiciel comptable ou outil d'extraction relié ; workflow d'approbation ; rapprochement bancaire automatique ; tableaux de bord | Logiciel comptable en ligne, outil d'extraction, workflow | Paramétrage, tables de correspondance | Abonnements, paramétrage | Dépendance aux fournisseurs ; qualité des historiques |
| **Avancé** | ERP intégrant achats, comptabilité, budget, trésorerie ; extraction et imputation automatiques avec apprentissage sur l'historique ; contrôles continus ; reporting bailleurs automatisé ; assistant RAG sur les conventions et procédures | ERP, API, entrepôt de données, RAG | Équipe financière et SI structurée | Élevés | Complexité, coût de maintenance, gouvernance des données |

## 12.7 Prompts prêts à l'emploi

### Fiche P12.1 — Extraire les données d'une facture

**A. Titre.** Extraction structurée d'une pièce justificative.

**B. Objectif.** Obtenir les champs d'une facture dans un format prêt à importer, avec signalement des incertitudes.

**C. Contexte d'utilisation.** Comptabilité, niveau Débutant ; ou test d'un outil avant paramétrage.

**D. Données nécessaires.** L'image ou le PDF de la facture (outil autorisé pour données orange) ; la liste des champs attendus.

**E. Prompt complet.**

```text
Contexte : je suis comptable d'une ASBL. Je dois enregistrer la
facture jointe.
Tâche : extrais les informations de la facture.
Résultat attendu : un tableau avec les champs suivants : fournisseur ;
numéro de facture ; date (AAAA-MM-JJ) ; date d'échéance ; référence de
commande ; devise ; pour chaque ligne : désignation, quantité, prix
unitaire, montant ; sous-total ; taxes (taux et montant, ou « aucune
taxe mentionnée ») ; total.
Pour chaque champ, ajoute une colonne « certitude » (élevée / moyenne
/ faible) et une colonne « remarque ».
Contrôles à effectuer et à signaler : somme des lignes = sous-total ;
sous-total + taxes = total ; présence de coordonnées bancaires (si
oui, écris seulement « coordonnées bancaires présentes », sans les
recopier).
Limites : si un champ est illisible ou absent, écris « ILLISIBLE » ou
« ABSENT ». Ne devine aucun chiffre.
```

**F. Instructions d'utilisation.** Joignez la pièce ; collez le tableau dans le tableur de saisie ; corrigez les champs à certitude faible ou moyenne en les comparant à l'image.

**G. Résultat attendu.** Un tableau de champs, des certitudes, les résultats des contrôles arithmétiques.

**H. Exemple d'application (illustratif).** Pour la facture F-2026-0412, le tableau obtenu indique « prix unitaire ligne 1 : 6,60 — certitude moyenne — remarque : le 5 et le 6 sont peu distincts » et « contrôle : 40 × 6,60 = 264 ≠ 260 indiqué ; incohérence ». La comptable vérifie l'image : 6,50. Le contrôle arithmétique a permis de détecter l'erreur de lecture.

**I. Méthode de vérification.** Comparez chaque champ à certitude non élevée à l'image ; recalculez les totaux dans le tableur ; vérifiez que le numéro de facture n'existe pas déjà pour ce fournisseur.

**J. Précautions.** Ne pas soumettre de pièces contenant des données personnelles sensibles (notes de frais avec informations médicales, bulletins de paie) à un outil non validé. Ne jamais recopier des coordonnées bancaires dans un outil externe.

**K. Amélioration.** Si l'outil confond prix unitaires et montants : « Pour chaque ligne, vérifie que quantité × prix unitaire = montant de la ligne et signale toute différence. »

### Fiche P12.2 — Proposer une imputation comptable et analytique

**A. Titre.** Proposition d'imputation justifiée.

**B. Objectif.** Obtenir une proposition d'imputation conforme **à votre** plan comptable et **à votre** plan analytique, avec justification et niveau de confiance.

**C. Contexte d'utilisation.** Saisie comptable ; formation d'une nouvelle recrue ; cas ambigus.

**D. Données nécessaires.** Extrait du plan comptable (comptes de charges utilisés) ; liste des projets, activités et lignes budgétaires ; règles d'éligibilité pertinentes de la convention ; données extraites de la pièce ; information du bon de commande.

**E. Prompt complet.**

```text
Contexte : comptabilité d'une ASBL multi-bailleurs.
Plan comptable (extrait) : <plan>[COMPTES ET INTITULÉS]</plan>
Plan analytique : <analytique>[PROJETS / ACTIVITÉS / LIGNES]</analytique>
Règles d'éligibilité applicables : <regles>[EXTRAITS DE CONVENTION]</regles>
Pièce : <piece>[CHAMPS EXTRAITS + RÉFÉRENCE DE COMMANDE + OBJET]</piece>
Tâche : propose l'imputation de cette dépense.
Résultat attendu : tableau « Ligne de la pièce | Compte proposé
(numéro et intitulé, choisi UNIQUEMENT dans le plan fourni) |
Projet | Activité | Ligne budgétaire | Justification | Confiance
(élevée/moyenne/faible) | Point d'éligibilité à vérifier ».
Règles : si aucun compte du plan ne convient, écris « AUCUN COMPTE
ADAPTÉ » ; si l'affectation à un projet est incertaine, propose
« À DÉTERMINER » et explique pourquoi ; ne crée aucun compte.
```

**F. Instructions d'utilisation.** Fournissez uniquement les extraits pertinents du plan (pas le plan entier si l'outil est limité). Reportez la proposition dans le logiciel après vérification.

**G. Résultat attendu.** Une proposition par ligne de facture, justifiée, avec points de vigilance.

**H. Exemple d'application (illustratif).** Proposition obtenue : « Ligne 1 et 2 — compte "Fournitures de bureau" — PRJ-SANTE-07 / 1.1 / ligne 2 — justification : bon de commande BC-2026-077 codé sur l'activité 1.1 ; consommables pour sessions de formation — confiance élevée — vérifier : la convention autorise les consommables de formation sur la ligne Activités (art. 6.2 fourni) ».

**I. Méthode de vérification.** Vérifiez que le compte existe dans votre plan et correspond à la nature ; que le codage analytique correspond au bon de commande approuvé ; que la règle d'éligibilité citée figure bien dans la convention.

**J. Précautions.** Données orange. La décision d'imputation reste celle de la comptable.

**K. Amélioration.** Pour un usage récurrent, ajoutez 10 exemples d'imputations validées (« exemples guidés ») afin d'aligner les propositions sur vos pratiques.

### Fiche P12.3 — Analyse narrative des écarts budgétaires

**A. Titre.** Note d'analyse des écarts budgétaires.

**B. Objectif.** Rédiger une analyse claire des écarts à partir de taux déjà calculés et des explications des responsables.

**C. Contexte d'utilisation.** Comité de direction mensuel ; rapport financier intermédiaire.

**D. Données nécessaires.** Tableau budget/réalisé/taux (calculé au tableur) ; prorata temporel ; commentaires des responsables d'activité ; règles de flexibilité budgétaire de la convention.

**E. Prompt complet.**

```text
Contexte : suivi budgétaire du projet [CODE], au [DATE], soit [X] %
de la période écoulée.
Données : <tableau>[LIGNE | BUDGET | RÉALISÉ | TAUX]</tableau>
<commentaires>[EXPLICATIONS DES RESPONSABLES]</commentaires>
<flexibilite>[RÈGLE : ex. réallocation autorisée jusqu'à 10 % par ligne
sans accord préalable]</flexibilite>
Tâche : rédige une note d'analyse des écarts.
Résultat attendu :
1. Synthèse en 3 phrases.
2. Pour chaque ligne dont le taux s'écarte de plus de [15] points du
   prorata : écart, explication (selon les commentaires ; sinon
   [EXPLICATION À OBTENIR]), conformité à la règle de flexibilité,
   action proposée.
3. Risques pour la fin de période (sous-exécution, dépassement,
   restitution de fonds).
4. Décisions à soumettre à la direction.
Règles : n'effectue aucun nouveau calcul ; utilise uniquement les
chiffres fournis.
```

**F. Instructions d'utilisation.** Calculez taux et écarts au tableur ; recueillez les commentaires des responsables avant d'utiliser la fiche.

**G. Résultat attendu.** Une note de une page, factuelle, avec actions et décisions proposées.

**H. Exemple d'application (illustratif).** Pour les données du tableau de la section 12.5, la note propose notamment : « Déplacements : 118,3 % à 75 % de la période. Dépassement de 11 000 UM sur un budget de 60 000 UM, soit 18,3 % de la ligne, supérieur au seuil de flexibilité de 10 % : accord préalable du bailleur nécessaire ou couverture par fonds non affectés. Décision à soumettre à la direction. »

**I. Méthode de vérification.** Vérifiez chaque chiffre repris ; recalculez les écarts cités (71 − 60 = 11 ; 11 / 60 = 18,3 %) ; vérifiez la règle de flexibilité dans la convention.

**J. Précautions.** Données orange.

**K. Amélioration.** « Ajoute une projection de fin de période pour chaque ligne au rythme actuel (calcul : réalisé / taux de période écoulée) et signale les lignes qui dépasseraient 100 %. » *(Vérifiez ces projections au tableur.)*

## 12.8 Résultats attendus

Pièces centralisées et liées aux écritures ; propositions d'imputation contrôlées ; rapprochements bancaires mensuels revus ; suivi budgétaire multi-axes à jour ; rapports produits à partir de la comptabilité ; dossier d'audit préparé en continu.

## 12.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** — Validation des écritures ; approbation des dépenses et des paiements par les personnes habilitées ; vérification de l'éligibilité ; toute modification de coordonnées bancaires de fournisseurs (vérifiée par un second canal) ; revue et signature des rapprochements bancaires ; comptage physique de la caisse ; arrêté des comptes et rapports financiers. L'IA ne valide, n'approuve et ne paie jamais.

## 12.10 Risques et erreurs à éviter

- Automatiser avant d'avoir stabilisé le plan analytique et les procédures.
- Valider en masse des propositions sans les lire (biais d'automatisation).
- Laisser l'outil modifier les données de référence (fournisseurs, RIB).
- Supprimer des écritures au lieu de passer des écritures de correction.
- Produire les rapports bailleurs par ressaisie au lieu de les dériver de la comptabilité.
- Confier des calculs financiers à un modèle de langage.
- Appliquer un plan comptable national comme s'il était universel.

## 12.11 Exercice pratique

**Consigne (3 heures).**

1. Prenez trois factures non sensibles de votre organisation. Appliquez la fiche P12.1, puis comparez champ par champ avec la pièce. Calculez le taux de champs exacts.
2. Appliquez la fiche P12.2 avec votre plan comptable. Comparez aux imputations réellement passées.
3. Réalisez le rapprochement bancaire suivant et trouvez l'écart : solde du relevé 12 400 ; chèque émis non encaissé 950 ; dépôt non crédité 300 ; solde comptable 11 820 ; frais bancaires non comptabilisés 20 ; virement reçu non comptabilisé ? (à trouver).
4. Rédigez la procédure de traitement de deux cas exceptionnels de l'étape 14.

**Éléments de correction.** (3) Solde bancaire rapproché = 12 400 − 950 + 300 = 11 750. Solde comptable rapproché = 11 820 − 20 + X = 11 750, d'où X = − 50 : il ne peut s'agir d'un virement **reçu** (qui augmenterait le solde) ; l'écart de 50 correspond à une sortie non comptabilisée (par exemple un prélèvement) ou à une erreur à rechercher. Cet exercice montre qu'un rapprochement ne se « force » pas : l'écart doit être expliqué par une pièce. (1, 2) Le taux d'exactitude mesuré fonde la décision d'utiliser ou non l'outil et le niveau de contrôle. (4) Les procédures précisent le déclencheur, les actions, les responsables et la trace documentaire.

## 12.12 Synthèse

- L'automatisation comptable repose sur des fondations : plans comptable et analytique, procédures, séparation des tâches, classement.
- Pour chaque pièce, l'IA propose et signale, le logiciel enregistre et trace, le professionnel vérifie et décide.
- Les contrôles clés restent humains : vérification du compte, approbation, validation, rapprochements, caisse.
- Le suivi multi-axes et les tables de correspondance permettent de produire les rapports de chaque bailleur à partir d'une seule comptabilité.
- Il n'existe pas de référentiel comptable universel : adaptez-vous au droit applicable.

## 12.13 QCM — Module 12

**Q1.** (une seule réponse) Dans le traitement assisté d'une facture, le rôle de l'IA est principalement de :

a) valider l'écriture comptable.
b) approuver le paiement.
c) signer le rapprochement bancaire.
d) proposer des champs, des imputations et signaler des anomalies.

**Q2.** (une ou plusieurs réponses) Quelles étapes relèvent impérativement d'une décision humaine ?

a) Vérification que le compte proposé est approprié.
b) Approbation par la personne habilitée.
c) Validation de l'écriture.
d) Calcul du disponible budgétaire.

**Q3.** (une seule réponse) Le rapprochement à trois voies compare :

a) budget, réalisé et prévision.
b) commande, bon de livraison et facture.
c) banque, caisse et grand livre.
d) trois devis.

**Q4.** (une seule réponse) Une demande de modification des coordonnées bancaires d'un fournisseur reçue par courriel doit :

a) être bloquée et vérifiée par un second canal par le responsable financier.
b) être appliquée immédiatement par l'outil.
c) être ignorée.
d) être traitée par l'IA.

**Q5.** (une seule réponse) Dans l'exemple du module, le solde rapproché au 31 mars est :

a) 46 980
b) 48 250
c) 47 515
d) 47 550

**Q6.** (une ou plusieurs réponses) Les fonds affectés :

a) ne peuvent financer que l'objet prévu par le donateur.
b) peuvent couvrir toute dépense de l'organisation.
c) exigent un suivi distinct.
d) peuvent devoir être restitués en cas de non-utilisation conforme.

**Q7.** (mise en situation — une seule réponse) L'outil signale un doublon possible : même fournisseur, même montant, deux numéros de facture différents. Que faites-vous ?

a) Supprimer la seconde facture.
b) Vérifier les bons de commande et de livraison avant de conclure, et documenter la conclusion.
c) Payer les deux sans vérification.
d) Désactiver l'alerte.

**Q8.** (mise en situation — une seule réponse) Une ligne « Déplacements » atteint 118 % de son budget à 75 % de la période. Première action ?

a) Analyser l'écart, vérifier la règle de flexibilité de la convention et soumettre une décision à la direction.
b) Réimputer discrètement l'excédent sur une autre ligne.
c) Attendre la fin du projet.
d) Supprimer des écritures.

**Q9.** (une seule réponse) Concernant les référentiels comptables des ASBL :

a) un plan comptable national unique s'applique dans tous les pays.
b) les normes IFRS s'appliquent obligatoirement à toutes les ASBL.
c) il n'existe aucune règle comptable pour les ASBL.
d) les règles dépendent de la juridiction ; un référentiel international volontaire (INPAS) existe depuis 2025.

**Q10.** (une ou plusieurs réponses) Indicateurs pertinents pour suivre l'automatisation du traitement des pièces :

a) temps moyen de traitement par pièce.
b) taux de propositions d'imputation acceptées sans modification.
c) délai de clôture mensuelle.
d) nombre de logiciels installés.

## 12.14 Corrigé détaillé — Module 12

**Q1 : d.** L'IA propose et signale ; elle ne valide ni n'approuve.

**Q2 : a, b, c.** Le calcul du disponible (d) est réalisé par le logiciel, l'humain en tirant les conséquences.

**Q3 : b.** Commande, livraison, facture : ce contrôle prévient les paiements de biens non commandés ou non reçus.

**Q4 : a.** C'est un schéma de fraude fréquent ; la vérification par un second canal (appel au contact habituel connu) est indispensable.

**Q5 : d.** 48 250 − 1 500 + 800 = 47 550, et 46 980 − 35 + 605 = 47 550.

**Q6 : a, c, d.** Les fonds affectés ne couvrent pas n'importe quelle dépense (b).

**Q7 : b.** On instruit avant de conclure ; dans l'exemple, il s'agissait de deux commandes distinctes.

**Q8 : a.** Le dépassement est analysé au regard de la convention ; une réimputation non autorisée (b) serait une irrégularité.

**Q9 : d.** Les obligations sont nationales ; INPAS est volontaire sauf adoption ou exigence d'un bailleur.

**Q10 : a, b, c.** Le nombre de logiciels (d) ne mesure pas la performance.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- COSO. (2013). *Internal Control — Integrated Framework*.
- International Non-Profit Reporting Foundation (INPRF) / projet IFR4NPO (CIPFA et Humentum). (2025). *International Non-Profit Accounting Standard (INPAS)*.
