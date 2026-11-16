## Chapitre 43 — Projet final : concevoir son propre système de travail assisté par Claude

### A. Mise en situation professionnelle

Vous arrivez au terme du parcours. Votre hiérarchie vous demande désormais de proposer, pour votre poste ou votre service, un **système de travail assisté par Claude** : quelles tâches, avec quelles méthodes, quels outils, quels contrôles, quelles règles, quels gains mesurés. Ce projet est votre réalisation concrète, celle qui prouve que vous savez transformer une compétence en valeur professionnelle.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous aurez :

1. **Diagnostiqué** vos tâches et choisi des cas d'usage prioritaires.
2. **Construit** une bibliothèque d'instructions CADRE testées.
3. **Configuré** un assistant spécialisé (projet, compétences, éventuellement connecteurs).
4. **Conçu** au moins un workflow avec portes de validation.
5. **Défini** vos règles de confidentialité et vos contrôles qualité.
6. **Mesuré** les gains et **présenté** votre système.

### C. Comprendre avant de pratiquer — Les huit composantes du système

![Figure 43.1 — Les huit composantes de votre système de travail assisté par Claude. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig43_1_systeme_travail.png){width=88%}

| Composante | Contenu | Chapitres |
|---|---|---|
| 1. Diagnostic | Carte des opportunités de vos tâches | 1 |
| 2. Cas d'usage prioritaires | 3 à 5 cas, grille en 12 points | 17–32 |
| 3. Bibliothèque CADRE | 10 instructions testées et versionnées | 10, 11 |
| 4. Assistant spécialisé | Projet, instructions, connaissances, compétences | 15, 16, 35 |
| 5. Workflow et portes | Au moins un processus complet | 36 |
| 6. Contrôles qualité | Check-lists, tests, recalculs | 5, 13, 34 |
| 7. Règles de confidentialité | Classification de vos données, minimisation | 37 |
| 8. Mesure des gains | Avant/après sur tâches réelles | 36, 42 |

### D. Démonstration guidée — Le projet de Grace Nsimba (HSE)

À titre d'exemple, voici la synthèse (fictive) du projet final de Grace :

| Composante | Réalisation |
|---|---|
| Diagnostic | 12 tâches cartographiées ; 160 h/mois pour l'équipe |
| Cas d'usage | Rapport préliminaire d'incident ; rapport mensuel ; causeries ; vérification des contrôles critiques |
| Bibliothèque | 11 instructions CADRE versionnées, avec check-list associée |
| Assistant | Projet « HSE — MCC » partagé (consultation pour les techniciens) ; compétences « rapport préliminaire » et « causerie » |
| Workflow | Rapport mensuel à 3 portes (ch. 36) |
| Contrôles | Recalcul de 2 indicateurs par mois ; liste des « phrases non issues des documents » |
| Confidentialité | Pseudonymisation des déclarations ; aucune donnée médicale ; mémoire désactivée pour le projet |
| Gains mesurés | Rapport mensuel : 16 h → 7 h ; rapports préliminaires : délai moyen 20 h → 6 h ; aucune régression de qualité aux revues |

### E. Prompts commentés

**Prompt 43.1 — Accompagnement du projet final**

```text
Je construis mon système de travail assisté par Claude pour mon poste de [poste] chez [entreprise].
Voici l'état de mes 8 composantes : <etat> … </etat>.
Joue le rôle d'un jury exigeant : pour chaque composante, indique ce qui est solide, ce qui manque,
les risques non traités et la preuve qu'un jury me demanderait. Termine par les 5 améliorations
prioritaires avant ma soutenance.
```

**Prompt 43.2 — Présentation de soutenance**

```text
À partir de mon dossier de projet final (joint), prépare une présentation de 10 diapositives
pour ma hiérarchie : problème, diagnostic, solution (8 composantes), démonstration d'un cas,
contrôles et sécurité, gains mesurés, limites, plan de déploiement, décisions demandées.
Chaque chiffre doit provenir du dossier ; aucune promesse de gain non mesuré.
```

