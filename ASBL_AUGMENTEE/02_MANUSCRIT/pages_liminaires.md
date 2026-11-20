::: {.fauxtitre}
ASBL AUGMENTÉE
:::

::: saut
:::

::: {.pagetitre}
**Verdi Imbole**

[ASBL AUGMENTÉE]{.titrelivre}

**Comment implémenter l'IA dans vos processus**

Édition 2026
:::

::: saut
:::

## L'auteur {.unnumbered}

**Verdi Imbole** est auteur indépendant, auditeur financier et consultant freelance en intelligence artificielle.

Contact : verdiimbole0@gmail.com

::: saut
:::

## Droits d'auteur {.unnumbered}

© 2026 Verdi Imbole. Tous droits réservés.

Aucune partie de cet ouvrage ne peut être reproduite, distribuée, adaptée, diffusée ou exploitée, sous quelque forme que ce soit, sans l'autorisation écrite préalable de l'auteur, sauf exceptions expressément prévues par la législation applicable.

Toute reproduction, commercialisation, distribution ou communication publique non autorisée de tout ou partie de cet ouvrage est susceptible d'engager la responsabilité de son auteur au regard des dispositions légales applicables.

Pour toute demande d'autorisation : verdiimbole0@gmail.com.

*Précisions.* Cette mention ne supprime pas les exceptions au droit d'auteur reconnues par la loi applicable (par exemple, selon les pays, la courte citation, l'usage privé ou certains usages pédagogiques). Les règles de protection, de dépôt et de preuve de la paternité d'une œuvre varient d'une juridiction à l'autre ; il appartient à chacun de vérifier celles qui s'appliquent à sa situation.

*Modèles et annexes.* Les acheteurs de l'ouvrage peuvent reproduire et adapter les modèles des annexes pour l'usage interne de leur propre organisation. Toute autre diffusion, notamment commerciale ou dans le cadre de formations payantes, requiert l'autorisation écrite de l'auteur.

