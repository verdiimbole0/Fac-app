# Module 9 — Choisir et mettre en place les bons outils

## 9.1 Mise en situation

Le Réseau Citoyen pour l'Eau (RCE) reçoit en une semaine trois sollicitations commerciales : un éditeur d'ERP propose un « module d'IA intégré », une start-up promet un « agent autonome » qui rédigera les rapports aux bailleurs, et un consultant recommande de « tout construire en interne avec des API ». De son côté, Lumière des Collines se demande simplement si l'assistant gratuit de son téléphone suffit.

Les deux organisations se posent, à des échelles différentes, la même question : comment choisir sans se tromper, sans surpayer et sans se rendre dépendantes ?

## 9.2 Problématique

Le marché des outils d'IA évolue très vite, avec des promesses parfois spectaculaires et des modèles économiques variés (gratuit, abonnement par utilisateur, paiement à l'usage, licence). Un mauvais choix coûte cher : abonnements inutilisés, doubles saisies, données prisonnières d'un outil, risques de sécurité. Le choix doit découler du cas d'usage, de la maturité de l'organisation et d'une analyse des risques — jamais d'une démonstration commerciale.

## 9.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. distinguer outils gratuits et payants, cloud et local, sans code, faible code et développement ;
2. expliquer ce que sont une application métier, une API, une intégration, une automatisation et un agent ;
3. choisir un niveau d'implémentation adapté (débutant, intermédiaire, avancé) ;
4. évaluer un fournisseur, y compris sur la sécurité et la réversibilité ;
5. analyser les coûts complets ;
6. utiliser une grille de sélection pondérée.

## 9.4 Notions et définitions

- **Cloud / SaaS** : logiciel utilisé via internet, hébergé par le fournisseur, généralement sur abonnement.
- **Solution locale (*on-premise*)** : logiciel installé sur les ordinateurs ou serveurs de l'organisation.
- **No-code** : création d'applications ou d'automatisations par assemblage visuel, sans programmation.
- **Low-code** : idem, avec possibilité d'ajouter un peu de code pour les cas particuliers.
- **Application métier** : logiciel spécialisé pour une fonction (comptabilité, paie, gestion des donateurs, suivi des bénéficiaires).
- **API** : interface permettant à deux logiciels d'échanger des données ou d'utiliser des services de manière automatisée. Les fournisseurs de modèles d'IA proposent généralement des API facturées à l'usage.
- **Intégration** : connexion entre deux applications pour éviter la ressaisie.
- **Réversibilité** : capacité à quitter un fournisseur en récupérant ses données dans un format exploitable.

## 9.5 Explications détaillées

### Trois niveaux d'implémentation