### F. Exercices pratiques — Le projet en six étapes (4 à 6 semaines)

1. **Semaine 1** : diagnostic (carte des opportunités) et choix de 3 à 5 cas d'usage.
2. **Semaine 2** : bibliothèque CADRE (10 instructions), tests et versions.
3. **Semaine 3** : assistant spécialisé (projet, connaissances, compétences) et jeu de tests.
4. **Semaine 4** : workflow avec portes ; règles de confidentialité ; contrôles.
5. **Semaines 5-6** : utilisation réelle ; mesures avant/après ; ajustements.
6. **Soutenance** : présentation de 20 minutes et questions.

### G. Livrable professionnel — Le dossier de projet final

Structure attendue (15 à 25 pages + annexes) :

1. Contexte et objectifs.
2. Diagnostic des tâches (carte des opportunités).
3. Cas d'usage retenus (fiches en 12 points).
4. Bibliothèque d'instructions (annexe).
5. Assistant spécialisé : cahier des charges, configuration, tests.
6. Workflow : procédure, RACI, portes.
7. Contrôles qualité et sécurité ; règles de confidentialité.
8. Mesures et résultats.
9. Limites, risques résiduels, plan d'amélioration.
10. Plan de déploiement et décisions demandées.

*Grille de soutenance (sur 100) :* pertinence métier (15) ; qualité des instructions et de l'assistant (20) ; workflow et contrôles (20) ; sécurité et confidentialité (15) ; mesure des gains (15) ; présentation et réponses aux questions (15).

### H. Vérification des résultats

::: controle
- Chaque composante est documentée et appuyée par des preuves.
- Les gains reposent sur des mesures réelles.
- Les lignes rouges (décisions critiques, données restreintes, décisions individuelles) sont respectées.
- Le système est transmissible : un collègue peut l'utiliser à partir de la documentation.
:::

::: setrompe
Dans une présentation de soutenance générée sans consigne, un assistant peut « arrondir » les gains ou ajouter des bénéfices non mesurés (« amélioration de la satisfaction des équipes »). Le jury le remarquera — et votre crédibilité en souffrira. Chaque affirmation doit être appuyée par le dossier.
:::

### I. Limites et précautions

- Votre système doit respecter la charte et la classification de votre entreprise ; faites-le valider avant tout usage sur des données réelles sensibles.
- Il devra être revu à chaque évolution importante des outils.

### J. Boîte à outils

- Prompts 43.1, 43.2 ; structure du dossier ; grille de soutenance.
- Rappel des annexes utiles : B (prompts), C (modèles CADRE), D (modèles de documents), E (check-lists), F (charte), G (classification), K (grille de compétences).

### K. Quiz

1. **(Compréhension)** Citez les huit composantes du système de travail assisté.
2. **(Vrai ou faux)** Les gains présentés dans la soutenance peuvent être estimés par Claude.
3. **(Application)** Quel est le gain de temps mesuré du rapport mensuel HSE dans l'exemple de Grace ?
4. **(QCM)** Quelle part de la grille de soutenance est consacrée à la sécurité et à la confidentialité ? a) 5 ; b) 15 ; c) 30 ; d) 50.
5. **(Mise en situation)** Un membre du jury demande la preuve d'un gain annoncé. Que lui présentez-vous ?
6. **(Vrai ou faux)** Un système transmissible doit pouvoir être utilisé par un collègue à partir de sa documentation.
7. **(Compréhension)** Pourquoi faire jouer à Claude le rôle d'un jury exigeant ?
8. **(Application)** Quelle est la durée indicative du projet final ?
9. **(Analyse critique)** Pourquoi les lignes rouges doivent-elles apparaître explicitement dans le dossier ?
10. **(Compréhension)** Que doit contenir la section « Limites » du dossier ?

<div class="carnet" titre="Chapitre 43 — Projet final : concevoir son propre système de travail assisté par Claude"></div>
