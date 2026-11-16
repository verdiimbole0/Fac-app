## Chapitre 29 — Claude appliqué à l'audit financier, à l'audit opérationnel et au contrôle interne

### A. Mise en situation professionnelle

Michel Lwamba, responsable de l'audit interne de MCC, doit présenter au comité d'audit le plan d'audit 2027, conduire la mission sur le processus achats (voir chapitre 11), et faire le point sur les 64 recommandations émises depuis trois ans, dont une partie n'a jamais été mise en œuvre. Son équipe compte trois auditeurs. Il voit dans Claude un moyen de multiplier la capacité d'analyse de l'équipe — à condition de préserver l'indépendance, le scepticisme professionnel et la qualité des preuves.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Utiliser** Claude pour préparer une mission d'audit (programme, demandes de documents, check-lists).
2. **Réaliser** des tests sur données (analyses de population) par calculs programmés et documentés.
3. **Rédiger** des constats structurés à partir de preuves validées.
4. **Suivre** les recommandations et produire un tableau de bord fiable.
5. **Identifier** les exigences propres à l'audit (preuve, indépendance, confidentialité, traçabilité) dans l'usage de l'IA.

### C. Comprendre avant de pratiquer — Profil du métier

*Tableau 29.1 — Profil de l'auditeur (interne ou externe) et du contrôleur interne.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Évaluer les risques et l'efficacité du contrôle interne ; formuler des constats et des recommandations ; rendre compte aux organes de gouvernance |
| Tâches quotidiennes | Planification, entretiens, tests, analyses de données, papiers de travail, rédaction, suivi |
| Difficultés | Volumes de transactions ; délais ; documentation des preuves ; rédaction ; suivi des recommandations |
| Documents | Procédures, matrices des risques et contrôles, délégations de pouvoirs, pièces justificatives, papiers de travail, rapports |
| Données | Extractions de l'ERP (achats, paiements, paie, stocks), journaux d'accès, registres |
| Livrables | Plan d'audit, programmes de travail, papiers de travail, rapports, tableaux de suivi |
| Assistables par Claude | Programmes et check-lists ; tests de population par code ; synthèses de procédures ; rédaction de constats ; suivi des recommandations ; préparation des comités |
| Limites | Jugement d'audit, conclusions, opinion, appréciation de la fraude, relations avec les audités, indépendance |

::: retenir
En audit, **ce qui n'est pas documenté n'est pas fait**. Toute analyse réalisée avec Claude doit être reproductible : données sources, prompt, code exécuté, résultat, contrôles de l'auditeur, conclusion de l'auditeur.
:::

![Figure 29.1 — Le cycle d'audit interne assisté par Claude : le jugement d'audit et l'opinion restent ceux de l'auditeur. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig29_1_cycle_audit.png){width=100%}

### D. Démonstration guidée — Cas d'usage

#### Cas d'usage 29.1 — Tests de population sur les achats

**1. Problème.** Tester l'ensemble des commandes de la période (et non un échantillon) contre les règles de la procédure d'achat.

**2. Méthode habituelle.** Échantillonnage manuel ; outils d'analyse de données réservés aux spécialistes.

**3. Contribution de Claude.** Écriture et exécution de tests par programme sur 100 % de la population, avec code conservé pour le dossier.

**4. Données.** `MCC_bons_de_commande.csv` ; procédure d'achat ; matrice des délégations (seuil chef de service : 10 000 USD).

**5. Procédure.** Définir les tests à partir de la procédure → exécution → revue des exceptions → demande de pièces → conclusion de l'auditeur.

**6. Prompt.**

```text
[C] Audit interne de MCC, mission « processus achats », période janvier 2025 – juin 2026.
[A] Exécute les tests suivants sur toute la population et documente-les comme un papier de travail.
[D] MCC_bons_de_commande.csv ; seuil d'approbation du chef de service : 10 000 USD.
[R] Exécution de code ; aucune conclusion sur la fraude ; chaque exception est un « point à investiguer ».
Tests :
T1 Fractionnement : mêmes fournisseur et date, somme > 10 000 USD, chaque commande < 10 000 USD.
T2 Doublons : fournisseur, article, quantité, prix et date identiques.
T3 Prix anormaux : écart > 15 % à la médiane de l'article (même unité).
T4 Montants ronds ≥ 5 000 USD (multiples de 100) pour des prestations de service.
[E] Pour chaque test : objectif, population, critère, code, nombre d'exceptions, liste des exceptions.
En fin : tableau de synthèse et liste des pièces à demander.
```

