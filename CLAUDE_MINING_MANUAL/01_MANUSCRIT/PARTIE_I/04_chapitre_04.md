## Chapitre 4. Découvrir Claude et l'écosystème Anthropic

### A. Mise en situation professionnelle

Le comité de pilotage IA de MCC doit choisir comment donner accès à Claude aux 40 utilisateurs du projet pilote. Les questions fusent : « Faut-il un abonnement individuel ou un abonnement d'entreprise ? », « Quelle différence entre l'application et l'API ? », « Le service informatique parle de Claude Code et de Cowork : est-ce pour nous ? », « Où vont nos données ? ». Kevin Mutombo doit présenter une vue d'ensemble claire de l'écosystème, sans se perdre dans les noms de produits.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Présenter** Anthropic et les principes qui guident le développement de Claude.
2. **Décrire** les différentes façons d'accéder à Claude (applications, Cowork, Claude Code, API, plateformes cloud).
3. **Distinguer** les familles de modèles Claude et leur positionnement.
4. **Comparer** les offres grand public et entreprise sur les critères qui comptent pour une entreprise minière.
5. **Identifier** les documents de référence (politique d'utilisation, confidentialité) à consulter avant un déploiement.

### C. Comprendre avant de pratiquer

#### C.1. Anthropic et Claude

**Claude** est une famille de grands modèles de langage développée par **Anthropic**, une entreprise spécialisée dans la recherche et le développement de systèmes d'IA. Anthropic publie un « centre de transparence » qui présente ses rapports de modèles et ses processus de développement responsable [@ANT-TRANSP], une **politique d'utilisation** qui encadre les usages autorisés et impose des exigences supplémentaires pour les cas d'usage à haut risque [@ANT-AUP], ainsi que la **constitution de Claude**, qui décrit les valeurs et le comportement visés pour le modèle [@ANT-CONSTIT].

Pour un professionnel, ces documents ne sont pas de simples textes de principe : la politique d'utilisation fait partie des règles à respecter, et votre charte d'entreprise devra s'y articuler (chapitre 40).

#### C.2. Les modèles Claude (état au 16 novembre 2026)

Anthropic propose plusieurs modèles, de tailles et de coûts différents. Le tableau 4.1 résume la gamme actuelle d'après la documentation officielle [@ANT-MODELS].

*Tableau 4.1. Gamme des modèles Claude actuels (source : Anthropic, Models overview, consulté le 16/11/2026).*

| Modèle | Positionnement selon la documentation | Latence comparative | Prix API (entrée / sortie, USD par million de tokens) |
|---|---|---|---|
| Claude Fable 5.2 | Raisonnement exigeant et travaux agentiques de longue durée | Modérée | 8 / 40 |
| Claude Opus 5.5 | Travaux agentiques longs, programmation et travail intellectuel ; point de départ recommandé pour la plupart des usages | Modérée | 4 / 20 |
| Claude Sonnet 5.5 | Meilleure combinaison de vitesse et d'intelligence | Rapide | 2 / 10 |
| Claude Haiku 5.5 | Tâches à fort volume et sensibles à la latence (classification, extraction, routage) | La plus rapide | à partir de 0,10 / 0,50 |

Tous ces modèles acceptent du texte et des images en entrée, produisent du texte, sont multilingues, peuvent utiliser des outils, disposent d'une fenêtre de contexte d'un million de tokens et d'une sortie maximale de 128 000 tokens via l'API [@ANT-MODELS]. La même documentation recommande, en cas de doute, de **commencer par Claude Opus 5.5** et de passer à Claude Fable 5.2 pour les raisonnements les plus exigeants.

![Figure 4.1. Positionnement des modèles Claude actuels selon le prix API et la latence comparative indiqués dans la documentation. Données : Anthropic, Models overview (consulté le 16/11/2026). Graphique réalisé pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig04_2_gamme_modeles.png){width=88%}

Les notes de version du centre d'aide retracent les lancements récents : Claude Opus 5.5 le 22 septembre 2026, Claude Sonnet 5.5 le 28 septembre 2026 et Claude Haiku 5.5 le 7 octobre 2026 [@ANT-HC-RELEASE; @ANT-OPUS55]. Des modèles plus anciens restent disponibles pendant un temps, avec des dates de retrait annoncées [@ANT-MODELS].

::: attention
Les noms, prix et caractéristiques des modèles changent plusieurs fois par an. Ce chapitre présente une photographie au 16 novembre 2026. **Avant toute décision, consultez la page officielle « Models overview ».** Les principes de choix (chapitre 8) resteront valables.
:::

#### C.3. Les façons d'accéder à Claude

![Figure 4.2. L'écosystème Claude. Les mêmes modèles sont accessibles par plusieurs « portes d'entrée », du simple utilisateur au développeur. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig04_1_ecosysteme.png){width=100%}

| Porte d'entrée | Pour qui ? | Usage typique à MCC |
|---|---|---|
| **Applications Claude** (Web, bureau, mobile) | Tous les utilisateurs | Conversations, analyse de documents, rédaction, projets, artefacts, recherche |
| **Claude Cowork** | Utilisateurs avancés | Tâches longues en plusieurs étapes sur des fichiers, tâches planifiées |
| **Claude Code** | Équipes techniques, analystes de données | Scripts d'analyse, automatisation, développement d'outils internes |
| **Claude Platform (API)** | Développeurs | Intégrer Claude dans une application interne (portail HSE, outil d'achats) |
| **Plateformes cloud** (Amazon Bedrock, Google Cloud, Microsoft Foundry) | Directions informatiques | Accès aux modèles dans l'infrastructure cloud déjà retenue par l'entreprise |
| **Extensions** (Claude in Chrome, Microsoft 365, connecteurs, Skills) | Selon l'offre | Travailler depuis le navigateur, la suite bureautique, relier Claude aux outils de l'entreprise |

Sources : documentation des modèles et identifiants par plateforme [@ANT-MODELS] ; page des offres [@ANT-PLANS] ; centre d'aide (Cowork, connecteurs) [@ANT-HC-COWORK; @ANT-HC-CONNECT].

Depuis septembre 2026, Anthropic a progressivement réuni dans une même expérience les fonctions de conversation et celles de Cowork : on peut poser une question rapide ou confier une tâche plus longue (rapport, tableur, présentation) depuis n'importe quelle conversation, et les conversations, tâches Cowork, projets, connecteurs et compétences sont partagés [@ANT-HC-RELEASE]. De même, la création de designs, présentations et documents (Claude Design, Claude Slides, Claude Docs) est disponible dans les conversations, sous forme d'artefacts [@ANT-HC-ARTIFACTS].

#### C.4. Les offres

La page officielle des offres distingue des offres **individuelles** (Free, Pro, Max, Ultra) et des offres **Team et Enterprise** destinées aux organisations [@ANT-PLANS]. Au 16 novembre 2026, elle indiquait notamment :

*Tableau 4.2. Offres individuelles (extrait de claude.com/pricing, consulté le 16/11/2026 ; prix hors taxes, susceptibles d'évoluer).*

| Offre | Prix indiqué | Éléments distinctifs |
|---|---|---|
| Free | 0 USD | Conversation sur Web, bureau et mobile ; recherche Web ; création de fichiers ; mémoire ; connecteurs ; artefacts ; jusqu'à 5 projets |
| Pro | 17 USD/mois en paiement annuel, 20 USD en paiement mensuel | Davantage d'utilisation ; projets ; recherche approfondie ; Claude Code ; plus de modèles |
| Max | 100 USD/mois | Environ 5 fois l'utilisation de Pro ; accès prioritaire ; crédits API mensuels |
| Ultra | 200 USD/mois | Pas de limite par période de 5 heures (comptes vérifiés) ; environ 10 fois l'utilisation hebdomadaire de Pro |

Pour une entreprise, les offres **Team** et **Enterprise** apportent des fonctions décisives : partage de projets entre collègues, administration centralisée, authentification unique (SSO), contrôles d'administration sur les connecteurs, et possibilités de contractualisation adaptées [@ANT-PLANS; @ANT-HC-PROJECTS]. Les notes de version mentionnent en novembre 2026 de nouveaux contrôles de sécurité et d'administration pour l'offre Enterprise [@ANT-HC-RELEASE].

::: application
À MCC, le comité de pilotage choisit l'offre **Team** pour le pilote (40 utilisateurs), afin de bénéficier du partage de projets et d'une administration centralisée, avec un **accès API** séparé pour l'équipe données. Il exclut l'usage de comptes personnels gratuits pour les données de l'entreprise. Le passage à l'offre Enterprise sera étudié après six mois, en fonction des besoins de sécurité (journalisation, contrôles d'accès).
:::

#### C.5. Données et confidentialité : où vont vos informations ?

C'est la question que pose toujours un directeur juridique. Les règles diffèrent selon le type d'offre :

- Pour les offres grand public (Free, Pro, Max, Ultra), la page des offres indique que l'utilisation des conversations pour l'entraînement des modèles fonctionne sur le principe de l'**exclusion volontaire** (« opt-out ») [@ANT-PLANS].
- Pour les offres commerciales et l'API, les conditions sont fixées par les **conditions commerciales** et le contrat : le service juridique doit les lire avant tout déploiement.
- La **politique de confidentialité** d'Anthropic décrit le traitement des données personnelles [@ANT-PRIV-POL].

::: erreur
Utiliser un compte personnel gratuit pour analyser un contrat confidentiel de l'entreprise « parce que c'est plus rapide ». Même si l'outil est performant, ce choix peut violer la politique de l'entreprise, des engagements de confidentialité et, selon les données, la réglementation. Le chapitre 37 détaille les règles.
:::

### D. Démonstration guidée : Construire la fiche d'identité de l'outil pour son entreprise

Kevin prépare pour le comité une fiche d'une page. Sa méthode :

1. **Partir des besoins** : nombre d'utilisateurs, types de documents, niveau de confidentialité, besoin de partage, besoin d'intégration avec les outils existants (messagerie, GED, ERP).
2. **Consulter les sources officielles** : page des modèles, page des offres, centre d'aide, politique d'utilisation, politique de confidentialité. Il note la date de consultation.
3. **Demander à Claude de structurer la comparaison** à partir des extraits qu'il a copiés (et non de la mémoire du modèle, qui peut être dépassée).
4. **Faire valider** la fiche par le service juridique (données), l'informatique (sécurité, SSO) et les achats (contrat).

### E. Prompts commentés

**Prompt 4.1. Comparer des offres à partir de sources fournies**

```text
Contexte : nous sommes une entreprise minière (2 350 personnes) qui prépare
un pilote d'IA générative pour 40 utilisateurs, avec des documents confidentiels.

Voici les extraits des pages officielles que j'ai copiés aujourd'hui [date] :
<offres>
[coller les extraits de la page des offres]
</offres>
<projets>
[coller l'extrait sur le partage des projets]
</projets>

Tâche : construis un tableau comparatif des offres sur ces critères :
partage entre collègues, administration centralisée, authentification unique,
contrôle des connecteurs, conditions d'utilisation des données, prix.
Règles : utilise UNIQUEMENT les extraits fournis ; pour tout critère non couvert,
écris « non précisé dans les extraits ». Termine par les questions à poser
au fournisseur avant de contractualiser.
```

*Commentaire.* Les balises `<offres>` et `<projets>` séparent clairement les sources ; la documentation d'Anthropic recommande d'ailleurs de structurer les documents fournis avec des balises de ce type [@ANT-PROMPT]. La règle « utilise uniquement les extraits fournis » évite que Claude complète avec des informations anciennes.

**Prompt 4.2. Expliquer l'écosystème à un public non technique**

```text
Explique en 250 mots à des chefs de service d'une mine la différence entre :
l'application Claude, Cowork, Claude Code et l'API. Pour chacun, donne un exemple
d'usage dans une entreprise minière et précise qui, dans l'entreprise, est concerné.
Ne cite aucun prix ni caractéristique chiffrée.
```

*Commentaire.* L'interdiction de citer des prix évite d'introduire des informations susceptibles d'être obsolètes dans un document destiné à durer.

### F. Exercices pratiques

**Exercice 4.1 (guidé) : Fiche d'identité de l'outil**

En consultant vous-même la page officielle des modèles et celle des offres, complétez le tableau suivant, en notant la date de consultation : modèles disponibles dans votre offre ; limites de taille des fichiers ; fonctions disponibles (projets, recherche, connecteurs, artefacts) ; paramètre de confidentialité applicable à votre compte.

**Exercice 4.2 (autonome) : Recommandation d'offre**

Pour un département de MCC de votre choix (par exemple le service juridique, 5 personnes, documents très confidentiels), rédigez une recommandation d'une demi-page sur le mode d'accès à Claude (offre, API, restrictions), avec les questions à soumettre au service juridique.

### G. Livrable professionnel

**Fiche d'identité « Claude dans notre entreprise »**, une page : mode d'accès retenu, modèles disponibles, fonctions activées et désactivées, règles de données, contacts (référent IA, informatique, juridique), date de mise à jour et sources consultées.

### H. Vérification des résultats

::: controle
- Toutes les informations sur les modèles, offres et prix proviennent d'une page officielle consultée récemment, avec la date de consultation.
- Les conditions relatives aux données ont été lues dans les documents contractuels, et non résumées de mémoire par Claude.
- La fiche a été validée par l'informatique et le service juridique.
:::

::: setrompe
Demandé « de mémoire », un modèle peut présenter une gamme de modèles ou des prix qui étaient exacts à sa date d'entraînement mais ne le sont plus. **Contre-mesure** : fournissez l'extrait de la page officielle du jour, ou utilisez la recherche Web avec citations, puis vérifiez la source.
:::

### I. Limites et précautions

- L'écosystème évolue très vite : prévoyez une **mise à jour trimestrielle** de votre fiche d'identité.
- Les fonctions disponibles dépendent de l'offre **et** des réglages de l'administrateur de votre organisation.
- Certaines fonctions sont en **version bêta** : utilisez-les avec prudence pour les processus critiques.

### J. Boîte à outils

**Liste des pages officielles à mettre en favoris**

- Modèles : platform.claude.com/docs/en/about-claude/models/overview
- Offres : claude.com/pricing
- Centre d'aide et notes de version : support.claude.com
- Politique d'utilisation : anthropic.com/legal/aup
- Politique de confidentialité : anthropic.com/legal/privacy
- Centre de transparence : anthropic.com/transparency

**Check-list 4.1. Avant de choisir une offre**

- [ ] Nombre d'utilisateurs et profils identifiés.
- [ ] Niveau de confidentialité des données à traiter connu.
- [ ] Besoins de partage et d'administration exprimés.
- [ ] Conditions relatives aux données lues par le service juridique.
- [ ] Exigences de sécurité (SSO, journalisation) validées par l'informatique.
- [ ] Budget et modalités de facturation validés.

### K. Quiz

1. **(QCM)** Selon la documentation consultée, quel modèle est recommandé comme point de départ en cas de doute ? a) Haiku 5.5 ; b) Sonnet 5.5 ; c) Opus 5.5 ; d) Fable 5.2.
2. **(Vrai ou faux)** Claude Code est principalement destiné aux équipes techniques et aux analystes de données.
3. **(Compréhension)** Quelle est la différence entre l'application Claude et l'API ?
4. **(QCM)** Quel modèle est positionné pour les tâches à fort volume comme la classification et l'extraction ? a) Haiku 5.5 ; b) Opus 5.5 ; c) Fable 5.2 ; d) aucun.
5. **(Vrai ou faux)** Les prix et noms de modèles indiqués dans un livre restent valables plusieurs années.
6. **(Mise en situation)** Un ingénieur veut analyser un contrat confidentiel avec son compte gratuit personnel. Que lui conseillez-vous ?
7. **(Compréhension)** Citez trois documents officiels d'Anthropic à consulter avant un déploiement en entreprise.
8. **(QCM)** Quelle fonction est particulièrement utile en entreprise et disponible sur les offres Team et Enterprise ? a) le partage de projets entre collègues ; b) la limite de 5 projets ; c) l'absence de connecteurs ; d) l'interdiction des artefacts.
9. **(Analyse critique)** Pourquoi est-il préférable de fournir à Claude l'extrait d'une page officielle plutôt que de lui demander de décrire les offres de mémoire ?
10. **(Application)** Votre entreprise utilise déjà un grand fournisseur cloud. Quelle porte d'entrée vers les modèles Claude la direction informatique pourrait-elle étudier ?

<div class="carnet" titre="Chapitre 4. Découvrir Claude et l'écosystème Anthropic"></div>
