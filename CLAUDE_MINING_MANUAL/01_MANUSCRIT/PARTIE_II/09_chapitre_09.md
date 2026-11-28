## Chapitre 9. Comprendre et maîtriser les paramètres de Claude

### A. Mise en situation professionnelle

Jean-Luc Tshibangu, métallurgiste en chef, utilise Claude pour analyser chaque semaine le bilan de l'usine. Certaines semaines, la réponse arrive en quelques secondes mais reste superficielle ; d'autres fois, Claude « réfléchit » longtemps et produit une analyse fouillée… pour une question simple. Parallèlement, l'équipe données de Kevin Mutombo prépare un petit outil interne qui appellera Claude via l'API pour résumer automatiquement les rapports de poste. Elle doit choisir des valeurs pour des paramètres dont personne, à l'usine, ne comprend le sens : `max_tokens`, `effort`, `thinking`, `system`.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Expliquer** le rôle des principaux réglages : modèle, effort, réflexion, contexte, longueur de réponse.
2. **Régler** l'effort selon la complexité de la tâche.
3. **Contrôler** la longueur et le format des réponses par l'instruction.
4. **Configurer** les réglages utiles de l'application (préférences, capacités, mémoire).
5. **Lire et comprendre** une requête simple à l'API Messages et ses paramètres principaux.

### C. Comprendre avant de pratiquer

#### C.1. Vue d'ensemble des réglages

| Réglage | Où ? | Effet |
|---|---|---|
| Modèle | Application et API | Capacités, vitesse, coût (chapitre 8) |
| Effort | API ; dans l'application selon l'offre et l'interface | Quantité de travail et de réflexion consacrée à la réponse |
| Réflexion (thinking) | API ; options de l'application | Raisonnement préalable à la réponse |
| Instructions système / préférences / instructions de projet | Application (préférences, projets) et API (`system`) | Rôle, règles et contexte permanents |
| Longueur maximale (`max_tokens`) | API | Plafond de la sortie, réflexion comprise |
| Format et longueur souhaités | Votre prompt | Structure, concision, ton |
| Outils (recherche Web, exécution de code, connecteurs) | Application et API | Capacités d'action et de vérification |

#### C.2. L'effort : régler l'intensité du travail

L'**effort** indique au modèle combien de tokens il peut consacrer à sa réponse : réflexion, texte et appels d'outils [@ANT-EFFORT]. La documentation décrit cinq niveaux :

![Figure 9.1. Les cinq niveaux d'effort. Plus l'effort est élevé, plus le modèle réfléchit, au prix d'un temps et d'un coût plus élevés. Source : Anthropic, Effort (consulté le 16/11/2026). Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig09_1_niveaux_effort.png){width=100%}

*Tableau 9.1. Niveaux d'effort (d'après la documentation Anthropic, consultée le 16/11/2026).*

| Niveau | Description selon la documentation | Usage typique à MCC |
|---|---|---|
| `low` | Le plus économe ; économies importantes avec une certaine réduction de capacité | Classement de libellés, reformulations, réponses courtes |
| `medium` | Approche équilibrée | Rédaction courante, synthèses, analyses simples |
| `high` | Autant de tokens que nécessaire pour un excellent résultat | Analyse d'un contrat, rapport complexe, raisonnement difficile |
| `xhigh` | Capacité étendue pour les travaux de longue durée | Travaux agentiques longs (plus de 30 minutes) |
| `max` | Capacité maximale, sans contrainte de consommation | Problèmes exceptionnellement difficiles ; gains souvent faibles au-delà de `xhigh` |

Valeurs par défaut via l'API : `medium` pour Claude Opus 5.5 et Claude Haiku 5.5, `high` pour Claude Fable 5.2 et Claude Sonnet 5.5 [@ANT-EFFORT; @ANT-MODELS]. La documentation précise que l'effort est un **signal de comportement**, pas un budget strict, et qu'il modifie peu la **longueur visible** des réponses : pour obtenir une réponse plus courte ou plus longue, il faut le demander dans le prompt [@ANT-EFFORT].