**7. Échanges successifs.** « Pour T1, ajoute les dates de réception et le nom du demandeur s'ils sont disponibles » ; « Rédige la demande de pièces au service achats. »

**8. Exemple de résultat (fictif).** T1 : 1 exception (3 × 9 800 USD au même prestataire le 14/03/2026) ; T2 : 1 exception (BC-60999 / BC-60012) ; T3 et T4 : exceptions à examiner.

**9. Contrôle.** L'auditeur relit le code, refait un test à la main (par exemple T2 avec un filtre du tableur) et vérifie le nombre de lignes de la population.

**10. Erreurs possibles.** Critère mal traduit en code ; exclusion silencieuse de lignes mal formatées.

**11. Limites.** Les exceptions doivent être investiguées avec les pièces et les audités ; Claude ne qualifie pas une irrégularité.

**12. Livrable.** Papier de travail complet (objectif, population, code, résultats, revue de l'auditeur).

#### Cas d'usage 29.2 — Rédaction des constats

**1. Problème.** Transformer les résultats des tests et des entretiens en constats clairs et équilibrés.

**2. Méthode habituelle.** Rédaction longue, constats parfois incomplets.

**3. Contribution de Claude.** Rédaction au format **CCCRR** : constat, critère, cause, risque (conséquence), recommandation, à partir des seuls éléments validés.

**4. Données.** Papiers de travail validés ; réponses des audités ; procédure.

**5–6. Procédure et prompt.**

```text
Rédige le constat d'audit à partir des éléments validés ci-dessous, au format :
Constat (faits) | Critère (règle de référence, citée) | Cause (selon les entretiens, citée)
| Risque | Recommandation (proportionnée, assortie d'un responsable proposé et d'une échéance proposée).
<elements_valides> … </elements_valides>
Règles : aucune accusation nominative ; aucune cause non issue des entretiens ;
ton factuel et équilibré ; mentionne les points positifs constatés s'il y en a.
```

**7. Échanges.** Application de la grille de qualité du chapitre 11 (prompt 11.4), puis relecture par Michel.

**8. Exemple (extrait, fictif).** *Constat :* trois commandes de 9 800 USD ont été passées le même jour auprès du même prestataire pour une « prestation diverse ». *Critère :* la procédure d'achat interdit le fractionnement des besoins et impose l'approbation du directeur au-delà de 10 000 USD. *Cause :* selon le service demandeur, urgence et méconnaissance de la règle. *Risque :* contournement des délégations, prix non négociés. *Recommandation :* contrôle automatique des cumuls journaliers par fournisseur dans l'ERP ; rappel de la procédure.

**9. Contrôle.** Chaque élément est rattaché à un papier de travail ; contradictoire avec l'audité.

**10. Erreurs possibles.** Cause supposée ; recommandation disproportionnée ; ton accusateur.

**11. Limites.** La formulation finale et la cotation du risque sont de la responsabilité de l'auditeur.

**12. Livrable.** Projet de rapport d'audit.

#### Cas d'usage 29.3 — Plan d'audit fondé sur les risques (condensé)

À partir de la cartographie des risques de l'entreprise, des audits passés et des changements récents (programme IA, extension Mbiyo Profond, nouveau contrat de transport), Claude propose une **structure** de plan (univers d'audit, critères de priorisation, missions candidates, ressources) et rédige l'argumentaire. Michel arbitre les priorités et soumet le plan au comité d'audit. À noter : le déploiement de l'IA générative est lui-même un sujet d'audit (gouvernance, données, contrôles), pour lequel des cadres comme le cadre de gestion des risques de l'IA du NIST ou la norme ISO/IEC 42001 fournissent des repères [@NIST-RMF; @ISO-42001].

#### Cas d'usage 29.4 — Suivi des recommandations (condensé)