![Figure 9.1 — Trois niveaux d'implémentation](03_ILLUSTRATIONS/figures/fig_9_1.svg)

| | Niveau 1 — Débutant | Niveau 2 — Intermédiaire | Niveau 3 — Avancé |
|---|---|---|---|
| Pour qui | Petites ASBL, peu de moyens techniques | ASBL disposant déjà d'outils numériques | Moyennes et grandes organisations, processus complexes |
| Outils types | Assistant conversationnel, tableur, formulaires, modèles de documents, classement documentaire simple | Suite bureautique professionnelle avec IA intégrée, logiciels métier, plateformes d'automatisation sans code, gestion électronique de documents, tableaux de bord, assistants configurés sur documents internes | API de modèles, bases de données, ERP, architecture RAG, agents, hébergement dédié ou local, gestion des identités, journalisation et supervision |
| Compétences | Bureautique et formation à l'usage | Un « référent numérique » capable de paramétrer | Spécialistes (développement, données, sécurité), internes ou prestataires |
| Coûts | Nuls à faibles | Abonnements par utilisateur, paramétrage | Développement, licences, hébergement, maintenance, sécurité |
| Limites | Offres gratuites : quotas, conditions de confidentialité souvent inadaptées aux données internes, absence de contrat | Dépendance à plusieurs fournisseurs, automatisations à maintenir | Complexité, coût récurrent, besoin d'une gouvernance solide |

> **🔎 À retenir** — Le bon niveau n'est pas le plus élevé, mais celui que l'organisation peut **utiliser, contrôler et maintenir** durablement.

### Gratuit ou payant ?

Les offres gratuites conviennent à l'apprentissage et aux données publiques (vert). Elles présentent généralement : des limites d'usage (nombre de requêtes, taille des fichiers) ; des conditions pouvant autoriser l'utilisation des contenus pour améliorer les services ; l'absence d'engagement contractuel de confidentialité ou de disponibilité ; des changements de conditions sans préavis. Les offres professionnelles payantes apportent, selon les fournisseurs, des garanties contractuelles, une administration centralisée des comptes, des paramètres de confidentialité et un support. Certains fournisseurs proposent des **programmes à tarif réduit pour les organisations à but non lucratif** : renseignez-vous directement auprès d'eux, conditions et éligibilité variant selon les pays.

### Cloud ou local ?

| Critère | Cloud | Local |
|---|---|---|
| Mise en route | Rapide | Plus longue |
| Coût | Abonnement récurrent | Investissement matériel et maintenance |
| Performance des modèles | Accès aux modèles les plus performants | Modèles plus petits, performances moindres sur du matériel courant |
| Confidentialité | Dépend du contrat et de la localisation | Maîtrise interne, mais sécurité à assurer soi-même |
| Connectivité | Indispensable | Fonctionne hors ligne |
| Maintenance | Assurée par le fournisseur | À votre charge |

> **📶 Faible connectivité** — Pour une organisation qui travaille en zone peu connectée, une approche hybride est souvent la plus réaliste : collecte et travail hors ligne (formulaires mobiles, tableurs), synchronisation périodique, et usage du cloud pour les traitements lourds lorsque la connexion est disponible. Des modèles de langage dits « ouverts » peuvent être installés sur un ordinateur portable récent pour des tâches simples hors ligne ; leur installation et leur sécurisation relèvent du niveau Avancé.

### No-code, low-code et développement

Les plateformes d'automatisation sans code permettent de créer des scénarios du type : « lorsqu'un formulaire est soumis → créer une ligne dans le tableau → envoyer le document à un assistant d'IA pour en extraire les informations → notifier le responsable pour validation ». Elles démocratisent l'automatisation, mais :

- chaque scénario devient un petit logiciel à **documenter et maintenir** ;
- une erreur se reproduit à grande échelle ;
- les données transitent par la plateforme : elle doit être évaluée comme tout fournisseur ;
- il faut éviter la prolifération d'automatisations créées par des personnes différentes sans inventaire (annexe 9).

### Applications métier avec IA intégrée

De nombreux logiciels métier (comptabilité, gestion des donateurs, RH, gestion de projets) intègrent désormais des fonctions d'IA. C'est souvent la voie la plus simple : pas d'intégration supplémentaire, données déjà présentes. Questions à poser : la fonction d'IA est-elle activable et désactivable ? quelles données utilise-t-elle ? où sont-elles traitées ? par quel sous-traitant ? peut-on tracer ce qu'elle a proposé et ce qui a été validé ?

### API, intégrations et agents

Au niveau avancé, l'organisation (ou son prestataire) utilise des API pour construire ses propres outils : un assistant RAG sur les procédures, une extraction automatique de factures reliée à l'ERP, un tableau de bord alimenté automatiquement. Les **agents** ajoutent la capacité d'enchaîner des actions. Principes de conception sûre :

1. **moindre privilège** : chaque composant n'accède qu'à ce qui est nécessaire ;
2. **validation humaine** avant toute action irréversible ou externe ;
3. **journalisation** des requêtes, des réponses et des validations ;
4. **séparation** entre contenus non fiables (courriels entrants, pages web) et instructions ;
5. **tests** systématiques avant mise en production (module 19).

### Évaluer un fournisseur

La grille ci-dessous (annexe 9 et fiche P9.1) structure l'évaluation.

| Domaine | Questions |
|---|---|
| Adéquation fonctionnelle | Répond-il au cas d'usage tel que défini ? Démonstration sur **vos** documents ? |
| Données et confidentialité | Données utilisées pour l'entraînement ? Localisation ? Sous-traitants ? Durée de conservation ? Suppression ? |
| Sécurité | Authentification forte ? Chiffrement ? Gestion des droits ? Historique des accès ? Certifications revendiquées (à vérifier) ? |
| Réversibilité | Export complet dans un format ouvert ? Assistance à la sortie ? |
| Pérennité | Ancienneté, clientèle, modèle économique, feuille de route ? |
| Coûts | Modèle de prix ? Évolution prévisible ? Coûts cachés (stockage, utilisateurs supplémentaires, dépassements) ? |
| Support et formation | Langue, délais, documentation ? |
| Accessibilité | Interface conforme aux règles d'accessibilité (par exemple WCAG 2.2) ? Fonctionnement sur mobile et en faible débit ? |
| Conformité | Clauses contractuelles de protection des données conformes aux lois applicables ? |

### Analyser les coûts

Reprenez la méthode du coût total sur trois ans (module 6) : licences et abonnements, mise en place, intégration, formation, temps de contrôle humain, maintenance des automatisations, coûts de sortie. Pour les API facturées à l'usage, estimez un volume mensuel, testez sur un mois pilote, et fixez une **alerte de consommation** pour éviter les mauvaises surprises.

### La grille de sélection

*Exemple (fictif) — RCE compare trois options pour un assistant de questions-réponses sur ses procédures :*

| Critère (poids) | A. Assistant configuré dans la suite bureautique (documents joints) | B. Module IA de l'ERP | C. Développement RAG sur mesure |
|---|---|---|---|
| Adéquation (25 %) | 3 | 2 | 5 |
| Confidentialité et sécurité (20 %) | 4 | 4 | 4 |
| Réversibilité (10 %) | 4 | 2 | 5 |
| Facilité d'adoption (15 %) | 5 | 4 | 3 |
| Coût sur 3 ans, inversé (15 %) | 4 | 3 | 2 |
| Maintenabilité interne (15 %) | 4 | 4 | 2 |
| **Score pondéré** | **3,90** | **3,15** | **3,60** |

*Calcul pour l'option A :* 3 × 0,25 + 4 × 0,20 + 4 × 0,10 + 5 × 0,15 + 4 × 0,15 + 4 × 0,15 = 0,75 + 0,80 + 0,40 + 0,75 + 0,60 + 0,60 = 3,90.

Décision de RCE : démarrer avec l'option A en pilote sur un périmètre restreint (procédures financières), mesurer le taux de réponses correctes, et réévaluer l'option C après six mois si les limites de A sont atteintes.

## 9.6 Application professionnelle : choisir un outil pour Horizons Partagés

| Étape | Action | Responsable | Livrable |
|---|---|---|---|
| 1 | Reprendre la fiche d'opportunité et préciser les exigences (indispensables / souhaitables) | Chef de projet | Liste d'exigences |
| 2 | Identifier 3 à 5 options, dont une sans IA ou avec les outils existants | Référent numérique | Liste courte |
| 3 | Envoyer le questionnaire fournisseur (fiche P9.1) | Référent numérique | Réponses écrites |
| 4 | Démonstration sur 10 documents réels non sensibles ou anonymisés | Utilisateurs clés | Notes de test |
| 5 | Notation avec la grille pondérée (dans un tableur) | Comité de 3 à 5 personnes | Grille signée |
| 6 | Vérification juridique des clauses de protection des données | Direction / conseil juridique | Avis |
| 7 | Décision et inscription au registre des outils | Direction | Décision, registre |

### Solutions selon le niveau

| Niveau | Démarche de choix | Coûts | Limites |
|---|---|---|---|
| Débutant | Liste des outils autorisés tenue par la direction ; usage limité aux données vertes ; test de 20 minutes (fiche P2.1) | Nuls | Pas de garanties contractuelles |
| Intermédiaire | Questionnaire fournisseur, démonstration sur cas réels, grille pondérée, revue des conditions | Temps, abonnements | Comparaison parfois difficile entre offres |
| Avancé | Appel d'offres ou consultation formalisée, preuve de concept chiffrée, audit de sécurité, clauses de réversibilité et de niveau de service | Élevés | Durée du processus |

## 9.7 Prompt prêt à l'emploi

### Fiche P9.1 — Préparer un questionnaire fournisseur

**A. Titre.** Questionnaire d'évaluation d'un fournisseur de solution d'IA.

**B. Objectif.** Obtenir un questionnaire complet, adapté au cas d'usage, pour comparer objectivement des fournisseurs.

**C. Contexte d'utilisation.** Avant toute souscription d'un outil traitant des données internes ou personnelles.

**D. Données nécessaires.** Description du cas d'usage ; classification des données ; contraintes (budget, connectivité, langues, lois applicables).

**E. Prompt complet.**

```text
Contexte : [NOM DE L'ASBL], [PAYS D'IMPLANTATION ET D'INTERVENTION],
souhaite choisir un outil pour le cas d'usage suivant : [CAS D'USAGE].
Données concernées : [TYPES ET COULEUR : vert/orange/rouge].
Contraintes : [BUDGET, CONNECTIVITÉ, LANGUES, LOIS OU EXIGENCES DES
BAILLEURS].
Tâche : rédige un questionnaire à envoyer aux fournisseurs.
Résultat attendu : 25 à 35 questions fermées ou précises, regroupées
en rubriques : adéquation fonctionnelle ; données et confidentialité ;
sécurité ; réversibilité ; pérennité ; coûts (modèle de prix et coûts
annexes) ; support et formation ; accessibilité et faible débit ;
conformité. Pour chaque question, indique entre parenthèses la
réponse attendue idéale et le niveau de criticité (éliminatoire /
important / souhaitable).
Limites : ne mentionne aucun fournisseur nommément. Formule des
questions auxquelles on peut répondre par oui/non ou par une
information vérifiable, et demande les preuves (documents,
certificats, clauses).
```

**F. Instructions d'utilisation.** Adaptez la criticité à votre situation ; envoyez le même questionnaire à tous les fournisseurs ; exigez des réponses écrites et les documents contractuels correspondants.

**G. Résultat attendu.** Un questionnaire structuré, avec critères éliminatoires explicites.

**H. Exemple d'application (illustratif).** Pour l'extraction de factures (données orange), le questionnaire obtenu inclut notamment la question éliminatoire : « Les documents transmis sont-ils exclus de l'entraînement de vos modèles, par défaut et contractuellement ? (Oui, avec clause contractuelle) ».

**I. Méthode de vérification.** Comparez les réponses aux documents contractuels (conditions générales, accord de traitement des données) ; une réponse commerciale non reprise dans le contrat n'engage pas le fournisseur.

**J. Précautions.** Ne transmettez pas de données réelles aux fournisseurs avant la signature d'un accord de confidentialité ; utilisez des documents anonymisés pour les démonstrations.

**K. Amélioration.** « Ajoute une section spécifique aux exigences de [BAILLEUR / LOI] en matière de localisation et de transfert des données. »

## 9.8 Résultats attendus

Une décision documentée, un outil inscrit au registre (annexe 9) avec son responsable, ses paramètres de confidentialité, les données autorisées et la date de prochaine revue.

## 9.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** — La souscription d'un outil traitant des données internes ou personnelles est approuvée par la direction après examen des clauses de protection des données. Les paramètres de confidentialité sont configurés par un administrateur désigné, et non laissés au choix de chaque utilisateur.

## 9.10 Risques et erreurs à éviter

- Choisir sur démonstration commerciale, sans test sur ses propres documents.
- Ignorer la réversibilité.
- Multiplier les outils qui font la même chose.
- Sous-estimer la maintenance des automatisations sans code.
- Donner à un agent des droits étendus sur la messagerie, les fichiers ou les paiements.
- Oublier les coûts à l'usage des API et ne pas fixer d'alerte de consommation.

## 9.11 Exercice pratique

**Consigne (2 heures).** Pour un cas d'usage retenu au module 6 : (1) identifiez trois options de niveaux différents ; (2) appliquez la fiche P9.1 ; (3) notez les options avec la grille pondérée dans un tableur ; (4) rédigez une recommandation d'une demi-page incluant les risques et la stratégie de sortie.

**Éléments de correction.** Une bonne réponse inclut au moins une option simple ; des critères éliminatoires liés aux données ; un calcul vérifiable ; une stratégie de sortie (export des données, durée d'engagement).

## 9.12 Synthèse

- Le niveau d'implémentation se choisit selon ce que l'organisation peut utiliser, contrôler et maintenir.
- Gratuit, payant, cloud, local, no-code, API : chaque option a ses avantages et ses limites.
- L'évaluation d'un fournisseur porte sur la fonction, mais aussi sur les données, la sécurité, la réversibilité et les coûts complets.
- Une grille pondérée, des tests sur des cas réels et la lecture des contrats fondent une décision solide.

## 9.13 QCM — Module 9

**Q1.** (une seule réponse) La réversibilité désigne :

a) la possibilité d'annuler une requête.
b) la capacité à quitter un fournisseur en récupérant ses données dans un format exploitable.
c) la traduction dans les deux sens.
d) le remboursement de l'abonnement.