::: retenir
- **Effort** = combien Claude travaille (réflexion, vérifications, appels d'outils).
- **Prompt** = ce que Claude produit (longueur, format, ton).
Ne confondez pas les deux : pour une réponse plus courte, demandez-la ; pour une analyse plus fouillée, augmentez l'effort **et** précisez la méthode attendue.
:::

#### C.3. La réflexion adaptative

Les modèles actuels utilisent une **réflexion adaptative** : le modèle décide lui-même quand et combien réfléchir, en fonction de la difficulté et de l'effort demandé [@ANT-THINK; @ANT-MODELS]. Sur Claude Opus 5.5 et Claude Fable 5.2, la réflexion adaptative est toujours active ; l'effort est alors le levier principal pour régler la profondeur du raisonnement [@ANT-MODELS; @ANT-EFFORT]. Les anciens modèles utilisaient une réflexion « étendue » réglée par un budget de tokens ; ce mode est déprécié ou non accepté sur les modèles récents [@ANT-MODELS].

::: terrain
Dans l'application, lorsque Claude réfléchit, un résumé de sa réflexion peut être affiché. Parcourez-le pour les tâches importantes : il révèle parfois une hypothèse erronée (par exemple une mauvaise unité) avant même que vous lisiez la réponse.
:::

#### C.4. Le contexte et la longueur

- **Fenêtre de contexte** : un million de tokens pour les modèles actuels [@ANT-MODELS]. Dans l'application, la capacité réellement disponible peut dépendre de l'offre [@ANT-PLANS].
- **Sortie maximale** : 128 000 tokens via l'API synchrone pour les modèles actuels [@ANT-MODELS].
- **`max_tokens`** (API) : plafond absolu de la sortie, **réflexion comprise**. S'il est trop bas, la réponse peut être tronquée. La documentation recommande une valeur élevée aux niveaux d'effort élevés [@ANT-EFFORT].

#### C.5. Les paramètres techniques de l'API (pour les équipes techniques)

![Figure 9.2. Anatomie d'une requête à l'API Messages (exemple simplifié). Paramètres d'après la référence de l'API Messages consultée le 16/11/2026. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig09_2_requete_api.png){width=100%}

*Tableau 9.2. Paramètres principaux de l'API Messages (source : référence de l'API, consultée le 16/11/2026).*

| Paramètre | Rôle | Conseil |
|---|---|---|
| `model` | Identifiant du modèle (par exemple `claude-opus-5-5`) | Utiliser un identifiant figé pour les processus validés |
| `max_tokens` | Nombre maximal de tokens générés | Laisser de la marge pour la réflexion |
| `system` | Instructions système : rôle, règles, contexte permanent | Y placer les règles de l'entreprise |
| `messages` | Historique de la conversation (tours utilisateur / assistant) | Envoyer seulement le contexte utile |
| `thinking` | Mode de réflexion (par exemple adaptatif) | Laisser la valeur par défaut sauf besoin précis |
| `output_config.effort` | Niveau d'effort | Fixer explicitement et tester |
| `stop_sequences` | Chaînes qui arrêtent la génération | Utile pour des sorties strictement délimitées |
| `tools` | Outils mis à disposition du modèle | Voir chapitre 16 |
| `stream` | Réception progressive de la réponse | Recommandé pour les longues réponses |

Sources : [@ANT-API-MSG; @ANT-EFFORT; @ANT-THINK].

::: attention
De nombreux tutoriels plus anciens mentionnent d'autres paramètres d'échantillonnage (comme la « température »). Ils ne figurent pas dans la référence de l'API Messages consultée pour cet ouvrage. Pour les modèles actuels, **référez-vous uniquement à la documentation officielle de votre modèle** avant d'utiliser un paramètre.
:::

#### C.6. Les réglages de l'application

Pour l'utilisateur non technique, les réglages les plus utiles sont dans l'application : préférences personnelles, capacités (exécution de code et création de fichiers, recherche Web), mémoire et recherche dans les conversations passées, connecteurs, et, dans les organisations, les réglages imposés par l'administrateur [@ANT-HC-ARTIFACTS; @ANT-HC-MEMORY; @ANT-HC-CONNECT].

### D. Démonstration guidée : Régler l'analyse hebdomadaire de l'usine

Jean-Luc et Kevin définissent deux configurations.

