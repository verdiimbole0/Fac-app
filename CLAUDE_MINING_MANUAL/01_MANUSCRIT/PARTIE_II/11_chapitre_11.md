## Chapitre 11. Les techniques avancées de prompting

### A. Mise en situation professionnelle

Michel Lwamba, responsable de l'audit interne de MCC, doit auditer le processus d'achats. Il dispose de 300 bons de commande, de la procédure d'achat, de la matrice des délégations de pouvoir et de trois rapports d'audit antérieurs. Une seule instruction, même bien construite avec CADRE, ne suffit pas : il faut extraire, contrôler, analyser, rédiger, puis relire. Michel découvre que les meilleurs résultats viennent non pas d'une instruction « géante », mais d'une **séquence** d'instructions plus simples, chacune contrôlée.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Utiliser** les exemples (apprentissage par l'exemple) pour obtenir un format et un style constants.
2. **Structurer** une instruction complexe avec des balises.
3. **Découper** une tâche complexe en chaîne d'instructions avec points de contrôle.
4. **Faire critiquer** un résultat par Claude selon une grille explicite.
5. **Obtenir** des sorties structurées exploitables (tableaux, listes normalisées).
6. **Construire** des modèles d'instructions réutilisables à variables.

### C. Comprendre avant de pratiquer

#### C.1. Attribuer un rôle

Donner un rôle à Claude (« tu es auditeur interne expérimenté dans le secteur minier ») oriente son comportement et son ton ; la documentation d'Anthropic note qu'une seule phrase suffit déjà à faire une différence [@ANT-PROMPT]. Le rôle complète le contexte, il ne le remplace pas.

::: erreur
Croire qu'un rôle confère une compétence réelle. « Tu es un géotechnicien expert » n'apporte à Claude aucune donnée de terrain ni aucune responsabilité professionnelle. Le rôle oriente le style et le niveau d'exigence ; les faits viennent des données.
:::

#### C.2. Montrer plutôt que décrire : les exemples

Les exemples sont l'un des moyens les plus fiables de contrôler le format, le ton et la structure d'une réponse. La documentation recommande des exemples **pertinents** (proches du cas réel), **variés** (couvrant les cas limites) et **structurés** (clairement délimités) [@ANT-PROMPT]. On parle d'apprentissage « par quelques exemples » (*few-shot*).

![Figure 11.1. L'apprentissage par l'exemple. Quelques exemples variés suffisent souvent pour que Claude reproduise le format et la logique de classement. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig11_2_exemples.png){width=85%}

#### C.3. Structurer avec des balises

Quand une instruction mélange consignes, documents et exemples, des **balises** (`<procedure>`, `<exemple>`, `<donnees>`) évitent les confusions. Elles permettent aussi de demander une sortie balisée, facile à extraire. Il n'existe pas de liste « officielle » de balises : choisissez des noms explicites et utilisez-les de façon cohérente [@ANT-PROMPT].

#### C.4. Chaîner les instructions

Le **chaînage** consiste à découper une tâche complexe en étapes successives, la sortie de l'une alimentant la suivante. Avantages : chaque étape est plus simple, donc plus fiable ; vous pouvez **contrôler** entre deux étapes ; une erreur est localisée et corrigée sans tout refaire.

![Figure 11.2. Le chaînage d'instructions. Chaque étape peut être suivie d'un point de contrôle humain. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig11_1_chainage.png){width=100%}

#### C.5. Faire réfléchir, faire vérifier, faire critiquer

- **Réflexion** : les modèles actuels réfléchissent de façon adaptative (chapitre 9). Pour les tâches complexes, la documentation conseille de préférer des **instructions générales** (« réfléchis soigneusement, examine plusieurs hypothèses ») à des étapes trop prescriptives, et de demander au modèle de **vérifier son travail** avant de conclure [@ANT-PROMPT].
- **Auto-critique avec grille** : demander à Claude d'évaluer sa réponse selon des critères explicites (exactitude, complétude, conformité au format, risques) puis de la corriger.
- **Points de vue multiples** : « Analyse ce projet du point de vue du directeur financier, du responsable HSE et du chef du village riverain. »
- **Pré-mortem** : « Imagine que ce plan d'action a échoué dans six mois. Quelles en seraient les causes probables ? »
- **Comparaison de réponses** : relancer la même question et comparer ; des divergences signalent une zone d'incertitude [@ANT-HALLU].

#### C.6. Les sorties structurées

Pour qu'un résultat soit exploitable (tableur, base de données, tableau de bord), imposez une structure stricte : colonnes nommées, valeurs autorisées, unités, une ligne par élément. Fournissez un exemple de ligne. Pour les échanges entre logiciels via l'API, l'équipe technique peut demander des formats de données normalisés.

