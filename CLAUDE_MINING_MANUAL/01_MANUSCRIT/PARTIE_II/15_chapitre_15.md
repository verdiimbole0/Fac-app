## Chapitre 15 — Découvrir Projects, Artifacts et les espaces de travail

### A. Mise en situation professionnelle

Chaque mois, Grace Nsimba rédige le rapport HSE de MCC. Et chaque mois, elle recommence la même routine : rappeler à Claude le contexte de la mine, recoller le modèle de rapport, rejoindre la liste des indicateurs et leurs définitions, réexpliquer les règles de rédaction. Trente minutes perdues avant même de commencer. De son côté, la direction aimerait voir les indicateurs HSE dans un tableau de bord consultable, plutôt que dans une pièce jointe de courriel.

Deux fonctions répondent à ces besoins : les **projets**, qui conservent le contexte d'un dossier récurrent, et les **artefacts**, qui produisent des documents, tableaux de bord et présentations modifiables et partageables.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Expliquer** ce qu'est un projet et ce qu'il apporte par rapport à une conversation isolée.
2. **Créer et configurer** un projet : instructions, connaissances, conversations.
3. **Expliquer** ce qu'est un artefact et les principaux modèles disponibles.
4. **Produire** un artefact (document, tableau de bord) et le faire évoluer.
5. **Appliquer** les règles de partage et de confidentialité propres aux projets et aux artefacts.

### C. Comprendre avant de pratiquer

#### C.1. Les projets

Selon le centre d'aide, les projets permettent de créer des **espaces de travail autonomes**, chacun avec son propre historique de conversations et sa propre **base de connaissances** : on peut y déposer des documents, fournir un contexte et y mener des conversations ciblées [@ANT-HC-PROJECTS]. Les projets sont accessibles à tous les utilisateurs ; l'offre gratuite est limitée à cinq projets.

Un projet comporte trois éléments :

| Élément | Rôle | Exemple pour le rapport HSE |
|---|---|---|
| **Instructions du projet** | Rôle, règles, format, ton applicables à toutes les conversations du projet | « Tu assistes la responsable HSE de MCC… Format du rapport en 6 rubriques… N'invente aucun chiffre… » |
| **Connaissances du projet** | Documents de référence toujours disponibles | Modèle de rapport, définitions des indicateurs, procédure de déclaration, rapports des mois précédents |
| **Conversations** | Les travaux successifs | Rapport de janvier, rapport de février, analyse trimestrielle |

Pour les offres payantes, lorsque les connaissances du projet approchent des limites du contexte, un mode de **recherche documentaire augmentée** (RAG, *Retrieval Augmented Generation*) s'active : Claude recherche les passages pertinents au lieu de tout charger, ce qui augmente la capacité du projet jusqu'à dix fois selon le centre d'aide [@ANT-HC-PROJECTS]. Les fichiers de projet sont limités à 30 Mo chacun [@ANT-HC-UPLOAD].

**Partage (offres Team et Enterprise)** : un projet peut être partagé avec des collègues de l'organisation, avec des droits « peut consulter » (lire et converser dans le projet) ou « peut modifier » (modifier instructions et connaissances, gérer les membres) ; les administrateurs peuvent désactiver le partage [@ANT-HC-PROJECTS].

