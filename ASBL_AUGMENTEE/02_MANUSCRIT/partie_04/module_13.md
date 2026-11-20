# Module 13 : Audit, contrôle interne, gestion des risques et conformité

## 13.1 Mise en situation

Au Réseau Citoyen pour l'Eau (RCE), Fatou est contrôleuse interne. Le comité d'audit lui demande une revue des dépenses du premier trimestre du projet « Eau et assainissement » et du siège. Elle dispose de l'extraction du grand livre (40 dépenses, 31 890,50 UM), du fichier fournisseurs, des pièces numérisées et du manuel de procédures. Avec la méthode classique (sélection d'un échantillon, vérification des pièces) elle aurait examiné une quinzaine d'opérations. Avec des tests analytiques assistés, elle peut examiner **toute la population**, puis concentrer son temps d'expert sur les opérations les plus risquées.

Ce module suit sa démarche, du fichier brut à la feuille de travail et aux recommandations. Les tests présentés ont été **réellement exécutés** sur le fichier fictif fourni en annexe (`depenses_RCE_T1_2026.csv`) à l'aide d'un script reproductible (`tests_audit.py`) ; les résultats chiffrés de ce module en sont issus. Les conclusions des vérifications de pièces et d'entretiens, elles, relèvent du scénario pédagogique.

## 13.2 Problématique

Les ASBL sont exposées à des risques de fraude, d'erreur et de non-conformité, souvent avec des fonctions de contrôle réduites. Dans l'étude mondiale de l'ACFE sur 1 921 cas de fraude interne survenus entre janvier 2022 et septembre 2023 dans 138 pays et territoires, 43 % des fraudes ont été détectées grâce à un signalement : davantage que par tout autre moyen (ACFE, 2024) : les contrôles formels, à eux seuls, en détectent une part bien moindre. L'IA et l'analyse de données permettent d'étendre les contrôles à l'ensemble des opérations, mais elles produisent aussi des faux positifs et ne remplacent ni le jugement professionnel, ni les dispositifs de signalement, ni le scepticisme de l'auditeur.

## 13.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. évaluer l'environnement de contrôle et cartographier les risques ;
2. concevoir et exécuter des tests analytiques sur un fichier de dépenses (doublons, fractionnement, fournisseurs, pièces, séparation des tâches) ;
3. interpréter les résultats, distinguer anomalies et faux positifs, et conduire les vérifications ;
4. documenter les travaux dans une feuille de travail ;
5. formuler des constats et des recommandations ;
6. suivre les recommandations et construire un tableau de bord des risques ;
7. utiliser l'IA dans le respect des normes professionnelles et de la confidentialité.

## 13.4 Notions et définitions

- **Contrôle interne** : processus mis en œuvre par la gouvernance, la direction et le personnel, destiné à fournir une assurance raisonnable quant à la réalisation des objectifs opérationnels, de reporting et de conformité (COSO, 2013).
- **Audit interne** : activité indépendante et objective qui donne une assurance et des conseils ; ses normes de référence au niveau international sont les *Global Internal Audit Standards* de l'IIA, en vigueur depuis le 9 janvier 2025.
- **Audit externe** : examen des états financiers par un auditeur indépendant, selon les normes et les obligations légales applicables.
- **Risque inhérent / résiduel** : risque avant / après prise en compte des mesures de maîtrise.
- **Test analytique** : examen de données pour repérer des tendances, des ruptures ou des opérations atypiques.
- **Faux positif** : opération signalée par un test qui se révèle normale après examen.
- **Feuille de travail** : document qui consigne l'objectif, la méthode, les éléments examinés, les constats et les conclusions d'un travail d'audit.
- **Constat** : écart entre la situation constatée et le critère attendu, avec sa cause, ses conséquences et une recommandation.

## 13.5 Explications détaillées

### L'environnement de contrôle

L'environnement de contrôle est la base des autres composantes : intégrité et valeurs affichées par la direction, rôle effectif du conseil (et d'un éventuel comité d'audit), structure et délégations, compétences, responsabilisation. Des tests analytiques sophistiqués ne compensent pas un environnement où les dirigeants contournent les procédures.