#### C.7. Les modèles à variables

Un **modèle d'instruction** (gabarit) contient des variables entre crochets : `[NOM_FOURNISSEUR]`, `[PÉRIODE]`. Il garantit la constance d'un processus et facilite le partage dans l'équipe (bibliothèque de l'Annexe B, compétences « Skills » au chapitre 16).

### D. Démonstration guidée : La chaîne d'audit de Michel

**Étape 1. Extraire.** Michel joint le fichier des bons de commande et la matrice des délégations. Il demande l'extraction structurée des commandes proches des seuils d'approbation (prompt 11.1).

*Contrôle 1 :* il vérifie sur 10 lignes que les montants extraits correspondent au fichier.

**Étape 2. Détecter les anomalies.** Il demande, par exécution de code, la recherche de commandes fractionnées (même fournisseur, même jour, montants juste sous le seuil) et de doublons.

*Contrôle 2 :* il ouvre le fichier et confirme les trois commandes de 9 800 USD du 14 mars 2026 à un même fournisseur, et le doublon BC-60999 / BC-60012.

**Étape 3. Analyser.** Il demande, pour chaque anomalie, les risques associés et les questions à poser aux responsables, en se référant à la procédure.

**Étape 4. Rédiger.** Il demande la rédaction des constats au format du rapport d'audit interne (constat, critère, cause présumée, risque, recommandation), avec des exemples tirés d'un ancien rapport.

**Étape 5. Critiquer.** Il fait relire le projet par Claude selon la grille de qualité de l'audit interne (prompt 11.4), puis le relit lui-même.

Les anomalies détectées sont celles insérées dans les données d'exercice (voir `ANOMALIES_ATTENDUES.md`) : la chaîne a fonctionné, et chaque constat est traçable jusqu'aux lignes du fichier.

### E. Prompts commentés

**Prompt 11.1. Extraction structurée avec exemple**

```text
<role>Tu es auditeur interne dans une entreprise minière.</role>

<donnees>Fichier joint : MCC_bons_de_commande.csv (séparateur ;, ligne 1 = bandeau à ignorer).
Seuil d'approbation du chef de service : 10 000 USD.</donnees>

<tache>Avec l'exécution de code, liste les commandes dont le montant est compris
entre 9 000 et 10 000 USD, ainsi que les groupes de commandes d'un même fournisseur
passées le même jour dont la somme dépasse 10 000 USD.</tache>

<format>Tableau : bc | date | fournisseur | montant_USD | motif_signalement.
Exemple de ligne :
BC-60123 | 2025-07-02 | Fournisseur X | 9 750,00 | proche du seuil
</format>

<regles>Aucune conclusion sur une fraude : il s'agit de signalements à investiguer.
Indique le nombre total de lignes analysées.</regles>
```

*Commentaire.* Balises, rôle, exemple de ligne et règle de prudence (« signalements à investiguer ») : la sortie est directement exploitable dans un papier de travail d'audit.

**Prompt 11.2. Classement avec exemples (few-shot)**

```text
Classe chaque incident selon : catégorie (Sécurité / Santé / Environnement / Matériel)
et gravité potentielle (1 à 5) selon la grille ci-dessous. Justifie en une phrase.

<grille> 1 = sans blessure possible ; 3 = blessure avec arrêt possible ;
5 = décès ou atteinte grave possible </grille>

<exemples>
<exemple>Incident : « Fuite hydraulique sur camion, huile au sol en atelier »
Catégorie : Environnement | Gravité potentielle : 2 | Justification : pollution limitée et confinée.</exemple>
<exemple>Incident : « Camion recule sans signal sonore près d'un piéton »
Catégorie : Sécurité | Gravité potentielle : 5 | Justification : écrasement possible d'une personne.</exemple>
</exemples>

<incidents> [liste] </incidents>

Règle : cette classification est une proposition, validée ensuite par le responsable HSE.
Marque « à revoir » tout cas ambigu.
```

**Prompt 11.3. Pré-mortem**

```text
Voici notre plan d'action pour réduire les incidents sur les rampes : [plan].
Imagine que, dans six mois, le nombre d'incidents n'a pas baissé.
Liste les 8 causes les plus plausibles de cet échec (organisationnelles, humaines,
techniques, de suivi), et pour chacune, une mesure préventive à ajouter au plan.
```

**Prompt 11.4. Critique selon une grille**

```text
Relis le projet de rapport ci-dessous selon cette grille, et note chaque critère de 1 à 5 :
1. Exactitude : chaque fait est-il étayé par une pièce ?
2. Complétude : constat, critère, cause, risque, recommandation présents ?
3. Clarté : compréhensible par un directeur non auditeur ?
4. Proportionnalité : la recommandation est-elle à la mesure du risque ?
5. Ton : factuel, sans accusation nominative ?
Pour chaque note inférieure à 4, propose une correction précise.
<projet> … </projet>
```