**Configuration « point rapide » (lundi matin)** : modèle Sonnet 5.5, effort `low` ou `medium` (si l'interface le permet), prompt imposant une réponse de 10 lignes : chiffres clés, trois écarts principaux, une question à creuser.

**Configuration « analyse approfondie » (fin de mois)** : modèle Opus 5.5, effort `high`, exécution de code activée, prompt détaillant la méthode (bilan matière, récupération, consommation d'acide, causes possibles des écarts) et exigeant des calculs par programme.

Pour l'outil interne de résumé des rapports de poste, l'équipe données retient : `model` figé, `system` contenant les règles MCC (ne rien inventer, signaler les données manquantes, format fixe), `output_config.effort` à `low` (tâche simple et répétitive), `max_tokens` confortable, et des tests sur 30 rapports réels avant mise en service.

### E. Prompts commentés

**Prompt 9.1. Contrôler la longueur par l'instruction**

```text
Réponds en 10 lignes maximum, sous forme de liste :
- 3 chiffres clés de la semaine (avec unité) ;
- 3 écarts principaux par rapport au budget (avec valeur) ;
- 1 question à approfondir.
Pas d'introduction, pas de conclusion.
```

**Prompt 9.2. Instructions système pour un outil interne (API)**

```text
Tu résumes des rapports de poste de la mine Mbiyo (entreprise MCC).
Règles :
1. Utilise uniquement le contenu du rapport fourni.
2. N'invente aucun chiffre ; si une donnée manque, écris « non renseigné ».
3. Signale en tête tout événement de sécurité, environnemental ou d'arrêt > 1 h.
4. Format de sortie : exactement les rubriques
   SÉCURITÉ / PRODUCTION / ÉQUIPEMENTS / ENVIRONNEMENT / À SUIVRE.
5. Langue : français ; style télégraphique ; 150 mots maximum.
```

*Commentaire.* Placées dans le paramètre `system`, ces règles s'appliquent à chaque appel et garantissent un format constant, facile à contrôler et à intégrer dans un tableau de bord.

**Prompt 9.3. Demander davantage de rigueur sans changer de modèle**

```text
Cette analyse demande un raisonnement en plusieurs étapes. Avant de conclure :
1. vérifie les unités et les ordres de grandeur ;
2. recalcule les indicateurs avec l'exécution de code ;
3. liste les hypothèses que tu fais.
Puis donne ta conclusion.
```

### F. Exercices pratiques

**Exercice 9.1 (guidé) : Effort et longueur**

Sur une même question (analyse du rapport mensuel de mars 2026, fichier d'exercice), comparez deux réponses : effort faible avec consigne « 10 lignes », et effort élevé avec consigne « analyse détaillée ». Notez temps, longueur, qualité, erreurs.

**Exercice 9.2 (guidé, profil technique) : Lire une requête**

Expliquez, paramètre par paramètre, la requête de la figure 9.2 à un collègue non technicien.

**Exercice 9.3 (autonome) : Vos deux configurations**

Définissez une configuration « rapide » et une configuration « approfondie » pour deux tâches récurrentes de votre métier : modèle, effort, outils, consignes de longueur et de format.

### G. Livrable professionnel

**Fiche de configuration** (une par tâche récurrente) : objectif, modèle, effort, outils activés, consignes de format, contrôles, date du dernier test.

### H. Vérification des résultats

::: controle
- La réponse n'est pas tronquée (fin de phrase, dernier élément de liste présent).
- La longueur et le format correspondent à la consigne.
- Pour les configurations API : identifiant de modèle figé, `max_tokens` suffisant, tests réalisés sur un échantillon réel.
- Les réglages de l'application (capacités, mémoire) correspondent à la politique de l'entreprise.
:::

::: setrompe
Avec un effort très faible, sur une question en réalité complexe (par exemple l'interprétation d'une baisse de récupération), Claude peut répondre trop vite et proposer une cause unique évidente sans examiner les autres. **Contre-mesure** : augmentez l'effort et exigez l'examen de plusieurs hypothèses.
:::

### I. Limites et précautions

- Un effort élevé augmente le temps et la consommation sans garantir l'exactitude.
- Les réglages disponibles dans l'application peuvent différer de ceux de l'API.
- Toute modification de réglage d'un processus validé doit être testée et documentée.

### J. Boîte à outils

**Règles de réglage rapides**

| Situation | Réglage |
|---|---|
| Réponse trop longue | Préciser la longueur et le format dans le prompt |
| Réponse superficielle | Augmenter l'effort + préciser la méthode attendue |
| Réponse trop lente pour une tâche simple | Modèle plus léger et/ou effort plus faible |
| Réponse tronquée (API) | Augmenter `max_tokens` |
| Format irrégulier (API) | Règles dans `system` + format imposé + exemples |

### K. Quiz

1. **(QCM)** Quel paramètre règle la quantité de travail que Claude consacre à une réponse ? a) `stream` ; b) `effort` ; c) `stop_sequences` ; d) `model_name`.
2. **(Vrai ou faux)** Augmenter l'effort est le meilleur moyen d'obtenir une réponse plus courte.
3. **(Compréhension)** Que se passe-t-il si `max_tokens` est trop faible ?
4. **(QCM)** Selon la documentation consultée, quelle est la valeur d'effort par défaut via l'API pour Claude Opus 5.5 ? a) `low` ; b) `medium` ; c) `high` ; d) `max`.
5. **(Compréhension)** Où placer les règles permanentes d'un outil interne fondé sur l'API ?
6. **(Mise en situation)** Vos analyses mensuelles sont superficielles. Proposez trois ajustements.
7. **(Vrai ou faux)** Les tokens de réflexion comptent dans la limite `max_tokens`.
8. **(Analyse critique)** Pourquoi faut-il se méfier des tutoriels anciens décrivant des paramètres d'API ?
9. **(Application)** Rédigez une consigne de format pour obtenir un tableau de 5 lignes maximum.
10. **(QCM)** Le niveau `xhigh` est recommandé pour : a) classer des libellés ; b) des travaux agentiques longs ; c) traduire un courriel ; d) reformuler une phrase.

<div class="carnet" titre="Chapitre 9. Comprendre et maîtriser les paramètres de Claude"></div>