**Q2.** (une seule réponse) Une API est :

a) un type d'ordinateur.
b) une interface permettant à des logiciels d'échanger des données ou d'utiliser des services de façon automatisée.
c) une norme de sécurité.
d) un assistant conversationnel.

**Q3.** (une ou plusieurs réponses) Les offres gratuites d'outils d'IA présentent souvent :

a) des limites d'usage.
b) des conditions pouvant autoriser l'utilisation des contenus pour améliorer les services.
c) un engagement contractuel de confidentialité adapté aux données sensibles.
d) des changements de conditions possibles sans préavis.

**Q4.** (une seule réponse) Le « bon » niveau d'implémentation est :

a) toujours le plus avancé.
b) celui que l'organisation peut utiliser, contrôler et maintenir.
c) le moins cher.
d) celui du principal bailleur.

**Q5.** (une ou plusieurs réponses) Principes de conception sûre pour des agents IA :

a) moindre privilège.
b) validation humaine avant action irréversible.
c) journalisation.
d) accès complet à la messagerie pour plus d'efficacité.

**Q6.** (une seule réponse) Avec les poids de l'exemple (25/20/10/15/15/15 %), l'option notée 2, 4, 2, 4, 3, 4 obtient :

a) 3,05
b) 3,15
c) 3,40
d) 19