### La cartographie des risques

![Figure 13.2 : Carte thermique des risques](03_ILLUSTRATIONS/figures/fig_13_2.svg)

Pour chaque processus (achats, paiements, avances, caisse, paie, subventions), on identifie les risques, on les évalue (probabilité × impact, de 1 à 5), on recense les contrôles existants, puis on estime le risque résiduel. L'IA aide à **proposer des risques** à partir de la description d'un processus et à **mettre en forme** la cartographie ; l'évaluation relève des responsables et de l'auditeur.

| Risque | Processus | P | I | Score | Contrôles existants | Évaluation |
|---|---|---|---|---|---|---|
| R1 Paiements en double | Paiements | 3 | 4 | 12 | Aucun contrôle automatique | Insuffisant |
| R2 Avances non justifiées | Avances | 4 | 3 | 12 | Relance manuelle irrégulière | Insuffisant |
| R3 Fractionnement des achats | Achats | 2 | 4 | 8 | Seuils écrits, non surveillés | Partiel |
| R4 Fuite de données via outils d'IA | Transverse | 3 | 5 | 15 | Aucune règle écrite | Insuffisant |
| R5 Dépendance à un fournisseur | Achats | 2 | 3 | 6 | Mise en concurrence au-delà du seuil | Partiel |

### Les tests analytiques

![Figure 13.1 : Entonnoir des tests analytiques assistés](03_ILLUSTRATIONS/figures/fig_13_1.svg)

| Test | Règle | Risque visé |
|---|---|---|
| T1 Doublons | Même fournisseur, même montant, même libellé | Paiement en double |
| T2 Fournisseur hors base | Code fournisseur absent du fichier fournisseurs | Fournisseur fictif |
| T3 Pièce manquante | Pièce jointe absente | Dépense non justifiée |
| T4 Auto-approbation | Demandeur = approbateur | Séparation des tâches |
| T5 Fractionnement | ≥ 2 dépenses sous le seuil, même fournisseur, dans un délai de 7 jours, cumul au-dessus du seuil | Contournement des seuils |
| T6 Montants ronds | Montant ≥ seuil et multiple de 500 | Estimation, facture de complaisance |
| T7 Week-end | Date un samedi ou un dimanche | Opération atypique (faible pertinence sur le terrain) |
| T8 Sans bon de commande | Montant ≥ seuil sans bon de commande | Non-respect de la procédure |
| T9 Libellé imprécis | Libellé contenant « divers », « prestation de services » | Opacité |

Ces tests reposent sur des **règles explicites** : ils relèvent davantage de l'analyse de données que de l'IA au sens strict. L'IA intervient pour : écrire les formules ou le script ; rapprocher des libellés semblables mais non identiques ; regrouper des fournisseurs aux noms proches (« Quincaillerie Delta » et « Quincaillerie Delta SARL ») ; résumer les résultats ; rédiger la feuille de travail et les recommandations.

### Résultats sur la population de 40 dépenses

Seuil d'autorisation et de bon de commande retenu dans le cas : 1 000 UM.

| Test | Nombre signalé | Opérations |
|---|---|---|
| T1 Doublons | 8 | D01/D13 ; D03/D39 ; D06/D35 ; D15/D31 |
| T2 Fournisseur hors base | 2 | D24, D33 |
| T3 Pièce manquante | 4 | D18, D24, D31, D33 |
| T4 Auto-approbation | 10 | D06, D12, D16, D17, D18, D20, D24, D27, D33, D35 |
| T5 Fractionnement | 3 | D16, D17, D18 (cumul 2 970 UM en 3 jours) |
| T6 Montants ronds | 2 | D24, D33 |
| T7 Week-end | 12 | D08, D09, D12, D19, D20, D23, D24, D27, D33, D36, D39, D40 |
| T8 Sans bon de commande | 2 | D24, D33 |
| T9 Libellé imprécis | 2 | D24, D33 |
| **Opérations signalées par au moins un test** | **22** | sur 40 |

