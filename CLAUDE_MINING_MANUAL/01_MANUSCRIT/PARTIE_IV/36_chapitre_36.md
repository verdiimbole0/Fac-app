## Chapitre 36. Construire des workflows professionnels assistés par l'intelligence artificielle

### A. Mise en situation professionnelle

Grace Nsimba veut aller plus loin que l'assistant HSE : chaque fin de mois, le rapport HSE doit être produit selon un **processus** fixe (collecte, calculs, rédaction, contrôles, validation, diffusion) avec des responsabilités claires et une trace de chaque étape. Elle veut savoir quelles étapes peuvent être automatisées (tâche planifiée, scripts), lesquelles assistées, et lesquelles doivent rester strictement humaines.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Cartographier** un processus existant et identifier les étapes à assister ou automatiser.
2. **Concevoir** un workflow avec des portes de validation humaine.
3. **Choisir** le bon niveau d'automatisation (conversation, projet, Cowork, Claude Code, API).
4. **Documenter** le workflow (procédure, RACI, traçabilité).
5. **Mesurer** les effets du workflow (temps, qualité, incidents).

### C. Comprendre avant de pratiquer

#### C.1. Trois niveaux d'intégration

| Niveau | Description | Outils | Exemple |
|---|---|---|---|
| Assisté | L'humain déclenche chaque étape et utilise Claude | Conversation, projet, compétences | Rapport d'incident (ch. 23) |
| Semi-automatisé | Certaines étapes s'exécutent seules, avec contrôle humain aux portes | Cowork (tâches planifiées), scripts | Synthèse hebdomadaire des rapports de poste |
| Automatisé (intégré) | Claude est appelé par une application, dans un processus outillé | API, développement interne | Résumé automatique des rapports de poste dans le portail (ch. 9) |

Plus le niveau d'automatisation est élevé, plus les tests, la surveillance et les portes de validation doivent être robustes.

#### C.2. Les portes de validation