**Q7.** (mise en situation — une seule réponse) Un commercial affirme oralement que « vos données ne servent jamais à l'entraînement ». Que faites-vous ?

a) Vous le croyez.
b) Vous exigez que cela figure dans le contrat ou l'accord de traitement des données.
c) Vous demandez la même chose à un assistant d'IA.
d) Vous ne posez plus de question.

**Q8.** (mise en situation — une seule réponse) Une petite association en zone peu connectée veut améliorer la collecte de données de terrain. Approche la plus réaliste ?

a) Un agent IA dans le cloud en continu.
b) Formulaires mobiles hors ligne, synchronisation périodique, traitements assistés lors des connexions.
c) Un ERP avancé.
d) Renoncer au numérique.

**Q9.** (une seule réponse) Pour un outil facturé à l'usage via API, une bonne pratique consiste à :

a) ne pas suivre la consommation.
b) fixer une alerte de consommation et tester sur un mois pilote.
c) payer d'avance trois ans.
d) partager la clé d'accès entre tous les collaborateurs.

**Q10.** (une ou plusieurs réponses) Les automatisations sans code :

a) doivent être documentées et inventoriées.
b) peuvent reproduire une erreur à grande échelle.
c) ne nécessitent jamais de maintenance.
d) font transiter des données par la plateforme, qui doit être évaluée.