Vingt-deux opérations sur quarante : c'est beaucoup trop pour tout examiner en détail, et beaucoup sont des **faux positifs**. Le test T7 (week-end) est peu discriminant pour une organisation qui mène des activités de terrain le samedi. Les « doublons » D03/D39 (hôtel, 270 UM) concernent deux missions de projets et de dates différents ; D06/D35 et D15/D31 correspondent à des dépenses récurrentes de même montant (carburant, hébergement). L'auditrice **priorise** donc :

- **priorité 1** : opérations cumulant plusieurs alertes fortes (T2, T3, T8, T9) : D24, D33 ;
- **priorité 2** : doublon portant sur le **même bon de commande** (D01/D13, BC-101) ; fractionnement avec pièce manquante (D16, D17, D18) ;
- **priorité 3** : pièce manquante isolée (D31) ;
- **traitement global** : auto-approbations récurrentes (T4) : faiblesse de conception du contrôle, à examiner au niveau de la procédure plutôt qu'opération par opération.

Soit **8 opérations prioritaires** examinées en détail (D01, D13, D16, D17, D18, D24, D31, D33).

### Vérification des pièces et conclusions (scénario)

| Opération | Vérifications réalisées | Conclusion |
|---|---|---|
| D01 / D13 | Les deux paiements de 1 240 UM se réfèrent au même bon de commande BC-101 et à la même facture ; un seul bon de livraison | **Constat 1 : paiement en double** de 1 240 UM. Demande de remboursement au fournisseur |
| D16 / D17 / D18 | Trois achats de fournitures à 990, 985 et 995 UM en trois jours, payés en caisse, approuvés par la demandeuse ; pas de pièce pour D18 | **Constat 2 : fractionnement** contournant le seuil de 1 000 UM et la mise en concurrence ; auto-approbation ; une dépense non justifiée |
| D24 / D33 | Fournisseur « Services Généraux KB » absent du fichier fournisseurs ; aucune pièce ; libellé imprécis ; montants ronds (3 000 et 2 500 UM) ; demandeur et approbateur identiques (coordinateur EAU-03) | **Constat 3 : dépenses non justifiées de 5 500 UM, indices de fraude.** L'auditrice ne conclut pas seule : elle applique la politique de lutte contre la fraude (information confidentielle de la direction et du président du comité d'audit, préservation des preuves, pas d'entretien avec l'intéressé avant décision) |
| D31 | Facture d'hôtel retrouvée dans la messagerie de l'agent, non jointe | Régularisée : pièce archivée. Pas de constat, mais point d'attention sur la collecte des pièces de mission |
| T4 (global) | La procédure autorise le logisticien à approuver ses propres achats de carburant en caisse | **Faiblesse de contrôle** : séparation des tâches insuffisante |

> **🛑 Contrôle humain obligatoire** : Une alerte n'est pas une preuve. Aucune conclusion de fraude, aucun nom, aucune sanction ne découle d'un résultat automatique. Les soupçons de fraude suivent la politique de l'organisation et, le cas échéant, les obligations légales, sous la responsabilité de personnes habilitées.

### La feuille de travail

Une feuille de travail comporte : référence ; objectif ; population et source des données ; méthode (tests, critères, seuils) ; résultats ; éléments examinés ; constats ; conclusion ; préparé par / revu par, avec dates. L'IA peut produire un premier projet à partir des résultats et des notes ; l'auditrice le complète et le signe ; un pair ou le responsable de l'audit le revoit.

### Constats et recommandations

Un constat bien rédigé suit le schéma **critère, constat, cause, conséquence, recommandation**. Exemple pour le constat 2 :