::: terrain
Le centre d'aide signale qu'une **nouvelle version des projets** est en cours de déploiement progressif (d'abord dans Claude Code), dans laquelle un projet fonctionne comme une conversation unique qui répartit le travail en tâches parallèles exécutées dans le cloud [@ANT-HC-PROJECTS]. Les principes de ce chapitre — contexte permanent, documents de référence, règles communes — restent valables quelle que soit la version.
:::

#### C.2. Les artefacts

Un **artefact** est un contenu substantiel et autonome que Claude crée et que vous pouvez modifier, réutiliser et partager : document, extrait de code, page Web, diagramme, tableau de bord, petit outil interactif [@ANT-HC-ARTIFACTS]. Depuis septembre 2026, on peut partir de **modèles** (*templates*) :

*Tableau 15.1 — Modèles d'artefacts (d'après le centre d'aide, consulté le 16/11/2026).*

| Modèle | Usage | Exemple minier |
|---|---|---|
| Docs | Documents vivants rédigés avec Claude et l'équipe | Procédure de consignation co-rédigée par la maintenance et le HSE |
| Slides | Présentations éditables, exportables en PowerPoint ou PDF | Présentation du rapport trimestriel au comité de direction |
| Design | Visuels, maquettes, one-pagers | Affiche de campagne sécurité |
| Data | Tableaux de bord et récits de données à partir de sources connectées | Tableau de bord HSE mensuel |
| Sheets (bêta) | Tableurs avec formules, édités à deux | Suivi des actions correctives |
| Whiteboards (bêta) | Tableau blanc partagé | Atelier d'analyse de risques |
| Motion (bêta, Team et Enterprise) | Explications animées exportables en vidéo | Module de formation sur les EPI |

Les artefacts nécessitent l'activation de l'exécution de code et de la création de fichiers ; la disponibilité de certains modèles dépend de l'offre [@ANT-HC-ARTIFACTS]. Tous les artefacts créés sont retrouvés dans l'onglet « Artefacts » de la barre latérale.

![Figure 15.1 — Organiser son travail : un projet regroupe instructions, connaissances et conversations ; les conversations produisent des artefacts modifiables et partageables. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig15_1_projets_artefacts.png){width=100%}

::: attention
**Partager un artefact ou un projet, c'est diffuser son contenu.** Vérifiez la classification des informations avant tout partage, et privilégiez le partage à l'intérieur de l'organisation. Ne publiez jamais d'artefact contenant des données confidentielles à l'extérieur.
:::

### D. Démonstration guidée — Le projet « Rapports HSE mensuels »

**Étape 1 — Créer le projet.** Grace crée le projet « HSE — Rapports mensuels MCC ».

**Étape 2 — Rédiger les instructions** (prompt 15.1).

**Étape 3 — Déposer les connaissances** : modèle de rapport (Word), définitions des indicateurs (taux de fréquence, taux de gravité, presque-accidents, etc.), procédure de déclaration des incidents, rapports validés des trois derniers mois. Elle vérifie que ces documents sont de niveau « usage interne ».

**Étape 4 — Travailler.** Pour le rapport d'avril, elle ouvre une conversation dans le projet, joint l'extraction du registre d'incidents du mois et demande le rapport. Plus besoin de réexpliquer le contexte.

**Étape 5 — Produire un artefact.** Elle demande un tableau de bord HSE (artefact) : nombre d'incidents par type et par zone, évolution sur 12 mois, statut des actions. Elle le fait évoluer (ajout d'un filtre par zone), puis le partage en lecture avec le directeur des opérations.

**Étape 6 — Partager le projet** avec ses deux techniciens HSE (droit « peut consulter ») pour qu'ils préparent les sections de leurs zones.

### E. Prompts commentés

**Prompt 15.1 — Instructions d'un projet**

```text
RÔLE : tu assistes la responsable HSE de Mbiyo Copper Cobalt SA (mine de cuivre-cobalt
à ciel ouvert, RDC, 2 350 personnes dont 900 sous-traitants).

OBJET DU PROJET : préparation des rapports HSE mensuels et trimestriels.

DOCUMENTS DE RÉFÉRENCE (connaissances du projet) : modèle de rapport, définitions
des indicateurs, procédure de déclaration, rapports validés des mois précédents.
En cas de contradiction, les définitions des indicateurs font foi.

RÈGLES :
1. Utilise uniquement les données fournies pour le mois concerné ; n'invente aucun chiffre.
2. Calcule les indicateurs avec l'exécution de code, selon les définitions de référence.
3. Ne cite aucun nom de personne impliquée dans un incident.
4. Distingue faits établis et analyses ; n'attribue aucune cause avant la clôture de l'enquête.
5. Signale toute donnée manquante ou incohérente en tête de réponse.

FORMAT : suivre exactement le modèle de rapport (6 rubriques), ton factuel, 3 pages maximum.
```

*Commentaire.* Ces instructions sont une application de CADRE à l'échelle d'un projet : elles évitent de répéter contexte, règles et format à chaque conversation, et garantissent la constance d'un mois sur l'autre.

**Prompt 15.2 — Créer un tableau de bord en artefact**

```text
À partir du fichier joint (extraction du registre d'incidents 2025-2026), crée un tableau
de bord interactif (artefact) comprenant :
- nombre d'incidents par mois sur 12 mois (graphique en barres) ;
- répartition par type et par zone (deux graphiques) ;
- tableau des actions en retard ;
- un filtre par zone.
Indique sous chaque graphique la période et la source des données.
Couleurs sobres ; titres en français.
```

