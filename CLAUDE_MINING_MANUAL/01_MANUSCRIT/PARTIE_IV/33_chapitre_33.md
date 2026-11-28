## Chapitre 33. Analyser des données, exploiter des fichiers et construire des tableaux de bord

### A. Mise en situation professionnelle

Nadine Kapinga, contrôleuse de gestion, reçoit chaque mois une dizaine de fichiers : production journalière, budget et réel, ordres de travail, incidents HSE, commandes, suivi de l'eau. Chaque service a ses formats et ses conventions. La direction veut un **tableau de bord mensuel unique**, fiable, compréhensible en cinq minutes. Nadine a déjà utilisé Claude pour des analyses ponctuelles (chapitres 19, 21, 28) ; elle veut maintenant une **méthode** reproductible.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Appliquer** une méthode d'analyse de données en six étapes avec Claude.
2. **Rédiger** un dictionnaire de données et des définitions d'indicateurs exploitables par Claude.
3. **Produire** des analyses reproductibles (code conservé, contrôles intégrés).
4. **Concevoir** un tableau de bord lisible et honnête.
5. **Reconnaître** les pièges statistiques et graphiques les plus fréquents.

### C. Comprendre avant de pratiquer

#### C.1. La méthode en six étapes

![Figure 33.1. Méthode d'analyse de données avec Claude : la question, les décisions de nettoyage et l'interprétation restent humaines ; Claude profile, calcule et visualise par programme. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig33_1_analyse_donnees.png){width=100%}

1. **Question** : quelle décision l'analyse doit-elle éclairer ? Quels indicateurs, définis comment ?
2. **Profil** : structure, période, valeurs manquantes, aberrantes, doublons (chapitre 13).
3. **Nettoyage** : décisions humaines, documentées, idéalement appliquées à la source.
4. **Calcul** : par exécution de code, formules affichées, nombre de lignes contrôlé.
5. **Visualisation** : graphiques adaptés, honnêtes, sourcés.
6. **Interprétation** : causes, limites, recommandations : par l'humain, aidé par Claude.

#### C.2. Le dictionnaire de données

Un **dictionnaire de données** décrit chaque colonne d'un fichier : nom, signification, unité, type, valeurs autorisées, source. C'est le document le plus rentable que vous puissiez fournir à Claude : il évite les erreurs d'interprétation (tonnes ou kilotonnes ? minerai extrait ou traité ?).

*Tableau 33.1. Extrait du dictionnaire du fichier de production (fictif).*

| Colonne | Signification | Unité | Règle de validité |
|---|---|---|---|
| `minerai_traite_t` | Minerai alimenté à l'usine dans la journée | t | 0 à 8 000 |
| `teneur_alim_Cu_pct` | Teneur en cuivre de l'alimentation (moyenne journalière) | % | 0,5 à 5 |
| `recuperation_Cu_pct` | Récupération du cuivre de l'usine | % | 0 à 100 |
| `cathode_Cu_t` | Cuivre cathode produit | t | ≈ traité × teneur × récupération (± 5 %) |

#### C.3. Des indicateurs bien définis

Chaque indicateur du tableau de bord doit avoir une **fiche** : définition, formule, source, fréquence, responsable, seuils d'alerte. Fournissez ces fiches à Claude : il calculera selon **vos** définitions et non selon une définition générique.

#### C.4. Les pièges

| Piège | Exemple | Parade |
|---|---|---|
| Moyenne de pourcentages | Récupération mensuelle = moyenne des journées | Recalculer à partir des totaux |
| Moyenne non pondérée | Teneur moyenne de passes de longueurs différentes | Pondérer |
| Corrélation prise pour une cause | Jours de pluie et production | Formuler comme association ; vérifier |
| Axe tronqué | Écart de 2 % présenté comme un effondrement | Axes adaptés, valeurs affichées |
| Données manquantes ignorées | Mois avec une journée absente | Signaler la couverture |
| Unités mélangées | t et kt dans un même total | Dictionnaire de données |

### D. Démonstration guidée : Le tableau de bord mensuel de direction

**Étape 1. Cadrer.** Nadine liste 12 indicateurs avec la direction (production, coûts, sécurité, environnement, social), rédige leurs fiches et le dictionnaire des fichiers.

**Étape 2. Créer un projet** « Tableau de bord mensuel » contenant les fiches d'indicateurs, les dictionnaires et les instructions (prompt 33.1).

**Étape 3. Chaque mois** : déposer les fichiers du mois ; lancer le profil ; décider des corrections ; lancer les calculs ; produire l'artefact de tableau de bord (chapitre 15) ; vérifier ; diffuser.