- *Critère* : manuel de procédures, § 5.3 : tout achat d'un montant cumulé supérieur à 1 000 UM auprès d'un même fournisseur pour un même besoin fait l'objet d'une consultation d'au moins trois fournisseurs et d'une approbation de la direction.
- *Constat* : trois achats de fournitures de bureau (990, 985 et 995 UM ; total 2 970 UM) ont été effectués auprès du même fournisseur du 3 au 5 février, payés en caisse et approuvés par la demandeuse ; la pièce de l'un d'eux est manquante.
- *Cause* : absence de contrôle du cumul par fournisseur ; possibilité d'auto-approbation en caisse.
- *Conséquence* : contournement de la mise en concurrence et de l'approbation ; risque de surcoût et de dépenses non justifiées ; risque de non-éligibilité auprès du bailleur.
- *Recommandation* : (1) interdire l'auto-approbation ; (2) mettre en place une alerte mensuelle de cumul par fournisseur ; (3) obtenir la pièce manquante ou reclasser la dépense sur fonds non affectés ; (4) rappeler la procédure aux équipes. Responsable : directrice administrative et financière. Échéance : 30 juin.

### Suivi des recommandations et tableau de bord des risques

Les recommandations sont inscrites dans un **registre de suivi** (annexe 20) : numéro, constat, recommandation, priorité, responsable, échéance, état, preuve de mise en œuvre. Le tableau de bord présenté au comité d'audit montre : nombre de recommandations par priorité et par état ; recommandations échues ; évolution des scores de risque ; indicateurs de contrôle (taux de pièces manquantes, nombre de doublons détectés, nombre d'auto-approbations).

### Analyse de données en continu

Au niveau avancé, les tests deviennent des **contrôles continus** exécutés chaque mois (voire chaque jour) sur l'ERP, avec des alertes transmises aux responsables. Il faut alors gérer le taux de faux positifs (sinon les alertes sont ignorées), documenter et tester les règles, et protéger l'accès aux résultats, qui peuvent être sensibles.

### L'IA et les normes professionnelles

L'usage de l'IA par l'auditeur doit respecter la confidentialité des données (outil autorisé, minimisation), la traçabilité (documenter dans la feuille de travail l'outil utilisé et la manière dont ses résultats ont été vérifiés), et le jugement professionnel. Les conclusions d'audit restent celles de l'auditeur.

## 13.6 Application métier : revue des dépenses du premier trimestre au RCE