**Prompt 15.3 — Faire évoluer un artefact**

```text
Dans le tableau de bord, ajoute un indicateur « presque-accidents / incidents avec blessure »
par trimestre, avec une phrase d'explication de cet indicateur pour la direction.
Ne modifie pas les autres éléments.
```

### F. Exercices pratiques

**Exercice 15.1 (guidé) — Votre premier projet**

Créez un projet pour une tâche récurrente de votre métier. Rédigez des instructions selon le modèle du prompt 15.1, déposez 2 à 4 documents de référence autorisés, et réalisez une première tâche.

**Exercice 15.2 (guidé) — Tableau de bord**

Avec `MCC_incidents_HSE_2025_2026.csv`, créez l'artefact du prompt 15.2. Vérifiez trois chiffres du tableau de bord directement dans le fichier.

**Exercice 15.3 (autonome) — Présentation**

À partir d'un rapport de votre choix, créez une présentation de 6 diapositives (modèle Slides) pour votre direction, puis exportez-la. Relisez chaque chiffre.

### G. Livrable professionnel

**Un projet configuré et documenté** (fiche : objet, instructions, liste des connaissances avec version et classification, membres et droits) et **un artefact** (tableau de bord ou présentation) vérifié.

### H. Vérification des résultats

::: controle
- Les connaissances du projet sont à jour, versionnées et de classification compatible.
- Les instructions du projet contiennent une règle de vérité et une règle de format.
- Les chiffres d'un artefact ont été contrôlés par sondage dans les données sources.
- Les droits de partage correspondent au besoin (principe du moindre privilège).
:::

::: setrompe
Un document de référence obsolète (définitions d'indicateurs de 2024) est resté dans les connaissances du projet à côté de la version 2026. Claude calcule le taux de fréquence selon l'ancienne définition. **Contre-mesure** : une seule version de chaque document de référence dans le projet, et une règle « en cas de contradiction, tel document fait foi ».
:::

### I. Limites et précautions

- Un projet partagé est un **espace commun** : ce qu'un membre y dépose est visible des autres membres.
- Les fonctions en bêta peuvent évoluer ou présenter des limites ; évitez de bâtir un processus critique sur une fonction bêta sans solution de repli.
- Un tableau de bord ne remplace pas le système de reporting officiel tant qu'il n'a pas été validé.

### J. Boîte à outils

**Fiche de création de projet**

| Rubrique | À compléter |
|---|---|
| Nom du projet | `[Service] – [Objet]` |
| Objet | |
| Instructions (CADRE) | |
| Connaissances (titre, version, classification) | |
| Membres et droits | |
| Responsable du projet | |
| Date de revue | |

### K. Quiz

1. **(QCM)** Un projet regroupe : a) uniquement des fichiers ; b) des instructions, des connaissances et des conversations ; c) des identifiants ; d) des modèles d'IA.
2. **(Vrai ou faux)** Les projets sont réservés aux offres payantes.
3. **(Compréhension)** À quoi sert le mode RAG des projets sur les offres payantes ?
4. **(QCM)** Quel modèle d'artefact convient à une présentation pour le comité de direction ? a) Docs ; b) Slides ; c) Whiteboards ; d) Motion.
5. **(Vrai ou faux)** Les artefacts nécessitent l'activation de l'exécution de code et de la création de fichiers.
6. **(Mise en situation)** Un collègue veut partager publiquement un tableau de bord contenant des données de production. Que lui répondez-vous ?
7. **(Compréhension)** Quelle est la différence entre les droits « peut consulter » et « peut modifier » d'un projet partagé ?
8. **(Application)** Rédigez la règle de priorité à inscrire dans les instructions d'un projet contenant plusieurs documents de référence.
9. **(Analyse critique)** Pourquoi faut-il éviter de bâtir un processus critique sur une fonction en bêta ?
10. **(QCM)** Quelle est la taille maximale d'un fichier de projet selon le centre d'aide ? a) 5 Mo ; b) 30 Mo ; c) 500 Mo ; d) illimitée.

<div class="carnet" titre="Chapitre 15 — Découvrir Projects, Artifacts et les espaces de travail"></div>