Une **porte de validation** est un point du workflow où un humain désigné vérifie un résultat selon des critères définis avant que le processus continue. Elle est placée : après tout calcul utilisé pour décider ; avant toute diffusion externe ; avant toute action irréversible (envoi, modification d'un système) ; après toute étape à fort risque d'erreur.

![Figure 36.1. Workflow assisté avec trois portes de validation humaine : aucune diffusion sans franchissement des trois portes ; retour en arrière en cas d'anomalie. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig36_1_workflow_portes.png){width=100%}

#### C.3. Agents et autonomie

Les outils comme Cowork ou Claude Code peuvent enchaîner plusieurs étapes de manière autonome (lire des fichiers, exécuter du code, produire des documents). La documentation de Claude Code souligne l'importance de donner à l'agent des moyens de **vérifier** son propre travail (tests, contrôles) [@ANT-CODE-BP], et le centre d'aide consacre un article à l'utilisation sûre de Cowork [@ANT-HC-COWORK]. Pour un workflow d'entreprise, la règle est simple : **l'autonomie de l'outil s'arrête aux portes de validation**.

### D. Démonstration guidée : Le workflow du rapport HSE mensuel

**Étape 1. Cartographie actuelle.** Grace décrit le processus actuel : 9 étapes, 4 personnes, environ 16 heures par mois (mesurées sur deux mois).

**Étape 2. Conception du nouveau workflow.**

| Étape | Qui / quoi | Niveau | Trace |
|---|---|---|---|
| 1. Extraction du registre (fin de mois) | Tâche planifiée (Cowork) ou script | Semi-automatisé | Fichier daté |
| 2. Profil et contrôles des données | Assistant HSE (code) | Assisté | Journal des anomalies |
| **Porte 1** : contrôle des données et des calculs | Technicien HSE | Humain | Visa |
| 3. Calcul des indicateurs et graphiques | Assistant HSE (code stabilisé) | Assisté | Script versionné |
| 4. Rédaction du rapport au format | Assistant HSE (compétence « rapport mensuel ») | Assisté | Version 0 |
| **Porte 2** : relecture métier | Responsable HSE | Humain | Commentaires |
| 5. Corrections | Assistant + responsable | Assisté | Version 1 |
| **Porte 3** : validation | Directeur des opérations | Humain | Signature |
| 6. Diffusion et archivage | Responsable HSE | Humain | Système documentaire |

**Étape 3. Procédure et RACI** rédigés avec Claude (prompt 36.2), validés par le système de management.

**Étape 4. Pilote** sur trois mois, avec mesure du temps et des erreurs détectées aux portes.

**Étape 5. Bilan (fictif).** Temps mensuel passé de 16 à 7 heures (mesure sur trois mois) ; deux anomalies de données détectées à la porte 1 ; une formulation suggérant une cause corrigée à la porte 2. Le workflow est adopté, avec une revue semestrielle.

### E. Prompts commentés

**Prompt 36.1. Analyse d'un processus existant**

```text
Voici la description de notre processus actuel de [processus] : <processus> … </processus>.
Pour chaque étape : nature (collecte, calcul, rédaction, contrôle, décision, diffusion), durée,
risque d'erreur, conséquences d'une erreur. Propose ensuite un workflow cible indiquant pour chaque
étape le niveau (humain / assisté / semi-automatisé) et les portes de validation nécessaires,
en justifiant. Aucune étape de décision ou de diffusion externe ne peut être automatisée.
```

**Prompt 36.2. Procédure et RACI**

```text
À partir du workflow cible validé ci-dessous, rédige la procédure au format de notre système
de management (objet, domaine, responsabilités, déroulement, enregistrements, indicateurs) et la
matrice RACI. Pour chaque porte de validation, précise les critères de passage et la conduite à tenir
en cas d'échec.
```

*Commentaire.* Les critères de passage d'une porte doivent être **observables** (« totaux recalculés concordants », « aucune cause mentionnée »), sinon la porte devient une formalité.

### F. Exercices pratiques

**Exercice 36.1 (guidé).** Cartographiez un processus mensuel de votre service, mesurez sa durée réelle, et utilisez le prompt 36.1.

**Exercice 36.2 (guidé).** Rédigez la procédure et le RACI de votre workflow cible (prompt 36.2), avec des critères de passage observables.

**Exercice 36.3 (autonome).** Pilotez votre workflow pendant deux cycles ; mesurez temps, anomalies détectées et incidents ; présentez le bilan.

### G. Livrable professionnel

**Dossier de workflow** : cartographie avant/après, procédure, RACI, critères des portes, mesures du pilote, décision d'adoption.

### H. Vérification des résultats

::: controle
- Chaque porte a un responsable désigné et des critères observables.
- Aucune décision ni diffusion externe n'est automatisée.
- Chaque étape laisse une trace (fichier daté, version, visa).
- Les gains annoncés reposent sur des mesures avant/après.
- Un mode dégradé est prévu (que faire si l'outil n'est pas disponible ?).
:::

::: setrompe
Après trois mois sans anomalie, l'équipe commence à « valider » la porte 1 sans recalcul. Le quatrième mois, un fichier source incomplet produit des indicateurs sous-estimés, diffusés à la direction. **Contre-mesure** : critères observables, contrôles automatiques dans le script (nombre de lignes, couverture), et audits ponctuels des portes.
:::

### I. Limites et précautions

- L'automatisation amplifie les erreurs autant que les gains.
- Un workflow dépendant d'un outil externe doit prévoir un mode dégradé.
- Toute évolution (modèle, outil, procédure) impose un retest.

### J. Boîte à outils

- Prompts 36.1 et 36.2.
- Gabarit de workflow : étape | acteur | niveau | entrée | sortie | contrôle | trace.
- Critères de placement des portes : avant décision, avant diffusion externe, avant action irréversible, après étape à risque.

### K. Quiz

1. **(QCM)** Où placer une porte de validation ? a) avant toute diffusion externe ; b) uniquement à la fin ; c) nulle part si l'outil est fiable ; d) au hasard.
2. **(Vrai ou faux)** Une décision de sécurité peut être automatisée si le workflow est testé.
3. **(Compréhension)** Quelle est la différence entre un workflow assisté et semi-automatisé ?
4. **(Application)** Rédigez un critère de passage observable pour une porte « contrôle des calculs ».
5. **(Mise en situation)** L'équipe valide les portes sans contrôle. Quelles mesures prenez-vous ?
6. **(Vrai ou faux)** Un workflow doit prévoir un mode dégradé.
7. **(Compréhension)** Pourquoi mesurer le temps avant et après ?
8. **(Analyse critique)** « L'automatisation amplifie les erreurs autant que les gains. » Expliquez.
9. **(QCM)** Quel outil convient pour une extraction mensuelle planifiée ? a) Cowork (tâche planifiée) ou script ; b) le mode incognito ; c) la mémoire ; d) un compte personnel.
10. **(Application)** Citez trois éléments de traçabilité d'un workflow.

<div class="carnet" titre="Chapitre 36. Construire des workflows professionnels assistés par l'intelligence artificielle"></div>