## 9.14 Corrigé détaillé — Module 9

**Q1 : b.** C'est la garantie contre la dépendance.

**Q2 : b.** L'API permet les échanges automatisés entre logiciels.

**Q3 : a, b, d.** Les offres gratuites n'offrent généralement pas les garanties contractuelles nécessaires (c).

**Q4 : b.** L'adéquation aux capacités prime.

**Q5 : a, b, c.** L'accès complet (d) contredit le moindre privilège et expose aux injections de prompt.

**Q6 : b.** 2×0,25 + 4×0,20 + 2×0,10 + 4×0,15 + 3×0,15 + 4×0,15 = 0,50 + 0,80 + 0,20 + 0,60 + 0,45 + 0,60 = 3,15. C'est le score de l'option B du tableau. Réponse d : erreur classique consistant à additionner les notes sans les pondérer.

**Q7 : b.** Seul le contrat engage le fournisseur.

**Q8 : b.** L'approche hybride hors ligne est adaptée à la faible connectivité.

**Q9 : b.** L'alerte évite les dépassements ; la clé d'accès ne se partage jamais (d).

**Q10 : a, b, d.** Elles exigent au contraire une maintenance (c).

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- OWASP Foundation. (2024). *OWASP Top 10 for LLM Applications* (version 2025).
- W3C. (2023, mise à jour 2024). *Web Content Accessibility Guidelines (WCAG) 2.2*.