**A. Contexte.** Grande ONG, ERP, comité d'audit, contrôleuse interne unique.
**B. Problème.** Revue limitée à de petits échantillons ; anomalies détectées tardivement.
**C. Symptômes.** Remarques récurrentes des auditeurs externes ; recommandations non suivies.
**D. Causes profondes.** Pas de tests sur la population complète ; pas de registre des recommandations ; faiblesses de conception des contrôles.
**E. Processus actuel.** Échantillonnage manuel annuel.
**F. Faiblesses.** Couverture faible ; pas de détection des schémas (fractionnement, fournisseurs fictifs).
**G. Résultat recherché.** Couverture de 100 % des opérations par des tests ciblés ; constats documentés ; recommandations suivies.
**H. Pertinence de l'IA.** Pour écrire et documenter les tests, rapprocher des libellés et des noms proches, rédiger les feuilles de travail et les recommandations. Les tests eux-mêmes sont des règles.
**I. Alternatives sans IA.** Les mêmes tests dans un tableur (filtres, tableaux croisés, `NB.SI.ENS`) : parfaitement possible pour de petits volumes.
**J. Solution recommandée.** Bibliothèque de tests standardisés, exécutés trimestriellement, avec priorisation et feuille de travail type.
**K. Niveau.** Débutant (tableur) à Intermédiaire (script ou outil d'analyse) ; Avancé pour le contrôle continu.
**L. Outils.** Tableur ou outil d'analyse de données ; assistant autorisé pour données orange ; registre des recommandations.
**M. Étapes détaillées.**

1. Définir l'objectif et la population (période, entités, comptes).
2. Extraire les données de l'ERP et le fichier fournisseurs ; contrôler l'exhaustivité (total de l'extraction = total du grand livre).
3. Pseudonymiser si nécessaire (les noms de personnes ne sont pas utiles pour les tests ; utiliser les fonctions).
4. Exécuter les tests T1 à T9 (fiche P13.1).
5. Prioriser les opérations signalées.
6. Examiner les pièces, interroger les responsables, documenter.
7. Rédiger la feuille de travail (fiche P13.2).
8. Rédiger les constats et recommandations (fiche P13.3) ; les discuter avec les responsables.
9. Présenter au comité d'audit ; inscrire au registre de suivi.
10. Relancer et vérifier la mise en œuvre ; réexécuter les tests au trimestre suivant.

**N. Prompts et automatisation.** Fiches P13.1 à P13.3 ; script reproductible en annexe.
**O. Exemple de résultat.** Tableaux ci-dessus.
**P. Méthode de vérification.** Exhaustivité de l'extraction ; recalcul indépendant de quelques résultats ; revue de la feuille de travail par un pair.
**Q. Contrôles humains.** Priorisation, examen des pièces, conclusions, qualification des faits, recommandations, traitement des soupçons de fraude.
**R. Risques.** Faux positifs nombreux ; faux négatifs (un test ne détecte que ce qu'il cherche) ; atteinte à la réputation de personnes ; confidentialité.
**S. Coûts et maintenance.** Tableur : temps. Outil d'analyse : licence. Maintenance de la bibliothèque de tests et des seuils.
**T. Indicateurs.** Couverture (% des opérations testées) ; taux de faux positifs par test ; nombre de constats ; montants concernés ; taux de mise en œuvre des recommandations à l'échéance.
**U. Amélioration continue.** Supprimer ou affiner les tests peu discriminants (ici T7) ; ajouter des tests selon les nouveaux risques ; mesurer l'évolution trimestrielle.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Tests T1 à T9 dans un tableur avec formules proposées par l'IA ; feuille de travail type ; registre des recommandations | Tableur, assistant | Faibles | Volumes limités ; risque d'erreur de formule : tester sur des cas connus |
| Intermédiaire | Script ou outil d'analyse de données exécutant une bibliothèque de tests ; rapprochement de noms proches ; tableaux de bord | Outil d'analyse, assistant professionnel | Licences modestes | Compétences en analyse de données |
| Avancé | Contrôle continu sur l'ERP, alertes automatiques, gestion des cas, tableau de bord des risques intégré, IA pour la détection d'anomalies statistiques | ERP, plateforme d'audit, outil de GRC | Élevés | Gestion des faux positifs ; gouvernance des accès |

## 13.7 Prompts prêts à l'emploi

### Fiche P13.1 : Concevoir les tests analytiques d'un fichier de dépenses

**A. Titre.** Bibliothèque de tests analytiques pour un tableur.

**B. Objectif.** Obtenir les formules ou les étapes pour exécuter des tests ciblés sur toute une population de dépenses.

**C. Contexte d'utilisation.** Audit interne, contrôle de gestion, revue de fin de période.

**D. Données nécessaires.** Structure du fichier (colonnes) ; seuils de la procédure ; quelques lignes **fictives ou pseudonymisées** d'exemple.

**E. Prompt complet.**

```text
Contexte : je réalise une revue des dépenses d'une ASBL dans
[TABLEUR, LANGUE]. Colonnes : [LISTE]. Seuil d'autorisation et de bon
de commande : [SEUIL]. Un fichier fournisseurs séparé contient la
colonne code_fournisseur.
Tâche : propose une bibliothèque de tests analytiques.
Pour chaque test : objectif ; risque visé ; règle précise ; formule
exacte (colonne d'alerte « 1 si anomalie, 0 sinon ») avec la cellule
de départ ; limites et faux positifs probables.
Tests demandés : doublons (fournisseur + montant + libellé) ;
fournisseur absent du fichier fournisseurs ; pièce manquante ;
demandeur = approbateur ; fractionnement (au moins 2 dépenses sous le
seuil, même fournisseur, dans un délai de 7 jours, cumul au-dessus du
seuil) ; montants ronds au-dessus du seuil ; dépenses au-dessus du
seuil sans bon de commande ; libellés imprécis.
Ajoute une colonne « score » = somme pondérée des alertes, en
proposant des poids justifiés.
Limites : n'utilise que les colonnes listées ; signale les tests qui
nécessitent un tri préalable.
```

**F. Instructions d'utilisation.** Appliquez les formules sur une copie ; **testez chaque formule sur des lignes dont vous connaissez la réponse** (par exemple en créant volontairement un doublon) avant de l'appliquer à la population.

**G. Résultat attendu.** Une colonne d'alerte par test, un score de priorité, une liste de faux positifs probables.

**H. Exemple d'application.** Appliquée au fichier du RCE, la bibliothèque produit les résultats présentés en section 13.5 (22 opérations signalées). La formule de fractionnement proposée doit être vérifiée avec soin : c'est la plus sujette aux erreurs de fenêtre de dates.

**I. Méthode de vérification.** Contrôlez le total de la population ; recalculez manuellement deux alertes par test ; comparez avec un second moyen (tableau croisé par fournisseur et par semaine pour le fractionnement).

**J. Précautions.** Les fichiers de dépenses sont orange ; noms de personnes physiques à remplacer par des fonctions.

**K. Amélioration.** « Le test week-end produit trop de faux positifs pour nos activités de terrain. Propose un test plus discriminant pour les opérations atypiques (par exemple, dépenses saisies hors des jours d'activité planifiés). »

### Fiche P13.2 : Rédiger une feuille de travail

**A. Titre.** Projet de feuille de travail d'audit.

**B. Objectif.** Documenter les travaux de façon complète et revue.

**C. Contexte d'utilisation.** Après l'exécution des tests et l'examen des pièces.

**D. Données nécessaires.** Objectif ; population ; méthode ; résultats chiffrés ; notes d'examen (pseudonymisées).

**E. Prompt complet.**

```text
Contexte : audit interne de [PROCESSUS], période [PÉRIODE].
Données : <objectif>…</objectif> <population>…</population>
<methode>…</methode> <resultats>…</resultats> <notes>…</notes>
Tâche : rédige la feuille de travail.
Rubriques : Référence | Objectif | Population et source (avec contrôle
d'exhaustivité) | Méthode et critères | Résultats des tests (tableau) |
Priorisation et justification | Éléments examinés | Constats
(critère, constat, cause, conséquence) | Conclusion | Limites des
travaux | Préparé par / date | Revu par / date (laisser vide).
Règles : n'ajoute aucun fait absent des notes ; distingue faits
constatés et hypothèses ; n'emploie pas le mot « fraude » : écris
« indices nécessitant une investigation » lorsque c'est le cas.
```

**F. Instructions d'utilisation.** Remplacez les noms par des fonctions ; complétez et signez ; faites revoir.

**G. Résultat attendu.** Une feuille de travail complète, structurée, prudente dans sa formulation.

**H. Exemple d'application (illustratif).** La rubrique « Limites des travaux » obtenue précise : « Les tests ne couvrent que les dépenses comptabilisées ; une dépense non enregistrée ou une facture fictive cohérente avec la procédure ne serait pas détectée. »

**I. Méthode de vérification.** Chaque chiffre est pointé sur les résultats ; chaque fait sur les notes ; revue par un pair.

**J. Précautions.** Données orange, voire rouges en cas d'indices de fraude : outil validé exclusivement, ou rédaction manuelle.

**K. Amélioration.** « Ajoute un tableau de traçabilité "Constat → pièces examinées → référence d'archivage". »

### Fiche P13.3 : Formuler des recommandations actionnables

**A. Titre.** Recommandations SMART à partir des constats.

**B. Objectif.** Transformer des constats en recommandations claires, priorisées, attribuées et vérifiables.

**C. Contexte d'utilisation.** Rapport d'audit, revue de contrôle interne.

**D. Données nécessaires.** Constats (critère, constat, cause, conséquence) ; organigramme fonctionnel ; contraintes de ressources.

**E. Prompt complet.**

```text
Tâche : pour chaque constat ci-dessous, propose 1 à 3 recommandations.
Format : tableau « Constat | Recommandation (verbe d'action) |
Cause traitée | Priorité (élevée/moyenne/faible) et justification |
Responsable proposé (fonction) | Échéance proposée | Preuve de mise en
œuvre attendue | Coût ou effort estimé (faible/moyen/élevé) ».
Données : <constats>[CONSTATS]</constats>
<organisation>[FONCTIONS DISPONIBLES]</organisation>
Règles : chaque recommandation traite la cause, pas seulement le
symptôme ; privilégie des mesures proportionnées aux moyens d'une
ASBL de [TAILLE] ; signale si une recommandation exige une décision
du conseil d'administration.
```

**F. Instructions d'utilisation.** Discutez les propositions avec les responsables avant finalisation ; inscrivez les recommandations retenues au registre.

**G. Résultat attendu.** Un tableau de recommandations prêtes à être discutées.

**H. Exemple d'application (illustratif).** Pour la faiblesse T4, la proposition obtenue : « Modifier la procédure de caisse : approbation des dépenses de carburant par le coordinateur de projet ; alerte mensuelle automatique des auto-approbations (responsable : DAF) échéance : 31 mai : preuve : procédure révisée et rapport d'alertes de juin ».

**I. Méthode de vérification.** Chaque recommandation est-elle reliée à une cause ? réaliste ? vérifiable ?

**J. Précautions.** Ne pas désigner de personnes nommément dans le document de travail.

**K. Amélioration.** « Regroupe les recommandations par processus et indique les gains rapides réalisables en moins de 30 jours. »

## 13.8 Résultats attendus

Couverture complète de la population ; priorisation documentée ; trois constats et une faiblesse de contrôle étayés ; recommandations suivies ; tableau de bord des risques pour le comité d'audit.

## 13.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Priorisation, examen des pièces, conclusions, rédaction finale des constats, traitement des soupçons de fraude et suivi des recommandations relèvent du jugement de l'auditeur et des personnes habilitées. Les résultats des tests ne sont jamais diffusés comme des accusations.

## 13.10 Risques et erreurs à éviter

- Présenter des alertes comme des fraudes.
- Noyer les responsables sous des alertes non priorisées.
- Oublier les faux négatifs : ce que les tests ne cherchent pas, ils ne le trouvent pas.
- Ne pas contrôler l'exhaustivité de l'extraction.
- Utiliser un outil non autorisé pour des données d'audit.
- Formuler des recommandations sans responsable ni échéance.

## 13.11 Exercice pratique

**Consigne (3 heures).** À partir du fichier `depenses_RCE_T1_2026.csv` (annexes) : (1) reproduisez les tests T1, T2, T3 et T5 dans un tableur ; (2) comparez vos résultats au tableau de la section 13.5 ; (3) proposez un test remplaçant T7 ; (4) rédigez le constat complet pour D01/D13 (critère, constat, cause, conséquence, recommandation).

**Éléments de correction.** Vous devez retrouver : T1 = 8 opérations (4 paires) ; T2 = D24, D33 ; T3 = D18, D24, D31, D33 ; T5 = D16, D17, D18. Si votre test de doublons ne trouve que D01/D13, vous avez probablement inclus la date ou la référence de commande dans la clé : c'est un test plus strict (moins de faux positifs), défendable si vous le justifiez. Le constat D01/D13 relie le double paiement à l'absence de contrôle du numéro de facture et du bon de commande avant paiement, et recommande un contrôle bloquant dans le logiciel.

## 13.12 Synthèse

- Le contrôle interne s'apprécie d'abord par son environnement ; la cartographie des risques oriente les travaux.
- Les tests analytiques couvrent toute la population ; ils produisent des alertes, dont beaucoup sont des faux positifs.
- La priorisation, l'examen des pièces et les conclusions relèvent du jugement professionnel.
- Les constats suivent le schéma critère, constat, cause, conséquence, recommandation.
- Les recommandations sont suivies dans un registre et un tableau de bord des risques.

## 13.13 QCM : Module 13

**Q1.** (une seule réponse) Les *Global Internal Audit Standards* de l'IIA sont en vigueur depuis :

a) le 9 janvier 2025.
b) le 1er janvier 2013.
c) le 1er août 2024.
d) le 18 décembre 2023.

