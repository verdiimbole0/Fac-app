## Chapitre 7 — Créer son compte et prendre en main Claude

### A. Mise en situation professionnelle

Lundi matin, Béatrice Musau, responsable RH de MCC, reçoit son invitation au pilote « MCC-IA 2026 ». Elle n'a jamais utilisé d'assistant d'IA. Elle a vingt minutes avant sa première réunion et une question précise : préparer une trame d'entretien annuel pour les superviseurs de la mine. Comment se connecter, où écrire, comment joindre la fiche de poste, et surtout comment éviter les erreurs de débutant ?

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Accéder** à Claude depuis le Web, l'application de bureau et l'application mobile, avec le compte approprié.
2. **Repérer** les zones principales de l'interface.
3. **Mener** une première conversation utile, avec un fichier joint.
4. **Configurer** les réglages essentiels : préférences, capacités (exécution de code et création de fichiers), mémoire, confidentialité.
5. **Appliquer** les bonnes pratiques d'hygiène numérique dès le premier jour.

### C. Comprendre avant de pratiquer

#### C.1. Compte personnel ou compte d'entreprise ?

Il existe deux situations très différentes :

| Situation | Comment accéder | Ce qui s'applique |
|---|---|---|
| Usage professionnel dans une organisation abonnée (Team, Enterprise) | Invitation de l'administrateur ou connexion par l'authentification unique (SSO) de l'entreprise | Règles et réglages définis par l'organisation ; charte IA de l'entreprise |
| Usage individuel (Free, Pro, Max, Ultra) | Inscription sur claude.ai avec une adresse électronique ou un compte tiers | Vos propres réglages ; conditions grand public |

::: attention
N'utilisez **pas** un compte personnel pour des données professionnelles sans l'accord explicite de votre entreprise. À MCC, la charte IA impose l'usage exclusif des comptes de l'organisation pour toute donnée de l'entreprise.
:::

#### C.2. Les applications

Claude est disponible sur le Web, en application de bureau et en application mobile [@ANT-PLANS]. Les fonctions de base sont les mêmes ; certaines fonctions avancées (par exemple des extensions de bureau ou des connecteurs locaux) dépendent de l'application. L'application mobile est pratique sur le terrain — par exemple pour dicter une observation ou photographier une pièce —, mais attention à la confidentialité des photographies prises sur site.

#### C.3. Les zones de l'interface

![Figure 7.1 — Les zones principales de l'interface. Illustration schématique, et non capture d'écran : la disposition et les libellés réels peuvent différer selon la version, l'offre et la langue de l'interface.](02_ILLUSTRATIONS/CAPTURES_CLAUDE/fig07_1_interface_schematique.png){width=100%}

| Zone | Rôle |
|---|---|
| A. Nouvelle conversation | Ouvre une conversation vierge, sans l'historique des autres conversations |
| B. Barre latérale | Accès aux conversations passées, aux projets, aux artefacts, aux réglages |
| C. Zone de saisie et bouton « + » | Rédiger le message ; joindre des fichiers ; activer des outils (recherche, connecteurs) |
| D. Sélecteur de modèle | Choisir le modèle et, selon l'offre, les options de réflexion |

::: terrain
Les interfaces changent souvent. Plutôt que d'apprendre par cœur l'emplacement d'un bouton, apprenez **ce que vous cherchez** (joindre un fichier, choisir un modèle, ouvrir un projet) : vous le retrouverez quelle que soit la version.
:::

#### C.4. Les réglages à connaître dès le premier jour

| Réglage | À quoi il sert | Source |
|---|---|---|
| **Préférences / instructions personnelles** | Indiquer une fois pour toutes votre fonction, votre langue, votre style de réponse préféré | [@ANT-PLANS] (« user preferences ») |
| **Capacités : exécution de code et création de fichiers** | Indispensable pour analyser des tableurs, créer des fichiers et utiliser les artefacts | [@ANT-HC-ARTIFACTS] |
| **Mémoire et recherche dans les conversations** | Permettre (ou non) à Claude de se souvenir d'éléments de vos conversations précédentes | [@ANT-HC-MEMORY] |
| **Conversations incognito** | Conversation temporaire, non enregistrée dans l'historique et non utilisée par la mémoire | [@ANT-HC-MEMORY] |
| **Confidentialité (offres individuelles)** | Choisir si vos conversations peuvent servir à améliorer les modèles | [@ANT-HC-PRIVACY] |