*Organisations et personnes citées.* Les organisations (Lumière des Collines, Fondation Horizons Partagés, Réseau Citoyen pour l'Eau, Maison des Aînés Solidaires), les personnes, les montants et les données utilisés dans les exemples sont **fictifs**. Toute ressemblance avec des organisations ou des personnes existantes serait fortuite. Les montants sont exprimés en « UM » (unité monétaire fictive).

*Marques.* Les noms de logiciels ou de services éventuellement mentionnés appartiennent à leurs propriétaires respectifs. Leur mention n'implique ni partenariat ni recommandation commerciale.

*Polices.* L'ouvrage est composé en Source Serif 4 et Source Sans 3 (licence SIL Open Font License 1.1).

Édition 2026.

::: saut
:::

## Note sur l'utilisation de l'intelligence artificielle dans la production de cet ouvrage {.unnumbered}

Cet ouvrage a été conçu et dirigé par son auteur humain, Verdi Imbole, qui en a défini la vocation, le public, l'architecture en six parties et vingt-deux modules, les exigences pédagogiques, documentaires et éthiques, ainsi que la direction artistique.

Conformément à la pratique de transparence que ce livre recommande à ses lecteurs, l'auteur précise que l'intelligence artificielle a été utilisée de manière importante comme outil d'assistance : recherche et pré-vérification de références, rédaction de versions de travail des chapitres à partir du cahier des charges de l'auteur, production des schémas originaux, construction des modèles d'annexes et mise en forme des fichiers.

Les contenus ainsi produits ont vocation à être examinés, corrigés et validés par l'auteur, qui assume la responsabilité éditoriale du manuscrit final. Un rapport de contrôle qualité joint au manuscrit recense les points qui demandent encore une vérification humaine avant publication.

L'utilisation de ces outils ne dispense pas le lecteur de vérifier les informations et de se référer aux sources officielles lorsqu'une décision professionnelle, juridique, comptable ou financière est envisagée.

## Avertissement professionnel {.unnumbered}

Cet ouvrage est un outil d'information, de formation et d'accompagnement. Il ne remplace pas :

- un conseil juridique adapté à une juridiction déterminée ;
- une expertise comptable réglementée ;
- une mission d'audit ;
- un avis fiscal ;
- une expertise en cybersécurité ;
- une étude de conformité relative à la protection des données.

Les obligations légales, comptables, fiscales et de protection des données varient selon les pays, la forme juridique de l'organisation, ses bailleurs et ses activités. Les lecteurs doivent consulter les professionnels compétents lorsque leur situation l'exige.

Les outils numériques évoluent très rapidement. Les catégories d'outils décrites ici sont stables ; les fonctionnalités, conditions d'utilisation et tarifs des produits commerciaux, eux, changent souvent. Vérifiez-les toujours auprès du fournisseur à la date de votre projet.

Les réponses d'IA reproduites dans cet ouvrage sont des **exemples de résultats attendus**, rédigés à des fins pédagogiques. Elles ne sont pas présentées comme des sorties effectivement obtenues avec un outil donné : un même prompt peut produire des réponses différentes selon l'outil, sa version et le moment.

::: saut
:::

## Avant-propos {.unnumbered}

Il est 18 h 40 dans les bureaux d'une association. La trésorière cherche une facture que le bailleur réclame pour le lendemain. Le coordinateur recopie, pour la troisième fois du mois, les mêmes chiffres dans trois modèles de rapport différents. La chargée de communication a des photos superbes d'une activité, mais ne sait plus si les familles ont donné leur accord. Le président a lu dans la presse que « l'IA va tout changer » et se demande si son organisation est déjà en retard.

Si cette scène vous semble familière, ce livre est pour vous.

Les organisations à but non lucratif portent des missions considérables avec des moyens limités. Elles doivent rendre des comptes à des bailleurs exigeants, protéger des personnes souvent vulnérables, motiver des équipes et des bénévoles, et tout cela avec des processus administratifs qui consomment une part croissante de leur énergie. L'intelligence artificielle ne résoudra pas ces tensions par magie. Mais, bien utilisée, elle peut rendre du temps aux équipes, réduire certaines erreurs, améliorer la qualité des documents et aider à mieux décider.

« Bien utilisée » : tout est là. J'ai vu des organisations perdre des mois à chercher l'outil miracle, d'autres confier sans précaution des données sensibles à des services en ligne gratuits, d'autres encore rejeter toute innovation par méfiance. Ces trois attitudes ont un point commun : elles partent de l'outil plutôt que du problème.

Ce manuel propose une autre démarche. Comprendre d'abord ce qu'est réellement l'IA, sans jargon et sans fascination. Comprendre ensuite son organisation : ses processus, ses blocages, ses risques. Identifier enfin, avec méthode, les situations où l'IA apporte une valeur réelle, et la mettre en œuvre avec des contrôles adaptés, à la mesure des moyens de chacun.

Mon métier d'auditeur m'a appris qu'une procédure ne vaut que par les contrôles qui l'accompagnent. C'est pourquoi chaque solution présentée ici précise qui fait quoi, ce qui doit être vérifié, et quelles décisions doivent impérativement rester humaines.

Vous n'avez pas besoin d'être informaticien pour lire ce livre. Vous avez seulement besoin d'un problème concret à résoudre et de l'envie de vous y attaquer avec méthode.

*Verdi Imbole*

## Présentation de l'ouvrage {.unnumbered}

### Ce que ce livre est : et ce qu'il n'est pas

*ASBL augmentée* est un manuel de formation et d'action. Il n'est ni un catalogue d'outils, ni un recueil de prompts à copier sans comprendre, ni un traité théorique sur l'intelligence artificielle.

Il suit un fil simple, que vous retrouverez dans chaque module : **problème → méthode → application → contrôle.**

### Un mot sur « ASBL »

Le sigle ASBL (association sans but lucratif) est employé ici **au sens pédagogique large**. Selon les pays et les traditions juridiques, on parle d'association, d'organisation non gouvernementale (ONG), de fondation, d'organisation sans but lucratif (OSBL), de *nonprofit*, de *charity*, d'organisation de la société civile ou encore d'organisation d'économie sociale. Ces statuts n'emportent pas les mêmes obligations : règles de gouvernance, normes comptables, fiscalité, déclarations aux autorités. Ce livre distingue systématiquement :

- les **principes universels** de bonne gestion, transposables partout ;
- les **obligations nationales**, qui doivent toujours être vérifiées localement.

Les encadrés « ⚖️ Adaptation réglementaire » signalent les points où la loi de votre pays peut changer la réponse.

### Organisation en six parties

| Partie | Question à laquelle elle répond | Modules |
|---|---|---|
| I. Comprendre l'IA | Qu'est-ce que l'IA, comment fonctionne-t-elle, comment l'utiliser ? | 1 à 3 |
| II. Comprendre son ASBL | Comment fonctionne mon organisation et où sont ses problèmes ? | 4 à 6 |
| III. Préparer et sécuriser | Quelles données, quelles règles, quels outils ? | 7 à 9 |
| IV. Implémenter par métier | Comment appliquer l'IA à chaque fonction ? | 10 à 18 |
| V. De l'idée à la mise en œuvre | Comment déployer et faire durer ? | 19 et 20 |
| VI. Laboratoire | Comment résoudre des cas complets et bâtir son plan ? | 21 et 22 |

### Les organisations du fil rouge

Quatre organisations fictives accompagnent le lecteur tout au long de l'ouvrage. Elles représentent des tailles, des moyens et des contextes différents.

| Organisation | Profil | Ce qu'elle illustre |
|---|---|---|
| **Lumière des Collines** | Soutien scolaire ; 6 salariés et 30 bénévoles ; zone semi-rurale ; connexion internet intermittente ; budget annuel d'environ 180 000 UM | Solutions de niveau Débutant, peu coûteuses, adaptées à la faible connectivité |
| **Fondation Horizons Partagés** | Santé communautaire ; 60 salariés ; 4 bureaux ; 5 bailleurs ; budget d'environ 3,2 millions d'UM | Fil rouge principal ; solutions de niveau Intermédiaire |
| **Réseau Citoyen pour l'Eau (RCE)** | Eau et assainissement ; 300 salariés ; 3 pays ; progiciel de gestion intégré (ERP) | Solutions de niveau Avancé ; achats, audit, assistants documentaires |
| **Maison des Aînés Solidaires** | Services aux personnes âgées ; 12 salariés et 80 bénévoles ; grande ville d'un pays à revenu élevé | Bénévolat, données sensibles, réglementation stricte |

### Les rubriques récurrentes

Chaque module suit la même structure, afin que vous sachiez toujours où trouver l'information : mise en situation, problématique, objectifs, notions, explications, illustrations, application professionnelle, mise en œuvre, solutions par niveau, outils, prompts, résultats attendus, contrôles humains, risques, exercice pratique, synthèse, QCM et corrigé.

Quatre encadrés ponctuent le texte, avec parcimonie :

- **🔎 À retenir** : l'idée essentielle à mémoriser ;
- **⚖️ Adaptation réglementaire** : ce qui dépend de la loi de votre pays ;
- **🛑 Contrôle humain obligatoire** : une décision qui ne doit jamais être déléguée à une machine ;
- **📶 Faible connectivité** : comment faire quand internet est lent ou intermittent.

### Les fiches prompts

Un prompt est la consigne que l'on adresse à un outil d'IA. Les prompts de ce livre sont présentés sous forme de **fiches complètes** (rubriques A à K) : objectif, contexte, données nécessaires, texte du prompt, mode d'emploi, résultat attendu, exemple, méthode de vérification, précautions et amélioration. Dans les prompts, les éléments à remplacer par vos propres informations sont écrits entre crochets et en majuscules : `[NOM DE L'ASBL]`.

## Guide de lecture {.unnumbered}

Vous pouvez lire ce livre de deux façons.

**Pour transformer l'ensemble de votre organisation**, lisez les vingt-deux modules dans l'ordre : chacun s'appuie sur les précédents.

**Pour progresser dans votre métier**, suivez le socle commun, puis votre parcours spécialisé.

**Socle commun, à lire par tous :**

- modules 1, 2 et 3 : les fondamentaux de l'IA ;
- modules 4, 5 et 6 : comprendre et diagnostiquer son organisation ;
- module 8 : éthique, sécurité et réglementation ;
- modules 19 et 20 : déployer et pérenniser.

Les modules 7 (données) et 9 (choix des outils) sont vivement recommandés à toute personne qui pilotera un projet.

**Parcours spécialisés :**

| Vous êtes… | Lisez en priorité | Puis |
|---|---|---|
| Fondateur, président, administrateur, directeur | Module 10 | Modules 5, 6, 20, 22 |
| Comptable, trésorier, responsable financier | Module 12 | Module 13 |
| Auditeur, contrôleur interne | Module 13 | Modules 12 et 16 |
| Chef de projet, responsable suivi-évaluation | Module 11 | Modules 15 et 18 |
| Responsable des ressources humaines ou du bénévolat | Module 14 | Module 8 (approfondi) |
| Chargé de recherche de financements | Module 15 | Modules 11 et 17 |
| Responsable logistique ou achats | Module 16 | Module 13 |
| Chargé de communication | Module 17 | Module 15 |
| Agent de terrain | Module 18 | Modules 8 et 11 |

Terminez toujours par le **laboratoire** : le module 21 (dix études de cas) et le module 22 (votre plan de transformation à 90 jours).

![Figure 0.1 : Carte des parcours de lecture](03_ILLUSTRATIONS/figures/fig_0_1.svg)

## Public cible {.unnumbered}

Ce livre s'adresse à toute personne qui contribue à la vie d'une organisation à but non lucratif :

- **gouvernance** : fondateurs, présidents, membres des conseils d'administration ;
- **direction** : directeurs exécutifs, coordonnateurs, secrétaires généraux ;
- **fonctions de support** : responsables administratifs, comptables, trésoriers, responsables financiers, responsables des ressources humaines, logisticiens, chargés de communication ;
- **contrôle** : auditeurs et contrôleurs internes ;
- **programmes** : responsables de programmes et de projets, responsables du suivi-évaluation, agents de terrain ;
- **engagement** : bénévoles ;
- **accompagnement et formation** : consultants, formateurs, étudiants.

Il a été écrit pour trois profils de lecteurs à la fois : **ceux qui découvrent l'IA**, qui y trouveront des explications sans jargon ; **ceux qui l'utilisent déjà**, qui y trouveront des méthodes plus rigoureuses ; **ceux qui restent sceptiques**, dont les doutes sont pris au sérieux et qui y trouveront des critères pour décider en connaissance de cause.

## Objectifs d'apprentissage de l'ouvrage {.unnumbered}

À l'issue de la lecture et des exercices, vous serez capable de :

1. **expliquer** avec des mots simples ce qu'est l'IA, comment elle fonctionne et quelles sont ses limites ;
2. **utiliser** un assistant d'IA de façon efficace et sûre, en rédigeant des consignes claires et en vérifiant les réponses ;
3. **diagnostiquer** les dysfonctionnements de votre organisation et cartographier ses processus ;
4. **sélectionner** les cas d'usage pertinents à l'aide d'une matrice de priorisation ;
5. **préparer** vos données et **appliquer** des règles de protection et d'éthique adaptées ;
6. **choisir** des outils proportionnés à vos moyens, du niveau débutant au niveau avancé ;
7. **mettre en œuvre** des solutions concrètes dans votre métier, avec les contrôles humains appropriés ;
8. **conduire** un projet IA de bout en bout et **accompagner** le changement ;
9. **construire** le plan de transformation numérique et intelligente de votre organisation.

## Liste des abréviations {.unnumbered}

| Abréviation | Signification |
|---|---|
| AG | Assemblée générale |
| AI Act | Règlement (UE) 2024/1689 sur l'intelligence artificielle |
| AIE (IEA) | Agence internationale de l'énergie |
| API | Interface de programmation d'application (*Application Programming Interface*) |
| ASBL | Association sans but lucratif (sens large, voir présentation) |
| CA | Conseil d'administration |
| CAD | Comité d'aide au développement de l'OCDE |
| CHS | *Core Humanitarian Standard* (Norme humanitaire fondamentale) |
| CSV | Fichier de valeurs séparées par des virgules ou points-virgules |
| ERP | Progiciel de gestion intégré (*Enterprise Resource Planning*) |
| IA | Intelligence artificielle |
| IIA | *The Institute of Internal Auditors* |
| INPAS | *International Non-Profit Accounting Standard* |
| ISO/IEC | Organisation internationale de normalisation / Commission électrotechnique internationale |
| KPI | Indicateur clé de performance |
| LLM | Grand modèle de langage (*Large Language Model*) |
| NIST | *National Institute of Standards and Technology* (États-Unis) |
| OCDE (OECD) | Organisation de coopération et de développement économiques |
| OCR | Reconnaissance optique de caractères |
| ONG | Organisation non gouvernementale |
| OSBL | Organisation sans but lucratif |
| PV | Procès-verbal |
| RAG | Génération augmentée par la recherche (*Retrieval-Augmented Generation*) |
| RGPD | Règlement général sur la protection des données (UE) 2016/679 |
| RH | Ressources humaines |
| RPA | Automatisation robotisée des processus (*Robotic Process Automation*) |
| S&E | Suivi et évaluation |
| SaaS | Logiciel fourni en ligne sous forme de service (*Software as a Service*) |
| UM | Unité monétaire fictive utilisée dans les exemples |
| UNESCO | Organisation des Nations unies pour l'éducation, la science et la culture |
| WCAG | *Web Content Accessibility Guidelines* (règles d'accessibilité des contenus web) |

## Glossaire {.unnumbered}

**Agent IA** : système qui ne se contente pas de répondre : il planifie et enchaîne des actions (rechercher, remplir un formulaire, envoyer un message) pour atteindre un objectif, en utilisant des outils auxquels on lui a donné accès. Plus un agent a de droits, plus les contrôles doivent être stricts.

**Algorithme** : suite d'instructions permettant de résoudre un problème ou d'accomplir une tâche. Une recette de cuisine est un algorithme.

**Anonymisation** : traitement qui rend impossible, de façon irréversible et par des moyens raisonnables, la réidentification d'une personne. À distinguer de la pseudonymisation.

**API** : « Prise » logicielle qui permet à deux programmes d'échanger des données automatiquement (par exemple, un formulaire en ligne qui envoie ses réponses à un tableur).

**Apprentissage automatique (*machine learning*)** : Famille de méthodes où un système apprend à partir d'exemples plutôt qu'à partir de règles écrites à la main.

**Apprentissage profond (*deep learning*)** : Forme d'apprentissage automatique utilisant des réseaux de neurones artificiels à nombreuses couches ; à la base de la reconnaissance d'images, de la voix et des modèles de langage modernes.

**Assistant conversationnel** : application avec laquelle on échange par écrit ou oralement, en langage naturel, et qui s'appuie généralement sur un grand modèle de langage.

**Base de connaissances** : ensemble organisé de documents de référence (procédures, politiques, FAQ) qu'un système peut consulter.

**Biais** : écart systématique qui conduit un système à produire des résultats injustes ou inexacts pour certains groupes ou situations, souvent parce que les données d'apprentissage sont déséquilibrées.

**Cadre logique** : matrice de planification de projet reliant objectifs, résultats, activités, indicateurs, sources de vérification et hypothèses.

**Cloud (informatique en nuage)** : utilisation de logiciels, de stockage ou de puissance de calcul fournis à distance par un prestataire, via internet.

**Contexte (fenêtre de)** : quantité de texte qu'un modèle de langage peut prendre en compte en une fois (consigne, documents fournis et conversation).

**Contrôle interne** : ensemble des dispositifs (règles, séparation des tâches, autorisations, vérifications) qui donnent une assurance raisonnable que l'organisation atteint ses objectifs, protège ses ressources et produit une information fiable.

**Donnée personnelle** : toute information se rapportant à une personne identifiée ou identifiable, directement ou indirectement.

**Données structurées / non structurées** : les premières sont organisées en lignes et colonnes (tableur, base de données) ; les secondes ne le sont pas (courriels, PDF, photos, enregistrements).

**Explicabilité** : capacité à rendre compréhensibles, pour les personnes concernées, les raisons d'un résultat produit par un système.

**Hallucination** : contenu produit par une IA générative qui paraît plausible mais qui est faux, inventé ou non fidèle aux sources fournies.

**IA générative** : IA qui produit de nouveaux contenus (texte, image, son, code) à partir d'une consigne.

**IA prédictive** : IA qui estime une valeur ou une probabilité future (par exemple un risque d'abandon) à partir de données passées.

**Imputation** : en comptabilité, affectation d'une opération à un compte, et en comptabilité analytique ou budgétaire, à un projet, une ligne budgétaire ou un bailleur.

**Inférence** : utilisation d'un modèle déjà entraîné pour produire une réponse à partir d'une nouvelle donnée.

**Injection de prompt** : attaque consistant à insérer, dans un texte lu par l'IA (courriel, page web, document), des instructions cachées destinées à détourner son comportement.

**Low-code / no-code** : outils permettant de construire des applications ou des automatisations avec peu ou pas de programmation, par assemblage de blocs.

**Métadonnées** : données décrivant d'autres données : date, auteur, type de document, projet, niveau de confidentialité.

**Modèle** : résultat de l'apprentissage : un ensemble de paramètres qui permet de produire des prédictions ou des contenus.

**Modèle de langage (grand, LLM)** : modèle entraîné sur de très grandes quantités de textes pour prédire la suite la plus probable d'un texte ; à la base des assistants conversationnels.

**OCR** : reconnaissance optique de caractères : transformation d'une image de texte (scan, photo) en texte exploitable.

**Piste d'audit** : ensemble des traces permettant de reconstituer une opération de son origine à son enregistrement final (qui, quoi, quand, sur quelle pièce).

**Prompt** : consigne rédigée en langage naturel et adressée à un outil d'IA.

**Pseudonymisation** : remplacement des identifiants directs (nom, numéro) par un code ; la réidentification reste possible avec une table de correspondance, qui doit être protégée. Les données pseudonymisées restent des données personnelles.

**RAG** : technique qui consiste à rechercher, dans une base documentaire, les passages pertinents pour une question, puis à les fournir au modèle de langage afin qu'il réponde à partir de ces documents.

**Rapprochement bancaire** : comparaison entre les écritures de la comptabilité et le relevé bancaire, afin d'expliquer et de corriger les écarts.

**RPA** : logiciel qui reproduit les clics et saisies d'un utilisateur sur des applications, selon des règles fixes.

**Séparation des tâches** : principe de contrôle interne selon lequel une même personne ne doit pas cumuler des fonctions incompatibles (par exemple, commander, réceptionner et payer).

**Supervision humaine** : capacité, organisée et documentée, pour des personnes compétentes de contrôler, corriger, interrompre ou refuser le résultat d'un système d'IA.

**Système de management de l'IA** : ensemble de politiques, de rôles, de processus et de contrôles qu'une organisation met en place pour gouverner ses usages de l'IA (voir ISO/IEC 42001:2023).

**Token (jeton)** : unité de texte (souvent un fragment de mot) traitée par un modèle de langage ; les limites et la facturation des outils sont fréquemment exprimées en jetons.

**Traitement du langage naturel** : domaine de l'IA consacré à la compréhension et à la production du langage humain.

**Workflow** : enchaînement d'étapes d'un processus, avec ses acteurs, ses règles de passage et ses validations.

::: tdm
:::