**Q2.** (une seule réponse) Un faux positif est :

a) une fraude non détectée.
b) un test qui n'a rien trouvé.
c) une erreur de saisie.
d) une opération signalée qui se révèle normale après examen.

**Q3.** (une ou plusieurs réponses) Quels tests visent un risque de fournisseur fictif ?

a) Fournisseur absent du fichier fournisseurs.
b) Libellé imprécis.
c) Montants ronds élevés.
d) Date de week-end uniquement.

**Q4.** (une seule réponse) Dans le cas du RCE, combien d'opérations ont été signalées par au moins un test ?

a) 8
b) 22
c) 12
d) 40

**Q5.** (une seule réponse) Le fractionnement consiste à :

a) découper un achat en plusieurs dépenses sous le seuil pour contourner une règle.
b) payer une facture en plusieurs fois selon le contrat.
c) répartir une dépense entre plusieurs projets.
d) arrondir les montants.

**Q6.** (une ou plusieurs réponses) Un constat d'audit complet comprend :

a) le critère.
b) la cause.
c) la conséquence.
d) le nom de la personne fautive.

**Q7.** (mise en situation, une seule réponse) Deux dépenses de 5 500 UM au total, sans pièce, auprès d'un fournisseur absent de la base, approuvées par le demandeur. Que fait l'auditrice ?