Le centre d'aide précise par exemple que les artefacts nécessitent l'activation de l'exécution de code et de la création de fichiers dans les réglages des capacités (ou dans ceux de l'organisation pour les offres Team et Enterprise) [@ANT-HC-ARTIFACTS], et que la mémoire peut être consultée, modifiée ou supprimée par thème dans les réglages [@ANT-HC-MEMORY; @ANT-HC-RELEASE].

::: erreur
Laisser la mémoire mémoriser des informations sensibles sans le savoir. Avant d'utiliser Claude pour des sujets confidentiels, vérifiez les réglages de mémoire de votre compte et ce que votre organisation a configuré, et consultez régulièrement ce que Claude a retenu.
:::

### D. Démonstration guidée — La première demi-heure de Béatrice

**Étape 1 — Se connecter (2 min).** Béatrice clique sur le lien d'invitation reçu de l'administrateur, se connecte avec son identifiant d'entreprise et vérifie, en haut de la barre latérale ou dans les réglages, qu'elle est bien dans l'espace de l'organisation « MCC » et non dans un espace personnel.

**Étape 2 — Renseigner ses préférences (5 min).** Dans les réglages de profil, elle rédige un court texte de préférences (voir prompt 7.1). Ces préférences s'appliqueront à toutes ses conversations.

**Étape 3 — Vérifier les capacités (2 min).** Elle vérifie que l'exécution de code et la création de fichiers sont activées (ou que l'organisation les a activées), pour pouvoir obtenir un document Word en sortie.

**Étape 4 — Première conversation (10 min).** Elle ouvre une nouvelle conversation, joint la fiche de poste « Superviseur de poste — mine » (document interne de niveau « usage interne », autorisé par la charte), et utilise le prompt 7.2.

**Étape 5 — Itérer (8 min).** Elle demande deux modifications : ajouter une section sur la sécurité, et réduire la trame à deux pages. Elle télécharge le fichier produit.

**Étape 6 — Ranger (3 min).** Elle renomme la conversation « Trame entretien annuel superviseurs — v1 » pour la retrouver facilement.

### E. Prompts commentés

**Prompt 7.1 — Texte de préférences personnelles**

```text
Je suis responsable des ressources humaines dans une entreprise minière
(cuivre-cobalt, République démocratique du Congo, 2 350 personnes).
Réponds en français, avec un ton professionnel et clair.
Quand une question touche au droit du travail, rappelle que la réponse doit être
vérifiée au regard du droit applicable et des conventions de l'entreprise.
Préfère les réponses structurées (titres, listes, tableaux) et concises.
Signale toujours tes incertitudes.
```

*Commentaire.* Ce texte évite de répéter votre contexte dans chaque conversation. Il ne doit contenir **aucune donnée confidentielle** : il est réutilisé partout.

**Prompt 7.2 — Première tâche avec un fichier joint**

```text
Voici la fiche de poste « Superviseur de poste — mine » (fichier joint).
Prépare une trame d'entretien annuel d'évaluation pour ce poste, sous forme
de document Word de 2 pages maximum, avec :
1. un bilan de l'année (objectifs, réalisations, difficultés) ;
2. l'évaluation des compétences clés tirées de la fiche de poste ;
3. une rubrique sécurité (comportements, leadership sécurité de l'équipe) ;
4. les objectifs de l'année suivante (format SMART) ;
5. les besoins de formation ;
6. les commentaires de l'évalué et de l'évaluateur.
Utilise un langage neutre et non discriminant.
```

*Commentaire.* La demande de « document Word » mobilise la création de fichiers ; la mention « langage neutre et non discriminant » est une règle importante en RH.

### F. Exercices pratiques

**Exercice 7.1 (guidé) — Configurer son environnement**

1. Connectez-vous avec le compte approprié.
2. Rédigez votre texte de préférences (5 à 8 lignes) sur le modèle du prompt 7.1.
3. Vérifiez l'état des capacités (exécution de code, création de fichiers) et des réglages de mémoire ; notez-les.
4. Ouvrez une conversation incognito et vérifiez qu'elle n'apparaît pas dans l'historique.

