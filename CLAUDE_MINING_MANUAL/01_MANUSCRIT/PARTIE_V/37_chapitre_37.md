## Chapitre 37 — Confidentialité et protection des données minières

### A. Mise en situation professionnelle

Un vendredi soir, un ingénieur de MCC, pressé, copie dans son compte personnel d'un assistant d'IA grand public le projet d'estimation des réserves de l'extension « Mbiyo Profond » — non publié — pour « faire relire la syntaxe ». Le lundi, le service informatique le découvre lors d'un contrôle. Rien ne prouve que l'information ait fuité. Mais l'entreprise ne peut plus garantir sa confidentialité : la donnée est sortie de son périmètre de maîtrise. Pour une information susceptible d'intéresser les marchés et les partenaires, c'est un incident sérieux.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Classer** une information selon les quatre niveaux de la classification de MCC.
2. **Appliquer** les règles d'usage de Claude correspondant à chaque niveau.
3. **Minimiser et pseudonymiser** les données avant tout traitement.
4. **Comprendre** les paramètres de confidentialité de l'outil et les conditions contractuelles.
5. **Réagir** correctement en cas d'incident de données.

### C. Comprendre avant de pratiquer

#### C.1. Les données sensibles d'une entreprise minière

| Catégorie | Exemples | Pourquoi c'est sensible |
|---|---|---|
| Géologiques et techniques | Résultats d'exploration non publiés, ressources et réserves, plans miniers | Valeur stratégique ; information privilégiée pour une société cotée |
| Commerciales | Contrats, prix, offres, négociations | Concurrence, obligations contractuelles de confidentialité |
| Financières et fiscales | Résultats non publiés, positions fiscales | Marchés, administration, litiges |
| Personnelles | Données RH, santé, incidents nominatifs, plaintes | Droits des personnes, obligations légales |
| Communautaires | Données sur les ménages réinstallés, plaintes | Vulnérabilité des personnes, tensions |
| Sécurité | Plans de sûreté, stocks d'explosifs, transports de cathodes | Risques de malveillance |
| Juridiques | Contentieux, stratégie, avis | Secret professionnel, position de l'entreprise |

#### C.2. La classification de MCC