**Prompt 11.5. Faire écrire une instruction par Claude (méta-prompt)**

```text
Je dois répéter chaque mois la tâche suivante : [description].
Rédige pour moi une instruction réutilisable selon la méthode CADRE
(Contexte, Action, Données, Règles, Exigences de sortie), avec des variables
entre crochets pour ce qui change chaque mois, et une check-list de contrôle du résultat.
```

### F. Exercices pratiques

**Exercice 11.1 (guidé) : Few-shot sur les incidents**

Avec 20 lignes de `MCC_incidents_HSE_2025_2026.csv`, testez le prompt 11.2 sans exemples, puis avec exemples. Comparez la constance des classements.

**Exercice 11.2 (guidé) : Chaîne en trois étapes**

Avec `MCC_registre_plaintes.csv` : (1) classer les plaintes par thème et village ; (2) calculer les délais de traitement par catégorie (exécution de code) ; (3) rédiger une synthèse de 300 mots pour le comité de direction. Notez un contrôle entre chaque étape.

**Exercice 11.3 (autonome) : Votre gabarit à variables**

Transformez votre meilleure instruction du chapitre 10 en gabarit à variables, avec sa check-list de contrôle, et faites-la tester par un collègue.

### G. Livrable professionnel

**Une chaîne d'instructions documentée** pour un processus de votre métier : schéma des étapes, instruction de chaque étape, point de contrôle associé, format de sortie de chaque étape.

### H. Vérification des résultats

::: controle
- Chaque étape d'une chaîne a été contrôlée avant de passer à la suivante.
- Les exemples fournis sont représentatifs et ne contiennent pas d'erreur (Claude reproduirait l'erreur).
- Les sorties structurées respectent exactement les colonnes et valeurs autorisées.
- L'auto-critique de Claude a été suivie d'une relecture humaine.
:::

::: setrompe
Dans une chaîne, une petite erreur à l'étape 1 (une ligne non lue) se propage aux étapes suivantes et produit une conclusion bien rédigée mais fausse. **Contre-mesure** : à chaque étape, demandez le nombre d'éléments traités et comparez-le au nombre attendu.
:::

### I. Limites et précautions

- Les exemples influencent fortement la réponse : un exemple biaisé produit des résultats biaisés.
- Une auto-critique par le même modèle ne vaut pas une revue indépendante.
- Les chaînes longues demandent du temps : réservez-les aux tâches qui le justifient.

### J. Boîte à outils

**Panorama des techniques**

| Technique | Quand l'utiliser |
|---|---|
| Rôle | Pour fixer le niveau d'exigence et le ton |
| Exemples | Pour un format ou un classement constant |
| Balises | Dès qu'il y a plusieurs sources ou consignes |
| Chaînage | Pour les tâches en plusieurs étapes |
| Questions préalables | Quand vous ne savez pas quel contexte fournir |
| Auto-critique avec grille | Pour améliorer un livrable avant relecture |
| Points de vue multiples | Pour les décisions à plusieurs parties prenantes |
| Pré-mortem | Pour éprouver un plan d'action |
| Sortie structurée | Pour alimenter un tableur ou un tableau de bord |
| Gabarit à variables | Pour les tâches répétitives et le partage d'équipe |

### K. Quiz

1. **(QCM)** L'apprentissage « par quelques exemples » sert principalement à : a) accélérer la réponse ; b) obtenir un format et un style constants ; c) réduire le prix ; d) activer la recherche Web.
2. **(Vrai ou faux)** Attribuer le rôle de « géotechnicien expert » à Claude lui permet d'évaluer la stabilité d'une digue.
3. **(Compréhension)** Citez deux avantages du chaînage d'instructions.
4. **(Application)** Rédigez une consigne de pré-mortem pour un plan de réduction de la consommation d'acide.
5. **(QCM)** Quelles qualités les exemples doivent-ils avoir selon la documentation d'Anthropic ? a) longs et nombreux ; b) pertinents, variés, structurés ; c) identiques ; d) en anglais.
6. **(Mise en situation)** Dans une chaîne, le total de l'étape 3 ne correspond pas à celui du fichier. Comment localisez-vous l'erreur ?
7. **(Vrai ou faux)** Une auto-critique de Claude remplace la relecture humaine.
8. **(Compréhension)** À quoi servent les balises dans une instruction ?
9. **(Analyse critique)** Quel est le risque d'un exemple contenant une erreur ?
10. **(Application)** Transformez en gabarit à variables : « Résume le rapport de production de mars 2026 pour le DG. »

<div class="carnet" titre="Chapitre 11. Les techniques avancées de prompting"></div>