a) Elle conclut à une fraude dans son rapport.
b) Elle interroge immédiatement le demandeur devant l'équipe.
c) Elle applique la politique de lutte contre la fraude : information confidentielle des personnes habilitées, préservation des preuves, pas de conclusion hâtive.
d) Elle ignore l'alerte faute de preuve.

**Q8.** (mise en situation, une seule réponse) Le test « week-end » signale 12 opérations, presque toutes liées à des activités de terrain normales. Que faites-vous ?

a) Vous examinez quand même les 12 en détail chaque trimestre.
b) Vous documentez sa faible pertinence et le remplacez ou l'affinez.
c) Vous le gardez pour avoir plus d'alertes.
d) Vous supprimez toutes les opérations du week-end.

**Q9.** (une seule réponse) Avant d'exécuter des tests, il faut vérifier :

a) l'exhaustivité de l'extraction (total = grand livre).
b) la couleur du fichier.
c) le nombre de colonnes.
d) le nom de l'outil d'IA.

**Q10.** (une ou plusieurs réponses) Le rôle de l'IA dans cette démarche peut être de :

a) écrire les formules ou le script des tests.
b) rapprocher des noms de fournisseurs proches.
c) rédiger un projet de feuille de travail.
d) conclure sur la culpabilité d'une personne.