![Figure 37.1 — Classification des données de MCC et usage autorisé de Claude (modèle fictif détaillé à l'Annexe G). Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig37_1_classification_donnees.png){width=92%}

| Niveau | Définition | Usage de Claude à MCC |
|---|---|---|
| 1 — Public | Information publiée ou destinée à l'être | Libre (vérifier que l'information est réellement publique) |
| 2 — Usage interne | Diffusion interne sans dommage notable en cas de fuite | Espace d'entreprise uniquement |
| 3 — Confidentiel | Dommage significatif en cas de fuite | Espace d'entreprise, accord du propriétaire de la donnée, minimisation |
| 4 — Restreint | Dommage grave ; diffusion nominative | Interdit dans Claude |

#### C.3. Ce que dit l'outil — et ce que décide l'entreprise

Les règles d'utilisation des données diffèrent selon les offres (chapitre 4) : pour les offres grand public, la page des offres indique un fonctionnement par exclusion volontaire pour l'usage des conversations à des fins d'entraînement, avec un paramètre dédié [@ANT-PLANS; @ANT-HC-PRIVACY] ; pour les offres commerciales, les conditions contractuelles s'appliquent ; la politique de confidentialité décrit le traitement des données personnelles [@ANT-PRIV-POL]. Les offres d'entreprise offrent en outre des contrôles d'administration (authentification unique, gestion des accès, contrôles de connecteurs, et, selon les offres, journalisation et autres fonctions de sécurité) [@ANT-PLANS; @ANT-HC-RELEASE].

Mais la question n'est pas seulement « que fait le fournisseur ? » ; c'est aussi « **qu'avons-nous le droit de faire ?** » : engagements de confidentialité dans les contrats, réglementation sur les données personnelles, règles boursières, secret professionnel. C'est l'entreprise qui fixe ces règles, dans sa charte (Annexe F) et sa politique de classification (Annexe G).

#### C.4. Minimiser et pseudonymiser

- **Minimiser** : ne transmettre que les données nécessaires à la tâche (une colonne, un extrait, un échantillon).
- **Pseudonymiser** : remplacer les noms par des codes (matricules, « Témoin A ») ; la table de correspondance reste hors de l'outil.
- **Agréger** : transmettre des totaux plutôt que des données individuelles quand c'est suffisant.
- **Anonymiser** pour toute diffusion large, en se méfiant de la ré-identification (dans un petit village, « la femme du chef de quartier qui a perdu son champ » est identifiable).

::: attention
La mémoire, les projets partagés et les connecteurs étendent la portée de ce que vous transmettez : une information confidentielle déposée dans un projet partagé devient visible de tous ses membres ; une information retenue par la mémoire peut ressurgir ailleurs. Vérifiez ces réglages (chapitres 12 et 15).
:::

#### C.5. Que faire en cas d'incident ?

1. **Arrêter** : ne plus utiliser l'outil pour cette donnée ; supprimer la conversation si possible.
2. **Signaler** immédiatement au référent IA et à la sécurité informatique — sans attendre, sans dissimuler.
3. **Documenter** : quoi, quand, quel outil, quel compte, quelles données.
4. **Évaluer** avec le juridique : obligations de notification (personnes, partenaires, autorités, marchés).
5. **Corriger** : mesures techniques et formation ; retour d'expérience sans recherche de bouc émissaire.

### D. Démonstration guidée — Classer avant d'agir

Kevin Mutombo forme les utilisateurs du pilote avec un exercice : 10 documents réels (rendus fictifs pour la formation) à classer, puis à associer à un mode de traitement. Exemple :

| Document | Niveau | Traitement possible avec Claude |
|---|---|---|
| Rapport ITIE publié | 1 | Libre |
| Procédure de réception des réactifs | 2 | Espace MCC |
| Registre des incidents nominatif | 3 | Après pseudonymisation, espace MCC, accord HSE |
| Projet d'estimation des réserves non publié | 4 (avant publication) | Interdit |
| Contrat d'acide | 3 | Espace MCC, accord du juridique, extrait pertinent |
| Dossier médical d'un accidenté | 4 | Interdit |

### E. Prompts commentés

**Prompt 37.1 — Aide à la pseudonymisation (sur un échantillon fictif ou déjà autorisé)**

```text
Voici un modèle de texte de déclaration d'incident (exemple fictif) : <texte> … </texte>.
Identifie tous les éléments permettant d'identifier directement ou indirectement une personne
(noms, fonctions uniques, lieux précis, dates combinées) et propose une version pseudonymisée
(Témoin A, Conducteur B…). Liste les éléments indirects qui resteraient identifiants dans un petit site.
```

*Commentaire.* Utilisez ce prompt pour **apprendre** à repérer les identifiants, sur des exemples fictifs, ou dans un cadre autorisé. Pour les données réelles de niveau élevé, la pseudonymisation doit être faite **avant** tout envoi, avec des outils internes.

**Prompt 37.2 — Vérifier son propre envoi**

```text
Avant que je ne te transmette des données, voici la description de ce que je compte envoyer
(sans les données elles-mêmes) : [description]. Quelles catégories d'informations sensibles
pourraient s'y trouver, et quelles minimisations proposerais-tu ?
```

### F. Exercices pratiques

**Exercice 37.1 (guidé).** Classez 10 documents de votre service selon les quatre niveaux et indiquez le traitement autorisé.

**Exercice 37.2 (guidé).** Pseudonymisez la déclaration d'incident d'exercice (INC-2026-0412) à la main, puis comparez avec le prompt 37.1.

**Exercice 37.3 (autonome).** Vérifiez les réglages de votre compte (mémoire, confidentialité, projets partagés, connecteurs) et notez les écarts avec la charte.

### G. Livrable professionnel

**Fiche réflexe « Données et Claude »** de votre service : catégories de données, niveaux, traitements autorisés, minimisation, contacts en cas d'incident.

### H. Vérification des résultats

::: controle
- J'ai classé l'information avant de l'utiliser.
- J'utilise l'espace d'entreprise pour toute donnée de niveau 2 ou 3, avec les accords requis.
- Je n'utilise jamais Claude pour les données de niveau 4.
- J'ai minimisé, pseudonymisé ou agrégé ce qui pouvait l'être.
- Mes réglages (mémoire, partage, connecteurs) sont conformes à la charte.
:::

::: setrompe
Un utilisateur demande à Claude « Est-ce que je peux te confier ce contrat confidentiel ? ». Claude répond de manière générale sur ses conditions de traitement. La réponse peut être exacte, mais elle ne dit rien de **vos** obligations contractuelles et de la charte de votre entreprise. La décision ne se demande pas à l'outil : elle se trouve dans la politique de l'entreprise.
:::

### I. Limites et précautions

- Les conditions des fournisseurs évoluent : la direction juridique doit les suivre.
- La ré-identification est un risque réel dans les petites communautés.
- La sécurité des comptes (authentification forte, appareils) fait partie de la protection des données.

### J. Boîte à outils

- Classification en 4 niveaux (Annexe G) ; charte (Annexe F).
- Réflexe « 3 questions » : Quel niveau ? Quel espace ? Quelle minimisation ?
- Procédure d'incident en 5 étapes (section C.5).

### K. Quiz

1. **(QCM)** Un projet d'estimation des réserves non publié est de niveau : a) 1 ; b) 2 ; c) 3 ; d) 4.
2. **(Vrai ou faux)** Si le fournisseur n'entraîne pas ses modèles sur les données, l'entreprise peut lui confier toute information.
3. **(Compréhension)** Quelle différence entre pseudonymiser et anonymiser ?
4. **(Mise en situation)** Vous avez collé par erreur un document de niveau 4 dans Claude. Que faites-vous ?
5. **(Vrai ou faux)** Un document déposé dans un projet partagé est visible par tous les membres du projet.
6. **(Compréhension)** Pourquoi la ré-identification est-elle un risque particulier dans les communautés riveraines ?
7. **(Application)** Proposez une minimisation pour l'analyse des délais de traitement des plaintes.
8. **(QCM)** Qui décide des règles d'usage des données dans l'entreprise ? a) l'outil d'IA ; b) l'entreprise via sa charte et sa politique ; c) chaque utilisateur ; d) le fournisseur d'accès Internet.
9. **(Analyse critique)** Pourquoi faut-il signaler un incident sans attendre, même sans preuve de fuite ?
10. **(Compréhension)** Citez trois catégories de données sensibles spécifiques à une entreprise minière.

<div class="carnet" titre="Chapitre 37 — Confidentialité et protection des données minières"></div>