Claude consolide le tableau de suivi (recommandation, responsable, échéance, statut, preuves reçues), calcule les taux de mise en œuvre et le vieillissement par code, et prépare la synthèse pour le comité d'audit. Les statuts « mis en œuvre » ne sont validés qu'après examen des preuves par l'auditeur.

### E. Prompts commentés

**Prompt 29.1 — Programme de travail d'une mission**

```text
Prépare le programme de travail d'une mission d'audit interne sur [processus] dans une société minière.
Pour chaque objectif de contrôle : risques, contrôles attendus, tests proposés (avec la population
et les données nécessaires), documents à demander, temps estimé. Base-toi sur la procédure jointe
et signale les contrôles attendus qui n'y figurent pas.
```

*Commentaire.* Le programme est une proposition : l'auditeur l'adapte à son appréciation des risques.

### F. Exercices pratiques

**Exercice 29.1 (guidé).** Réalisez le cas 29.1 ; conservez le code et le résultat comme un papier de travail. Refaites T2 à la main.

**Exercice 29.2 (guidé).** Rédigez le constat sur le fractionnement (cas 29.2), puis faites-le relire selon la grille du prompt 11.4.

**Exercice 29.3 (autonome).** Préparez le programme de travail d'un audit de la gouvernance de l'IA dans votre entreprise (appuyez-vous sur les chapitres 37 à 40).

### G. Livrable professionnel

**Dossier de mission** : programme de travail, papiers de travail reproductibles, constats, projet de rapport, tableau de suivi des recommandations.

### H. Vérification des résultats

::: controle
- Chaque test est reproductible : données, code, résultat, revue de l'auditeur.
- La taille de la population testée est vérifiée.
- Les constats ne contiennent que des éléments validés et rattachés à des preuves.
- Le contradictoire avec les audités a été respecté.
- Les données d'audit confidentielles n'ont été traitées que dans l'environnement autorisé.
:::

::: setrompe
Dans un papier de travail, Claude indique « 0 exception » au test des doublons… parce que les montants étaient lus comme du texte et que la comparaison échouait. **Contre-mesure** : toujours vérifier le nombre de lignes traitées, les types de données, et réaliser un contrôle de vraisemblance (un doublon connu doit être détecté).
:::

### I. Limites et précautions

- Le jugement d'audit et la conclusion engagent l'auditeur ; l'IA ne peut ni signer ni émettre d'opinion.
- Les documents fournis par les audités peuvent contenir des instructions malveillantes (injection de prompt, chapitre 38) : vigilance.
- L'indépendance impose de ne pas laisser un outil configuré par l'audité orienter les analyses.

### J. Boîte à outils

- Prompts des cas 29.1, 29.2 et prompt 29.1.
- Format CCCRR : constat, critère, cause, risque, recommandation.
- Check-list de papier de travail IA : objectif, source des données, prompt, code, résultat, revue, conclusion, date, auteur.

### K. Quiz

1. **(QCM)** Que signifie le format CCCRR ? a) contrôle, coût, calendrier ; b) constat, critère, cause, risque, recommandation ; c) cinq contrôles de conformité ; d) une norme ISO.
2. **(Vrai ou faux)** Un test réalisé par Claude n'a pas besoin d'être documenté s'il est exact.
3. **(Compréhension)** Quel avantage offre le test de 100 % de la population par rapport à l'échantillonnage ?
4. **(Mise en situation)** Un test « doublons » donne 0 exception alors que vous en connaissez une. Que soupçonnez-vous ?
5. **(Vrai ou faux)** Claude peut qualifier une exception de fraude.
6. **(Application)** Rédigez le critère d'un constat sur le fractionnement des commandes.
7. **(QCM)** Quels cadres peuvent servir de repères pour auditer la gouvernance de l'IA ? a) NIST AI RMF et ISO/IEC 42001 ; b) GISTM ; c) JORC ; d) ITIE.
8. **(Compréhension)** Pourquoi le contradictoire avec les audités reste-t-il indispensable ?
9. **(Analyse critique)** En quoi l'injection de prompt est-elle un risque particulier en audit ?
10. **(Application)** Citez les éléments d'un papier de travail réalisé avec Claude.

<div class="carnet" titre="Chapitre 29 — Claude appliqué à l'audit financier, à l'audit opérationnel et au contrôle interne"></div>