**Étape 4. Conserver** le code de calcul : au fil des mois, Nadine demande à Claude de stabiliser le code dans un script réutilisable (éventuellement avec Claude Code par l'équipe données), ce qui rend le calcul identique d'un mois à l'autre.

### E. Prompts commentés

**Prompt 33.1. Instructions du projet « Tableau de bord »**

```text
RÔLE : tu assistes la contrôleuse de gestion de MCC pour le tableau de bord mensuel de direction.
RÉFÉRENCES (font foi) : fiches d'indicateurs et dictionnaires de données (connaissances du projet).
MÉTHODE OBLIGATOIRE :
1. Profil de chaque fichier ; signale les anomalies sans les corriger ; attends mes décisions.
2. Calculs uniquement par exécution de code, selon les fiches d'indicateurs ; affiche les formules.
3. Contrôles : nombre de lignes, couverture de la période, cohérence entre fichiers.
4. Graphiques : axes commençant à zéro pour les quantités, unités, source et période sous chaque graphique.
5. Commentaire : faits, puis associations observées formulées comme telles, puis questions ; aucune cause affirmée.
FORMAT : artefact tableau de bord + tableau des 12 indicateurs (valeur, budget, écart, tendance 3 mois, statut).
```

**Prompt 33.2. Stabiliser le code**

```text
Rassemble les calculs que tu as réalisés ce mois-ci dans un script Python unique, commenté,
qui lit les fichiers du mois, applique les contrôles, calcule les 12 indicateurs selon les fiches
et produit le tableau de synthèse. Ajoute des tests simples (par exemple : somme des effets = écart total).
```

*Commentaire.* Transformer un échange ponctuel en script testé est le passage de l'**usage** à la **méthode** : le calcul devient vérifiable, transmissible et constant.

### F. Exercices pratiques

**Exercice 33.1 (guidé).** Rédigez le dictionnaire de données du fichier `MCC_maintenance_ordres_travail.csv`.

**Exercice 33.2 (guidé).** Rédigez les fiches de 5 indicateurs (production, coût, sécurité, environnement, social) et produisez avec Claude un tableau de bord à partir des fichiers d'exercice.

**Exercice 33.3 (autonome).** Pour votre service, concevez un tableau de bord de 6 indicateurs, avec fiches, dictionnaires et script stabilisé.

### G. Livrable professionnel

**Tableau de bord mensuel** (artefact ou fichier) accompagné de son dossier de méthode : fiches d'indicateurs, dictionnaires de données, script de calcul, journal des anomalies et décisions.

### H. Vérification des résultats

::: controle
- Chaque indicateur est calculé selon sa fiche, avec formule visible.
- Les nombres de lignes et la couverture de la période sont vérifiés.
- Les graphiques respectent les règles d'honnêteté (axes, unités, source).
- Les anomalies et décisions de nettoyage sont journalisées.
- Deux indicateurs au moins sont recalculés indépendamment chaque mois.
:::

::: setrompe
Le tableau de bord affiche une récupération mensuelle de 89,2 %, calculée comme moyenne des valeurs journalières incluant la valeur aberrante de 121,4 %. Recalculée à partir des totaux et sans l'anomalie, la récupération est plus basse. **Contre-mesure** : fiches d'indicateurs explicites et profil préalable systématique.
:::

### I. Limites et précautions

- Un tableau de bord ne vaut que par la qualité des données sources.
- Les données consolidées peuvent devenir plus sensibles que les données isolées : classification à revoir.
- Les tableaux de bord vivants (connectés) exigent une gouvernance des accès.

### J. Boîte à outils

- Gabarit de fiche d'indicateur : nom | définition | formule | source | fréquence | responsable | seuils | limites.
- Gabarit de dictionnaire de données (tableau 33.1).
- Prompts 33.1 et 33.2.

### K. Quiz

1. **(QCM)** Quelle étape de la méthode reste humaine ? a) le profil ; b) le nettoyage décisionnel ; c) le calcul ; d) la visualisation.
2. **(Vrai ou faux)** La récupération mensuelle est la moyenne des récupérations journalières.
3. **(Compréhension)** Qu'est-ce qu'un dictionnaire de données ?
4. **(Application)** Rédigez la fiche de l'indicateur « taux de fréquence ».
5. **(Mise en situation)** Un graphique montre un « effondrement » de 2 % avec un axe commençant à 85 %. Que faites-vous ?
6. **(Vrai ou faux)** Conserver le code de calcul rend l'analyse reproductible.
7. **(Compréhension)** Pourquoi la consolidation de données peut-elle augmenter leur sensibilité ?
8. **(Analyse critique)** Pourquoi formuler les relations observées comme des « associations » ?
9. **(Application)** Citez trois contrôles automatiques à intégrer dans un script de tableau de bord.
10. **(Compréhension)** Quelle est la différence entre « usage » et « méthode » ?

<div class="carnet" titre="Chapitre 33. Analyser des données, exploiter des fichiers et construire des tableaux de bord"></div>
