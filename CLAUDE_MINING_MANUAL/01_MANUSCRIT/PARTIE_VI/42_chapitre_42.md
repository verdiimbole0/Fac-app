## Chapitre 42. Évaluation des compétences et mesure de la maîtrise de Claude

### A. Mise en situation professionnelle

À la fin du pilote, le comité de MCC doit décider qui pourra devenir « utilisateur référent » dans chaque service et quels besoins de formation subsistent. Kevin Mutombo refuse de s'appuyer sur le seul ressenti (« je me débrouille bien ») ou sur le nombre de conversations. Il veut une évaluation **objective**, fondée sur des preuves : des livrables, des tests pratiques, des comportements observables.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Évaluer** votre niveau sur les huit blocs de compétences du manuel.
2. **Réaliser** un test pratique de maîtrise et l'autoévaluer.
3. **Construire** votre plan de progression personnel.
4. **Évaluer** les compétences d'une équipe (managers et formateurs).
5. **Mesurer** les effets de l'usage de Claude sur votre travail.

### C. Comprendre avant de pratiquer

#### C.1. Les huit blocs de compétences

| Bloc | Compétence | Chapitres |
|---|---|---|
| C1 | Comprendre l'IA et les grands modèles de langage | 1–6 |
| C2 | Maîtriser l'environnement Claude | 7–9, 12, 15, 16 |
| C3 | Formuler des instructions professionnelles (CADRE) | 10–11 |
| C4 | Exploiter documents et données | 13, 14, 33 |
| C5 | Appliquer Claude à son métier minier | 17–32 |
| C6 | Produire des livrables de qualité | 34 |
| C7 | Vérifier, sécuriser, protéger | 5, 6, 37–40 |
| C8 | Concevoir des méthodes de travail assistées | 35, 36, 43 |

#### C.2. L'échelle de maîtrise

1. **Découverte** : connaît la notion.
2. **Application guidée** : réalise la tâche avec un modèle de prompt.
3. **Autonomie** : adapte la méthode à un cas nouveau et vérifie le résultat.
4. **Maîtrise** : conçoit des méthodes réutilisables, forme ses collègues, gère les risques.

![Figure 42.1. Exemple de profil de compétences avant et après la formation (valeurs illustratives). Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig42_1_radar_competences.png){width=70%}

#### C.3. Les preuves de maîtrise

Une compétence se démontre par des **preuves observables** : un livrable vérifié, un prompt documenté, un contrôle réalisé, un incident évité, un collègue formé. L'Annexe K propose une grille détaillée par bloc avec les preuves attendues à chaque niveau.

### D. Démonstration guidée : Le test pratique de maîtrise (2 heures)

Le test comporte cinq épreuves, réalisées avec les fichiers d'exercice :

| Épreuve | Contenu | Blocs | Points |
|---|---|---|---|
| 1. Diagnostic | Expliquer en 10 lignes pourquoi Claude peut se tromper sur un calcul et comment l'éviter | C1 | 10 |
| 2. Instruction | Rédiger une instruction CADRE pour un cas fourni par l'évaluateur | C3 | 20 |
| 3. Données | Profiler `MCC_production_journaliere_S1_2026.csv`, trouver les anomalies, calculer la cathode de mars avec contrôle | C2, C4 | 25 |
| 4. Livrable | Produire une note d'une page vérifiée sur un sujet de son métier | C5, C6 | 25 |
| 5. Sécurité | Classer 5 documents, analyser la procédure piégée, rédiger la règle de protection | C7 | 20 |

*Seuils indicatifs :* 50/100 = application guidée ; 70/100 = autonomie ; 85/100 avec livrable de méthode (C8) = maîtrise, prérequis du statut de référent.

### E. Prompts commentés

**Prompt 42.1. Autoévaluation assistée**

```text
Voici mes réponses au test pratique (épreuves 1 à 5) et la grille d'évaluation.
Évalue chaque épreuve selon la grille, en justifiant chaque point retiré par un élément précis
de ma réponse. Indique ensuite mes trois priorités de progression et les chapitres à revoir.
Sois exigeant : je préfère une évaluation sévère et juste.
```

*Commentaire.* L'autoévaluation assistée est utile pour progresser ; pour une certification interne, l'évaluation est réalisée par un évaluateur humain.

**Prompt 42.2. Plan de progression**

```text
Mon profil (échelle 1 à 4) : C1 [x], C2 [x], C3 [x], C4 [x], C5 [x], C6 [x], C7 [x], C8 [x].
Mon métier : [métier]. Temps disponible : [n] minutes par jour.
Propose un plan de progression sur 4 semaines, avec pour chaque semaine : objectifs, exercices
du manuel, une tâche réelle de mon travail à réaliser avec Claude, et la preuve de maîtrise à produire.
```

### F. Exercices pratiques

**Exercice 42.1 (guidé).** Passez le test pratique dans les conditions indiquées (2 heures, sans aide extérieure), puis faites-vous évaluer.

**Exercice 42.2 (guidé).** Remplissez la grille de l'Annexe K et tracez votre profil.

**Exercice 42.3 (autonome).** Mesurez, sur trois tâches réelles, le temps et la qualité avant/après l'usage de Claude (méthode du chapitre 36).

### G. Livrable professionnel

**Dossier de compétences** : résultats du test, grille de l'Annexe K, profil, preuves de maîtrise, mesures avant/après, plan de progression.

### H. Vérification des résultats

::: controle
- L'évaluation repose sur des preuves, pas sur le ressenti.
- Les mesures de gain sont faites sur des tâches réelles, avant/après.
- Le plan de progression cible les blocs les plus faibles et les besoins du métier.
:::

::: setrompe
Lors d'une autoévaluation assistée, Claude peut se montrer trop indulgent si la consigne n'est pas exigeante, ou attribuer des points à des éléments absents. **Contre-mesure** : demander la justification de chaque point retiré **et** accordé, et faire valider par un évaluateur.
:::

### I. Limites et précautions

- Un test ponctuel ne mesure pas tout : complétez par l'observation dans la durée.
- Les compétences évoluent avec les outils : réévaluez chaque année.

### J. Boîte à outils

- Test pratique (section D) ; prompts 42.1, 42.2 ; Annexe K (grille) ; Annexe J (programme 30 jours).

### K. Quiz

1. **(QCM)** Combien de blocs de compétences le manuel définit-il ? a) 4 ; b) 6 ; c) 8 ; d) 10.
2. **(Compréhension)** Qu'est-ce qu'une preuve de maîtrise ?
3. **(Vrai ou faux)** Le nombre de conversations avec Claude est un bon indicateur de compétence.
4. **(Application)** À quel niveau correspond « adapte la méthode à un cas nouveau et vérifie le résultat » ?
5. **(Calcul)** Un candidat obtient 8, 15, 20, 18 et 16 aux cinq épreuves. Quel est son score et son niveau indicatif ?
6. **(Vrai ou faux)** Pour une certification interne, l'évaluation doit être réalisée par un évaluateur humain.
7. **(Compréhension)** Quels blocs l'épreuve « Sécurité » évalue-t-elle ?
8. **(Analyse critique)** Pourquoi l'autoévaluation assistée doit-elle être exigeante ?
9. **(Application)** Citez deux preuves de maîtrise du bloc C8.
10. **(Compréhension)** Pourquoi réévaluer les compétences chaque année ?

<div class="carnet" titre="Chapitre 42. Évaluation des compétences et mesure de la maîtrise de Claude"></div>