## 13.14 Corrigé détaillé : Module 13

**Q1 : a.** Publiées le 9 janvier 2024, elles sont en vigueur depuis le 9 janvier 2025.

**Q2 : d.** D'où l'importance de la priorisation et de l'examen.

**Q3 : a, b, c.** La date de week-end seule (d) n'est pas un indicateur de fournisseur fictif.

**Q4 : b.** 22 opérations sur 40, dont de nombreux faux positifs ; 8 ont été examinées en priorité.

**Q5 : a.** C'est un contournement des seuils d'autorisation ou de mise en concurrence.

**Q6 : a, b, c.** Le constat porte sur des faits et des processus, pas sur la désignation de coupables.

**Q7 : c.** Les indices de fraude exigent une procédure rigoureuse et confidentielle.

**Q8 : b.** Un test peu discriminant use l'attention et doit être amélioré.

**Q9 : a.** Sans exhaustivité, la couverture « 100 % » est illusoire.

**Q10 : a, b, c.** La conclusion (d) relève de l'auditeur et des instances habilitées.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Association of Certified Fraud Examiners. (2024). *Occupational Fraud 2024: A Report to the Nations*.
- COSO. (2013). *Internal Control : Integrated Framework*.
- The Institute of Internal Auditors. (2024). *Global Internal Audit Standards*.