**Exercice 7.2 (guidé) — Première production**

Avec le fichier d'exercice `MCC_rapport_mensuel_production_mars_2026.pdf`, demandez à Claude un résumé de cinq lignes pour le directeur général, puis une version en anglais. Renommez la conversation.

**Exercice 7.3 (autonome) — Votre première tâche réelle**

Choisissez une tâche simple et non confidentielle de votre travail (trame de document, plan de présentation, courrier type). Réalisez-la avec Claude en au plus trois itérations, puis notez le temps passé et la qualité perçue (1 à 5).

### G. Livrable professionnel

**Fiche « Mon environnement Claude »** : compte utilisé, préférences rédigées, état des capacités, réglages de mémoire et de confidentialité, règles de nommage de mes conversations, contacts d'assistance.

### H. Vérification des résultats

::: controle
- Je suis connecté au bon espace (organisation et non compte personnel) pour les données de l'entreprise.
- Mes préférences ne contiennent aucune donnée confidentielle.
- Je connais l'état de la mémoire et de l'historique de mon compte.
- Les fichiers produits ont été ouverts et relus avant usage.
:::

::: setrompe
Béatrice demande une trame « conforme au Code du travail ». Claude produit une trame correcte et ajoute une mention sur une « durée légale de conservation des évaluations de 5 ans ». Rien dans les documents fournis ne l'indiquait. **Contre-mesure** : demander la source précise de toute affirmation juridique, et la faire vérifier par le service juridique.
:::

### I. Limites et précautions

- Les réglages disponibles dépendent de l'offre et des choix de l'administrateur de l'organisation.
- L'application mobile est pratique, mais les photos et notes prises sur site peuvent contenir des informations sensibles (visages, installations, données) : appliquez la classification des données (chapitre 37).
- Ne communiquez jamais vos identifiants ; signalez toute connexion suspecte à l'informatique.

### J. Boîte à outils

**Règle de nommage des conversations (recommandée à MCC)**

`[Service] – [Objet] – [Version ou date]`, par exemple : `HSE – Rapport INC-2026-0412 – v2`.

**Check-list 7.1 — Premier jour**

- [ ] Connexion au bon espace.
- [ ] Préférences rédigées.
- [ ] Capacités vérifiées.
- [ ] Mémoire et confidentialité vérifiées.
- [ ] Charte IA lue.
- [ ] Première tâche non confidentielle réalisée.

### K. Quiz

1. **(Vrai ou faux)** On peut utiliser un compte gratuit personnel pour analyser des données confidentielles de l'entreprise si l'on supprime la conversation ensuite.
2. **(QCM)** Quelle capacité doit être activée pour utiliser les artefacts ? a) le mode vocal ; b) l'exécution de code et la création de fichiers ; c) la recherche approfondie ; d) la mémoire.
3. **(Compréhension)** À quoi servent les préférences personnelles ?
4. **(QCM)** Une conversation incognito : a) est partagée avec l'équipe ; b) n'est pas enregistrée dans l'historique ; c) utilise un autre modèle ; d) est réservée à l'administrateur.
5. **(Mise en situation)** Vous constatez que Claude « se souvient » d'un détail confidentiel d'une conversation précédente. Que faites-vous ?
6. **(Vrai ou faux)** Il est utile d'apprendre par cœur l'emplacement exact de chaque bouton de l'interface.
7. **(Application)** Proposez un nom de conversation conforme à la règle de nommage pour l'analyse du budget de juin du service maintenance.
8. **(Compréhension)** Pourquoi faut-il être prudent avec les photographies prises sur site avec l'application mobile ?
9. **(Analyse critique)** Pourquoi le texte de préférences ne doit-il contenir aucune donnée confidentielle ?
10. **(QCM)** Dans une organisation Team ou Enterprise, qui contrôle certains réglages comme la disponibilité de la mémoire ? a) chaque utilisateur seul ; b) les propriétaires ou administrateurs de l'organisation ; c) personne ; d) le fournisseur d'accès Internet.

<div class="carnet" titre="Chapitre 7 — Créer son compte et prendre en main Claude"></div>
