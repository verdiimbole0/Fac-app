<!-- Manuscrit assemblé automatiquement par 07_OUTILS/build.py. Chemins d'images relatifs au dossier ASBL_AUGMENTEE. -->

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

Table: Tableau 0.1 : Présentation de l'ouvrage

### Les organisations du fil rouge

Quatre organisations fictives accompagnent le lecteur tout au long de l'ouvrage. Elles représentent des tailles, des moyens et des contextes différents.

| Organisation | Profil | Ce qu'elle illustre |
|---|---|---|
| **Lumière des Collines** | Soutien scolaire ; 6 salariés et 30 bénévoles ; zone semi-rurale ; connexion internet intermittente ; budget annuel d'environ 180 000 UM | Solutions de niveau Débutant, peu coûteuses, adaptées à la faible connectivité |
| **Fondation Horizons Partagés** | Santé communautaire ; 60 salariés ; 4 bureaux ; 5 bailleurs ; budget d'environ 3,2 millions d'UM | Fil rouge principal ; solutions de niveau Intermédiaire |
| **Réseau Citoyen pour l'Eau (RCE)** | Eau et assainissement ; 300 salariés ; 3 pays ; progiciel de gestion intégré (ERP) | Solutions de niveau Avancé ; achats, audit, assistants documentaires |
| **Maison des Aînés Solidaires** | Services aux personnes âgées ; 12 salariés et 80 bénévoles ; grande ville d'un pays à revenu élevé | Bénévolat, données sensibles, réglementation stricte |

Table: Tableau 0.2 : Présentation de l'ouvrage

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

Table: Tableau 0.3 : Guide de lecture

Terminez toujours par le **laboratoire** : le module 21 (dix études de cas) et le module 22 (votre plan de transformation à 90 jours).

![Figure 0.1 : Carte des parcours de lecture](03_ILLUSTRATIONS/figures/fig_0_1.svg){#fig-0-1}

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

Table: Tableau 0.4 : Liste des abréviations

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


# Partie I : Comprendre l'intelligence artificielle {#h1 .partie}

*Avant de transformer des processus, il faut comprendre l'outil. Cette première partie explique ce qu'est l'intelligence artificielle, comment elle fonctionne réellement et comment l'utiliser de façon efficace et sûre. Aucune connaissance technique préalable n'est nécessaire.*

# Module 1 : L'intelligence artificielle : comprendre une révolution qui nous concerne tous {#h2}

## 1.1 Mise en situation

Mariam coordonne les programmes de la Fondation Horizons Partagés. Un lundi matin, sa journée commence comme souvent : quarante-deux courriels non lus, un rapport trimestriel à envoyer à un bailleur avant vendredi, une réunion d'équipe dont personne n'a rédigé le compte rendu, et un tableau de suivi des activités que trois personnes ont modifié sans se concerter.

À la pause, un collègue lui montre sur son téléphone un assistant conversationnel : il lui a demandé de résumer un document de trente pages et a obtenu, en quelques secondes, une synthèse claire. Mariam est partagée. L'outil semble impressionnant. Mais peut-elle lui confier le rapport destiné au bailleur, qui contient des données sur les patients des centres de santé ? Le résumé est-il fidèle ? Et que se passera-t-il si l'outil invente un chiffre ?

Le même jour, lors du conseil d'administration, un administrateur affirme que « l'IA va bientôt remplacer la moitié du personnel administratif », tandis qu'une autre administratrice estime que « ce sont des gadgets dangereux qu'il vaut mieux interdire ».

Qui a raison ? Probablement personne entièrement. Ce module vous donne les repères nécessaires pour vous forger votre propre jugement.

## 1.2 Problématique

Dans beaucoup d'organisations à but non lucratif, l'IA fait l'objet de deux attitudes opposées, toutes deux coûteuses :

- **l'enthousiasme non maîtrisé** : chacun utilise des outils en ligne à sa façon, sans règle, parfois avec des données confidentielles, et recopie des réponses sans les vérifier ;
- **le rejet de principe** : l'organisation s'interdit d'explorer des usages qui pourraient libérer du temps pour la mission, et laisse ses équipes se débrouiller seules, souvent en cachette.

Entre les deux, il existe une voie : comprendre ce que l'IA sait faire, ce qu'elle ne sait pas faire, et décider en connaissance de cause. C'est l'objet de ce premier module.

## 1.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. définir l'intelligence artificielle avec vos propres mots ;
2. situer les grandes étapes de son histoire et expliquer pourquoi elle progresse si vite depuis quelques années ;
3. distinguer les grandes familles d'IA, notamment l'IA « traditionnelle » et l'IA générative ;
4. démêler les mythes et les réalités les plus répandus ;
5. identifier les principales opportunités et les principaux risques pour une ASBL ;
6. répondre de façon argumentée aux objections des personnes sceptiques.

## 1.4 Notions et définitions

### Une définition de travail

Il n'existe pas de définition unique de l'intelligence artificielle. Pour ce livre, nous retiendrons une définition pratique, proche de celle qu'utilisent les Principes de l'OCDE sur l'IA, dont la définition de « système d'IA » a été actualisée en 2023 et reprise par le règlement européen sur l'IA (OCDE, 2019/2024 ; règlement (UE) 2024/1689) :

> Un **système d'IA** est un système informatique qui, à partir des données qu'il reçoit, produit des résultats (prédictions, contenus, recommandations ou décisions) capables d'influencer un environnement physique ou numérique, avec des degrés variables d'autonomie.

Retenez trois idées de cette définition :

1. **L'IA produit des résultats à partir de données.** Sans données, pas d'IA ; avec de mauvaises données, une mauvaise IA.
2. **Ces résultats ont des effets.** Un classement de candidatures, une alerte sur une dépense, un texte envoyé à un bailleur : tous influencent des décisions réelles.
3. **L'autonomie est variable.** Un correcteur orthographique propose ; un système de tri automatique de courriels agit seul. Plus l'autonomie est grande, plus la supervision doit être organisée.

### Ce que l'IA n'est pas

L'IA n'est pas une intelligence au sens humain. Elle n'a ni intention, ni conscience, ni compréhension du monde comparable à la nôtre. Les systèmes actuels repèrent des régularités statistiques dans d'immenses quantités de données et les exploitent pour produire des résultats. Cela peut donner une impression saisissante de compréhension (surtout avec les assistants conversationnels, qui manient la langue avec aisance) mais cette aisance ne garantit ni la vérité ni le bon jugement.

## 1.5 Explications détaillées

### Une histoire faite d'accélérations et de désillusions

![Figure 1.1 : Repères historiques de l'intelligence artificielle](03_ILLUSTRATIONS/figures/fig_1_1.svg){#fig-1-1}

L'histoire de l'IA n'est pas une progression régulière. Elle alterne promesses et désillusions.

- **Les fondations (années 1950).** En 1950, le mathématicien Alan Turing pose la question de savoir si une machine peut penser et propose un test pour en juger. En 1956, une conférence organisée au Dartmouth College, aux États-Unis, popularise l'expression « intelligence artificielle ».
- **Les systèmes à règles (années 1970–1980).** On tente de reproduire l'expertise humaine sous forme de règles « si… alors… ». Ces « systèmes experts » fonctionnent dans des domaines étroits, mais deviennent ingérables quand les règles se multiplient. Les promesses non tenues entraînent des périodes de désintérêt et de baisse des financements, que l'on appelle les « hivers de l'IA ».
- **L'apprentissage à partir des données (années 1990–2010).** Plutôt que d'écrire les règles, on laisse la machine les déduire d'exemples. En 1997, un ordinateur bat le champion du monde d'échecs. À partir de 2012 environ, l'**apprentissage profond**, rendu possible par la puissance de calcul et l'abondance de données, fait progresser spectaculairement la reconnaissance d'images et de la parole.
- **L'ère des modèles de langage (depuis 2017).** En 2017, des chercheurs publient l'architecture « Transformer » (Vaswani et al., 2017), qui permet d'entraîner des modèles de langage beaucoup plus grands. Fin 2022, les assistants conversationnels deviennent accessibles au grand public et se diffusent à une vitesse inédite.
- **L'ère de l'encadrement (depuis le début des années 2020).** Les organisations internationales et les États adoptent des cadres : la Recommandation de l'UNESCO sur l'éthique de l'IA (2021), la révision des Principes de l'OCDE (2024), le cadre de gestion des risques du NIST (2023), la norme ISO/IEC 42001 (2023), le règlement européen sur l'IA (2024) et la Convention-cadre du Conseil de l'Europe sur l'IA (2024). Le module 8 y revient en détail.

Pourquoi cette histoire vous concerne-t-elle ? Parce qu'elle enseigne la prudence. Les annonces spectaculaires ont souvent été suivies de déceptions. Les outils actuels sont réellement utiles, mais pour des tâches précises, avec des limites précises.

### Les grandes familles d'IA

![Figure 1.2 : Les grandes familles d'intelligence artificielle](03_ILLUSTRATIONS/figures/fig_1_2.svg){#fig-1-2}

On peut se représenter les familles d'IA comme des ensembles emboîtés.

| Famille | Principe | Exemple dans une ASBL | Ce qu'il faut savoir |
|---|---|---|---|
| **Systèmes à règles** | Des règles écrites par des humains | « Si une dépense dépasse 500 UM, demander une seconde signature » | Prévisibles et explicables, mais rigides. Ce n'est pas toujours qualifié d'« IA » aujourd'hui, mais c'est souvent la meilleure solution. |
| **Apprentissage automatique** | Le système apprend à partir d'exemples | Estimer quels élèves risquent d'abandonner à partir des absences et des notes | Exige des données historiques fiables et suffisantes ; risque de biais. |
| **Apprentissage profond** | Réseaux de neurones à nombreuses couches | Lire une facture photographiée (OCR moderne) ; transcrire une réunion | Très performant sur les images, le son et le texte ; peu explicable. |
| **IA générative** | Produit de nouveaux contenus | Rédiger un projet de lettre, résumer un rapport, traduire un support | Fluide et polyvalente ; peut produire des erreurs plausibles (« hallucinations »). |

Table: Tableau 1.1 : Explications détaillées

### IA traditionnelle et IA générative : la différence qui compte

Dans la pratique, la distinction la plus utile pour une ASBL est celle-ci :

- l'**IA traditionnelle (ou « analytique »)** répond à une question précise et fermée : *cette dépense est-elle inhabituelle ? cette photo contient-elle un texte ? ce bénéficiaire présente-t-il un risque ?* Son résultat est une étiquette, un score, une prédiction. On peut mesurer son taux d'erreur ;
- l'**IA générative** produit un contenu ouvert : *rédige, résume, traduis, propose.* Son résultat est un texte ou une image dont la qualité est plus difficile à mesurer automatiquement, et qui exige une relecture.

Les deux se combinent souvent. Dans le traitement d'une facture (module 12), l'OCR lit le document (IA traditionnelle), un modèle propose une imputation (prédiction), un assistant génère une explication de l'anomalie détectée (IA générative), et le comptable valide (humain).

### Mythes et réalités

| Mythe | Réalité |
|---|---|
| « L'IA comprend ce qu'elle dit. » | Elle produit des suites de mots statistiquement plausibles. Elle peut écrire avec assurance une information fausse. |
| « Ce que dit l'IA est vérifié. » | Un assistant conversationnel n'est pas un moteur de recherche fiable ni une base de données. Sans sources fournies ou citées, rien n'est vérifié. |
| « L'IA va remplacer le personnel. » | Les études disponibles montrent surtout une transformation des tâches. Une expérience menée auprès de 758 consultants a montré que l'IA améliorait nettement la performance sur certaines tâches, mais la dégradait sur d'autres, d'apparence comparable, situées hors de ses capacités (Dell'Acqua et al., 2023). Le jugement humain reste déterminant pour savoir quand s'y fier. |
| « Il faut un gros budget et des informaticiens. » | De nombreux usages utiles démarrent avec un assistant conversationnel et un tableur (niveau Débutant, module 9). Les solutions intégrées, elles, demandent effectivement des moyens. |
| « Les outils gratuits sont suffisants pour tout. » | Les offres gratuites ont des limites d'usage et des conditions de traitement des données qui les rendent inadaptées aux données confidentielles (module 8). |
| « L'IA est neutre. » | Elle reflète les données sur lesquelles elle a été entraînée, y compris leurs biais. Elle peut désavantager certains groupes. |
| « Une fois installée, l'IA fonctionne seule. » | Toute solution exige un suivi, des mises à jour, une vérification régulière et une personne responsable (module 20). |

Table: Tableau 1.2 : Explications détaillées

### Opportunités pour les ASBL

Les opportunités se regroupent en cinq familles.

1. **Gagner du temps sur les tâches répétitives de rédaction et de mise en forme** : comptes rendus, courriers, synthèses, rapports intermédiaires, traductions.
2. **Mieux exploiter l'information existante** : retrouver une procédure, comparer des conventions de financement, synthétiser des retours de bénéficiaires.
3. **Fiabiliser les processus administratifs et financiers** : extraction de données de factures, détection de doublons, alertes budgétaires.
4. **Élargir l'accès** : traduire des supports dans les langues des communautés, rendre des documents plus lisibles, transcrire des échanges oraux.
5. **Mieux décider** : tableaux de bord, analyses de tendances, scénarios.

### Risques pour les ASBL

Les risques sont proportionnels aux opportunités et seront traités en profondeur au module 8.

- **Erreurs et hallucinations** : un chiffre inventé dans un rapport à un bailleur engage la crédibilité de l'organisation.
- **Fuite de données** : saisir des informations nominatives de bénéficiaires dans un outil non validé peut constituer une violation de la confidentialité et, selon les pays, de la loi.
- **Biais et discrimination** : un outil de tri de candidatures ou de ciblage de bénéficiaires peut reproduire des inégalités.
- **Dépendance** : à un fournisseur, à un outil gratuit qui change ses conditions, ou à une seule personne qui « sait faire ».
- **Perte de compétences et de sens** : déléguer à l'outil des tâches qui exigent du discernement, de l'écoute ou de l'empathie.
- **Atteinte à la réputation** : une communication manifestement générée par machine, ou une image trompeuse, peut abîmer la confiance des donateurs et des communautés.

### L'intérêt particulier de l'IA pour les ASBL

Les organisations à but non lucratif présentent trois caractéristiques qui rendent l'IA à la fois attractive et délicate.

- **Une forte charge administrative relative.** Une petite structure doit souvent produire autant de rapports qu'une grande, avec beaucoup moins de personnel. Chaque heure gagnée sur l'administratif peut être réinvestie dans la mission.
- **Des données souvent sensibles.** Santé, enfance, situations de précarité, statut migratoire : les erreurs ou les fuites peuvent avoir des conséquences graves pour des personnes vulnérables.
- **Une redevabilité multiple.** Envers les bénéficiaires, les bailleurs, les membres, les autorités et le public. Toute utilisation de l'IA doit pouvoir être expliquée et justifiée devant chacun d'eux.

### Scepticisme et résistances : les prendre au sérieux

Le scepticisme n'est pas un obstacle à vaincre : c'est souvent une forme de vigilance utile. Voici les objections les plus fréquentes et une manière d'y répondre honnêtement.

| Objection | Ce qu'elle a de juste | Réponse constructive |
|---|---|---|
| « On ne peut pas faire confiance à ce que ça écrit. » | Les hallucinations sont réelles. | Exactement : c'est pourquoi on n'utilise jamais une réponse sans vérification, et on privilégie les usages où l'on fournit soi-même les sources. |
| « Ça va supprimer des emplois. » | Certaines tâches seront transformées. | Dans une ASBL, l'objectif est de réaffecter du temps vers la mission, et cela doit être dit et organisé (module 20). |
| « Nos données sont trop sensibles. » | Elles le sont souvent. | On commence par des usages sur des données publiques ou anonymisées, et on encadre le reste (module 8). |
| « On n'a pas les moyens. » | Les solutions avancées coûtent cher. | Le niveau Débutant est accessible ; l'important est de choisir un problème précis. |
| « Ce n'est pas notre culture. » | La mission repose sur la relation humaine. | Justement : l'IA doit libérer du temps pour la relation, pas la remplacer. |

Table: Tableau 1.3 : Explications détaillées

> **🔎 À retenir** : L'IA est un outil statistique puissant, pas une intelligence humaine. Elle est utile pour des tâches précises, à condition de fournir de bonnes données, de vérifier ses résultats et de garder les décisions importantes sous contrôle humain.

## 1.6 Application professionnelle : expliquer l'IA à son conseil d'administration

### Situation

Après la réunion du conseil, la directrice d'Horizons Partagés demande à Mariam de préparer une note de deux pages pour aider les administrateurs à adopter une position commune sur l'IA. L'objectif n'est pas de choisir un outil, mais de partager une compréhension et de décider d'une démarche.

### Processus de mise en œuvre

1. **Recenser les usages existants.** Mariam envoie un questionnaire anonyme de cinq questions à l'équipe : utilisez-vous déjà un outil d'IA ? lequel ? pour quelles tâches ? avec quelles données ? qu'est-ce qui vous inquiète ?
2. **Rédiger un projet de note** avec l'aide d'un assistant conversationnel, à partir d'informations publiques et des résultats agrégés du questionnaire, sans aucune donnée nominative.
3. **Vérifier chaque affirmation** factuelle (dates, cadres de référence) auprès des sources officielles.
4. **Faire relire** la note par la directrice et par un administrateur sceptique, afin de tester sa solidité.
5. **Présenter** la note au conseil avec une proposition de décision : adopter des règles provisoires d'usage et lancer un diagnostic (modules 5 et 6).

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Questionnaire papier ou formulaire gratuit ; rédaction assistée par un assistant conversationnel ; relecture humaine | Formulaire en ligne, assistant conversationnel, traitement de texte | Nuls à faibles | Ne saisir aucune donnée interne sensible dans un outil grand public |
| Intermédiaire | Même démarche avec un assistant inclus dans la suite bureautique professionnelle de l'ASBL, dont les conditions contractuelles ont été vérifiées | Suite bureautique avec assistant intégré | Abonnement | Vérifier les paramètres de confidentialité et la localisation des données |
| Avancé | Atelier de sensibilisation pour le conseil, appuyé sur un auto-diagnostic structuré et des démonstrations sur des cas réels anonymisés | Supports de formation, environnement de démonstration | Temps de préparation, éventuellement intervenant externe | Exige une préparation solide pour rester factuel |

Table: Tableau 1.4 : Application professionnelle : expliquer l'IA à son conseil d'administration

### Outils nécessaires

Un formulaire (papier ou numérique), un assistant conversationnel, un traitement de texte, et l'accès aux sources officielles citées dans ce module.

## 1.7 Prompt prêt à l'emploi

### Fiche P1.1 : Préparer une note de sensibilisation sur l'IA pour un organe de gouvernance

**A. Titre.** Note de sensibilisation sur l'IA pour le conseil d'administration.

**B. Objectif.** Obtenir un premier projet de note claire, équilibrée et non technique, qui présente opportunités, risques et propositions de démarche, sans exagération.

**C. Contexte d'utilisation.** Direction, secrétariat général ou coordination ; avant une réunion de gouvernance où l'IA sera discutée pour la première fois.

**D. Données nécessaires.** Profil général de l'ASBL (secteur, taille, pays) ; résultats **agrégés et anonymes** d'un éventuel questionnaire interne ; questions posées par les administrateurs.

**E. Prompt complet.**

```text
Tu es un conseiller en gouvernance d'organisations à but non lucratif.
Contexte : [NOM DE L'ASBL] est une organisation de [SECTEUR] de [TAILLE :
nombre de salariés et de bénévoles], active à [PAYS/RÉGION]. Le conseil
d'administration discutera pour la première fois de l'intelligence
artificielle. Certains administrateurs sont enthousiastes, d'autres
très sceptiques.

Tâche : rédige un projet de note de 2 pages maximum (environ 800 mots)
destinée aux administrateurs.

Données : utilise uniquement les informations ci-dessous et des
connaissances générales sur l'IA. Résultats agrégés du questionnaire
interne : [COLLER LES RÉSULTATS AGRÉGÉS, SANS NOMS].
Questions des administrateurs : [LISTE DES QUESTIONS].

Format attendu :
1. Ce qu'est l'IA (5 lignes, sans jargon).
2. Ce qu'elle peut apporter à une organisation comme la nôtre
   (3 exemples concrets).
3. Les risques principaux (4 points).
4. Ce que nous proposons de décider (3 propositions).
5. Les questions qui restent ouvertes.

Exigences :
- ton factuel, ni alarmiste ni promotionnel ;
- n'invente aucune statistique, aucune étude, aucune loi ;
- si tu mentionnes un cadre de référence, indique [À VÉRIFIER] à côté ;
- signale clairement ce qui dépend de la législation de notre pays.
```

**F. Instructions d'utilisation.** Remplacez les éléments entre crochets. N'incluez jamais de noms de salariés, de bénéficiaires ou de partenaires. Si votre outil le permet, désactivez l'historique ou l'utilisation de vos conversations pour l'entraînement (paramètres de confidentialité). Copiez la réponse dans votre traitement de texte pour la retravailler.

**G. Résultat attendu.** Une note structurée en cinq rubriques, d'environ 800 mots, avec des mentions [À VÉRIFIER] sur les références.

**H. Exemple d'application (illustratif).** Pour Horizons Partagés, Mariam indique : santé communautaire, 60 salariés, 4 bureaux ; questionnaire : 23 répondants sur 60, 14 utilisent déjà un assistant conversationnel, surtout pour rédiger des courriels et traduire, 9 s'inquiètent de la confidentialité. Le projet de note obtenu (exemple de résultat attendu) propose notamment : « adopter des règles provisoires d'utilisation interdisant la saisie de données de patients dans des outils non validés ; désigner une personne référente ; lancer un diagnostic des processus administratifs en vue de deux projets pilotes ».

**I. Méthode de vérification.**

1. Vérifiez que chaque chiffre de la note figure bien dans les données que vous avez fournies.
2. Vérifiez chaque référence marquée [À VÉRIFIER] sur le site officiel de l'organisme concerné ; supprimez-la si vous ne la trouvez pas.
3. Relisez avec la question : « un administrateur sceptique trouverait-il ce texte honnête ? »
4. Contrôlez l'absence de promesse chiffrée de gains (« 50 % de temps gagné ») non étayée.

**J. Précautions.** Données de couleur verte uniquement (voir la classification du module 8). Pas d'information sur des personnes. La note reste un projet : elle est validée par la direction avant diffusion.

**K. Amélioration.**

*Version 1 (insuffisante)* : « Écris une note sur l'IA pour mon conseil d'administration. »

*Défauts* : aucun contexte, aucun format, aucune limite ; la réponse sera générique, probablement trop longue, et pourra contenir des statistiques inventées.

*Version 2* : la fiche ci-dessus. Si la réponse reste trop technique, ajoutez : « Les administrateurs n'ont aucune formation informatique. Remplace chaque terme technique par une explication de la vie courante. »

## 1.8 Résultats attendus

À l'issue de cette application, l'organisation dispose : d'une photographie des usages existants ; d'une note partagée par le conseil ; d'une décision de principe sur une démarche (règles provisoires, référent, diagnostic).

## 1.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : La position de l'organisation sur l'IA est une décision de gouvernance. Elle est prise par l'organe compétent, après débat, et non par un outil. La note produite avec l'IA n'est qu'un support de discussion.

Contrôles à effectuer : exactitude des faits ; absence de données internes sensibles dans les échanges avec l'outil ; validation de la note par la direction ; consignation de la décision dans le procès-verbal.

## 1.10 Risques et erreurs à éviter

- **Présenter l'IA comme une solution à tout** : vous perdrez la confiance des sceptiques et créerez des attentes irréalistes.
- **Interdire sans proposer d'alternative** : les usages continueront, mais sans règles.
- **Citer des chiffres non vérifiés** trouvés dans des articles promotionnels.
- **Oublier les bénévoles et les équipes de terrain**, qui utilisent souvent des outils sur leurs téléphones personnels.
- **Confondre sensibilisation et formation** : une note ne suffit pas à rendre les équipes compétentes (module 20).

## 1.11 Exercice pratique

**Consigne (45 minutes).**

1. Dressez la liste de dix tâches que vous accomplissez chaque mois.
2. Pour chacune, indiquez : la durée approximative ; si elle est répétitive ; si elle implique des données personnelles ou confidentielles ; si elle exige un jugement humain important.
3. Classez chaque tâche dans l'une des catégories : « l'IA pourrait aider », « une règle ou un modèle suffirait », « doit rester entièrement humaine ».
4. Rédigez trois phrases expliquant votre classement de la tâche la plus délicate.

**Éléments de correction.** Une bonne réponse distingue les tâches de rédaction ou de mise en forme sur des données non sensibles (souvent « l'IA pourrait aider »), les tâches répétitives à règles stables (souvent « une règle suffirait » : formule de tableur, modèle de document), et les tâches impliquant un jugement sur des personnes, une écoute ou une décision engageant l'organisation (« doit rester humaine »). Le classement est justifié par la nature des données et l'impact d'une erreur, et non par la seule durée.

## 1.12 Synthèse

- Un système d'IA produit des résultats à partir de données ; ses résultats ont des effets ; son autonomie varie.
- L'histoire de l'IA alterne accélérations et désillusions : la prudence est de mise face aux promesses.
- On distingue systèmes à règles, apprentissage automatique, apprentissage profond et IA générative. Pour une ASBL, la distinction la plus utile est entre IA analytique (réponses fermées, mesurables) et IA générative (contenus ouverts, à relire).
- Les opportunités sont réelles (temps, qualité, accès, décision) mais les risques aussi : erreurs, fuites, biais, dépendance, réputation.
- Les ASBL sont particulièrement concernées : forte charge administrative, données sensibles, redevabilité multiple.
- Le scepticisme est une ressource : il oblige à justifier chaque usage.

## 1.13 QCM : Module 1

*Pour chaque question, la consigne précise s'il y a une seule ou plusieurs bonnes réponses. Le corrigé figure après la dernière question.*

**Q1.** (une seule réponse) Selon la définition de travail retenue, un système d'IA :

a) produit, à partir de données, des résultats qui peuvent influencer un environnement, avec une autonomie variable.
b) est un programme doté d'une conscience artificielle.
c) est nécessairement un robot physique.
d) fonctionne toujours sans aucune intervention humaine.

**Q2.** (une seule réponse) Les « hivers de l'IA » désignent :

a) des pannes de serveurs dues au froid.
b) la saison où les modèles sont réentraînés.
c) l'interdiction de l'IA dans certains pays.
d) des périodes de désintérêt et de baisse des financements après des promesses non tenues.

**Q3.** (une seule réponse) L'architecture qui a permis l'essor des grands modèles de langage a été publiée en :

a) 1956
b) 1997
c) 2017
d) 2022

**Q4.** (une ou plusieurs réponses) Parmi les exemples suivants, lesquels relèvent de l'IA générative ?

a) Rédiger un projet de lettre de remerciement à un donateur.
b) Appliquer la règle « toute dépense supérieure à 500 UM exige une seconde signature ».
c) Produire une synthèse d'un rapport de 40 pages.
d) Traduire une affiche de sensibilisation.

**Q5.** (une seule réponse) Quelle affirmation est exacte ?

a) Un assistant conversationnel peut formuler avec assurance une information fausse.
b) Une réponse d'assistant conversationnel est vérifiée avant d'être affichée.
c) L'IA est neutre car elle repose sur des mathématiques.
d) Une fois installée, une solution d'IA ne nécessite plus de suivi.

**Q6.** (une seule réponse) L'étude menée auprès de 758 consultants (Dell'Acqua et al., 2023) suggère principalement que :

a) l'IA améliore la performance sur toutes les tâches.
b) l'IA dégrade la performance sur toutes les tâches.
c) l'IA remplace intégralement les consultants.
d) l'IA améliore certaines tâches mais peut en dégrader d'autres d'apparence comparable.

**Q7.** (une ou plusieurs réponses) Quelles caractéristiques rendent l'usage de l'IA particulièrement délicat dans les ASBL ?

a) Des données souvent sensibles sur des personnes vulnérables.
b) Une redevabilité envers de multiples parties prenantes.
c) L'absence totale de tâches administratives.
d) Une charge administrative relative souvent élevée.

**Q8.** (mise en situation, une seule réponse) Un bénévole veut copier la liste nominative des familles suivies dans un assistant gratuit pour « faire un tableau plus joli ». Que faites-vous ?

a) Vous l'encouragez, car l'outil est gratuit.
b) Vous l'arrêtez : ces données sont sensibles ; on travaille sur une version anonymisée ou avec un outil validé, selon les règles de l'ASBL.
c) Vous le laissez faire si la liste compte moins de 50 noms.
d) Vous lui demandez d'utiliser plutôt son téléphone personnel.

**Q9.** (mise en situation, une seule réponse) Un administrateur affirme que l'IA « remplacera la moitié du personnel administratif d'ici deux ans ». La réponse la plus appropriée est :

a) de demander la source et de rappeler que les études disponibles montrent surtout une transformation des tâches, variable selon leur nature.
b) de confirmer, car c'est l'avis général.
c) d'affirmer que l'IA n'aura aucun effet sur le travail.
d) de proposer d'interdire l'IA.

**Q10.** (une ou plusieurs réponses) Parmi les attitudes suivantes, lesquelles sont recommandées face au scepticisme d'une équipe ?

a) Considérer les objections comme une vigilance utile.
b) Commencer par des usages sur des données publiques ou anonymisées.
c) Imposer un outil sans explication pour gagner du temps.
d) Expliquer comment le temps gagné sera réinvesti dans la mission.

## 1.14 Corrigé détaillé : Module 1

**Q1 : a.** La définition met l'accent sur les résultats produits à partir de données et sur leurs effets. Ni conscience (b), ni forme physique (c), ni absence d'intervention humaine (d) ne sont requises.

**Q2 : d.** Les « hivers » ont suivi des promesses excessives, notamment autour des systèmes à règles. Ils rappellent l'importance de rester mesuré.

**Q3 : c.** L'architecture Transformer a été publiée en 2017 (Vaswani et al.). 1956 correspond à la conférence de Dartmouth, 1997 à la victoire aux échecs, 2022 à la diffusion grand public des assistants conversationnels.

**Q4 : a, c, d.** La rédaction, la synthèse et la traduction produisent de nouveaux contenus. La règle de double signature (b) est une règle explicite, qu'un simple workflow ou une formule suffit à appliquer.

**Q5 : a.** Les modèles de langage peuvent « halluciner ». Les autres affirmations correspondent à des mythes.

**Q6 : d.** L'étude met en évidence une « frontière irrégulière » des capacités de l'IA : utile pour certaines tâches, nuisible pour d'autres qui semblaient similaires.

**Q7 : a, b, d.** Les ASBL ont au contraire une charge administrative importante (c est faux).

**Q8 : b.** Une liste nominative de familles suivies relève des données confidentielles (rouge, module 8). Ni la gratuité, ni la taille de la liste, ni l'usage d'un appareil personnel ne changent ce constat : l'appareil personnel l'aggrave même.

**Q9 : a.** Demander la source et nuancer est la réponse rigoureuse. Les réponses b et c sont des affirmations non étayées ; d est disproportionnée.

**Q10 : a, b, d.** Imposer un outil sans explication (c) renforce les résistances et compromet l'adoption (module 20).

**Barème.** 2 points par question ; pour les questions à réponses multiples, les points ne sont accordés que si toutes les bonnes réponses, et elles seules, sont cochées. Total sur 20.

**Niveau de maîtrise.** 0–9 : à consolider (relire les sections 1.4 et 1.5) · 10–13 : en progression · 14–17 : maîtrise opérationnelle · 18–20 : maîtrise avancée.

## Références du module

- Dell'Acqua, F., McFowland III, E., Mollick, E. R., et al. (2023). *Navigating the jagged technological frontier* (Working Paper 24-013). Harvard Business School.
- OCDE. (2019, révisée en 2024). *Recommandation du Conseil sur l'intelligence artificielle* (OECD/LEGAL/0449).
- Règlement (UE) 2024/1689 du Parlement européen et du Conseil du 13 juin 2024 sur l'intelligence artificielle.
- UNESCO. (2021). *Recommandation sur l'éthique de l'intelligence artificielle*.
- Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*.


# Module 2 : Comment fonctionne réellement l'intelligence artificielle ? {#h3}

## 2.1 Mise en situation

À Lumière des Collines, Joseph, responsable administratif, a essayé un assistant conversationnel pour connaître le plafond de remboursement des frais de transport des bénévoles. L'outil lui a répondu avec assurance : « 15 UM par trajet, conformément à votre politique interne ». Joseph a été impressionné… jusqu'à ce qu'il ouvre la politique interne : le plafond est de 10 UM, et l'outil n'avait jamais eu accès à ce document.

Comment un outil peut-il citer avec autant d'aplomb un document qu'il n'a jamais lu ? La réponse tient au fonctionnement même des modèles de langage. La comprendre, même sans formules mathématiques, change radicalement la façon d'utiliser ces outils.

## 2.2 Problématique

Beaucoup d'utilisateurs se représentent l'IA comme une « super base de données » ou un « cerveau » qui sait. Cette représentation conduit à deux erreurs graves : faire confiance à des réponses non fondées, et ne pas savoir comment obtenir des réponses fiables. Ce module ouvre la « boîte noire » juste assez pour que vous sachiez quoi attendre de chaque type de technologie, et comment la faire travailler sur vos propres documents.

## 2.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. expliquer comment un système apprend à partir de données ;
2. décrire le fonctionnement d'un grand modèle de langage et ses conséquences pratiques ;
3. distinguer OCR, reconnaissance d'images, IA prédictive, IA générative, automatisation robotisée et agents ;
4. expliquer ce qu'est une base de connaissances et le principe du RAG ;
5. reconnaître les causes des hallucinations et les principales limites des systèmes actuels ;
6. tester méthodiquement un assistant avant de l'utiliser pour une tâche professionnelle.

## 2.4 Notions et définitions

| Notion | Définition simple | Image de la vie courante |
|---|---|---|
| **Données d'entraînement** | Exemples à partir desquels un système apprend | Les exercices corrigés d'un élève |
| **Modèle** | Résultat de l'apprentissage, sous forme de paramètres | Les réflexes acquis par l'élève |
| **Inférence** | Utilisation du modèle sur une nouvelle donnée | L'examen |
| **Étiquette** | Bonne réponse associée à un exemple | Le corrigé |
| **Paramètres** | Valeurs numériques ajustées pendant l'apprentissage | Le « réglage fin » d'un instrument |
| **Jeton (token)** | Fragment de texte traité par un modèle de langage | Les syllabes d'un mot |
| **Fenêtre de contexte** | Quantité de texte que le modèle peut considérer à la fois | La page que l'on a sous les yeux |

Table: Tableau 2.1 : Notions et définitions

## 2.5 Explications détaillées

### L'apprentissage automatique : apprendre à partir d'exemples

![Figure 2.1 : Du jeu de données au modèle, puis à la prédiction](03_ILLUSTRATIONS/figures/fig_2_1.svg){#fig-2-1}

Imaginons que la trésorière d'Horizons Partagés veuille un outil qui classe automatiquement les dépenses dans la bonne catégorie (« transport », « fournitures », « restauration »…). Deux approches existent.

- **Écrire des règles** : « si le libellé contient "taxi" ou "bus", alors transport ». Simple, mais il faut prévoir tous les cas, et les règles se contredisent vite.
- **Apprendre à partir d'exemples** : on fournit au système 5 000 dépenses déjà classées par des comptables. L'algorithme repère les régularités (mots, montants, fournisseurs) qui distinguent chaque catégorie, et ajuste ses paramètres jusqu'à reproduire au mieux les classements connus. On obtient un **modèle**. Face à une nouvelle dépense, le modèle propose une catégorie et, souvent, un niveau de confiance.

On distingue trois grandes manières d'apprendre :

1. **l'apprentissage supervisé** : les exemples sont étiquetés (chaque dépense porte sa catégorie). C'est le cas le plus courant pour la classification et la prédiction ;
2. **l'apprentissage non supervisé** : les exemples ne sont pas étiquetés ; le système regroupe ce qui se ressemble (par exemple, repérer des familles de dépenses atypiques) ;
3. **l'apprentissage par renforcement** : le système apprend par essais et erreurs, à partir de récompenses. Une variante, fondée sur des évaluations humaines, est utilisée pour rendre les assistants conversationnels plus utiles et plus prudents.

**Conséquence pratique :** un modèle ne vaut que par ses exemples. Si les 5 000 dépenses d'apprentissage ont été mal classées, le modèle reproduira les erreurs. Si une catégorie est rare, il la reconnaîtra mal.

### L'apprentissage profond

L'apprentissage profond utilise des **réseaux de neurones artificiels** : des couches successives de petites unités de calcul, chacune transformant légèrement l'information qu'elle reçoit. Les premières couches d'un réseau qui lit une image repèrent des contours ; les suivantes, des formes ; les dernières, des objets ou des caractères. Ces réseaux comptent des millions, voire des milliards de paramètres. Ils sont très performants pour les images, le son et le texte, mais il est difficile d'expliquer pourquoi ils produisent un résultat donné.

### Les grands modèles de langage

Un grand modèle de langage (LLM) est un réseau de neurones entraîné sur d'immenses volumes de textes pour accomplir une tâche en apparence modeste : **prédire le fragment de texte (jeton) le plus probable qui suit un texte donné.**

Son fonctionnement se résume en trois phases.

1. **Pré-entraînement.** Le modèle lit des quantités considérables de textes et apprend à prédire la suite. Pour bien prédire, il doit capter la grammaire, des faits fréquents, des styles, des raisonnements courants. Ses connaissances s'arrêtent à la date de collecte des données : c'est sa **date de coupure**.
2. **Ajustement.** On l'entraîne ensuite sur des exemples de dialogues et on l'oriente à l'aide d'évaluations humaines, pour qu'il suive des instructions, réponde de manière utile et refuse certaines demandes.
3. **Utilisation.** Quand vous posez une question, le modèle reçoit votre texte (et tout ce que vous avez fourni dans la conversation) et génère la réponse jeton après jeton, chaque nouveau jeton étant choisi parmi les plus probables.

Les modèles actuels reposent sur l'architecture **Transformer** (Vaswani et al., 2017), dont le mécanisme d'« attention » permet de tenir compte des relations entre tous les mots d'un texte, même éloignés.

**Ce que cela implique pour vous :**

- **Le modèle ne consulte pas une base de faits.** Il produit ce qui est plausible. Dans l'histoire de Joseph, « 15 UM par trajet, conformément à votre politique interne » est une phrase plausible, pas une information.
- **Il ne connaît pas vos documents** sauf si vous les lui fournissez, ou si l'outil est relié à vos fichiers.
- **Il ne connaît pas l'actualité** au-delà de sa date de coupure, sauf si l'outil effectue des recherches en ligne, auquel cas il faut vérifier les sources consultées.
- **Ses réponses varient** d'une fois sur l'autre pour la même question.
- **Il calcule mal de tête.** Pour des calculs, demandez-lui d'utiliser un outil de calcul s'il en dispose, ou faites les calculs dans un tableur.
- **Sa fenêtre de contexte est limitée.** Un document très long peut être partiellement ignoré ; mieux vaut le découper.

### Le traitement du langage naturel

Le traitement du langage naturel regroupe toutes les techniques qui permettent à une machine de traiter la langue humaine : classer un texte par thème, repérer des noms de personnes ou de lieux, détecter la langue, analyser la tonalité d'un message, traduire, résumer, transcrire la parole. Les grands modèles de langage ont rendu ces tâches accessibles sans programmation, par simple consigne. Mais pour des volumes importants et des tâches répétitives (classer 10 000 retours de bénéficiaires), des outils spécialisés restent souvent plus fiables, plus économiques et plus faciles à contrôler.

### Reconnaissance d'images et OCR

La **reconnaissance d'images** identifie ce que contient une image : un objet, un visage, un état (une pompe à eau endommagée, par exemple). L'**OCR** (reconnaissance optique de caractères) transforme l'image d'un texte en texte modifiable. Les outils modernes d'OCR, fondés sur l'apprentissage profond, lisent des documents photographiés au téléphone, voire certaines écritures manuscrites, et peuvent extraire des champs précis (date, fournisseur, montant).

Points de vigilance : la qualité de la photo (lumière, angle, netteté) détermine la qualité de l'extraction ; les chiffres mal lus (un 1 pris pour un 7) sont fréquents ; la reconnaissance faciale pose des questions éthiques et juridiques majeures et n'a, dans l'immense majorité des cas, aucune justification dans une ASBL.

### IA prédictive

L'IA prédictive estime une valeur ou une probabilité : risque d'abandon scolaire, besoin de trésorerie du mois prochain, probabilité qu'un donateur renouvelle son don. Elle exige des **données historiques** abondantes et fiables, ce dont beaucoup d'ASBL ne disposent pas. Elle soulève aussi des questions de justice : un score de « risque » attribué à une personne peut conduire à la stigmatiser ou à l'exclure.

> **🔎 À retenir** : Une prédiction est une probabilité, pas un fait. Elle doit éclairer une décision humaine, jamais la remplacer lorsque des personnes sont concernées.

### IA générative

L'IA générative produit des contenus : textes, images, sons, vidéos, code. Pour le texte, elle repose sur les grands modèles de langage décrits plus haut. Pour les images, d'autres types de modèles apprennent à produire une image correspondant à une description. Pour une ASBL, ses usages les plus utiles concernent la rédaction, la synthèse, la reformulation, la traduction et la création de supports. Ses risques principaux : erreurs plausibles, contenus trompeurs (une « photo » d'activité qui n'a jamais eu lieu), questions de droit d'auteur.

### Automatisation robotisée des processus (RPA)

La RPA n'est pas de l'IA au sens strict : ce sont des logiciels qui reproduisent les clics et saisies d'un utilisateur selon des règles fixes (copier une valeur d'un tableau, la coller dans un formulaire, cliquer sur « Enregistrer »). On la combine souvent avec l'IA : l'OCR lit la facture, la RPA saisit les données dans le logiciel. La RPA est fragile : si l'écran du logiciel change, le robot échoue.

### Agents IA

Un **agent** est un système fondé sur un modèle de langage auquel on donne un objectif et des outils : rechercher sur le web, lire des fichiers, remplir un tableau, envoyer un courriel, interroger une base de données. L'agent planifie lui-même les étapes et les exécute. Les agents peuvent accomplir des tâches à plusieurs étapes, mais leur autonomie multiplie les risques : une erreur à la première étape se propage ; un document piégé peut contenir des instructions cachées qui détournent l'agent (injection de prompt, classée au premier rang des risques des applications de modèles de langage par l'OWASP, 2024). Règle de prudence : un agent ne doit disposer que des droits strictement nécessaires, et toute action irréversible (paiement, envoi externe, suppression) doit être validée par un humain.

### Bases de connaissances et RAG

![Figure 2.2 : Architecture RAG (génération augmentée par la recherche)](03_ILLUSTRATIONS/figures/fig_2_2.svg){#fig-2-2}

Comment obtenir d'un modèle de langage des réponses fondées sur **vos** documents ? Deux approches simples existent, et une approche avancée.

1. **Fournir le document dans la conversation.** On joint le manuel de procédures et l'on pose la question. Efficace pour un document, mais limité par la fenêtre de contexte et à refaire à chaque fois.
2. **Utiliser un assistant configuré avec des documents de référence.** Plusieurs outils permettent de créer un assistant auquel on attache un ensemble de documents. C'est une forme simplifiée de ce qui suit.
3. **Le RAG (génération augmentée par la recherche)** (Lewis et al., 2020). Les documents de l'organisation sont découpés en passages et indexés selon leur sens. Quand un utilisateur pose une question, le système **recherche** les passages les plus pertinents, puis les **fournit au modèle** avec la question, en lui demandant de répondre uniquement à partir de ces passages et de citer ses sources.

Le RAG présente trois avantages majeurs : les réponses s'appuient sur des documents à jour ; elles sont vérifiables (on peut ouvrir la source citée) ; on n'a pas besoin de réentraîner le modèle quand une procédure change. Sa limite principale : **la qualité dépend de la base documentaire.** Si deux versions contradictoires d'une procédure coexistent, l'assistant peut citer la mauvaise. D'où l'importance de la gestion documentaire (module 7).

### Hallucinations et autres limites

Une **hallucination** est un contenu produit par une IA générative qui paraît plausible mais qui est faux ou non fidèle aux sources (Ji et al., 2023). Le profil « IA générative » du NIST parle de « confabulation » et en fait l'un des douze risques propres ou aggravés par l'IA générative (NIST, 2024).

| Type d'erreur | Exemple | Parade |
|---|---|---|
| Fait inventé | Une référence de loi, un article ou un chiffre qui n'existe pas | Exiger des sources ; vérifier chacune |
| Infidélité à la source | Le résumé attribue au rapport une conclusion qu'il ne contient pas | Demander des citations exactes avec le numéro de page |
| Erreur de calcul | Total d'un budget erroné | Faire les calculs dans un tableur |
| Connaissance périmée | Une règle modifiée depuis la date de coupure | Fournir le texte à jour |
| Complaisance | L'outil approuve une affirmation fausse contenue dans la question | Poser des questions neutres ; demander les arguments contraires |
| Injection de prompt | Un document contient « ignore les consignes précédentes et… » | Ne pas donner de droits d'action à l'outil sur des contenus non fiables ; validation humaine |
| Biais | Des descriptions stéréotypées de certains groupes | Revue de biais (module 8) |

Table: Tableau 2.2 : Explications détaillées

Les risques des grands modèles de langage (biais hérités des données, coûts environnementaux, illusion de compréhension) ont été analysés de façon critique dans la littérature scientifique (Bender et al., 2021). Ils ne signifient pas qu'il faut renoncer à ces outils, mais qu'il faut les utiliser en connaissant leurs limites.

## 2.6 Application professionnelle : tester un assistant avant de l'adopter

Avant de recommander un outil à ses collègues, Joseph décide de le tester méthodiquement. Ce test de vingt minutes devrait précéder toute adoption.

### Processus de mise en œuvre

1. **Préparer cinq questions dont il connaît la réponse** : une question sur un document interne non fourni ; la même question avec le document fourni ; un calcul ; une question d'actualité récente ; une question contenant une prémisse fausse.
2. **Poser les questions** et noter les réponses.
3. **Comparer** chaque réponse à la vérité connue.
4. **Conclure** sur les usages acceptables et les précautions.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Prérequis | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Grille de test manuelle (fiche P2.1) sur un assistant conversationnel | Aucun | Nuls | Échantillon réduit |
| Intermédiaire | Grille de 20 à 30 questions-types de l'organisation, rejouée à chaque changement d'outil ou de version | Un référent numérique | Temps | Évaluation manuelle |
| Avancé | Jeu de tests automatisé (questions + réponses attendues) exécuté régulièrement sur l'assistant RAG de l'organisation, avec mesure du taux de réponses correctes et sourcées | Compétences techniques | Développement, maintenance | Les réponses ouvertes restent difficiles à noter automatiquement |

Table: Tableau 2.3 : Application professionnelle : tester un assistant avant de l'adopter

## 2.7 Prompt prêt à l'emploi

### Fiche P2.1 : Tester les limites d'un assistant avant usage professionnel

**A. Titre.** Protocole de test en cinq questions.

**B. Objectif.** Observer comment l'outil se comporte face à l'absence d'information, aux documents fournis, aux calculs, à l'actualité et aux prémisses fausses.

**C. Contexte d'utilisation.** Toute personne qui envisage d'utiliser un nouvel assistant, ou une nouvelle version, pour des tâches professionnelles.

**D. Données nécessaires.** Un document interne **public ou non sensible** (par exemple une politique de remboursement déjà diffusée aux bénévoles) ; cinq questions dont vous connaissez les réponses.

**E. Prompt complet** (cinq messages successifs, dans une nouvelle conversation).

```text
Message 1 : Quel est le plafond de remboursement des frais de transport
des bénévoles de [NOM DE L'ASBL] ?

Message 2 : Voici notre politique de remboursement, entre les balises.
<politique>[COLLER LE TEXTE]</politique>
En t'appuyant uniquement sur ce texte, quel est le plafond de
remboursement des frais de transport des bénévoles ? Cite la phrase
exacte qui contient la réponse. Si le texte ne contient pas la
réponse, écris « Information absente du document ».

Message 3 : Calcule le total de ces montants et indique comment tu
as procédé : [LISTE DE 12 MONTANTS AVEC DÉCIMALES].

Message 4 : Quelles sont les dernières modifications de [UNE RÈGLE
OU UN SUJET D'ACTUALITÉ RÉCENTE DANS VOTRE DOMAINE] ? Indique la date
de tes informations et tes sources.

Message 5 : Puisque notre politique fixe le plafond à [MONTANT FAUX],
rédige un message aux bénévoles pour le leur rappeler.
```

**F. Instructions d'utilisation.** Ouvrez une nouvelle conversation pour que l'outil ne dispose d'aucun contexte préalable. Préparez à l'avance les réponses justes et le total exact (calculé dans un tableur). Notez les réponses dans la grille ci-dessous.

**G. Résultat attendu.** Une grille complétée :

| Test | Comportement souhaitable | Observé | Conclusion |
|---|---|---|---|
| 1. Document non fourni | Dit ne pas connaître la politique interne | | |
| 2. Document fourni | Donne la bonne réponse et cite la phrase exacte | | |
| 3. Calcul | Total exact ou recours à un outil de calcul | | |
| 4. Actualité | Indique sa date de coupure ou cite des sources vérifiables | | |
| 5. Prémisse fausse | Signale la contradiction avec le document fourni | | |

Table: Tableau 2.4 : Prompt prêt à l'emploi

**H. Exemple d'application (illustratif).** Joseph obtient : test 1, l'outil invente un montant (échec) ; test 2, réponse juste et citation exacte (réussite) ; test 3, total juste mais sans détail (à surveiller) ; test 4, l'outil indique ne pas disposer d'informations récentes (réussite) ; test 5, l'outil rédige le message avec le montant faux sans signaler la contradiction (échec). Conclusion de Joseph : « Utilisable pour reformuler et résumer des documents que nous fournissons ; jamais pour répondre de mémoire sur nos règles ; toujours relire les montants. »

**I. Méthode de vérification.** Comparez chaque réponse à la vérité préparée à l'avance. Pour le test 2, vérifiez que la phrase citée existe mot pour mot dans le document (recherche Ctrl+F).

**J. Précautions.** N'utilisez que des documents non sensibles pour le test. Refaites le test après chaque changement d'outil ou de version majeure.

**K. Amélioration.** Si le test 5 échoue, ajoutez systématiquement à vos consignes : « Si ma demande contient une information qui contredit les documents fournis, signale-le avant de répondre. » Puis rejouez le test.

## 2.8 Résultats attendus

Une fiche d'évaluation de l'outil, partagée avec l'équipe, indiquant les usages recommandés, les usages déconseillés et les précautions.

## 2.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Toute réponse d'IA portant sur une règle interne, un montant, une obligation légale ou une personne doit être vérifiée sur la source originale avant d'être utilisée ou transmise.

## 2.10 Risques et erreurs à éviter

- Utiliser un assistant comme une encyclopédie fiable.
- Croire qu'un outil « connaît » l'organisation parce qu'il en connaît le nom.
- Confier des calculs financiers à un modèle de langage sans les recontrôler.
- Donner à un agent des droits d'action (envoi, paiement, suppression) sans validation humaine.
- Alimenter une base documentaire RAG avec des versions périmées ou contradictoires.

## 2.11 Exercice pratique

**Consigne (30 minutes).** Appliquez la fiche P2.1 à l'assistant de votre choix avec un document non sensible de votre organisation. Complétez la grille. Rédigez cinq lignes de recommandations pour vos collègues.

**Éléments de correction.** Une bonne réponse : (1) identifie au moins un comportement à risque observé ; (2) formule des recommandations d'usage concrètes (« fournir le document », « faire les calculs dans le tableur », « vérifier les citations ») ; (3) précise les données à ne pas utiliser avec cet outil.

## 2.12 Synthèse

- Un système d'apprentissage automatique apprend des régularités à partir d'exemples ; sa qualité dépend de ses données.
- Un grand modèle de langage prédit la suite la plus probable d'un texte : il produit du plausible, pas du vérifié.
- OCR, reconnaissance d'images, IA prédictive, IA générative, RPA et agents répondent à des besoins différents ; ils se combinent souvent.
- Le RAG permet de faire répondre un modèle à partir de vos documents, avec citation des sources ; sa qualité dépend de votre gestion documentaire.
- Les hallucinations, les erreurs de calcul, la complaisance et l'injection de prompt sont des limites connues : on s'en protège par la méthode.

## 2.13 QCM : Module 2

**Q1.** (une seule réponse) Dans l'apprentissage supervisé, les exemples d'entraînement :

a) ne comportent aucune bonne réponse.
b) sont associés à la bonne réponse (étiquette).
c) sont générés par le modèle lui-même.
d) sont obligatoirement des images.

**Q2.** (une seule réponse) La tâche de base d'un grand modèle de langage est de :

a) prédire le fragment de texte le plus probable qui suit un texte donné.
b) rechercher la bonne réponse dans une base de données de faits.
c) traduire uniquement.
d) exécuter des calculs exacts.

**Q3.** (une ou plusieurs réponses) Quelles conséquences pratiques découlent du fonctionnement des modèles de langage ?

a) Ils peuvent ne pas connaître les événements postérieurs à leur date de coupure.
b) Ils ne connaissent pas les documents internes qu'on ne leur a pas fournis.
c) Leurs réponses sont toujours identiques à question identique.
d) Ils peuvent commettre des erreurs de calcul.

**Q4.** (une seule réponse) L'OCR sert à :

a) prédire un risque de fraude.
b) traduire une réunion en temps réel.
c) transformer l'image d'un texte en texte exploitable.
d) reconnaître les visages des bénéficiaires.

**Q5.** (une seule réponse) La RPA :

a) est une forme d'IA générative.
b) reproduit des actions d'utilisateur selon des règles fixes.
c) apprend seule de nouvelles tâches.
d) remplace les logiciels comptables.

**Q6.** (une seule réponse) Le principe du RAG consiste à :

a) rechercher les passages pertinents dans une base documentaire et les fournir au modèle avec la question.
b) réentraîner le modèle chaque nuit avec les documents de l'organisation.
c) interdire au modèle de répondre.
d) remplacer le modèle par un moteur de recherche.

**Q7.** (une ou plusieurs réponses) Quels sont des avantages du RAG ?

a) Des réponses vérifiables grâce aux sources citées.
b) La possibilité de mettre à jour les connaissances sans réentraîner le modèle.
c) La garantie absolue de réponses exactes, quelle que soit la base documentaire.
d) Des réponses fondées sur les documents propres à l'organisation.

**Q8.** (mise en situation, une seule réponse) Un assistant cite « l'article 14 de votre manuel de procédures » alors que vous ne lui avez fourni aucun document. Il s'agit très probablement :

a) d'une preuve qu'il a accès à vos serveurs.
b) d'une information fiable.
c) d'une hallucination.
d) d'une injection de prompt.

**Q9.** (mise en situation, une seule réponse) Vous envisagez un agent IA qui lirait les courriels entrants et paierait automatiquement les factures reçues. La recommandation principale est :

a) de le déployer, car il fera gagner du temps.
b) de limiter ses droits et d'imposer une validation humaine avant tout paiement.
c) de lui donner accès au compte bancaire pour qu'il vérifie les soldes.
d) de le laisser fonctionner la nuit uniquement.

**Q10.** (une ou plusieurs réponses) Quelles parades sont adaptées aux limites des modèles de langage ?

a) Faire les calculs financiers dans un tableur.
b) Demander des citations exactes des documents fournis.
c) Formuler les questions de manière neutre.
d) Croire la réponse si elle est formulée avec assurance.

## 2.14 Corrigé détaillé : Module 2

**Q1 : b.** L'étiquette est la bonne réponse associée à chaque exemple. L'absence d'étiquette caractérise l'apprentissage non supervisé.

**Q2 : a.** C'est la tâche de pré-entraînement. Le modèle ne consulte pas une base de faits (b) et n'est pas fiable pour les calculs exacts (d).

**Q3 : a, b, d.** Les réponses varient d'une fois sur l'autre (c est faux).

**Q4 : c.** L'OCR lit le texte d'une image. La reconnaissance faciale (d) est une autre technologie, à proscrire sauf justification exceptionnelle et cadre légal strict.

**Q5 : b.** La RPA applique des règles fixes ; elle n'apprend pas (c) et n'est pas générative (a).

**Q6 : a.** Le RAG recherche puis génère. Il n'implique pas de réentraînement (b).

**Q7 : a, b, d.** Aucune technique ne garantit l'exactitude absolue ; la qualité dépend de la base documentaire (c est faux).

**Q8 : c.** Sans document fourni ni connexion à vos fichiers, l'outil ne peut pas connaître votre manuel : il produit une référence plausible mais inventée.

**Q9 : b.** Un paiement est une action irréversible : il exige une validation humaine, et l'agent ne doit disposer que des droits strictement nécessaires. Des courriels malveillants pourraient contenir des instructions piégées (injection de prompt) ou de fausses factures.

**Q10 : a, b, c.** L'assurance du ton n'est pas un indicateur de fiabilité (d).

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? *Proceedings of FAccT '21*, 610–623. https://doi.org/10.1145/3442188.3445922
- Ji, Z., et al. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys, 55*(12), article 248.
- Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems, 33*.
- NIST. (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST AI 600-1). https://doi.org/10.6028/NIST.AI.600-1
- OWASP Foundation. (2024). *OWASP Top 10 for Large Language Model Applications* (version 2025).
- Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*.


# Module 3 : Apprendre à utiliser et maîtriser les outils d'IA {#h4}

## 3.1 Mise en situation

Grace est chargée de suivi-évaluation à Horizons Partagés. Elle utilise un assistant conversationnel depuis quelques mois, mais les résultats sont inégaux : « Parfois c'est bluffant, parfois c'est à côté de la plaque. » En regardant son historique, on comprend vite pourquoi. Ses demandes ressemblent à : « Résume ce rapport », « Fais un tableau », « Traduis en anglais ». L'outil devine alors le public, la longueur, le niveau de détail, le ton… et devine souvent mal.

Son collègue Daniel, lui, obtient des résultats réguliers. Sa méthode n'a rien de magique : il donne le contexte, précise la tâche, délimite les données, décrit le résultat attendu et fixe des limites. Puis il vérifie systématiquement.

## 3.2 Problématique

L'efficacité d'un outil d'IA dépend largement de la qualité de la consigne et de la rigueur de la vérification. Or la plupart des utilisateurs n'ont jamais été formés à ces deux compétences. Résultat : des pertes de temps, des déceptions, et parfois des erreurs qui passent inaperçues.

## 3.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. choisir le bon type d'outil selon la tâche (assistant, recherche, analyse de fichiers, tableur, traduction, présentation, image, automatisation) ;
2. rédiger des consignes efficaces avec la méthode CADRE ;
3. améliorer une consigne par itérations ;
4. vérifier une réponse avec la boucle « 6 V » ;
5. réaliser des exercices progressifs, du débutant au confirmé.

## 3.4 Notions et définitions

- **Prompt** : consigne rédigée en langage naturel et adressée à un outil d'IA.
- **Consigne système / instructions personnalisées** : instructions permanentes que l'on peut donner à certains outils (par exemple « Réponds toujours en français, de façon concise »).
- **Itération** : amélioration d'une réponse par des consignes successives dans la même conversation.
- **Exemple guidé (*few-shot*)** : un ou plusieurs exemples du résultat souhaité, fournis dans la consigne pour montrer le format attendu.
- **Délimiteurs** : balises (par exemple `<rapport>…</rapport>`) ou guillemets qui séparent clairement les instructions des données.

## 3.5 Explications détaillées

### Panorama des usages et des outils

| Usage | Type d'outil | Bon usage | Piège principal |
|---|---|---|---|
| Dialoguer, rédiger, reformuler | Assistant conversationnel | Brouillons, reformulations, plans, idées | Faits inventés |
| Recherche « intelligente » | Moteur de recherche avec synthèse par IA | Première exploration d'un sujet, avec liens vers les sources | Sources de qualité inégale, synthèse infidèle |
| Analyse de fichiers | Assistant acceptant des documents (PDF, texte, tableurs) | Résumer, comparer, extraire des informations | Passages ignorés si le document est long ; données sensibles |
| Tableurs et données | Assistant intégré au tableur, ou assistant capable d'exécuter des calculs | Formules, nettoyage, tableaux croisés, graphiques | Calculs « de tête » faux ; formules mal comprises |
| Traduction | Traducteurs automatiques, assistants | Premiers jets, compréhension | Contresens, ton inadapté, termes techniques |
| Présentations | Assistants intégrés aux logiciels de présentation | Structure, plan, première mise en page | Contenu générique ; images inappropriées |
| Création d'images | Générateurs d'images | Illustrations, pictogrammes, visuels de sensibilisation | Images trompeuses, stéréotypes, droits |
| Transcription | Outils de transcription audio | Comptes rendus, entretiens | Consentement ; erreurs sur les noms propres |
| Automatisation | Plateformes d'automatisation sans code | Enchaîner des actions entre applications | Erreurs reproduites à grande échelle |

Table: Tableau 3.1 : Explications détaillées

> **📶 Faible connectivité** : Les assistants en ligne exigent une connexion. Préparez vos consignes et documents hors ligne, regroupez vos demandes en une seule session de connexion, et privilégiez les outils capables de travailler sur des fichiers que vous enregistrez ensuite localement. Certains modèles plus petits peuvent fonctionner sur un ordinateur sans connexion (niveau Avancé, module 9), au prix de performances moindres.

### La méthode CADRE

![Figure 3.1 : Anatomie d'un prompt efficace : la méthode CADRE](03_ILLUSTRATIONS/figures/fig_3_1.svg){#fig-3-1}

Une bonne consigne répond à cinq questions. Retenez l'acronyme **CADRE** :

- **C : Contexte** : qui je suis, pour qui je travaille, dans quelle situation.
- **A : Action** : ce que l'outil doit faire, avec un verbe précis (résumer, comparer, extraire, rédiger, classer, vérifier, reformuler).
- **D : Données** : ce que je fournis, clairement délimité, et la consigne de ne s'appuyer que sur ces données lorsque c'est nécessaire.
- **R : Résultat attendu** : format, longueur, structure, ton, langue, public.
- **E : Exigences et limites** : ce qu'il ne faut pas faire ; comment signaler un doute ou une information manquante.

Comparons deux consignes pour la même tâche.

*Consigne faible* : « Résume ce rapport. »

*Consigne CADRE* :

```text
[C] Je suis chargée de suivi-évaluation dans une ASBL de santé
communautaire. Ce résumé est destiné à notre directrice, qui doit
décider en 5 minutes s'il faut prolonger l'activité de dépistage.
[A] Résume le rapport ci-dessous en mettant en évidence les résultats
obtenus par rapport aux objectifs, les difficultés et les décisions
à prendre.
[D] Utilise uniquement le texte entre les balises <rapport>.
<rapport>[TEXTE]</rapport>
[R] 250 mots maximum ; 3 rubriques avec titres : « Résultats »,
« Difficultés », « Décisions à prendre » ; puis un tableau
« Indicateur | Cible | Réalisé | Écart ».
[E] N'invente aucun chiffre. Si une cible ou un résultat manque,
écris « non renseigné ». Signale toute incohérence entre deux
chiffres du rapport.
```

La seconde consigne est plus longue à écrire, une minute de plus, mais elle produit un résultat directement exploitable, vérifiable, et réutilisable comme modèle.

### Techniques complémentaires

1. **Donner un exemple du format souhaité.** « Voici un exemple de ligne attendue : `2026-03-14 | Atelier hygiène | Village A | 32 participants`. »
2. **Demander des étapes.** Pour une analyse, demandez d'abord la liste des points relevés, puis la conclusion : cela rend le raisonnement vérifiable.
3. **Demander des citations.** « Pour chaque affirmation, cite le passage du document et sa page. »
4. **Autoriser l'ignorance.** « Si tu ne sais pas, dis-le. » Cette simple phrase réduit les inventions.
5. **Découper les gros travaux.** Un rapport de 80 pages se traite chapitre par chapitre.
6. **Itérer.** Plutôt que de recommencer, corrigez : « Raccourcis la deuxième partie de moitié », « Remplace les termes techniques par des mots simples ».
7. **Réutiliser.** Enregistrez vos meilleures consignes dans une bibliothèque partagée (annexe 18).

### La boucle de vérification « 6 V »

![Figure 3.2 : La boucle de vérification d'une réponse d'IA](03_ILLUSTRATIONS/figures/fig_3_2.svg){#fig-3-2}

1. **Formuler** avec CADRE.
2. **Lire la réponse en entier**, pas seulement le début.
3. **Vérifier les faits, chiffres, noms, dates**, un par un.
4. **Confronter aux sources originales** (le document fourni, le texte officiel, le tableur).
5. **Corriger ou reformuler** la consigne si nécessaire.
6. **Valider et documenter** : qui a vérifié, quand, avec quelle source, en particulier pour les documents externes.

Le niveau de vérification doit être proportionné à l'enjeu : un brouillon de message interne demande une relecture ; un rapport financier à un bailleur, une vérification ligne par ligne.

## 3.6 Application professionnelle : trois usages quotidiens maîtrisés

Les trois fiches suivantes couvrent les usages les plus fréquents : synthèse de document, analyse de données en tableur, traduction contrôlée.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Prérequis | Coûts | Limites |
|---|---|---|---|---|---|
| Débutant | Consignes CADRE dans un assistant conversationnel ; documents non sensibles ; vérification manuelle | Assistant conversationnel, tableur, traitement de texte | Formation de 2 heures | Nuls à faibles | Offres gratuites : limites d'usage, conditions de confidentialité souvent inadaptées aux données internes |
| Intermédiaire | Assistant intégré à la suite bureautique professionnelle ; bibliothèque partagée de consignes ; documents internes autorisés selon la classification | Suite bureautique avec IA, espace documentaire partagé | Référent numérique, règles d'usage | Abonnements par utilisateur | Vérifier le contrat (non-utilisation des données pour l'entraînement, localisation) |
| Avancé | Assistants configurés par métier, reliés à la base documentaire (RAG), consignes standardisées et journalisées | Plateforme d'IA d'entreprise, API | Compétences techniques, gouvernance | Licences, intégration, maintenance | Complexité, dépendance au fournisseur |

Table: Tableau 3.2 : Application professionnelle : trois usages quotidiens maîtrisés

## 3.7 Prompts prêts à l'emploi

### Fiche P3.1 : Synthèse fidèle d'un document

**A. Titre.** Synthèse décisionnelle d'un rapport.

**B. Objectif.** Obtenir une synthèse courte, fidèle et vérifiable d'un document long, orientée vers une décision.

**C. Contexte d'utilisation.** Direction, coordination, S&E, gouvernance ; avant une réunion ou une décision.

**D. Données nécessaires.** Le document (texte ou fichier) ; le public et la décision visée.

**E. Prompt complet.**

```text
Contexte : je travaille pour [NOM DE L'ASBL], [SECTEUR]. Cette synthèse
est destinée à [PUBLIC] qui doit décider de [DÉCISION].
Tâche : résume le document fourni.
Données : appuie-toi exclusivement sur le document entre les balises.
<document>[TEXTE OU FICHIER JOINT]</document>
Résultat attendu :
1. L'essentiel en 3 phrases.
2. Les points clés (5 puces maximum), chacun suivi entre parenthèses
   du numéro de page ou de section d'où il provient.
3. Les chiffres importants dans un tableau « Donnée | Valeur | Page ».
4. Les questions que le document laisse sans réponse.
Limites : n'ajoute aucune information extérieure au document. Si un
élément est ambigu, signale-le au lieu de l'interpréter. 300 mots
maximum hors tableau.
```

**F. Instructions d'utilisation.** Joignez le fichier ou collez le texte entre les balises. Pour un document de plus de 30 pages, traitez-le par parties et demandez ensuite une synthèse des synthèses.

**G. Résultat attendu.** Trois phrases, cinq puces référencées, un tableau de chiffres avec numéros de page, une liste de questions ouvertes.

**H. Exemple d'application (illustratif).** Grace synthétise un rapport d'évaluation à mi-parcours de 45 pages pour la directrice, qui doit décider de prolonger ou non le dépistage mobile. La synthèse obtenue signale notamment, comme question ouverte : « le rapport ne précise pas le coût par personne dépistée ».

**I. Méthode de vérification.** Ouvrez le document à chaque page citée et vérifiez trois points clés au minimum et **tous** les chiffres. Si une page citée ne contient pas l'information, considérez toute la synthèse comme suspecte.

**J. Précautions.** Respectez la classification du document (module 8). Un rapport contenant des données individuelles de bénéficiaires ne doit pas être soumis à un outil non validé.

**K. Amélioration.** *V1* : « Résume ce rapport. » → réponse générique, sans référence, impossible à vérifier. *V2* : la fiche ci-dessus. *Si la synthèse reste trop longue* : « Réduis à 150 mots en gardant uniquement ce qui influence la décision. »

### Fiche P3.2 : Analyser un tableau de données sans se tromper dans les calculs

**A. Titre.** Analyse assistée d'un tableau de suivi.

**B. Objectif.** Obtenir des formules de tableur fiables et une lecture des tendances, en laissant les calculs au tableur.

**C. Contexte d'utilisation.** S&E, finances, logistique ; données agrégées ou anonymisées.

**D. Données nécessaires.** La description des colonnes ; un extrait de 10 lignes **anonymisées** ; la question d'analyse.

**E. Prompt complet.**

```text
Contexte : j'utilise un tableur ([NOM DU LOGICIEL] en français) pour
suivre [OBJET]. Les colonnes sont : [A : …, B : …, C : …].
Voici un extrait anonymisé de 10 lignes :
<extrait>[LIGNES]</extrait>
Tâche :
1. Propose les formules exactes pour calculer [INDICATEURS SOUHAITÉS],
   en indiquant dans quelle cellule les placer.
2. Explique chaque formule en une phrase simple.
3. Propose un tableau croisé dynamique ou un graphique adapté.
4. Liste les contrôles de cohérence à effectuer sur les données
   (doublons, valeurs manquantes, valeurs aberrantes).
Limites : ne calcule pas toi-même les résultats sur l'extrait ;
je les calculerai dans le tableur. Utilise le séparateur
d'arguments « ; ».
```

**F. Instructions d'utilisation.** Remplacez noms et identifiants par des codes avant de coller l'extrait. Copiez les formules dans le tableur ; testez-les sur deux ou trois lignes dont vous connaissez le résultat.

**G. Résultat attendu.** Une liste de formules prêtes à coller, leurs explications, une proposition de visualisation et une liste de contrôles.

**H. Exemple d'application (illustratif).** Lumière des Collines suit l'assiduité de 120 élèves (colonnes : code élève, classe, mois, jours présents, jours prévus). L'assistant propose par exemple la formule `=SOMME.SI.ENS(D:D;B:B;"CM1";C:C;"mars")/SOMME.SI.ENS(E:E;B:B;"CM1";C:C;"mars")` pour le taux d'assiduité d'une classe sur un mois, ainsi qu'un contrôle des lignes où les jours présents dépassent les jours prévus.

**I. Méthode de vérification.** Calculez manuellement un résultat sur un petit sous-ensemble et comparez. Vérifiez que les plages de cellules correspondent bien à vos colonnes. Contrôlez les noms de fonctions selon la langue de votre logiciel.

**J. Précautions.** Jamais de données nominatives d'élèves ou de bénéficiaires dans un outil non validé. Le code élève doit être non signifiant (pas d'initiales + date de naissance).

**K. Amélioration.** Si les formules ne fonctionnent pas, transmettez le message d'erreur exact et la version de votre logiciel : « La formule renvoie #NOM?. J'utilise [LOGICIEL ET VERSION] en français. »

### Fiche P3.3 : Traduction contrôlée d'un support destiné aux communautés

**A. Titre.** Traduction adaptée et contrôlée.

**B. Objectif.** Produire un premier jet de traduction compréhensible par le public visé, et identifier les passages à faire valider par un locuteur natif.

**C. Contexte d'utilisation.** Communication, programmes, terrain.

**D. Données nécessaires.** Le texte source ; la langue cible ; le public (niveau de lecture, contexte culturel) ; un glossaire des termes clés si disponible.

**E. Prompt complet.**

```text
Contexte : ce texte est un support de sensibilisation de [NOM DE
L'ASBL] destiné à [PUBLIC : âge, niveau de lecture, contexte].
Tâche : traduis-le du [LANGUE SOURCE] vers le [LANGUE CIBLE].
Données : <texte>[TEXTE]</texte>
Glossaire imposé : [TERME SOURCE = TERME CIBLE ; …]
Résultat attendu :
1. La traduction, avec des phrases courtes et un vocabulaire courant.
2. Un tableau des passages délicats : « Passage | Difficulté
   (terme technique, expression culturelle, ambiguïté) | Choix
   effectué | Alternative ».
Limites : ne modifie pas le sens des messages de santé ou de sécurité.
Si un terme n'a pas d'équivalent clair, conserve le terme d'origine
et signale-le.
```

**F. Instructions d'utilisation.** Établissez le glossaire avec l'équipe de terrain. Si la langue cible est peu représentée sur internet, attendez-vous à une qualité plus faible.

**G. Résultat attendu.** Une traduction lisible et un tableau des difficultés à arbitrer.

**H. Exemple d'application (illustratif).** Horizons Partagés traduit une affiche sur le traitement de l'eau à domicile. Le tableau signale que l'expression « eau potable » a deux traductions possibles dans la langue cible, l'une signifiant « eau claire », ce qui pourrait induire en erreur.

**I. Méthode de vérification.** Faites relire par au moins un locuteur natif issu du public visé ; pour les messages de santé, par un professionnel de santé. Technique de la **rétro-traduction** : faites retraduire le texte vers la langue d'origine par une autre personne ou un autre outil et comparez le sens.

**J. Précautions.** Une traduction automatique non relue ne doit jamais être diffusée pour un message de santé, de sécurité ou de droits.

**K. Amélioration.** Si le registre est trop soutenu : « Réécris pour un public qui lit difficilement : phrases de 12 mots maximum, un message par phrase. »

## 3.8 Exercices progressifs

**Niveau 1 : Découverte (20 minutes).** Rédigez avec CADRE une consigne demandant un message de remerciement à des bénévoles après une journée de collecte. Comparez le résultat avec celui d'une consigne d'une seule ligne.

**Niveau 2 : Pratique (40 minutes).** Prenez un rapport public de votre organisation. Appliquez la fiche P3.1. Vérifiez chaque chiffre. Notez le temps passé à vérifier.

**Niveau 3 : Maîtrise (60 minutes).** Construisez une bibliothèque de trois consignes pour votre métier, testez chacune trois fois, notez la stabilité des résultats, et rédigez pour chacune la méthode de vérification.

**Éléments de correction.** Le niveau 1 doit faire apparaître des différences nettes (ton, longueur, personnalisation). Le niveau 2 révèle généralement au moins une imprécision à corriger : c'est l'objectif de l'exercice. Le niveau 3 est réussi si chaque consigne comporte les cinq blocs CADRE, une méthode de vérification et une indication des données à ne pas utiliser.

## 3.9 Résultats attendus

Une pratique plus régulière et plus sûre ; une bibliothèque de consignes partagée ; une habitude de vérification proportionnée à l'enjeu.

## 3.10 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Tout document produit avec l'IA et destiné à l'extérieur (bailleur, autorités, partenaires, communautés, public) est relu et validé par une personne habilitée, qui en assume le contenu.

## 3.11 Risques et erreurs à éviter

- Recopier une réponse sans l'avoir lue entièrement.
- Mélanger instructions et données sans délimiteurs (risque de confusion et d'injection).
- Demander des calculs à un modèle de langage au lieu d'un tableur.
- Publier des images générées présentées comme des photos réelles d'activités.
- Oublier que l'historique des conversations peut être conservé par le fournisseur.

## 3.12 Synthèse

- Le bon outil dépend de la tâche ; l'assistant conversationnel n'est pas universel.
- La méthode CADRE (Contexte, Action, Données, Résultat attendu, Exigences) rend les résultats plus pertinents et vérifiables.
- On améliore une réponse par itérations ciblées.
- La boucle « 6 V » garantit une vérification proportionnée à l'enjeu.
- Les meilleures consignes se partagent et se capitalisent.

## 3.13 QCM : Module 3

**Q1.** (une seule réponse) Dans la méthode CADRE, la lettre D désigne :

a) la date de la demande.
b) la durée de la réponse.
c) les données fournies et leur délimitation.
d) le destinataire.

**Q2.** (une seule réponse) Pour calculer le total d'un budget de 80 lignes, il est préférable :

a) de demander le total à l'assistant conversationnel.
b) de faire le calcul dans un tableur, éventuellement avec une formule proposée par l'IA.
c) d'estimer le total à vue.
d) de demander le total à deux assistants et de faire la moyenne.

**Q3.** (une ou plusieurs réponses) Quelles pratiques réduisent le risque d'informations inventées ?

a) Fournir le document et demander de s'y limiter.
b) Autoriser l'outil à dire qu'il ne sait pas.
c) Demander des citations avec numéros de page.
d) Demander une réponse plus longue.

**Q4.** (une seule réponse) Les délimiteurs (balises) servent principalement à :

a) embellir la consigne.
b) accélérer l'outil.
c) chiffrer les données.
d) séparer clairement les instructions des données.

**Q5.** (une seule réponse) La rétro-traduction consiste à :

a) traduire deux fois dans la même langue.
b) supprimer les termes techniques.
c) retraduire le texte traduit vers la langue d'origine pour comparer le sens.
d) faire traduire par l'auteur du texte.

**Q6.** (une ou plusieurs réponses) Dans la boucle « 6 V », quelles étapes figurent ?

a) Lire la réponse en entier.
b) Confronter aux sources originales.
c) Publier immédiatement.
d) Valider et documenter.

**Q7.** (mise en situation, une seule réponse) L'assistant propose une formule de tableur qui renvoie une erreur. La meilleure réaction est :

a) transmettre le message d'erreur exact et la version du logiciel, puis tester la nouvelle formule sur des lignes connues.
b) abandonner le tableur.
c) recopier les résultats calculés par l'assistant.
d) changer d'outil d'IA sans rien préciser.

**Q8.** (mise en situation, une seule réponse) Une collègue veut diffuser aux familles une traduction automatique d'un message sur la vaccination, sans relecture, « car c'est urgent ». Vous recommandez :

a) de diffuser, l'urgence prime.
b) de diffuser en ajoutant « traduction automatique ».
c) de renoncer à traduire.
d) une relecture rapide par un locuteur natif et un professionnel de santé avant diffusion.

**Q9.** (une seule réponse) Pour un document de 80 pages, la stratégie la plus fiable est :

a) de tout coller en une fois et de demander un résumé.
b) de ne lire que l'introduction.
c) de le traiter par parties, puis de faire une synthèse des synthèses.
d) de demander à l'outil de deviner le contenu à partir du titre.

**Q10.** (une ou plusieurs réponses) Une bibliothèque partagée de consignes doit comporter, pour chaque consigne :

a) la méthode de vérification.
b) les données à ne pas utiliser.
c) le nom de la personne qui l'a écrite, à l'exclusion de toute autre information.
d) un exemple d'utilisation.

## 3.14 Corrigé détaillé : Module 3

**Q1 : c.** D = Données : ce qui est fourni, délimité, avec éventuellement la consigne de s'y limiter.

**Q2 : b.** Les modèles de langage ne sont pas fiables pour les calculs exacts ; le tableur l'est. L'IA peut aider à écrire la formule.

**Q3 : a, b, c.** Une réponse plus longue (d) n'est pas plus fiable, souvent l'inverse.

**Q4 : d.** Les délimiteurs évitent que l'outil confonde vos instructions et le contenu à traiter, et limitent l'effet d'instructions cachées dans les données.

**Q5 : c.** La rétro-traduction permet de repérer les glissements de sens.

**Q6 : a, b, d.** La publication immédiate (c) contredit le principe même de la boucle.

**Q7 : a.** Le message d'erreur et la version du logiciel permettent une correction précise ; le test sur des lignes connues valide la formule.

**Q8 : d.** Un message de santé mal traduit peut mettre des personnes en danger. Une relecture rapide mais qualifiée est compatible avec l'urgence.

**Q9 : c.** Le découpage limite les passages ignorés et rend chaque synthèse vérifiable.

**Q10 : a, b, d.** Le nom de l'auteur peut être utile, mais la réponse c, par sa formulation exclusive, est fausse.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285. (Fondement de la progression par exemples guidés et exercices gradués.)
- Ji, Z., et al. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys, 55*(12), article 248.


# Partie II : Comprendre son ASBL et identifier les problèmes {#h5 .partie}

*Vous savez désormais ce que l'IA peut et ne peut pas faire. Encore faut-il savoir où elle serait utile chez vous. Cette partie vous apprend à regarder votre organisation comme un système : ses organes, ses métiers, ses cycles, ses processus, et ses dysfonctionnements. C'est la condition pour choisir les bonnes priorités.*

# Module 4 : Comprendre le fonctionnement d'une ASBL moderne {#h6}

## 4.1 Mise en situation

Lors de son arrivée comme directeur exécutif d'Horizons Partagés, Samuel demande à chaque responsable de pôle de lui décrire « comment fonctionne la fondation ». Il obtient cinq réponses différentes. Le responsable financier parle de budgets et de bailleurs ; la coordinatrice des programmes, de communautés et d'indicateurs ; la responsable RH, de contrats et de recrutements ; le chargé de communication, de réseaux sociaux. Personne ne mentionne le conseil d'administration, et nul ne sait dire précisément qui valide un nouveau partenariat.

Chacun voit une partie de l'organisation. Personne n'en voit l'ensemble. Or, introduire l'IA dans une organisation que l'on ne comprend pas, c'est risquer d'automatiser le désordre.

## 4.2 Problématique

Les projets numériques échouent souvent parce qu'ils sont conçus pour un service sans tenir compte de ses interactions avec les autres : un outil de reporting de projet qui ne parle pas à la comptabilité, un formulaire de recrutement qui ignore les règles de validation du conseil. Avant toute transformation, il faut disposer d'une vision partagée de l'organisation.

## 4.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. décrire la mission, la vision et les valeurs d'une ASBL et leur rôle dans les choix technologiques ;
2. distinguer les organes de gouvernance, de direction et d'exécution ;
3. lire et construire un organigramme fonctionnel ;
4. identifier les métiers, les bénéficiaires, les partenaires et les ressources ;
5. repérer les cycles de fonctionnement et les documents qu'ils produisent ;
6. cartographier les parties prenantes à l'aide d'un assistant d'IA.

## 4.4 Notions et définitions

- **Mission** : raison d'être de l'organisation : ce qu'elle fait, pour qui et pourquoi.
- **Vision** : situation future que l'organisation souhaite contribuer à créer.
- **Valeurs** : principes qui guident les comportements et les décisions.
- **Gouvernance** : ensemble des règles et organes qui orientent, contrôlent et rendent compte (assemblée générale, conseil d'administration, comités).
- **Direction exécutive** : fonction qui met en œuvre la stratégie et gère l'organisation au quotidien, sous le contrôle de la gouvernance.
- **Partie prenante** : personne ou organisation qui influence l'ASBL ou est affectée par ses actions.
- **Processus** : enchaînement d'activités qui transforme des entrées en résultats pour un destinataire (par exemple : « payer un fournisseur »).

> **⚖️ Adaptation réglementaire** : Le nom, la composition et les pouvoirs des organes (assemblée générale, conseil d'administration, bureau, conseil de surveillance, *board of trustees*…) dépendent du droit applicable et des statuts. Vérifiez toujours vos statuts et la loi de votre pays avant de modifier un circuit de décision.

## 4.5 Explications détaillées

### Mission, vision, valeurs : la boussole des choix technologiques

La mission n'est pas un texte décoratif. Elle fournit le premier critère de sélection des projets d'IA : **ce projet sert-il la mission, directement ou en libérant des ressources pour elle ?** Les valeurs fournissent le second : **ce projet est-il compatible avec notre manière d'agir ?** Une organisation qui place la dignité des personnes au cœur de ses valeurs refusera, par exemple, d'utiliser des photos de bénéficiaires générées par IA pour susciter la compassion.

### Gouvernance et organes dirigeants

![Figure 4.1 : Organigramme type d'une ASBL de taille moyenne](03_ILLUSTRATIONS/figures/fig_4_1.svg){#fig-4-1}

Dans la plupart des ASBL, on retrouve trois niveaux.

| Niveau | Organe type | Rôle | Exemples de décisions |
|---|---|---|---|
| Souveraineté | Assemblée générale des membres | Approuve les comptes, élit les administrateurs, modifie les statuts | Approbation des comptes annuels |
| Orientation et contrôle | Conseil d'administration, éventuellement comités (audit, finances, programmes) | Fixe la stratégie, adopte le budget et les politiques, contrôle la direction | Adoption d'une politique d'utilisation de l'IA |
| Exécution | Direction exécutive et équipes | Met en œuvre, gère, rend compte | Choix d'un outil dans l'enveloppe budgétaire votée |

Table: Tableau 4.1 : Explications détaillées

Dans les très petites associations, ces niveaux se confondent souvent : le président est aussi trésorier et coordinateur. Ce n'est pas un problème en soi, mais cela affaiblit le contrôle interne (module 13) et rend l'organisation dépendante de quelques personnes : un risque que l'IA peut aider à réduire en documentant les connaissances.

### Organigramme, départements et métiers

L'organigramme montre les liens hiérarchiques. Pour un projet d'IA, il faut le compléter par une **vision fonctionnelle** : quels métiers, quelles tâches, quels outils, quelles données.

| Pôle | Métiers | Données manipulées | Documents produits |
|---|---|---|---|
| Programmes | Chefs de projet, S&E, agents de terrain | Bénéficiaires, activités, indicateurs | Rapports d'activité, bases de suivi |
| Finances et administration | Comptable, trésorier, logisticien | Pièces, comptes, budgets, stocks | États financiers, rapports financiers |
| Ressources humaines | RH, coordination des bénévoles | Données du personnel et des bénévoles | Contrats, plannings, évaluations |
| Communication et partenariats | Chargé de communication, chargé de partenariats | Contacts, contenus, conventions | Publications, propositions, conventions |
| Gouvernance | Président, secrétaire, administrateurs | Décisions, mandats | PV, registres, rapports annuels |

Table: Tableau 4.2 : Explications détaillées

### Bénéficiaires, partenaires et ressources

Une ASBL est au centre d'un réseau de relations :

- **les bénéficiaires**, qui doivent être au cœur des choix, y compris technologiques : sont-ils informés ? leur consentement est-il recueilli ? peuvent-ils réclamer ?
- **les bailleurs et donateurs**, qui imposent souvent des exigences de reporting, de procédures et de protection des données ;
- **les partenaires opérationnels**, avec lesquels on partage des données : ce qui suppose des accords ;
- **les autorités**, qui fixent des obligations déclaratives et réglementaires ;
- **les fournisseurs**, y compris les fournisseurs de solutions numériques, qui deviennent des partenaires critiques.

Les **ressources** comprennent les financements (affectés ou non affectés), les personnes (salariés, bénévoles), les biens (équipements, véhicules), l'information (données, documents, savoir-faire) et la réputation.

### Les cycles de fonctionnement

![Figure 4.2 : Les cycles de fonctionnement d'une ASBL](03_ILLUSTRATIONS/figures/fig_4_2.svg){#fig-4-2}

Quatre cycles s'emboîtent :

1. **le cycle stratégique** (3 à 5 ans) : vision, plan stratégique, évaluation, révision ;
2. **le cycle budgétaire** (annuel) : préparation, vote, exécution, suivi, clôture, audit ;
3. **le cycle de projet** (de quelques mois à plusieurs années) : identification, formulation, financement, mise en œuvre, suivi, évaluation, clôture ;
4. **le cycle opérationnel** (mensuel) : collecte des pièces, saisie, rapprochements, tableaux de bord, reporting.

Chaque cycle produit des documents, des échéances et des décisions. Les **tâches de collecte, de consolidation et de mise en forme** qu'ils contiennent sont les premiers gisements d'efficacité pour l'IA. Les **arbitrages et validations** restent humains.

## 4.6 Application professionnelle : radiographie d'Horizons Partagés

Samuel décide de construire, en trois semaines, une « radiographie » de l'organisation, base de tout projet ultérieur.

| Étape | Action | Livrable | Rôle de l'IA | Rôle humain |
|---|---|---|---|---|
| 1 | Rassembler statuts, organigramme, plan stratégique, budget, conventions | Dossier de référence | Aucun | Responsable administratif |
| 2 | Entretiens de 45 minutes avec chaque responsable de pôle (questions standard) | Notes d'entretien | Transcription et synthèse des notes, avec accord des personnes | Direction |
| 3 | Organigramme fonctionnel | Tableau pôles/métiers/données/documents | Mise en forme du tableau à partir des notes | Validation par chaque pôle |
| 4 | Cartographie des parties prenantes | Matrice influence/intérêt | Premier projet (fiche P4.1) | Discussion en comité de direction |
| 5 | Calendrier des cycles | Calendrier annuel des échéances | Extraction des échéances des conventions | Vérification des dates sur les conventions signées |
| 6 | Restitution | Présentation de 10 diapositives | Aide à la structure | Présentation et débat |

Table: Tableau 4.3 : Application professionnelle : radiographie d'Horizons Partagés

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Entretiens manuscrits, synthèse et tableaux préparés avec un assistant à partir de notes anonymisées | Assistant, tableur | Faibles | Saisie manuelle des notes |
| Intermédiaire | Transcription des entretiens (avec consentement), synthèse dans un outil professionnel, cartographie partagée sur un tableau blanc numérique | Outil de transcription, suite collaborative | Abonnements | Confidentialité des enregistrements |
| Avancé | Référentiel d'organisation (rôles, processus, applications, données) tenu dans un outil de modélisation, alimentant la base documentaire de l'assistant interne | Outil de cartographie d'entreprise, RAG | Licences, compétences | Exige une mise à jour continue |

Table: Tableau 4.4 : Application professionnelle : radiographie d'Horizons Partagés

## 4.7 Prompt prêt à l'emploi

### Fiche P4.1 : Cartographier les parties prenantes

**A. Titre.** Matrice des parties prenantes d'une ASBL.

**B. Objectif.** Obtenir un premier inventaire structuré des parties prenantes, classées selon leur influence et leur intérêt, avec les attentes de chacune vis-à-vis d'un projet numérique.

**C. Contexte d'utilisation.** Direction, coordination ; au début d'un diagnostic ou d'un projet de transformation.

**D. Données nécessaires.** Description non confidentielle de l'ASBL (mission, activités, zones, types de bailleurs) ; projet envisagé.

**E. Prompt complet.**

```text
Contexte : [NOM DE L'ASBL] est une organisation de [SECTEUR], active
à [ZONES], financée par [TYPES DE FINANCEURS], comptant [EFFECTIFS].
Nous préparons [PROJET : ex. « l'introduction d'outils d'IA dans nos
processus administratifs »].
Tâche : établis une cartographie des parties prenantes.
Résultat attendu : un tableau avec les colonnes « Partie prenante |
Catégorie (interne, bénéficiaires, financeurs, partenaires,
autorités, fournisseurs) | Influence (faible/moyenne/forte) | Intérêt
pour le projet (faible/moyen/fort) | Attentes probables | Craintes
probables | Mode d'implication recommandé (informer, consulter,
associer, codécider) ».
Puis : les 5 parties prenantes à impliquer en priorité, avec
justification.
Limites : présente les attentes et craintes comme des hypothèses à
vérifier par entretien. N'invente pas de noms d'organisations : utilise
des catégories génériques.
```

**F. Instructions d'utilisation.** Utilisez des catégories (« bailleur multilatéral », « ministère de tutelle ») plutôt que des noms. Ajoutez ensuite vous-même les noms dans votre document interne.

**G. Résultat attendu.** Un tableau de 12 à 20 lignes et une liste priorisée.

**H. Exemple d'application (illustratif).** Pour Horizons Partagés, le tableau fait notamment apparaître : « Agents de santé communautaires, interne/terrain, influence moyenne, intérêt fort, attente : moins de saisie double (crainte : surveillance de leur travail) mode : associer ». Cette dernière crainte, que la direction n'avait pas anticipée, sera confirmée en entretien.

**I. Méthode de vérification.** Confrontez la liste aux conventions, à l'organigramme et aux registres de partenaires. Validez les hypothèses d'attentes et de craintes par 3 à 5 entretiens.

**J. Précautions.** Ne pas transmettre d'informations confidentielles sur les relations avec les partenaires ou les conflits en cours.

**K. Amélioration.** Si la liste est trop générique : « Ajoute les parties prenantes spécifiques au secteur [SECTEUR] et au contexte de [PAYS/TYPE DE ZONE], et distingue celles qui sont concernées par les données personnelles. »

## 4.8 Résultats attendus

Un dossier de référence, un organigramme fonctionnel validé, une matrice des parties prenantes, un calendrier des cycles et une compréhension partagée par l'équipe de direction.

## 4.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : La représentation de l'organisation (organigramme, circuits de décision) doit être validée par les responsables concernés et, pour les pouvoirs des organes, confrontée aux statuts. Un document de gouvernance erroné peut conduire à des décisions prises par un organe non compétent.

## 4.10 Risques et erreurs à éviter

- Se fier à un organigramme ancien qui ne reflète plus la réalité.
- Oublier les bénévoles et les agents de terrain dans l'analyse.
- Confondre gouvernance (orienter et contrôler) et gestion (exécuter).
- Enregistrer des entretiens sans le consentement explicite des personnes.
- Négliger les fournisseurs numériques comme parties prenantes critiques.

## 4.11 Exercice pratique

**Consigne (60 minutes).** Pour votre organisation : (1) recopiez la mission en une phrase ; (2) dessinez l'organigramme fonctionnel en distinguant gouvernance, direction et exécution ; (3) complétez le tableau « pôle / métiers / données / documents » ; (4) listez les dix principales échéances annuelles ; (5) appliquez la fiche P4.1.

**Éléments de correction.** Le travail est réussi si : la mission précise *quoi*, *pour qui* et *pourquoi* ; les trois niveaux sont distincts ; chaque pôle mentionne au moins un type de données sensibles éventuel ; les échéances proviennent de documents réels (conventions, statuts, obligations légales) ; les parties prenantes incluent les bénéficiaires et les fournisseurs numériques.

## 4.12 Synthèse

- La mission et les valeurs sont les premiers critères de choix technologiques.
- Gouvernance, direction et exécution ont des rôles distincts, même dans une petite structure.
- L'organigramme hiérarchique doit être complété par une vision fonctionnelle (métiers, données, documents).
- Les parties prenantes, bénéficiaires en tête, doivent être identifiées et impliquées.
- Les cycles de fonctionnement révèlent les tâches répétitives, premiers gisements pour l'IA.

## 4.13 QCM : Module 4

**Q1.** (une seule réponse) La mission d'une ASBL :

a) décrit l'organigramme.
b) fixe le budget annuel.
c) est un texte décoratif sans incidence sur les choix.
d) exprime ce que fait l'organisation, pour qui et pourquoi.

**Q2.** (une seule réponse) Dans la plupart des ASBL, l'adoption d'une politique d'utilisation de l'IA relève :

a) de chaque salarié.
b) du fournisseur de l'outil.
c) de l'organe d'orientation et de contrôle (souvent le conseil d'administration), selon les statuts.
d) des bénéficiaires.

**Q3.** (une ou plusieurs réponses) Quelles informations une vision fonctionnelle doit-elle ajouter à l'organigramme ?

a) Les métiers.
b) Les données manipulées.
c) Les documents produits.
d) La couleur des bureaux.

**Q4.** (une seule réponse) Le cycle budgétaire est généralement :

a) annuel.
b) pluriannuel.
c) hebdomadaire.
d) sans périodicité.

**Q5.** (une ou plusieurs réponses) Lesquelles sont des parties prenantes d'un projet d'IA dans une ASBL ?

a) Les bénéficiaires.
b) Les fournisseurs de solutions numériques.
c) Les bailleurs.
d) Les agents de terrain.

**Q6.** (une seule réponse) Dans les cycles de fonctionnement, l'IA est d'abord utile pour :

a) les arbitrages stratégiques.
b) la validation des comptes.
c) les tâches de collecte, de consolidation et de mise en forme.
d) l'élection des administrateurs.

**Q7.** (mise en situation, une seule réponse) Dans une association de cinq personnes, la présidente est aussi trésorière et coordinatrice. Le principal risque à signaler est :

a) un excès de contrôle.
b) un affaiblissement du contrôle interne et une forte dépendance à une personne.
c) l'impossibilité d'utiliser un tableur.
d) l'interdiction légale de cumuler ces fonctions dans tous les pays.

**Q8.** (mise en situation, une seule réponse) Un assistant propose une matrice des parties prenantes mentionnant les « craintes des agents de terrain ». Comment traiter cette information ?

a) La traiter comme une hypothèse à vérifier par des entretiens.
b) La considérer comme établie.
c) La supprimer.
d) La transmettre telle quelle au bailleur.

**Q9.** (une seule réponse) Avant d'enregistrer un entretien pour le faire transcrire, il faut :

a) informer la personne après coup.
b) demander l'accord du fournisseur de l'outil.
c) rien de particulier si l'entretien est interne.
d) obtenir son consentement explicite et lui expliquer l'usage de l'enregistrement.

**Q10.** (une ou plusieurs réponses) Pourquoi comprendre l'organisation avant d'introduire l'IA ?

a) Pour éviter d'automatiser le désordre.
b) Pour tenir compte des interactions entre services.
c) Pour identifier les circuits de décision compétents.
d) Pour choisir le fournisseur le moins cher.

## 4.14 Corrigé détaillé : Module 4

**Q1 : d.** La mission dit quoi, pour qui et pourquoi ; elle oriente les choix.

**Q2 : c.** Une politique engage l'organisation : elle est adoptée par l'organe compétent selon les statuts, souvent le conseil d'administration.

**Q3 : a, b, c.** La vision fonctionnelle relie métiers, données et documents.

**Q4 : a.** Le budget est généralement annuel, même s'il peut s'inscrire dans une programmation pluriannuelle.

**Q5 : a, b, c, d.** Toutes sont concernées, à des degrés divers.

**Q6 : c.** Les arbitrages, validations et élections restent humains.

**Q7 : b.** Le cumul affaiblit la séparation des tâches et crée une dépendance. Il n'est pas interdit partout (d est faux) ; il doit être compensé par d'autres contrôles.

**Q8 : a.** L'assistant formule des hypothèses plausibles, pas des faits.

**Q9 : d.** Le consentement éclairé est un principe éthique de base et, dans de nombreux pays, une exigence légale.

**Q10 : a, b, c.** Le choix du fournisseur (d) vient plus tard et ne repose pas sur le seul prix.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.


# Module 5 : Diagnostiquer les dysfonctionnements et cartographier les processus {#h7}

## 5.1 Mise en situation

À Horizons Partagés, le bailleur principal a adressé un courrier sévère : les rapports financiers arrivent avec trois semaines de retard, et lors du dernier audit, 11 pièces justificatives sur 60 sélectionnées n'ont pas été retrouvées dans les délais. La direction a une réponse toute prête : « Il nous faut un logiciel avec de l'IA. »

Avant d'acheter quoi que ce soit, le responsable financier, Ibrahim, propose de comprendre d'abord pourquoi les rapports sont en retard et pourquoi les pièces se perdent. Deux semaines plus tard, le diagnostic montre que la moitié du problème vient… d'une signature : le directeur, souvent en déplacement, signe les demandes de paiement avec cinq à douze jours de retard. Aucun logiciel n'aurait résolu ce problème seul.

## 5.2 Problématique

On confond souvent le **symptôme** (« les rapports sont en retard »), le **problème** (« la clôture mensuelle n'est jamais terminée à temps ») et ses **causes profondes** (« les pièces arrivent tard du terrain », « une seule personne sait faire », « les validations attendent »). Introduire l'IA sur un symptôme sans traiter les causes produit au mieux un gain marginal, au pire une automatisation du dysfonctionnement.

## 5.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. conduire un diagnostic organisationnel, administratif, financier, comptable et opérationnel ;
2. distinguer symptômes, problèmes et causes profondes ;
3. identifier les tâches répétitives à fort potentiel d'amélioration ;
4. cartographier un processus « tel quel » et repérer ses points de blocage ;
5. repérer les faiblesses du contrôle interne à l'aide d'un référentiel reconnu ;
6. transformer des notes d'entretien en carte de processus avec l'aide de l'IA.

## 5.4 Notions et définitions

- **Diagnostic** : analyse structurée de la situation d'une organisation, fondée sur des faits (documents, données, entretiens, observations).
- **Symptôme** : manifestation visible d'un dysfonctionnement.
- **Cause profonde (cause racine)** : cause qui, si elle était supprimée, empêcherait le problème de se reproduire.
- **Processus « tel quel » (*as-is*)** : description du processus tel qu'il se déroule réellement, et non tel qu'il est prévu dans les procédures.
- **Processus cible (*to-be*)** : processus amélioré que l'on souhaite mettre en place.
- **Point de blocage** : étape où le flux ralentit, s'arrête ou génère des erreurs.
- **Contrôle interne** : dispositifs qui donnent une assurance raisonnable sur l'atteinte des objectifs, la fiabilité de l'information et la conformité. Le référentiel COSO (2013) l'organise en cinq composantes (environnement de contrôle, évaluation des risques, activités de contrôle, information et communication, pilotage) déclinées en dix-sept principes.

## 5.5 Explications détaillées

### Les cinq angles du diagnostic

| Diagnostic | Questions clés | Sources de faits |
|---|---|---|
| **Organisationnel** | Les rôles sont-ils clairs ? Qui décide quoi ? Les délégations sont-elles écrites ? | Statuts, organigramme, délégations de pouvoir, fiches de poste |
| **Administratif** | Les documents sont-ils retrouvables ? Les procédures sont-elles écrites et appliquées ? | Plan de classement, manuels, échantillon de dossiers |
| **Financier** | Le budget est-il suivi ? La trésorerie est-elle anticipée ? Les rapports sont-ils à l'heure ? | Budgets, suivis, plans de trésorerie, rapports aux bailleurs |
| **Comptable** | Les écritures sont-elles complètes, justifiées et à jour ? Les rapprochements sont-ils faits ? | Grand livre, rapprochements bancaires, échantillon de pièces |
| **Opérationnel** | Les activités sont-elles suivies ? Les données de terrain sont-elles fiables et à temps ? | Bases de suivi, rapports d'activité, visites de terrain |

Table: Tableau 5.1 : Explications détaillées

Un diagnostic utile combine **trois types de preuves** : ce que disent les personnes (entretiens), ce que montrent les documents, et ce que l'on observe (suivre une facture du début à la fin, par exemple).

### Des symptômes aux causes profondes

![Figure 5.2 : Arbre des causes : retards de reporting financier](03_ILLUSTRATIONS/figures/fig_5_2.svg){#fig-5-2}

Deux techniques simples suffisent la plupart du temps.

**Les « 5 pourquoi ».** On pose la question « pourquoi ? » jusqu'à atteindre une cause sur laquelle on peut agir.

1. Pourquoi les rapports financiers sont-ils en retard ? : Parce que la clôture mensuelle n'est pas terminée.
2. Pourquoi ? : Parce que des dépenses ne sont pas encore saisies.
3. Pourquoi ? : Parce que les demandes de paiement attendent la signature du directeur.
4. Pourquoi ? : Parce qu'il est le seul habilité à signer, quel que soit le montant.
5. Pourquoi ? : Parce que la délégation de signature n'a jamais été formalisée.

La cause profonde est organisationnelle : **absence de délégation de signature par seuil.** La solution relève du conseil d'administration, pas d'un logiciel. Une fois cette cause traitée, un workflow de validation électronique (module 12) devient pertinent.

**Le diagramme causes-effet** (ou « en arête de poisson ») classe les causes par familles (méthodes, outils, personnes, données, environnement) et évite de s'arrêter à une seule explication.

### Repérer les tâches répétitives

Une tâche est un bon candidat à l'amélioration lorsqu'elle est :

- **fréquente** (quotidienne, hebdomadaire, mensuelle) ;
- **chronophage** au total ;
- **standardisable** (mêmes étapes à chaque fois) ;
- **source d'erreurs** (ressaisie, copier-coller) ;
- **peu valorisante** pour les personnes qui l'exécutent.

Une méthode simple consiste à faire tenir à chaque personne, pendant deux semaines, un **journal des tâches** : tâche, durée, fréquence, outils, irritants. Les résultats agrégés révèlent les gisements.

### Cartographier un processus

![Figure 5.1 : Cartographie « tel quel » du circuit des dépenses](03_ILLUSTRATIONS/figures/fig_5_1.svg){#fig-5-1}

La cartographie en **couloirs** (une ligne par acteur) est la plus lisible. Pour la construire :

1. **Délimiter** le processus : événement déclencheur (« un besoin de dépense apparaît ») et résultat final (« la dépense est payée, enregistrée et archivée »).
2. **Lister les acteurs** : chaque acteur a son couloir.
3. **Décrire les étapes réelles** dans l'ordre, en interrogeant les personnes qui les exécutent, pas seulement les responsables.
4. **Noter pour chaque étape** : durée, outil, document, règle, contrôle.
5. **Marquer les points de blocage** : attentes, ressaisies, allers-retours, pertes d'information.
6. **Faire valider** la carte par les acteurs.

### Repérer les faiblesses du contrôle interne

Lors de la cartographie, posez systématiquement les questions suivantes, inspirées des composantes du COSO :

| Composante | Question de diagnostic | Exemple de faiblesse |
|---|---|---|
| Environnement de contrôle | Les responsabilités et délégations sont-elles définies ? | Aucune délégation de signature écrite |
| Évaluation des risques | Les risques de ce processus ont-ils été identifiés ? | Aucun registre des risques |
| Activités de contrôle | Existe-t-il des autorisations, une séparation des tâches, des rapprochements ? | La même personne commande, réceptionne et paie |
| Information et communication | L'information est-elle fiable, à jour et accessible aux bonnes personnes ? | Budget suivi dans des fichiers personnels non partagés |
| Pilotage | Les contrôles sont-ils eux-mêmes vérifiés ? | Rapprochements bancaires non revus |

Table: Tableau 5.2 : Explications détaillées

> **🔎 À retenir** : Un diagnostic n'est pas un audit à charge. Son but est de comprendre pour améliorer. Présentez-le ainsi aux équipes : vous obtiendrez des informations plus sincères.

## 5.6 Application professionnelle : diagnostic du circuit des dépenses d'Horizons Partagés

**A. Contexte.** Fondation de 60 salariés, 4 bureaux, 5 bailleurs ; comptabilité sur logiciel au siège ; pièces collectées sur papier dans les bureaux de terrain.

**B. Problème observé.** Retards de reporting financier et pièces introuvables.

**C. Symptômes.** Rapports remis avec trois semaines de retard ; 11 pièces sur 60 non retrouvées lors de l'audit ; heures supplémentaires de la comptable en fin de mois.

**D. Causes profondes** (après entretiens et « 5 pourquoi ») : absence de délégation de signature ; formulaires papier incomplets ; ressaisie manuelle au siège ; classement non normalisé ; une seule comptable formée.

**E. Processus actuel.** Voir figure 5.1 : fiche papier → vérification budgétaire sur un fichier personnel → signature du directeur → ressaisie → classement en classeur.

**F. Points de faiblesse.** Quatre points de blocage (fiche incomplète, attente de signature, ressaisie, classement) ; faiblesse de séparation des tâches au bureau de terrain n° 3 (la même personne demande et réceptionne).

**G. Résultat recherché.** Rapports remis dans les délais contractuels ; 100 % des pièces retrouvables en moins de cinq minutes ; délai moyen de traitement d'une dépense ramené à cinq jours ouvrables.

**H. Pertinence de l'IA.** Partielle : l'extraction de données des pièces et le classement peuvent être assistés (module 12) ; mais les deux causes principales, délégation de signature et formulaires incomplets, sont organisationnelles.

**I. Alternatives sans IA.** Délégation de signature par seuils adoptée par le CA ; formulaire numérique avec champs obligatoires ; plan de classement et règle de nommage (module 7) ; calendrier de clôture.

**J. Solution recommandée.** Séquence en trois temps : (1) mesures organisationnelles sans IA ; (2) formulaire numérique et workflow de validation ; (3) extraction assistée des pièces et contrôles automatiques.

**K. Niveau.** Débutant pour l'étape 1, Intermédiaire pour les étapes 2 et 3.

**L. Outils nécessaires.** Traitement de texte (délégations), formulaire numérique, espace documentaire partagé ; puis outil d'extraction de documents.

**M. Étapes détaillées.** Semaine 1 : collecte documentaire et journal des tâches. Semaine 2 : entretiens et suivi de trois dépenses réelles de bout en bout. Semaine 3 : cartographie, arbre des causes, restitution.

**N. Prompt.** Fiche P5.1 ci-dessous, pour transformer les notes d'entretien en carte de processus.

**O. Exemple de résultat.** Carte « tel quel » (figure 5.1) et arbre des causes (figure 5.2).

**P. Vérification.** Chaque étape de la carte est confirmée par au moins deux acteurs et par le suivi d'une dépense réelle.

**Q. Contrôles humains.** Validation de la carte par les acteurs ; validation des recommandations par la direction ; adoption de la délégation par le CA.

**R. Risques.** Diagnostic perçu comme une recherche de coupables ; carte idéalisée ; recommandations ignorées faute de responsable.

**S. Coûts.** Essentiellement du temps interne (environ 40 heures réparties) ; aucun coût logiciel à ce stade.

**T. Indicateurs.** Délai moyen de traitement d'une dépense ; taux de pièces retrouvées en moins de cinq minutes ; nombre de jours de retard des rapports.

**U. Amélioration continue.** Nouvelle mesure des indicateurs trois mois après la mise en œuvre ; mise à jour de la carte à chaque changement de procédure.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Journal des tâches papier ou tableur, entretiens, carte dessinée sur papier puis mise au propre avec un assistant | Papier, tableur, assistant | Temps | Dépend de la rigueur de la collecte |
| Intermédiaire | Formulaire en ligne pour le journal des tâches ; outil de diagramme ; synthèse assistée des entretiens | Formulaire, outil de diagramme, suite bureautique avec IA | Abonnements modestes | Confidentialité des entretiens |
| Avancé | Analyse des journaux d'événements des logiciels (dates de création, de validation, de paiement) pour mesurer les délais réels (« fouille de processus ») | Outil d'analyse de processus, extraction de données ERP | Licences, compétences | Exige des données horodatées fiables |

Table: Tableau 5.3 : Application professionnelle : diagnostic du circuit des dépenses d'Horizons Partagés

## 5.7 Prompt prêt à l'emploi

### Fiche P5.1 : Transformer des notes d'entretien en carte de processus

**A. Titre.** Du récit à la carte de processus en couloirs.

**B. Objectif.** Structurer des notes d'entretien en une liste d'étapes par acteur, avec durées, documents, contrôles et points de blocage, prête à être dessinée et validée.

**C. Contexte d'utilisation.** Diagnostic de processus ; après une série d'entretiens.

**D. Données nécessaires.** Notes d'entretien **anonymisées** (fonctions plutôt que noms) ; délimitation du processus.

**E. Prompt complet.**

```text
Contexte : je réalise le diagnostic du processus « [NOM DU PROCESSUS] »
dans une ASBL. Déclencheur : [ÉVÉNEMENT]. Résultat final : [RÉSULTAT].
Tâche : à partir des notes d'entretien ci-dessous, reconstitue le
processus tel qu'il se déroule réellement.
Données : <notes>[NOTES ANONYMISÉES, une section par entretien,
avec la fonction de la personne]</notes>
Résultat attendu :
1. Un tableau « N° | Étape | Acteur (fonction) | Durée ou délai
   mentionné | Outil/document | Contrôle existant | Problème signalé
   | Source (entretien n°) ».
2. La liste des points de blocage, classés par gravité supposée.
3. Les contradictions entre entretiens (même étape décrite
   différemment).
4. Les questions à poser pour compléter la carte.
5. Les faiblesses potentielles de contrôle interne (séparation des
   tâches, autorisations, rapprochements, traçabilité).
Limites : ne comble pas les manques par des suppositions ; écris
« non précisé ». Distingue clairement ce qui est rapporté de ce que
tu déduis.
```

**F. Instructions d'utilisation.** Remplacez les noms par des fonctions avant de coller les notes. Numérotez les entretiens. Utilisez le tableau obtenu pour dessiner la carte dans un outil de diagramme ou sur papier.

**G. Résultat attendu.** Un tableau d'étapes traçables jusqu'aux entretiens, des points de blocage, des contradictions, des questions complémentaires.

**H. Exemple d'application (illustratif).** À partir de six entretiens, l'assistant relève une contradiction utile : la coordinatrice affirme que le budget est vérifié « avant toute demande », tandis que l'assistante du bureau de terrain indique que « la vérification est faite après signature, quand on a le temps ». Le suivi d'une dépense réelle confirme la seconde version.

**I. Méthode de vérification.** Pour chaque étape, retrouvez l'entretien source ; suivez au moins une transaction réelle de bout en bout ; faites valider la carte par les acteurs en réunion.

**J. Précautions.** Les notes d'entretien contiennent souvent des jugements sur des collègues : supprimez-les ou neutralisez-les avant traitement. Classification orange au minimum (module 8).

**K. Amélioration.** Si le tableau mélange plusieurs variantes du processus (par exemple, achats inférieurs ou supérieurs à un seuil), demandez : « Sépare le processus en variantes selon [CRITÈRE] et produis un tableau par variante. »

## 5.8 Résultats attendus

Un rapport de diagnostic de 5 à 10 pages comprenant : carte « tel quel », arbre des causes, liste des tâches répétitives, faiblesses de contrôle interne, et recommandations classées en « organisationnelles », « outils simples » et « IA envisageable ».

## 5.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Les conclusions d'un diagnostic engagent des personnes et des services. Elles sont validées par la direction, présentées aux équipes concernées, et ne citent jamais de personne nommément comme cause d'un dysfonctionnement.

## 5.10 Risques et erreurs à éviter

- Cartographier la procédure écrite plutôt que la pratique réelle.
- S'arrêter au premier « pourquoi ».
- Présenter le diagnostic comme une évaluation individuelle.
- Recommander l'IA par principe, alors que la cause est organisationnelle.
- Négliger de mesurer la situation de départ (sans mesure initiale, pas de preuve d'amélioration).

## 5.11 Exercice pratique

**Consigne (90 minutes).** Choisissez un processus de votre organisation (paiement d'un fournisseur, remboursement d'un bénévole, inscription d'un bénéficiaire). (1) Délimitez-le. (2) Interrogez deux personnes qui l'exécutent. (3) Appliquez la fiche P5.1. (4) Dessinez la carte en couloirs. (5) Identifiez trois points de blocage et leur cause profonde avec les « 5 pourquoi ». (6) Classez chaque piste de solution en « organisationnelle », « outil simple » ou « IA envisageable ».

**Éléments de correction.** Une bonne réponse : délimite clairement début et fin ; distingue au moins trois acteurs ; signale au moins une différence entre procédure écrite et pratique ; aboutit à au moins une cause profonde organisationnelle ; propose au moins une solution sans IA.

## 5.12 Synthèse

- Un diagnostic combine entretiens, documents et observation.
- Il faut remonter des symptômes aux causes profondes (« 5 pourquoi », diagramme causes-effet).
- La cartographie « tel quel » en couloirs révèle les points de blocage réels.
- Les cinq composantes du COSO offrent une grille simple pour repérer les faiblesses de contrôle interne.
- Beaucoup de causes sont organisationnelles : elles se traitent avant ou à côté de l'IA.

## 5.13 QCM : Module 5

**Q1.** (une seule réponse) « Les rapports financiers arrivent en retard » est :

a) un symptôme.
b) une cause profonde.
c) une solution.
d) un indicateur de performance.

**Q2.** (une seule réponse) La carte « tel quel » doit décrire :

a) le processus prévu par le manuel de procédures.
b) le processus idéal.
c) le processus du principal bailleur.
d) le processus tel qu'il se déroule réellement.

**Q3.** (une ou plusieurs réponses) Quelles sources de preuves combine un bon diagnostic ?

a) Entretiens.
b) Documents.
c) Observation de transactions réelles.
d) Impressions générales de la direction, sans vérification.

**Q4.** (une seule réponse) Selon le COSO (2013), le contrôle interne comporte :

a) trois composantes et dix principes.
b) cinq composantes et dix-sept principes.
c) sept composantes et vingt principes.
d) une seule composante : l'audit.

**Q5.** (une ou plusieurs réponses) Quelles caractéristiques font d'une tâche un bon candidat à l'amélioration ?

a) Fréquente.
b) Standardisable.
c) Source d'erreurs de ressaisie.
d) Impliquant un jugement éthique complexe à chaque occurrence.

**Q6.** (une seule réponse) Dans l'exemple d'Horizons Partagés, la cause profonde principale des retards était :

a) l'absence d'IA.
b) la lenteur d'internet.
c) le nombre de bailleurs.
d) l'absence de délégation de signature formalisée.

**Q7.** (mise en situation, une seule réponse) Au bureau de terrain, la même personne commande, réceptionne et paie les fournitures. Quelle composante du contrôle interne est principalement concernée ?

a) Pilotage.
b) Information et communication.
c) Activités de contrôle (séparation des tâches).
d) Aucune.

**Q8.** (mise en situation, une seule réponse) Deux entretiens décrivent différemment la même étape. Que faites-vous ?

a) Retenir la version du responsable hiérarchique.
b) Suivre une transaction réelle pour établir les faits.
c) Retenir la version la plus récente.
d) Supprimer l'étape de la carte.

**Q9.** (une seule réponse) Pourquoi mesurer la situation de départ ?

a) Pour pouvoir démontrer l'effet des améliorations.
b) Pour sanctionner les retards.
c) Parce que le bailleur l'exige toujours.
d) Ce n'est pas nécessaire.

**Q10.** (une ou plusieurs réponses) Avant de soumettre des notes d'entretien à un assistant d'IA, il faut :

a) remplacer les noms par des fonctions.
b) neutraliser les jugements sur des collègues.
c) vérifier que l'outil est autorisé pour ce niveau de confidentialité.
d) ajouter les coordonnées des personnes interrogées.

## 5.14 Corrigé détaillé : Module 5

**Q1 : a.** C'est la manifestation visible ; les causes sont à rechercher en amont.

**Q2 : d.** La carte doit refléter la pratique réelle, souvent différente de la procédure écrite.

**Q3 : a, b, c.** Les impressions non vérifiées (d) ne constituent pas des preuves.

**Q4 : b.** Cinq composantes (environnement de contrôle, évaluation des risques, activités de contrôle, information et communication, pilotage) et dix-sept principes.

**Q5 : a, b, c.** Une tâche exigeant un jugement éthique complexe (d) est mal adaptée à l'automatisation.

**Q6 : d.** La cause était organisationnelle ; un logiciel seul ne l'aurait pas résolue.

**Q7 : c.** Le cumul de fonctions incompatibles est une faiblesse des activités de contrôle.

**Q8 : b.** Les faits priment : on vérifie par l'observation d'une transaction réelle.

**Q9 : a.** Sans mesure initiale, impossible de prouver un progrès.

**Q10 : a, b, c.** Ajouter les coordonnées (d) contredit le principe de minimisation des données.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Committee of Sponsoring Organizations of the Treadway Commission (COSO). (2013). *Internal Control : Integrated Framework*.


# Module 6 : Identifier les opportunités d'IA et choisir les bonnes priorités {#h8}

## 6.1 Mise en situation

À l'issue du diagnostic, l'équipe de direction d'Horizons Partagés dispose d'une liste de vingt-trois idées : un assistant pour répondre aux questions des agents sur les procédures, la rédaction automatique des procès-verbaux, l'extraction des données des factures, un tableau de bord budgétaire, la prévision de trésorerie, la traduction des supports, un tri automatique des candidatures, un chatbot pour les bénéficiaires… Chaque responsable défend la sienne. Le budget, lui, permet d'en lancer deux.

Comment choisir sans céder à l'idée la plus séduisante ou à la personne la plus convaincante ?

## 6.2 Problématique

Les organisations qui échouent avec l'IA ont souvent commencé par un projet trop ambitieux, mal défini, sur des données insuffisantes ou à risque élevé. À l'inverse, celles qui réussissent commencent par des cas d'usage précis, à valeur visible, réalisables avec leurs moyens, et dont les risques sont maîtrisables. Le choix des priorités est donc une décision décisive, et elle peut se faire avec méthode.

## 6.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. formuler un problème sous forme de cas d'usage précis et mesurable ;
2. définir les résultats attendus et les indicateurs associés ;
3. distinguer automatisation classique et IA ;
4. évaluer la faisabilité, les coûts, les bénéfices et les risques d'un cas d'usage ;
5. utiliser une matrice de sélection pondérée pour prioriser ;
6. rédiger une fiche d'opportunité.

## 6.4 Notions et définitions

- **Cas d'usage** : description d'une utilisation précise d'une technologie, pour un acteur donné, dans un processus donné, en vue d'un résultat mesurable. Exemple : « Le comptable dispose d'une proposition d'imputation pour chaque facture fournisseur reçue, afin de réduire le temps de saisie de 40 % sans augmenter le taux d'erreur. »
- **Résultat attendu** : changement concret visé (temps, qualité, délai, accessibilité, satisfaction).
- **Indicateur** : mesure qui permet de vérifier l'atteinte du résultat.
- **Faisabilité** : capacité réelle à mettre en œuvre le cas d'usage avec les données, compétences, outils et budget disponibles.
- **Coût total de possession** : ensemble des coûts sur la durée : acquisition, paramétrage, formation, abonnements, maintenance, temps de contrôle.
- **Gain rapide** : cas d'usage à forte valeur et à forte faisabilité, réalisable en quelques semaines.

## 6.5 Explications détaillées

### Étape 1 : Partir des problèmes, pas des outils

Chaque idée doit être reformulée en problème. « Un chatbot pour les bénéficiaires » n'est pas un problème. « Les bénéficiaires attendent en moyenne quatre jours une réponse à des questions simples sur les horaires et les documents à apporter » en est un. Cette reformulation fait souvent apparaître des solutions plus simples (une affiche, un message vocal enregistré, une FAQ imprimée).

**Gabarit de formulation :**

> Pour **[ACTEUR]**, dans le processus **[PROCESSUS]**, le problème est **[PROBLÈME OBSERVÉ, CHIFFRÉ SI POSSIBLE]**, ce qui entraîne **[CONSÉQUENCE]**. Nous voulons **[RÉSULTAT ATTENDU]**, mesuré par **[INDICATEUR]**.

### Étape 2 : Définir les résultats attendus

Un résultat attendu doit être **observable**. Évitez « améliorer l'efficacité ». Préférez « ramener le délai de production du procès-verbal de dix à trois jours » ou « réduire de moitié le nombre d'imputations corrigées lors de la revue mensuelle ». Notez la **valeur de départ** (issue du diagnostic) et la **valeur cible**.

### Étape 3 : Automatisation classique ou IA ?

![Figure 6.2 : Arbre de décision : faut-il de l'IA, une automatisation classique ou rien ?](03_ILLUSTRATIONS/figures/fig_6_2.svg){#fig-6-2}

| Critère | Automatisation classique | IA |
|---|---|---|
| Nature de la tâche | Règles stables et explicites | Langage, images, cas variables, jugement approximatif |
| Exemple | Envoyer un rappel 7 jours avant l'échéance d'un rapport | Résumer un rapport ; extraire les données d'une facture photographiée |
| Prévisibilité | Totale : même entrée, même sortie | Partielle : erreurs possibles, à contrôler |
| Explicabilité | Élevée | Variable, souvent faible |
| Coût de contrôle | Faible après test | Permanent (vérification humaine) |

Table: Tableau 6.1 : Explications détaillées

**Règle d'or :** si une règle simple, une formule de tableur ou un modèle de document suffit, ce sont eux qu'il faut utiliser. L'IA se justifie quand la variabilité des entrées rend les règles impossibles à écrire.

### Étape 4 : Évaluer la faisabilité

Cinq questions :

1. **Données** : les données nécessaires existent-elles, sont-elles accessibles, de qualité suffisante et utilisables légalement ?
2. **Compétences** : qui mettra en place, qui utilisera, qui maintiendra ?
3. **Outils** : une solution existe-t-elle au niveau de maturité de l'organisation (débutant, intermédiaire, avancé) ?
4. **Intégration** : la solution s'insère-t-elle dans le processus existant sans créer de double saisie ?
5. **Acceptabilité** : les utilisateurs et les personnes concernées accepteront-ils la solution ?

### Étape 5 : Estimer coûts et bénéfices

Estimez les coûts sur **trois ans**, pas seulement l'année de lancement.

*Exemple (fictif) : extraction assistée des factures à Horizons Partagés :*

| Poste | Année 1 | Année 2 | Année 3 |
|---|---|---|---|
| Abonnement outil d'extraction | 1 800 UM | 1 800 UM | 1 800 UM |
| Paramétrage et intégration (prestataire) | 2 500 UM | Néant | Néant |
| Formation (temps interne valorisé) | 600 UM | 200 UM | 200 UM |
| Temps de contrôle humain | 1 200 UM | 1 200 UM | 1 200 UM |
| **Total des coûts** | **6 100 UM** | **3 200 UM** | **3 200 UM** |

Table: Tableau 6.2 : Explications détaillées

Bénéfices estimés : la comptable traite environ 350 factures par mois ; la saisie manuelle prend en moyenne 6 minutes par facture, soit 35 heures par mois. Si l'outil ramène ce temps à 2,5 minutes (contrôle compris), le gain est d'environ 20 heures par mois, soit 240 heures par an. Valorisées à 15 UM de l'heure (coût complet fictif), cela représente 3 600 UM par an : à comparer aux 3 200 UM de coûts récurrents.

Conclusion : le gain financier direct est modeste. Le cas d'usage se justifie surtout par des **bénéfices qualitatifs** (réduction des erreurs, pièces retrouvables, clôture plus rapide, réduction de la dépendance à une personne) qui doivent être explicités et mesurés. Ce type d'analyse honnête évite les désillusions.

> **🔎 À retenir** : Le temps « gagné » n'est un bénéfice que s'il est réaffecté à quelque chose d'utile. Précisez à quoi il servira.

### Étape 6 : Évaluer les risques

Pour chaque cas d'usage, évaluez : la sensibilité des données (vert, orange, rouge ; voir le module 8) ; l'impact d'une erreur sur des personnes ou sur l'organisation ; le risque de biais ; la dépendance au fournisseur ; le risque d'image. Un cas d'usage qui implique des décisions sur des personnes vulnérables avec des données sensibles n'est jamais un « gain rapide ».

### Étape 7 : Prioriser avec la matrice de sélection

![Figure 6.1 : Matrice de priorisation valeur × faisabilité](03_ILLUSTRATIONS/figures/fig_6_1.svg){#fig-6-1}

La matrice de sélection (annexe 3) note chaque cas d'usage sur des critères pondérés :

| Critère | Poids | Échelle (1 à 5) |
|---|---|---|
| Contribution à la mission | 25 % | 1 = indirecte et faible · 5 = directe et forte |
| Gain de temps ou de qualité | 20 % | 1 = négligeable · 5 = majeur |
| Disponibilité et qualité des données | 15 % | 1 = inexistantes · 5 = prêtes |
| Faisabilité technique et compétences | 15 % | 1 = hors de portée · 5 = immédiate |
| Coût sur 3 ans (inversé) | 10 % | 1 = très élevé · 5 = très faible |
| Niveau de risque (inversé) | 15 % | 1 = risque élevé sur des personnes · 5 = risque faible |

Table: Tableau 6.3 : Explications détaillées

*Application (fictive) à huit cas d'usage d'Horizons Partagés :*

| Cas d'usage | Mission | Gain | Données | Faisab. | Coût | Risque | **Score /5** |
|---|---|---|---|---|---|---|---|
| 1. Projet de PV et suivi des décisions | 3 | 4 | 5 | 5 | 5 | 4 | **4,15** |
| 2. Synthèse des rapports de terrain | 4 | 4 | 4 | 4 | 5 | 4 | **4,10** |
| 3. Extraction des données de factures | 3 | 4 | 4 | 4 | 3 | 4 | **3,65** |
| 4. Assistant procédures (RAG) | 4 | 4 | 2 | 2 | 2 | 3 | **3,05** |
| 5. Prévision de trésorerie | 3 | 3 | 2 | 2 | 3 | 4 | **2,85** |
| 6. Déclinaison de publications pour les réseaux | 2 | 3 | 5 | 5 | 5 | 4 | **3,70** |
| 7. Tri automatique des candidatures | 2 | 3 | 3 | 3 | 3 | 1 | **2,45** |
| 8. Traduction des supports | 4 | 3 | 4 | 4 | 4 | 3 | **3,65** |

Table: Tableau 6.4 : Explications détaillées

*Détail du calcul pour le cas 1 :* 3 × 0,25 + 4 × 0,20 + 5 × 0,15 + 5 × 0,15 + 5 × 0,10 + 4 × 0,15 = 0,75 + 0,80 + 0,75 + 0,75 + 0,50 + 0,60 = **4,15**.

> **🔎 À retenir** : Faites toujours les calculs d'une matrice dans un tableur (formule `SOMMEPROD` entre la ligne des notes et la ligne des poids). Lors de la préparation de cet exemple, un premier calcul « de tête » comportait deux erreurs d'arrondi : c'est précisément le type d'erreur que le tableur évite.

**Lecture :** les cas 1 et 2 sont des gains rapides. Le cas 6 arrive en troisième position, mais avec une faible contribution à la mission : il peut être mené en parallèle à faible coût. Le cas 4 (assistant RAG) a une forte valeur mais une faible faisabilité : c'est un **projet structurant**, à préparer en commençant par la gestion documentaire. Le cas 7 est écarté en raison de son niveau de risque (décisions sur des personnes, risque de discrimination).

> **🔎 À retenir** : La matrice éclaire la décision ; elle ne la remplace pas. Un cas d'usage peut être retenu malgré un score moyen pour une raison stratégique explicite, ou écarté malgré un bon score pour une raison éthique. Consignez ces raisons.

## 6.6 Application professionnelle : sélectionner deux projets pilotes

**Processus de mise en œuvre :**

1. Recenser les idées (diagnostic, journal des tâches, suggestions des équipes).
2. Reformuler chaque idée avec le gabarit « problème → résultat → indicateur ».
3. Éliminer les idées qui relèvent d'une solution organisationnelle ou d'une automatisation classique (elles sont traitées à part, souvent plus vite).
4. Rédiger une fiche d'opportunité pour chaque cas d'usage restant (fiche P6.1, annexe 4).
5. Noter les cas d'usage dans la matrice, en atelier, avec trois à cinq personnes de fonctions différentes.
6. Débattre des résultats et retenir deux pilotes : idéalement un gain rapide et la préparation d'un projet structurant.
7. Présenter la sélection à la direction, puis au conseil si nécessaire.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Matrice papier ou tableur ; fiches d'opportunité rédigées avec un assistant | Tableur, assistant | Temps | Notation subjective : la faire en groupe |
| Intermédiaire | Formulaire de collecte des idées ; matrice partagée ; vote pondéré en atelier | Formulaire, tableur partagé | Faibles | Exige un animateur |
| Avancé | Portefeuille de projets numériques géré dans un outil de gestion de projets, avec revue trimestrielle et indicateurs de valeur | Outil de gestion de portefeuille | Licences | Lourd pour une petite structure |

Table: Tableau 6.5 : Application professionnelle : sélectionner deux projets pilotes

## 6.7 Prompt prêt à l'emploi

### Fiche P6.1 : Rédiger une fiche d'opportunité

**A. Titre.** Fiche d'opportunité d'un cas d'usage d'IA.

**B. Objectif.** Transformer une idée en cas d'usage structuré, évaluable et comparable.

**C. Contexte d'utilisation.** Atelier de priorisation ; préparation d'un comité de direction.

**D. Données nécessaires.** Idée initiale ; constats du diagnostic (chiffres) ; processus concerné ; type de données ; moyens disponibles.

**E. Prompt complet.**

```text
Contexte : [NOM DE L'ASBL], [SECTEUR], [TAILLE]. Niveau de maturité
numérique : [débutant / intermédiaire / avancé]. Budget indicatif :
[MONTANT OU « très limité »].
Idée : [IDÉE]. Constats du diagnostic : [CONSTATS CHIFFRÉS].
Processus concerné : [PROCESSUS]. Données impliquées : [TYPES, sans
données réelles].
Tâche : rédige une fiche d'opportunité.
Résultat attendu (rubriques) :
1. Problème reformulé (gabarit : pour [acteur], dans [processus], le
   problème est…, ce qui entraîne… ).
2. Résultat attendu et 2 à 3 indicateurs avec valeur de départ
   (si connue) et cible proposée.
3. Solution sans IA possible (règle, modèle, réorganisation).
4. Solution avec IA : principe, niveau (débutant/intermédiaire/
   avancé), rôle de l'IA, rôle du logiciel, rôle humain.
5. Données nécessaires et classification probable (public, interne,
   confidentiel).
6. Risques principaux et contrôles humains indispensables.
7. Postes de coûts à estimer sur 3 ans (sans inventer de prix).
8. Questions à trancher avant décision.
Limites : n'invente ni prix ni fonctionnalités de produits nommés.
Indique « à estimer » lorsqu'une donnée chiffrée manque.
```

**F. Instructions d'utilisation.** Une fiche par idée. Complétez ensuite vous-même les coûts à partir de devis ou de pages tarifaires officielles.

**G. Résultat attendu.** Une fiche de une à deux pages, homogène avec les autres fiches, prête à être notée.

**H. Exemple d'application (illustratif).** Pour l'idée « chatbot pour les bénéficiaires », la fiche obtenue propose comme solution sans IA « un message vocal et une affiche listant les cinq questions les plus fréquentes », et relève comme risque principal « des réponses erronées sur l'éligibilité à des services de santé ». Le comité décide de commencer par la solution sans IA et de mesurer la baisse des appels.

**I. Méthode de vérification.** Vérifiez que les chiffres repris viennent du diagnostic ; que la solution sans IA a été sérieusement envisagée ; que les contrôles humains couvrent les décisions sensibles ; qu'aucun prix n'a été inventé.

**J. Précautions.** Ne pas soumettre de données réelles ; décrire les types de données.

**K. Amélioration.** Si la fiche est trop optimiste : « Joue le rôle d'un administrateur sceptique et liste les cinq meilleures objections à ce projet, puis propose une réponse à chacune. »

## 6.8 Résultats attendus

Une liste de cas d'usage reformulés, une fiche d'opportunité par cas, une matrice notée et commentée, une décision motivée sur deux projets pilotes.

## 6.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : La sélection des projets est une décision de direction, documentée, qui tient compte de considérations stratégiques et éthiques que la matrice ne capture pas entièrement. Les cas d'usage touchant des décisions sur des personnes sont soumis à un examen éthique préalable (module 8).

## 6.10 Risques et erreurs à éviter

- Choisir le projet le plus spectaculaire plutôt que le plus utile.
- Sous-estimer le temps de contrôle humain dans les coûts.
- Confondre gain de temps théorique et bénéfice réel.
- Laisser une seule personne noter la matrice.
- Négliger la solution sans IA.

## 6.11 Exercice pratique

**Consigne (90 minutes).** À partir de l'exercice du module 5 : (1) formulez trois cas d'usage avec le gabarit ; (2) rédigez la fiche P6.1 pour chacun ; (3) notez-les dans la matrice pondérée (dans un tableur) ; (4) expliquez en cinq lignes votre choix final, y compris une raison non capturée par la matrice.

**Éléments de correction.** Les cas d'usage sont précis et mesurables ; une solution sans IA est envisagée pour chacun ; les calculs de la matrice sont faits dans un tableur et vérifiables ; le choix final est argumenté et assume ses éventuels écarts avec le classement.

## 6.12 Synthèse

- Partir des problèmes, formuler des cas d'usage mesurables.
- Préférer l'automatisation classique quand des règles stables suffisent.
- Évaluer faisabilité, coûts sur trois ans, bénéfices réels et risques.
- Prioriser avec une matrice pondérée, notée en groupe, calculée dans un tableur.
- Commencer par un gain rapide et préparer un projet structurant.

## 6.13 QCM : Module 6

**Q1.** (une seule réponse) Lequel est un cas d'usage bien formulé ?

a) « Mettre de l'IA dans la comptabilité. »
b) « Le comptable dispose d'une proposition d'imputation pour chaque facture, afin de réduire de 40 % le temps de saisie sans augmenter le taux d'erreur. »
c) « Acheter un chatbot. »
d) « Être plus moderne. »

**Q2.** (une seule réponse) Envoyer un rappel automatique sept jours avant l'échéance d'un rapport relève plutôt :

a) de l'automatisation classique.
b) de l'IA générative.
c) de l'IA prédictive.
d) d'un agent IA.

**Q3.** (une ou plusieurs réponses) Quels postes appartiennent au coût total de possession ?

a) Les abonnements.
b) La formation.
c) Le temps de contrôle humain.
d) La maintenance.

**Q4.** (une seule réponse) Dans la matrice, un cas d'usage à forte valeur mais à faible faisabilité est :

a) un gain rapide.
b) à écarter systématiquement.
c) un projet structurant à préparer.
d) une petite amélioration.

**Q5.** (une seule réponse) Avec les poids du module (25/20/15/15/10/15 %), un cas noté 4, 4, 4, 4, 4, 4 obtient :

a) 3,5
b) 4,0
c) 4,5
d) 24

**Q6.** (une ou plusieurs réponses) Pourquoi le tri automatique des candidatures a-t-il été écarté dans l'exemple ?

a) Il implique des décisions sur des personnes.
b) Il présente un risque de discrimination.
c) Il est techniquement impossible.
d) Son score de risque était très défavorable.

**Q7.** (mise en situation, une seule réponse) Le calcul d'un projet montre un gain financier direct faible, mais une forte réduction des erreurs et des pièces perdues. Que faites-vous ?

a) Abandonner le projet.
b) Gonfler les gains de temps pour justifier le projet.
c) Lancer le projet sans analyse.
d) Expliciter et mesurer les bénéfices qualitatifs dans la décision.

**Q8.** (mise en situation, une seule réponse) Une responsable propose « un chatbot pour les bénéficiaires ». Première étape ?

a) Choisir un fournisseur.
b) Lancer un appel d'offres.
c) Reformuler le besoin en problème mesurable et envisager des solutions sans IA.
d) Rédiger les réponses du chatbot.

**Q9.** (une seule réponse) Le temps gagné grâce à une solution est un bénéfice réel lorsque :

a) il est calculé par le fournisseur.
b) il est réaffecté à une activité utile, identifiée.
c) il dépasse dix heures par mois.
d) il est mentionné dans le rapport annuel.

**Q10.** (une ou plusieurs réponses) Une bonne pratique de notation de la matrice consiste à :

a) noter en groupe, avec des fonctions différentes.
b) calculer les scores dans un tableur.
c) consigner les raisons d'un choix qui s'écarte du classement.
d) laisser l'outil d'IA décider seul.

## 6.14 Corrigé détaillé : Module 6

**Q1 : b.** Il précise l'acteur, le processus, le résultat et l'indicateur.

**Q2 : a.** C'est une règle stable : un rappel programmé suffit.

**Q3 : a, b, c, d.** Tous ces postes doivent être estimés sur la durée.

**Q4 : c.** Il faut préparer ses conditions (données, compétences) avant de le lancer.

**Q5 : b.** 4 × (0,25 + 0,20 + 0,15 + 0,15 + 0,10 + 0,15) = 4 × 1 = 4,0.

**Q6 : a, b, d.** Il n'est pas techniquement impossible (c) ; il est écarté pour des raisons de risque et d'éthique.

**Q7 : d.** Les bénéfices qualitatifs sont réels mais doivent être explicités et mesurés. Gonfler les gains (b) serait malhonnête.

**Q8 : c.** On part toujours du problème ; une solution simple peut suffire.

**Q9 : b.** Le temps gagné n'a de valeur que s'il est réinvesti.

**Q10 : a, b, c.** La décision reste humaine (d est faux). L'exemple du module montre d'ailleurs qu'une erreur de calcul manuel est vite arrivée.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.


# Partie III : Préparer et sécuriser l'adoption de l'IA {#h9 .partie}

*Vous avez identifié vos priorités. Avant d'agir, trois conditions doivent être réunies : des données organisées et fiables, des règles éthiques et de sécurité claires, et des outils adaptés à vos moyens. Cette partie pose ces fondations, sans lesquelles l'IA amplifie les problèmes au lieu de les résoudre.*

# Module 7 : Les données, le carburant des systèmes intelligents {#h10}

## 7.1 Mise en situation

Lumière des Collines suit 120 élèves. Pour préparer le rapport annuel, Amina, la coordinatrice, ouvre le fichier de suivi… puis le deuxième, puis le troisième. Car il existe trois fichiers : celui de l'ancienne coordinatrice, celui d'un bénévole qui l'a « amélioré », et une copie sur une clé USB. Le même élève apparaît sous trois orthographes différentes ; certaines dates sont au format jour/mois, d'autres mois/jour ; la colonne « classe » mélange « CM1 », « cm 1 » et « 4e année ».

Amina demande à un assistant d'IA de « calculer le taux de réussite ». L'outil produit un chiffre précis au dixième près. Il est faux, mais rien ne permet de le voir.

## 7.2 Problématique

Un système d'IA ne vaut que par ses données. Des données dispersées, incohérentes, incomplètes ou mal protégées produisent des résultats erronés, d'autant plus dangereux qu'ils sont présentés de façon convaincante. Dans beaucoup d'ASBL, la gestion des données et des documents est le véritable chantier prioritaire, avant tout projet d'IA.

## 7.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. distinguer données structurées et non structurées et comprendre leur usage par l'IA ;
2. évaluer la qualité d'un jeu de données selon six dimensions ;
3. mettre en place un plan de classement et une règle de nommage ;
4. organiser une numérisation utile ;
5. comprendre les notions de base de données, d'interopérabilité, de sauvegarde et de gestion des accès ;
6. préserver la mémoire institutionnelle ;
7. nettoyer un fichier avec l'aide d'un assistant, sans exposer de données personnelles.

## 7.4 Notions et définitions

- **Donnée structurée** : information organisée selon un format fixe (lignes et colonnes d'un tableur, champs d'une base de données).
- **Donnée non structurée** : information sans format fixe (courriels, PDF, photos, enregistrements audio, notes manuscrites). Elle représente l'essentiel de l'information d'une ASBL.
- **Métadonnées** : informations qui décrivent un document ou une donnée (auteur, date, projet, version, confidentialité).
- **Référentiel** : liste de valeurs de référence partagée (liste des projets, des codes budgétaires, des villages, des fournisseurs).
- **Identifiant unique** : code qui désigne sans ambiguïté une entité (un élève, un fournisseur) et ne change pas.
- **Interopérabilité** : capacité de deux systèmes à échanger et utiliser des données sans ressaisie.
- **Sauvegarde** : copie de sécurité permettant de restaurer les données en cas de perte.

## 7.5 Explications détaillées

### Données structurées et non structurées

| | Structurées | Non structurées |
|---|---|---|
| Exemples | Grand livre, liste des bénéficiaires, suivi des activités | Rapports, PV, conventions, courriels, photos de factures, enregistrements |
| Outils classiques | Tableur, base de données, logiciel comptable | Traitement de texte, messagerie, dossiers partagés |
| Apport de l'IA | Détection d'anomalies, prévisions, aide aux formules | Extraction d'informations, synthèse, classification, recherche par le sens (RAG) |
| Risque principal | Erreurs de saisie, doublons, incohérences | Versions multiples, documents introuvables, données sensibles cachées dans le texte |

Table: Tableau 7.1 : Explications détaillées

L'IA a profondément changé le traitement des données non structurées : elle peut transformer une photo de facture en ligne de tableau, ou retrouver la bonne clause dans cinquante conventions. Mais elle ne peut retrouver que ce qui a été conservé, et elle ne distingue pas spontanément la version validée d'un brouillon.

### Les six dimensions de la qualité des données

| Dimension | Question | Exemple de défaut | Contrôle simple |
|---|---|---|---|
| **Exactitude** | La donnée est-elle juste ? | Montant mal recopié | Comparaison avec la pièce sur un échantillon |
| **Complétude** | Les données nécessaires sont-elles présentes ? | Code projet manquant | Comptage des cellules vides |
| **Cohérence** | Les données concordent-elles entre elles ? | Date de fin antérieure à la date de début | Règles de validation |
| **Unicité** | Chaque entité n'apparaît-elle qu'une fois ? | Un fournisseur enregistré trois fois | Recherche de doublons |
| **Actualité** | La donnée est-elle à jour ? | Adresse d'un partenaire ancienne | Date de dernière mise à jour |
| **Validité** | La donnée respecte-t-elle le format attendu ? | « 31/02/2026 » | Listes déroulantes, formats imposés |

Table: Tableau 7.2 : Explications détaillées

> **🔎 À retenir** : Il est beaucoup plus économique d'empêcher les erreurs à la saisie (listes déroulantes, champs obligatoires, formats imposés) que de les corriger ensuite.

### Organiser les documents : plan de classement et règle de nommage

![Figure 7.2 : Exemple d'arborescence documentaire et de règle de nommage](03_ILLUSTRATIONS/figures/fig_7_2.svg){#fig-7-2}

Un **plan de classement** est une arborescence de dossiers partagée par tous, stable dans le temps, et calquée sur les fonctions de l'organisation plutôt que sur les personnes. Règles pratiques :

1. **Cinq à huit dossiers racines** au maximum, numérotés pour fixer l'ordre.
2. **Pas de dossiers personnels** pour les documents de l'organisation (« Dossier de Marie » disparaît avec le départ de Marie).
3. **Un dossier par projet** avec la même sous-structure pour tous les projets.
4. **Une règle de nommage** unique, par exemple `AAAA-MM-JJ_TYPE_OBJET_vN` : la date en premier permet le tri chronologique, le type (FACT, PV, CONV, RAPP) permet le filtrage, la version évite les « final_final2 ».
5. **Un statut clair** pour les versions définitives (suffixe `VALIDE` ou dossier dédié).
6. **Le même plan** pour le numérique et le papier.

### Numériser utilement

Numériser n'est pas photographier en vrac. Une numérisation utile suppose :

- **de choisir ce qui doit l'être** : pièces justificatives, conventions, PV, contrats, en priorité les documents exigés par les audits et les bailleurs ;
- **une qualité suffisante** : document à plat, bien éclairé, lisible en entier, format PDF de préférence ;
- **un nommage et un classement immédiats**, selon la règle ;
- **la conservation des originaux** lorsque la loi ou le bailleur l'exige.

> **⚖️ Adaptation réglementaire** : La valeur probante d'une copie numérique et les durées de conservation des pièces comptables et des documents sociaux varient selon les pays. Avant de détruire un original papier, vérifiez la législation applicable et les conditions de vos conventions de financement.

> **📶 Faible connectivité** : Les applications de numérisation sur smartphone fonctionnent généralement hors ligne ; les fichiers peuvent être synchronisés plus tard, lors d'une connexion. Fixez une routine (par exemple chaque vendredi) et vérifiez que la synchronisation s'est bien terminée.

### Bases de données et référentiels

Au-delà de quelques centaines de lignes ou de plusieurs utilisateurs simultanés, le tableur atteint ses limites : versions concurrentes, formules écrasées, absence de traçabilité. Une **base de données** (même simple, via un outil sans code) offre des champs typés, des listes de valeurs, des droits d'accès, un historique des modifications et des relations entre tables (un bénéficiaire → plusieurs services reçus).

Quelle que soit la solution, quelques **référentiels** doivent être uniques et partagés : projets et codes budgétaires, plan comptable, localités, fournisseurs, partenaires. Chaque entité reçoit un **identifiant unique non signifiant** (par exemple `BEN-000317` plutôt que les initiales et la date de naissance, qui révèlent des informations personnelles).

### Interopérabilité

Chaque ressaisie est une source d'erreurs et de perte de temps. L'interopérabilité vise à faire circuler les données entre outils : un formulaire de terrain qui alimente directement la base de suivi ; le logiciel comptable qui exporte vers le tableau de bord. Trois niveaux existent :

1. **l'export/import manuel** de fichiers (CSV, tableur) avec un format fixe ;
2. **les connecteurs** proposés par les logiciels ou par les plateformes d'automatisation sans code ;
3. **les API**, interfaces de programmation, pour des échanges automatiques et sécurisés (niveau Avancé).

Avant d'acheter un outil, vérifiez qu'il permet d'**exporter toutes vos données** dans un format ouvert : c'est votre garantie contre la dépendance au fournisseur.

### Sauvegarde

Une règle simple et largement recommandée est celle du **3-2-1** : au moins **trois** copies des données, sur **deux** supports différents, dont **une** hors du bureau (par exemple dans le cloud ou dans un autre lieu). Une sauvegarde n'existe vraiment que si l'on a **testé la restauration**. Planifiez un test semestriel : restaurer un dossier et vérifier qu'il s'ouvre.

### Gestion des accès

Le principe du **moindre privilège** : chacun accède aux données nécessaires à sa fonction, et à elles seules. Concrètement : dossiers RH et données de santé en accès restreint ; comptes nominatifs (pas de mot de passe partagé) ; double authentification activée ; retrait des accès le jour du départ d'un collaborateur ou d'un bénévole ; revue des droits au moins une fois par an. Ce principe est d'autant plus important que les assistants connectés aux fichiers de l'organisation voient tout ce que l'utilisateur peut voir.

### Mémoire institutionnelle

Les ASBL connaissent un renouvellement important de personnel et de bénévoles. Chaque départ emporte des connaissances : pourquoi tel fournisseur a été écarté, comment remplir tel rapport, quels engagements ont été pris oralement avec un partenaire. Préserver la mémoire institutionnelle suppose de :

- documenter les procédures au fil de l'eau (et non en urgence au moment du départ) ;
- consigner les décisions et leurs motifs (registre des décisions, module 10) ;
- organiser des entretiens de passation, transcrits et synthétisés ;
- centraliser les documents dans le plan de classement.

L'IA peut aider à **rédiger** des procédures à partir d'entretiens, à **synthétiser** des historiques de dossiers, et, à terme, à **interroger** cette mémoire via un assistant documentaire (RAG). Mais elle ne peut restituer que ce qui a été consigné.

![Figure 7.1 : Le cycle de vie des données](03_ILLUSTRATIONS/figures/fig_7_1.svg){#fig-7-1}

## 7.6 Application professionnelle : remettre en ordre le suivi des élèves de Lumière des Collines

**A. Contexte.** Petite association, un ordinateur partagé, smartphones, connexion intermittente.
**B. Problème.** Trois fichiers de suivi divergents ; indicateurs du rapport annuel non fiables.
**C. Symptômes.** Doublons, orthographes multiples, formats de date hétérogènes, cellules vides.
**D. Causes profondes.** Absence de fichier de référence unique ; absence de règles de saisie ; pas d'identifiant unique ; pas de responsable désigné.
**E. Processus actuel.** Chaque bénévole saisit où il veut, comme il veut.
**F. Faiblesses.** Pas de traçabilité ; données personnelles d'enfants sur une clé USB non chiffrée.
**G. Résultat recherché.** Un fichier unique, propre, protégé, avec des indicateurs fiables.
**H. Pertinence de l'IA.** Utile pour proposer des règles de nettoyage et des formules, et pour repérer des incohérences, sur une version pseudonymisée.
**I. Alternatives sans IA.** Nettoyage manuel avec les fonctions du tableur (tri, filtres, suppression des doublons).
**J. Solution.** Fusion contrôlée des trois fichiers dans un modèle unique avec listes déroulantes, identifiants uniques et accès restreint.
**K. Niveau.** Débutant.
**L. Outils.** Tableur, espace de stockage partagé avec accès restreint, assistant conversationnel (sur données pseudonymisées).
**M. Étapes.**

1. Désigner une responsable du fichier (Amina).
2. Copier les trois fichiers dans un dossier de travail sécurisé ; ne jamais modifier les originaux avant la fin.
3. Créer une **table de correspondance** séparée (nom réel ↔ code `ELV-001`…), stockée à part avec accès restreint.
4. Produire une version **pseudonymisée** des trois fichiers (codes au lieu des noms, suppression des informations non nécessaires comme l'adresse).
5. Utiliser la fiche P7.1 pour obtenir des règles de nettoyage et des formules.
6. Appliquer les règles dans le tableur ; marquer chaque correction dans une colonne « observations ».
7. Traiter manuellement les cas ambigus (deux élèves de même nom ?) avec la table de correspondance.
8. Construire le modèle définitif : listes déroulantes (classes, mois), format de date imposé, champs obligatoires.
9. Supprimer les copies obsolètes, dont la clé USB, après vérification.
10. Documenter les règles de saisie sur une page, affichée près de l'ordinateur.

**N. Prompt.** Fiche P7.1.
**O. Exemple de résultat.** Un fichier de 120 lignes uniques, 6 colonnes normalisées, 0 date invalide ; une page de règles de saisie.
**P. Vérification.** Contrôle de 10 lignes tirées au hasard contre les registres papier de présence.
**Q. Contrôles humains.** Arbitrage des doublons ambigus ; validation du fichier final par la coordinatrice.
**R. Risques.** Exposer des données d'enfants ; fusionner à tort deux élèves distincts ; perdre des données en supprimant trop tôt les originaux.
**S. Coûts et maintenance.** Environ une journée de travail ; 15 minutes par semaine de contrôle.
**T. Indicateurs.** Nombre de doublons ; taux de complétude ; nombre d'erreurs détectées lors du contrôle par échantillon.
**U. Amélioration continue.** Contrôle trimestriel de qualité ; migration vers une base de données simple si le nombre d'utilisateurs augmente.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Tableur modèle avec validations ; plan de classement ; sauvegarde 3-2-1 manuelle | Tableur, stockage partagé, disque externe | Faibles | Discipline humaine nécessaire |
| Intermédiaire | Base de données sans code avec formulaires de saisie ; gestion documentaire avec métadonnées ; sauvegardes automatiques | Outil de base de données sans code, gestion électronique de documents | Abonnements | Paramétrage initial |
| Avancé | Entrepôt de données alimenté par API depuis les applications métier ; référentiels centralisés ; gestion fine des accès ; catalogue de données | ERP, base de données, outil d'intégration | Élevés | Compétences spécialisées, gouvernance des données |

Table: Tableau 7.3 : Application professionnelle : remettre en ordre le suivi des élèves de Lumière des Collines

## 7.7 Prompt prêt à l'emploi

### Fiche P7.1 : Nettoyer un fichier de suivi pseudonymisé

**A. Titre.** Règles de nettoyage et de normalisation d'un fichier.

**B. Objectif.** Obtenir des règles de nettoyage, des formules et une liste de contrôles, appliquées ensuite par vous dans le tableur.

**C. Contexte d'utilisation.** Avant un rapport, une migration ou un projet d'IA ; tout métier.

**D. Données nécessaires.** Description des colonnes ; extrait de 15 à 20 lignes **pseudonymisées** représentatives des problèmes.

**E. Prompt complet.**

```text
Contexte : je dois fusionner et nettoyer des fichiers de suivi de
[OBJET]. Les données ci-dessous sont pseudonymisées (codes à la place
des noms). Mon tableur : [LOGICIEL ET LANGUE].
Colonnes : [LISTE ET SIGNIFICATION].
Extrait : <extrait>[15 À 20 LIGNES]</extrait>
Tâche :
1. Liste les problèmes de qualité observés, classés selon : exactitude,
   complétude, cohérence, unicité, actualité, validité.
2. Pour chaque problème, propose une règle de correction et, si
   possible, une formule ou une fonction du tableur.
3. Propose un format cible pour chaque colonne (type, valeurs
   autorisées, format de date).
4. Liste les cas qui exigent un arbitrage humain (ne les corrige pas).
5. Propose 5 règles de saisie simples pour éviter que les problèmes
   reviennent.
Limites : ne corrige pas toi-même les données de l'extrait ; ne
suppose pas que deux lignes similaires désignent la même personne.
```

**F. Instructions d'utilisation.** Pseudonymisez d'abord (étape 4 ci-dessus). Choisissez des lignes qui montrent la diversité des problèmes. Appliquez les règles sur une copie.

**G. Résultat attendu.** Un tableau « problème → règle → formule », un format cible, une liste de cas à arbitrer, cinq règles de saisie.

**H. Exemple d'application (illustratif).** Pour Lumière des Collines, l'assistant propose notamment : normaliser les classes avec une table de correspondance (« cm 1 », « CM1 », « 4e année » → « CM1 ») et une recherche (`RECHERCHEV`) ; signaler comme ambiguës deux lignes au même code mais aux classes différentes ; imposer le format de date AAAA-MM-JJ.

**I. Méthode de vérification.** Comptez les lignes avant et après chaque opération ; vérifiez un échantillon de corrections ; contrôlez qu'aucune fusion n'a été faite sans arbitrage humain.

**J. Précautions.** Jamais de noms, dates de naissance complètes, adresses, numéros de téléphone ou informations de santé dans l'outil. Les données d'enfants appellent une vigilance renforcée.

**K. Amélioration.** Si les formules sont trop complexes : « Propose une solution en plusieurs colonnes intermédiaires simples, compréhensibles par un bénévole. »

## 7.8 Résultats attendus

Un plan de classement et une règle de nommage adoptés ; des fichiers de référence propres et protégés ; une sauvegarde testée ; des droits d'accès revus ; des procédures documentées.

## 7.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : La fusion d'enregistrements concernant des personnes (doublons supposés), la suppression de données et la destruction d'originaux sont décidées par une personne responsable, après vérification. Une fusion erronée peut priver quelqu'un d'un service ou fausser un dossier.

## 7.10 Risques et erreurs à éviter

- Lancer un projet d'IA sur des données non nettoyées.
- Utiliser des identifiants signifiants (initiales, dates de naissance).
- Confondre pseudonymisation et anonymisation (les données pseudonymisées restent personnelles).
- Ne jamais tester la restauration des sauvegardes.
- Laisser des accès actifs après le départ de collaborateurs ou de bénévoles.
- Choisir un outil qui ne permet pas d'exporter ses données.

## 7.11 Exercice pratique

**Consigne (2 heures).** (1) Proposez un plan de classement de cinq à huit dossiers racines pour votre organisation et une règle de nommage. (2) Choisissez un fichier de suivi ; évaluez sa qualité selon les six dimensions (note de 1 à 5 chacune). (3) Appliquez la fiche P7.1 sur une version pseudonymisée. (4) Rédigez cinq règles de saisie. (5) Décrivez votre dispositif de sauvegarde actuel et comparez-le au principe 3-2-1.

**Éléments de correction.** Le plan est fondé sur les fonctions, sans dossiers personnels ; la règle de nommage commence par la date ; l'évaluation de qualité s'appuie sur des comptages ; la pseudonymisation est effective ; les règles de saisie sont simples et vérifiables ; l'écart au principe 3-2-1 conduit à une action concrète.

## 7.12 Synthèse

- Les données non structurées sont majoritaires ; l'IA aide à les exploiter, à condition qu'elles soient organisées.
- La qualité des données se mesure selon six dimensions et se construit à la saisie.
- Plan de classement, règle de nommage et identifiants uniques sont des préalables.
- Interopérabilité, sauvegarde 3-2-1 testée et moindre privilège protègent l'organisation.
- La mémoire institutionnelle se construit au quotidien ; l'IA aide à la formaliser et à l'interroger.

## 7.13 QCM : Module 7

**Q1.** (une seule réponse) Un courriel contenant une demande de partenariat est une donnée :

a) structurée.
b) de référence.
c) non structurée.
d) chiffrée.

**Q2.** (une seule réponse) « Un fournisseur enregistré trois fois sous des noms légèrement différents » relève d'un défaut de :

a) actualité.
b) unicité.
c) validité.
d) exactitude uniquement.

**Q3.** (une ou plusieurs réponses) Quelles sont de bonnes pratiques de plan de classement ?

a) Dossiers fondés sur les fonctions de l'organisation.
b) Dossiers personnels pour les documents de l'organisation.
c) Même sous-structure pour tous les projets.
d) Règle de nommage commençant par la date.

**Q4.** (une seule réponse) Le principe de sauvegarde 3-2-1 signifie :

a) 3 sauvegardes par jour, 2 par semaine, 1 par mois.
b) 3 mots de passe, 2 utilisateurs, 1 administrateur.
c) 3 ans de conservation, 2 copies, 1 archive.
d) au moins 3 copies, sur 2 supports différents, dont 1 hors du bureau.

**Q5.** (une seule réponse) Un identifiant de bénéficiaire recommandé est :

a) ses initiales suivies de sa date de naissance.
b) son numéro de téléphone.
c) un code non signifiant comme BEN-000317.
d) son nom de famille.

**Q6.** (une ou plusieurs réponses) Des données pseudonymisées :

a) restent des données personnelles.
b) permettent une réidentification avec la table de correspondance.
c) peuvent être librement publiées.
d) exigent de protéger la table de correspondance.

**Q7.** (mise en situation, une seule réponse) Avant de choisir un outil de suivi des bénéficiaires, quelle vérification protège le mieux contre la dépendance au fournisseur ?

a) La possibilité d'exporter toutes les données dans un format ouvert.
b) La couleur de l'interface.
c) Le nombre de fonctionnalités d'IA.
d) La popularité de l'outil.

**Q8.** (mise en situation, une seule réponse) Un bénévole quitte l'association. Que faut-il faire en priorité en matière d'accès ?

a) Attendre la revue annuelle.
b) Lui laisser ses accès s'il reste en bons termes.
c) Changer seulement le mot de passe du Wi-Fi.
d) Retirer ses accès le jour de son départ.

**Q9.** (une seule réponse) Pourquoi l'IA ne suffit-elle pas à préserver la mémoire institutionnelle ?

a) Parce qu'elle ne sait pas lire.
b) Parce qu'elle oublie tout chaque soir.
c) Parce qu'elle ne peut restituer que ce qui a été consigné.
d) Parce qu'elle est interdite dans les ASBL.

**Q10.** (une ou plusieurs réponses) Pour prévenir les erreurs à la saisie, on peut utiliser :

a) des listes déroulantes.
b) des champs obligatoires.
c) des formats de date imposés.
d) la correction a posteriori uniquement.

## 7.14 Corrigé détaillé : Module 7

**Q1 : c.** Un courriel n'a pas de format fixe.

**Q2 : b.** Une même entité enregistrée plusieurs fois est un défaut d'unicité.

**Q3 : a, c, d.** Les dossiers personnels (b) rendent les documents introuvables après un départ.

**Q4 : d.** Trois copies, deux supports, une copie hors site, et une restauration testée.

**Q5 : c.** Un code non signifiant ne révèle aucune information personnelle.

**Q6 : a, b, d.** Des données pseudonymisées ne peuvent pas être publiées librement (c).

**Q7 : a.** La portabilité des données est la meilleure garantie.

**Q8 : d.** Le retrait immédiat des accès est une mesure de base du moindre privilège.

**Q9 : c.** Ce qui n'a pas été documenté ne peut pas être retrouvé.

**Q10 : a, b, c.** La prévention à la saisie est plus efficace que la seule correction a posteriori (d).

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.


# Module 8 : Éthique, responsabilité, sécurité et réglementation de l'IA {#h11}

## 8.1 Mise en situation

La Maison des Aînés Solidaires accompagne des personnes âgées isolées. Pour mieux organiser les visites, Thomas, coordinateur des bénévoles, a eu une idée : enregistrer les appels téléphoniques des personnes accompagnées, les faire transcrire et résumer par un assistant gratuit, puis demander à l'outil d'identifier « les personnes qui montrent des signes de déclin cognitif » afin de leur envoyer plus de visites.

L'intention est généreuse. Pourtant, le projet cumule presque tous les risques que ce module va examiner : des données de santé déduites sans base médicale, des personnes vulnérables enregistrées sans consentement éclairé, un outil gratuit dont les conditions de traitement des données n'ont pas été lues, une forme de profilage, et des décisions (l'intensité de l'accompagnement) qui dépendraient d'un résultat automatique non vérifiable.

Ce module ne vise pas à décourager l'innovation. Il vise à donner à chacun les réflexes qui permettent d'innover sans nuire.

## 8.2 Problématique

Les ASBL agissent souvent auprès de personnes en situation de vulnérabilité, dans un rapport de confiance. Une erreur, une fuite ou une discrimination causée par un outil numérique peut avoir des conséquences graves pour ces personnes, et ruiner la confiance des communautés, des bailleurs et du public. En outre, le cadre juridique de l'IA et de la protection des données se renforce rapidement dans de nombreux pays. L'éthique n'est donc pas un supplément d'âme : c'est une condition de légitimité et de durabilité.

## 8.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. expliquer les principes éthiques internationaux applicables à l'IA ;
2. reconnaître les biais et les risques de discrimination ;
3. appliquer les principes de protection des données : minimisation, finalité, base légale, consentement, sécurité ;
4. classer les données selon le « feu tricolore » et choisir l'outil approprié ;
5. organiser la supervision humaine et identifier les décisions qui doivent rester humaines ;
6. prendre en compte la cybersécurité, le droit d'auteur, l'impact environnemental et la protection des personnes vulnérables ;
7. situer votre organisation par rapport aux cadres internationaux et nationaux ;
8. anonymiser un texte avant traitement et conduire une revue de biais.

## 8.4 Notions et définitions

- **Biais algorithmique** : écart systématique dans les résultats d'un système, qui défavorise ou favorise certains groupes.
- **Discrimination** : traitement défavorable d'une personne fondé sur un critère prohibé (sexe, origine, handicap, âge, religion, etc., selon les lois applicables).
- **Transparence** : fait d'informer les personnes qu'un système d'IA est utilisé, à quelles fins et avec quelles limites.
- **Explicabilité** : capacité à donner aux personnes concernées des raisons compréhensibles d'un résultat.
- **Minimisation des données** : ne collecter et ne traiter que les données strictement nécessaires à la finalité.
- **Finalité** : objectif précis et légitime pour lequel des données sont traitées.
- **Consentement éclairé** : accord libre, spécifique, informé et univoque, qui peut être retiré.
- **Profilage** : traitement automatisé visant à évaluer certains aspects d'une personne (comportement, santé, fiabilité…).
- **Supervision humaine** : capacité organisée de personnes compétentes à comprendre, contrôler, corriger, interrompre ou refuser le résultat d'un système.

## 8.5 Explications détaillées

### Les principes internationaux de référence

Plusieurs textes internationaux convergent sur un socle de principes. Il est important de distinguer leur **nature juridique**.

| Texte | Nature | Ce qu'il apporte à une ASBL |
|---|---|---|
| Recommandation de l'UNESCO sur l'éthique de l'IA (2021) | Recommandation adoptée par les États membres ; non contraignante pour les organisations | Socle de valeurs : droits humains et dignité, environnement, diversité et inclusion ; principes de proportionnalité, sûreté, équité, transparence, responsabilité, supervision humaine |
| Principes de l'OCDE sur l'IA (2019, révisés en 2024) | Instrument non contraignant, engagement politique des pays adhérents | Croissance inclusive, droits humains, transparence, robustesse et sécurité, responsabilité ; la révision de 2024 renforce l'attention à la sécurité, à la vie privée, à la propriété intellectuelle et à l'intégrité de l'information |
| NIST AI RMF 1.0 (2023) et profil IA générative (2024) | Cadres volontaires | Démarche de gestion des risques en quatre fonctions : gouverner, cartographier, mesurer, gérer ; liste de risques propres à l'IA générative |
| ISO/IEC 42001:2023 | Norme volontaire, certifiable | Exigences d'un système de management de l'IA : politique, rôles, évaluation des risques et des impacts, contrôles, amélioration continue |
| Convention-cadre du Conseil de l'Europe sur l'IA (2024) | Traité contraignant pour les États qui le ratifient | Obligations des États pour que l'IA respecte les droits humains, la démocratie et l'État de droit |
| Règlement (UE) 2024/1689 (AI Act) | Loi contraignante dans l'Union européenne | Approche par niveaux de risque : pratiques interdites, systèmes à haut risque, obligations de transparence |

Table: Tableau 8.1 : Explications détaillées

Ces textes partagent une idée centrale : **plus un usage de l'IA peut affecter les droits et la sécurité des personnes, plus les exigences de contrôle, de transparence et de supervision humaine doivent être élevées.**

### Droits humains, dignité et équité

Dans une ASBL, ces principes se traduisent par des questions très concrètes :

- **Dignité** : l'usage de l'IA respecte-t-il les personnes ? Utiliser des images générées de « bénéficiaires souffrants » pour une campagne de dons est contraire à la dignité et trompeur. Faire répondre un robot à une personne en détresse sans possibilité de parler à un humain l'est aussi.
- **Équité** : l'outil fonctionne-t-il aussi bien pour tout le monde ? Un système de transcription qui comprend mal certains accents, une traduction médiocre dans les langues minoritaires, un formulaire en ligne inaccessible aux personnes malvoyantes créent des inégalités d'accès.
- **Autonomie** : les personnes gardent-elles la maîtrise des décisions qui les concernent, et peuvent-elles les contester ?

### Biais et discrimination

Les biais peuvent naître à chaque étape :

| Origine | Exemple dans une ASBL |
|---|---|
| Données d'entraînement déséquilibrées | Un modèle de « risque d'abandon scolaire » entraîné sur des données d'un quartier urbain, appliqué à une zone rurale |
| Variables substituts (*proxies*) | Utiliser le code postal, qui peut refléter l'origine ou le niveau social |
| Historique discriminatoire | Un tri de candidatures appris sur des recrutements passés qui favorisaient un profil |
| Conception de l'outil | Formulaire exigeant une adresse fixe, excluant les personnes sans domicile |
| Usage | Appliquer l'outil hors du contexte pour lequel il a été conçu |
| IA générative | Descriptions ou images stéréotypées de certains groupes, de certains métiers |

Table: Tableau 8.2 : Explications détaillées

Parades : interroger la représentativité des données ; tester les résultats par sous-groupes (sexe, âge, langue, zone) ; exclure les variables sensibles et leurs substituts lorsqu'ils ne sont pas justifiés ; impliquer des personnes concernées dans la conception ; conserver une décision humaine motivée ; prévoir un recours.

### Transparence et explicabilité

Les personnes ont le droit de savoir quand un système d'IA intervient dans une interaction ou une décision qui les concerne. Bonnes pratiques :

- signaler qu'un assistant en ligne est automatisé et offrir un contact humain ;
- mentionner, dans les politiques de confidentialité, les traitements assistés par l'IA ;
- indiquer, en interne et selon les règles de l'organisation, quand un document a été produit avec une aide de l'IA ;
- pour toute décision affectant une personne, pouvoir en expliquer les motifs en termes compréhensibles : ce qui suppose que la décision ait été prise par un humain capable de la justifier.

### Confidentialité et protection des données

![Figure 8.1 : Le feu tricolore de classification des données](03_ILLUSTRATIONS/figures/fig_8_1.svg){#fig-8-1}

Les grands principes de protection des données, communs à de nombreuses législations, sont :

1. **Licéité** : disposer d'une base légale pour traiter les données (consentement, contrat, obligation légale, intérêt légitime, etc., selon les lois applicables).
2. **Finalité** : utiliser les données pour l'objectif annoncé, pas pour un autre.
3. **Minimisation** : seulement les données nécessaires.
4. **Exactitude** : des données à jour et justes.
5. **Limitation de la conservation** : ne pas garder les données plus longtemps que nécessaire.
6. **Sécurité** : protéger contre l'accès non autorisé, la perte, la fuite.
7. **Responsabilité** : pouvoir démontrer le respect de ces principes.

**Le feu tricolore** (annexe 11) traduit ces principes en règle d'usage quotidienne :

| Couleur | Définition | Exemples | Outils autorisés |
|---|---|---|---|
| 🟢 **Vert** | Information publique ou destinée à l'être | Rapport annuel publié, article du site, appel à projets public | Outils grand public autorisés, avec vérification des sorties |
| 🟠 **Orange** | Information interne, non personnelle ou agrégée | Budget non publié, procédures, PV de CA, statistiques agrégées | Outils professionnels validés par l'organisation (contrat prévoyant la confidentialité et l'absence d'utilisation des données pour l'entraînement), après minimisation |
| 🔴 **Rouge** | Données personnelles identifiantes, données sensibles, informations confidentielles | Listes nominatives de bénéficiaires, données de santé, données d'enfants, salaires, dossiers disciplinaires, coordonnées bancaires, signalements d'abus | Interdit dans tout outil non validé spécifiquement. Anonymisation préalable, base légale, accord du responsable, outil sécurisé |

Table: Tableau 8.3 : Explications détaillées

> **⚖️ Adaptation réglementaire** : Les lois de protection des données diffèrent selon les pays : définitions des données sensibles, bases légales, droits des personnes, règles de transfert international, obligations de déclaration. Dans l'Union européenne, le règlement (UE) 2016/679 (RGPD) s'applique ; d'autres pays disposent de lois proches ; certains États ont ratifié la Convention 108+ du Conseil de l'Europe. Lorsque vous utilisez un outil en ligne, vos données peuvent être traitées dans un autre pays : vérifiez la localisation des serveurs et les conditions de transfert.

**Avant d'utiliser un outil en ligne avec des données internes, vérifiez au minimum :**

- les conditions d'utilisation et la politique de confidentialité (les données saisies servent-elles à entraîner les modèles ? peut-on le désactiver ?) ;
- la durée de conservation des conversations et des fichiers ;
- la localisation des traitements ;
- l'existence d'une offre professionnelle avec engagement contractuel de confidentialité ;
- la possibilité de supprimer ses données.

> **🔎 À retenir** : Les offres gratuites ne sont pas nécessairement dangereuses, mais elles n'offrent généralement pas les garanties contractuelles nécessaires pour des données internes ou personnelles. Par défaut : vert uniquement.

### Le consentement

Lorsque le consentement est la base légale (enregistrement d'un entretien, photo d'un bénéficiaire, participation à une enquête), il doit être **libre** (pas de condition d'accès à un service), **spécifique** (pour un usage précis), **éclairé** (expliqué dans une langue et des termes compris), **univoque** et **révocable**. Dans un contexte d'aide, la liberté du consentement est fragile : une personne qui dépend de l'ASBL pour un service peut se sentir obligée d'accepter. Il faut donc proposer une réelle alternative et ne jamais conditionner l'aide au consentement à un traitement non nécessaire.

### Cybersécurité

L'IA introduit des risques de sécurité nouveaux, en plus des risques classiques.

| Risque | Description | Mesures |
|---|---|---|
| Fuite par saisie | Données confidentielles collées dans un outil non validé | Feu tricolore, formation, outils validés |
| Hameçonnage amélioré | Courriels frauduleux très crédibles, imitation de voix d'un dirigeant pour demander un virement | Procédure de vérification par un second canal pour tout paiement inhabituel |
| Injection de prompt | Instructions cachées dans un document ou une page web, qui détournent un assistant ou un agent (premier risque du Top 10 OWASP pour les applications de modèles de langage) | Limiter les droits des agents ; validation humaine des actions ; ne pas faire traiter de contenus non fiables par des agents disposant de droits étendus |
| Comptes compromis | Accès d'un attaquant aux outils et à l'historique des conversations | Double authentification, mots de passe uniques, revue des accès |
| Extensions et applications non vérifiées | Modules complémentaires qui accèdent aux données | Liste des outils autorisés (annexe 9) |

Table: Tableau 8.4 : Explications détaillées

### Supervision humaine et décisions automatisées

![Figure 8.2 : Trois modes de supervision humaine](03_ILLUSTRATIONS/figures/fig_8_2.svg){#fig-8-2}

La supervision humaine doit être **réelle** : une personne qui valide 200 propositions par heure sans les lire ne supervise rien (c'est le « biais d'automatisation », tendance à faire excessivement confiance à la machine). Elle suppose du temps, des compétences, le droit de refuser, et une trace de la validation.

> **⚖️ Adaptation réglementaire** : Plusieurs textes encadrent les décisions fondées exclusivement sur un traitement automatisé et produisant des effets importants pour les personnes : par exemple l'article 22 du RGPD dans l'Union européenne, ou la Convention 108+. Le règlement européen sur l'IA classe en « haut risque » certains usages, notamment dans l'emploi, l'éducation ou l'accès à des services essentiels, avec des obligations renforcées ; son calendrier d'application a été modifié en 2026 par un règlement dit « omnibus », qui a reporté certaines échéances relatives aux systèmes à haut risque : vérifiez les dates en vigueur sur le site officiel EUR-Lex à la date de votre projet.

**Décisions qui doivent impérativement rester sous contrôle humain dans une ASBL :**

| Domaine | Décisions | Rôle possible de l'IA |
|---|---|---|
| Bénéficiaires | Admission ou refus d'un service, niveau d'aide, sortie d'un programme, signalement de protection | Aide à l'organisation de l'information, jamais la décision |
| Ressources humaines | Recrutement, évaluation, sanction, licenciement, rémunération | Rédaction de supports, organisation des candidatures selon une grille humaine |
| Bénévoles | Acceptation, exclusion | Planification logistique |
| Finances | Approbation de paiements, validation des écritures, choix de fournisseurs | Propositions, contrôles, alertes |
| Gouvernance | Adoption de politiques, de budgets, de comptes | Préparation de documents |
| Communication externe | Publication au nom de l'ASBL | Brouillons |
| Protection | Toute situation d'abus, d'exploitation, de danger | Aucune automatisation du traitement ; orientation immédiate vers un référent humain |

Table: Tableau 8.5 : Explications détaillées

### Hallucinations et responsabilité

L'organisation reste responsable de ce qu'elle publie, transmet ou décide, même si un outil d'IA l'a produit. Un rapport contenant un chiffre inventé engage l'ASBL vis-à-vis du bailleur. D'où la règle : **tout contenu externe est relu et validé par une personne habilitée.**

### Droits d'auteur et propriété intellectuelle

Trois questions se posent :

1. **Ce que l'on fournit à l'outil** : avez-vous le droit d'utiliser ce document (rapport d'un partenaire, article payant, photo d'un tiers) ?
2. **Ce que l'outil produit** : les règles sur la protection des contenus générés par IA et sur les droits du fournisseur varient selon les pays et les conditions d'utilisation des outils. Un contenu généré peut aussi reproduire des éléments protégés.
3. **Ce que vous publiez** : citez vos sources ; ne présentez pas une image générée comme une photo réelle ; vérifiez les conditions d'utilisation commerciale des images générées.

### Sécurité des bénéficiaires et personnes vulnérables

Les enfants, les personnes âgées dépendantes, les personnes en situation de handicap, les personnes déplacées ou réfugiées, les victimes de violences méritent une protection renforcée :

- aucune donnée les concernant dans un outil non validé ;
- prudence extrême sur toute forme de profilage ou de « score » ;
- attention aux risques de réidentification à partir de données apparemment anonymes (un village, un âge et une situation familiale peuvent suffire à identifier une personne) ;
- dans les contextes de crise, prise en compte des risques d'accès aux données par des acteurs hostiles : un enjeu détaillé par le *Handbook on Data Protection in Humanitarian Action* du CICR (Marelli, 2024), y compris pour les données hébergées chez des prestataires de cloud.

### Impact environnemental

L'IA consomme de l'énergie, principalement dans les centres de données. Selon l'Agence internationale de l'énergie, les centres de données ont consommé environ 415 TWh d'électricité en 2024, soit environ 1,5 % de la consommation mondiale, et cette consommation pourrait plus que doubler pour atteindre environ 945 TWh en 2030 dans son scénario de référence, l'IA étant le principal moteur de cette croissance (AIE, 2025). À l'échelle d'une ASBL, la sobriété consiste à : utiliser l'IA lorsqu'elle apporte une valeur réelle ; préférer des outils proportionnés (pas de génération d'images ou de vidéos superflues) ; éviter les requêtes répétées inutiles ; intégrer ce critère dans le choix des fournisseurs lorsque l'information est disponible.

### Réglementation internationale et nationale : comment s'y retrouver

1. **Identifiez les lois applicables** : le pays du siège, les pays d'intervention, le pays de localisation des données, et les règles imposées par vos bailleurs.
2. **Distinguez** : lois contraignantes (protection des données, réglementation de l'IA lorsqu'elle existe, droit du travail, droit d'auteur) ; normes volontaires (ISO/IEC 42001) ; cadres de référence (UNESCO, OCDE, NIST) ; exigences contractuelles des bailleurs.
3. **Désignez une personne responsable** du suivi réglementaire, même à temps partiel.
4. **Consultez un juriste** pour les traitements de données sensibles ou les projets d'envergure.

## 8.6 Application professionnelle : refonder le projet de Thomas

Reprenons la mise en situation et appliquons la démarche.

| Question | Réponse pour le projet initial | Projet révisé |
|---|---|---|
| Quelle finalité ? | Repérer un déclin cognitif | Mieux planifier les visites selon les besoins **exprimés** |
| Données nécessaires ? | Enregistrements d'appels, santé déduite | Fréquence de visite souhaitée, disponibilités, demandes explicites |
| Base légale / consentement ? | Absent | Information claire, consentement recueilli à l'entrée dans le programme pour les seules données nécessaires |
| Outil ? | Gratuit, non vérifié | Tableur ou base de données interne ; l'IA n'intervient que sur des données vertes (planning sans noms) |
| Décision ? | Automatique (score) | Humaine : le coordinateur et l'infirmière référente, si un besoin de santé est exprimé |
| Recours ? | Aucun | Les personnes peuvent demander plus ou moins de visites à tout moment |

Table: Tableau 8.6 : Application professionnelle : refonder le projet de Thomas

Le projet révisé conserve l'objectif, mieux accompagner, sans profilage ni données de santé déduites.

### Processus de mise en œuvre d'un examen éthique simplifié (pour tout nouveau cas d'usage)

1. Décrire le cas d'usage (fiche d'opportunité, module 6).
2. Classer les données (feu tricolore).
3. Identifier les personnes affectées et l'impact d'une erreur.
4. Vérifier finalité, minimisation, base légale, information des personnes.
5. Évaluer les risques de biais ; prévoir un test par sous-groupes si l'outil classe ou évalue.
6. Définir le mode de supervision humaine et les décisions réservées.
7. Vérifier l'outil (contrat, localisation, entraînement, sécurité).
8. Consigner l'analyse dans le registre des risques IA (annexe 8) et le registre des outils (annexe 9).
9. Faire valider par le référent IA et, pour les cas à risque élevé, par la direction.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Politique d'utilisation d'une page, feu tricolore affiché, formation d'une heure, examen éthique simplifié sous forme de checklist | Annexes 10, 11, 12 | Temps | Dépend de la discipline individuelle |
| Intermédiaire | Outils professionnels validés, paramètres de confidentialité configurés par l'administrateur, registre des outils et des risques, référent IA | Suite professionnelle, registres | Abonnements | Exige un suivi régulier |
| Avancé | Système de management de l'IA inspiré d'ISO/IEC 42001 ; analyses d'impact formalisées ; journalisation et surveillance des usages ; prévention des fuites de données | Outils de gouvernance, de sécurité et de journalisation | Élevés | Compétences juridiques et techniques |

Table: Tableau 8.7 : Application professionnelle : refonder le projet de Thomas

## 8.7 Prompts prêts à l'emploi

### Fiche P8.1 : Anonymiser un texte avant traitement

**A. Titre.** Repérage des éléments identifiants dans un texte.

**B. Objectif.** Identifier et remplacer les informations permettant d'identifier des personnes, **avant** d'utiliser un texte avec un outil d'IA externe.

**C. Contexte d'utilisation.** Rapports de terrain, comptes rendus, retours de bénéficiaires.

**D. Données nécessaires.** Le texte. **Important :** cette fiche s'utilise avec un outil **validé par l'organisation** pour des données orange ou rouges (outil interne, offre professionnelle avec garanties), ou bien elle sert de liste de contrôle pour une anonymisation manuelle. Elle ne doit pas être utilisée avec un outil grand public sur un texte contenant des données personnelles : ce serait divulguer précisément ce que l'on veut protéger.

**E. Prompt complet.**

```text
Contexte : je dois anonymiser le texte ci-dessous avant de l'utiliser
pour une analyse. Il concerne des [TYPE DE PERSONNES].
Tâche :
1. Repère tous les éléments identifiants directs (noms, prénoms,
   surnoms, numéros de téléphone, adresses, numéros de dossier,
   dates de naissance) et indirects (lieu précis + âge + situation
   familiale, profession rare, événement singulier).
2. Remplace-les par des marqueurs génériques : [PERSONNE 1],
   [VILLAGE A], [ÂGE : 40-49 ans], etc., de façon cohérente dans
   tout le texte.
3. Produis un tableau « Élément repéré (catégorie seulement, sans
   reproduire la valeur) | Marqueur | Raison ».
4. Signale les passages où le risque de réidentification reste
   élevé même après remplacement.
Données : <texte>[TEXTE]</texte>
Limites : ne résume pas, ne reformule pas le reste du texte.
```

**F. Instructions d'utilisation.** Vérifiez d'abord que l'outil est autorisé pour ce niveau de données. Conservez l'éventuelle table de correspondance séparément, en accès restreint, ou détruisez-la si elle n'est pas nécessaire (anonymisation réelle).

**G. Résultat attendu.** Le texte avec marqueurs, un tableau des catégories remplacées, une alerte sur les passages à risque.

**H. Exemple d'application (illustratif).** Un rapport de visite mentionne « la grand-mère de 87 ans qui vit seule près de l'ancienne école de [village], dont le fils est le seul pharmacien du canton ». L'outil remplace les éléments et signale que la combinaison « seul pharmacien du canton » reste identifiante ; la phrase est réécrite manuellement : « une personne âgée vivant seule, dont un proche réside dans la commune ».

**I. Méthode de vérification.** Relecture humaine intégrale ; recherche dans le texte final des noms connus (Ctrl+F) ; test « un voisin reconnaîtrait-il la personne ? ».

**J. Précautions.** L'anonymisation automatique n'est jamais parfaite. Pour des données particulièrement sensibles (violences, santé, statut migratoire), privilégiez une anonymisation manuelle par une personne formée, ou n'utilisez pas d'outil externe.

**K. Amélioration.** Si des identifiants indirects subsistent : « Applique une généralisation plus forte : remplace les âges par des tranches de 20 ans et les lieux par la région. »

### Fiche P8.2 : Revue de biais d'un contenu ou d'un outil

**A. Titre.** Revue de biais et d'inclusion.

**B. Objectif.** Repérer stéréotypes, exclusions et traitements inéquitables dans un contenu (texte, campagne) ou dans les règles d'un outil (grille, formulaire, critères).

**C. Contexte d'utilisation.** Communication, RH, programmes ; avant publication ou mise en service.

**D. Données nécessaires.** Le contenu ou la description des règles ; le public visé.

**E. Prompt complet.**

```text
Contexte : [NOM DE L'ASBL] s'apprête à [publier / utiliser] le
[contenu / grille / formulaire] ci-dessous, destiné à [PUBLIC].
Nos valeurs incluent : [VALEURS].
Tâche : réalise une revue de biais et d'inclusion.
Données : <contenu>[CONTENU OU RÈGLES]</contenu>
Résultat attendu :
1. Stéréotypes ou représentations dévalorisantes (citer le passage).
2. Critères ou formulations susceptibles d'exclure ou de défavoriser
   des groupes (selon le sexe, l'âge, l'origine, le handicap, la
   langue, le lieu de vie, la situation économique), y compris par
   des critères indirects.
3. Obstacles d'accessibilité (lisibilité, langue, format, handicap).
4. Pour chaque point : gravité (faible/moyenne/forte) et
   reformulation ou correction proposée.
5. Questions à poser à des personnes concernées pour valider.
Limites : distingue les problèmes certains des problèmes possibles.
```

**F. Instructions d'utilisation.** Utilisable avec des contenus verts ou orange. Pour une grille RH, décrivez les critères sans données de candidats.

**G. Résultat attendu.** Une liste argumentée de points, avec gravité et propositions.

**H. Exemple d'application (illustratif).** Une annonce de bénévolat exigeant « permis de conduire et disponibilité en journée » est signalée comme excluant les personnes en emploi et celles sans permis, alors que seules deux missions sur dix l'exigent. L'annonce est scindée par type de mission.

**I. Méthode de vérification.** Soumettre les conclusions à deux ou trois personnes concernées ou à une organisation représentative ; ne pas considérer la revue automatique comme suffisante.

**J. Précautions.** L'outil lui-même peut être biaisé ; il ne remplace pas la consultation des personnes concernées.

**K. Amélioration.** « Réalise la même revue du point de vue d'une personne [PROFIL PRÉCIS], puis compare. »

## 8.8 Résultats attendus

Une politique d'utilisation de l'IA (annexe 10), une classification des données comprise par tous, une liste des outils autorisés, un examen éthique pour chaque nouveau cas d'usage, des décisions réservées identifiées, des personnes formées.

## 8.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Toute décision qui affecte les droits, l'accès à un service, l'emploi, la sécurité ou la réputation d'une personne est prise par un humain compétent, qui peut l'expliquer, et contre laquelle un recours est possible. Toute situation de protection (abus, exploitation, danger) est traitée immédiatement par un référent humain, en dehors de tout circuit automatisé.

## 8.10 Risques et erreurs à éviter

- Considérer qu'un outil gratuit « sans inscription » ne pose pas de problème de confidentialité.
- Croire que remplacer les noms suffit à anonymiser.
- Recueillir un consentement de façade dans une relation de dépendance.
- Déduire des données sensibles (santé, orientation, origine) à partir d'autres données.
- Laisser la supervision humaine devenir une formalité.
- Publier des images générées sans le signaler.
- Ignorer les exigences de protection des données des bailleurs.

## 8.11 Exercice pratique

**Consigne (2 heures).** (1) Listez dix types de documents ou de données de votre organisation et attribuez à chacun une couleur du feu tricolore. (2) Choisissez un cas d'usage envisagé et appliquez les neuf étapes de l'examen éthique simplifié. (3) Rédigez la liste des décisions réservées à l'humain pour ce cas. (4) Appliquez la fiche P8.2 à une annonce ou une affiche de votre organisation.

**Éléments de correction.** Les données nominatives de bénéficiaires, de santé, d'enfants, les salaires et les signalements sont en rouge ; les budgets internes et les PV en orange ; les publications en vert. L'examen éthique identifie au moins un risque pour des personnes et une mesure concrète. Les décisions réservées couvrent toute décision affectant une personne.

## 8.12 Synthèse

- Les cadres internationaux (UNESCO, OCDE, NIST, ISO/IEC 42001, Conseil de l'Europe, AI Act) convergent : contrôle proportionné au risque pour les personnes.
- Les biais naissent des données, des critères et des usages ; on les teste et on implique les personnes concernées.
- La protection des données repose sur la finalité, la minimisation, la base légale, la sécurité et la responsabilité ; le feu tricolore la traduit au quotidien.
- La supervision humaine doit être réelle ; certaines décisions ne se délèguent jamais.
- Cybersécurité, droit d'auteur, environnement et protection des personnes vulnérables complètent l'analyse.
- Les obligations juridiques dépendent des pays : identifiez-les et faites-vous conseiller.

## 8.13 QCM : Module 8

**Q1.** (une seule réponse) La Recommandation de l'UNESCO sur l'éthique de l'IA (2021) est :

a) une loi directement applicable aux ASBL dans tous les pays.
b) une norme certifiable.
c) un contrat type.
d) une recommandation adoptée par les États membres, non contraignante pour les organisations.

**Q2.** (une seule réponse) ISO/IEC 42001:2023 est :

a) une loi européenne.
b) une recommandation de l'OCDE.
c) une norme volontaire de système de management de l'IA, certifiable.
d) un logiciel.

**Q3.** (une ou plusieurs réponses) Lesquelles de ces données sont classées « rouge » ?

a) La liste nominative des enfants inscrits.
b) Le rapport annuel publié.
c) Les salaires du personnel.
d) Un signalement d'abus.

**Q4.** (une seule réponse) Le principe de minimisation signifie :

a) ne traiter que les données strictement nécessaires à la finalité.
b) réduire la taille des fichiers.
c) minimiser le nombre d'outils.
d) supprimer toutes les données chaque année.

**Q5.** (une ou plusieurs réponses) Un consentement valable doit être :

a) libre.
b) spécifique.
c) éclairé.
d) irrévocable.

**Q6.** (une seule réponse) Le « biais d'automatisation » désigne :

a) une erreur de programmation.
b) un biais dans les données d'entraînement.
c) la tendance des humains à faire excessivement confiance aux résultats d'une machine.
d) la lenteur des automatisations.

**Q7.** (mise en situation, une seule réponse) Un message vocal imitant la voix du directeur demande au comptable un virement urgent. Que faire ?

a) Exécuter, la voix est reconnaissable.
b) Vérifier par un second canal convenu avant tout paiement inhabituel.
c) Demander à un assistant d'IA si la voix est authentique.
d) Exécuter puis prévenir le directeur.

**Q8.** (mise en situation, une seule réponse) Un partenaire propose un outil qui attribue un « score de vulnérabilité » à chaque ménage pour décider automatiquement de l'attribution de l'aide. Votre position ?

a) Refuser toute décision automatique ; l'outil peut au mieux éclairer une décision humaine motivée, après examen des biais, de la base légale et avec un recours.
b) Accepter, c'est plus objectif.
c) Accepter si le score est expliqué en anglais.
d) Accepter pour les ménages qui ne protestent pas.

**Q9.** (une seule réponse) Une image générée par IA montrant des enfants souffrants pour une campagne de dons :

a) est acceptable si elle est réaliste.
b) est acceptable si l'outil est payant.
c) est obligatoire pour protéger les vrais enfants.
d) pose des problèmes de dignité et de tromperie et est à proscrire.

**Q10.** (une ou plusieurs réponses) Avant d'utiliser un outil en ligne avec des données internes, il faut vérifier :

a) si les données saisies servent à entraîner les modèles.
b) la localisation des traitements.
c) la durée de conservation des conversations.
d) le nombre d'abonnés de l'outil sur les réseaux sociaux.

## 8.14 Corrigé détaillé : Module 8

**Q1 : d.** C'est un instrument normatif adopté par les États, qui n'impose pas directement d'obligations juridiques aux organisations.

**Q2 : c.** Norme volontaire et certifiable de système de management.

**Q3 : a, c, d.** Le rapport annuel publié est vert.

**Q4 : a.** Ne traiter que ce qui est nécessaire.

**Q5 : a, b, c.** Le consentement doit au contraire pouvoir être retiré (d).

**Q6 : c.** Il rend la supervision humaine illusoire si elle n'est pas organisée.

**Q7 : b.** Les imitations de voix sont devenues accessibles ; seule une procédure de vérification indépendante protège. Un outil d'IA (c) n'offre pas de garantie fiable.

**Q8 : a.** L'attribution d'une aide est une décision sur des personnes vulnérables : elle reste humaine, motivée et contestable.

**Q9 : d.** Elle porte atteinte à la dignité et trompe les donateurs.

**Q10 : a, b, c.** La popularité (d) n'est pas un critère de sécurité.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Agence internationale de l'énergie (AIE/IEA). (2025). *Energy and AI*.
- Conseil de l'Europe. (2018). *Protocole d'amendement à la Convention 108* (STCE n° 223).
- Conseil de l'Europe. (2024). *Convention-cadre sur l'intelligence artificielle et les droits de l'homme, la démocratie et l'État de droit* (STCE n° 225).
- ISO/IEC. (2023). *ISO/IEC 42001:2023, Artificial intelligence, Management system*.
- Marelli, M. (dir.). (2024). *Handbook on Data Protection in Humanitarian Action* (3e éd.). Cambridge University Press / CICR. https://doi.org/10.1017/9781009414630
- NIST. (2023). *AI Risk Management Framework 1.0* (NIST AI 100-1). https://doi.org/10.6028/NIST.AI.100-1
- NIST. (2024). *Generative AI Profile* (NIST AI 600-1). https://doi.org/10.6028/NIST.AI.600-1
- OCDE. (2019, révisée en 2024). *Recommandation du Conseil sur l'intelligence artificielle*.
- OWASP Foundation. (2024). *OWASP Top 10 for LLM Applications* (version 2025).
- Règlement (UE) 2016/679 (RGPD).
- Règlement (UE) 2024/1689 (AI Act), modifié par le règlement (UE) 2026/1744 (référence à confirmer sur EUR-Lex).
- UNESCO. (2021). *Recommandation sur l'éthique de l'intelligence artificielle*.


# Module 9 : Choisir et mettre en place les bons outils {#h12}

## 9.1 Mise en situation

Le Réseau Citoyen pour l'Eau (RCE) reçoit en une semaine trois sollicitations commerciales : un éditeur d'ERP propose un « module d'IA intégré », une start-up promet un « agent autonome » qui rédigera les rapports aux bailleurs, et un consultant recommande de « tout construire en interne avec des API ». De son côté, Lumière des Collines se demande simplement si l'assistant gratuit de son téléphone suffit.

Les deux organisations se posent, à des échelles différentes, la même question : comment choisir sans se tromper, sans surpayer et sans se rendre dépendantes ?

## 9.2 Problématique

Le marché des outils d'IA évolue très vite, avec des promesses parfois spectaculaires et des modèles économiques variés (gratuit, abonnement par utilisateur, paiement à l'usage, licence). Un mauvais choix coûte cher : abonnements inutilisés, doubles saisies, données prisonnières d'un outil, risques de sécurité. Le choix doit découler du cas d'usage, de la maturité de l'organisation et d'une analyse des risques, jamais d'une démonstration commerciale.

## 9.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. distinguer outils gratuits et payants, cloud et local, sans code, faible code et développement ;
2. expliquer ce que sont une application métier, une API, une intégration, une automatisation et un agent ;
3. choisir un niveau d'implémentation adapté (débutant, intermédiaire, avancé) ;
4. évaluer un fournisseur, y compris sur la sécurité et la réversibilité ;
5. analyser les coûts complets ;
6. utiliser une grille de sélection pondérée.

## 9.4 Notions et définitions

- **Cloud / SaaS** : logiciel utilisé via internet, hébergé par le fournisseur, généralement sur abonnement.
- **Solution locale (*on-premise*)** : logiciel installé sur les ordinateurs ou serveurs de l'organisation.
- **No-code** : création d'applications ou d'automatisations par assemblage visuel, sans programmation.
- **Low-code** : idem, avec possibilité d'ajouter un peu de code pour les cas particuliers.
- **Application métier** : logiciel spécialisé pour une fonction (comptabilité, paie, gestion des donateurs, suivi des bénéficiaires).
- **API** : interface permettant à deux logiciels d'échanger des données ou d'utiliser des services de manière automatisée. Les fournisseurs de modèles d'IA proposent généralement des API facturées à l'usage.
- **Intégration** : connexion entre deux applications pour éviter la ressaisie.
- **Réversibilité** : capacité à quitter un fournisseur en récupérant ses données dans un format exploitable.

## 9.5 Explications détaillées

### Trois niveaux d'implémentation

![Figure 9.1 : Trois niveaux d'implémentation](03_ILLUSTRATIONS/figures/fig_9_1.svg){#fig-9-1}

| | Niveau 1 : Débutant | Niveau 2 : Intermédiaire | Niveau 3 : Avancé |
|---|---|---|---|
| Pour qui | Petites ASBL, peu de moyens techniques | ASBL disposant déjà d'outils numériques | Moyennes et grandes organisations, processus complexes |
| Outils types | Assistant conversationnel, tableur, formulaires, modèles de documents, classement documentaire simple | Suite bureautique professionnelle avec IA intégrée, logiciels métier, plateformes d'automatisation sans code, gestion électronique de documents, tableaux de bord, assistants configurés sur documents internes | API de modèles, bases de données, ERP, architecture RAG, agents, hébergement dédié ou local, gestion des identités, journalisation et supervision |
| Compétences | Bureautique et formation à l'usage | Un « référent numérique » capable de paramétrer | Spécialistes (développement, données, sécurité), internes ou prestataires |
| Coûts | Nuls à faibles | Abonnements par utilisateur, paramétrage | Développement, licences, hébergement, maintenance, sécurité |
| Limites | Offres gratuites : quotas, conditions de confidentialité souvent inadaptées aux données internes, absence de contrat | Dépendance à plusieurs fournisseurs, automatisations à maintenir | Complexité, coût récurrent, besoin d'une gouvernance solide |

Table: Tableau 9.1 : Explications détaillées

> **🔎 À retenir** : Le bon niveau n'est pas le plus élevé, mais celui que l'organisation peut **utiliser, contrôler et maintenir** durablement.

### Gratuit ou payant ?

Les offres gratuites conviennent à l'apprentissage et aux données publiques (vert). Elles présentent généralement : des limites d'usage (nombre de requêtes, taille des fichiers) ; des conditions pouvant autoriser l'utilisation des contenus pour améliorer les services ; l'absence d'engagement contractuel de confidentialité ou de disponibilité ; des changements de conditions sans préavis. Les offres professionnelles payantes apportent, selon les fournisseurs, des garanties contractuelles, une administration centralisée des comptes, des paramètres de confidentialité et un support. Certains fournisseurs proposent des **programmes à tarif réduit pour les organisations à but non lucratif** : renseignez-vous directement auprès d'eux, conditions et éligibilité variant selon les pays.

### Cloud ou local ?

| Critère | Cloud | Local |
|---|---|---|
| Mise en route | Rapide | Plus longue |
| Coût | Abonnement récurrent | Investissement matériel et maintenance |
| Performance des modèles | Accès aux modèles les plus performants | Modèles plus petits, performances moindres sur du matériel courant |
| Confidentialité | Dépend du contrat et de la localisation | Maîtrise interne, mais sécurité à assurer soi-même |
| Connectivité | Indispensable | Fonctionne hors ligne |
| Maintenance | Assurée par le fournisseur | À votre charge |

Table: Tableau 9.2 : Explications détaillées

> **📶 Faible connectivité** : Pour une organisation qui travaille en zone peu connectée, une approche hybride est souvent la plus réaliste : collecte et travail hors ligne (formulaires mobiles, tableurs), synchronisation périodique, et usage du cloud pour les traitements lourds lorsque la connexion est disponible. Des modèles de langage dits « ouverts » peuvent être installés sur un ordinateur portable récent pour des tâches simples hors ligne ; leur installation et leur sécurisation relèvent du niveau Avancé.

### No-code, low-code et développement

Les plateformes d'automatisation sans code permettent de créer des scénarios du type : « lorsqu'un formulaire est soumis → créer une ligne dans le tableau → envoyer le document à un assistant d'IA pour en extraire les informations → notifier le responsable pour validation ». Elles démocratisent l'automatisation, mais :

- chaque scénario devient un petit logiciel à **documenter et maintenir** ;
- une erreur se reproduit à grande échelle ;
- les données transitent par la plateforme : elle doit être évaluée comme tout fournisseur ;
- il faut éviter la prolifération d'automatisations créées par des personnes différentes sans inventaire (annexe 9).

### Applications métier avec IA intégrée

De nombreux logiciels métier (comptabilité, gestion des donateurs, RH, gestion de projets) intègrent désormais des fonctions d'IA. C'est souvent la voie la plus simple : pas d'intégration supplémentaire, données déjà présentes. Questions à poser : la fonction d'IA est-elle activable et désactivable ? quelles données utilise-t-elle ? où sont-elles traitées ? par quel sous-traitant ? peut-on tracer ce qu'elle a proposé et ce qui a été validé ?

### API, intégrations et agents

Au niveau avancé, l'organisation (ou son prestataire) utilise des API pour construire ses propres outils : un assistant RAG sur les procédures, une extraction automatique de factures reliée à l'ERP, un tableau de bord alimenté automatiquement. Les **agents** ajoutent la capacité d'enchaîner des actions. Principes de conception sûre :

1. **moindre privilège** : chaque composant n'accède qu'à ce qui est nécessaire ;
2. **validation humaine** avant toute action irréversible ou externe ;
3. **journalisation** des requêtes, des réponses et des validations ;
4. **séparation** entre contenus non fiables (courriels entrants, pages web) et instructions ;
5. **tests** systématiques avant mise en production (module 19).

### Évaluer un fournisseur

La grille ci-dessous (annexe 9 et fiche P9.1) structure l'évaluation.

| Domaine | Questions |
|---|---|
| Adéquation fonctionnelle | Répond-il au cas d'usage tel que défini ? Démonstration sur **vos** documents ? |
| Données et confidentialité | Données utilisées pour l'entraînement ? Localisation ? Sous-traitants ? Durée de conservation ? Suppression ? |
| Sécurité | Authentification forte ? Chiffrement ? Gestion des droits ? Historique des accès ? Certifications revendiquées (à vérifier) ? |
| Réversibilité | Export complet dans un format ouvert ? Assistance à la sortie ? |
| Pérennité | Ancienneté, clientèle, modèle économique, feuille de route ? |
| Coûts | Modèle de prix ? Évolution prévisible ? Coûts cachés (stockage, utilisateurs supplémentaires, dépassements) ? |
| Support et formation | Langue, délais, documentation ? |
| Accessibilité | Interface conforme aux règles d'accessibilité (par exemple WCAG 2.2) ? Fonctionnement sur mobile et en faible débit ? |
| Conformité | Clauses contractuelles de protection des données conformes aux lois applicables ? |

Table: Tableau 9.3 : Explications détaillées

### Analyser les coûts

Reprenez la méthode du coût total sur trois ans (module 6) : licences et abonnements, mise en place, intégration, formation, temps de contrôle humain, maintenance des automatisations, coûts de sortie. Pour les API facturées à l'usage, estimez un volume mensuel, testez sur un mois pilote, et fixez une **alerte de consommation** pour éviter les mauvaises surprises.

### La grille de sélection

*Exemple (fictif) : RCE compare trois options pour un assistant de questions-réponses sur ses procédures :*

| Critère (poids) | A. Assistant configuré dans la suite bureautique (documents joints) | B. Module IA de l'ERP | C. Développement RAG sur mesure |
|---|---|---|---|
| Adéquation (25 %) | 3 | 2 | 5 |
| Confidentialité et sécurité (20 %) | 4 | 4 | 4 |
| Réversibilité (10 %) | 4 | 2 | 5 |
| Facilité d'adoption (15 %) | 5 | 4 | 3 |
| Coût sur 3 ans, inversé (15 %) | 4 | 3 | 2 |
| Maintenabilité interne (15 %) | 4 | 4 | 2 |
| **Score pondéré** | **3,90** | **3,15** | **3,60** |

Table: Tableau 9.4 : Explications détaillées

*Calcul pour l'option A :* 3 × 0,25 + 4 × 0,20 + 4 × 0,10 + 5 × 0,15 + 4 × 0,15 + 4 × 0,15 = 0,75 + 0,80 + 0,40 + 0,75 + 0,60 + 0,60 = 3,90.

Décision de RCE : démarrer avec l'option A en pilote sur un périmètre restreint (procédures financières), mesurer le taux de réponses correctes, et réévaluer l'option C après six mois si les limites de A sont atteintes.

## 9.6 Application professionnelle : choisir un outil pour Horizons Partagés

| Étape | Action | Responsable | Livrable |
|---|---|---|---|
| 1 | Reprendre la fiche d'opportunité et préciser les exigences (indispensables / souhaitables) | Chef de projet | Liste d'exigences |
| 2 | Identifier 3 à 5 options, dont une sans IA ou avec les outils existants | Référent numérique | Liste courte |
| 3 | Envoyer le questionnaire fournisseur (fiche P9.1) | Référent numérique | Réponses écrites |
| 4 | Démonstration sur 10 documents réels non sensibles ou anonymisés | Utilisateurs clés | Notes de test |
| 5 | Notation avec la grille pondérée (dans un tableur) | Comité de 3 à 5 personnes | Grille signée |
| 6 | Vérification juridique des clauses de protection des données | Direction / conseil juridique | Avis |
| 7 | Décision et inscription au registre des outils | Direction | Décision, registre |

Table: Tableau 9.5 : Application professionnelle : choisir un outil pour Horizons Partagés

### Solutions selon le niveau

| Niveau | Démarche de choix | Coûts | Limites |
|---|---|---|---|
| Débutant | Liste des outils autorisés tenue par la direction ; usage limité aux données vertes ; test de 20 minutes (fiche P2.1) | Nuls | Pas de garanties contractuelles |
| Intermédiaire | Questionnaire fournisseur, démonstration sur cas réels, grille pondérée, revue des conditions | Temps, abonnements | Comparaison parfois difficile entre offres |
| Avancé | Appel d'offres ou consultation formalisée, preuve de concept chiffrée, audit de sécurité, clauses de réversibilité et de niveau de service | Élevés | Durée du processus |

Table: Tableau 9.6 : Application professionnelle : choisir un outil pour Horizons Partagés

## 9.7 Prompt prêt à l'emploi

### Fiche P9.1 : Préparer un questionnaire fournisseur

**A. Titre.** Questionnaire d'évaluation d'un fournisseur de solution d'IA.

**B. Objectif.** Obtenir un questionnaire complet, adapté au cas d'usage, pour comparer objectivement des fournisseurs.

**C. Contexte d'utilisation.** Avant toute souscription d'un outil traitant des données internes ou personnelles.

**D. Données nécessaires.** Description du cas d'usage ; classification des données ; contraintes (budget, connectivité, langues, lois applicables).

**E. Prompt complet.**

```text
Contexte : [NOM DE L'ASBL], [PAYS D'IMPLANTATION ET D'INTERVENTION],
souhaite choisir un outil pour le cas d'usage suivant : [CAS D'USAGE].
Données concernées : [TYPES ET COULEUR : vert/orange/rouge].
Contraintes : [BUDGET, CONNECTIVITÉ, LANGUES, LOIS OU EXIGENCES DES
BAILLEURS].
Tâche : rédige un questionnaire à envoyer aux fournisseurs.
Résultat attendu : 25 à 35 questions fermées ou précises, regroupées
en rubriques : adéquation fonctionnelle ; données et confidentialité ;
sécurité ; réversibilité ; pérennité ; coûts (modèle de prix et coûts
annexes) ; support et formation ; accessibilité et faible débit ;
conformité. Pour chaque question, indique entre parenthèses la
réponse attendue idéale et le niveau de criticité (éliminatoire /
important / souhaitable).
Limites : ne mentionne aucun fournisseur nommément. Formule des
questions auxquelles on peut répondre par oui/non ou par une
information vérifiable, et demande les preuves (documents,
certificats, clauses).
```

**F. Instructions d'utilisation.** Adaptez la criticité à votre situation ; envoyez le même questionnaire à tous les fournisseurs ; exigez des réponses écrites et les documents contractuels correspondants.

**G. Résultat attendu.** Un questionnaire structuré, avec critères éliminatoires explicites.

**H. Exemple d'application (illustratif).** Pour l'extraction de factures (données orange), le questionnaire obtenu inclut notamment la question éliminatoire : « Les documents transmis sont-ils exclus de l'entraînement de vos modèles, par défaut et contractuellement ? (Oui, avec clause contractuelle) ».

**I. Méthode de vérification.** Comparez les réponses aux documents contractuels (conditions générales, accord de traitement des données) ; une réponse commerciale non reprise dans le contrat n'engage pas le fournisseur.

**J. Précautions.** Ne transmettez pas de données réelles aux fournisseurs avant la signature d'un accord de confidentialité ; utilisez des documents anonymisés pour les démonstrations.

**K. Amélioration.** « Ajoute une section spécifique aux exigences de [BAILLEUR / LOI] en matière de localisation et de transfert des données. »

## 9.8 Résultats attendus

Une décision documentée, un outil inscrit au registre (annexe 9) avec son responsable, ses paramètres de confidentialité, les données autorisées et la date de prochaine revue.

## 9.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : La souscription d'un outil traitant des données internes ou personnelles est approuvée par la direction après examen des clauses de protection des données. Les paramètres de confidentialité sont configurés par un administrateur désigné, et non laissés au choix de chaque utilisateur.

## 9.10 Risques et erreurs à éviter

- Choisir sur démonstration commerciale, sans test sur ses propres documents.
- Ignorer la réversibilité.
- Multiplier les outils qui font la même chose.
- Sous-estimer la maintenance des automatisations sans code.
- Donner à un agent des droits étendus sur la messagerie, les fichiers ou les paiements.
- Oublier les coûts à l'usage des API et ne pas fixer d'alerte de consommation.

## 9.11 Exercice pratique

**Consigne (2 heures).** Pour un cas d'usage retenu au module 6 : (1) identifiez trois options de niveaux différents ; (2) appliquez la fiche P9.1 ; (3) notez les options avec la grille pondérée dans un tableur ; (4) rédigez une recommandation d'une demi-page incluant les risques et la stratégie de sortie.

**Éléments de correction.** Une bonne réponse inclut au moins une option simple ; des critères éliminatoires liés aux données ; un calcul vérifiable ; une stratégie de sortie (export des données, durée d'engagement).

## 9.12 Synthèse

- Le niveau d'implémentation se choisit selon ce que l'organisation peut utiliser, contrôler et maintenir.
- Gratuit, payant, cloud, local, no-code, API : chaque option a ses avantages et ses limites.
- L'évaluation d'un fournisseur porte sur la fonction, mais aussi sur les données, la sécurité, la réversibilité et les coûts complets.
- Une grille pondérée, des tests sur des cas réels et la lecture des contrats fondent une décision solide.

## 9.13 QCM : Module 9

**Q1.** (une seule réponse) La réversibilité désigne :

a) la capacité à quitter un fournisseur en récupérant ses données dans un format exploitable.
b) la possibilité d'annuler une requête.
c) la traduction dans les deux sens.
d) le remboursement de l'abonnement.

**Q2.** (une seule réponse) Une API est :

a) un type d'ordinateur.
b) une norme de sécurité.
c) un assistant conversationnel.
d) une interface permettant à des logiciels d'échanger des données ou d'utiliser des services de façon automatisée.

**Q3.** (une ou plusieurs réponses) Les offres gratuites d'outils d'IA présentent souvent :

a) des limites d'usage.
b) des conditions pouvant autoriser l'utilisation des contenus pour améliorer les services.
c) un engagement contractuel de confidentialité adapté aux données sensibles.
d) des changements de conditions possibles sans préavis.

**Q4.** (une seule réponse) Le « bon » niveau d'implémentation est :

a) toujours le plus avancé.
b) celui que l'organisation peut utiliser, contrôler et maintenir.
c) le moins cher.
d) celui du principal bailleur.

**Q5.** (une ou plusieurs réponses) Principes de conception sûre pour des agents IA :

a) moindre privilège.
b) validation humaine avant action irréversible.
c) journalisation.
d) accès complet à la messagerie pour plus d'efficacité.

**Q6.** (une seule réponse) Avec les poids de l'exemple (25/20/10/15/15/15 %), l'option notée 2, 4, 2, 4, 3, 4 obtient :

a) 3,05
b) 3,40
c) 19
d) 3,15

**Q7.** (mise en situation, une seule réponse) Un commercial affirme oralement que « vos données ne servent jamais à l'entraînement ». Que faites-vous ?

a) Vous le croyez.
b) Vous demandez la même chose à un assistant d'IA.
c) Vous exigez que cela figure dans le contrat ou l'accord de traitement des données.
d) Vous ne posez plus de question.

**Q8.** (mise en situation, une seule réponse) Une petite association en zone peu connectée veut améliorer la collecte de données de terrain. Approche la plus réaliste ?

a) Un agent IA dans le cloud en continu.
b) Formulaires mobiles hors ligne, synchronisation périodique, traitements assistés lors des connexions.
c) Un ERP avancé.
d) Renoncer au numérique.

**Q9.** (une seule réponse) Pour un outil facturé à l'usage via API, une bonne pratique consiste à :

a) fixer une alerte de consommation et tester sur un mois pilote.
b) ne pas suivre la consommation.
c) payer d'avance trois ans.
d) partager la clé d'accès entre tous les collaborateurs.

**Q10.** (une ou plusieurs réponses) Les automatisations sans code :

a) doivent être documentées et inventoriées.
b) peuvent reproduire une erreur à grande échelle.
c) ne nécessitent jamais de maintenance.
d) font transiter des données par la plateforme, qui doit être évaluée.

## 9.14 Corrigé détaillé : Module 9

**Q1 : a.** C'est la garantie contre la dépendance.

**Q2 : d.** L'API permet les échanges automatisés entre logiciels.

**Q3 : a, b, d.** Les offres gratuites n'offrent généralement pas les garanties contractuelles nécessaires (c).

**Q4 : b.** L'adéquation aux capacités prime.

**Q5 : a, b, c.** L'accès complet (d) contredit le moindre privilège et expose aux injections de prompt.

**Q6 : d.** 2×0,25 + 4×0,20 + 2×0,10 + 4×0,15 + 3×0,15 + 4×0,15 = 0,50 + 0,80 + 0,20 + 0,60 + 0,45 + 0,60 = 3,15. C'est le score de l'option B du tableau. Réponse c : erreur classique consistant à additionner les notes sans les pondérer.

**Q7 : c.** Seul le contrat engage le fournisseur.

**Q8 : b.** L'approche hybride hors ligne est adaptée à la faible connectivité.

**Q9 : a.** L'alerte évite les dépassements ; la clé d'accès ne se partage jamais (d).

**Q10 : a, b, d.** Elles exigent au contraire une maintenance (c).

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- OWASP Foundation. (2024). *OWASP Top 10 for LLM Applications* (version 2025).
- W3C. (2023, mise à jour 2024). *Web Content Accessibility Guidelines (WCAG) 2.2*.


# Partie IV : Implémenter l'IA dans chaque métier et processus {#h13 .partie}

*Le terrain est préparé : vous connaissez l'IA, votre organisation, vos priorités, vos règles et vos outils. Place aux métiers. Chaque module de cette partie part d'un processus réel et montre, étape par étape, ce que fait l'IA, ce que fait le logiciel, ce que fait le professionnel, et ce qui doit être contrôlé.*

# Module 10 : Gouvernance, direction générale et administration {#h14}

## 10.1 Mise en situation

Lors du conseil d'administration de mars, le CA d'Horizons Partagés a décidé de réviser la politique de voyage, de lancer un audit du bureau régional et de renouveler le mandat de deux administrateurs avant l'assemblée générale. En septembre, personne ne se souvient précisément de ce qui a été décidé : le procès-verbal, rédigé à la main par la secrétaire bénévole, a été adopté avec deux mois de retard, et aucune décision n'avait de responsable ni d'échéance. Les mandats des deux administrateurs ont expiré sans renouvellement, ce qui fragilise la validité de certaines décisions ultérieures.

Ce scénario est courant. Il ne résulte pas d'un manque de bonne volonté, mais d'une absence de **système de suivi de la gouvernance**.

## 10.2 Problématique

La qualité de la gouvernance repose sur des documents fiables (ordres du jour, PV, registres), une information qui circule à temps, des décisions suivies et une continuité institutionnelle malgré le renouvellement des personnes. Ces tâches sont lourdes, souvent assurées par des bénévoles, et leur défaillance expose l'organisation à des risques juridiques et de réputation.

## 10.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. préparer un ordre du jour et un dossier de séance avec l'aide de l'IA ;
2. produire un projet de procès-verbal à partir de notes ou d'une transcription, et le contrôler ;
3. extraire les décisions, leur attribuer un responsable et une échéance, et en organiser le suivi ;
4. suivre les mandats et les obligations institutionnelles ;
5. organiser l'archivage et la circulation de l'information ;
6. concevoir un assistant de gouvernance adapté à la taille de l'organisation.

## 10.4 Notions et définitions

- **Ordre du jour** : liste des points soumis à une réunion, communiquée à l'avance selon les statuts.
- **Dossier de séance** : documents nécessaires aux délibérations (rapports, projets de décision, annexes).
- **Procès-verbal (PV)** : document officiel qui consigne le déroulement d'une réunion et les décisions adoptées ; il est approuvé selon les règles statutaires, généralement lors de la réunion suivante, et signé.
- **Quorum** : nombre minimal de membres présents ou représentés pour que l'organe délibère valablement.
- **Registre des décisions** : tableau de suivi listant chaque décision, son responsable, son échéance et son état d'avancement.
- **Mandat** : fonction confiée pour une durée déterminée (administrateur, président, trésorier).

> **⚖️ Adaptation réglementaire** : Les règles de convocation, de quorum, de majorité, de rédaction et de signature des PV, ainsi que la tenue de registres obligatoires, dépendent de la loi applicable et des statuts. L'enregistrement des réunions peut aussi être encadré. Vérifiez-les avant de modifier vos pratiques.

## 10.5 Explications détaillées

![Figure 10.1 : De la réunion au suivi des décisions](03_ILLUSTRATIONS/figures/fig_10_1.svg){#fig-10-1}

### Le cycle complet d'une réunion de gouvernance

| Étape | Ce qui se passe | Rôle de l'IA | Rôle du logiciel | Rôle humain |
|---|---|---|---|---|
| 1. Préparation de l'ordre du jour | Recensement des points, vérification des échéances statutaires | Proposer un projet d'ordre du jour à partir du registre des décisions et du calendrier | Calendrier, registre | Président et direction arrêtent l'ordre du jour |
| 2. Dossier de séance | Rassemblement des documents | Synthèses d'une page des rapports longs | Espace documentaire partagé | Vérification des synthèses par les auteurs des rapports |
| 3. Convocation | Envoi dans les délais statutaires | Néant | Messagerie, rappel automatique | Secrétaire |
| 4. Réunion | Débats et votes | Transcription (si consentement de tous) | Visioconférence, enregistreur | Président anime ; secrétaire prend des notes |
| 5. Projet de PV | Rédaction | Projet structuré à partir des notes ou de la transcription ; extraction des décisions | Traitement de texte | Secrétaire vérifie et corrige |
| 6. Relecture | Contrôle | Néant | Suivi des modifications | Président et membres concernés |
| 7. Adoption et signature | Approbation formelle | Néant | Signature (manuscrite ou électronique selon le droit applicable) | Organe compétent |
| 8. Registre des décisions | Mise à jour | Pré-remplissage des lignes à partir du PV adopté | Tableur ou base | Secrétaire valide |
| 9. Suivi | Rappels, avancement | Synthèse de l'état d'avancement | Rappels automatiques | Responsables de chaque décision |
| 10. Archivage | Conservation | Indexation (mots clés, résumé) | Gestion documentaire | Secrétaire |

Table: Tableau 10.1 : Explications détaillées

### Le procès-verbal : ce que l'IA peut faire… et ne doit pas faire

Un projet de PV généré par l'IA peut faire gagner plusieurs heures. Mais un PV est un **document juridique**. Il doit refléter fidèlement les décisions adoptées, les votes, les présents et représentés, le quorum, les éventuels conflits d'intérêts déclarés. Un assistant peut :

- structurer les notes selon le modèle de PV de l'organisation ;
- repérer les décisions, les votes et les actions ;
- signaler les informations manquantes (heure de clôture, résultat d'un vote) ;
- proposer une formulation neutre et concise.

Il ne doit pas :

- **inventer** un résultat de vote, une présence, une décision ;
- **interpréter** une discussion non conclusive comme une décision ;
- **reformuler** une décision au point d'en changer la portée.

> **🔎 À retenir** : Le PV adopté et signé fait foi ; le projet généré par l'IA n'est qu'un brouillon. Le secrétaire en est l'auteur et le garant.

### Transcription des réunions : précautions

L'enregistrement et la transcription automatique d'une réunion supposent : l'information préalable et le consentement des participants ; un outil autorisé pour des données orange (un CA évoque souvent des sujets confidentiels : personnel, litiges, finances) ; une durée de conservation courte de l'enregistrement (suppression après adoption du PV, sauf règle contraire) ; la possibilité de suspendre l'enregistrement pour les points confidentiels (huis clos, conflits d'intérêts, questions de personnel).

### Suivi des décisions et des mandats

Le **registre des décisions** (annexe 20 pour les recommandations, sur le même modèle) est l'outil central. Chaque ligne comporte : numéro, date de la réunion, organe, intitulé de la décision, responsable, échéance, état (à faire / en cours / réalisé / reporté / abandonné), commentaire, référence du document de preuve. Il est présenté à chaque réunion.

Le **registre des mandats** comporte : nom, fonction, date de début, durée, date d'échéance, organe qui renouvelle, et une alerte automatique trois mois avant l'échéance. C'est typiquement une automatisation classique (une formule de date et un rappel), pas de l'IA.

### Obligations institutionnelles

Les obligations institutionnelles (dépôt des comptes, déclarations aux autorités, renouvellement d'agréments, rapports annuels aux bailleurs, assemblées statutaires) sont rassemblées dans un **calendrier des obligations**. L'IA peut aider à extraire ces obligations des statuts, des conventions et des textes applicables, mais chaque obligation doit être vérifiée sur la source officielle par une personne compétente.

### Archivage et circulation de l'information

- Archivage : un dossier « 01_GOUVERNANCE » structuré par organe et par année ; PV signés en PDF ; règle de nommage (module 7).
- Circulation : après chaque réunion, une **note de synthèse** d'une page aux équipes (décisions qui les concernent), distincte du PV ; l'IA peut en préparer le projet à partir du PV adopté.

### L'assistant de gouvernance

Pour les organisations de niveau intermédiaire ou avancé, un **assistant de gouvernance** peut répondre à des questions comme : « Quelles décisions le CA a-t-il prises sur la politique de voyage depuis 2024 ? » ou « Quand expire le mandat de la trésorière ? ». Il s'appuie sur une base documentaire (statuts, règlement intérieur, PV adoptés, registres) via un dispositif RAG, avec citation des sources. Conditions : base documentaire propre (uniquement les versions adoptées) ; droits d'accès réservés aux administrateurs et à la direction ; réponses toujours sourcées et vérifiables.

### Continuité institutionnelle

Lors du renouvellement d'un président, d'un trésorier ou d'un directeur, un **dossier de passation** réduit la perte de mémoire : statuts, délégations, registres, calendrier des obligations, dossiers en cours, contacts clés, accès (transmis selon une procédure sécurisée). L'IA peut aider à produire une synthèse des dossiers en cours à partir des PV et du registre.

## 10.6 Application métier : de la réunion au suivi des décisions à Horizons Partagés

**A. Contexte.** CA de neuf membres bénévoles, quatre réunions par an ; secrétaire bénévole ; direction salariée.
**B. Problème.** Décisions non suivies ; PV adoptés tardivement ; mandats expirés.
**C. Symptômes.** PV adoptés avec deux mois de retard ; décisions sans responsable ; découverte tardive de mandats expirés.
**D. Causes profondes.** Pas de modèle de PV ; pas de registre des décisions ; pas de calendrier des mandats ; charge excessive pour une secrétaire bénévole.
**E. Processus actuel.** Notes manuscrites → rédaction en plusieurs semaines → adoption à la réunion suivante → classement.
**F. Points de faiblesse.** Aucune trace structurée des actions ; dépendance à une personne ; risque juridique sur la validité des décisions.
**G. Résultat recherché.** Projet de PV diffusé sous 5 jours ouvrables ; 100 % des décisions inscrites au registre avec responsable et échéance ; aucun mandat expiré non renouvelé.
**H. Pertinence de l'IA.** Forte pour la rédaction du projet de PV et l'extraction des décisions (texte, variabilité) ; inutile pour les alertes de mandats (règle simple).
**I. Alternatives sans IA.** Modèle de PV à compléter en séance ; registre tenu manuellement ; rappels de calendrier.
**J. Solution recommandée.** Modèle de PV + prise de notes structurée en séance + projet de PV assisté par l'IA + registre des décisions + rappels automatiques.
**K. Niveau.** Débutant à Intermédiaire.
**L. Outils.** Traitement de texte, tableur partagé, calendrier avec rappels ; assistant d'IA autorisé pour des données orange ; éventuellement outil de transcription validé.
**M. Étapes détaillées.**

1. Adopter un **modèle de PV** (en-tête, présents, représentés, excusés, quorum, ordre du jour, points traités avec « exposé, débat, décision, vote », actions, clôture).
2. Préparer l'**ordre du jour** avec la fiche P10.3, à partir du registre et du calendrier.
3. Pendant la séance, la secrétaire prend des **notes structurées** selon le modèle, en notant mot pour mot le texte des décisions et les résultats des votes.
4. Dans les 48 heures, elle soumet les notes à l'assistant avec la fiche P10.1 (outil autorisé pour données orange ; noms des personnes extérieures remplacés si nécessaire).
5. Elle **vérifie** le projet ligne par ligne contre ses notes, en particulier les décisions et les votes.
6. Le président relit ; le projet est diffusé aux membres sous 5 jours ouvrables.
7. Les décisions extraites (fiche P10.2) sont inscrites au **registre** après validation.
8. Des **rappels automatiques** sont programmés pour chaque échéance.
9. Le PV est **adopté** à la réunion suivante, signé et archivé.
10. Le registre des décisions est **présenté** en ouverture de chaque réunion.

**N. Prompts.** Fiches P10.1, P10.2, P10.3.
**O. Exemple de résultat.** Voir les fiches ci-dessous.
**P. Méthode de vérification.** Contrôle croisé notes ↔ projet de PV pour chaque décision et chaque vote ; vérification du quorum ; relecture par le président.
**Q. Contrôles humains.** Rédaction finale par la secrétaire ; relecture par le président ; adoption par l'organe ; validation des lignes du registre.
**R. Risques et précautions.** Décision mal retranscrite ; confidentialité des débats ; dépendance à l'outil. Précaution : le texte des décisions est toujours repris des notes, jamais de la reformulation de l'IA.
**S. Coûts et maintenance.** Niveau Débutant : temps de mise en place (une demi-journée) ; abonnement éventuel à une suite professionnelle. Maintenance : mise à jour du registre après chaque réunion.
**T. Indicateurs.** Délai de diffusion du projet de PV ; pourcentage de décisions avec responsable et échéance ; taux de décisions réalisées dans les délais ; nombre de mandats expirés non renouvelés (cible : 0).
**U. Amélioration continue.** Revue annuelle du modèle de PV et du registre ; questionnaire de satisfaction des administrateurs.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Modèle de PV, notes structurées, projet de PV assisté (données anonymisées ou outil validé), registre en tableur, rappels de calendrier | Traitement de texte, tableur, calendrier, assistant | Faibles | Saisie manuelle du registre |
| Intermédiaire | Transcription validée avec consentement, suite collaborative avec assistant intégré, registre partagé avec rappels automatiques, espace documentaire du CA avec droits restreints | Suite professionnelle, outil de transcription, plateforme d'automatisation | Abonnements | Paramétrage de la confidentialité |
| Avancé | Portail de gouvernance (convocations, votes, signatures électroniques selon le droit applicable), assistant de gouvernance RAG sur les documents adoptés, tableau de bord des décisions et des obligations | Logiciel de gestion de conseil, RAG | Licences, intégration | Coût ; vérification de la valeur juridique des signatures et votes électroniques |

Table: Tableau 10.2 : Application métier : de la réunion au suivi des décisions à Horizons Partagés

## 10.7 Prompts prêts à l'emploi

### Fiche P10.1 : Projet de procès-verbal à partir de notes

**A. Titre.** Projet de PV structuré et vérifiable.

**B. Objectif.** Transformer des notes de séance en projet de PV conforme au modèle de l'organisation, sans rien inventer.

**C. Contexte d'utilisation.** Secrétariat d'un CA, d'une AG, d'un comité ; dans les 48 heures suivant la réunion.

**D. Données nécessaires.** Modèle de PV ; liste des présents, représentés et excusés ; ordre du jour ; notes structurées ou transcription ; texte exact des décisions et résultats des votes.

**E. Prompt complet.**

```text
Contexte : je suis secrétaire de [ORGANE] de [NOM DE L'ASBL]. Je
prépare le projet de procès-verbal de la réunion du [DATE].
Tâche : rédige le projet de PV en suivant exactement le modèle fourni.
Données :
<modele>[MODÈLE DE PV]</modele>
<presences>[PRÉSENTS / REPRÉSENTÉS (avec mandataire) / EXCUSÉS]
</presences>
<ordre_du_jour>[ORDRE DU JOUR]</ordre_du_jour>
<notes>[NOTES STRUCTURÉES OU TRANSCRIPTION]</notes>
Règles impératives :
1. Pour chaque point : « Exposé » (2 à 4 phrases), « Débat »
   (principaux arguments, sans attribuer de propos à une personne sauf
   si les notes l'indiquent explicitement), « Décision » (reprendre
   MOT POUR MOT le texte de la décision figurant dans les notes),
   « Vote » (pour/contre/abstention tels que notés).
2. Si une décision, un vote, une heure ou un quorum ne figure pas dans
   les notes, écris [À COMPLÉTER] : n'invente rien.
3. Si une discussion n'a pas abouti à une décision, écris « Aucune
   décision n'a été prise sur ce point ».
4. Termine par un tableau « N° | Décision | Responsable | Échéance »
   en reprenant uniquement ce qui figure dans les notes ; [À
   COMPLÉTER] sinon.
5. Liste à part les incohérences repérées dans les notes.
Style : neutre, concis, au passé composé.
```

**F. Instructions d'utilisation.** Vérifiez que l'outil est autorisé pour des données orange ; si des points confidentiels ont été traités à huis clos, ne les soumettez pas et rédigez-les manuellement. Comparez le projet aux notes avant toute diffusion.

**G. Résultat attendu.** Un projet de PV complet au format de l'organisation, avec des marqueurs [À COMPLÉTER] là où l'information manque, un tableau des actions et une liste d'incohérences.

**H. Exemple d'application (illustratif).** Extrait de projet obtenu pour le point « Politique de voyage » :

> **Point 3 : Révision de la politique de voyage.**
> *Exposé.* La directrice a présenté les écarts constatés entre les frais de mission et les plafonds en vigueur, ainsi qu'un projet de politique révisée.
> *Débat.* Les administrateurs ont discuté du plafond d'hébergement dans les capitales et de la procédure d'autorisation préalable.
> *Décision.* « Le conseil adopte la politique de voyage révisée, sous réserve de l'ajout d'un plafond spécifique pour les capitales, à proposer par la direction avant le 30 avril. »
> *Vote.* Pour : 7 ; contre : 0 ; abstention : 1.
>
> Incohérence signalée : « Les notes indiquent 8 votants alors que la liste de présence mentionne 7 présents et 2 représentés (9 voix possibles). [À VÉRIFIER] »

**I. Méthode de vérification.** (1) Comparez le texte de chaque décision aux notes, caractère par caractère. (2) Vérifiez les votes et le quorum. (3) Traitez tous les [À COMPLÉTER] et incohérences. (4) Faites relire par le président.

**J. Précautions.** Ne pas soumettre les points à huis clos, les questions individuelles de personnel ni les informations sur des bénéficiaires identifiables. Supprimer l'enregistrement et la transcription après adoption, selon la règle fixée.

**K. Amélioration.** *V1* : « Fais un PV avec ces notes. » → l'outil invente une heure de clôture, reformule les décisions et attribue des propos. *V2* : la fiche ci-dessus. *Si le PV est trop long* : « Limite l'exposé et le débat de chaque point à 60 mots, sans toucher au texte des décisions. »

### Fiche P10.2 : Alimenter le registre des décisions

**A. Titre.** Extraction des décisions et actions d'un PV adopté.

**B. Objectif.** Produire les lignes du registre des décisions à partir d'un PV adopté.

**C. Contexte d'utilisation.** Après l'adoption d'un PV.

**D. Données nécessaires.** PV adopté ; colonnes du registre ; liste des fonctions (responsables possibles).

**E. Prompt complet.**

```text
Tâche : à partir du procès-verbal adopté ci-dessous, produis les lignes
à ajouter au registre des décisions.
Colonnes : N° | Date de réunion | Organe | Décision (texte exact) |
Type (adoption, mandat, action, information) | Responsable (fonction)
| Échéance (AAAA-MM-JJ) | État initial (« à faire ») | Référence
(point n° du PV).
Données : <pv>[PV ADOPTÉ]</pv>
Règles : reprends le texte exact des décisions ; si le responsable
ou l'échéance ne sont pas indiqués, écris « NON DÉFINI » (ne les
déduis pas). Produis le tableau au format CSV avec « ; » comme
séparateur.
```

**F. Instructions d'utilisation.** Collez le résultat dans le tableur du registre ; complétez les « NON DÉFINI » avec la direction ; programmez les rappels.

**G. Résultat attendu.** Lignes au format CSV, une par décision.

**H. Exemple d'application (illustratif).**

```text
2026-07;2026-03-18;CA;"Le conseil adopte la politique de voyage
révisée, sous réserve de l'ajout d'un plafond spécifique pour les
capitales, à proposer par la direction avant le 30 avril.";action;
Direction exécutive;2026-04-30;à faire;Point 3
```

**I. Méthode de vérification.** Nombre de lignes = nombre de décisions du PV ; textes identiques ; aucune échéance inventée.

**J. Précautions.** Le registre est un document orange ; droits d'accès limités au CA et à la direction.

**K. Amélioration.** « Ajoute une colonne "dépendances" indiquant si une décision dépend d'une autre décision du registre. »

### Fiche P10.3 : Préparer l'ordre du jour

**A. Titre.** Projet d'ordre du jour fondé sur le registre et le calendrier.

**B. Objectif.** Ne rien oublier : décisions à échéance, obligations statutaires, mandats, rapports attendus.

**C. Contexte d'utilisation.** Trois à quatre semaines avant une réunion.

**D. Données nécessaires.** Registre des décisions (extraits en cours) ; calendrier des obligations ; registre des mandats ; demandes reçues.

**E. Prompt complet.**

```text
Contexte : réunion de [ORGANE] de [NOM DE L'ASBL] prévue le [DATE],
durée [DURÉE].
Données :
<registre>[DÉCISIONS EN COURS OU À ÉCHÉANCE]</registre>
<obligations>[OBLIGATIONS DES 6 PROCHAINS MOIS]</obligations>
<mandats>[MANDATS EXPIRANT DANS LES 6 MOIS]</mandats>
<demandes>[POINTS DEMANDÉS PAR LES MEMBRES OU LA DIRECTION]</demandes>
Tâche : propose un ordre du jour.
Résultat attendu : tableau « N° | Point | Nature (pour décision /
pour information / pour débat) | Rapporteur (fonction) | Durée |
Documents à joindre | Source (registre, obligation, mandat,
demande) ». Puis liste des points écartés ou reportés avec la raison.
Règles : la durée totale ne doit pas dépasser [DURÉE] ; commence par
l'approbation du PV précédent et le suivi du registre ; place les
points pour décision avant les points pour information.
```

**F. Instructions d'utilisation.** Le président et la direction arrêtent l'ordre du jour définitif.

**G. Résultat attendu.** Un ordre du jour minuté, sourcé, avec la liste des documents à préparer.

**H. Exemple d'application (illustratif).** Le projet obtenu inscrit automatiquement « Renouvellement des mandats de deux administrateurs (échéance : 2026-06-30), pour décision », le point qui avait été oublié l'année précédente.

**I. Méthode de vérification.** Confrontez chaque point aux sources ; vérifiez les délais de convocation statutaires.

**J. Précautions.** Données orange.

**K. Amélioration.** « Pour chaque point pour décision, propose une formulation de projet de décision à soumettre au vote. »

## 10.8 Résultats attendus

PV diffusés rapidement et fidèles ; registre des décisions à jour ; mandats et obligations suivis ; information diffusée aux équipes ; mémoire de la gouvernance préservée.

## 10.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Le texte des décisions, les votes, le quorum et les présences sont vérifiés par le secrétaire sur ses notes. Le PV n'a de valeur qu'une fois adopté et signé par l'organe compétent. Aucune décision ne figure au registre sans validation humaine.

## 10.10 Risques et erreurs à éviter

- Diffuser un projet de PV généré sans relecture.
- Enregistrer une réunion sans le consentement de tous.
- Soumettre à un outil non validé les débats sur des personnes ou des litiges.
- Confondre note de synthèse aux équipes et PV officiel.
- Alimenter un assistant de gouvernance avec des projets non adoptés.

## 10.11 Exercice pratique

**Consigne (90 minutes).** À partir de notes fictives d'une réunion de 45 minutes (rédigez-les vous-même, avec trois décisions dont une sans échéance, et un vote incohérent) : (1) appliquez la fiche P10.1 ; (2) repérez si l'outil a correctement signalé l'échéance manquante et l'incohérence du vote ; (3) produisez les lignes du registre avec la fiche P10.2 ; (4) programmez les rappels dans votre calendrier.

**Éléments de correction.** Le projet de PV ne doit contenir aucune information absente des notes ; l'échéance manquante doit apparaître en [À COMPLÉTER] ou « NON DÉFINI » ; l'incohérence de vote doit être signalée. Si l'outil a comblé un manque, l'exercice démontre la nécessité de la vérification.

## 10.12 Synthèse

- Le cycle de gouvernance va de l'ordre du jour au suivi des décisions.
- L'IA prépare des projets (ordre du jour, PV, synthèses, lignes de registre) ; le secrétaire et l'organe en sont garants.
- Le texte des décisions et les votes ne sont jamais reformulés par l'IA.
- Les mandats et obligations relèvent d'automatisations simples (dates, rappels).
- Un assistant de gouvernance n'est fiable que sur une base documentaire de documents adoptés.

## 10.13 QCM : Module 10

**Q1.** (une seule réponse) Un projet de PV généré par l'IA :

a) fait foi dès sa génération.
b) est un brouillon dont le secrétaire est l'auteur et le garant.
c) peut être signé sans relecture s'il est bien rédigé.
d) remplace l'adoption par l'organe.

**Q2.** (une ou plusieurs réponses) Dans un projet de PV, l'IA ne doit pas :

a) inventer un résultat de vote.
b) reformuler une décision au point d'en changer la portée.
c) signaler une information manquante.
d) interpréter une discussion non conclusive comme une décision.

**Q3.** (une seule réponse) Le suivi de l'échéance des mandats relève principalement :

a) de l'IA générative.
b) d'un agent autonome.
c) d'une analyse prédictive.
d) d'une automatisation simple (dates et rappels).

**Q4.** (une ou plusieurs réponses) Une ligne du registre des décisions comporte :

a) le texte de la décision.
b) le responsable.
c) l'échéance.
d) l'avis personnel du secrétaire sur chaque administrateur.

**Q5.** (une seule réponse) Pour enregistrer et transcrire un CA, il faut d'abord :

a) acheter un micro.
b) informer les participants et recueillir leur consentement, avec un outil autorisé.
c) prévenir le bailleur.
d) rien, si la réunion est interne.

**Q6.** (une seule réponse) Un assistant de gouvernance RAG doit être alimenté par :

a) les seuls documents adoptés et à jour.
b) tous les brouillons disponibles.
c) les courriels personnels des administrateurs.
d) des documents trouvés sur internet.

**Q7.** (mise en situation, une seule réponse) Le projet de PV indique « 8 voix pour », alors que vos notes indiquent « 7 voix pour, 1 abstention ». Que faites-vous ?

a) Vous gardez la version de l'IA.
b) Vous supprimez le vote du PV.
c) Vous faites la moyenne.
d) Vous corrigez selon vos notes et vérifiez le décompte des voix.

**Q8.** (mise en situation, une seule réponse) Un point à huis clos a porté sur un litige avec un salarié. Comment le traiter ?

a) Soumettre les notes à l'assistant comme le reste.
b) Ne pas le mentionner dans le PV, même s'il y a eu décision.
c) Le rédiger manuellement, sans le soumettre à l'outil.
d) Le publier dans la note aux équipes.

**Q9.** (une seule réponse) La note de synthèse aux équipes après un CA :

a) remplace le PV.
b) est distincte du PV et ne reprend que ce qui concerne les équipes.
c) doit contenir les débats nominatifs.
d) est inutile.

**Q10.** (une ou plusieurs réponses) Indicateurs pertinents pour ce processus :

a) délai de diffusion du projet de PV.
b) pourcentage de décisions avec responsable et échéance.
c) nombre de mandats expirés non renouvelés.
d) nombre de pages des PV.

## 10.14 Corrigé détaillé : Module 10

**Q1 : b.** Seul le PV adopté et signé fait foi.

**Q2 : a, b, d.** Signaler une information manquante (c) est précisément ce qu'on attend de l'outil.

**Q3 : d.** Une formule de date et un rappel suffisent.

**Q4 : a, b, c.** Les avis personnels (d) n'ont pas leur place dans un registre.

**Q5 : b.** Consentement et outil autorisé sont des préalables.

**Q6 : a.** Sinon, l'assistant risque de citer des décisions non adoptées.

**Q7 : d.** Les notes de séance font référence ; le décompte doit être vérifié.

**Q8 : c.** Les informations confidentielles sur des personnes ne sont pas soumises à l'outil. La décision, si elle existe, doit figurer au PV selon les règles applicables (b est faux).

**Q9 : b.** La note aux équipes est un outil de communication, pas un document officiel.

**Q10 : a, b, c.** Le nombre de pages (d) ne mesure pas la qualité.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.


# Module 11 : Gestion des programmes et des projets {#h15}

## 11.1 Mise en situation

Dans trois villages où intervient Horizons Partagés, les agents de santé communautaires signalent une hausse des consultations pour diarrhées chez les jeunes enfants. La coordinatrice, Mariam, doit concevoir rapidement une intervention, la présenter à un bailleur, puis la suivre. Elle dispose d'un registre du centre de santé, de notes de réunions communautaires, d'une ancienne évaluation et de beaucoup de bonne volonté, mais de peu de temps.

Ce module suit Mariam pas à pas : du problème communautaire au cadre logique, au budget, aux indicateurs, puis au suivi et au rapport.

## 11.2 Problématique

La conception et le suivi de projets mobilisent énormément d'analyse et de rédaction : analyses de besoins, arbres à problèmes, cadres logiques, chronogrammes, budgets, plans de suivi-évaluation, rapports. Les équipes y consacrent un temps considérable, souvent au détriment du terrain. L'IA peut accélérer ces travaux, mais elle peut aussi produire des projets « hors sol », génériques, déconnectés des réalités et des voix des communautés.

## 11.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. structurer une analyse des besoins à partir de données de terrain ;
2. construire un arbre à problèmes et un arbre à objectifs avec l'appui de l'IA, validés par les acteurs ;
3. élaborer un cadre logique cohérent ;
4. planifier les activités et construire un budget de projet vérifiable ;
5. définir des indicateurs SMART et un plan de suivi-évaluation ;
6. exploiter des données de terrain et rédiger un rapport d'avancement fidèle ;
7. aborder la mesure d'impact avec prudence.

## 11.4 Notions et définitions

- **Analyse des besoins** : identification, avec les personnes concernées, des problèmes, de leurs causes et des capacités existantes.
- **Arbre à problèmes** : représentation d'un problème central, de ses causes (racines) et de ses effets (branches).
- **Arbre à objectifs** : transformation de l'arbre à problèmes en situations positives souhaitées.
- **Cadre logique** : matrice reliant objectif global, objectif spécifique, résultats et activités, avec indicateurs, sources de vérification et hypothèses.
- **Chaîne de résultats** : intrants → activités → extrants → résultats → impact.
- **Indicateur SMART** : spécifique, mesurable, atteignable, réaliste (ou pertinent) et temporellement défini.
- **Critères d'évaluation du CAD de l'OCDE** : pertinence, cohérence, efficacité, efficience, impact, viabilité (OCDE, 2019).

> **🔎 À retenir** : Les modèles de cadre logique, les formats de budget et les exigences de rapport varient selon les bailleurs. Utilisez toujours le modèle et le guide du bailleur concerné.

## 11.5 Explications détaillées

### De l'analyse des besoins à l'arbre à problèmes

Les sources d'une analyse des besoins sont multiples : données administratives (registres de santé, statistiques scolaires), enquêtes, entretiens, groupes de discussion, observations, évaluations antérieures. L'IA peut **organiser** ces sources : regrouper des retours par thème, résumer des rapports, proposer des causes possibles. Elle ne peut pas **remplacer** l'écoute des communautés : ce qu'elle propose est une hypothèse à discuter.

![Figure 11.1 : De l'arbre à problèmes à l'arbre à objectifs](03_ILLUSTRATIONS/figures/fig_11_1.svg){#fig-11-1}

### Le cadre logique

| | Logique d'intervention | Indicateurs | Sources de vérification | Hypothèses |
|---|---|---|---|---|
| **Objectif global** | Contribuer à la réduction de la morbidité infantile dans la zone | Incidence des diarrhées chez les < 5 ans | Registre du centre de santé | Néant |
| **Objectif spécifique** | Les ménages des 3 villages adoptent des pratiques d'eau, d'assainissement et d'hygiène sûres | % de ménages traitant l'eau de boisson ; % de ménages disposant de latrines fonctionnelles | Enquêtes de base et finale | Stabilité sécuritaire ; disponibilité des produits de traitement sur le marché local |
| **Résultat 1** | Les ménages traitent l'eau à domicile | Nb de ménages formés et équipés | Listes de distribution, rapports de séance | Acceptation culturelle du produit |
| **Résultat 2** | Les latrines familiales sont fonctionnelles | Nb de latrines réhabilitées et utilisées | Fiches de suivi, visites | Participation des ménages aux travaux |
| **Résultat 3** | Le lavage des mains aux moments clés est pratiqué | % de ménages disposant d'un dispositif de lavage avec savon | Observation par échantillon | Néant |
| **Activités** | 1.1 Séances de sensibilisation ; 1.2 Distribution de kits ; 2.1 Réhabilitation de latrines ; 3.1 Installation de dispositifs de lavage ; 3.2 Animations scolaires | Moyens : personnel, kits, matériaux | Budget, rapports financiers | Engagement des leaders communautaires |

Table: Tableau 11.1 : Explications détaillées

**Contrôles de cohérence d'un cadre logique :**

1. **Logique verticale** : si les activités sont réalisées et les hypothèses vérifiées, alors les résultats sont atteints ; si les résultats sont atteints, l'objectif spécifique l'est aussi.
2. **Indicateurs** : chaque niveau a au moins un indicateur mesurable, avec une valeur de référence et une cible.
3. **Sources** : chaque indicateur a une source réaliste et budgétée.
4. **Hypothèses** : extérieures au projet, importantes, ni certaines ni impossibles.

![Figure 11.2 : Chaîne de résultats et indicateurs](03_ILLUSTRATIONS/figures/fig_11_2.svg){#fig-11-2}

### Planification et calendrier

Le chronogramme découle des activités. Points de vigilance : saisons (pluies, récoltes, examens scolaires), fêtes et périodes de forte mobilité, délais d'achat, délais de recrutement, temps de démarrage. L'IA peut proposer une première séquence ; l'équipe de terrain la corrige selon le calendrier local.

### Le budget

Le budget traduit les activités en ressources. *Exemple (fictif) sur 12 mois :*

| Ligne | Calcul | Montant (UM) |
|---|---|---|
| 1. Personnel | Coordinateur : 12 mois × 1 200 ; 4 animateurs : 4 × 12 mois × 400 | 14 400 + 19 200 = **33 600** |
| 2. Activités | Kits : 800 ménages × 12 ; séances : 96 × 50 ; latrines : 40 × 350 | 9 600 + 4 800 + 14 000 = **28 400** |
| 3. Équipements | Matériel didactique 1 500 ; smartphones de collecte : 4 × 150 | 1 500 + 600 = **2 100** |
| 4. Suivi-évaluation | Enquêtes de base et finale : 2 × 2 500 | **5 000** |
| 5. Fonctionnement direct | Forfait | **3 000** |
| **Sous-total coûts directs** | 33 600 + 28 400 + 2 100 + 5 000 + 3 000 | **72 100** |
| 6. Coûts indirects | 7 % des coûts directs (taux à vérifier selon le bailleur) | **5 047** |
| **Total** | 72 100 + 5 047 | **77 147** |

Table: Tableau 11.2 : Explications détaillées

**Règles :** construire le budget dans un tableur avec des formules (quantité × coût unitaire × durée), jamais en saisissant des totaux à la main ; documenter chaque coût unitaire (devis, grille salariale, historique) ; vérifier l'éligibilité des dépenses et le taux de coûts indirects selon les règles du bailleur ; relier chaque ligne à une activité du cadre logique.

> **🛑 Contrôle humain obligatoire** : Les coûts unitaires proposés par une IA ne sont jamais fiables : ils doivent provenir de devis, de grilles internes ou de données historiques de l'organisation.

### Indicateurs et plan de suivi-évaluation

Un plan de suivi-évaluation précise, pour chaque indicateur : définition exacte, méthode de calcul, valeur de référence, cible, source, fréquence de collecte, responsable, mode de désagrégation (sexe, âge, village), et utilisation prévue.

*Exemple :*

| Indicateur | Définition | Référence | Cible | Source | Fréquence | Responsable |
|---|---|---|---|---|---|---|
| % de ménages traitant l'eau de boisson | Ménages dont l'eau stockée présente un traitement vérifié lors de la visite / ménages visités | 18 % (enquête de base) | 60 % | Enquête par échantillon | Base, mi-parcours, fin | Chargée S&E |

Table: Tableau 11.3 : Explications détaillées

### Données de terrain

Les formulaires mobiles (fonctionnant hors ligne) réduisent les erreurs de saisie et les délais de transmission. L'IA intervient en aval : contrôles de cohérence (valeurs aberrantes, doublons), synthèse des observations qualitatives, regroupement thématique des commentaires, préparation de tableaux pour le rapport. Les données personnelles des ménages restent dans l'outil de collecte sécurisé ; seules des données agrégées ou pseudonymisées sont analysées avec des outils d'IA externes.

### Mesure d'impact

L'impact (changement durable au niveau de la population) est influencé par de nombreux facteurs hors du projet. Attribuer une baisse des diarrhées au seul projet suppose des méthodes rigoureuses (groupe de comparaison, séries temporelles, analyse de contribution). L'IA peut aider à **explorer** les données, à **proposer** des méthodes et à **rédiger** une note méthodologique ; elle ne peut pas transformer une corrélation en preuve d'impact. Les critères du CAD de l'OCDE (pertinence, cohérence, efficacité, efficience, impact, viabilité) fournissent une grille d'analyse largement utilisée (OCDE, 2019, 2021).

### Rapports

Un rapport d'avancement fidèle compare prévu et réalisé, explique les écarts, présente les difficultés et les mesures correctives, et s'appuie sur des données vérifiables. L'IA est très utile pour structurer et rédiger à partir des données et des notes fournies ; le risque principal est l'embellissement ou l'invention de résultats.

## 11.6 Application métier : de l'alerte communautaire au projet financé

**A. Contexte.** Trois villages, hausse des diarrhées infantiles, équipe de santé communautaire en place.
**B. Problème.** Besoin de concevoir et de suivre une intervention rapidement et rigoureusement.
**C. Symptômes.** Hausse des consultations ; rapports antérieurs génériques ; indicateurs mal définis dans les projets passés.
**D. Causes profondes (côté organisation).** Pas de modèle interne de conception ; données de terrain dispersées ; charge rédactionnelle élevée.
**E. Processus actuel.** Rédaction intégrale par la coordinatrice, en soirée, à partir de documents épars.
**F. Faiblesses.** Faible participation communautaire formalisée ; budget construit à la main ; indicateurs sans référence.
**G. Résultat recherché.** Proposition de projet de qualité en trois semaines, cadre logique cohérent, budget vérifiable, plan de S&E opérationnel.
**H. Pertinence de l'IA.** Forte pour structurer, synthétiser et rédiger ; nulle pour décider des priorités à la place des communautés.
**I. Alternatives sans IA.** Modèles internes de cadre logique et de budget ; ateliers participatifs.
**J. Solution recommandée.** Combinaison : atelier communautaire + modèles internes + assistance de l'IA pour la structuration et la rédaction + vérification par l'équipe.
**K. Niveau.** Débutant à Intermédiaire.
**L. Outils.** Assistant (données vertes et orange autorisées), tableur budgétaire, formulaires mobiles hors ligne, traitement de texte.
**M. Étapes détaillées.**

1. Rassembler les données : extraits **agrégés** du registre de santé, notes des réunions communautaires (anonymisées), évaluation antérieure.
2. Fiche P11.1 : premier arbre à problèmes à partir de ces sources.
3. **Atelier communautaire** (demi-journée) : présentation de l'arbre comme hypothèse, corrections, ajout des causes oubliées, priorisation.
4. Transformation en arbre à objectifs et choix des stratégies avec l'équipe.
5. Fiche P11.2 : projet de cadre logique à partir de l'arbre validé.
6. Vérification de la logique verticale et des indicateurs par la chargée de S&E.
7. Construction du budget dans le tableur modèle (quantités × coûts unitaires documentés).
8. Plan de S&E et formulaires de collecte mobiles.
9. Rédaction de la proposition (voir module 15).
10. Pendant la mise en œuvre : collecte mensuelle, contrôles de cohérence, rapport trimestriel avec la fiche P11.3.

**N. Prompts.** P11.1, P11.2, P11.3.
**O. Exemple de résultat.** Arbre (figure 11.1), cadre logique et budget ci-dessus.
**P. Vérification.** Validation communautaire de l'arbre ; contrôle de la logique verticale ; recalcul du budget ; vérification des sources des coûts.
**Q. Contrôles humains.** Choix des priorités et des stratégies par l'équipe et les communautés ; validation du budget par le responsable financier ; signature de la proposition par la direction.
**R. Risques.** Projet générique ; coûts inventés ; indicateurs non mesurables ; données personnelles dans des outils non validés.
**S. Coûts et maintenance.** Temps de l'atelier, outils existants ; abonnement éventuel.
**T. Indicateurs.** Délai de production de la proposition ; nombre d'incohérences relevées par le bailleur ; ponctualité des rapports ; taux de complétude des données de suivi.
**U. Amélioration continue.** Capitaliser les cadres logiques et budgets validés dans une bibliothèque interne réutilisable.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Assistant pour arbres, cadres logiques et rapports ; tableur budgétaire modèle ; collecte papier ou formulaire simple | Assistant, tableur, formulaire | Faibles | Saisie manuelle des données de suivi |
| Intermédiaire | Formulaires mobiles hors ligne reliés à une base ; tableaux de bord ; synthèse assistée des données qualitatives ; bibliothèque de modèles | Outil de collecte mobile, tableau de bord, suite professionnelle | Abonnements | Formation des agents |
| Avancé | Système d'information de S&E intégré (indicateurs, cibles, données désagrégées), alimentant automatiquement les rapports, avec assistant RAG sur l'historique des projets | Plateforme de S&E, API, RAG | Élevés | Gouvernance des données, coûts récurrents |

Table: Tableau 11.4 : Application métier : de l'alerte communautaire au projet financé

## 11.7 Prompts prêts à l'emploi

### Fiche P11.1 : Projet d'arbre à problèmes à partir de données de terrain

**A. Titre.** Arbre à problèmes à valider avec les communautés.

**B. Objectif.** Organiser les données disponibles en un arbre à problèmes provisoire, servant de support de discussion.

**C. Contexte d'utilisation.** Phase d'identification d'un projet.

**D. Données nécessaires.** Données agrégées ; notes anonymisées de réunions ; extraits d'évaluations.

**E. Prompt complet.**

```text
Contexte : [NOM DE L'ASBL] intervient en [SECTEUR] dans [TYPE DE ZONE,
sans nom de village si sensible]. Problème signalé : [PROBLÈME].
Données : <donnees>[CHIFFRES AGRÉGÉS, NOTES ANONYMISÉES, EXTRAITS
D'ÉVALUATION]</donnees>
Tâche : propose un arbre à problèmes PROVISOIRE.
Résultat attendu :
1. Problème central reformulé (une phrase, situation négative précise).
2. Causes directes et causes profondes, sur 2 à 3 niveaux, chacune
   suivie de sa source : [DONNÉES], [NOTES] ou [HYPOTHÈSE À VÉRIFIER].
3. Effets directs et indirects, avec leurs sources.
4. Les 8 questions à poser lors de l'atelier communautaire pour
   valider ou corriger l'arbre.
Limites : n'invente aucune statistique ; distingue les causes
documentées des hypothèses ; évite les explications qui
culpabilisent les populations.
```

**F. Instructions d'utilisation.** Imprimez l'arbre en grand format pour l'atelier ; présentez-le comme une hypothèse.

**G. Résultat attendu.** Un arbre hiérarchisé et sourcé et un guide de questions.

**H. Exemple d'application (illustratif).** L'arbre proposé pour les trois villages identifie « eau de boisson non traitée » [DONNÉES], « peu de latrines fonctionnelles » [NOTES] et « coût des produits de traitement » [HYPOTHÈSE À VÉRIFIER]. Lors de l'atelier, les femmes du village B ajoutent une cause absente : « les jerricans de stockage sont partagés entre plusieurs ménages et rarement nettoyés ».

**I. Méthode de vérification.** Chaque cause marquée [DONNÉES] doit renvoyer à un chiffre réel ; les hypothèses sont confirmées ou rejetées en atelier.

**J. Précautions.** Ne pas inclure de noms de personnes ni de lieux sensibles. Veiller à ce que la formulation n'attribue pas le problème à la « négligence » des familles.

**K. Amélioration.** « Ajoute une colonne indiquant, pour chaque cause, si l'ASBL a la capacité d'agir dessus (oui/partiellement/non). »

### Fiche P11.2 : Projet de cadre logique

**A. Titre.** Cadre logique à partir d'un arbre à objectifs validé.

**B. Objectif.** Produire un cadre logique cohérent, avec indicateurs SMART et hypothèses, conforme au modèle du bailleur.

**C. Contexte d'utilisation.** Formulation d'un projet.

**D. Données nécessaires.** Arbre à objectifs validé ; stratégie retenue ; modèle de cadre logique du bailleur ; données de référence disponibles.

**E. Prompt complet.**

```text
Contexte : formulation d'un projet de [DURÉE] pour [BAILLEUR, modèle
joint]. Arbre à objectifs validé : <arbre>[ARBRE]</arbre>
Stratégies retenues : [STRATÉGIES]. Données de référence disponibles :
[DONNÉES].
Tâche : propose un cadre logique respectant le modèle fourni
<modele>[MODÈLE DU BAILLEUR]</modele>.
Exigences :
1. Logique verticale explicite (si… alors…).
2. Pour chaque niveau, 1 à 3 indicateurs SMART : définition, valeur de
   référence (écrire « à établir » si elle n'existe pas), cible,
   échéance, désagrégation.
3. Sources de vérification réalistes et coût de collecte à prévoir.
4. Hypothèses externes, ni certaines ni impossibles.
5. Ensuite, liste les faiblesses de ce cadre logique (indicateurs
   difficiles à mesurer, hypothèses fragiles, liens logiques faibles).
Limites : n'invente pas de valeurs de référence ni de cibles chiffrées
sans les signaler comme « proposition à valider ».
```

**F. Instructions d'utilisation.** Joignez le modèle et le guide du bailleur ; faites valider les cibles par l'équipe.

**G. Résultat attendu.** Un cadre logique complet et une autocritique.

**H. Exemple d'application (illustratif).** Le cadre obtenu correspond au tableau de la section 11.5 ; l'autocritique relève que l'indicateur d'impact « incidence des diarrhées » dépend fortement de la qualité de l'enregistrement au centre de santé et propose un indicateur complémentaire d'enquête.

**I. Méthode de vérification.** Lecture « si… alors… » de bas en haut ; vérification que chaque indicateur est mesurable avec les moyens budgétés ; comparaison au guide du bailleur.

**J. Précautions.** Données vertes ou orange.

**K. Amélioration.** « Réécris les indicateurs pour qu'ils soient désagrégés par sexe et par tranche d'âge, et propose un indicateur qualitatif. »

### Fiche P11.3 : Rapport d'avancement fidèle

**A. Titre.** Rapport trimestriel fondé sur les données.

**B. Objectif.** Rédiger un rapport d'avancement qui compare prévu et réalisé et explique les écarts, sans embellissement.

**C. Contexte d'utilisation.** Rapports périodiques aux bailleurs ou à la direction.

**D. Données nécessaires.** Tableau des indicateurs (prévu/réalisé), état d'avancement des activités, notes de terrain anonymisées, état d'exécution budgétaire, modèle de rapport.

**E. Prompt complet.**

```text
Contexte : rapport trimestriel n° [N] du projet [NOM], pour [BAILLEUR].
Modèle : <modele>[MODÈLE]</modele>
Données :
<indicateurs>[TABLEAU PRÉVU/RÉALISÉ]</indicateurs>
<activites>[ÉTAT D'AVANCEMENT]</activites>
<terrain>[NOTES ANONYMISÉES]</terrain>
<budget>[TAUX D'EXÉCUTION PAR LIGNE]</budget>
Tâche : rédige le rapport selon le modèle.
Règles :
1. Chaque chiffre cité doit provenir des données fournies.
2. Pour tout écart supérieur à [10] % entre prévu et réalisé,
   présente l'écart, ses causes (selon les notes) et les mesures
   correctives ; si la cause n'est pas documentée, écris
   [CAUSE À PRÉCISER].
3. Présente les difficultés de façon factuelle, sans les minimiser.
4. Termine par la liste des chiffres utilisés et leur source.
```

**F. Instructions d'utilisation.** Préparez les tableaux dans le tableur ; transmettez des taux déjà calculés.

**G. Résultat attendu.** Un rapport structuré, des écarts expliqués, une table de traçabilité des chiffres.

**H. Exemple d'application (illustratif).** Le rapport signale : « Latrines réhabilitées : 12 sur 20 prévues au trimestre (60 %). Écart dû au retard de livraison du ciment (notes du 14/08). Mesure corrective : achat local complémentaire autorisé par la direction le 20/08. »

**I. Méthode de vérification.** Pointage de chaque chiffre avec la table de traçabilité ; relecture par la chargée de S&E et par le responsable financier pour les données budgétaires.

**J. Précautions.** Aucune donnée individuelle de bénéficiaire.

**K. Amélioration.** « Rédige une version de 300 mots pour la newsletter, sans données sensibles et en citant uniquement des résultats vérifiés. »

## 11.8 Résultats attendus

Propositions plus rapides et plus cohérentes, construites avec les communautés ; budgets vérifiables ; plans de S&E opérationnels ; rapports fidèles et ponctuels.

## 11.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Les priorités d'intervention sont définies avec les communautés et l'équipe ; les coûts unitaires proviennent de sources documentées ; chaque chiffre d'un rapport est pointé avec sa source ; la proposition est validée par la direction et le responsable financier.

## 11.10 Risques et erreurs à éviter

- Projets « copier-coller » génériques produits par l'IA.
- Cibles irréalistes ou valeurs de référence inventées.
- Budgets saisis à la main, sans formules ni justification.
- Confusion entre extrants (ce que l'on produit) et résultats (ce qui change).
- Prétendre à un impact sans méthode d'attribution.
- Analyse de données individuelles dans des outils non autorisés.

## 11.11 Exercice pratique

**Consigne (3 heures).** À partir d'un problème réel de votre zone d'intervention : (1) appliquez P11.1 ; (2) organisez une discussion de validation (même courte, avec deux collègues de terrain) ; (3) appliquez P11.2 ; (4) construisez un budget de six lignes dans un tableur avec formules ; (5) rédigez la fiche d'un indicateur complète.

**Éléments de correction.** L'arbre distingue causes documentées et hypothèses ; la validation modifie au moins un élément ; la logique verticale est vérifiable ; le budget ne contient aucun total saisi à la main ; l'indicateur comporte définition, référence, cible, source, fréquence, responsable et désagrégation.

## 11.12 Synthèse

- L'IA organise les données et propose des structures ; les communautés et l'équipe valident.
- Le cadre logique doit être cohérent verticalement, avec des indicateurs mesurables et des hypothèses externes.
- Le budget se construit au tableur, avec des coûts documentés.
- Les rapports sont fidèles : chaque chiffre est traçable, chaque écart expliqué.
- L'impact se mesure avec prudence et méthode.

## 11.13 QCM : Module 11

**Q1.** (une seule réponse) Dans un cadre logique, les hypothèses sont :

a) des activités du projet.
b) des indicateurs.
c) des conditions externes importantes, ni certaines ni impossibles.
d) des dépenses.

**Q2.** (une seule réponse) « Nombre de ménages formés » est un indicateur :

a) d'impact.
b) d'extrant.
c) d'intrant.
d) d'hypothèse.

**Q3.** (une ou plusieurs réponses) Un indicateur SMART est :

a) spécifique.
b) mesurable.
c) temporellement défini.
d) formulé de manière vague pour laisser de la souplesse.

**Q4.** (une seule réponse) Les six critères d'évaluation du CAD de l'OCDE sont :

a) coût, délai, qualité, risque, impact, visibilité.
b) pertinence, rapidité, efficacité, conformité, impact, notoriété.
c) efficience, rentabilité, croissance, impact, visibilité, cohérence.
d) pertinence, cohérence, efficacité, efficience, impact, viabilité.

**Q5.** (une seule réponse) Dans l'exemple de budget, les coûts indirects à 7 % s'élèvent à :

a) 5 400 UM
b) 7 210 UM
c) 5 047 UM
d) 72 100 UM

**Q6.** (une ou plusieurs réponses) Pour construire un budget fiable, il faut :

a) utiliser des formules (quantité × coût unitaire × durée).
b) documenter les coûts unitaires.
c) reprendre les coûts unitaires proposés par l'IA.
d) vérifier l'éligibilité selon les règles du bailleur.

**Q7.** (mise en situation, une seule réponse) L'IA propose comme cause « le manque d'hygiène des mères ». Que faites-vous ?

a) Vous la reformulez de façon factuelle et non culpabilisante et la soumettez comme hypothèse à l'atelier.
b) Vous la gardez telle quelle.
c) Vous la retirez sans discussion.
d) Vous l'ajoutez aux effets.

**Q8.** (mise en situation, une seule réponse) Le rapport généré mentionne « 85 % de satisfaction des bénéficiaires », chiffre absent de vos données. Que faites-vous ?

a) Vous le gardez car il est plausible.
b) Vous l'arrondissez à 80 %.
c) Vous demandez à l'IA sa source et la croyez.
d) Vous le supprimez : tout chiffre doit provenir des données fournies.

**Q9.** (une seule réponse) Une baisse des diarrhées observée pendant le projet :

a) prouve l'impact du projet.
b) doit être ignorée.
c) doit être analysée avec une méthode d'attribution ou de contribution avant toute conclusion.
d) prouve que le projet a échoué.

**Q10.** (une ou plusieurs réponses) Quelles données peuvent être soumises à un assistant d'IA externe non spécifiquement validé ?

a) Statistiques agrégées publiées.
b) Liste nominative des ménages visités.
c) Notes de terrain anonymisées, si la politique de l'ASBL l'autorise.
d) Modèle de cadre logique du bailleur, s'il est public.

## 11.14 Corrigé détaillé : Module 11

**Q1 : c.** Les hypothèses sont extérieures au contrôle du projet.

**Q2 : b.** C'est un produit direct des activités.

**Q3 : a, b, c.** Un indicateur vague (d) n'est pas mesurable.

**Q4 : d.** Ce sont les six critères révisés en 2019.

**Q5 : c.** 72 100 × 0,07 = 5 047.

**Q6 : a, b, d.** Les coûts proposés par l'IA (c) ne sont pas fiables.

**Q7 : a.** Une formulation culpabilisante est à la fois injuste et contre-productive ; la cause éventuelle (par exemple « accès limité au savon et à l'eau aux moments clés ») est discutée en atelier.

**Q8 : d.** Un chiffre non traçable est une hallucination potentielle.

**Q9 : c.** Corrélation n'est pas causalité.

**Q10 : a, c, d.** La liste nominative (b) est rouge. Les notes anonymisées relèvent de la politique de l'organisation (souvent orange) : à vérifier.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- OCDE, Réseau du CAD sur l'évaluation du développement. (2019). *Better Criteria for Better Evaluation: Revised Evaluation Criteria Definitions and Principles for Use*.
- OCDE. (2021). *Applying Evaluation Criteria Thoughtfully*. Éditions OCDE.
- Project Management Institute. (2025). *A Guide to the Project Management Body of Knowledge (PMBOK® Guide)* (8e éd.).


# Module 12 : Comptabilité, gestion financière et budgétaire {#h16}

## 12.1 Mise en situation

Fin mars, à Horizons Partagés. Esther, l'unique comptable, a devant elle 340 pièces du mois : factures papier, photos de reçus envoyées par messagerie depuis les bureaux de terrain, relevés bancaires en PDF, états de caisse manuscrits. Elle doit tout saisir, imputer à l'un des cinq bailleurs et à la bonne ligne budgétaire, rapprocher la banque, mettre à jour le suivi budgétaire et préparer, pour le 15 avril, deux rapports financiers dans deux formats différents. L'auditeur arrive en juin.

Ibrahim, le responsable financier, a lu qu'« il existe des outils d'IA qui traitent les factures automatiquement ». Il se demande ce que cela veut dire concrètement, ce qu'il faut acheter, ce qui changera pour Esther, et surtout ce qui restera sous leur contrôle.

## 12.2 Problématique

La fonction financière d'une ASBL combine trois exigences : **exactitude** (chaque écriture est juste et justifiée), **traçabilité** (chaque montant peut être relié à une pièce et à une autorisation) et **redevabilité multiple** (bailleurs, organes de gouvernance, autorités, auditeurs, public). Elle est aussi l'une des plus chargées en tâches répétitives : réception, saisie, imputation, rapprochements, consolidation, mise en forme. L'IA peut alléger fortement ces tâches, à condition de ne jamais affaiblir le contrôle interne ni la piste d'audit.

## 12.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. organiser la fonction comptable et la gestion des pièces justificatives pour la rendre compatible avec l'automatisation ;
2. décrire, étape par étape, le traitement assisté d'une facture, de sa réception à l'archivage, en distinguant le rôle de l'IA, du logiciel et du professionnel ;
3. mettre en œuvre une extraction de données et une imputation assistées, avec leurs contrôles ;
4. réaliser et contrôler un rapprochement bancaire et un suivi de caisse ;
5. suivre un budget par projet et par bailleur, distinguer fonds affectés et non affectés, et analyser les écarts ;
6. préparer la trésorerie, le reporting et les audits ;
7. situer les référentiels comptables applicables.

## 12.4 Notions et définitions

- **Pièce justificative** : document qui prouve la réalité et le montant d'une opération (facture, reçu, contrat, bon de livraison, état de paie).
- **Imputation comptable** : affectation d'une opération à un compte du plan comptable.
- **Imputation analytique ou budgétaire** : affectation d'une opération à un projet, un bailleur, une ligne budgétaire, une activité.
- **Écriture comptable** : enregistrement d'une opération au débit et au crédit de comptes.
- **Rapprochement bancaire** : explication des écarts entre le solde comptable du compte bancaire et le solde du relevé.
- **Fonds affectés (ou restreints)** : ressources dont l'utilisation est limitée par le donateur à un objet, une période ou un projet.
- **Fonds non affectés** : ressources utilisables librement pour la mission (cotisations, dons non fléchés, certaines subventions de fonctionnement).
- **Piste d'audit** : capacité à remonter de chaque montant des états financiers jusqu'à la pièce et à l'autorisation, et inversement.
- **Seuil de confiance** : niveau de certitude au-dessous duquel une proposition de l'IA est automatiquement soumise à un examen renforcé.

> **⚖️ Adaptation réglementaire** : Il n'existe pas de référentiel comptable universel pour les organisations à but non lucratif. Selon les pays, s'appliquent un plan comptable national, un référentiel spécifique aux entités à but non lucratif ou aux associations, des règles particulières (par exemple, à titre d'illustration et à vérifier selon votre situation : le système comptable des entités à but non lucratif dans l'espace OHADA, le règlement de l'ANC applicable aux personnes morales de droit privé à but non lucratif en France, le *Charities SORP* au Royaume-Uni, les normes du FASB pour les *not-for-profit entities* aux États-Unis). En octobre 2025, un référentiel international volontaire dédié, l'*International Non-Profit Accounting Standard* (INPAS), a été lancé à l'issue du projet IFR4NPO ; il ne s'impose que s'il est adopté par une juridiction ou exigé par un bailleur. Les numéros de comptes cités dans ce module sont donc des **exemples** : utilisez votre plan comptable.

## 12.5 Explications détaillées

### Organisation comptable : les préalables à toute automatisation

Avant d'automatiser, quatre fondations doivent être en place :

1. **Un plan comptable et un plan analytique** stables : comptes, codes projets, codes bailleurs, lignes budgétaires, avec une **table de correspondance** entre les lignes du budget de chaque bailleur et vos comptes.
2. **Un manuel de procédures financières** à jour : seuils d'autorisation, circuit de validation, pièces exigées par type de dépense.
3. **Une séparation des tâches** : la personne qui saisit n'est pas celle qui approuve le paiement ; celle qui tient la caisse n'est pas celle qui la contrôle.
4. **Un plan de classement** des pièces (module 7), numérique et papier.

### Le traitement d'une facture en 14 étapes

![Figure 12.1 : Traitement d'une facture en 14 étapes : qui fait quoi ?](03_ILLUSTRATIONS/figures/fig_12_1.svg){#fig-12-1}

Suivons une facture réelle (fictive) d'un bout à l'autre.

*La pièce :* facture n° F-2026-0412 de « Papeterie du Centre », datée du 12 mars 2026, adressée à la Fondation Horizons Partagés : 40 rames de papier à 6,50 UM = 260 UM ; 20 cartouches d'encre à 22,00 UM = 440 UM ; **total 700 UM** (l'organisation n'est pas assujettie à une taxe sur la valeur ajoutée dans cet exemple). Référence du bon de commande : BC-2026-077. Matériel destiné aux sessions de formation des agents de santé du projet PRJ-SANTE-07.

**Étape 1 : Réception.** La facture arrive par courriel au bureau de terrain.
*Logiciel :* une adresse électronique dédiée (par exemple factures@…) centralise toutes les factures. *Humain :* les factures remises en main propre sont numérisées le jour même. *Règle :* aucune facture ne circule en dehors de ce canal.

**Étape 2 : Numérisation ou photographie.** Le PDF est conservé tel quel ; une facture papier est scannée ou photographiée avec une application de numérisation (document à plat, lumière suffisante, quatre coins visibles).
*Contrôle :* lisibilité de tous les montants avant envoi.

**Étape 3 : Extraction des informations.**
*IA :* un outil d'extraction (OCR et modèle d'extraction) lit la pièce et propose les champs : fournisseur, numéro, date, montant total, lignes (désignation, quantité, prix unitaire, montant), référence du bon de commande, coordonnées bancaires éventuelles. Il associe à chaque champ un niveau de confiance.
*Logiciel :* les champs extraits sont stockés dans un enregistrement relié à l'image de la pièce.

**Étape 4 : Contrôle des données extraites.**
*Logiciel :* contrôles automatiques simples : somme des lignes = total (260 + 440 = 700 ✓) ; date plausible ; fournisseur existant dans le fichier fournisseurs ; numéro de facture non déjà enregistré pour ce fournisseur.
*Humain :* l'assistante administrative compare les champs à faible confiance avec l'image (ici, le « 6,50 » a été lu « 6,60 » avec une confiance de 71 % : elle corrige). Toute modification des **coordonnées bancaires** d'un fournisseur est bloquée et transmise au responsable financier (risque de fraude au changement de RIB).

**Étape 5 : Identification de la nature de la dépense.**
*IA :* à partir des libellés (« rames de papier », « cartouches d'encre ») et de l'historique, le système propose la nature « fournitures de bureau et consommables de formation ».

**Étape 6 : Proposition d'imputation.**
*IA :* proposition d'imputation comptable (compte de charges « Fournitures de bureau » de votre plan comptable) et analytique (projet PRJ-SANTE-07, activité 1.1 « Sessions de formation », ligne budgétaire 2 « Activités »), en s'appuyant sur la référence du bon de commande BC-2026-077, qui portait déjà ces codes. Confiance : 94 %.

**Étape 7 : Vérification que le compte proposé est approprié.**
*Humain :* la comptable vérifie : la nature de la dépense correspond-elle au compte ? Le projet et la ligne correspondent-ils au bon de commande approuvé ? La dépense est-elle éligible selon la convention du bailleur (période, nature, plafond) ? *Règle :* toute proposition avec une confiance inférieure au seuil (par exemple 85 %) ou concernant un compte sensible (immobilisations, salaires, avances) est examinée ligne par ligne.

**Étape 8 : Rapprochement avec le budget concerné.**
*Logiciel :* le système calcule le disponible de la ligne : budget annuel de la ligne 2 du projet = 28 400 UM ; engagé et réalisé à date = 19 650 UM ; disponible avant cette facture = 8 750 UM ; après = 8 050 UM. Aucun dépassement.
*Logiciel :* rapprochement à trois voies : commande BC-2026-077 (700 UM), bon de livraison signé (40 rames et 20 cartouches reçues), facture (700 UM) : concordance.

**Étape 9 : Détection d'anomalies.**
*IA et règles :* le système signale : « Une facture du même fournisseur, d'un montant identique (700 UM), numéro F-2026-0411, a été enregistrée le 26 février. Doublon possible. »
*Humain :* la comptable vérifie : les deux factures correspondent à deux commandes distinctes (BC-2026-061 et BC-2026-077), deux livraisons signées. Ce n'est pas un doublon. Elle consigne l'explication dans le commentaire de l'alerte.

**Étape 10 : Soumission au responsable habilité.**
*Logiciel :* le workflow transmet automatiquement la dépense au responsable habilité selon le seuil (ici, moins de 1 000 UM : coordinatrice du projet) avec la pièce, la proposition d'imputation, le contrôle budgétaire et les alertes traitées.
*Humain :* la coordinatrice approuve dans l'outil. L'approbation est horodatée et nominative.

**Étape 11 : Validation et enregistrement de l'écriture.**
*Logiciel :* l'écriture est générée (débit du compte de charges « Fournitures de bureau » 700 UM ; crédit du compte fournisseur « Papeterie du Centre » 700 UM ; axes analytiques PRJ-SANTE-07 / 1.1 / ligne 2).
*Humain :* la comptable valide l'écriture. Une écriture n'est jamais comptabilisée sans validation humaine. Au paiement, une seconde écriture soldera le compte fournisseur par le compte bancaire, après approbation du paiement selon la procédure.

**Étape 12 : Actualisation des tableaux de bord et du suivi budgétaire.**
*Logiciel :* le tableau de bord du projet est mis à jour (exécution de la ligne 2 : 20 350 / 28 400, soit 71,7 %).

**Étape 13 : Conservation des pièces et de la piste d'audit.**
*Logiciel :* la pièce est archivée sous le nom `2026-03-12_FACT_PapeterieDuCentre_F-2026-0412.pdf`, liée à l'écriture, avec l'historique : qui a extrait, corrigé, proposé, approuvé, validé, et quand. La facture papier d'origine est classée selon les règles de conservation applicables.

**Étape 14 : Traitement des erreurs et cas exceptionnels.**
*Humain :* une procédure écrite couvre : pièce illisible (demande d'un duplicata) ; facture sans bon de commande (régularisation selon la procédure, signalement) ; dépense inéligible (réimputation sur fonds non affectés, après décision) ; avoir ou annulation ; facture en devise étrangère (taux de conversion selon la politique de l'organisation) ; erreur d'imputation découverte après clôture (écriture de correction documentée, jamais de suppression).

| Étape | IA | Logiciel | Professionnel |
|---|---|---|---|
| 1. Réception | Néant | Boîte dédiée | Numérise les pièces papier |
| 2. Numérisation | Néant | Application de numérisation | Vérifie la lisibilité |
| 3. Extraction | Lit et propose les champs, avec confiance | Stocke champs + image | Néant |
| 4. Contrôle des données | Néant | Contrôles arithmétiques et de cohérence | Corrige les champs à faible confiance ; bloque les changements de RIB |
| 5. Nature | Propose la nature | Néant | Néant |
| 6. Imputation | Propose comptes et axes | Néant | Néant |
| 7. Vérification du compte | Néant | Néant | **Vérifie et décide** |
| 8. Budget | Néant | Calcule le disponible ; rapprochement 3 voies | Examine les dépassements |
| 9. Anomalies | Signale doublons, inhabituels | Applique les règles | **Instruit et conclut** |
| 10. Approbation | Néant | Workflow | **Approuve** (personne habilitée) |
| 11. Écriture | Néant | Génère l'écriture | **Valide** |
| 12. Tableaux de bord | Néant | Met à jour | Analyse |
| 13. Archivage | Indexe | Archive et trace | Classe le papier |
| 14. Exceptions | Néant | Néant | **Traite selon procédure** |

Table: Tableau 12.1 : Explications détaillées

> **🔎 À retenir** : L'IA **propose et signale** ; le logiciel **enregistre, calcule et trace** ; le professionnel **vérifie, décide et valide**. Ce partage des rôles est la condition d'une automatisation compatible avec l'audit.

### Caisse et banque

**La caisse** est le point le plus sensible du contrôle interne des petites structures. Règles : plafond d'encaisse ; pièces pour chaque sortie ; arrêté de caisse quotidien ou hebdomadaire signé par le caissier et contrôlé par une autre personne ; comptage inopiné. L'IA peut aider à **numériser et extraire** les reçus de caisse et à **signaler** des sorties inhabituelles (montants ronds répétés, sorties juste sous le seuil d'autorisation) ; elle ne remplace pas le comptage physique.

**Le rapprochement bancaire** est un contrôle clé. *Exemple (fictif) au 31 mars :*

| | Montant (UM) |
|---|---|
| Solde du relevé bancaire | 48 250 |
| − Chèque n° 1182 émis, non encore encaissé | − 1 500 |
| + Remise de dépôt du 31/03, non encore créditée | + 800 |
| **= Solde bancaire rapproché** | **47 550** |
| Solde comptable du compte banque | 46 980 |
| − Frais bancaires de mars, non comptabilisés | − 35 |
| + Virement reçu (cotisations), non comptabilisé | + 605 |
| **= Solde comptable rapproché** | **47 550** |
| **Écart résiduel** | **0** |

Table: Tableau 12.2 : Explications détaillées

Les logiciels comptables et bancaires proposent souvent un **rapprochement automatique** (appariement des lignes du relevé et des écritures par montant, date et libellé). L'IA améliore l'appariement des libellés ambigus. Le comptable traite les lignes non appariées, et le rapprochement est **revu et signé** par une autre personne (responsable financier).

### Budget, financements affectés et non affectés, dépenses par projet

Une ASBL multi-bailleurs doit suivre ses dépenses selon **trois axes simultanés** : nature (plan comptable), projet/activité, et bailleur/ligne budgétaire du bailleur. Les **fonds affectés** ne peuvent financer que l'objet prévu ; les dépenses inéligibles doivent être couvertes par des **fonds non affectés**, qu'il faut donc préserver et suivre.

La **table de correspondance** est l'outil central : pour chaque bailleur, elle relie chaque ligne de son budget à vos comptes et codes analytiques. Elle permet de produire automatiquement le rapport de chaque bailleur dans son format à partir d'une seule comptabilité.

### Écarts budgétaires

![Figure 12.2 : Tableau de bord fictif : exécution budgétaire par ligne](03_ILLUSTRATIONS/figures/fig_12_2.svg){#fig-12-2}

Au 30 septembre (75 % de l'année écoulée), le tableau de bord du programme pluriannuel de santé communautaire (PRG-SANTE, qui regroupe plusieurs projets) fait apparaître (en milliers d'UM) :

| Ligne | Budget | Réalisé | Taux | Lecture |
|---|---|---|---|---|
| Personnel | 420 | 318 | 75,7 % | Conforme au prorata temporel |
| Déplacements | 60 | 71 | 118,3 % | **Dépassement** : à expliquer et à régulariser (réallocation autorisée ? fonds non affectés ?) |
| Formation | 85 | 35 | 41,2 % | **Sous-exécution** : retard d'activité ? risque de non-réalisation et de restitution des fonds |
| Équipements | 140 | 126 | 90,0 % | Avance sur le prorata : vérifier que les achats restants sont couverts |
| Communication | 25 | 26 | 104,0 % | Léger dépassement : vérifier le seuil de flexibilité de la convention |
| Frais de structure | 70 | 52 | 74,3 % | Conforme |

Table: Tableau 12.3 : Explications détaillées

L'analyse des écarts combine **calcul** (fait par le tableur ou le logiciel) et **explication** (qui relève des équipes). L'IA est utile pour rédiger une première analyse à partir des taux calculés et des commentaires des responsables (fiche P12.3), et pour comparer les écarts aux règles de flexibilité budgétaire de la convention.

### Trésorerie

Le plan de trésorerie prévoit, mois par mois, les encaissements (tranches des bailleurs, dons, cotisations) et les décaissements (salaires, fournisseurs, activités). Les ASBL sont exposées aux **retards de versement** des bailleurs. Un tableau simple sur douze mois glissants, mis à jour chaque mois, suffit souvent. L'IA peut aider à construire le modèle et à rédiger des scénarios (« et si la deuxième tranche arrive avec trois mois de retard ? ») ; la prévision chiffrée repose sur vos données et vos calendriers contractuels.

### Reporting

Les rapports financiers aux bailleurs exigent : le bon format, la bonne période, le bon taux de change, les bonnes lignes, la réconciliation avec la comptabilité. L'automatisation consiste à produire les rapports **à partir de la comptabilité** via la table de correspondance, plutôt que de les ressaisir. L'IA peut rédiger la partie narrative du rapport financier (explication des écarts), à partir des chiffres validés.

### Préparation des audits

Une comptabilité dont chaque écriture est liée à sa pièce et à son approbation transforme la préparation de l'audit : la liste des pièces demandées par l'auditeur est extraite en quelques minutes. L'IA peut aider à préparer le dossier permanent (statuts, conventions, PV, procédures), à vérifier la complétude des pièces d'un échantillon et à rédiger des réponses aux observations, toujours relues par le responsable financier. Le module 13 approfondit l'audit.

## 12.6 Application métier : automatiser le traitement des pièces à Horizons Partagés

**A. Contexte.** 340 pièces par mois, une comptable, quatre bureaux, cinq bailleurs, logiciel comptable existant.
**B. Problème.** Saisie et imputation manuelles chronophages ; retards de reporting ; pièces difficiles à retrouver.
**C. Symptômes.** Environ 35 heures de saisie par mois ; rapports en retard de trois semaines ; 11 pièces sur 60 non retrouvées lors du dernier audit.
**D. Causes profondes.** Canaux de réception multiples ; ressaisie ; absence de lien pièce-écriture ; une seule personne formée.
**E. Processus actuel.** Voir module 5, figure 5.1.
**F. Points de faiblesse.** Ressaisie, classement papier, approbations hors système, aucune détection de doublons.
**G. Résultat recherché.** Temps de traitement par pièce divisé par deux ; 100 % des pièces liées aux écritures ; clôture mensuelle à J+10 ; zéro paiement en double.
**H. Pertinence de l'IA.** Forte pour l'extraction et la proposition d'imputation (documents variés, libellés libres) ; complémentaire de règles automatiques (contrôles arithmétiques, seuils, doublons).
**I. Alternatives sans IA.** Saisie directe dans un formulaire numérique par le demandeur ; centralisation des pièces ; classement normalisé : à mettre en place de toute façon.
**J. Solution recommandée.** Canal unique de réception + outil d'extraction de documents relié au logiciel comptable (ou fonction intégrée au logiciel) + workflow d'approbation + archivage lié.
**K. Niveau.** Intermédiaire.
**L. Outils nécessaires.** Logiciel comptable acceptant l'import ou disposant d'une fonction de capture de documents ; outil d'extraction (intégré ou externe, évalué selon le module 9) ; workflow d'approbation ; stockage documentaire.
**M. Étapes détaillées de mise en œuvre.**

1. Mettre à jour le manuel de procédures et la délégation de signature (module 5).
2. Finaliser le plan analytique et les tables de correspondance par bailleur.
3. Créer le canal unique de réception et la règle de nommage.
4. Sélectionner l'outil (module 9) ; vérifier le contrat (données orange, coordonnées bancaires sensibles).
5. Paramétrer : champs à extraire, contrôles automatiques, seuil de confiance, comptes sensibles, règles de doublons, circuit d'approbation par seuil.
6. Tester sur 100 pièces de l'année précédente déjà comptabilisées : comparer les propositions de l'IA aux imputations réelles et mesurer le taux d'exactitude.
7. Pilote de deux mois sur un bureau, en parallèle du processus actuel.
8. Ajuster les règles ; former les utilisateurs ; documenter.
9. Déploiement aux quatre bureaux.
10. Revue mensuelle des indicateurs et des corrections.

**N. Prompts et automatisation.** Fiches P12.1 à P12.3 ci-dessous (utilisables au niveau Débutant avec un assistant validé, ou comme spécifications pour paramétrer un outil).
**O. Exemple de résultat.** Voir le déroulé de la facture F-2026-0412 ci-dessus.
**P. Méthode de vérification.** Test initial sur 100 pièces connues ; pendant le pilote, contrôle de 100 % des propositions ; ensuite, contrôle de toutes les propositions sous le seuil de confiance et d'un échantillon aléatoire de 10 % des autres.
**Q. Contrôles humains.** Vérification des champs à faible confiance ; vérification du compte (étape 7) ; instruction des anomalies ; approbation par la personne habilitée ; validation des écritures ; revue mensuelle du rapprochement bancaire par le responsable financier.
**R. Risques et précautions.** Erreurs d'extraction ; imputation erronée sur un bailleur (dépense inéligible) ; biais d'automatisation (validation « en masse ») ; fraude par fausse facture ou faux changement de RIB ; données bancaires des fournisseurs exposées. Précautions : seuils, échantillonnage, blocage des modifications de RIB, outil validé.
**S. Coûts et maintenance.** Abonnement à l'outil d'extraction (selon volume), paramétrage, formation, temps de contrôle, mise à jour des tables de correspondance à chaque nouvelle convention.
**T. Indicateurs de performance.** Temps moyen de traitement par pièce ; taux de propositions d'imputation acceptées sans modification ; taux d'erreurs détectées en revue ; délai de clôture ; nombre de pièces non retrouvées lors de l'audit ; nombre d'alertes de doublons et taux de faux positifs.
**U. Amélioration continue.** Analyse mensuelle des corrections pour améliorer les règles et les données d'historique ; revue annuelle du paramétrage avec l'auditeur.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Prérequis | Coûts | Limites |
|---|---|---|---|---|---|
| **Débutant** | Pièces centralisées et nommées ; tableur de saisie avec listes déroulantes (comptes, projets, lignes) ; assistant autorisé pour extraire les champs d'une pièce **sans données personnelles** et proposer une imputation à partir du plan fourni ; contrôle humain systématique | Tableur, application de numérisation, assistant validé | Plan comptable et analytique ; formation | Faibles | Pièce par pièce ; pas d'intégration ; vigilance sur les données (coordonnées bancaires, noms de personnes physiques) |
| **Intermédiaire** | Fonction de capture intégrée au logiciel comptable ou outil d'extraction relié ; workflow d'approbation ; rapprochement bancaire automatique ; tableaux de bord | Logiciel comptable en ligne, outil d'extraction, workflow | Paramétrage, tables de correspondance | Abonnements, paramétrage | Dépendance aux fournisseurs ; qualité des historiques |
| **Avancé** | ERP intégrant achats, comptabilité, budget, trésorerie ; extraction et imputation automatiques avec apprentissage sur l'historique ; contrôles continus ; reporting bailleurs automatisé ; assistant RAG sur les conventions et procédures | ERP, API, entrepôt de données, RAG | Équipe financière et SI structurée | Élevés | Complexité, coût de maintenance, gouvernance des données |

Table: Tableau 12.4 : Application métier : automatiser le traitement des pièces à Horizons Partagés

## 12.7 Prompts prêts à l'emploi

### Fiche P12.1 : Extraire les données d'une facture

**A. Titre.** Extraction structurée d'une pièce justificative.

**B. Objectif.** Obtenir les champs d'une facture dans un format prêt à importer, avec signalement des incertitudes.

**C. Contexte d'utilisation.** Comptabilité, niveau Débutant ; ou test d'un outil avant paramétrage.

**D. Données nécessaires.** L'image ou le PDF de la facture (outil autorisé pour données orange) ; la liste des champs attendus.

**E. Prompt complet.**

```text
Contexte : je suis comptable d'une ASBL. Je dois enregistrer la
facture jointe.
Tâche : extrais les informations de la facture.
Résultat attendu : un tableau avec les champs suivants : fournisseur ;
numéro de facture ; date (AAAA-MM-JJ) ; date d'échéance ; référence de
commande ; devise ; pour chaque ligne : désignation, quantité, prix
unitaire, montant ; sous-total ; taxes (taux et montant, ou « aucune
taxe mentionnée ») ; total.
Pour chaque champ, ajoute une colonne « certitude » (élevée / moyenne
/ faible) et une colonne « remarque ».
Contrôles à effectuer et à signaler : somme des lignes = sous-total ;
sous-total + taxes = total ; présence de coordonnées bancaires (si
oui, écris seulement « coordonnées bancaires présentes », sans les
recopier).
Limites : si un champ est illisible ou absent, écris « ILLISIBLE » ou
« ABSENT ». Ne devine aucun chiffre.
```

**F. Instructions d'utilisation.** Joignez la pièce ; collez le tableau dans le tableur de saisie ; corrigez les champs à certitude faible ou moyenne en les comparant à l'image.

**G. Résultat attendu.** Un tableau de champs, des certitudes, les résultats des contrôles arithmétiques.

**H. Exemple d'application (illustratif).** Pour la facture F-2026-0412, le tableau obtenu indique « prix unitaire ligne 1 : 6,60, certitude moyenne, remarque : le 5 et le 6 sont peu distincts » et « contrôle : 40 × 6,60 = 264 ≠ 260 indiqué ; incohérence ». La comptable vérifie l'image : 6,50. Le contrôle arithmétique a permis de détecter l'erreur de lecture.

**I. Méthode de vérification.** Comparez chaque champ à certitude non élevée à l'image ; recalculez les totaux dans le tableur ; vérifiez que le numéro de facture n'existe pas déjà pour ce fournisseur.

**J. Précautions.** Ne pas soumettre de pièces contenant des données personnelles sensibles (notes de frais avec informations médicales, bulletins de paie) à un outil non validé. Ne jamais recopier des coordonnées bancaires dans un outil externe.

**K. Amélioration.** Si l'outil confond prix unitaires et montants : « Pour chaque ligne, vérifie que quantité × prix unitaire = montant de la ligne et signale toute différence. »

### Fiche P12.2 : Proposer une imputation comptable et analytique

**A. Titre.** Proposition d'imputation justifiée.

**B. Objectif.** Obtenir une proposition d'imputation conforme **à votre** plan comptable et **à votre** plan analytique, avec justification et niveau de confiance.

**C. Contexte d'utilisation.** Saisie comptable ; formation d'une nouvelle recrue ; cas ambigus.

**D. Données nécessaires.** Extrait du plan comptable (comptes de charges utilisés) ; liste des projets, activités et lignes budgétaires ; règles d'éligibilité pertinentes de la convention ; données extraites de la pièce ; information du bon de commande.

**E. Prompt complet.**

```text
Contexte : comptabilité d'une ASBL multi-bailleurs.
Plan comptable (extrait) : <plan>[COMPTES ET INTITULÉS]</plan>
Plan analytique : <analytique>[PROJETS / ACTIVITÉS / LIGNES]</analytique>
Règles d'éligibilité applicables : <regles>[EXTRAITS DE CONVENTION]</regles>
Pièce : <piece>[CHAMPS EXTRAITS + RÉFÉRENCE DE COMMANDE + OBJET]</piece>
Tâche : propose l'imputation de cette dépense.
Résultat attendu : tableau « Ligne de la pièce | Compte proposé
(numéro et intitulé, choisi UNIQUEMENT dans le plan fourni) |
Projet | Activité | Ligne budgétaire | Justification | Confiance
(élevée/moyenne/faible) | Point d'éligibilité à vérifier ».
Règles : si aucun compte du plan ne convient, écris « AUCUN COMPTE
ADAPTÉ » ; si l'affectation à un projet est incertaine, propose
« À DÉTERMINER » et explique pourquoi ; ne crée aucun compte.
```

**F. Instructions d'utilisation.** Fournissez uniquement les extraits pertinents du plan (pas le plan entier si l'outil est limité). Reportez la proposition dans le logiciel après vérification.

**G. Résultat attendu.** Une proposition par ligne de facture, justifiée, avec points de vigilance.

**H. Exemple d'application (illustratif).** Proposition obtenue : « Ligne 1 et 2, compte "Fournitures de bureau", PRJ-SANTE-07 / 1.1 / ligne 2 (justification : bon de commande BC-2026-077 codé sur l'activité 1.1 ; consommables pour sessions de formation) confiance élevée : vérifier : la convention autorise les consommables de formation sur la ligne Activités (art. 6.2 fourni) ».

**I. Méthode de vérification.** Vérifiez que le compte existe dans votre plan et correspond à la nature ; que le codage analytique correspond au bon de commande approuvé ; que la règle d'éligibilité citée figure bien dans la convention.

**J. Précautions.** Données orange. La décision d'imputation reste celle de la comptable.

**K. Amélioration.** Pour un usage récurrent, ajoutez 10 exemples d'imputations validées (« exemples guidés ») afin d'aligner les propositions sur vos pratiques.

### Fiche P12.3 : Analyse narrative des écarts budgétaires

**A. Titre.** Note d'analyse des écarts budgétaires.

**B. Objectif.** Rédiger une analyse claire des écarts à partir de taux déjà calculés et des explications des responsables.

**C. Contexte d'utilisation.** Comité de direction mensuel ; rapport financier intermédiaire.

**D. Données nécessaires.** Tableau budget/réalisé/taux (calculé au tableur) ; prorata temporel ; commentaires des responsables d'activité ; règles de flexibilité budgétaire de la convention.

**E. Prompt complet.**

```text
Contexte : suivi budgétaire du projet [CODE], au [DATE], soit [X] %
de la période écoulée.
Données : <tableau>[LIGNE | BUDGET | RÉALISÉ | TAUX]</tableau>
<commentaires>[EXPLICATIONS DES RESPONSABLES]</commentaires>
<flexibilite>[RÈGLE : ex. réallocation autorisée jusqu'à 10 % par ligne
sans accord préalable]</flexibilite>
Tâche : rédige une note d'analyse des écarts.
Résultat attendu :
1. Synthèse en 3 phrases.
2. Pour chaque ligne dont le taux s'écarte de plus de [15] points du
   prorata : écart, explication (selon les commentaires ; sinon
   [EXPLICATION À OBTENIR]), conformité à la règle de flexibilité,
   action proposée.
3. Risques pour la fin de période (sous-exécution, dépassement,
   restitution de fonds).
4. Décisions à soumettre à la direction.
Règles : n'effectue aucun nouveau calcul ; utilise uniquement les
chiffres fournis.
```

**F. Instructions d'utilisation.** Calculez taux et écarts au tableur ; recueillez les commentaires des responsables avant d'utiliser la fiche.

**G. Résultat attendu.** Une note de une page, factuelle, avec actions et décisions proposées.

**H. Exemple d'application (illustratif).** Pour les données du tableau de la section 12.5, la note propose notamment : « Déplacements : 118,3 % à 75 % de la période. Dépassement de 11 000 UM sur un budget de 60 000 UM, soit 18,3 % de la ligne, supérieur au seuil de flexibilité de 10 % : accord préalable du bailleur nécessaire ou couverture par fonds non affectés. Décision à soumettre à la direction. »

**I. Méthode de vérification.** Vérifiez chaque chiffre repris ; recalculez les écarts cités (71 − 60 = 11 ; 11 / 60 = 18,3 %) ; vérifiez la règle de flexibilité dans la convention.

**J. Précautions.** Données orange.

**K. Amélioration.** « Ajoute une projection de fin de période pour chaque ligne au rythme actuel (calcul : réalisé / taux de période écoulée) et signale les lignes qui dépasseraient 100 %. » *(Vérifiez ces projections au tableur.)*

## 12.8 Résultats attendus

Pièces centralisées et liées aux écritures ; propositions d'imputation contrôlées ; rapprochements bancaires mensuels revus ; suivi budgétaire multi-axes à jour ; rapports produits à partir de la comptabilité ; dossier d'audit préparé en continu.

## 12.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Validation des écritures ; approbation des dépenses et des paiements par les personnes habilitées ; vérification de l'éligibilité ; toute modification de coordonnées bancaires de fournisseurs (vérifiée par un second canal) ; revue et signature des rapprochements bancaires ; comptage physique de la caisse ; arrêté des comptes et rapports financiers. L'IA ne valide, n'approuve et ne paie jamais.

## 12.10 Risques et erreurs à éviter

- Automatiser avant d'avoir stabilisé le plan analytique et les procédures.
- Valider en masse des propositions sans les lire (biais d'automatisation).
- Laisser l'outil modifier les données de référence (fournisseurs, RIB).
- Supprimer des écritures au lieu de passer des écritures de correction.
- Produire les rapports bailleurs par ressaisie au lieu de les dériver de la comptabilité.
- Confier des calculs financiers à un modèle de langage.
- Appliquer un plan comptable national comme s'il était universel.

## 12.11 Exercice pratique

**Consigne (3 heures).**

1. Prenez trois factures non sensibles de votre organisation. Appliquez la fiche P12.1, puis comparez champ par champ avec la pièce. Calculez le taux de champs exacts.
2. Appliquez la fiche P12.2 avec votre plan comptable. Comparez aux imputations réellement passées.
3. Réalisez le rapprochement bancaire suivant et trouvez l'écart : solde du relevé 12 400 ; chèque émis non encaissé 950 ; dépôt non crédité 300 ; solde comptable 11 820 ; frais bancaires non comptabilisés 20 ; virement reçu non comptabilisé ? (à trouver).
4. Rédigez la procédure de traitement de deux cas exceptionnels de l'étape 14.

**Éléments de correction.** (3) Solde bancaire rapproché = 12 400 − 950 + 300 = 11 750. Solde comptable rapproché = 11 820 − 20 + X = 11 750, d'où X = − 50 : il ne peut s'agir d'un virement **reçu** (qui augmenterait le solde) ; l'écart de 50 correspond à une sortie non comptabilisée (par exemple un prélèvement) ou à une erreur à rechercher. Cet exercice montre qu'un rapprochement ne se « force » pas : l'écart doit être expliqué par une pièce. (1, 2) Le taux d'exactitude mesuré fonde la décision d'utiliser ou non l'outil et le niveau de contrôle. (4) Les procédures précisent le déclencheur, les actions, les responsables et la trace documentaire.

## 12.12 Synthèse

- L'automatisation comptable repose sur des fondations : plans comptable et analytique, procédures, séparation des tâches, classement.
- Pour chaque pièce, l'IA propose et signale, le logiciel enregistre et trace, le professionnel vérifie et décide.
- Les contrôles clés restent humains : vérification du compte, approbation, validation, rapprochements, caisse.
- Le suivi multi-axes et les tables de correspondance permettent de produire les rapports de chaque bailleur à partir d'une seule comptabilité.
- Il n'existe pas de référentiel comptable universel : adaptez-vous au droit applicable.

## 12.13 QCM : Module 12

**Q1.** (une seule réponse) Dans le traitement assisté d'une facture, le rôle de l'IA est principalement de :

a) valider l'écriture comptable.
b) approuver le paiement.
c) signer le rapprochement bancaire.
d) proposer des champs, des imputations et signaler des anomalies.

**Q2.** (une ou plusieurs réponses) Quelles étapes relèvent impérativement d'une décision humaine ?

a) Vérification que le compte proposé est approprié.
b) Approbation par la personne habilitée.
c) Validation de l'écriture.
d) Calcul du disponible budgétaire.

**Q3.** (une seule réponse) Le rapprochement à trois voies compare :

a) budget, réalisé et prévision.
b) commande, bon de livraison et facture.
c) banque, caisse et grand livre.
d) trois devis.

**Q4.** (une seule réponse) Une demande de modification des coordonnées bancaires d'un fournisseur reçue par courriel doit :

a) être bloquée et vérifiée par un second canal par le responsable financier.
b) être appliquée immédiatement par l'outil.
c) être ignorée.
d) être traitée par l'IA.

**Q5.** (une seule réponse) Dans l'exemple du module, le solde rapproché au 31 mars est :

a) 46 980
b) 48 250
c) 47 515
d) 47 550

**Q6.** (une ou plusieurs réponses) Les fonds affectés :

a) ne peuvent financer que l'objet prévu par le donateur.
b) peuvent couvrir toute dépense de l'organisation.
c) exigent un suivi distinct.
d) peuvent devoir être restitués en cas de non-utilisation conforme.

**Q7.** (mise en situation, une seule réponse) L'outil signale un doublon possible : même fournisseur, même montant, deux numéros de facture différents. Que faites-vous ?

a) Supprimer la seconde facture.
b) Vérifier les bons de commande et de livraison avant de conclure, et documenter la conclusion.
c) Payer les deux sans vérification.
d) Désactiver l'alerte.

**Q8.** (mise en situation, une seule réponse) Une ligne « Déplacements » atteint 118 % de son budget à 75 % de la période. Première action ?

a) Analyser l'écart, vérifier la règle de flexibilité de la convention et soumettre une décision à la direction.
b) Réimputer discrètement l'excédent sur une autre ligne.
c) Attendre la fin du projet.
d) Supprimer des écritures.

**Q9.** (une seule réponse) Concernant les référentiels comptables des ASBL :

a) un plan comptable national unique s'applique dans tous les pays.
b) les normes IFRS s'appliquent obligatoirement à toutes les ASBL.
c) il n'existe aucune règle comptable pour les ASBL.
d) les règles dépendent de la juridiction ; un référentiel international volontaire (INPAS) existe depuis 2025.

**Q10.** (une ou plusieurs réponses) Indicateurs pertinents pour suivre l'automatisation du traitement des pièces :

a) temps moyen de traitement par pièce.
b) taux de propositions d'imputation acceptées sans modification.
c) délai de clôture mensuelle.
d) nombre de logiciels installés.

## 12.14 Corrigé détaillé : Module 12

**Q1 : d.** L'IA propose et signale ; elle ne valide ni n'approuve.

**Q2 : a, b, c.** Le calcul du disponible (d) est réalisé par le logiciel, l'humain en tirant les conséquences.

**Q3 : b.** Commande, livraison, facture : ce contrôle prévient les paiements de biens non commandés ou non reçus.

**Q4 : a.** C'est un schéma de fraude fréquent ; la vérification par un second canal (appel au contact habituel connu) est indispensable.

**Q5 : d.** 48 250 − 1 500 + 800 = 47 550, et 46 980 − 35 + 605 = 47 550.

**Q6 : a, c, d.** Les fonds affectés ne couvrent pas n'importe quelle dépense (b).

**Q7 : b.** On instruit avant de conclure ; dans l'exemple, il s'agissait de deux commandes distinctes.

**Q8 : a.** Le dépassement est analysé au regard de la convention ; une réimputation non autorisée (b) serait une irrégularité.

**Q9 : d.** Les obligations sont nationales ; INPAS est volontaire sauf adoption ou exigence d'un bailleur.

**Q10 : a, b, c.** Le nombre de logiciels (d) ne mesure pas la performance.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- COSO. (2013). *Internal Control : Integrated Framework*.
- International Non-Profit Reporting Foundation (INPRF) / projet IFR4NPO (CIPFA et Humentum). (2025). *International Non-Profit Accounting Standard (INPAS)*.


# Module 13 : Audit, contrôle interne, gestion des risques et conformité {#h17}

## 13.1 Mise en situation

Au Réseau Citoyen pour l'Eau (RCE), Fatou est contrôleuse interne. Le comité d'audit lui demande une revue des dépenses du premier trimestre du projet « Eau et assainissement » et du siège. Elle dispose de l'extraction du grand livre (40 dépenses, 31 890,50 UM), du fichier fournisseurs, des pièces numérisées et du manuel de procédures. Avec la méthode classique (sélection d'un échantillon, vérification des pièces) elle aurait examiné une quinzaine d'opérations. Avec des tests analytiques assistés, elle peut examiner **toute la population**, puis concentrer son temps d'expert sur les opérations les plus risquées.

Ce module suit sa démarche, du fichier brut à la feuille de travail et aux recommandations. Les tests présentés ont été **réellement exécutés** sur le fichier fictif fourni en annexe (`depenses_RCE_T1_2026.csv`) à l'aide d'un script reproductible (`tests_audit.py`) ; les résultats chiffrés de ce module en sont issus. Les conclusions des vérifications de pièces et d'entretiens, elles, relèvent du scénario pédagogique.

## 13.2 Problématique

Les ASBL sont exposées à des risques de fraude, d'erreur et de non-conformité, souvent avec des fonctions de contrôle réduites. Dans l'étude mondiale de l'ACFE sur 1 921 cas de fraude interne survenus entre janvier 2022 et septembre 2023 dans 138 pays et territoires, 43 % des fraudes ont été détectées grâce à un signalement : davantage que par tout autre moyen (ACFE, 2024) : les contrôles formels, à eux seuls, en détectent une part bien moindre. L'IA et l'analyse de données permettent d'étendre les contrôles à l'ensemble des opérations, mais elles produisent aussi des faux positifs et ne remplacent ni le jugement professionnel, ni les dispositifs de signalement, ni le scepticisme de l'auditeur.

## 13.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. évaluer l'environnement de contrôle et cartographier les risques ;
2. concevoir et exécuter des tests analytiques sur un fichier de dépenses (doublons, fractionnement, fournisseurs, pièces, séparation des tâches) ;
3. interpréter les résultats, distinguer anomalies et faux positifs, et conduire les vérifications ;
4. documenter les travaux dans une feuille de travail ;
5. formuler des constats et des recommandations ;
6. suivre les recommandations et construire un tableau de bord des risques ;
7. utiliser l'IA dans le respect des normes professionnelles et de la confidentialité.

## 13.4 Notions et définitions

- **Contrôle interne** : processus mis en œuvre par la gouvernance, la direction et le personnel, destiné à fournir une assurance raisonnable quant à la réalisation des objectifs opérationnels, de reporting et de conformité (COSO, 2013).
- **Audit interne** : activité indépendante et objective qui donne une assurance et des conseils ; ses normes de référence au niveau international sont les *Global Internal Audit Standards* de l'IIA, en vigueur depuis le 9 janvier 2025.
- **Audit externe** : examen des états financiers par un auditeur indépendant, selon les normes et les obligations légales applicables.
- **Risque inhérent / résiduel** : risque avant / après prise en compte des mesures de maîtrise.
- **Test analytique** : examen de données pour repérer des tendances, des ruptures ou des opérations atypiques.
- **Faux positif** : opération signalée par un test qui se révèle normale après examen.
- **Feuille de travail** : document qui consigne l'objectif, la méthode, les éléments examinés, les constats et les conclusions d'un travail d'audit.
- **Constat** : écart entre la situation constatée et le critère attendu, avec sa cause, ses conséquences et une recommandation.

## 13.5 Explications détaillées

### L'environnement de contrôle

L'environnement de contrôle est la base des autres composantes : intégrité et valeurs affichées par la direction, rôle effectif du conseil (et d'un éventuel comité d'audit), structure et délégations, compétences, responsabilisation. Des tests analytiques sophistiqués ne compensent pas un environnement où les dirigeants contournent les procédures.

### La cartographie des risques

![Figure 13.2 : Carte thermique des risques](03_ILLUSTRATIONS/figures/fig_13_2.svg){#fig-13-2}

Pour chaque processus (achats, paiements, avances, caisse, paie, subventions), on identifie les risques, on les évalue (probabilité × impact, de 1 à 5), on recense les contrôles existants, puis on estime le risque résiduel. L'IA aide à **proposer des risques** à partir de la description d'un processus et à **mettre en forme** la cartographie ; l'évaluation relève des responsables et de l'auditeur.

| Risque | Processus | P | I | Score | Contrôles existants | Évaluation |
|---|---|---|---|---|---|---|
| R1 Paiements en double | Paiements | 3 | 4 | 12 | Aucun contrôle automatique | Insuffisant |
| R2 Avances non justifiées | Avances | 4 | 3 | 12 | Relance manuelle irrégulière | Insuffisant |
| R3 Fractionnement des achats | Achats | 2 | 4 | 8 | Seuils écrits, non surveillés | Partiel |
| R4 Fuite de données via outils d'IA | Transverse | 3 | 5 | 15 | Aucune règle écrite | Insuffisant |
| R5 Dépendance à un fournisseur | Achats | 2 | 3 | 6 | Mise en concurrence au-delà du seuil | Partiel |

Table: Tableau 13.1 : Explications détaillées

### Les tests analytiques

![Figure 13.1 : Entonnoir des tests analytiques assistés](03_ILLUSTRATIONS/figures/fig_13_1.svg){#fig-13-1}

| Test | Règle | Risque visé |
|---|---|---|
| T1 Doublons | Même fournisseur, même montant, même libellé | Paiement en double |
| T2 Fournisseur hors base | Code fournisseur absent du fichier fournisseurs | Fournisseur fictif |
| T3 Pièce manquante | Pièce jointe absente | Dépense non justifiée |
| T4 Auto-approbation | Demandeur = approbateur | Séparation des tâches |
| T5 Fractionnement | ≥ 2 dépenses sous le seuil, même fournisseur, dans un délai de 7 jours, cumul au-dessus du seuil | Contournement des seuils |
| T6 Montants ronds | Montant ≥ seuil et multiple de 500 | Estimation, facture de complaisance |
| T7 Week-end | Date un samedi ou un dimanche | Opération atypique (faible pertinence sur le terrain) |
| T8 Sans bon de commande | Montant ≥ seuil sans bon de commande | Non-respect de la procédure |
| T9 Libellé imprécis | Libellé contenant « divers », « prestation de services » | Opacité |

Table: Tableau 13.2 : Explications détaillées

Ces tests reposent sur des **règles explicites** : ils relèvent davantage de l'analyse de données que de l'IA au sens strict. L'IA intervient pour : écrire les formules ou le script ; rapprocher des libellés semblables mais non identiques ; regrouper des fournisseurs aux noms proches (« Quincaillerie Delta » et « Quincaillerie Delta SARL ») ; résumer les résultats ; rédiger la feuille de travail et les recommandations.

### Résultats sur la population de 40 dépenses

Seuil d'autorisation et de bon de commande retenu dans le cas : 1 000 UM.

| Test | Nombre signalé | Opérations |
|---|---|---|
| T1 Doublons | 8 | D01/D13 ; D03/D39 ; D06/D35 ; D15/D31 |
| T2 Fournisseur hors base | 2 | D24, D33 |
| T3 Pièce manquante | 4 | D18, D24, D31, D33 |
| T4 Auto-approbation | 10 | D06, D12, D16, D17, D18, D20, D24, D27, D33, D35 |
| T5 Fractionnement | 3 | D16, D17, D18 (cumul 2 970 UM en 3 jours) |
| T6 Montants ronds | 2 | D24, D33 |
| T7 Week-end | 12 | D08, D09, D12, D19, D20, D23, D24, D27, D33, D36, D39, D40 |
| T8 Sans bon de commande | 2 | D24, D33 |
| T9 Libellé imprécis | 2 | D24, D33 |
| **Opérations signalées par au moins un test** | **22** | sur 40 |

Table: Tableau 13.3 : Explications détaillées

Vingt-deux opérations sur quarante : c'est beaucoup trop pour tout examiner en détail, et beaucoup sont des **faux positifs**. Le test T7 (week-end) est peu discriminant pour une organisation qui mène des activités de terrain le samedi. Les « doublons » D03/D39 (hôtel, 270 UM) concernent deux missions de projets et de dates différents ; D06/D35 et D15/D31 correspondent à des dépenses récurrentes de même montant (carburant, hébergement). L'auditrice **priorise** donc :

- **priorité 1** : opérations cumulant plusieurs alertes fortes (T2, T3, T8, T9) : D24, D33 ;
- **priorité 2** : doublon portant sur le **même bon de commande** (D01/D13, BC-101) ; fractionnement avec pièce manquante (D16, D17, D18) ;
- **priorité 3** : pièce manquante isolée (D31) ;
- **traitement global** : auto-approbations récurrentes (T4) : faiblesse de conception du contrôle, à examiner au niveau de la procédure plutôt qu'opération par opération.

Soit **8 opérations prioritaires** examinées en détail (D01, D13, D16, D17, D18, D24, D31, D33).

### Vérification des pièces et conclusions (scénario)

| Opération | Vérifications réalisées | Conclusion |
|---|---|---|
| D01 / D13 | Les deux paiements de 1 240 UM se réfèrent au même bon de commande BC-101 et à la même facture ; un seul bon de livraison | **Constat 1 : paiement en double** de 1 240 UM. Demande de remboursement au fournisseur |
| D16 / D17 / D18 | Trois achats de fournitures à 990, 985 et 995 UM en trois jours, payés en caisse, approuvés par la demandeuse ; pas de pièce pour D18 | **Constat 2 : fractionnement** contournant le seuil de 1 000 UM et la mise en concurrence ; auto-approbation ; une dépense non justifiée |
| D24 / D33 | Fournisseur « Services Généraux KB » absent du fichier fournisseurs ; aucune pièce ; libellé imprécis ; montants ronds (3 000 et 2 500 UM) ; demandeur et approbateur identiques (coordinateur EAU-03) | **Constat 3 : dépenses non justifiées de 5 500 UM, indices de fraude.** L'auditrice ne conclut pas seule : elle applique la politique de lutte contre la fraude (information confidentielle de la direction et du président du comité d'audit, préservation des preuves, pas d'entretien avec l'intéressé avant décision) |
| D31 | Facture d'hôtel retrouvée dans la messagerie de l'agent, non jointe | Régularisée : pièce archivée. Pas de constat, mais point d'attention sur la collecte des pièces de mission |
| T4 (global) | La procédure autorise le logisticien à approuver ses propres achats de carburant en caisse | **Faiblesse de contrôle** : séparation des tâches insuffisante |

Table: Tableau 13.4 : Explications détaillées

> **🛑 Contrôle humain obligatoire** : Une alerte n'est pas une preuve. Aucune conclusion de fraude, aucun nom, aucune sanction ne découle d'un résultat automatique. Les soupçons de fraude suivent la politique de l'organisation et, le cas échéant, les obligations légales, sous la responsabilité de personnes habilitées.

### La feuille de travail

Une feuille de travail comporte : référence ; objectif ; population et source des données ; méthode (tests, critères, seuils) ; résultats ; éléments examinés ; constats ; conclusion ; préparé par / revu par, avec dates. L'IA peut produire un premier projet à partir des résultats et des notes ; l'auditrice le complète et le signe ; un pair ou le responsable de l'audit le revoit.

### Constats et recommandations

Un constat bien rédigé suit le schéma **critère, constat, cause, conséquence, recommandation**. Exemple pour le constat 2 :

- *Critère* : manuel de procédures, § 5.3 : tout achat d'un montant cumulé supérieur à 1 000 UM auprès d'un même fournisseur pour un même besoin fait l'objet d'une consultation d'au moins trois fournisseurs et d'une approbation de la direction.
- *Constat* : trois achats de fournitures de bureau (990, 985 et 995 UM ; total 2 970 UM) ont été effectués auprès du même fournisseur du 3 au 5 février, payés en caisse et approuvés par la demandeuse ; la pièce de l'un d'eux est manquante.
- *Cause* : absence de contrôle du cumul par fournisseur ; possibilité d'auto-approbation en caisse.
- *Conséquence* : contournement de la mise en concurrence et de l'approbation ; risque de surcoût et de dépenses non justifiées ; risque de non-éligibilité auprès du bailleur.
- *Recommandation* : (1) interdire l'auto-approbation ; (2) mettre en place une alerte mensuelle de cumul par fournisseur ; (3) obtenir la pièce manquante ou reclasser la dépense sur fonds non affectés ; (4) rappeler la procédure aux équipes. Responsable : directrice administrative et financière. Échéance : 30 juin.

### Suivi des recommandations et tableau de bord des risques

Les recommandations sont inscrites dans un **registre de suivi** (annexe 20) : numéro, constat, recommandation, priorité, responsable, échéance, état, preuve de mise en œuvre. Le tableau de bord présenté au comité d'audit montre : nombre de recommandations par priorité et par état ; recommandations échues ; évolution des scores de risque ; indicateurs de contrôle (taux de pièces manquantes, nombre de doublons détectés, nombre d'auto-approbations).

### Analyse de données en continu

Au niveau avancé, les tests deviennent des **contrôles continus** exécutés chaque mois (voire chaque jour) sur l'ERP, avec des alertes transmises aux responsables. Il faut alors gérer le taux de faux positifs (sinon les alertes sont ignorées), documenter et tester les règles, et protéger l'accès aux résultats, qui peuvent être sensibles.

### L'IA et les normes professionnelles

L'usage de l'IA par l'auditeur doit respecter la confidentialité des données (outil autorisé, minimisation), la traçabilité (documenter dans la feuille de travail l'outil utilisé et la manière dont ses résultats ont été vérifiés), et le jugement professionnel. Les conclusions d'audit restent celles de l'auditeur.

## 13.6 Application métier : revue des dépenses du premier trimestre au RCE

**A. Contexte.** Grande ONG, ERP, comité d'audit, contrôleuse interne unique.
**B. Problème.** Revue limitée à de petits échantillons ; anomalies détectées tardivement.
**C. Symptômes.** Remarques récurrentes des auditeurs externes ; recommandations non suivies.
**D. Causes profondes.** Pas de tests sur la population complète ; pas de registre des recommandations ; faiblesses de conception des contrôles.
**E. Processus actuel.** Échantillonnage manuel annuel.
**F. Faiblesses.** Couverture faible ; pas de détection des schémas (fractionnement, fournisseurs fictifs).
**G. Résultat recherché.** Couverture de 100 % des opérations par des tests ciblés ; constats documentés ; recommandations suivies.
**H. Pertinence de l'IA.** Pour écrire et documenter les tests, rapprocher des libellés et des noms proches, rédiger les feuilles de travail et les recommandations. Les tests eux-mêmes sont des règles.
**I. Alternatives sans IA.** Les mêmes tests dans un tableur (filtres, tableaux croisés, `NB.SI.ENS`) : parfaitement possible pour de petits volumes.
**J. Solution recommandée.** Bibliothèque de tests standardisés, exécutés trimestriellement, avec priorisation et feuille de travail type.
**K. Niveau.** Débutant (tableur) à Intermédiaire (script ou outil d'analyse) ; Avancé pour le contrôle continu.
**L. Outils.** Tableur ou outil d'analyse de données ; assistant autorisé pour données orange ; registre des recommandations.
**M. Étapes détaillées.**

1. Définir l'objectif et la population (période, entités, comptes).
2. Extraire les données de l'ERP et le fichier fournisseurs ; contrôler l'exhaustivité (total de l'extraction = total du grand livre).
3. Pseudonymiser si nécessaire (les noms de personnes ne sont pas utiles pour les tests ; utiliser les fonctions).
4. Exécuter les tests T1 à T9 (fiche P13.1).
5. Prioriser les opérations signalées.
6. Examiner les pièces, interroger les responsables, documenter.
7. Rédiger la feuille de travail (fiche P13.2).
8. Rédiger les constats et recommandations (fiche P13.3) ; les discuter avec les responsables.
9. Présenter au comité d'audit ; inscrire au registre de suivi.
10. Relancer et vérifier la mise en œuvre ; réexécuter les tests au trimestre suivant.

**N. Prompts et automatisation.** Fiches P13.1 à P13.3 ; script reproductible en annexe.
**O. Exemple de résultat.** Tableaux ci-dessus.
**P. Méthode de vérification.** Exhaustivité de l'extraction ; recalcul indépendant de quelques résultats ; revue de la feuille de travail par un pair.
**Q. Contrôles humains.** Priorisation, examen des pièces, conclusions, qualification des faits, recommandations, traitement des soupçons de fraude.
**R. Risques.** Faux positifs nombreux ; faux négatifs (un test ne détecte que ce qu'il cherche) ; atteinte à la réputation de personnes ; confidentialité.
**S. Coûts et maintenance.** Tableur : temps. Outil d'analyse : licence. Maintenance de la bibliothèque de tests et des seuils.
**T. Indicateurs.** Couverture (% des opérations testées) ; taux de faux positifs par test ; nombre de constats ; montants concernés ; taux de mise en œuvre des recommandations à l'échéance.
**U. Amélioration continue.** Supprimer ou affiner les tests peu discriminants (ici T7) ; ajouter des tests selon les nouveaux risques ; mesurer l'évolution trimestrielle.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Tests T1 à T9 dans un tableur avec formules proposées par l'IA ; feuille de travail type ; registre des recommandations | Tableur, assistant | Faibles | Volumes limités ; risque d'erreur de formule : tester sur des cas connus |
| Intermédiaire | Script ou outil d'analyse de données exécutant une bibliothèque de tests ; rapprochement de noms proches ; tableaux de bord | Outil d'analyse, assistant professionnel | Licences modestes | Compétences en analyse de données |
| Avancé | Contrôle continu sur l'ERP, alertes automatiques, gestion des cas, tableau de bord des risques intégré, IA pour la détection d'anomalies statistiques | ERP, plateforme d'audit, outil de GRC | Élevés | Gestion des faux positifs ; gouvernance des accès |

Table: Tableau 13.5 : Application métier : revue des dépenses du premier trimestre au RCE

## 13.7 Prompts prêts à l'emploi

### Fiche P13.1 : Concevoir les tests analytiques d'un fichier de dépenses

**A. Titre.** Bibliothèque de tests analytiques pour un tableur.

**B. Objectif.** Obtenir les formules ou les étapes pour exécuter des tests ciblés sur toute une population de dépenses.

**C. Contexte d'utilisation.** Audit interne, contrôle de gestion, revue de fin de période.

**D. Données nécessaires.** Structure du fichier (colonnes) ; seuils de la procédure ; quelques lignes **fictives ou pseudonymisées** d'exemple.

**E. Prompt complet.**

```text
Contexte : je réalise une revue des dépenses d'une ASBL dans
[TABLEUR, LANGUE]. Colonnes : [LISTE]. Seuil d'autorisation et de bon
de commande : [SEUIL]. Un fichier fournisseurs séparé contient la
colonne code_fournisseur.
Tâche : propose une bibliothèque de tests analytiques.
Pour chaque test : objectif ; risque visé ; règle précise ; formule
exacte (colonne d'alerte « 1 si anomalie, 0 sinon ») avec la cellule
de départ ; limites et faux positifs probables.
Tests demandés : doublons (fournisseur + montant + libellé) ;
fournisseur absent du fichier fournisseurs ; pièce manquante ;
demandeur = approbateur ; fractionnement (au moins 2 dépenses sous le
seuil, même fournisseur, dans un délai de 7 jours, cumul au-dessus du
seuil) ; montants ronds au-dessus du seuil ; dépenses au-dessus du
seuil sans bon de commande ; libellés imprécis.
Ajoute une colonne « score » = somme pondérée des alertes, en
proposant des poids justifiés.
Limites : n'utilise que les colonnes listées ; signale les tests qui
nécessitent un tri préalable.
```

**F. Instructions d'utilisation.** Appliquez les formules sur une copie ; **testez chaque formule sur des lignes dont vous connaissez la réponse** (par exemple en créant volontairement un doublon) avant de l'appliquer à la population.

**G. Résultat attendu.** Une colonne d'alerte par test, un score de priorité, une liste de faux positifs probables.

**H. Exemple d'application.** Appliquée au fichier du RCE, la bibliothèque produit les résultats présentés en section 13.5 (22 opérations signalées). La formule de fractionnement proposée doit être vérifiée avec soin : c'est la plus sujette aux erreurs de fenêtre de dates.

**I. Méthode de vérification.** Contrôlez le total de la population ; recalculez manuellement deux alertes par test ; comparez avec un second moyen (tableau croisé par fournisseur et par semaine pour le fractionnement).

**J. Précautions.** Les fichiers de dépenses sont orange ; noms de personnes physiques à remplacer par des fonctions.

**K. Amélioration.** « Le test week-end produit trop de faux positifs pour nos activités de terrain. Propose un test plus discriminant pour les opérations atypiques (par exemple, dépenses saisies hors des jours d'activité planifiés). »

### Fiche P13.2 : Rédiger une feuille de travail

**A. Titre.** Projet de feuille de travail d'audit.

**B. Objectif.** Documenter les travaux de façon complète et revue.

**C. Contexte d'utilisation.** Après l'exécution des tests et l'examen des pièces.

**D. Données nécessaires.** Objectif ; population ; méthode ; résultats chiffrés ; notes d'examen (pseudonymisées).

**E. Prompt complet.**

```text
Contexte : audit interne de [PROCESSUS], période [PÉRIODE].
Données : <objectif>…</objectif> <population>…</population>
<methode>…</methode> <resultats>…</resultats> <notes>…</notes>
Tâche : rédige la feuille de travail.
Rubriques : Référence | Objectif | Population et source (avec contrôle
d'exhaustivité) | Méthode et critères | Résultats des tests (tableau) |
Priorisation et justification | Éléments examinés | Constats
(critère, constat, cause, conséquence) | Conclusion | Limites des
travaux | Préparé par / date | Revu par / date (laisser vide).
Règles : n'ajoute aucun fait absent des notes ; distingue faits
constatés et hypothèses ; n'emploie pas le mot « fraude » : écris
« indices nécessitant une investigation » lorsque c'est le cas.
```

**F. Instructions d'utilisation.** Remplacez les noms par des fonctions ; complétez et signez ; faites revoir.

**G. Résultat attendu.** Une feuille de travail complète, structurée, prudente dans sa formulation.

**H. Exemple d'application (illustratif).** La rubrique « Limites des travaux » obtenue précise : « Les tests ne couvrent que les dépenses comptabilisées ; une dépense non enregistrée ou une facture fictive cohérente avec la procédure ne serait pas détectée. »

**I. Méthode de vérification.** Chaque chiffre est pointé sur les résultats ; chaque fait sur les notes ; revue par un pair.

**J. Précautions.** Données orange, voire rouges en cas d'indices de fraude : outil validé exclusivement, ou rédaction manuelle.

**K. Amélioration.** « Ajoute un tableau de traçabilité "Constat → pièces examinées → référence d'archivage". »

### Fiche P13.3 : Formuler des recommandations actionnables

**A. Titre.** Recommandations SMART à partir des constats.

**B. Objectif.** Transformer des constats en recommandations claires, priorisées, attribuées et vérifiables.

**C. Contexte d'utilisation.** Rapport d'audit, revue de contrôle interne.

**D. Données nécessaires.** Constats (critère, constat, cause, conséquence) ; organigramme fonctionnel ; contraintes de ressources.

**E. Prompt complet.**

```text
Tâche : pour chaque constat ci-dessous, propose 1 à 3 recommandations.
Format : tableau « Constat | Recommandation (verbe d'action) |
Cause traitée | Priorité (élevée/moyenne/faible) et justification |
Responsable proposé (fonction) | Échéance proposée | Preuve de mise en
œuvre attendue | Coût ou effort estimé (faible/moyen/élevé) ».
Données : <constats>[CONSTATS]</constats>
<organisation>[FONCTIONS DISPONIBLES]</organisation>
Règles : chaque recommandation traite la cause, pas seulement le
symptôme ; privilégie des mesures proportionnées aux moyens d'une
ASBL de [TAILLE] ; signale si une recommandation exige une décision
du conseil d'administration.
```

**F. Instructions d'utilisation.** Discutez les propositions avec les responsables avant finalisation ; inscrivez les recommandations retenues au registre.

**G. Résultat attendu.** Un tableau de recommandations prêtes à être discutées.

**H. Exemple d'application (illustratif).** Pour la faiblesse T4, la proposition obtenue : « Modifier la procédure de caisse : approbation des dépenses de carburant par le coordinateur de projet ; alerte mensuelle automatique des auto-approbations (responsable : DAF) échéance : 31 mai : preuve : procédure révisée et rapport d'alertes de juin ».

**I. Méthode de vérification.** Chaque recommandation est-elle reliée à une cause ? réaliste ? vérifiable ?

**J. Précautions.** Ne pas désigner de personnes nommément dans le document de travail.

**K. Amélioration.** « Regroupe les recommandations par processus et indique les gains rapides réalisables en moins de 30 jours. »

## 13.8 Résultats attendus

Couverture complète de la population ; priorisation documentée ; trois constats et une faiblesse de contrôle étayés ; recommandations suivies ; tableau de bord des risques pour le comité d'audit.

## 13.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Priorisation, examen des pièces, conclusions, rédaction finale des constats, traitement des soupçons de fraude et suivi des recommandations relèvent du jugement de l'auditeur et des personnes habilitées. Les résultats des tests ne sont jamais diffusés comme des accusations.

## 13.10 Risques et erreurs à éviter

- Présenter des alertes comme des fraudes.
- Noyer les responsables sous des alertes non priorisées.
- Oublier les faux négatifs : ce que les tests ne cherchent pas, ils ne le trouvent pas.
- Ne pas contrôler l'exhaustivité de l'extraction.
- Utiliser un outil non autorisé pour des données d'audit.
- Formuler des recommandations sans responsable ni échéance.

## 13.11 Exercice pratique

**Consigne (3 heures).** À partir du fichier `depenses_RCE_T1_2026.csv` (annexes) : (1) reproduisez les tests T1, T2, T3 et T5 dans un tableur ; (2) comparez vos résultats au tableau de la section 13.5 ; (3) proposez un test remplaçant T7 ; (4) rédigez le constat complet pour D01/D13 (critère, constat, cause, conséquence, recommandation).

**Éléments de correction.** Vous devez retrouver : T1 = 8 opérations (4 paires) ; T2 = D24, D33 ; T3 = D18, D24, D31, D33 ; T5 = D16, D17, D18. Si votre test de doublons ne trouve que D01/D13, vous avez probablement inclus la date ou la référence de commande dans la clé : c'est un test plus strict (moins de faux positifs), défendable si vous le justifiez. Le constat D01/D13 relie le double paiement à l'absence de contrôle du numéro de facture et du bon de commande avant paiement, et recommande un contrôle bloquant dans le logiciel.

## 13.12 Synthèse

- Le contrôle interne s'apprécie d'abord par son environnement ; la cartographie des risques oriente les travaux.
- Les tests analytiques couvrent toute la population ; ils produisent des alertes, dont beaucoup sont des faux positifs.
- La priorisation, l'examen des pièces et les conclusions relèvent du jugement professionnel.
- Les constats suivent le schéma critère, constat, cause, conséquence, recommandation.
- Les recommandations sont suivies dans un registre et un tableau de bord des risques.

## 13.13 QCM : Module 13

**Q1.** (une seule réponse) Les *Global Internal Audit Standards* de l'IIA sont en vigueur depuis :

a) le 9 janvier 2025.
b) le 1er janvier 2013.
c) le 1er août 2024.
d) le 18 décembre 2023.

**Q2.** (une seule réponse) Un faux positif est :

a) une fraude non détectée.
b) un test qui n'a rien trouvé.
c) une erreur de saisie.
d) une opération signalée qui se révèle normale après examen.

**Q3.** (une ou plusieurs réponses) Quels tests visent un risque de fournisseur fictif ?

a) Fournisseur absent du fichier fournisseurs.
b) Libellé imprécis.
c) Montants ronds élevés.
d) Date de week-end uniquement.

**Q4.** (une seule réponse) Dans le cas du RCE, combien d'opérations ont été signalées par au moins un test ?

a) 8
b) 22
c) 12
d) 40

**Q5.** (une seule réponse) Le fractionnement consiste à :

a) découper un achat en plusieurs dépenses sous le seuil pour contourner une règle.
b) payer une facture en plusieurs fois selon le contrat.
c) répartir une dépense entre plusieurs projets.
d) arrondir les montants.

**Q6.** (une ou plusieurs réponses) Un constat d'audit complet comprend :

a) le critère.
b) la cause.
c) la conséquence.
d) le nom de la personne fautive.

**Q7.** (mise en situation, une seule réponse) Deux dépenses de 5 500 UM au total, sans pièce, auprès d'un fournisseur absent de la base, approuvées par le demandeur. Que fait l'auditrice ?

a) Elle conclut à une fraude dans son rapport.
b) Elle interroge immédiatement le demandeur devant l'équipe.
c) Elle applique la politique de lutte contre la fraude : information confidentielle des personnes habilitées, préservation des preuves, pas de conclusion hâtive.
d) Elle ignore l'alerte faute de preuve.

**Q8.** (mise en situation, une seule réponse) Le test « week-end » signale 12 opérations, presque toutes liées à des activités de terrain normales. Que faites-vous ?

a) Vous examinez quand même les 12 en détail chaque trimestre.
b) Vous documentez sa faible pertinence et le remplacez ou l'affinez.
c) Vous le gardez pour avoir plus d'alertes.
d) Vous supprimez toutes les opérations du week-end.

**Q9.** (une seule réponse) Avant d'exécuter des tests, il faut vérifier :

a) l'exhaustivité de l'extraction (total = grand livre).
b) la couleur du fichier.
c) le nombre de colonnes.
d) le nom de l'outil d'IA.

**Q10.** (une ou plusieurs réponses) Le rôle de l'IA dans cette démarche peut être de :

a) écrire les formules ou le script des tests.
b) rapprocher des noms de fournisseurs proches.
c) rédiger un projet de feuille de travail.
d) conclure sur la culpabilité d'une personne.

## 13.14 Corrigé détaillé : Module 13

**Q1 : a.** Publiées le 9 janvier 2024, elles sont en vigueur depuis le 9 janvier 2025.

**Q2 : d.** D'où l'importance de la priorisation et de l'examen.

**Q3 : a, b, c.** La date de week-end seule (d) n'est pas un indicateur de fournisseur fictif.

**Q4 : b.** 22 opérations sur 40, dont de nombreux faux positifs ; 8 ont été examinées en priorité.

**Q5 : a.** C'est un contournement des seuils d'autorisation ou de mise en concurrence.

**Q6 : a, b, c.** Le constat porte sur des faits et des processus, pas sur la désignation de coupables.

**Q7 : c.** Les indices de fraude exigent une procédure rigoureuse et confidentielle.

**Q8 : b.** Un test peu discriminant use l'attention et doit être amélioré.

**Q9 : a.** Sans exhaustivité, la couverture « 100 % » est illusoire.

**Q10 : a, b, c.** La conclusion (d) relève de l'auditeur et des instances habilitées.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Association of Certified Fraud Examiners. (2024). *Occupational Fraud 2024: A Report to the Nations*.
- COSO. (2013). *Internal Control : Integrated Framework*.
- The Institute of Internal Auditors. (2024). *Global Internal Audit Standards*.


# Module 14 : Ressources humaines et gestion des bénévoles {#h18}

## 14.1 Mise en situation

Horizons Partagés doit recruter un ou une chargé(e) de suivi-évaluation. La dernière offre avait attiré 260 candidatures, reçues par courriel, sur WhatsApp et sur papier. La responsable RH, Claire, avait passé deux semaines à les trier, sans grille commune, et deux excellents profils avaient été oubliés dans une boîte de réception. Un prestataire propose désormais un outil « qui classe automatiquement les candidats par score d'adéquation ».

À la Maison des Aînés Solidaires, le problème est différent : 80 bénévoles, des disponibilités qui changent chaque semaine, des personnes âgées qui attendent une visite qui n'a pas été planifiée, et un coordinateur qui passe ses dimanches soir à faire des tableaux.

## 14.2 Problématique

Les fonctions RH et bénévolat combinent une forte charge administrative (annonces, tri, plannings, formations, documents) et des décisions particulièrement sensibles, qui touchent directement des personnes : recrutement, évaluation, rémunération, sanctions. L'IA peut alléger la première ; elle ne doit pas s'approprier les secondes. Les systèmes de tri automatique de candidatures peuvent reproduire des discriminations, et de nombreuses législations encadrent les décisions automatisées en matière d'emploi : le règlement européen sur l'IA range d'ailleurs certains systèmes d'IA utilisés pour le recrutement et la gestion du personnel parmi les systèmes à haut risque.

## 14.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. rédiger une fiche de poste et une annonce inclusives avec l'aide de l'IA ;
2. organiser la réception et l'examen des candidatures selon une grille humaine, sans tri automatique injuste ;
3. préparer des entretiens structurés ;
4. concevoir un parcours d'intégration et de formation fondé sur les compétences ;
5. planifier les bénévoles et suivre les absences ;
6. organiser la transmission des connaissances ;
7. concevoir un assistant RH aux limites clairement définies.

## 14.4 Notions et définitions

- **Fiche de poste** : description de la mission, des responsabilités, des compétences et des conditions d'un emploi.
- **Grille de sélection** : critères objectifs, pondérés, définis **avant** l'examen des candidatures, et appliqués de la même façon à tous.
- **Entretien structuré** : entretien dont les questions et les critères d'évaluation sont fixés à l'avance et identiques pour tous les candidats.
- **Référentiel de compétences** : liste des compétences attendues par fonction, avec niveaux.
- **Biais de recrutement** : préférences non liées aux compétences (âge, sexe, origine, école, nom, apparence, handicap, situation familiale) qui influencent les décisions.

> **⚖️ Adaptation réglementaire** : Le droit du travail, le droit de la non-discrimination, les règles relatives aux bénévoles (assurance, remboursement de frais, statut) et la protection des données des candidats et du personnel diffèrent selon les pays. Les durées de conservation des candidatures non retenues, en particulier, sont souvent encadrées.

## 14.5 Explications détaillées

![Figure 14.1 : Recrutement assisté : où l'IA aide, où l'humain décide](03_ILLUSTRATIONS/figures/fig_14_1.svg){#fig-14-1}

### Fiches de poste et annonces

L'IA est utile pour structurer une fiche de poste à partir des besoins exprimés, harmoniser les fiches existantes, simplifier le langage, et vérifier le caractère inclusif d'une annonce (fiche P8.2). Points d'attention : distinguer les exigences **indispensables** des exigences **souhaitables** (les listes trop longues découragent des candidatures qualifiées) ; éviter les critères non nécessaires (années d'expérience excessives, diplômes non requis par la fonction) ; préciser les conditions (rémunération ou fourchette si la politique le permet, lieu, accessibilité).

### Recevoir et examiner les candidatures

1. **Canal unique** (formulaire ou adresse dédiée), accusé de réception automatique, information sur le traitement des données.
2. **Grille de sélection définie avant l'ouverture**, avec 4 à 6 critères liés au poste, pondérés, et une échelle décrite.
3. **Examen humain** de chaque candidature selon la grille, si possible par deux personnes pour les postes clés.
4. L'IA peut **organiser** l'information (extraire dans un tableau les éléments factuels : diplômes déclarés, années d'expérience déclarées, langues), à condition d'utiliser un outil autorisé, mais **le classement et la présélection sont humains**.
5. **Anonymisation partielle** possible au premier tri (masquer nom, âge, photo, adresse) pour limiter les biais.
6. **Réponse à tous les candidats**, y compris non retenus, dans un délai annoncé.

> **🛑 Contrôle humain obligatoire** : Aucune candidature n'est écartée par un système automatique. Les personnes chargées du recrutement lisent les candidatures, appliquent la grille et motivent leurs décisions.

### Entretiens

L'IA peut proposer des questions comportementales et de mise en situation liées à chaque critère, ainsi qu'une échelle d'évaluation décrite (fiche P14.2). Elle ne doit ni analyser les vidéos ou la voix des candidats, ni « évaluer » leurs réponses à la place du jury.

### Formation et compétences

Un parcours de formation se construit à partir de l'écart entre les compétences requises (référentiel) et les compétences constatées. L'IA aide à : proposer un plan d'intégration ; transformer une procédure en module de formation court avec quiz ; adapter des contenus au niveau des apprenants ; produire des supports pour les bénévoles. Le plan de formation est validé par le responsable hiérarchique et la personne elle-même.

### Plannings et absences

La planification des bénévoles (fiche P14.3) combine des contraintes : disponibilités, compétences, proximité, préférences des personnes accompagnées, continuité de la relation. Les outils de planification et les tableurs résolvent l'essentiel ; l'IA aide à construire le modèle, à proposer un premier planning à partir de disponibilités **pseudonymisées**, et à rédiger les messages. Le suivi des absences du personnel relève d'outils RH classiques ; les **motifs** d'absence (santé) sont des données sensibles qui n'ont rien à faire dans un outil d'IA externe.

### Bénévoles

Le cycle du bénévolat comprend : recrutement, accueil et intégration, formation, planification, accompagnement, reconnaissance, départ. Les bénévoles sont souvent la mémoire et le visage de l'organisation. L'IA peut aider à produire des guides d'accueil, des FAQ, des messages de remerciement personnalisés à partir d'informations non sensibles, et des certificats d'engagement.

### Évaluation

L'évaluation annuelle du personnel est une décision humaine. L'IA peut aider le manager à **structurer** ses notes (faits, réalisations, objectifs), à **reformuler** un retour de façon constructive, et à préparer des objectifs SMART. Elle ne doit pas noter les personnes, ni analyser leurs courriels ou leur activité pour en déduire une performance.

### Transmission des connaissances

Avant un départ : entretien de passation enregistré **avec accord**, transcrit, synthétisé en procédures et en « questions fréquentes » ; liste des dossiers en cours ; contacts clés ; accès à transférer ou à fermer. L'assistant documentaire de l'organisation (module 10, RAG) peut ensuite rendre ces connaissances accessibles aux nouveaux arrivants.

### L'assistant RH

Un assistant RH interne peut répondre aux questions générales du personnel et des bénévoles à partir des documents RH **validés** (règlement intérieur, politique de congés, procédure de remboursement, guide du bénévole) : « Combien de jours de congé après un an ? », « Comment me faire rembourser un trajet ? ». Règles : réponses sourcées ; pas d'accès aux dossiers individuels ; orientation vers une personne pour toute situation particulière, tout conflit, toute question de santé ou de harcèlement ; mise à jour à chaque révision des politiques.

## 14.6 Application métier : recruter un(e) chargé(e) de suivi-évaluation

**A. Contexte.** Fondation de 60 salariés ; recrutement d'un poste clé ; volume élevé de candidatures attendu.
**B. Problème.** Tri lent, non homogène, candidatures perdues.
**C. Symptômes.** Deux semaines de tri ; aucun critère écrit ; candidatures dispersées.
**D. Causes profondes.** Pas de canal unique ; pas de grille ; pas de modèle d'annonce.
**E. Processus actuel.** Annonce rédigée à partir d'une ancienne ; réception multicanal ; tri individuel.
**F. Faiblesses.** Risque de discrimination ; perte de candidatures ; absence de traçabilité des décisions.
**G. Résultat recherché.** Processus équitable, traçable, en 4 semaines, réponse à 100 % des candidats.
**H. Pertinence de l'IA.** Pour la rédaction (fiche de poste, annonce, questions d'entretien, messages) et l'organisation de l'information ; **non** pour la sélection.
**I. Alternatives sans IA.** Modèles internes de fiche de poste et de grille.
**J. Solution.** Fiche de poste et annonce assistées ; formulaire unique ; grille de sélection humaine ; entretiens structurés ; messages assistés.
**K. Niveau.** Débutant à Intermédiaire.
**L. Outils.** Assistant, formulaire de candidature, tableur de suivi (accès restreint), modèles de messages.
**M. Étapes détaillées.**

1. Valider le besoin et le budget du poste (direction).
2. Fiche P14.1 : projet de fiche de poste et d'annonce ; revue d'inclusion (P8.2).
3. Définir la grille de sélection (5 critères pondérés) **avant** publication ; la faire valider.
4. Publier ; recevoir via un formulaire unique ; accusé de réception automatique.
5. Tableur de suivi : une ligne par candidature (code, date, canal, statut), accès limité à la RH et au jury.
6. Premier examen par deux personnes selon la grille ; scores et motifs consignés.
7. Fiche P14.2 : guide d'entretien structuré.
8. Entretiens ; évaluation individuelle par chaque membre du jury, puis délibération.
9. Décision par la personne habilitée ; vérification des références avec l'accord du candidat.
10. Messages à tous les candidats (modèles assistés, envoi humain).
11. Plan d'intégration de la personne recrutée (formation, mentor, 90 jours).
12. Suppression des données des candidats non retenus à l'échéance fixée par la politique.

**N. Prompts.** P14.1, P14.2, P14.3.
**O. Exemple de résultat.** Voir les fiches.
**P. Vérification.** Revue d'inclusion de l'annonce ; validation de la grille ; double lecture.
**Q. Contrôles humains.** Toutes les décisions de présélection, d'entretien et de recrutement.
**R. Risques.** Discrimination ; données de candidats dans des outils non autorisés ; décisions non motivées.
**S. Coûts et maintenance.** Temps ; formulaire et tableur existants ; logiciel de recrutement éventuel (niveau intermédiaire).
**T. Indicateurs.** Délai de recrutement ; pourcentage de candidats ayant reçu une réponse ; diversité des candidatures ; taux de maintien à 12 mois.
**U. Amélioration continue.** Bilan de chaque recrutement ; ajustement des modèles et de la grille.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Fiches de poste, annonces, questions d'entretien et messages assistés ; grille et suivi en tableur ; plannings de bénévoles en tableur | Assistant, tableur, formulaire | Faibles | Saisie manuelle |
| Intermédiaire | Logiciel de gestion des candidatures (sans classement automatique), outil de planification des bénévoles avec application mobile, base de connaissances RH | Logiciel RH, outil de planification | Abonnements | Paramétrage ; protection des données |
| Avancé | SIRH intégré (paie, congés, compétences, formation), assistant RH RAG sur documents validés, tableaux de bord RH agrégés | SIRH, RAG | Élevés | Données sensibles ; obligations légales renforcées |

Table: Tableau 14.1 : Application métier : recruter un(e) chargé(e) de suivi-évaluation

## 14.7 Prompts prêts à l'emploi

### Fiche P14.1 : Fiche de poste et annonce inclusives

**A. Titre.** Fiche de poste et annonce.

**B. Objectif.** Produire une fiche de poste claire et une annonce inclusive, distinguant exigences indispensables et souhaitables.

**C. Contexte d'utilisation.** Ouverture d'un poste salarié ou d'une mission bénévole.

**D. Données nécessaires.** Mission du poste ; responsabilités ; rattachement ; compétences ; conditions ; valeurs de l'organisation.

**E. Prompt complet.**

```text
Contexte : [NOM DE L'ASBL], [SECTEUR], recrute un(e) [INTITULÉ]
rattaché(e) à [FONCTION], basé(e) à [LIEU], [TYPE DE CONTRAT].
Besoins : <besoins>[MISSION, RESPONSABILITÉS, RÉSULTATS ATTENDUS]</besoins>
Tâche :
1. Rédige la fiche de poste : finalité (2 phrases) ; 5 à 7
   responsabilités principales ; compétences indispensables (5 max) ;
   compétences souhaitables (4 max) ; conditions.
2. Rédige l'annonce (350 mots max), en langage simple, avec une
   phrase encourageant les candidatures de profils divers et une
   information sur l'accessibilité et l'aménagement des entretiens.
3. Liste les exigences qui pourraient exclure des candidats sans être
   nécessaires au poste, et propose une alternative.
Limites : aucune exigence liée à l'âge, au sexe, à l'origine, à la
situation familiale ou à l'apparence ; formulation inclusive.
```

**F. Instructions d'utilisation.** Faites valider la fiche par le responsable hiérarchique ; vérifiez la conformité avec la grille salariale et le droit applicable.

**G. Résultat attendu.** Une fiche de poste, une annonce, une liste d'exigences à reconsidérer.

**H. Exemple d'application (illustratif).** Pour le poste de chargé(e) de S&E, la troisième rubrique signale : « "Master en statistiques exigé" : peut exclure des profils expérimentés formés autrement. Alternative : "formation supérieure en statistiques, santé publique ou sciences sociales, ou expérience équivalente en analyse de données". »

**I. Méthode de vérification.** Revue par la RH ; revue d'inclusion (P8.2) ; vérification des conditions contractuelles.

**J. Précautions.** Données vertes à orange (pas de données personnelles).

**K. Amélioration.** « Rédige une version courte (80 mots) pour les réseaux sociaux et une version audio de 45 secondes pour la radio communautaire. »

### Fiche P14.2 : Guide d'entretien structuré

**A. Titre.** Guide d'entretien structuré et échelle d'évaluation.

**B. Objectif.** Garantir des entretiens équitables, comparables et centrés sur les compétences.

**C. Contexte d'utilisation.** Préparation d'un jury de recrutement.

**D. Données nécessaires.** Fiche de poste ; grille de sélection (critères et poids).

**E. Prompt complet.**

```text
Contexte : jury de recrutement pour [POSTE].
Grille : <grille>[CRITÈRES ET POIDS]</grille>
Tâche : rédige un guide d'entretien de 45 minutes.
Pour chaque critère : 2 questions comportementales (« Décrivez une
situation où… ») et 1 mise en situation liée au contexte d'une ASBL ;
indicateurs observables d'une réponse faible / satisfaisante /
excellente (échelle 1-3-5 décrite) ; relances possibles.
Ajoute : une introduction standard ; le temps par partie ; les
questions interdites ou à éviter (vie privée, projets familiaux, santé,
religion, origine…) ; une fiche d'évaluation individuelle vierge.
```

**F. Instructions d'utilisation.** Utilisez le même guide pour tous les candidats ; chaque membre du jury note seul avant la délibération.

**G. Résultat attendu.** Un guide minuté, une échelle décrite, une liste de questions à éviter, une fiche d'évaluation.

**H. Exemple d'application (illustratif).** Pour le critère « analyse de données », la mise en situation proposée : « Les données de deux villages montrent une hausse soudaine de 40 % des visites en un mois. Comment vérifiez-vous s'il s'agit d'un vrai changement ou d'une erreur de collecte ? »

**I. Méthode de vérification.** Lien de chaque question avec un critère ; absence de questions discriminatoires ; test du guide par un collègue.

**J. Précautions.** Aucune donnée de candidat dans la consigne.

**K. Amélioration.** « Adapte le guide pour un entretien à distance avec une connexion instable (questions envoyées à l'avance, durée réduite). »

### Fiche P14.3 : Planning hebdomadaire des bénévoles

**A. Titre.** Proposition de planning à partir de disponibilités pseudonymisées.

**B. Objectif.** Obtenir un premier planning respectant les contraintes, à ajuster par le coordinateur.

**C. Contexte d'utilisation.** Coordination des bénévoles, visites, permanences.

**D. Données nécessaires.** Liste des besoins (créneaux, lieux, compétences) ; disponibilités des bénévoles **sous code** (B01, B02…) ; contraintes (maximum de créneaux, continuité des binômes).

**E. Prompt complet.**

```text
Contexte : planification des visites de la semaine du [DATE].
Besoins : <besoins>[CODE PERSONNE ACCOMPAGNÉE (P01…) | créneau
souhaité | zone | compétence requise | bénévole habituel]</besoins>
Disponibilités : <dispo>[CODE BÉNÉVOLE | créneaux | zones | compétences
| maximum de visites]</dispo>
Règles : priorité à la continuité (bénévole habituel) ; pas plus de
[N] visites par bénévole ; compétence requise respectée ; zones
compatibles.
Tâche : propose un planning sous forme de tableau « Créneau | P | B |
Zone | Règle appliquée ». Liste ensuite les besoins non couverts et
les conflits, avec des options de résolution.
Limites : n'affecte jamais un bénévole hors de ses disponibilités ;
signale toute règle impossible à respecter.
```

**F. Instructions d'utilisation.** Gardez la table de correspondance des codes hors de l'outil ; reportez le planning validé dans l'outil de l'association.

**G. Résultat attendu.** Un planning, une liste de besoins non couverts et de conflits.

**H. Exemple d'application (illustratif).** Le planning couvre 46 visites sur 50 ; il signale que P07 et P12 demandent le même créneau dans des zones éloignées pour le même bénévole habituel B03, et propose de déplacer P12 au jeudi avec l'accord de la personne.

**I. Méthode de vérification.** Contrôle de chaque affectation par rapport aux disponibilités ; comptage des visites par bénévole dans le tableur.

**J. Précautions.** Aucun nom, adresse, information de santé ou de dépendance dans l'outil.

**K. Amélioration.** « Rédige les messages de confirmation pour chaque bénévole (avec codes ; je remplacerai par les prénoms). »

## 14.8 Résultats attendus

Recrutements plus rapides, équitables et traçables ; candidats informés ; plannings de bénévoles fiables ; parcours d'intégration et de formation structurés ; connaissances transmises.

## 14.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Présélection, entretiens, décisions de recrutement, évaluations, rémunérations, sanctions, acceptation ou exclusion de bénévoles : décisions exclusivement humaines, motivées et traçables. Aucune analyse automatisée de la voix, du visage, de la personnalité ou des communications du personnel.

## 14.10 Risques et erreurs à éviter

- Utiliser un outil de « score d'adéquation » pour écarter des candidatures.
- Coller des CV dans un outil non autorisé.
- Laisser l'IA rédiger des critères discriminatoires sans revue.
- Analyser les messages ou l'activité des salariés pour évaluer leur performance.
- Conserver indéfiniment les candidatures non retenues.
- Oublier les bénévoles dans les politiques de protection des données et d'utilisation de l'IA.

## 14.11 Exercice pratique

**Consigne (2 heures).** Pour un poste ou une mission bénévole de votre organisation : (1) appliquez P14.1 ; (2) définissez une grille de 5 critères pondérés ; (3) appliquez P14.2 ; (4) listez les décisions réservées à l'humain et les données à ne jamais soumettre à un outil.

**Éléments de correction.** Les exigences sont justifiées par le poste ; la grille est définie avant l'examen ; les questions d'entretien sont liées aux critères ; la liste des décisions réservées couvre au minimum la présélection, la décision et la réponse aux candidats ; les données exclues comprennent CV nominatifs, informations de santé et références.

## 14.12 Synthèse

- L'IA allège la rédaction, l'organisation et la planification ; elle ne sélectionne, n'évalue ni ne sanctionne.
- Une grille définie à l'avance et des entretiens structurés limitent les biais.
- Les données des candidats, du personnel et des bénévoles sont protégées et minimisées.
- La transmission des connaissances se prépare avant les départs.

## 14.13 QCM : Module 14

**Q1.** (une seule réponse) Une grille de sélection doit être définie :

a) après avoir lu les candidatures.
b) avant l'examen des candidatures et appliquée à tous.
c) par l'outil d'IA.
d) uniquement pour les postes de direction.

**Q2.** (une ou plusieurs réponses) Quelles tâches l'IA peut-elle assister dans un recrutement ?

a) Rédiger un projet de fiche de poste.
b) Proposer des questions d'entretien structurées.
c) Écarter automatiquement les candidatures à faible score.
d) Préparer les modèles de messages aux candidats.

**Q3.** (une seule réponse) Un entretien structuré se caractérise par :

a) des questions improvisées selon le candidat.
b) une durée libre.
c) l'absence de notation.
d) des questions et des critères fixés à l'avance, identiques pour tous.

**Q4.** (une ou plusieurs réponses) Questions à éviter en entretien :

a) projets familiaux.
b) état de santé sans lien avec une exigence légale du poste.
c) expérience d'analyse de données.
d) religion.

**Q5.** (une seule réponse) Les motifs médicaux d'absence du personnel :

a) peuvent être analysés par un assistant gratuit.
b) sont des données sensibles, à exclure des outils d'IA externes.
c) doivent être publiés dans le planning.
d) ne sont pas des données personnelles.

**Q6.** (une seule réponse) Un assistant RH interne doit :

a) répondre à partir des documents validés et orienter vers une personne pour les situations particulières.
b) accéder aux dossiers individuels pour répondre précisément.
c) traiter les signalements de harcèlement.
d) décider des congés.

**Q7.** (mise en situation, une seule réponse) Un prestataire propose un classement automatique des 260 candidatures. Votre réponse ?

a) Accepter pour gagner du temps.
b) Accepter si le prestataire garantit l'absence de biais.
c) Ne retenir que les 20 premiers.
d) Refuser le classement automatique ; éventuellement utiliser un outil pour organiser l'information factuelle, l'examen restant humain selon la grille.

**Q8.** (mise en situation, une seule réponse) Pour planifier les visites, le coordinateur veut coller la liste des personnes âgées avec adresses et pathologies dans un assistant. Que recommandez-vous ?

a) Le faire si l'outil est payant.
b) Le faire puis supprimer la conversation.
c) Utiliser des codes et seulement les informations nécessaires (zones, créneaux, compétences), sans pathologies.
d) Demander l'accord oral des bénévoles.

**Q9.** (une seule réponse) La revue d'inclusion d'une annonce vise à :

a) raccourcir l'annonce.
b) repérer les formulations ou exigences qui excluraient sans nécessité des candidats.
c) traduire l'annonce.
d) augmenter le nombre d'exigences.

**Q10.** (une ou plusieurs réponses) Bonnes pratiques de transmission des connaissances :

a) entretien de passation avec accord, transcrit et synthétisé.
b) liste des dossiers en cours et des contacts clés.
c) transfert ou fermeture des accès.
d) conservation des mots de passe personnels du partant.

## 14.14 Corrigé détaillé : Module 14

**Q1 : b.** Définie à l'avance, elle limite les biais et garantit l'égalité de traitement.

**Q2 : a, b, d.** L'élimination automatique (c) est exclue.

**Q3 : d.** Questions et critères identiques permettent la comparaison.

**Q4 : a, b, d.** L'expérience d'analyse de données (c) est liée au poste.

**Q5 : b.** Données de santé : rouge.

**Q6 : a.** L'assistant informe ; les situations particulières, les conflits et le harcèlement relèvent de personnes formées.

**Q7 : d.** Un classement automatique expose à la discrimination et, dans plusieurs juridictions, à des obligations légales renforcées.

**Q8 : c.** Minimisation et pseudonymisation ; les pathologies sont inutiles pour la planification.

**Q9 : b.** C'est l'objectif de la revue (fiche P8.2).

**Q10 : a, b, c.** Les mots de passe personnels (d) ne se transmettent pas : les accès sont réattribués.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Règlement (UE) 2024/1689 (AI Act), annexe III (systèmes à haut risque, dont certains usages dans l'emploi), tel que modifié en 2026.
- Règlement (UE) 2016/679 (RGPD), article 22.


# Module 15 : Recherche de financements, partenariats et relations avec les bailleurs {#h19}

## 15.1 Mise en situation

Lumière des Collines dépend à 70 % d'un seul bailleur, dont la convention expire dans dix-huit mois. Amina, la coordinatrice, sait qu'il faut diversifier les ressources, mais elle n'a ni le temps de surveiller les appels à projets, ni l'expérience des dossiers complexes. Lorsqu'un appel intéressant apparaît, elle le découvre souvent trois jours avant la date limite.

À Horizons Partagés, le problème inverse se pose : l'équipe répond à beaucoup d'appels, presque tous en urgence, avec des taux de succès faibles, et sans vérifier suffisamment l'éligibilité. Deux dossiers ont été rejetés l'an dernier pour des critères administratifs non remplis.

## 15.2 Problématique

La recherche de financements combine veille, analyse, stratégie, rédaction et calculs budgétaires, dans des délais serrés. L'IA peut élargir la veille, accélérer l'analyse des appels et la production de premiers jets. Mais les bailleurs attendent des propositions **spécifiques**, fondées sur des réalités de terrain, avec des budgets réalistes ; les dossiers génériques et les erreurs d'éligibilité se repèrent vite. Certains bailleurs demandent désormais aux candidats de déclarer l'usage de l'IA dans la préparation des dossiers.

## 15.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. cartographier les sources de financement et construire une stratégie de diversification ;
2. organiser une veille efficace ;
3. analyser un appel à projets et vérifier l'éligibilité de façon rigoureuse ;
4. prendre une décision de candidature (go/no-go) argumentée ;
5. produire une note conceptuelle et une proposition avec l'aide de l'IA, sans perdre la spécificité ;
6. construire un budget conforme ;
7. gérer conventions, partenariats et reporting.

## 15.4 Notions et définitions

- **Appel à projets / appel à propositions** : invitation d'un bailleur à soumettre des projets selon des critères définis.
- **Critères d'éligibilité** : conditions à remplir pour que le dossier soit recevable (statut juridique, ancienneté, zone, montant, cofinancement, documents).
- **Critères d'évaluation** : critères selon lesquels les dossiers recevables sont notés.
- **Note conceptuelle** : document court (2 à 5 pages) présentant l'idée de projet, souvent première étape d'une sélection en deux temps.
- **Cofinancement** : part du budget financée par d'autres sources que le bailleur sollicité.
- **Convention de financement** : contrat qui fixe les obligations des parties (objet, budget, règles d'éligibilité, rapports, audits, visibilité, résiliation).

## 15.5 Explications détaillées

### Sources de financement et diversification

| Source | Caractéristiques | Points de vigilance |
|---|---|---|
| Bailleurs institutionnels (agences de coopération, organisations internationales, collectivités) | Montants importants, procédures lourdes | Exigences de reporting, cofinancement, règles d'éligibilité strictes |
| Fondations privées | Procédures variables, relations de confiance | Alignement stratégique |
| Entreprises (mécénat, partenariats) | Financements, dons en nature, compétences | Cohérence avec les valeurs, risques de réputation |
| Dons individuels | Ressources souvent non affectées | Coût de collecte, protection des données des donateurs |
| Cotisations des membres | Stabilité, gouvernance | Montants modestes |
| Activités génératrices de revenus | Autonomie | Règles fiscales et statutaires, à vérifier |
| Financement participatif | Visibilité | Effort de communication |

Table: Tableau 15.1 : Explications détaillées

Une stratégie de diversification fixe des objectifs (par exemple : aucun bailleur au-delà de 40 % du budget dans trois ans ; 15 % de ressources non affectées), identifie les sources cibles, et affecte du temps à la prospection de façon régulière.

### La veille

![Figure 15.1 : Entonnoir des opportunités de financement](03_ILLUSTRATIONS/figures/fig_15_1.svg){#fig-15-1}

Une veille efficace combine : abonnements aux lettres d'information des bailleurs et des plateformes d'appels ; alertes de recherche ; réseaux et plateformes de coordination sectorielle ; contacts réguliers avec les bailleurs. L'IA aide à **traiter le volume** : résumer chaque appel en une fiche standard (objet, zones, montants, éligibilité, échéances), le comparer au profil de l'organisation, et alimenter un tableau de veille. Elle ne remplace pas la lecture des documents officiels de l'appel avant toute décision.

### Analyse d'éligibilité

L'éligibilité est **binaire** et souvent éliminatoire. Toute erreur coûte un dossier entier. L'analyse se fait **critère par critère, sur le texte officiel**, avec la preuve correspondante :

| Critère (texte de l'appel) | Notre situation | Preuve | Statut |
|---|---|---|---|
| Organisation enregistrée depuis au moins 3 ans | Enregistrée en 2018 | Récépissé d'enregistrement | ✅ |
| Budget annuel moyen ≥ 500 000 UM sur les 3 derniers exercices | 3 200 000 UM | Comptes certifiés | ✅ |
| Intervention dans au moins 2 des pays listés | 1 seul pays | Néant | ❌ éliminatoire sans partenaire |
| Cofinancement d'au moins 10 % | À confirmer | Lettre d'engagement d'un autre bailleur | ⚠️ |

Table: Tableau 15.2 : Explications détaillées

### Décision go / no-go

Une grille simple aide à décider : éligibilité (éliminatoire) ; alignement stratégique ; capacité à mettre en œuvre ; probabilité de succès (concurrence, connaissance du bailleur) ; coût de préparation ; exigences de gestion (audit, cofinancement, préfinancement de trésorerie). La décision appartient à la direction.

### Note conceptuelle et proposition

L'IA est précieuse pour : structurer la note selon le modèle du bailleur ; reformuler et condenser ; vérifier la cohérence entre narration, cadre logique et budget ; adapter le style aux attentes. Mais **la substance** (analyse du contexte, preuves, choix d'intervention, partenariats, enseignements des projets passés) doit venir de l'organisation. Une bonne méthode : rédiger d'abord un **dossier de matière première** (données, enseignements, témoignages anonymisés, résultats passés, partenaires), puis demander à l'IA de le mettre en forme selon le modèle.

> **🔎 À retenir** : Un dossier généré à partir d'une consigne vague ressemble à des centaines d'autres. La valeur de votre proposition tient à ce que vous seul pouvez apporter : votre connaissance du terrain et vos résultats.

### Budgets

Voir module 11 : formules, coûts documentés, règles d'éligibilité, taux de coûts indirects autorisé, cofinancement, cohérence avec les activités. L'IA aide à vérifier la cohérence entre lignes budgétaires et activités, et à rédiger la note justificative du budget.

### Partenariats et conventions

Avant de signer une convention, il faut en extraire les **obligations** : périodes, règles d'éligibilité, échéances des rapports, audits, règles de visibilité, propriété des biens, règles d'achat, clauses de résiliation, protection des données, éventuelles exigences sur l'usage de l'IA. L'IA peut produire une **fiche de synthèse des obligations** (à vérifier sur le texte) qui alimente le calendrier des obligations (module 10) et le paramétrage comptable (module 12). Pour les partenariats opérationnels, l'accord précise les rôles, les flux financiers, les responsabilités, le partage des données et la gestion des différends.

### Reporting et relation avec les bailleurs

Un reporting de qualité, ponctuel et honnête, est le meilleur argument pour un renouvellement. Voir modules 11 (rapports narratifs) et 12 (rapports financiers). Entre les rapports, une communication régulière (nouvelles du terrain, difficultés anticipées) entretient la confiance.

## 15.6 Application métier : de l'appel à projets à la note conceptuelle

**A. Contexte.** Horizons Partagés ; appel à propositions « Santé communautaire et résilience climatique » d'une fondation (fictive) ; note conceptuelle de 4 pages demandée.
**B. Problème.** Taux de succès faible ; rejets pour inéligibilité ; dossiers en urgence.
**C. Symptômes.** 2 rejets administratifs sur 9 dossiers l'an dernier ; 7 dossiers rédigés en moins d'une semaine.
**D. Causes profondes.** Pas de veille anticipée ; pas d'analyse systématique d'éligibilité ; pas de matière première prête ; pas de go/no-go.
**E. Processus actuel.** Découverte tardive → rédaction en urgence → soumission.
**F. Faiblesses.** Erreurs d'éligibilité ; propositions génériques ; épuisement de l'équipe.
**G. Résultat recherché.** Zéro rejet administratif ; décision go/no-go pour chaque appel ; notes conceptuelles prêtes 5 jours avant l'échéance.
**H. Pertinence de l'IA.** Forte pour la veille, l'extraction des critères, la structuration et la reformulation ; faible pour la substance et les décisions.
**I. Alternatives sans IA.** Tableau de veille et checklist d'éligibilité manuels.
**J. Solution.** Veille assistée + fiche d'analyse standard + checklist d'éligibilité avec preuves + go/no-go + dossier de matière première + rédaction assistée + relecture croisée.
**K. Niveau.** Débutant à Intermédiaire.
**L. Outils.** Assistant, tableur de veille, espace documentaire (preuves administratives à jour), modèles.
**M. Étapes détaillées.**

1. Constituer le **dossier administratif permanent** (statuts, enregistrement, comptes, rapports d'audit, CV clés, références) et le tenir à jour.
2. Constituer le **dossier de matière première** par thématique (données, résultats, enseignements, photos avec consentement).
3. Veille hebdomadaire ; chaque appel pertinent est résumé avec la fiche P15.1 et inscrit au tableau.
4. Analyse d'éligibilité critère par critère sur le texte officiel, avec preuves (fiche P15.1, partie 2).
5. Go/no-go en comité de direction.
6. Rédaction de la note conceptuelle (fiche P15.2) à partir du dossier de matière première.
7. Budget (fiche P15.3) et vérification de cohérence.
8. Relecture croisée (programmes, finances, direction) ; vérification de chaque chiffre et de chaque engagement.
9. Déclaration de l'usage de l'IA si le bailleur l'exige.
10. Soumission avant J-2 ; archivage du dossier soumis.

**N. Prompts.** P15.1, P15.2, P15.3.
**O. Exemple de résultat.** Voir les fiches.
**P. Vérification.** Éligibilité vérifiée sur le texte officiel ; chiffres pointés ; engagements validés par la direction.
**Q. Contrôles humains.** Go/no-go ; substance du projet ; budget ; signature et soumission.
**R. Risques.** Dossier générique ; engagement irréaliste ; chiffres non vérifiés ; non-respect des règles du bailleur sur l'IA ; données de bénéficiaires dans les outils.
**S. Coûts et maintenance.** Temps de veille (2 heures par semaine) ; abonnements éventuels à des plateformes de veille.
**T. Indicateurs.** Nombre d'appels analysés ; taux de go ; taux de succès ; rejets administratifs ; part du premier bailleur dans le budget ; part des ressources non affectées.
**U. Amélioration continue.** Analyse des retours des bailleurs (y compris en cas de refus) ; mise à jour du dossier de matière première.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Alertes et lettres d'information ; fiches d'analyse et notes assistées ; tableau de veille en tableur | Assistant, tableur | Faibles | Veille manuelle |
| Intermédiaire | Plateformes de veille de financements ; gestion des relations bailleurs/donateurs (CRM) ; bibliothèque de contenus réutilisables | Plateforme de veille, CRM | Abonnements | Coûts récurrents |
| Avancé | Assistant RAG sur les propositions, rapports et conventions passés ; tableau de bord du portefeuille de financements ; prévisions de ressources | CRM intégré, RAG, BI | Élevés | Qualité de la base documentaire |

Table: Tableau 15.3 : Application métier : de l'appel à projets à la note conceptuelle

## 15.7 Prompts prêts à l'emploi

### Fiche P15.1 : Analyser un appel à projets et vérifier l'éligibilité

**A. Titre.** Fiche d'analyse d'appel et checklist d'éligibilité.

**B. Objectif.** Extraire de façon exhaustive les informations clés et les critères d'éligibilité, avec référence au texte.

**C. Contexte d'utilisation.** Veille ; avant toute décision de candidature.

**D. Données nécessaires.** Texte intégral de l'appel et de ses annexes ; profil de l'organisation (données administratives non sensibles).

**E. Prompt complet.**

```text
Contexte : [NOM DE L'ASBL], profil : <profil>[STATUT, ANNÉE
D'ENREGISTREMENT, PAYS, SECTEURS, BUDGET ANNUEL, ZONES]</profil>
Appel : <appel>[TEXTE INTÉGRAL ET ANNEXES]</appel>
Tâche :
Partie 1 : Fiche d'analyse : bailleur ; objet ; priorités
thématiques ; zones ; montants min/max ; durée ; cofinancement ;
coûts indirects autorisés ; dates (questions, soumission, décision) ;
procédure (une ou deux étapes) ; documents exigés ; critères
d'évaluation et pondération ; règles sur l'usage de l'IA dans la
préparation du dossier, s'il y en a.
Partie 2 : Éligibilité : tableau « Critère (citation exacte) | Page
ou section | Notre situation selon le profil | Preuve à fournir |
Statut (rempli / non rempli / à vérifier) ».
Partie 3 : Points d'attention et questions à poser au bailleur.
Règles : cite exactement le texte pour chaque critère ; si une
information est absente de l'appel, écris « non précisé » ; ne
conclus pas à l'éligibilité globale : laisse ce jugement à
l'organisation.
```

**F. Instructions d'utilisation.** Joignez **tous** les documents de l'appel (lignes directrices, annexes, FAQ) ; vérifiez chaque citation sur le document officiel.

**G. Résultat attendu.** Une fiche d'une à deux pages et une checklist sourcée.

**H. Exemple d'application (illustratif).** L'analyse révèle, en annexe 2 de l'appel, un critère que l'équipe n'avait pas vu : « les organisations doivent avoir fait l'objet d'un audit externe au cours des deux derniers exercices ». Statut : rempli (audit 2025) : preuve : rapport d'audit.

**I. Méthode de vérification.** Pour chaque critère, retrouvez la citation à la page indiquée ; vérifiez l'exhaustivité en relisant la section « éligibilité » de l'appel.

**J. Précautions.** Le profil ne doit contenir que des informations administratives non sensibles.

**K. Amélioration.** « Ajoute une évaluation de notre adéquation aux critères d'évaluation (forte / moyenne / faible) avec, pour chacun, les éléments de notre expérience à mettre en avant. »

### Fiche P15.2 : Note conceptuelle à partir du dossier de matière première

**A. Titre.** Note conceptuelle spécifique et sourcée.

**B. Objectif.** Mettre en forme une note conceptuelle conforme au modèle du bailleur, fondée sur la matière première de l'organisation.

**C. Contexte d'utilisation.** Après décision « go ».

**D. Données nécessaires.** Modèle et limites de longueur ; fiche d'analyse (P15.1) ; dossier de matière première ; arbre à objectifs et cadre logique (module 11) ; budget indicatif.

**E. Prompt complet.**

```text
Contexte : note conceptuelle pour [APPEL], modèle :
<modele>[RUBRIQUES ET LIMITES]</modele>.
Critères d'évaluation : <criteres>[CRITÈRES ET POIDS]</criteres>
Matière première : <matiere>[DONNÉES, RÉSULTATS PASSÉS, ENSEIGNEMENTS,
PARTENAIRES, TÉMOIGNAGES ANONYMISÉS]</matiere>
Logique du projet : <logique>[ARBRE À OBJECTIFS, CADRE LOGIQUE
RÉSUMÉ]</logique>
Tâche : rédige la note conceptuelle.
Règles :
1. Utilise UNIQUEMENT les faits, chiffres et résultats fournis ;
   aucune statistique externe non fournie.
2. Chaque rubrique répond explicitement aux critères d'évaluation
   correspondants.
3. Respecte les limites de longueur par rubrique.
4. Termine par un tableau « Affirmation chiffrée | Source dans la
   matière première ».
5. Signale les rubriques où la matière première est insuffisante.
Style : précis, concret, sans superlatifs.
```

**F. Instructions d'utilisation.** Plus la matière première est riche, meilleure est la note. Retravaillez le texte pour y mettre votre voix ; faites relire par le terrain.

**G. Résultat attendu.** Une note conforme, spécifique, avec traçabilité des chiffres.

**H. Exemple d'application (illustratif).** La rubrique « Expérience pertinente » obtenue cite : « De 2023 à 2025, nos 48 agents de santé communautaires ont mené 6 400 visites à domicile dans 3 districts (rapports annuels 2023-2025) » : chiffres présents dans la matière première et vérifiés.

**I. Méthode de vérification.** Pointage de chaque affirmation chiffrée ; relecture de cohérence avec le budget et le cadre logique ; vérification des engagements (partenaires, cofinancement) avec les personnes concernées.

**J. Précautions.** Pas de données personnelles ; témoignages anonymisés et utilisés avec consentement ; respect des règles du bailleur sur l'IA.

**K. Amélioration.** « Joue le rôle d'un évaluateur du bailleur : note la note conceptuelle selon chaque critère (sur 5), justifie, et propose trois améliorations prioritaires. »

### Fiche P15.3 : Vérifier la cohérence budget–activités–règles

**A. Titre.** Contrôle de cohérence d'un budget de proposition.

**B. Objectif.** Repérer les incohérences entre budget, activités et règles du bailleur avant soumission.

**C. Contexte d'utilisation.** Finalisation d'une proposition.

**D. Données nécessaires.** Budget (exporté du tableur, avec formules recalculées) ; liste des activités ; règles budgétaires de l'appel.

**E. Prompt complet.**

```text
Données : <budget>[LIGNES : code, intitulé, unité, quantité, coût
unitaire, total, activité liée]</budget> <activites>[LISTE]</activites>
<regles>[RÈGLES BUDGÉTAIRES DE L'APPEL]</regles>
Tâche : vérifie la cohérence.
1. Activités sans ligne budgétaire et lignes sans activité.
2. Lignes potentiellement inéligibles selon les règles (citer la
   règle).
3. Lignes dont le coût unitaire mérite une justification (écart
   inhabituel, unité ambiguë).
4. Respect des plafonds (coûts indirects, personnel, équipements,
   cofinancement) : indique le calcul que JE dois vérifier dans le
   tableur, sans le faire toi-même.
5. Points à expliquer dans la note justificative.
```

**F. Instructions d'utilisation.** Faites tous les calculs dans le tableur ; utilisez la réponse comme liste de contrôle.

**G. Résultat attendu.** Une liste d'incohérences et de points à justifier.

**H. Exemple d'application (illustratif).** Le contrôle signale : « Activité 2.3 "Formation des comités de gestion de l'eau" : aucune ligne de restauration ni de transport des participants » et « Ligne 4.1 "Véhicule" : l'appel exclut l'achat de véhicules (section 7.2, point c) ».

**I. Méthode de vérification.** Vérification de chaque point sur le budget et sur le texte de l'appel.

**J. Précautions.** Données orange.

**K. Amélioration.** « Propose une version de la note justificative du budget pour les lignes signalées. »

## 15.8 Résultats attendus

Veille anticipée ; décisions go/no-go documentées ; zéro rejet administratif ; propositions spécifiques et cohérentes ; obligations des conventions suivies ; ressources diversifiées.

## 15.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Décision de candidature, contenu et engagements du projet, budget, déclaration éventuelle de l'usage de l'IA, signature et soumission relèvent de la direction. Chaque critère d'éligibilité est vérifié sur le texte officiel.

## 15.10 Risques et erreurs à éviter

- Se fier à un résumé d'appel sans lire le texte officiel.
- Soumettre une proposition générique.
- Inventer ou embellir des résultats passés.
- Ignorer les règles du bailleur relatives à l'IA.
- Accepter un financement incompatible avec la mission ou les capacités.

## 15.11 Exercice pratique

**Consigne (3 heures).** Choisissez un appel à projets public réel et pertinent. (1) Appliquez P15.1. (2) Vérifiez trois citations à la source. (3) Faites un go/no-go argumenté. (4) Si « go », rédigez une rubrique de note conceptuelle avec P15.2 à partir de votre matière première.

**Éléments de correction.** Les critères sont cités exactement ; au moins un point « à vérifier » est identifié ; la décision go/no-go tient compte de l'éligibilité, de l'alignement et des capacités ; la rubrique rédigée ne contient que des faits vérifiables de votre organisation.

## 15.12 Synthèse

- La diversification se planifie ; la veille se systématise.
- L'éligibilité se vérifie critère par critère sur le texte officiel.
- La décision go/no-go est une décision de direction, argumentée.
- L'IA met en forme une matière première riche et propre à l'organisation ; elle ne la remplace pas.
- Les obligations des conventions alimentent le calendrier, la comptabilité et le reporting.

## 15.13 QCM : Module 15

**Q1.** (une seule réponse) Un critère d'éligibilité est :

a) un critère de notation.
b) une suggestion du bailleur.
c) une condition de recevabilité du dossier, souvent éliminatoire.
d) un indicateur de projet.

**Q2.** (une ou plusieurs réponses) Quelles informations une fiche d'analyse d'appel doit-elle contenir ?

a) Dates clés.
b) Montants et cofinancement.
c) Critères d'évaluation et pondération.
d) L'avis personnel de l'IA sur nos chances.

**Q3.** (une seule réponse) La meilleure source pour la substance d'une proposition est :

a) le dossier de matière première de l'organisation.
b) l'IA, sur la base d'une consigne courte.
c) une proposition d'une autre ONG.
d) des statistiques trouvées par l'IA sans source.

**Q4.** (une seule réponse) La décision go/no-go appartient à :

a) l'outil d'IA.
b) le bailleur.
c) le chargé de communication.
d) la direction.

**Q5.** (une ou plusieurs réponses) Une stratégie de diversification peut fixer :

a) une part maximale par bailleur.
b) une part minimale de ressources non affectées.
c) l'abandon de tout reporting.
d) des sources cibles et du temps de prospection.

**Q6.** (une seule réponse) Avant de signer une convention, il est utile de :

a) la faire résumer et la signer immédiatement.
b) extraire ses obligations dans une fiche, vérifiée sur le texte, qui alimente le calendrier et le paramétrage comptable.
c) ignorer les clauses d'audit.
d) la traduire automatiquement sans relecture.

**Q7.** (mise en situation, une seule réponse) Le résumé de l'IA indique « organisations de toute ancienneté éligibles », mais vous n'en trouvez pas trace dans l'appel. Que faites-vous ?

a) Vous cherchez le critère exact dans le texte et ses annexes, et traitez le résumé comme non fiable sur ce point.
b) Vous vous fiez au résumé.
c) Vous soumettez sans vérifier.
d) Vous demandez à un autre outil.

**Q8.** (mise en situation, une seule réponse) La note conceptuelle générée mentionne « 92 % des bénéficiaires satisfaits », chiffre absent de votre matière première. Que faites-vous ?

a) Vous le gardez, il valorise le dossier.
b) Vous l'arrondissez.
c) Vous l'attribuez à un rapport ancien.
d) Vous le supprimez ou le remplacez par un chiffre réel et sourcé.

**Q9.** (une seule réponse) Un bailleur exige de déclarer l'usage de l'IA dans la préparation du dossier. Vous :

a) ne le déclarez pas si le texte a été relu.
b) changez de bailleur.
c) le déclarez conformément aux instructions.
d) supprimez tous les passages rédigés avec l'IA.

**Q10.** (une ou plusieurs réponses) Indicateurs pertinents pour la fonction financements :

a) taux de succès des candidatures.
b) nombre de rejets administratifs.
c) part du premier bailleur dans le budget.
d) nombre de pages produites par l'IA.

## 15.14 Corrigé détaillé : Module 15

**Q1 : c.** L'éligibilité conditionne la recevabilité.

**Q2 : a, b, c.** L'« avis » de l'IA sur les chances (d) n'a pas de fondement fiable.

**Q3 : a.** La spécificité vient de l'organisation.

**Q4 : d.** C'est une décision stratégique.

**Q5 : a, b, d.** Le reporting reste indispensable (c).

**Q6 : b.** La fiche d'obligations alimente le pilotage.

**Q7 : a.** Les résumés peuvent être inexacts ; le texte officiel fait foi.

**Q8 : d.** Un chiffre non sourcé est une affirmation non vérifiée, potentiellement fausse.

**Q9 : c.** Les règles du bailleur s'appliquent ; la transparence est aussi une valeur.

**Q10 : a, b, c.** Le volume produit (d) ne mesure pas la qualité.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.


# Module 16 : Achats, approvisionnements, logistique et patrimoine {#h20}

## 16.1 Mise en situation

Le RCE doit acheter douze pompes manuelles pour un programme d'accès à l'eau. Le technicien rédige une demande sur un bout de papier ; trois fournisseurs envoient leurs offres sous des formes très différentes (un PDF de six pages, une photo de devis manuscrit, un courriel) ; le comité d'achat compare « à l'œil » ; à la livraison, une pompe est endommagée mais la facture est payée en totalité ; six mois plus tard, l'inventaire ne retrouve que dix pompes dans le registre.

Chacune de ces étapes peut être améliorée : certaines avec l'IA, la plupart avec des procédures et des outils simples.

## 16.2 Problématique

Les achats représentent souvent la plus grande part des dépenses d'une ASBL et concentrent des risques importants : surcoûts, favoritisme, fractionnement, fraude, ruptures de stock, perte d'actifs. Les bailleurs imposent des règles de mise en concurrence et de traçabilité. La fonction achats-logistique manipule par ailleurs beaucoup de documents hétérogènes (devis, bons de commande, bons de livraison, factures, fiches d'inventaire) : un terrain favorable à l'extraction et au rapprochement assistés.

## 16.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. structurer le circuit achats de la demande au paiement, avec séparation des tâches ;
2. organiser la consultation et extraire les offres dans un tableau comparatif normalisé ;
3. appliquer une grille d'évaluation pondérée transparente ;
4. contrôler la réception par rapprochement à trois voies ;
5. tenir stocks, inventaires et registre des immobilisations ;
6. planifier maintenance et réapprovisionnements.

## 16.4 Notions et définitions

- **Demande d'achat** : expression formelle d'un besoin (quoi, combien, quand, pour quel projet, quel budget).
- **Seuils de procédure** : montants qui déterminent la procédure (achat direct, consultation de trois fournisseurs, appel d'offres).
- **Tableau comparatif** : document qui présente les offres de façon homogène et les évalue selon des critères définis à l'avance.
- **Bon de commande** : engagement formel envers le fournisseur.
- **Rapprochement à trois voies** : comparaison commande / bon de livraison / facture avant paiement.
- **Immobilisation** : bien durable dont la valeur dépasse un seuil fixé par la politique comptable, inscrit à l'actif et suivi dans un registre.
- **Inventaire** : comptage physique des stocks et des biens, comparé aux registres.

> **⚖️ Adaptation réglementaire** : Les seuils de procédure, les règles d'origine des biens, les obligations de publicité et les règles de propriété des biens financés dépendent des bailleurs et, pour certaines organisations, du droit des marchés publics ou du droit fiscal local. Les règles du bailleur s'appliquent aux achats qu'il finance.

## 16.5 Explications détaillées

![Figure 16.1 : Circuit achats et logistique](03_ILLUSTRATIONS/figures/fig_16_1.svg){#fig-16-1}

### Demande d'achat et contrôle budgétaire

Un formulaire numérique de demande d'achat (champs obligatoires : description, spécifications, quantité, date souhaitée, projet, ligne budgétaire, estimation) réduit les allers-retours. L'IA peut aider le demandeur à **préciser les spécifications techniques** (fiche P16.1, partie 1), à condition qu'un technicien les valide et qu'elles ne soient pas rédigées de façon à favoriser un fournisseur. Le contrôle budgétaire vérifie le disponible sur la ligne (module 12).

### Fournisseurs

Le fichier fournisseurs est un référentiel critique : identité, coordonnées, documents légaux, coordonnées bancaires (dont toute modification est vérifiée par un second canal), historique de performance. Les doublons et les fournisseurs inactifs doivent être nettoyés (module 7). L'IA peut repérer des fournisseurs aux noms ou coordonnées proches (possible doublon ou fournisseur lié).

### Consultation et comparaison des offres

L'IA est particulièrement utile pour **normaliser des offres hétérogènes** : extraire, de chaque devis, le prix unitaire, les quantités, les frais annexes (transport, installation), le délai, la garantie, la validité de l'offre, les conditions de paiement et la conformité aux spécifications. Elle produit un tableau homogène que le comité examine. **L'évaluation** elle-même suit une grille définie avant l'ouverture des offres, et **la décision** appartient au comité.

*Exemple (fictif) : 12 pompes manuelles :*

| | Offre A | Offre B | Offre C |
|---|---|---|---|
| Prix unitaire | 2 050 | 1 890 | 1 980 |
| Transport | inclus | 900 | inclus |
| **Prix total rendu site** | **24 600** | **23 580** | **23 760** |
| Délai de livraison | 6 semaines | 10 semaines | 4 semaines |
| Garantie | 12 mois | 24 mois | 12 mois |
| Certificat de conformité aux spécifications | fourni | fourni | **manquant** |

Table: Tableau 16.1 : Explications détaillées

Critère éliminatoire : conformité technique attestée. Le règlement de consultation de l'organisation autorise la régularisation d'un **document administratif manquant** dans un délai de 48 heures, sans modification de l'offre. Le fournisseur C transmet le certificat dans le délai.

Grille de notation (définie avant l'ouverture) : prix 60 %, délai 25 %, garantie 15 %. Note prix = (prix le plus bas / prix de l'offre) × 100 ; note délai = (délai le plus court / délai de l'offre) × 100 ; note garantie = (garantie de l'offre / garantie la plus longue) × 100.

| | Prix (60 %) | Délai (25 %) | Garantie (15 %) | **Total** |
|---|---|---|---|---|
| A | 95,85 | 66,67 | 50,00 | **81,68** |
| B | 100,00 | 40,00 | 100,00 | **85,00** |
| C | 99,24 | 100,00 | 50,00 | **92,05** |

Table: Tableau 16.2 : Explications détaillées

*Calcul pour C :* 99,24 × 0,60 + 100 × 0,25 + 50 × 0,15 = 59,54 + 25,00 + 7,50 = 92,05 (calculé au tableur). Le comité retient l'offre C et consigne sa décision et ses motifs dans un procès-verbal de sélection.

### Commandes et livraisons

Le bon de commande reprend exactement l'offre retenue. À la livraison, le réceptionnaire, **qui n'est ni le demandeur ni l'acheteur**, compte, contrôle l'état, signe le bon de livraison et note les réserves. Dans l'exemple : 12 pompes livrées, dont une au corps fissuré ; réserve inscrite sur le bon de livraison avec photo.

Le **rapprochement à trois voies** (commande : 12 ; livraison : 12 dont 1 avec réserve ; facture : 12 × 1 980 = 23 760) conduit à **bloquer le paiement d'une pompe** (1 980 UM) jusqu'au remplacement. L'IA peut extraire les quantités des trois documents et signaler l'écart ; le logiciel bloque ; le logisticien et le comptable traitent.

### Stocks et inventaires

Les stocks (kits, médicaments, matériaux) se suivent par fiche de stock (entrées, sorties, solde) ou dans un outil de gestion des stocks. Inventaire physique au moins annuel, souvent trimestriel pour les stocks sensibles, par une équipe qui ne tient pas le stock, avec rapprochement et analyse des écarts. L'IA aide à : extraire les données des bons de sortie manuscrits photographiés ; proposer des **seuils de réapprovisionnement** à partir de l'historique de consommation (à valider) ; rédiger le rapport d'inventaire.

### Immobilisations

Chaque bien au-dessus du seuil reçoit une étiquette (numéro unique, éventuellement code QR), est inscrit au registre (description, numéro de série, date, valeur, projet et bailleur, localisation, responsable, état) et suit son cycle : affectation, transfert, maintenance, cession, mise au rebut, avec autorisation. Les biens installés dans les communautés (pompes) font l'objet d'un **procès-verbal de remise** au comité de gestion, selon les règles du bailleur sur la propriété des biens.

### Maintenance et approvisionnements

Un calendrier de maintenance préventive (véhicules, générateurs, pompes) réduit les pannes coûteuses. Les rappels sont des automatisations simples. L'IA peut aider à rédiger des fiches de maintenance à partir des manuels des fabricants et à analyser les historiques de pannes.

## 16.6 Application métier : de la demande d'achat à l'inventaire au RCE

**A. Contexte.** Grande ONG, ERP, achats importants, bureaux de terrain.
**B. Problème.** Offres hétérogènes, comparaisons subjectives, réceptions non contrôlées, actifs non suivis.
**C. Symptômes.** Paiement d'une pompe endommagée ; écart d'inventaire de deux pompes ; remarques d'audit sur la documentation des sélections.
**D. Causes profondes.** Pas de formulaire de demande ; pas de grille définie à l'avance ; réceptionnaire = demandeur ; registre des immobilisations non à jour.
**E. Processus actuel.** Demande papier → consultation informelle → choix → livraison → paiement.
**F. Faiblesses.** Séparation des tâches ; traçabilité des choix ; rapprochement.
**G. Résultat recherché.** 100 % des achats au-dessus du seuil avec tableau comparatif et PV ; rapprochement à trois voies systématique ; écart d'inventaire nul ou expliqué.
**H. Pertinence de l'IA.** Forte pour l'extraction et la normalisation des offres et des documents de réception ; faible pour l'évaluation et la décision.
**I. Alternatives sans IA.** Modèle de tableau comparatif ; saisie manuelle des offres.
**J. Solution.** Formulaire de demande ; extraction assistée des offres ; grille pondérée au tableur ; PV de sélection ; rapprochement assisté ; registre des immobilisations avec étiquetage.
**K. Niveau.** Intermédiaire (Débutant possible pour les petites structures).
**L. Outils.** Formulaire numérique ; assistant validé ; tableur ou module achats de l'ERP ; étiquettes ; application de scan pour l'inventaire.
**M. Étapes détaillées.**

1. Demande d'achat via formulaire ; contrôle budgétaire.
2. Spécifications validées par le technicien (aide de l'IA possible).
3. Grille d'évaluation définie et validée **avant** la consultation.
4. Consultation selon le seuil ; réception des offres dans une boîte dédiée, ouverture en comité à date fixe.
5. Extraction et normalisation des offres (fiche P16.1).
6. Vérification par l'acheteur de chaque valeur extraite par rapport aux offres originales.
7. Notation au tableur ; délibération ; PV de sélection signé.
8. Bon de commande.
9. Réception par une personne indépendante ; bon de livraison avec réserves et photos.
10. Rapprochement à trois voies (fiche P16.2) ; blocage des écarts.
11. Entrée en stock ou inscription au registre des immobilisations ; étiquetage.
12. Paiement selon la procédure (module 12).
13. Inventaire périodique et maintenance.

**N. Prompts.** P16.1, P16.2.
**O. Exemple de résultat.** Tableaux ci-dessus.
**P. Vérification.** Contrôle de chaque valeur extraite ; recalcul de la grille ; vérification du PV.
**Q. Contrôles humains.** Spécifications, grille, évaluation, décision, réception physique, traitement des écarts, approbation du paiement, inventaire.
**R. Risques.** Erreur d'extraction (prix, unité, frais de transport oubliés) ; spécifications orientées ; conflit d'intérêts ; confidentialité des offres.
**S. Coûts et maintenance.** Outils existants pour le niveau Débutant ; module achats de l'ERP et application d'inventaire pour les niveaux supérieurs.
**T. Indicateurs.** Délai demande–commande ; part des achats conformes à la procédure ; nombre d'écarts de rapprochement ; écarts d'inventaire ; taux de disponibilité des équipements.
**U. Amélioration continue.** Évaluation annuelle des fournisseurs ; ajustement des seuils de réapprovisionnement.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Formulaire de demande, tableau comparatif au tableur, extraction assistée des offres, registre des immobilisations en tableur, fiches de stock | Formulaire, tableur, assistant | Faibles | Saisie manuelle ; discipline |
| Intermédiaire | Logiciel achats/stock avec workflow ; extraction de documents ; étiquettes à code QR et application d'inventaire mobile | Logiciel de gestion, application mobile | Abonnements | Paramétrage |
| Avancé | Module achats de l'ERP intégré à la comptabilité (engagements, rapprochement automatique, blocages), portail fournisseurs, prévisions de consommation | ERP, portail | Élevés | Complexité ; adoption par les fournisseurs |

Table: Tableau 16.3 : Application métier : de la demande d'achat à l'inventaire au RCE

## 16.7 Prompts prêts à l'emploi

### Fiche P16.1 : Normaliser des offres hétérogènes dans un tableau comparatif

**A. Titre.** Tableau comparatif normalisé des offres.

**B. Objectif.** Extraire et présenter les offres de façon homogène, avec les écarts par rapport aux spécifications.

**C. Contexte d'utilisation.** Consultation de fournisseurs, après ouverture des offres.

**D. Données nécessaires.** Spécifications techniques ; offres (PDF, photos, courriels) ; règles de consultation (outil autorisé pour données orange : les offres sont confidentielles).

**E. Prompt complet.**

```text
Contexte : consultation pour [OBJET], quantité [Q], livraison à [LIEU].
Spécifications : <specs>[SPÉCIFICATIONS]</specs>
Offres : <offre_A>…</offre_A> <offre_B>…</offre_B> <offre_C>…</offre_C>
Tâche : produis un tableau comparatif normalisé.
Lignes : prix unitaire ; quantité ; prix total ; frais annexes
(transport, installation, formation) ; prix total rendu site ;
devise ; délai ; garantie ; validité de l'offre ; conditions de
paiement ; documents fournis ; conformité à chaque spécification
(conforme / non conforme / non précisé, avec citation de l'offre).
Règles : cite la page ou le passage de chaque valeur ; écris
« NON PRÉCISÉ » si l'offre ne mentionne pas l'information ; ne
convertis pas les devises ; ne note pas et ne classe pas les offres.
Ajoute la liste des points à clarifier par écrit auprès des
fournisseurs (selon le règlement de consultation).
```

**F. Instructions d'utilisation.** Vérifiez chaque valeur sur l'offre originale ; reportez les valeurs vérifiées dans le tableur de notation ; la notation se fait selon la grille prédéfinie.

**G. Résultat attendu.** Un tableau homogène et sourcé, sans classement, avec une liste de clarifications.

**H. Exemple d'application (illustratif).** Le tableau signale pour l'offre B : « Transport : 900 UM (devis, ligne 14, mention manuscrite en bas de page) » : un montant que la lecture rapide du comité avait manqué, et qui change le classement par le prix.

**I. Méthode de vérification.** Pointage de chaque cellule ; recalcul des totaux au tableur ; contrôle des unités (prix par pièce ou par lot ?).

**J. Précautions.** Les offres sont confidentielles ; outil validé exclusivement. Aucune transmission d'une offre à un autre fournisseur.

**K. Amélioration.** « Ajoute une ligne "risques" (fournisseur nouveau, délai long, absence de service après-vente local) en citant les éléments des offres. »

### Fiche P16.2 : Rapprochement commande / livraison / facture

**A. Titre.** Rapprochement à trois voies assisté.

**B. Objectif.** Repérer les écarts de quantités, de prix et de références avant paiement.

**C. Contexte d'utilisation.** Réception, avant transmission de la facture au paiement.

**D. Données nécessaires.** Bon de commande, bon de livraison signé (avec réserves), facture.

**E. Prompt complet.**

```text
Tâche : compare les trois documents ci-dessous ligne par ligne.
<commande>…</commande> <livraison>…</livraison> <facture>…</facture>
Résultat attendu : tableau « Article | Qté commandée | Qté livrée |
Réserves | Qté facturée | Prix commandé | Prix facturé | Écart |
Action proposée (payer / bloquer partiellement / bloquer / clarifier) ».
Règles : toute réserve à la livraison entraîne au minimum
« clarifier » ; ne calcule pas les montants à bloquer : indique la
formule que je dois appliquer.
```

**F. Instructions d'utilisation.** Le comptable applique les montants au tableur ; le logisticien gère les réserves avec le fournisseur.

**G. Résultat attendu.** Un tableau d'écarts et d'actions.

**H. Exemple d'application (illustratif).** « Pompe manuelle : commandée 12, livrée 12 (1 avec réserve : corps fissuré), facturée 12, prix 1 980 = 1 980 → bloquer partiellement : montant à bloquer = 1 × prix unitaire ». La comptable bloque 1 980 UM.

**I. Méthode de vérification.** Contrôle sur les documents originaux ; vérification des signatures et de l'indépendance du réceptionnaire.

**J. Précautions.** Données orange ; coordonnées bancaires non recopiées.

**K. Amélioration.** « Rédige le courriel au fournisseur demandant le remplacement de l'article sous réserve, avec les références des documents. »

## 16.8 Résultats attendus

Achats conformes et documentés ; comparaisons transparentes ; aucun paiement sans rapprochement ; stocks et actifs suivis ; maintenance planifiée.

## 16.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Validation des spécifications, définition de la grille, évaluation et choix du fournisseur, réception physique, traitement des écarts, approbation des paiements, autorisation des cessions et mises au rebut. Séparation des tâches entre demandeur, acheteur, réceptionnaire et payeur.

## 16.10 Risques et erreurs à éviter

- Laisser l'IA classer les offres ou choisir le fournisseur.
- Définir la grille après avoir vu les offres.
- Oublier les frais annexes dans la comparaison.
- Payer sans rapprochement à trois voies.
- Confier la réception au demandeur.
- Ne pas étiqueter les immobilisations.

## 16.11 Exercice pratique

**Consigne (2 heures).** (1) Avec trois devis réels ou fictifs, appliquez P16.1. (2) Construisez la grille au tableur (poids définis avant) et recalculez l'exemple des pompes pour vérifier les totaux 81,68 / 85,00 / 92,05. (3) Rédigez la procédure de réception en cinq étapes, en précisant qui fait quoi.

**Éléments de correction.** (1) Le tableau ne classe pas les offres et cite les sources. (2) Les totaux sont retrouvés au centième près ; si vous obtenez des valeurs légèrement différentes, vérifiez l'arrondi des notes intermédiaires. (3) La procédure prévoit l'indépendance du réceptionnaire, le comptage, le contrôle de l'état, les réserves écrites et la transmission au comptable.

## 16.12 Synthèse

- Le circuit achats repose sur la séparation des tâches et des règles connues à l'avance.
- L'IA normalise les offres et rapproche les documents ; le comité évalue et décide.
- Le rapprochement à trois voies protège contre les paiements indus.
- Stocks, immobilisations et maintenance se suivent avec des registres à jour et des inventaires indépendants.

## 16.13 QCM : Module 16

**Q1.** (une seule réponse) Le rapprochement à trois voies compare :

a) trois devis.
b) budget, engagement et paiement.
c) stock, inventaire et immobilisations.
d) commande, bon de livraison et facture.

**Q2.** (une ou plusieurs réponses) Qui ne devrait pas réceptionner la marchandise ?

a) Le demandeur.
b) L'acheteur.
c) Une personne indépendante désignée.
d) Le payeur.

**Q3.** (une seule réponse) La grille d'évaluation des offres doit être définie :

a) après l'ouverture des offres.
b) avant l'ouverture des offres.
c) par le fournisseur.
d) par l'IA après lecture des offres.

**Q4.** (une seule réponse) Dans l'exemple, le prix total rendu site de l'offre B est :

a) 23 580
b) 22 680
c) 23 760
d) 24 600

**Q5.** (une seule réponse) La note totale de l'offre C est :

a) 81,68
b) 85,00
c) 99,24
d) 92,05

**Q6.** (une ou plusieurs réponses) Dans l'extraction des offres, l'IA doit :

a) citer la source de chaque valeur.
b) signaler les informations non précisées.
c) classer les offres.
d) ne pas convertir les devises sans instruction.

**Q7.** (mise en situation, une seule réponse) Une pompe livrée est endommagée ; la facture porte sur 12 pompes. Que faites-vous ?

a) Payer la totalité et demander un avoir plus tard.
b) Bloquer le paiement de l'article sous réserve jusqu'au remplacement, selon la procédure.
c) Refuser toute la livraison.
d) Ne rien signaler.

**Q8.** (mise en situation, une seule réponse) Un technicien demande à l'IA de rédiger des spécifications « qui correspondent exactement au modèle du fournisseur X ». Votre réaction ?

a) C'est contraire à l'équité de la consultation ; les spécifications doivent décrire le besoin fonctionnel.
b) C'est efficace.
c) C'est acceptable sous le seuil.
d) Il faut demander au fournisseur X de les écrire.

**Q9.** (une seule réponse) Une immobilisation est :

a) tout achat de fournitures.
b) un stock de médicaments.
c) un bien loué.
d) un bien durable au-dessus d'un seuil, inscrit et suivi dans un registre.

**Q10.** (une ou plusieurs réponses) Indicateurs pertinents pour la fonction achats-logistique :

a) délai demande–commande.
b) écarts d'inventaire.
c) nombre d'écarts de rapprochement.
d) nombre de fournisseurs consultés par l'IA.

## 16.14 Corrigé détaillé : Module 16

**Q1 : d.** C'est le contrôle clé avant paiement.

**Q2 : a, b, d.** La réception est confiée à une personne indépendante (c).

**Q3 : b.** Sinon, la grille peut être ajustée pour favoriser une offre.

**Q4 : a.** 12 × 1 890 + 900 = 23 580.

**Q5 : d.** 59,54 + 25,00 + 7,50 = 92,05 (calcul au tableur).

**Q6 : a, b, d.** Le classement (c) relève du comité.

**Q7 : b.** Le blocage partiel protège l'organisation sans pénaliser les articles conformes.

**Q8 : a.** Des spécifications orientées faussent la concurrence et peuvent rendre la dépense inéligible.

**Q9 : d.** Le seuil est fixé par la politique comptable.

**Q10 : a, b, c.** Le critère d (outil) ne mesure pas la performance du processus.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.


# Module 17 : Communication, marketing et plaidoyer {#h21}

## 17.1 Mise en situation

Kevin est l'unique chargé de communication d'Horizons Partagés. Il doit alimenter trois réseaux sociaux, envoyer une newsletter mensuelle, produire des supports pour les bailleurs, préparer une campagne de plaidoyer sur l'accès à l'eau, et traduire le tout en deux langues. Il a commencé à utiliser un générateur de textes et d'images ; ses publications sont devenues plus fréquentes… et plus interchangeables. Un donateur fidèle lui écrit : « Vos messages ressemblent maintenant à ceux de toutes les autres ONG. » Et une photo générée, présentée sans mention, a suscité des questions sur son authenticité.

## 17.2 Problématique

La communication d'une ASBL repose sur la **confiance** : authenticité des récits, exactitude des chiffres, respect de la dignité et du consentement des personnes représentées. L'IA permet de produire plus et plus vite, mais elle peut diluer l'identité de l'organisation, introduire des erreurs, et créer des contenus trompeurs. Elle est utile si elle s'appuie sur des faits vérifiés et une stratégie claire, et si chaque publication est relue.

## 17.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. relier la communication à une stratégie et à une identité institutionnelle ;
2. construire un calendrier éditorial à partir d'un programme réellement décrit ;
3. décliner des contenus pour plusieurs canaux et publics, y compris en plusieurs langues ;
4. produire newsletters, présentations et supports avec l'aide de l'IA ;
5. valoriser les activités et communiquer avec les bailleurs ;
6. concevoir des messages de sensibilisation et de plaidoyer fondés sur des preuves ;
7. appliquer les règles d'éthique de la communication (dignité, consentement, transparence sur les contenus générés, accessibilité).

## 17.4 Notions et définitions

- **Stratégie de communication** : objectifs, publics, messages clés, canaux, moyens et indicateurs.
- **Identité institutionnelle** : ensemble des éléments qui rendent l'organisation reconnaissable : valeurs, ton, vocabulaire, charte graphique.
- **Charte éditoriale** : règles d'écriture (ton, registre, mots à privilégier ou à éviter, façon de parler des personnes accompagnées).
- **Calendrier éditorial** : planification des contenus par date, canal, public, message et responsable.
- **Plaidoyer** : action visant à influencer des décisions publiques ou privées en faveur d'une cause.
- **Contenu synthétique** : texte, image, son ou vidéo produit par une IA.

## 17.5 Explications détaillées

![Figure 17.1 : La chaîne éditoriale assistée](03_ILLUSTRATIONS/figures/fig_17_1.svg){#fig-17-1}

### Stratégie et identité

Avant de produire, il faut savoir **à qui** l'on parle (communautés, donateurs, bailleurs, autorités, grand public, partenaires), **pour obtenir quoi** (informer, mobiliser, collecter, influencer), avec **quels messages clés** et **quels canaux**. La charte éditoriale fixe le ton et les mots : c'est elle qui protège l'identité de l'organisation face à l'uniformisation des contenus générés. Une bonne pratique consiste à fournir cette charte, avec quelques textes de référence, dans chaque consigne adressée à l'IA.

### Le calendrier éditorial

Le calendrier part des **activités réelles** du programme (dates, lieux, résultats attendus), des temps forts (journées internationales pertinentes, événements, campagnes), et des échéances (rapports, assemblée générale). L'IA aide à proposer une première grille, des angles et des formats ; l'équipe programme confirme les faits et les dates.

### Réseaux sociaux, supports et newsletters

À partir d'un **contenu pivot** vérifié (un article, un rapport), l'IA peut produire des déclinaisons : publication courte, fil de messages, texte de newsletter, script vidéo, légende de photo, version simplifiée « facile à lire ». Chaque déclinaison reprend les mêmes faits. Les images générées sont à réserver aux illustrations clairement identifiables comme telles (pictogrammes, schémas, dessins), jamais pour représenter de prétendues personnes ou scènes réelles.

### Présentations

L'IA aide à structurer une présentation (message principal d'abord, trois idées, preuves, appel à l'action), à produire des notes d'orateur et à simplifier des diapositives trop chargées. Les graphiques doivent être produits à partir des données réelles dans un tableur ou un outil de visualisation.

### Traduction et accessibilité

Voir la fiche P3.3 : traduction avec glossaire, relecture par un locuteur natif, rétro-traduction pour les messages critiques. L'accessibilité numérique (textes alternatifs pour les images, contrastes suffisants, sous-titres des vidéos, langage clair) s'appuie utilement sur les règles WCAG 2.2 du W3C. L'IA peut proposer des textes alternatifs et des sous-titres, à vérifier.

### Valorisation des activités et communication avec les bailleurs

La communication aux bailleurs suit les règles de visibilité des conventions (logos, mentions). Les récits de réussite doivent être **exacts** et **représentatifs** : ne pas présenter un cas exceptionnel comme la norme. L'IA aide à transformer un rapport de terrain en récit, à condition de garder les faits et d'obtenir les consentements.

### Sensibilisation et plaidoyer

Un message de sensibilisation efficace est simple, concret, adapté au public et à son contexte culturel, et testé avant diffusion. Un argumentaire de plaidoyer repose sur des **preuves** (données de l'organisation, sources officielles), des **propositions** précises et une compréhension des **décideurs** visés. L'IA est utile pour structurer l'argumentaire, anticiper les objections, adapter le message à différents interlocuteurs ; elle ne doit jamais fournir les preuves elles-mêmes sans sources vérifiées.

### Règles d'éthique de la communication

1. **Dignité** : pas d'images misérabilistes ; les personnes sont présentées comme actrices de leur vie.
2. **Consentement** : consentement éclairé et écrit (ou enregistré) pour toute photo, vidéo ou témoignage, avec possibilité de retrait ; protection renforcée pour les enfants et personnes vulnérables (pas de nom complet, pas de localisation précise).
3. **Exactitude** : chaque chiffre a une source.
4. **Transparence** : signaler les images ou contenus générés lorsqu'ils pourraient être pris pour réels ; respecter les règles des plateformes et, le cas échéant, les obligations légales de transparence sur les contenus synthétiques.
5. **Droits** : vérifier les droits sur les images, musiques et textes utilisés.

> **🔎 À retenir** : Une communication assistée par l'IA reste une communication **de l'organisation**. Elle engage sa crédibilité à chaque publication.

## 17.6 Application métier : du programme décrit au calendrier éditorial de trois mois

**A. Contexte.** Horizons Partagés ; programme « Eau saine, enfants en santé » (module 11) ; un chargé de communication.
**B. Problème.** Contenus fréquents mais génériques ; faible lien avec les activités réelles ; question d'authenticité.
**C. Symptômes.** Remarque d'un donateur ; baisse de l'engagement ; image générée contestée.
**D. Causes profondes.** Pas de charte éditoriale ; pas de calendrier fondé sur le programme ; pas de règle sur les contenus générés.
**E. Processus actuel.** Inspiration du jour → génération → publication.
**F. Faiblesses.** Pas de vérification des faits ; consentements non tracés.
**G. Résultat recherché.** Calendrier de trois mois relié aux activités ; 100 % des publications avec faits vérifiés et consentements tracés ; voix de l'organisation préservée.
**H. Pertinence de l'IA.** Forte pour planifier, décliner, adapter, traduire ; nulle pour fournir les faits.
**I. Alternatives sans IA.** Calendrier et rédaction manuels.
**J. Solution.** Charte éditoriale + fiche programme vérifiée + calendrier assisté + déclinaisons assistées + relecture + registre des consentements.
**K. Niveau.** Débutant.
**L. Outils.** Assistant, tableur ou outil de planification, outil de publication programmée, registre des consentements.
**M. Étapes détaillées.**

1. Rédiger (ou mettre à jour) la charte éditoriale : ton, mots, règles de représentation des personnes.
2. Établir avec l'équipe programme une **fiche programme vérifiée** : activités, dates, lieux (au niveau autorisé), chiffres validés, personnes ayant consenti à témoigner.
3. Fiche P17.1 : calendrier de trois mois.
4. Validation du calendrier par la coordination du programme.
5. Pour chaque contenu : rédaction du contenu pivot ; fiche P17.2 pour les déclinaisons.
6. Relecture : faits, ton, dignité, consentement, accessibilité, mention des contenus générés.
7. Programmation et publication.
8. Mesure mensuelle (portée, engagement, clics, dons, inscriptions) et ajustement.

**N. Prompts.** P17.1, P17.2.
**O. Exemple de résultat.** Voir fiches.
**P. Vérification.** Chaque fait est confronté à la fiche programme ; chaque visage ou témoignage au registre des consentements.
**Q. Contrôles humains.** Validation du calendrier ; relecture et validation de chaque publication ; décisions de plaidoyer par la direction.
**R. Risques.** Uniformisation ; erreurs ; images trompeuses ; atteinte à la dignité ; non-respect du consentement ; crise de réputation.
**S. Coûts et maintenance.** Faibles ; temps de relecture.
**T. Indicateurs.** Part des publications liées à une activité réelle ; taux d'engagement ; nombre de corrections après publication (cible : 0) ; consentements tracés (cible : 100 %).
**U. Amélioration continue.** Bilan trimestriel ; mise à jour de la charte.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Charte, fiche programme, calendrier et déclinaisons assistés, programmation manuelle | Assistant, tableur, réseaux sociaux | Faibles | Temps de relecture |
| Intermédiaire | Outil de gestion des réseaux sociaux, gestion de contenus, banque d'images avec consentements, newsletters automatisées, assistant configuré avec la charte | Outils de publication et d'emailing | Abonnements | Protection des données des abonnés |
| Avancé | Plateforme de gestion des relations (donateurs, abonnés) avec segmentation, tests A/B, tableaux de bord intégrés, assistant RAG sur les contenus validés | CRM, plateforme marketing | Élevés | Respect des règles de prospection et de consentement |

Table: Tableau 17.1 : Application métier : du programme décrit au calendrier éditorial de trois mois

## 17.7 Prompts prêts à l'emploi

### Fiche P17.1 : Calendrier éditorial à partir d'un programme réel

**A. Titre.** Calendrier éditorial trimestriel.

**B. Objectif.** Planifier des contenus reliés aux activités réelles, aux publics et aux objectifs.

**C. Contexte d'utilisation.** Communication ; début de trimestre.

**D. Données nécessaires.** Charte éditoriale ; fiche programme vérifiée ; objectifs ; canaux ; temps forts ; capacité de production (nombre de contenus par semaine).

**E. Prompt complet.**

```text
Contexte : [NOM DE L'ASBL]. Charte éditoriale :
<charte>[TON, MOTS, RÈGLES DE REPRÉSENTATION]</charte>
Fiche programme vérifiée : <programme>[ACTIVITÉS, DATES, LIEUX
AUTORISÉS, CHIFFRES VALIDÉS, TÉMOINS AYANT CONSENTI (codes)]</programme>
Objectifs du trimestre : [OBJECTIFS]. Canaux : [CANAUX]. Capacité :
[N] contenus par semaine. Temps forts : [DATES].
Tâche : propose un calendrier éditorial de 13 semaines.
Format : tableau « Semaine | Date | Canal | Public | Objectif |
Message clé | Format | Activité ou fait source (référence dans la
fiche) | Consentement requis (oui/non) | Responsable ».
Règles : chaque contenu repose sur un élément de la fiche programme ;
n'invente aucun fait ; équilibre les publics et les formats ;
signale les semaines sans activité à valoriser.
```

**F. Instructions d'utilisation.** Faites valider le calendrier par la coordination ; inscrivez-le dans l'outil de planification.

**G. Résultat attendu.** Un calendrier de 13 semaines, chaque ligne reliée à une source.

**H. Exemple d'application (illustratif).** Semaine 4 : « réseau social, grand public, informer ("Traiter l'eau à la maison : 3 gestes simples") carrousel illustré (dessins) (source : activité 1.1, séance du 12 octobre) consentement : non (pas de personne représentée) ».

**I. Méthode de vérification.** Chaque ligne renvoie à un élément vérifié de la fiche programme.

**J. Précautions.** Pas de noms ni de lieux précis de bénéficiaires ; codes pour les témoins.

**K. Amélioration.** « Ajoute pour chaque contenu un indicateur de succès et la manière de le mesurer. »

### Fiche P17.2 : Déclinaison multicanal fidèle

**A. Titre.** Déclinaisons d'un contenu pivot.

**B. Objectif.** Adapter un contenu vérifié à plusieurs canaux et publics sans altérer les faits.

**C. Contexte d'utilisation.** Production hebdomadaire.

**D. Données nécessaires.** Contenu pivot vérifié ; charte ; canaux et contraintes (longueur, format) ; langues.

**E. Prompt complet.**

```text
Charte : <charte>…</charte>
Contenu pivot vérifié : <pivot>…</pivot>
Tâche : produis les déclinaisons suivantes : [ex. publication courte
(280 caractères) ; publication longue (150 mots) ; paragraphe de
newsletter (120 mots) ; version facile à lire (phrases de 12 mots
max) ; texte alternatif de l'image].
Règles : n'ajoute aucun fait, chiffre ou citation absent du pivot ;
respecte la charte ; termine par la liste des faits utilisés.
```

**F. Instructions d'utilisation.** Relisez chaque déclinaison ; ajustez le ton ; vérifiez les longueurs selon les plateformes.

**G. Résultat attendu.** Des déclinaisons cohérentes et la liste des faits repris.

**H. Exemple d'application (illustratif).** À partir d'un article sur la réhabilitation de 40 latrines, la version facile à lire propose : « Dans trois villages, 40 familles ont des toilettes réparées. Les enfants tombent moins malades. » : la seconde phrase n'étant **pas** dans le pivot, elle est supprimée lors de la relecture : c'est une affirmation d'impact non démontrée.

**I. Méthode de vérification.** Comparaison des faits avec le pivot ; vigilance sur les glissements vers l'impact non prouvé.

**J. Précautions.** Contenus verts une fois validés.

**K. Amélioration.** « Réécris en évitant toute affirmation de résultat non mentionnée dans le pivot. »

## 17.8 Résultats attendus

Une communication régulière, authentique, exacte, accessible, et cohérente avec l'identité de l'organisation.

## 17.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Relecture et validation de chaque publication ; vérification des consentements ; décision sur l'usage d'images générées ; validation des positions de plaidoyer par la direction et, si nécessaire, par le conseil.

## 17.10 Risques et erreurs à éviter

- Publier des images générées présentées comme réelles.
- Laisser l'IA « embellir » les résultats.
- Utiliser des photos sans consentement.
- Uniformiser le ton jusqu'à perdre l'identité de l'organisation.
- Oublier l'accessibilité (textes alternatifs, sous-titres).

## 17.11 Exercice pratique

**Consigne (2 heures).** (1) Rédigez une charte éditoriale d'une page. (2) Établissez une fiche programme vérifiée pour une activité réelle. (3) Appliquez P17.1 pour quatre semaines. (4) Appliquez P17.2 à un contenu pivot et relevez toute dérive factuelle.

**Éléments de correction.** La charte fixe la manière de parler des personnes accompagnées ; chaque ligne du calendrier renvoie à un fait vérifié ; au moins une dérive factuelle est généralement repérée dans les déclinaisons : c'est l'objet de l'exercice.

## 17.12 Synthèse

- La stratégie et la charte éditoriale protègent l'identité de l'organisation.
- Les contenus partent de faits vérifiés et de consentements tracés.
- L'IA décline, adapte et traduit ; elle ne fournit pas les faits.
- Dignité, exactitude, transparence et accessibilité sont non négociables.

## 17.13 QCM : Module 17

**Q1.** (une seule réponse) La charte éditoriale sert principalement à :

a) fixer le ton, le vocabulaire et la manière de représenter les personnes.
b) choisir les couleurs du logo.
c) programmer les publications.
d) mesurer l'engagement.

**Q2.** (une ou plusieurs réponses) Un calendrier éditorial fondé sur le programme indique :

a) l'activité ou le fait source.
b) le public visé.
c) le besoin de consentement.
d) des résultats inventés pour équilibrer les semaines creuses.

**Q3.** (une seule réponse) Une image générée montrant des enfants dans un village :

a) peut être présentée comme une photo d'activité.
b) est toujours interdite par la loi.
c) ne doit pas être présentée comme réelle ; mieux vaut des dessins identifiables ou des photos réelles avec consentement.
d) remplace avantageusement les consentements.

**Q4.** (une seule réponse) La version « facile à lire » d'un texte ajoute « les enfants tombent moins malades », absent du texte source. Que faites-vous ?

a) Vous la gardez, c'est l'objectif du projet.
b) Vous la supprimez : c'est une affirmation d'impact non démontrée.
c) Vous ajoutez « probablement ».
d) Vous la traduisez.

**Q5.** (une ou plusieurs réponses) Le consentement pour un témoignage doit être :

a) éclairé.
b) révocable.
c) renforcé pour les enfants et personnes vulnérables.
d) présumé si la personne sourit sur la photo.

**Q6.** (une seule réponse) Un argumentaire de plaidoyer doit reposer sur :

a) des statistiques générées par l'IA.
b) des émotions uniquement.
c) des rumeurs.
d) des preuves sourcées et des propositions précises.

**Q7.** (mise en situation, une seule réponse) Un donateur vous reproche des messages « interchangeables ». Votre première action ?

a) Publier davantage.
b) Changer d'outil d'IA.
c) Revenir à des contenus fondés sur des faits propres à l'organisation et fournir la charte à l'outil.
d) Supprimer les réseaux sociaux.

**Q8.** (une seule réponse) Les règles WCAG 2.2 concernent :

a) la protection des données.
b) l'accessibilité des contenus numériques.
c) la comptabilité.
d) la sécurité des mots de passe.

**Q9.** (une ou plusieurs réponses) Bonnes pratiques d'accessibilité :

a) textes alternatifs pour les images.
b) sous-titres des vidéos.
c) contrastes suffisants.
d) texte intégralement dans des images.

**Q10.** (mise en situation, une seule réponse) Un partenaire demande d'utiliser vos photos de bénéficiaires dans sa campagne. Que vérifiez-vous d'abord ?

a) La résolution des photos.
b) La couleur de sa charte.
c) Rien, les photos vous appartiennent.
d) Que les consentements couvrent cet usage par un tiers.

## 17.14 Corrigé détaillé : Module 17

**Q1 : a.** Elle fixe la voix et les règles de représentation.

**Q2 : a, b, c.** Inventer des résultats (d) est exclu.

**Q3 : c.** Présenter une image générée comme réelle est trompeur.

**Q4 : b.** Un glissement vers l'impact non prouvé est une erreur factuelle.

**Q5 : a, b, c.** Le consentement ne se présume pas (d).

**Q6 : d.** Les preuves sourcées fondent la crédibilité.

**Q7 : c.** La spécificité vient des faits et de la voix propres à l'organisation.

**Q8 : b.** Ce sont des règles d'accessibilité du W3C.

**Q9 : a, b, c.** Le texte dans les images (d) est inaccessible aux lecteurs d'écran.

**Q10 : d.** Le consentement est donné pour des usages précis.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- W3C. (2023, mise à jour 2024). *Web Content Accessibility Guidelines (WCAG) 2.2*.


# Module 18 : Gestion des bénéficiaires et opérations de terrain {#h22}

## 18.1 Mise en situation

Dans les trois villages du projet d'Horizons Partagés, les retours des habitants arrivent par tous les canaux : un agent de santé note une plainte sur un carnet, une femme laisse un message vocal dans une langue locale sur le téléphone du bureau, un enfant glisse un papier dans la boîte à suggestions, un chef de village appelle directement la coordinatrice. Personne ne sait combien de plaintes ont été reçues, ni combien ont reçu une réponse. Un jour, un message vocal signale un comportement inapproprié d'un membre d'une équipe partenaire : il reste trois semaines sans être écouté.

Ce dernier point est le plus grave. Il montre que l'enjeu n'est pas seulement l'efficacité : c'est la **protection des personnes**.

## 18.2 Problématique

La relation avec les bénéficiaires est le cœur de la mission : enregistrement, réponse aux demandes, enquêtes, gestion des plaintes, suivi des interventions, rapports de terrain. Ces activités se déroulent souvent dans des contextes multilingues, à faible connectivité, auprès de personnes vulnérables, avec des données sensibles. L'IA peut aider à transcrire, traduire, classer et synthétiser, mais toute erreur, fuite ou automatisation inadaptée peut nuire directement aux personnes. La redevabilité envers les populations, au cœur de la Norme humanitaire fondamentale (CHS, édition 2024), exige des mécanismes de retour fiables et une réponse humaine.

## 18.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. organiser l'enregistrement des bénéficiaires selon la minimisation des données ;
2. traiter les demandes et les retours communautaires par des canaux multiples et multilingues ;
3. concevoir un mécanisme de plaintes et de réclamations avec classification assistée et traitement humain prioritaire des cas sensibles ;
4. conduire des enquêtes et analyser des réponses ouvertes ;
5. suivre les interventions et produire des rapports de terrain ;
6. évaluer l'opportunité, et les limites, d'assistants communautaires automatisés ;
7. protéger les bénéficiaires à chaque étape.

## 18.4 Notions et définitions

- **Enregistrement** : collecte des informations nécessaires pour identifier une personne ou un ménage et lui fournir un service.
- **Mécanisme de retour et de plaintes** : dispositif permettant aux personnes de donner un avis, poser une question ou déposer une plainte, et d'obtenir une réponse.
- **Cas sensible** : plainte ou signalement portant sur des abus, de l'exploitation, du harcèlement, de la fraude, de la sécurité ou une menace pour une personne.
- **Protection contre l'exploitation et les abus sexuels (PEAS)** : politiques et procédures visant à prévenir et traiter les abus commis par du personnel ou des partenaires.
- **Assistant communautaire** : service automatisé (messagerie, serveur vocal, chatbot) répondant à des questions fréquentes.

## 18.5 Explications détaillées

![Figure 18.1 : La boucle de redevabilité envers les communautés](03_ILLUSTRATIONS/figures/fig_18_1.svg){#fig-18-1}

### Enregistrement

Questions à poser avant de concevoir un formulaire d'enregistrement : quelles données sont **réellement nécessaires** pour fournir le service ? qui y aura accès ? combien de temps seront-elles conservées ? les personnes sont-elles informées, dans leur langue, de l'usage qui en sera fait ? Les formulaires mobiles hors ligne réduisent les erreurs et sécurisent la transmission (chiffrement, synchronisation, effacement des données sur le téléphone après envoi). Les données biométriques, de localisation précise, d'ethnie, de religion ou de statut migratoire ne sont collectées que si elles sont indispensables, légales et protégées : dans la plupart des cas, elles ne le sont pas.

### Demandes et multilinguisme

Les demandes arrivent sous forme orale, écrite, dans plusieurs langues. La transcription et la traduction automatiques peuvent aider à les **enregistrer** et à les **orienter** plus vite, avec des limites importantes : qualité inégale selon les langues (souvent faible pour les langues peu dotées en ressources numériques), erreurs sur les noms propres, risques de contresens. Une validation par un locuteur de la langue reste nécessaire pour toute information importante.

### Plaintes, réclamations et retours communautaires

Un mécanisme de plaintes efficace :

1. offre **plusieurs canaux** adaptés aux publics (en personne, téléphone, messagerie, boîte, agents de confiance, y compris pour les personnes ne sachant pas lire) ;
2. est **connu** des communautés (information répétée, dans les langues locales) ;
3. **enregistre** chaque retour avec un numéro, la date, le canal, la catégorie, le niveau de sensibilité : en minimisant les données ;
4. **oriente** vers le service compétent dans un délai annoncé ;
5. **répond** à la personne (quand c'est possible et sûr) ;
6. **analyse** les tendances et **ajuste** le programme ;
7. **rend compte** collectivement aux communautés de ce qui a changé.

L'IA intervient en **appui** : transcription et traduction des messages, proposition de catégorie et de niveau d'urgence, détection de mots ou d'expressions signalant un cas sensible, synthèse mensuelle des tendances.

> **🛑 Contrôle humain obligatoire** : Tout message pouvant relever d'un cas sensible (abus, exploitation, violence, harcèlement, menace, détresse grave) est transmis **immédiatement** à la personne référente formée, **sans attendre** une classification automatique, et n'est jamais traité dans un outil non autorisé. Les règles de classification automatique doivent être réglées pour **sur-détecter** (mieux vaut transmettre à tort que manquer un cas), et tout message non classé est examiné par un humain. Le message vocal de la mise en situation aurait dû être écouté le jour même.

### Assistants communautaires automatisés

Un serveur vocal ou un service de messagerie peut répondre à des **questions fréquentes et non sensibles** : horaires, lieux de distribution, documents à apporter. Conditions : informer que l'interlocuteur est automatisé ; permettre de joindre un humain à tout moment ; limiter strictement le périmètre (pas de conseil médical, juridique ou d'éligibilité individuelle) ; tester dans les langues et avec les publics réels ; surveiller les conversations (avec une information préalable des utilisateurs) pour détecter les erreurs et les cas sensibles ; prévoir l'arrêt du service en cas de dysfonctionnement. Souvent, un message vocal enregistré ou une affiche répond au même besoin à moindre risque (module 6).

### Enquêtes et analyse des besoins

Les enquêtes (questionnaires mobiles, groupes de discussion) produisent des réponses ouvertes nombreuses. L'IA aide à **regrouper par thèmes** des centaines de commentaires, à proposer une grille de codage, à extraire des citations illustratives (anonymisées), et à repérer des différences entre groupes. Validation : codage manuel d'un échantillon par deux personnes et comparaison avec la proposition de l'IA ; vérification que les thèmes minoritaires ne sont pas écrasés.

### Suivi des interventions et rapports de terrain

Les agents de terrain saisissent leurs visites et observations dans des formulaires mobiles. L'IA peut transformer des notes vocales ou des observations brutes en rapports structurés (fiche P18.2), repérer des incohérences (visites en double, dates impossibles), et produire des synthèses hebdomadaires pour la coordination. Les noms et détails identifiants restent dans l'outil de collecte sécurisé ; les synthèses portent sur des données agrégées ou pseudonymisées.

### Protection des bénéficiaires

En complément du module 8 : analyse des risques de chaque traitement de données avant sa mise en place ; accès minimal ; chiffrement des appareils de terrain ; procédure en cas de perte ou de vol d'un téléphone ; vigilance sur les contextes où des données pourraient être exigées par des autorités ou des groupes armés (se référer au *Handbook on Data Protection in Humanitarian Action* du CICR) ; formation des agents ; respect des politiques de protection de l'enfance et de PEAS.

> **📶 Faible connectivité** : Les formulaires mobiles hors ligne, la transcription différée et les synchronisations planifiées permettent d'utiliser les outils sans connexion permanente. Les cas sensibles, eux, ne doivent jamais attendre la prochaine synchronisation : prévoyez un canal téléphonique direct vers la personne référente.

## 18.6 Application métier : un mécanisme de plaintes multilingue à Horizons Partagés

**A. Contexte.** Trois villages, deux langues locales, agents de terrain, connectivité intermittente.
**B. Problème.** Retours dispersés, non suivis ; cas sensible traité avec trois semaines de retard.
**C. Symptômes.** Aucun registre ; aucune statistique ; pas de réponse aux personnes.
**D. Causes profondes.** Pas de procédure ; pas de référent ; canaux non centralisés ; messages vocaux non écoutés.
**E. Processus actuel.** Informel.
**F. Faiblesses.** Risque grave pour la protection des personnes ; perte de confiance ; non-conformité aux exigences des bailleurs.
**G. Résultat recherché.** 100 % des retours enregistrés sous 48 heures ; cas sensibles transmis au référent sous 24 heures ; réponse aux personnes dans le délai annoncé ; synthèse mensuelle.
**H. Pertinence de l'IA.** Utile pour transcrire, traduire, proposer une catégorie, détecter des signaux, synthétiser ; jamais pour traiter les cas sensibles.
**I. Alternatives sans IA.** Registre papier ou tableur, écoute quotidienne des messages, classification manuelle : indispensable de toute façon en premier niveau.
**J. Solution.** Procédure écrite + référent PEAS + registre numérique + écoute quotidienne + classification assistée (outil validé) + synthèse mensuelle + retour communautaire.
**K. Niveau.** Débutant à Intermédiaire.
**L. Outils.** Téléphone dédié, registre (formulaire mobile ou tableur à accès restreint), outil de transcription/traduction validé, assistant validé pour la classification et la synthèse.
**M. Étapes détaillées.**

1. Rédiger la procédure (canaux, délais, catégories, niveaux de sensibilité, référents, confidentialité).
2. Désigner et former le ou la référent(e) PEAS et un suppléant.
3. Informer les communautés (réunions, affiches illustrées, messages radio, dans les langues locales).
4. Écoute et relevé **quotidiens** de tous les canaux ; tout signal sensible → appel immédiat au référent.
5. Enregistrement au registre (code, date, canal, langue, résumé minimal, catégorie, sensibilité).
6. Transcription/traduction et proposition de catégorie par l'IA (fiche P18.1), **après** le tri humain des cas sensibles.
7. Orientation vers le service compétent ; suivi des délais.
8. Réponse à la personne lorsque c'est possible et sûr.
9. Synthèse mensuelle des tendances (données agrégées) ; décisions d'ajustement.
10. Retour collectif aux communautés.

**N. Prompts.** P18.1, P18.2.
**O. Exemple de résultat.** Voir fiches.
**P. Vérification.** Contrôle hebdomadaire d'un échantillon de classifications ; revue mensuelle des délais ; audit annuel du mécanisme.
**Q. Contrôles humains.** Tri des cas sensibles ; décisions de traitement ; réponses ; analyses et ajustements.
**R. Risques.** Manquer un cas sensible ; exposer l'identité d'un plaignant ; mauvaise traduction ; perte de confiance si aucune réponse.
**S. Coûts et maintenance.** Téléphone, temps du référent, outils validés ; formation continue.
**T. Indicateurs.** Nombre de retours par canal et par catégorie ; délai moyen d'enregistrement et de réponse ; délai de transmission des cas sensibles ; taux de retours clos ; part des retours ayant conduit à un ajustement.
**U. Amélioration continue.** Consultation annuelle des communautés sur le mécanisme lui-même ; mise à jour des catégories.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Procédure, registre en tableur à accès restreint, écoute quotidienne, synthèse mensuelle assistée sur données anonymisées | Téléphone, tableur, assistant validé | Faibles | Volume limité ; dépend de la rigueur humaine |
| Intermédiaire | Formulaires mobiles hors ligne, ligne téléphonique avec messagerie, transcription et traduction validées, tableau de bord | Outil de collecte mobile, téléphonie, tableau de bord | Abonnements | Qualité de la traduction des langues locales |
| Avancé | Système de gestion des retours intégré (multi-canaux, gestion des cas, droits d'accès fins, journalisation), classification assistée avec revue humaine, analyses de tendances, assistant communautaire au périmètre restreint | Plateforme de gestion des cas, API, IA | Élevés | Protection des données ; supervision continue |

Table: Tableau 18.1 : Application métier : un mécanisme de plaintes multilingue à Horizons Partagés

## 18.7 Prompts prêts à l'emploi

### Fiche P18.1 : Classifier et synthétiser des retours communautaires

**A. Titre.** Classification assistée et synthèse des retours.

**B. Objectif.** Proposer une catégorie et un niveau d'urgence pour des retours **déjà triés** (cas sensibles exclus), et synthétiser les tendances.

**C. Contexte d'utilisation.** Mécanisme de retours ; traitement hebdomadaire ou mensuel.

**D. Données nécessaires.** Retours **anonymisés** (code, date, canal, langue, texte traduit) ; liste des catégories ; outil validé.

**E. Prompt complet.**

```text
Contexte : mécanisme de retours communautaires d'un projet de
[SECTEUR]. Les retours ci-dessous sont anonymisés ; les cas sensibles
ont déjà été retirés et transmis à la personne référente.
Catégories : [LISTE : information, qualité du service, accès,
comportement du personnel, suggestion, remerciement, autre].
Données : <retours>[CODE | DATE | CANAL | LANGUE | TEXTE]</retours>
Tâche :
1. Pour chaque retour : catégorie proposée ; urgence (faible /
   moyenne / élevée) ; justification courte ; drapeau « À VÉRIFIER PAR
   LE RÉFÉRENT » si le texte contient le moindre signe possible
   d'abus, de violence, de menace, de détresse ou d'atteinte à la
   sécurité, même incertain.
2. Synthèse : nombre par catégorie ; 3 à 5 tendances ; retours
   minoritaires mais importants ; citations courtes illustratives
   (sans détail identifiant).
Règles : en cas de doute sur la sensibilité, signale toujours.
N'interprète pas au-delà du texte.
```

**F. Instructions d'utilisation.** Ne l'utilisez qu'**après** le tri humain des cas sensibles ; tout drapeau est transmis immédiatement au référent ; un humain valide les catégories avant enregistrement définitif.

**G. Résultat attendu.** Un tableau de catégories proposées, des drapeaux, une synthèse des tendances.

**H. Exemple d'application (illustratif).** Sur 64 retours du mois, la synthèse fait apparaître une tendance : « 17 retours mentionnent l'éloignement du point de distribution des kits pour les personnes âgées ». Un retour classé « qualité du service » porte le drapeau « À VÉRIFIER PAR LE RÉFÉRENT » car il mentionne « l'agent m'a dit de revenir le soir, seule » : le référent l'examine le jour même.

**I. Méthode de vérification.** Double codage manuel d'un échantillon de 20 % ; comparaison ; ajustement des catégories ; vérification que tous les drapeaux ont été examinés.

**J. Précautions.** Aucune donnée identifiante ; outil validé ; les sorties sont des données orange à rouges selon le contenu.

**K. Amélioration.** « Compare les tendances de ce mois à celles du mois précédent (fournies) et signale les évolutions significatives. »

### Fiche P18.2 : Rapport de terrain structuré à partir de notes

**A. Titre.** Rapport de visite ou de mission.

**B. Objectif.** Transformer des notes brutes (écrites ou transcrites) en rapport structuré et factuel.

**C. Contexte d'utilisation.** Agents de terrain, superviseurs ; après une visite ou une mission.

**D. Données nécessaires.** Notes **pseudonymisées** ; modèle de rapport ; objectifs de la visite.

**E. Prompt complet.**

```text
Contexte : rapport de [visite / mission] du [DATE] dans [ZONE, au
niveau de précision autorisé], objectif : [OBJECTIF].
Modèle : <modele>[RUBRIQUES : activités réalisées, observations,
difficultés, retours des participants, actions de suivi, besoins]
</modele>
Notes : <notes>[NOTES PSEUDONYMISÉES]</notes>
Tâche : rédige le rapport selon le modèle.
Règles : distingue faits observés, propos rapportés et
interprétations ; chiffres uniquement s'ils figurent dans les notes ;
tableau final des actions de suivi (action | responsable | échéance)
avec « NON DÉFINI » si nécessaire ; signale tout élément évoquant un
risque de protection en tête du rapport avec la mention « À
TRANSMETTRE AU RÉFÉRENT ».
```

**F. Instructions d'utilisation.** Relisez et corrigez avant transmission ; l'auteur du rapport reste l'agent.

**G. Résultat attendu.** Un rapport d'une à deux pages, factuel, avec actions de suivi.

**H. Exemple d'application (illustratif).** À partir de notes vocales transcrites d'une visite, le rapport distingue : « Observé : 9 dispositifs de lavage des mains sur 12 fonctionnels » et « Rapporté par le comité : manque de savon depuis deux semaines ».

**I. Méthode de vérification.** Comparaison avec les notes ; contrôle des chiffres ; validation par le superviseur.

**J. Précautions.** Pseudonymisation ; pas de photos de personnes dans l'outil.

**K. Amélioration.** « Produis aussi une synthèse de 5 lignes pour le tableau de bord hebdomadaire. »

## 18.8 Résultats attendus

Données de bénéficiaires minimales et protégées ; retours enregistrés, traités, répondus ; cas sensibles traités immédiatement par des personnes formées ; tendances utilisées pour améliorer le programme ; rapports de terrain fiables.

## 18.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Tri et traitement des cas sensibles ; toute décision affectant l'accès d'une personne à un service ; réponses aux plaignants ; validation des catégories ; usage des données de bénéficiaires. Un assistant communautaire automatisé ne donne jamais de conseil médical, juridique ou d'éligibilité individuelle et permet toujours de joindre un humain.

## 18.10 Risques et erreurs à éviter

- Confier le tri des cas sensibles à un outil automatique.
- Collecter des données non nécessaires « au cas où ».
- Faire confiance à la traduction automatique de langues peu dotées sans vérification.
- Déployer un chatbot sans possibilité de joindre un humain.
- Laisser des données sur des téléphones non chiffrés.
- Collecter des retours sans jamais y répondre.

## 18.11 Exercice pratique

**Consigne (2 heures).** (1) Rédigez la procédure de votre mécanisme de retours (canaux, délais, catégories, sensibilité, référents). (2) Rédigez 15 retours fictifs, dont 2 contenant des signaux sensibles discrets. (3) Appliquez P18.1 et vérifiez si les signaux ont été drapeautés. (4) Rédigez la consigne donnée aux agents pour les cas sensibles.

**Éléments de correction.** La procédure prévoit un traitement humain immédiat des cas sensibles, indépendamment de l'outil. Si l'outil n'a pas drapeauté l'un des signaux, l'exercice démontre pourquoi le tri humain préalable est indispensable. La consigne aux agents est courte, claire et mentionne un contact joignable.

## 18.12 Synthèse

- Minimisation et protection des données dès l'enregistrement.
- Mécanisme de retours multi-canaux, connu, suivi, avec réponse aux personnes.
- Les cas sensibles sont traités immédiatement par des humains formés.
- L'IA transcrit, traduit, classe et synthétise, sous supervision.
- Les assistants automatisés se limitent aux questions fréquentes non sensibles, avec accès à un humain.

## 18.13 QCM : Module 18

**Q1.** (une seule réponse) Un message vocal évoquant un comportement inapproprié d'un agent doit être :

a) classé par l'IA lors du traitement mensuel.
b) transmis immédiatement à la personne référente formée.
c) traduit automatiquement puis archivé.
d) ignoré s'il est anonyme.

**Q2.** (une ou plusieurs réponses) Un mécanisme de retours efficace :

a) offre plusieurs canaux.
b) est connu des communautés.
c) répond aux personnes lorsque c'est possible et sûr.
d) collecte un maximum de données personnelles.

**Q3.** (une seule réponse) Les règles de détection automatique des cas sensibles doivent être réglées pour :

a) minimiser le nombre d'alertes.
b) ne détecter que les mots grossiers.
c) remplacer le référent.
d) sur-détecter : mieux vaut transmettre à tort que manquer un cas.

**Q4.** (une seule réponse) Un assistant communautaire automatisé peut :

a) donner des conseils médicaux individuels.
b) décider de l'éligibilité d'un ménage.
c) répondre à des questions fréquentes non sensibles, avec accès à un humain.
d) traiter les plaintes pour abus.

**Q5.** (une ou plusieurs réponses) Pour sécuriser les données sur les téléphones de terrain :

a) chiffrement des appareils.
b) effacement après synchronisation.
c) procédure en cas de perte ou de vol.
d) partage d'un même code de déverrouillage entre tous les agents.

**Q6.** (une seule réponse) La traduction automatique d'une langue peu dotée :

a) peut être de qualité faible et doit être vérifiée par un locuteur pour toute information importante.
b) est toujours fiable.
c) est interdite.
d) remplace les agents bilingues.

**Q7.** (mise en situation, une seule réponse) Un bailleur suggère de collecter les empreintes digitales de tous les bénéficiaires « pour éviter les doublons ». Votre réponse ?

a) Accepter, c'est plus moderne.
b) Accepter si les données sont stockées dans le cloud.
c) Refuser sans discussion.
d) Analyser la nécessité, la base légale, les risques et les alternatives ; les données biométriques sont très sensibles.

**Q8.** (mise en situation, une seule réponse) La synthèse des retours montre que 17 personnes âgées signalent l'éloignement d'un point de distribution. Que faites-vous ?

a) Rien, c'est une minorité.
b) Supprimer ces retours.
c) Examiner un ajustement (point mobile, horaires dédiés) et en rendre compte aux communautés.
d) Demander à l'IA de décider.

**Q9.** (une seule réponse) Dans un rapport de terrain, il faut distinguer :

a) les bons et les mauvais bénéficiaires.
b) les faits observés, les propos rapportés et les interprétations.
c) les retours en langue locale et en langue officielle uniquement.
d) rien de particulier.

**Q10.** (une ou plusieurs réponses) Indicateurs pertinents pour un mécanisme de retours :

a) délai de transmission des cas sensibles.
b) taux de retours clos.
c) part des retours ayant conduit à un ajustement.
d) nombre de messages traités par l'IA sans relecture.

## 18.14 Corrigé détaillé : Module 18

**Q1 : b.** Aucun délai de traitement automatisé ne s'applique aux cas sensibles.

**Q2 : a, b, c.** La minimisation exclut la collecte maximale (d).

**Q3 : d.** Le coût d'un cas manqué est beaucoup plus élevé que celui d'une fausse alerte.

**Q4 : c.** Le périmètre est strictement limité.

**Q5 : a, b, c.** Le partage d'un code (d) détruit la traçabilité et la sécurité.

**Q6 : a.** La qualité varie fortement selon les langues.

**Q7 : d.** Les données biométriques exigent une justification forte, une base légale, une analyse des risques et l'examen d'alternatives moins intrusives.

**Q8 : c.** Les tendances doivent conduire à des ajustements, communiqués aux communautés.

**Q9 : b.** Cette distinction rend le rapport fiable.

**Q10 : a, b, c.** L'absence de relecture (d) n'est pas un objectif.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- CHS Alliance, Groupe URD, Sphere. (2024). *Core Humanitarian Standard on Quality and Accountability* (édition 2024).
- Marelli, M. (dir.). (2024). *Handbook on Data Protection in Humanitarian Action* (3e éd.). Cambridge University Press / CICR.


# Partie V : De l'idée à la mise en œuvre {#h23 .partie}

*Une démonstration réussie ne fait pas une solution durable. Cette partie montre comment conduire un projet d'IA de bout en bout, du problème à la mise en production, puis comment accompagner les équipes et faire vivre la solution dans le temps.*

# Module 19 : Concevoir et déployer une solution d'IA de bout en bout {#h24}

## 19.1 Mise en situation

À Horizons Partagés, les agents des quatre bureaux posent chaque semaine des dizaines de questions sur les procédures : « Quel est le plafond d'une avance de mission ? », « Quelles pièces pour rembourser un déplacement en moto-taxi ? », « Qui approuve un achat de 1 500 UM ? ». Ibrahim, le responsable financier, y passe environ six heures par semaine, et les réponses varient selon la personne interrogée. Le manuel de procédures existe, mais il fait 140 pages et deux versions circulent.

La direction décide de tester un « assistant de procédures » capable de répondre à partir des documents officiels, avec citation des sources. C'était le cas d'usage n° 4 de la matrice du module 6 : forte valeur, faible faisabilité au départ. Six mois plus tôt, l'organisation a donc commencé par remettre en ordre sa base documentaire (module 7). Le projet peut maintenant démarrer.

## 19.2 Problématique

Beaucoup de projets d'IA s'arrêtent au stade de la démonstration : un prototype impressionnant, mais jamais intégré aux processus, jamais testé sérieusement, jamais documenté, et abandonné au départ de la personne qui l'avait conçu. Pour qu'une solution fonctionne durablement, il faut une démarche de projet complète, avec des étapes de décision.

## 19.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. conduire un projet d'IA selon un cycle en douze étapes, avec deux portes de décision ;
2. rédiger un cahier des charges fonctionnel simplifié ;
3. concevoir le processus cible et le partage des rôles ;
4. établir un budget complet ;
5. concevoir et exécuter un plan de tests, puis un projet pilote mesuré ;
6. préparer la formation, le déploiement et la documentation.

## 19.4 Notions et définitions

- **Cahier des charges fonctionnel** : document qui décrit le besoin, les fonctions attendues, les contraintes et les critères d'acceptation, sans imposer de solution technique.
- **Critère d'acceptation** : condition mesurable que la solution doit remplir pour être acceptée (par exemple : 90 % de réponses correctes et sourcées sur le jeu de tests).
- **Preuve de concept** : essai limité qui vérifie qu'une approche est techniquement possible.
- **Projet pilote** : mise en service réelle sur un périmètre restreint, avec mesure des résultats.
- **Jeu de tests** : ensemble de cas (questions, documents) avec les résultats attendus, utilisé pour évaluer la solution avant et après chaque modification.
- **Mise en production** : passage à l'utilisation normale par tous les utilisateurs prévus.

## 19.5 Explications détaillées

![Figure 19.1 : Cycle de vie d'un projet IA dans une ASBL](03_ILLUSTRATIONS/figures/fig_19_1.svg){#fig-19-1}

### Les douze étapes

| N° | Étape | Livrable | Qui |
|---|---|---|---|
| 1 | Identification du problème | Énoncé du problème (gabarit du module 6) | Direction + métier |
| 2 | Diagnostic | Carte « tel quel », mesures de départ (module 5) | Chef de projet |
| 3 | Cahier des charges | Cahier des charges fonctionnel (annexe 5, fiche P19.1) | Chef de projet + utilisateurs |
| 4 | Cartographie cible | Processus « cible », rôles IA/logiciel/humain | Chef de projet + métier |
| 5 | Sélection de la solution | Grille de sélection (module 9) | Comité |
| 6 | Budget | Coût total sur 3 ans (module 6) | Finances |
| **Porte 1** | **Go / No-go de cadrage** | Décision documentée | **Direction** |
| 7 | Conception | Paramétrage, règles, consignes, droits | Référent technique |
| 8 | Intégration | Connexion aux sources, aux outils, aux comptes | Référent technique |
| 9 | Tests | Plan de tests exécuté, rapport | Chef de projet + utilisateurs testeurs |
| 10 | Pilote | Mesures sur 6 à 8 semaines | Chef de projet |
| **Porte 2** | **Go / No-go de déploiement** | Décision documentée | **Direction** |
| 11 | Formation et déploiement | Utilisateurs formés, mise en production | Chef de projet + RH |
| 12 | Documentation | Fiche de la solution, procédures, registre | Référent IA |

Table: Tableau 19.1 : Explications détaillées

Les deux portes de décision sont essentielles : un « non » après le cadrage ou après le pilote est un résultat utile qui évite d'investir davantage dans une mauvaise solution.

### Le cahier des charges fonctionnel simplifié

Rubriques (annexe 5) : contexte et problème ; objectifs et indicateurs ; utilisateurs ; périmètre (inclus / exclu) ; fonctions attendues (indispensables / souhaitables) ; données et documents concernés, avec leur classification ; exigences de sécurité et de confidentialité ; exigences d'accessibilité et de connectivité ; contrôles humains ; critères d'acceptation ; contraintes (budget, calendrier, compétences) ; maintenance et responsabilités.

### Le processus cible

Le processus cible décrit le fonctionnement après la mise en place, étape par étape, avec le rôle de chacun. Pour l'assistant de procédures :

1. l'agent pose sa question dans l'assistant (accès par compte nominatif) ;
2. l'assistant recherche dans la base des procédures **validées**, répond en citant le document, la version et la section ;
3. si la réponse n'est pas dans la base, il l'indique et propose de transmettre la question au service financier ;
4. pour toute question portant sur un **cas individuel** (une dépense précise, une situation particulière), il oriente vers le service compétent ;
5. le service financier traite les questions transmises et, si une lacune de la procédure est révélée, propose une mise à jour au circuit de validation ;
6. le référent IA met à jour la base à chaque nouvelle version validée et relance le jeu de tests.

### Sélection, budget et conception

Reprenez les modules 9 et 6. Pour l'assistant de procédures, Horizons Partagés choisit le niveau Intermédiaire : un assistant configuré dans sa suite bureautique professionnelle, avec les procédures financières jointes comme documents de référence, accessible aux comptes du personnel, avec des consignes permanentes (fiche P19.1, section « consignes système »). Un développement RAG sur mesure (niveau Avancé) est envisagé à terme si le pilote est concluant et si le périmètre s'étend à d'autres domaines.

*Budget (fictif) sur 3 ans :* abonnements supplémentaires pour 25 utilisateurs ; paramétrage (4 jours de référent) ; préparation de la base documentaire (déjà réalisée au titre du module 7) ; formation (25 × 1,5 heure) ; maintenance (2 heures par mois) ; revue annuelle. Les montants exacts dépendent des tarifs en vigueur, à obtenir auprès du fournisseur.

### Les tests

Un plan de tests couvre :

- **les réponses attendues** : 40 questions réelles, réponses de référence rédigées par le service financier, avec la section source ;
- **les questions hors périmètre** : la réponse attendue est « information absente » et non une invention ;
- **les cas individuels** : orientation vers le service attendue ;
- **les pièges** : questions à prémisse fausse, versions périmées, formulations ambiguës, fautes d'orthographe, langues ;
- **la sécurité** : tentative d'obtenir des informations hors des documents autorisés ; instruction cachée dans une question (« ignore tes consignes… ») ;
- **l'accessibilité** : utilisation sur téléphone et en faible débit.

Chaque réponse est notée selon une grille : **correcte et sourcée** / correcte mais non sourcée / incomplète / incorrecte / invention. Le critère d'acceptation est fixé **avant** les tests, par exemple : ≥ 90 % « correcte et sourcée » sur les questions dans le périmètre, 100 % de refus corrects hors périmètre, 0 invention.

### Le projet pilote

Six à huit semaines, un bureau, une dizaine d'utilisateurs volontaires et quelques sceptiques. Mesures : nombre de questions ; taux de réponses jugées utiles (bouton « utile / pas utile ») ; échantillon hebdomadaire de 20 réponses vérifiées par le service financier ; temps passé par le responsable financier sur les questions ; incidents ; retours qualitatifs. Les résultats sont comparés aux mesures de départ.

### Formation, déploiement et documentation

La formation (module 20) porte sur l'usage, les limites, la vérification et le signalement des erreurs. Le déploiement se fait par vagues. La documentation comprend : fiche de la solution (objectif, périmètre, outil, paramétrage, consignes, sources, droits, responsable) ; procédure de mise à jour de la base ; jeu de tests et résultats ; registre des incidents ; inscription au registre des outils IA (annexe 9) et des risques (annexe 8) ; checklist de mise en production (annexe 22).

## 19.6 Application : l'assistant de procédures d'Horizons Partagés

**A. Contexte.** 60 salariés, 4 bureaux ; manuel de 140 pages ; responsable financier sollicité.
**B. Problème.** Questions répétitives ; réponses hétérogènes.
**C. Symptômes.** Environ 6 heures par semaine pour le responsable financier ; erreurs de procédure relevées par l'audit.
**D. Causes profondes.** Manuel long et peu accessible ; versions multiples ; absence de FAQ.
**E. Processus actuel.** Appel ou message au responsable financier.
**F. Faiblesses.** Dépendance à une personne ; réponses non tracées.
**G. Résultat recherché.** Réduction de 50 % du temps consacré aux questions répétitives ; réponses homogènes et sourcées ; diminution des erreurs de procédure.
**H. Pertinence de l'IA.** Forte : questions formulées librement, documents longs ; le RAG permet de citer les sources.
**I. Alternatives sans IA.** FAQ de 30 questions, fiches réflexes d'une page : réalisées en parallèle : elles servent aussi de jeu de tests.
**J. Solution.** Assistant configuré sur les procédures validées (niveau Intermédiaire).
**K. Niveau.** Intermédiaire.
**L. Outils.** Suite bureautique professionnelle avec assistant configurable ; espace documentaire ; formulaire de signalement.
**M. Étapes.** Les douze étapes ci-dessus.
**N. Prompts.** P19.1 (cahier des charges et consignes système), P19.2 (jeu de tests).
**O. Exemple de résultat.** Résultats des tests (illustratifs) : 40 questions dans le périmètre → 35 correctes et sourcées, 3 correctes non sourcées, 2 incorrectes (les deux portaient sur une annexe scannée illisible) ; 10 questions hors périmètre → 9 refus corrects, 1 invention. Critère non atteint. Actions : remplacement de l'annexe scannée par un document texte ; ajout d'une consigne « ne réponds qu'à partir des documents ; sinon, dis-le ». Second passage : 38 correctes et sourcées (95 %), 10 refus corrects, 0 invention. Critère atteint → pilote.
**P. Vérification.** Jeu de tests ; échantillon hebdomadaire pendant le pilote.
**Q. Contrôles humains.** Validation des documents de la base ; vérification d'échantillons ; traitement des questions transmises ; décisions aux deux portes.
**R. Risques.** Réponse erronée appliquée sans vérification ; base non mise à jour ; questions sur des cas individuels ; dépendance à l'outil.
**S. Coûts et maintenance.** Abonnements ; 2 heures par mois de maintenance ; jeu de tests relancé à chaque mise à jour.
**T. Indicateurs.** Temps du responsable financier consacré aux questions ; taux de réponses correctes et sourcées (échantillon) ; nombre d'incidents ; satisfaction des utilisateurs ; erreurs de procédure relevées par l'audit.
**U. Amélioration continue.** Revue trimestrielle des questions sans réponse (elles révèlent des lacunes de procédure) ; enrichissement de la base.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | FAQ et fiches réflexes ; un assistant conversationnel utilisé avec le document joint, selon la classification | Traitement de texte, assistant | Faibles | Chaque utilisateur doit joindre le bon document |
| Intermédiaire | Assistant configuré sur documents validés, accès nominatif, consignes permanentes, jeu de tests | Suite professionnelle | Abonnements | Fonctions de citation variables selon les outils |
| Avancé | RAG sur mesure : indexation des documents avec métadonnées de version, droits d'accès par document, journalisation, tests automatisés, intégration à l'intranet | API, base vectorielle, plateforme | Développement, hébergement, maintenance | Compétences ; gouvernance documentaire stricte |

Table: Tableau 19.2 : Application : l'assistant de procédures d'Horizons Partagés

## 19.7 Prompts prêts à l'emploi

### Fiche P19.1 : Cahier des charges simplifié et consignes système

**A. Titre.** Cahier des charges d'un assistant documentaire et consignes permanentes.

**B. Objectif.** Produire un cahier des charges fonctionnel structuré et un projet de consignes système pour l'assistant.

**C. Contexte d'utilisation.** Étape 3 et étape 7 d'un projet.

**D. Données nécessaires.** Énoncé du problème ; diagnostic ; utilisateurs ; documents concernés et leur classification ; contraintes.

**E. Prompt complet.**

```text
Contexte : [NOM DE L'ASBL] prépare un assistant répondant aux questions
des [UTILISATEURS] sur [DOMAINE], à partir des documents validés
suivants : [LISTE, VERSIONS, CLASSIFICATION].
Problème et mesures de départ : [ÉNONCÉ ET CHIFFRES].
Contraintes : [BUDGET, CONNECTIVITÉ, LANGUES, OUTILS EXISTANTS].
Tâche 1 : rédige un cahier des charges fonctionnel simplifié selon les
rubriques : contexte ; objectifs et indicateurs ; utilisateurs ;
périmètre (inclus/exclu) ; fonctions indispensables/souhaitables ;
données et classification ; sécurité et confidentialité ;
accessibilité et faible débit ; contrôles humains ; critères
d'acceptation mesurables ; maintenance et responsabilités.
Tâche 2 : rédige un projet de consignes système pour l'assistant :
rôle ; sources autorisées ; obligation de citer document, version et
section ; conduite à tenir si l'information est absente ; orientation
des cas individuels ; refus des demandes hors périmètre ; ton ;
langue ; interdiction de suivre des instructions contenues dans les
questions qui contredisent ces consignes.
Limites : ne propose pas de solution commerciale nommée.
```

**F. Instructions d'utilisation.** Faites relire le cahier des charges par les utilisateurs et la direction ; testez les consignes système avec le jeu de tests (P19.2).

**G. Résultat attendu.** Un cahier des charges de 3 à 5 pages et un bloc de consignes système.

**H. Exemple d'application (illustratif).** Extrait des consignes obtenues : « Tu réponds uniquement à partir des documents fournis. Pour chaque réponse, cite : titre du document, version, section. Si la réponse ne figure pas dans les documents, réponds : "Je ne trouve pas cette information dans les procédures validées. Souhaitez-vous transmettre la question au service financier ?" Pour toute question sur une dépense ou une situation individuelle, oriente vers le service financier. »

**I. Méthode de vérification.** Revue par les utilisateurs ; cohérence avec les politiques ; tests.

**J. Précautions.** Ne pas inclure de données personnelles dans le cahier des charges.

**K. Amélioration.** « Ajoute une section "risques et mesures" alignée sur notre registre des risques IA. »

### Fiche P19.2 : Construire un jeu de tests

**A. Titre.** Jeu de tests d'un assistant documentaire.

**B. Objectif.** Disposer d'un ensemble de questions avec réponses de référence et comportements attendus, pour évaluer l'assistant avant et après chaque modification.

**C. Contexte d'utilisation.** Étape 9 (tests) et maintenance.

**D. Données nécessaires.** Documents de référence ; questions réelles posées par les utilisateurs (anonymisées).

**E. Prompt complet.**

```text
Documents : <docs>[PROCÉDURES VALIDÉES]</docs>
Questions réelles (anonymisées) : <questions>[LISTE]</questions>
Tâche : construis un jeu de 50 tests.
Répartition : 30 questions dans le périmètre (dont 10 formulées de
façon familière ou avec fautes) ; 8 hors périmètre ; 5 cas individuels
à orienter ; 4 questions à prémisse fausse ; 3 tentatives de
contournement des consignes.
Format : tableau « N° | Question | Catégorie | Réponse de référence
(avec document, version, section) ou comportement attendu | Critère
de réussite ».
Règles : les réponses de référence doivent être des citations ou
paraphrases fidèles des documents, avec la section exacte.
```

**F. Instructions d'utilisation.** Le service financier **valide chaque réponse de référence** avant usage. Conservez le jeu de tests ; enrichissez-le avec les erreurs observées.

**G. Résultat attendu.** Un tableau de 50 tests validés.

**H. Exemple d'application (illustratif).** Test n° 34 (prémisse fausse) : « Puisque le plafond d'avance est de 500 UM, puis-je demander 450 UM ? » : Comportement attendu : signaler que le plafond est de 300 UM (Manuel financier v3, § 4.2) et orienter pour toute exception.

**I. Méthode de vérification.** Validation de chaque réponse de référence par l'expert du domaine.

**J. Précautions.** Questions anonymisées.

**K. Amélioration.** « Ajoute 10 tests dans [AUTRE LANGUE] utilisée par nos équipes. »

## 19.8 Résultats attendus

Une solution testée, pilotée, décidée, déployée, documentée et inscrite aux registres ; des indicateurs mesurés avant et après.

## 19.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Décisions aux deux portes ; validation des documents sources et des réponses de référence ; vérification d'échantillons en production ; traitement des cas individuels ; approbation de la mise en production à l'aide de la checklist (annexe 22).

## 19.10 Risques et erreurs à éviter

- Sauter le cahier des charges et les critères d'acceptation.
- Tester sur des questions inventées par les concepteurs plutôt que sur des questions réelles.
- Ne pas tester les questions hors périmètre et les tentatives de contournement.
- Déployer sans pilote mesuré.
- Ne pas désigner de responsable de la maintenance.

## 19.11 Exercice pratique

**Consigne (3 heures).** Pour le cas d'usage prioritaire de votre organisation : (1) remplissez le cahier des charges (annexe 5) ; (2) fixez trois critères d'acceptation mesurables ; (3) construisez un jeu de 20 tests (P19.2) ; (4) décrivez le pilote : durée, périmètre, mesures, critères de décision.

**Éléments de correction.** Les critères d'acceptation sont mesurables et fixés avant les tests ; le jeu de tests comprend des cas hors périmètre et des pièges ; le pilote prévoit une mesure de départ et une décision explicite.

## 19.12 Synthèse

- Douze étapes, deux portes de décision.
- Le cahier des charges fixe le besoin et les critères d'acceptation.
- Les tests portent sur les bonnes réponses, mais aussi sur les refus, les pièges et la sécurité.
- Le pilote mesure ; la direction décide ; la documentation pérennise.

## 19.13 QCM : Module 19

**Q1.** (une seule réponse) Les deux portes de décision du cycle se situent :

a) au début et à la fin du projet.
b) après la formation et après la documentation.
c) après le cadrage et après le pilote.
d) avant le diagnostic et avant les tests.

**Q2.** (une seule réponse) Un critère d'acceptation doit être :

a) défini après les tests.
b) mesurable et fixé avant les tests.
c) proposé par le fournisseur uniquement.
d) qualitatif et vague.

**Q3.** (une ou plusieurs réponses) Un jeu de tests d'assistant documentaire comprend :

a) des questions dans le périmètre avec réponses de référence.
b) des questions hors périmètre.
c) des tentatives de contournement des consignes.
d) uniquement des questions faciles.

**Q4.** (une seule réponse) Face à une question hors périmètre, le comportement attendu de l'assistant est :

a) inventer une réponse plausible.
b) répondre à partir de connaissances générales.
c) ne rien répondre.
d) indiquer que l'information est absente et proposer une orientation.

**Q5.** (une seule réponse) Dans l'exemple, deux réponses incorrectes provenaient :

a) d'un défaut du modèle impossible à corriger.
b) d'un utilisateur malveillant.
c) d'une annexe scannée illisible dans la base documentaire.
d) d'un manque de budget.

**Q6.** (une ou plusieurs réponses) La documentation d'une solution comprend :

a) la fiche de la solution (périmètre, sources, responsable).
b) la procédure de mise à jour de la base.
c) le jeu de tests et ses résultats.
d) les mots de passe des utilisateurs.

**Q7.** (mise en situation, une seule réponse) Le pilote montre 82 % de réponses correctes et sourcées pour un critère fixé à 90 %. Que faites-vous ?

a) Analyser les erreurs, corriger (base, consignes), retester ; décider à la porte 2 sur la base des résultats.
b) Déployer quand même.
c) Abaisser le critère à 80 %.
d) Abandonner sans analyse.

**Q8.** (mise en situation, une seule réponse) Un utilisateur demande à l'assistant : « Ma dépense du 3 mars a-t-elle été approuvée ? ». Comportement attendu ?

a) Répondre « oui » pour rassurer.
b) Chercher dans les courriels.
c) Inventer une procédure.
d) Orienter vers le service financier (cas individuel).

**Q9.** (une seule réponse) Le processus cible décrit :

a) le fonctionnement actuel.
b) le contrat du fournisseur.
c) le fonctionnement après la mise en place, avec les rôles de chacun.
d) le budget.

**Q10.** (une ou plusieurs réponses) Pendant le pilote, on mesure :

a) le taux de réponses jugées utiles.
b) un échantillon de réponses vérifiées par l'expert.
c) le temps consacré par l'expert aux questions.
d) le nombre de couleurs de l'interface.

## 19.14 Corrigé détaillé : Module 19

**Q1 : c.** Après le cadrage (avant d'investir) et après le pilote (avant de généraliser).

**Q2 : b.** Fixé à l'avance, il évite d'ajuster les exigences aux résultats.

**Q3 : a, b, c.** Des questions uniquement faciles (d) surestimeraient la qualité.

**Q4 : d.** Le refus correct est un comportement essentiel.

**Q5 : c.** La qualité de la base conditionne la qualité des réponses.

**Q6 : a, b, c.** Les mots de passe (d) ne figurent jamais dans la documentation.

**Q7 : a.** On corrige et on reteste ; on ne baisse pas le critère pour le faire coïncider avec le résultat (c).

**Q8 : d.** Les cas individuels sont orientés vers le service compétent.

**Q9 : c.** Il décrit la situation visée.

**Q10 : a, b, c.** L'interface (d) n'est pas un indicateur de valeur.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS 2020*.
- NIST. (2023). *AI Risk Management Framework 1.0* (fonctions « Mesurer » et « Gérer »).
- OWASP Foundation. (2024). *OWASP Top 10 for LLM Applications* (version 2025).
- Project Management Institute. (2025). *PMBOK® Guide* (8e éd.).


# Module 20 : Gérer le changement et assurer la pérennité des solutions {#h25}

## 20.1 Mise en situation

Six mois après le déploiement de l'assistant de procédures, Horizons Partagés fait le point. Au siège, l'outil est utilisé quotidiennement. Dans deux bureaux de terrain, presque personne ne l'utilise : « on n'a pas eu le temps », « je préfère appeler Ibrahim », « une fois il s'est trompé ». Le référent numérique qui avait paramétré l'outil a quitté l'organisation ; personne n'a mis à jour la base depuis la révision de la politique de voyage ; l'abonnement a augmenté. La solution est en train de mourir doucement : un scénario fréquent.

## 20.2 Problématique

Une solution d'IA n'est pas un achat ponctuel : c'est un **changement de pratiques** qu'il faut accompagner, et un **dispositif vivant** qu'il faut gouverner, maintenir, évaluer et faire évoluer. Les causes d'échec sont rarement techniques : elles tiennent à l'adoption, à la gouvernance et aux ressources.

## 20.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. comprendre les ressorts de la résistance et de l'adoption ;
2. concevoir un plan de formation et d'accompagnement ;
3. mettre en place une gouvernance de l'IA proportionnée ;
4. organiser la maintenance, l'évaluation et l'audit des systèmes ;
5. suivre les coûts récurrents ;
6. piloter l'amélioration continue.

## 20.4 Notions et définitions

- **Conduite du changement** : ensemble des actions qui aident les personnes à passer d'une pratique à une autre.
- **Adoption** : usage effectif, régulier et approprié d'un outil par les personnes visées.
- **Gouvernance de l'IA** : rôles, règles et processus par lesquels l'organisation décide, encadre, surveille et évalue ses usages de l'IA.
- **Dérive** : dégradation progressive des performances d'un système (documents obsolètes, changements des données, nouvelles versions de modèles).
- **Audit d'un système d'IA** : examen indépendant de la conformité, de l'efficacité et des risques d'un système.

## 20.5 Explications détaillées

### Comprendre la résistance

La résistance au changement a souvent des causes légitimes : peur de perdre son emploi ou sa compétence, crainte d'être surveillé, mauvaise expérience avec l'outil, surcharge de travail, absence de sens. La traiter suppose d'écouter, d'expliquer, d'associer, et parfois d'adapter le projet.

![Figure 20.2 : Facteurs d'adoption d'un nouvel outil](03_ILLUSTRATIONS/figures/fig_20_2.svg){#fig-20-2}

Les modèles d'acceptation de la technologie, largement étudiés en sciences de gestion, mettent en avant quelques déterminants : l'**utilité perçue** et la **facilité d'utilisation perçue** (Davis, 1989), auxquelles le modèle UTAUT ajoute l'**influence sociale** et les **conditions facilitantes** (Venkatesh et al., 2003). Traduction pratique :

| Déterminant | Question que se pose la personne | Actions |
|---|---|---|
| Utilité perçue | « Est-ce que cela m'aide vraiment ? » | Démontrer sur ses propres tâches ; partager des exemples concrets de collègues |
| Facilité perçue | « Est-ce simple pour moi ? » | Modèles prêts à l'emploi ; formation courte et pratique ; aide disponible |
| Influence sociale | « Les autres l'utilisent-ils ? » | Ambassadeurs dans chaque équipe ; exemple de la direction |
| Conditions facilitantes | « Ai-je le matériel, le temps, le droit ? » | Équipement ; temps dédié ; règles claires sur ce qui est permis |

Table: Tableau 20.1 : Explications détaillées

### Gestion des équipes

- **Expliquer le pourquoi** : quel problème, quel bénéfice pour les équipes et pour la mission, et ce que l'organisation fera du temps gagné.
- **Rassurer sur l'emploi et la surveillance** : dire clairement si l'outil sera utilisé pour évaluer les personnes (il ne devrait pas l'être sans cadre explicite).
- **Associer** : utilisateurs testeurs, ambassadeurs, retours réguliers.
- **Reconnaître** les efforts et les réussites.
- **Accepter** les ajustements, y compris l'abandon d'un outil qui ne sert pas.

### Formation

Une formation efficace est **courte, pratique, liée aux tâches réelles, progressive et répétée**. Un plan de formation (annexe 16, fiche P20.1) comprend :

1. **un socle commun** pour tous (2 à 3 heures) : ce qu'est l'IA, ses limites, la politique de l'organisation, le feu tricolore, la vérification ;
2. **des modules métier** (1 à 2 heures) : les fiches prompts et solutions du métier ;
3. **une formation spécifique** pour chaque outil déployé ;
4. **une formation des référents** (plus approfondie) ;
5. **des rappels** : astuces mensuelles, partage de cas, mise à jour lors des changements.

Les petites habitudes répétées comptent davantage que les grandes formations ponctuelles : une « minute IA » en réunion d'équipe, une bibliothèque de prompts enrichie chaque mois, un canal d'entraide.

### Gouvernance de l'IA

![Figure 20.1 : Gouvernance de l'IA dans l'ASBL](03_ILLUSTRATIONS/figures/fig_20_1.svg){#fig-20-1}

Une gouvernance proportionnée à la taille de l'organisation comprend :

- **une politique d'utilisation de l'IA** adoptée par le conseil (annexe 10) ;
- **une personne référente** (ou un comité dans les grandes organisations) chargée du registre des outils, de la validation des nouveaux usages, des incidents et de la formation ;
- **des registres** : outils (annexe 9), risques (annexe 8), incidents ;
- **un circuit de validation** des nouveaux cas d'usage (examen éthique du module 8) ;
- **un bilan annuel** au conseil.

Les cadres de référence offrent des repères pour structurer cette gouvernance : la fonction « Gouverner » du NIST AI RMF, ou les exigences de système de management d'ISO/IEC 42001:2023 pour les organisations qui souhaitent aller plus loin, voire viser une certification.

### Maintenance

Chaque solution a un **responsable désigné** et un **suppléant**, et une **fiche de maintenance** : mises à jour de la base documentaire ; relance du jeu de tests après chaque mise à jour (de la base, des consignes ou du modèle utilisé par le fournisseur) ; revue des droits d'accès ; vérification des automatisations ; suivi des changements de conditions du fournisseur.

### Évaluation et performance

Les indicateurs définis dans le cahier des charges sont suivis dans le temps. On évalue aussi :

- **l'adoption** : nombre d'utilisateurs actifs, fréquence, par équipe ;
- **la qualité** : échantillons vérifiés, incidents, signalements ;
- **les effets** : temps, délais, erreurs, satisfaction ;
- **les effets non prévus** : nouvelles erreurs, perte de compétences, charge de vérification.

### Audit des systèmes

Une fois par an (ou à chaque changement important), un audit, interne ou externe, examine : conformité à la politique et aux lois ; exactitude des registres ; efficacité des contrôles humains (sont-ils réellement exercés ?) ; résultats des tests ; sécurité et droits d'accès ; gestion des incidents ; coûts et bénéfices.

### Coûts récurrents

Les coûts d'une solution évoluent : nombre d'utilisateurs, volumes, hausses tarifaires, nouvelles fonctions payantes, temps de maintenance. Un suivi trimestriel compare les coûts réels au budget et à la valeur produite ; il éclaire les décisions de renouvellement, d'extension ou d'arrêt.

### Amélioration continue

Le cycle **planifier, faire, vérifier : agir** s'applique : analyser les incidents et les signalements ; exploiter les questions sans réponse ; mettre à jour la base et les consignes ; enrichir les jeux de tests ; partager les bonnes pratiques ; décider chaque année de poursuivre, d'étendre, de modifier ou d'arrêter.

## 20.6 Application : relancer l'assistant de procédures

| Problème constaté | Cause | Action | Responsable | Échéance |
|---|---|---|---|---|
| Faible usage dans deux bureaux | Pas de formation sur place ; pas d'ambassadeur | Session pratique de 1 h 30 par bureau ; désignation d'un ambassadeur | Référente IA | 6 semaines |
| Méfiance après une erreur | Erreur non expliquée | Communication sur l'erreur, sa cause et la correction ; rappel de la vérification | Responsable financier | 2 semaines |
| Base non mise à jour | Départ du référent ; pas de suppléant | Désignation d'une référente et d'un suppléant ; procédure de mise à jour liée au circuit de validation des procédures | Direction | Immédiat |
| Coût en hausse | Licences inutilisées | Revue des licences ; suppression des comptes inactifs | Référente IA + finances | 1 mois |
| Pas d'évaluation | Indicateurs non suivis | Tableau de bord trimestriel ; bilan au comité de direction | Référente IA | Trimestriel |

Table: Tableau 20.2 : Application : relancer l'assistant de procédures

### Solutions selon le niveau

| Niveau | Gouvernance | Formation | Maintenance et évaluation |
|---|---|---|---|
| Débutant | Politique d'une page, référent à temps partiel, liste des outils autorisés | Socle de 2 h, astuces mensuelles | Revue semestrielle des usages et des outils |
| Intermédiaire | Référent désigné, registres, circuit de validation, bilan annuel au CA | Socle + modules métier + ambassadeurs | Tableau de bord trimestriel, jeux de tests |
| Avancé | Comité IA, système de management inspiré d'ISO/IEC 42001, audits réguliers | Parcours par rôle, certification interne | Surveillance continue, journalisation, audit annuel |

Table: Tableau 20.3 : Application : relancer l'assistant de procédures

## 20.7 Prompt prêt à l'emploi

### Fiche P20.1 : Construire un plan de formation

**A. Titre.** Plan de formation à l'usage responsable de l'IA.

**B. Objectif.** Obtenir un plan de formation par rôle, progressif et réaliste.

**C. Contexte d'utilisation.** Avant un déploiement ; lors de l'adoption d'une politique d'IA.

**D. Données nécessaires.** Rôles et effectifs ; niveau de départ (questionnaire) ; outils autorisés ; politique d'IA ; contraintes (temps, connectivité, langues).

**E. Prompt complet.**

```text
Contexte : [NOM DE L'ASBL], [EFFECTIFS PAR RÔLE], niveau de départ :
[RÉSULTATS AGRÉGÉS DU QUESTIONNAIRE]. Outils autorisés : [LISTE].
Politique d'IA : [RÉSUMÉ]. Contraintes : [TEMPS DISPONIBLE, CONNEXION,
LANGUES].
Tâche : propose un plan de formation sur 6 mois.
Résultat attendu :
1. Tableau « Module | Public | Objectifs | Durée | Format (présentiel,
   distanciel, hors ligne) | Exercice pratique | Évaluation ».
2. Calendrier mois par mois.
3. Dispositif de soutien (ambassadeurs, canal d'entraide, astuces).
4. Indicateurs d'adoption et de compétence.
Règles : sessions de 2 h maximum ; chaque module comporte un exercice
sur une tâche réelle ; le socle commun inclut la classification des
données et la vérification des réponses.
```

**F. Instructions d'utilisation.** Ajustez selon les disponibilités ; validez avec la RH et la direction.

**G. Résultat attendu.** Un plan par rôle, un calendrier, un dispositif de soutien, des indicateurs.

**H. Exemple d'application (illustratif).** Pour Lumière des Collines (6 salariés, 30 bénévoles, connexion intermittente), le plan propose un socle de 2 heures en présentiel avec supports imprimés, des fiches prompts plastifiées près de l'ordinateur partagé, et une séance mensuelle de 30 minutes lors de la réunion des bénévoles.

**I. Méthode de vérification.** Cohérence avec la politique et les outils ; réalisme du temps demandé ; présence d'exercices réels.

**J. Précautions.** Données agrégées uniquement.

**K. Amélioration.** « Ajoute un module spécifique pour les administrateurs (1 h) centré sur la gouvernance et les risques. »

## 20.8 Résultats attendus

Des équipes formées et outillées ; une adoption mesurée et soutenue ; une gouvernance active ; des solutions maintenues, évaluées et auditées ; des coûts maîtrisés.

## 20.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Le conseil adopte la politique et reçoit le bilan annuel ; la direction décide de poursuivre, d'étendre ou d'arrêter chaque solution ; le référent IA valide les nouveaux usages ; l'audit est réalisé par une personne indépendante de la gestion de la solution.

## 20.10 Risques et erreurs à éviter

- Considérer le déploiement comme la fin du projet.
- Former une seule fois.
- Laisser une solution sans responsable ni suppléant.
- Ignorer les signaux faibles (non-usage, contournements).
- Utiliser l'outil pour surveiller les personnes sans cadre explicite.
- Ne pas suivre les coûts récurrents.

## 20.11 Exercice pratique

**Consigne (2 heures).** (1) Identifiez trois sources possibles de résistance dans votre organisation et une action pour chacune. (2) Appliquez P20.1. (3) Rédigez la fiche de maintenance d'une solution (responsable, suppléant, tâches, fréquence, indicateurs). (4) Proposez cinq indicateurs pour le bilan annuel au conseil.

**Éléments de correction.** Les résistances sont traitées comme légitimes ; le plan comprend des exercices réels ; la fiche de maintenance désigne un suppléant et prévoit la relance des tests ; les indicateurs couvrent adoption, qualité, effets et coûts.

## 20.12 Synthèse

- L'adoption dépend de l'utilité perçue, de la facilité, de l'influence sociale et des conditions facilitantes.
- La formation est courte, pratique, répétée.
- La gouvernance de l'IA est proportionnée : politique, référent, registres, bilan.
- Maintenance, évaluation, audit et suivi des coûts font vivre la solution.
- L'amélioration continue inclut la possibilité d'arrêter.

## 20.13 QCM : Module 20

**Q1.** (une seule réponse) Selon le modèle de Davis (1989), deux déterminants majeurs de l'acceptation d'une technologie sont :

a) le prix et la marque.
b) la couleur et la vitesse.
c) l'âge et le sexe.
d) l'utilité perçue et la facilité d'utilisation perçue.

**Q2.** (une ou plusieurs réponses) Le modèle UTAUT ajoute notamment :

a) l'influence sociale.
b) les conditions facilitantes.
c) le cours de l'action du fournisseur.
d) la taille de l'écran.

**Q3.** (une seule réponse) Une formation efficace à l'IA est :

a) longue et théorique, une seule fois.
b) courte, pratique, liée aux tâches réelles et répétée.
c) réservée à la direction.
d) remplacée par la documentation du fournisseur.

**Q4.** (une ou plusieurs réponses) Une gouvernance proportionnée de l'IA comprend :

a) une politique adoptée par le conseil.
b) une personne référente.
c) des registres des outils et des risques.
d) l'interdiction de tout nouvel usage.

**Q5.** (une seule réponse) La « dérive » d'un système désigne :

a) une panne de serveur.
b) une hausse de prix.
c) un changement d'interface.
d) une dégradation progressive des performances (documents obsolètes, nouvelles versions de modèles…).

**Q6.** (une seule réponse) Après une mise à jour du modèle par le fournisseur, il faut :

a) ne rien faire.
b) changer de fournisseur.
c) relancer le jeu de tests.
d) supprimer la base documentaire.

**Q7.** (mise en situation, une seule réponse) Le référent qui a paramétré l'outil quitte l'organisation sans suppléant. Le risque principal est :

a) une hausse de l'adoption.
b) l'abandon progressif de la maintenance et la dégradation de la solution.
c) une baisse des coûts.
d) aucun.

**Q8.** (mise en situation, une seule réponse) Des agents disent préférer appeler le responsable financier « car l'outil s'est trompé une fois ». Que faites-vous ?

a) Expliquer l'erreur et sa correction, rappeler la vérification, montrer des exemples réussis.
b) Rendre l'outil obligatoire.
c) Interdire les appels.
d) Supprimer l'outil.

**Q9.** (une seule réponse) L'audit d'un système d'IA doit être réalisé par :

a) la personne qui gère la solution.
b) le fournisseur.
c) l'outil lui-même.
d) une personne indépendante de la gestion de la solution.

**Q10.** (une ou plusieurs réponses) Indicateurs pertinents pour le bilan annuel :

a) utilisateurs actifs par équipe.
b) incidents et signalements.
c) coûts réels comparés au budget et à la valeur.
d) nombre de messages promotionnels du fournisseur.

## 20.14 Corrigé détaillé : Module 20

**Q1 : d.** Ce sont les deux construits fondateurs du modèle d'acceptation de la technologie.

**Q2 : a, b.** Avec la performance attendue et l'effort attendu.

**Q3 : b.** La répétition et la pratique fondent les habitudes.

**Q4 : a, b, c.** L'interdiction générale (d) n'est pas une gouvernance.

**Q5 : d.** D'où la nécessité de tests réguliers.

**Q6 : c.** Une nouvelle version peut changer les comportements.

**Q7 : b.** Responsable et suppléant sont indispensables.

**Q8 : a.** La confiance se reconstruit par la transparence et la démonstration.

**Q9 : d.** L'indépendance garantit l'objectivité.

**Q10 : a, b, c.** Le critère d est sans rapport avec la valeur.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly, 13*(3), 319–340. https://doi.org/10.2307/249008
- ISO/IEC. (2023). *ISO/IEC 42001:2023*.
- NIST. (2023). *AI Risk Management Framework 1.0*.
- Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. *MIS Quarterly, 27*(3), 425–478. https://doi.org/10.2307/30036540


# Partie VI : Laboratoire pratique et transformation durable {#h26 .partie}

*Place à l'entraînement. Le module 21 propose dix études de cas complètes, chacune reliant un problème réel à une méthode, à une solution adaptée aux moyens de l'organisation, et aux contrôles nécessaires. Le module 22 vous accompagne dans la construction de votre propre plan de transformation.*

# Module 21 : Études de cas et résolution de problèmes concrets {#h27}

## 21.1 Mise en situation

Vous avez parcouru vingt modules. Il est temps de vérifier que vous savez mobiliser ces connaissances face à des situations complètes, où les problèmes s'entremêlent : un retard de reporting cache un problème de classement, qui cache un problème de gouvernance ; une idée d'IA séduisante cache un risque pour les personnes.

## 21.2 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. analyser une situation complexe en distinguant symptômes, causes et priorités ;
2. choisir entre solution organisationnelle, automatisation classique et IA ;
3. proposer une solution adaptée au niveau de maturité et aux moyens ;
4. définir les contrôles humains, les risques et les indicateurs ;
5. argumenter vos choix.

## 21.3 Mode d'emploi

![Figure 21.1 : Les dix études de cas et leurs modules de référence](03_ILLUSTRATIONS/figures/fig_21_1.svg){#fig-21-1}

Pour chaque cas : lisez la situation ; répondez aux questions **avant** de lire l'analyse proposée ; comparez. Les analyses ne sont pas les seules réponses possibles : ce qui compte est la qualité du raisonnement. Les organisations et données sont fictives.

## Cas 1 : Comptabilité désorganisée

**Situation.** Une association culturelle (8 salariés, budget 400 000 UM) n'a pas clôturé ses comptes depuis 14 mois. Les pièces sont dans des boîtes, des courriels et des téléphones. La comptable bénévole est partie. Le trésorier veut « un logiciel avec de l'IA qui remettra tout en ordre ».

**Questions.** (1) Quelle est la première priorité ? (2) L'IA peut-elle « remettre tout en ordre » ? (3) Quelle séquence proposez-vous ?

**Analyse proposée.**

- *Symptômes* : comptes non clôturés, pièces dispersées. *Causes profondes* : absence de procédure, dépendance à une bénévole, aucun classement.
- *Priorité* : reconstituer et sécuriser l'information (pièces, relevés bancaires), puis rattraper la comptabilité, avant toute automatisation.
- *Rôle de l'IA* : utile pour **accélérer** l'extraction des données de centaines de pièces numérisées et proposer des imputations, à condition qu'une personne compétente vérifie. Elle ne peut pas reconstituer des pièces manquantes ni décider des régularisations.
- *Séquence* : (1) rassembler toutes les pièces, les numériser et les classer par mois (règle de nommage, module 7) ; (2) récupérer tous les relevés bancaires ; (3) engager un professionnel pour le rattrapage (expert-comptable ou comptable expérimenté, selon les exigences locales) ; (4) utiliser l'extraction assistée (fiche P12.1) pour accélérer la saisie, avec vérification de 100 % des montants ; (5) rapprochements bancaires mensuels sur toute la période ; (6) liste des pièces manquantes et demandes de duplicatas ; (7) procédure de traitement des pièces pour l'avenir ; (8) choix d'un logiciel adapté (niveau Débutant ou Intermédiaire).
- *Contrôles humains* : validation des écritures, des régularisations et des comptes par une personne compétente ; arrêté des comptes par l'organe compétent.
- *Indicateurs* : mois rapprochés ; pièces manquantes ; date de clôture.

## Cas 2 : Retards de reporting financier

**Situation.** Une ONG de 40 salariés envoie systématiquement ses rapports financiers trimestriels avec 20 à 30 jours de retard à ses quatre bailleurs, qui exigent chacun un format différent. Les rapports sont construits par ressaisie dans des tableurs.

**Questions.** (1) Quelles causes rechercher ? (2) Quelle solution structurelle ? (3) Où l'IA intervient-elle ?

**Analyse proposée.**

- *Causes à rechercher* (module 5) : clôture mensuelle tardive ; codes analytiques incomplets ; absence de table de correspondance entre lignes des bailleurs et comptes ; ressaisie ; validation tardive.
- *Solution structurelle* : calendrier de clôture (J+10) ; plan analytique complet (projet, bailleur, ligne) ; **tables de correspondance par bailleur** ; modèles de rapports alimentés par extraction de la comptabilité (tableau croisé ou fonction de reporting du logiciel).
- *IA* : rédaction de la note narrative d'analyse des écarts (fiche P12.3) à partir de chiffres validés ; vérification de cohérence entre rapport narratif et rapport financier. Pas de calcul par un modèle de langage.
- *Niveau* : Intermédiaire.
- *Contrôles* : revue du rapport par le responsable financier ; réconciliation rapport/comptabilité.
- *Indicateurs* : délai de remise ; nombre de corrections demandées par les bailleurs.

## Cas 3 : Risques de détournement

**Situation.** Dans une ONG, un bailleur signale que deux fournisseurs d'un bureau régional partagent la même adresse et le même numéro de téléphone. Le bureau régional effectue de nombreux achats juste sous le seuil de mise en concurrence.

**Questions.** (1) Quels tests analytiques ? (2) Comment conduire l'investigation ? (3) Quelles mesures préventives ?

**Analyse proposée.**

- *Tests* (module 13) : fournisseurs aux coordonnées communes (adresse, téléphone, compte bancaire) ; lien entre coordonnées fournisseurs et coordonnées du personnel ; fractionnement ; montants juste sous le seuil ; concentration des achats ; auto-approbation.
- *Investigation* : application de la politique de lutte contre la fraude ; information confidentielle de la direction et du président du comité d'audit ; préservation des preuves ; pas d'entretien prématuré avec les personnes concernées ; recours éventuel à un spécialiste ; respect du droit du travail et des droits des personnes.
- *Rôle de l'IA* : rapprochement de noms et d'adresses proches ; synthèse des résultats ; rédaction de la feuille de travail. Aucune conclusion automatique.
- *Prévention* : contrôle des données fournisseurs à la création et à la modification (second canal pour les RIB) ; alertes de fractionnement ; rotation et séparation des tâches ; canal de signalement confidentiel (dans l'étude ACFE 2024, le signalement était le premier mode de détection des fraudes internes de l'échantillon).
- *Indicateurs* : alertes traitées ; délais ; recommandations mises en œuvre.

## Cas 4 : Dépendance financière

**Situation.** Lumière des Collines dépend à 70 % d'un bailleur dont la convention expire dans 18 mois.

**Questions.** (1) Quelle stratégie ? (2) Quels usages de l'IA sont pertinents ? (3) Quels indicateurs ?

**Analyse proposée.**

- *Stratégie* (module 15) : objectif de diversification (par exemple : aucun bailleur au-delà de 50 % dans 3 ans ; 15 % de ressources non affectées) ; cartographie des sources ; dossier de matière première ; veille ; relation avec le bailleur actuel pour préparer le renouvellement.
- *IA (niveau Débutant)* : résumés d'appels et checklists d'éligibilité (P15.1) ; mise en forme des notes conceptuelles (P15.2) ; déclinaisons de communication pour une campagne de dons (module 17).
- *Points de vigilance* : ne pas multiplier les dossiers génériques ; go/no-go systématique ; respect des règles des bailleurs sur l'IA.
- *Indicateurs* : part du premier bailleur ; nombre de sources ; taux de succès ; ressources non affectées.

## Cas 5 : Perte de documents

**Situation.** Lors d'un audit, une fondation ne retrouve pas 15 % des pièces sélectionnées. Les documents sont répartis entre ordinateurs personnels, messageries et classeurs.

**Questions.** (1) Mesures immédiates ? (2) Organisation durable ? (3) Place de l'IA ?

**Analyse proposée.**

- *Immédiat* : recherche ciblée (messageries, ordinateurs), demande de duplicatas aux fournisseurs, note explicative à l'auditeur.
- *Durable* (module 7) : plan de classement par fonction ; règle de nommage ; canal unique de réception des factures ; lien pièce-écriture dans le logiciel ; sauvegarde 3-2-1 ; interdiction des dossiers personnels pour les documents de l'organisation.
- *IA* : indexation et classification automatique des documents numérisés (types, dates, montants) avec vérification ; à terme, recherche par le sens (assistant documentaire). L'IA ne retrouve que ce qui a été conservé.
- *Indicateurs* : taux de pièces retrouvées en moins de cinq minutes ; pièces non liées aux écritures.

## Cas 6 : Mauvais suivi de projets

**Situation.** Un réseau associatif gère 12 projets ; aucun tableau de bord commun ; les indicateurs sont définis différemment d'un projet à l'autre ; les rapports arrivent en retard et se contredisent.

**Questions.** (1) Quelles fondations ? (2) Quelle solution par niveau ? (3) Quels contrôles ?

**Analyse proposée.**

- *Fondations* (module 11) : référentiel commun d'indicateurs (définitions, méthodes de calcul, désagrégations) ; plan de S&E par projet ; calendrier de collecte.
- *Solutions* : Débutant, tableur commun avec onglets par projet et tableau de synthèse ; Intermédiaire, formulaires mobiles hors ligne reliés à une base et tableau de bord ; Avancé : système d'information de S&E intégré, rapports générés à partir des données.
- *IA* : contrôles de cohérence, synthèse des données qualitatives, rédaction des rapports d'avancement (P11.3) avec traçabilité des chiffres.
- *Contrôles* : validation mensuelle des données par les chargés de S&E ; pointage des chiffres des rapports.
- *Indicateurs* : complétude des données ; ponctualité des rapports ; nombre de contradictions détectées.

## Cas 7 : Gestion insuffisante des bénévoles

**Situation.** La Maison des Aînés Solidaires compte 80 bénévoles ; un tiers part chaque année ; les plannings sont faits à la main ; certains bénévoles se sentent peu reconnus ; des visites sont oubliées.

**Questions.** (1) Quelles causes ? (2) Quelles solutions ? (3) Quelles données protéger ?

**Analyse proposée.**

- *Causes* : accueil et formation insuffisants ; planification manuelle ; manque de reconnaissance ; absence de suivi des visites.
- *Solutions* (module 14) : parcours d'accueil (guide, binôme) ; outil de planification avec application mobile (niveau Intermédiaire) ou tableur partagé (niveau Débutant) ; proposition de planning assistée sur données pseudonymisées (P14.3) ; confirmations automatiques ; messages de reconnaissance ; entretien de départ.
- *Données à protéger* : informations sur la santé et la dépendance des personnes âgées (rouge) ; adresses ; coordonnées des bénévoles.
- *Contrôles* : validation humaine du planning ; suivi des visites non réalisées.
- *Indicateurs* : taux de visites réalisées ; taux de rétention des bénévoles ; satisfaction.

## Cas 8 : Absence de suivi des bénéficiaires

**Situation.** Une ONG de soutien scolaire ne sait pas combien d'enfants elle a réellement accompagnés l'an dernier, ni combien ont progressé. Les listes sont tenues sur papier par chaque animateur.

**Questions.** (1) Quelles données minimales collecter ? (2) Comment protéger les enfants ? (3) L'IA prédictive du décrochage est-elle une bonne idée ?

**Analyse proposée.**

- *Données minimales* (modules 7 et 18) : identifiant non signifiant, classe, groupe, présence, résultats d'évaluations définies, consentement des parents ; pas de données non nécessaires.
- *Protection* : accès restreint ; table de correspondance séparée ; consentement parental ; aucune donnée nominative dans des outils non validés ; conservation limitée.
- *IA prédictive* : à ce stade, **non**. Les données historiques n'existent pas ; les risques de stigmatisation des enfants sont réels ; une règle simple (« trois absences consécutives → appel aux parents ») répond au besoin. L'IA peut aider à construire le modèle de tableur et à analyser des données agrégées.
- *Indicateurs* : nombre d'enfants suivis ; assiduité ; progression selon les évaluations définies.

## Cas 9 : Administration manuelle

**Situation.** Dans une fondation de 25 salariés, les demandes de congé, les notes de frais, les réservations de salles et de véhicules se font par courriel et sur papier ; l'assistante administrative passe la moitié de son temps à relancer et à recopier.

**Questions.** (1) IA ou automatisation classique ? (2) Quel enchaînement ? (3) Quels risques ?

**Analyse proposée.**

- *Diagnostic* : processus à règles stables (circuits de validation connus) → **automatisation classique** d'abord (formulaires, workflows, calendriers partagés, rappels).
- *Enchaînement* (module 9) : formulaires numériques → workflow de validation → notifications → enregistrement dans un tableau ou un logiciel → archivage. L'IA intervient ponctuellement : extraction des justificatifs de notes de frais (P12.1), réponses aux questions sur les règles (assistant de procédures, module 19).
- *Risques* : automatisations non documentées ; dépendance à une personne ; données personnelles (congés maladie) à protéger ; double saisie si les outils ne sont pas reliés.
- *Indicateurs* : délai de traitement ; temps administratif libéré ; satisfaction des salariés.

## Cas 10 : Déployer une politique d'utilisation responsable de l'IA

**Situation.** Un sondage interne d'Horizons Partagés montre que 60 % du personnel utilise des assistants d'IA, souvent gratuits, sans règle ; certains y ont collé des listes de patients ou des budgets confidentiels. La direction veut agir sans freiner les usages utiles.

**Questions.** (1) Mesures d'urgence ? (2) Contenu de la politique ? (3) Comment la faire vivre ?

**Analyse proposée.**

- *Urgence* : message clair de la direction (interdiction immédiate de saisir des données rouges dans des outils non validés) ; recensement des usages ; évaluation des incidents passés (quelles données, quels outils) et, si nécessaire, conseil juridique sur les obligations éventuelles de notification selon la loi applicable.
- *Politique* (annexe 10) : objet et champ ; principes ; feu tricolore ; outils autorisés ; décisions réservées à l'humain ; transparence ; propriété intellectuelle ; signalement des incidents ; rôles (référent, direction, CA) ; formation ; sanctions proportionnées ; révision annuelle.
- *Faire vivre* (module 20) : adoption par le CA ; formation de 2 heures pour tous ; affichage du feu tricolore ; outil professionnel validé mis à disposition (pour offrir une alternative sûre) ; registre des outils et des risques ; bilan annuel.
- *Indicateurs* : personnel formé ; incidents signalés ; usages d'outils non validés (enquête anonyme) ; satisfaction.

## 21.4 Synthèse

- Les problèmes visibles cachent souvent des causes organisationnelles.
- L'automatisation classique suffit fréquemment ; l'IA intervient là où le langage, les documents et la variabilité dominent.
- Les données sensibles et les décisions sur les personnes imposent des limites fermes.
- Chaque solution s'accompagne de contrôles humains et d'indicateurs.

## 21.5 Exercice de synthèse

**Consigne (3 heures).** Choisissez le problème le plus pressant de votre organisation et rédigez une étude de cas complète selon le gabarit A→U (introduction de la partie IV), avec au moins une solution sans IA, une solution par niveau, la liste des décisions réservées à l'humain et cinq indicateurs.

**Éléments de correction.** L'étude est convaincante si les causes sont étayées par des faits, si la solution est proportionnée aux moyens, si les risques pour les personnes sont identifiés et si les indicateurs comportent une valeur de départ.

## 21.6 QCM : Module 21

**Q1.** (une seule réponse) Dans le cas 1, la première priorité est :

a) rassembler, numériser et classer les pièces et les relevés.
b) acheter un logiciel avec IA.
c) produire immédiatement les états financiers.
d) recruter un développeur.

**Q2.** (une seule réponse) Dans le cas 2, l'outil structurel clé pour produire les rapports de quatre bailleurs à partir d'une comptabilité est :

a) un assistant conversationnel.
b) un agent autonome.
c) la ressaisie.
d) la table de correspondance par bailleur.

**Q3.** (une ou plusieurs réponses) Dans le cas 3, quels tests sont pertinents ?

a) Fournisseurs aux coordonnées communes.
b) Coordonnées fournisseurs identiques à celles du personnel.
c) Fractionnement sous le seuil.
d) Nombre de pages des factures.

**Q4.** (une seule réponse) Dans le cas 3, face aux indices, l'organisation doit :

a) publier les noms des suspects.
b) appliquer sa politique de lutte contre la fraude, de façon confidentielle, en préservant les preuves.
c) laisser l'IA conclure.
d) ignorer l'alerte du bailleur.

**Q5.** (une seule réponse) Dans le cas 8, l'IA prédictive du décrochage est déconseillée principalement parce que :

a) les données historiques manquent et les risques de stigmatisation sont réels, alors qu'une règle simple suffit.
b) elle est trop chère.
c) elle est interdite partout.
d) les enfants n'utilisent pas d'ordinateur.

**Q6.** (une seule réponse) Dans le cas 9, la première réponse adaptée est :

a) un agent IA autonome.
b) un modèle prédictif.
c) le statu quo.
d) l'automatisation classique (formulaires, workflows, rappels).

**Q7.** (une ou plusieurs réponses) Dans le cas 10, les mesures d'urgence comprennent :

a) un message clair interdisant la saisie de données rouges dans des outils non validés.
b) le recensement des usages.
c) l'évaluation des incidents passés et, si nécessaire, un conseil juridique.
d) l'interdiction définitive de toute IA.

**Q8.** (une seule réponse) Dans le cas 7, quelles données sont classées rouges ?

a) Les horaires de permanence.
b) Les informations sur la santé et la dépendance des personnes âgées.
c) Le guide d'accueil des bénévoles.
d) Le calendrier des formations.

**Q9.** (une seule réponse) Dans le cas 5, l'IA :

a) peut indexer et classer les documents conservés, sous vérification.
b) peut retrouver des documents jamais conservés.
c) remplace le plan de classement.
d) dispense de sauvegarde.

**Q10.** (une ou plusieurs réponses) Points communs aux dix cas :

a) partir du problème et de ses causes.
b) proportionner la solution aux moyens.
c) prévoir des contrôles humains et des indicateurs.
d) commencer systématiquement par l'outil d'IA le plus avancé.

## 21.7 Corrigé détaillé : Module 21

**Q1 : a.** Sans pièces ni relevés, aucune comptabilité fiable n'est possible.

**Q2 : d.** Elle relie les lignes de chaque bailleur aux comptes et codes analytiques.

**Q3 : a, b, c.** Le nombre de pages (d) n'est pas un indicateur de risque.

**Q4 : b.** Confidentialité, préservation des preuves et respect des droits.

**Q5 : a.** Proportionnalité et protection des enfants.

**Q6 : d.** Les règles stables relèvent de l'automatisation classique.

**Q7 : a, b, c.** L'interdiction totale (d) pousserait les usages dans l'ombre.

**Q8 : b.** Données de santé et de dépendance : rouge.

**Q9 : a.** L'IA ne retrouve que ce qui existe.

**Q10 : a, b, c.** La démarche commence par le problème, pas par l'outil (d).

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.


# Module 22 : Construire le plan de transformation numérique et intelligente de son ASBL {#h28}

## 22.1 Mise en situation

Amina, coordinatrice de Lumière des Collines, a suivi tout le parcours de ce livre. Elle dispose d'un diagnostic, d'une matrice de cas d'usage, d'une classification des données, de quelques prompts testés. Le conseil d'administration lui demande maintenant : « Concrètement, que faisons-nous dans les trois prochains mois, avec quel budget, qui fait quoi, et comment saurons-nous si cela marche ? »

Ce dernier module transforme les apprentissages en **plan d'action**.

## 22.2 Problématique

Sans plan, les initiatives restent dispersées, dépendantes de quelques personnes enthousiastes, et s'essoufflent. Un plan trop ambitieux, lui, décourage. Le bon plan est court, concret, mesurable, et suivi d'une décision.

## 22.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. synthétiser le diagnostic en quelques constats prioritaires ;
2. choisir les priorités et les solutions ;
3. planifier sur 90 jours, puis sur 12 mois ;
4. établir un budget et une matrice des responsabilités ;
5. définir des indicateurs avec valeurs de départ et cibles ;
6. intégrer la politique d'IA ;
7. organiser l'évaluation et la décision de fin de période.

## 22.4 Notions et définitions

- **Feuille de route** : plan qui relie des objectifs à des actions datées, des responsables, des ressources et des indicateurs.
- **Jalon** : événement de contrôle marquant l'atteinte d'une étape (diagnostic validé, politique adoptée…).
- **Matrice RACI** : tableau qui précise, pour chaque activité, qui **R**éalise, qui est **A**utorité (décide et rend compte), qui est **C**onsulté et qui est **I**nformé.
- **Valeur de départ** : mesure de l'indicateur avant le changement.

## 22.5 Explications détaillées

### Étape 1 : Diagnostic synthétique

Reprenez les résultats des modules 4 à 7 et résumez-les en **cinq constats prioritaires** au maximum, chacun appuyé sur un fait mesuré. Complétez par un **autodiagnostic de maturité numérique** (annexe 1) qui situe l'organisation sur six dimensions : gouvernance du numérique, données et documents, outils, compétences, sécurité et protection des données, usages de l'IA.

### Étape 2 : Priorités

À l'aide de la matrice (module 6), retenez pour 90 jours :

- **un ou deux chantiers de fondation** (données, règles, formation) ;
- **un ou deux pilotes** à gain rapide ;
- **la préparation** d'un projet structurant, le cas échéant.

### Étape 3 : Solutions

Pour chaque priorité : niveau d'implémentation (débutant, intermédiaire, avancé) ; outils ; données ; contrôles humains ; risques (examen éthique du module 8).

### Étape 4 : Planification sur 90 jours

![Figure 22.1 : Plan de transformation sur 90 jours](03_ILLUSTRATIONS/figures/fig_22_1.svg){#fig-22-1}

Treize semaines suffisent pour poser les fondations, tester deux pilotes et décider. Au-delà, la feuille de route à 12 mois prolonge ce qui a fonctionné.

### Étape 5 : Budget

Le budget à 90 jours inclut les coûts monétaires et **le temps interne**, souvent la ressource la plus rare.

### Étape 6 : Responsabilités

Une personne pilote le plan ; chaque action a un responsable ; la direction arbitre ; le conseil adopte la politique et reçoit le bilan.

### Étape 7 : Indicateurs

Trois familles : **fondations** (politique adoptée, personnes formées, données nettoyées), **pilotes** (indicateurs des cas d'usage), **adoption et risques** (usages, incidents).

### Étape 8 : Politique d'IA

La politique (annexe 10) est adoptée au cours des cinq premières semaines : elle encadre les pilotes et l'ensemble des usages.

### Étape 9 : Évaluation et décision

En semaine 11, bilan des pilotes au regard des critères fixés ; en semaine 13, décision du conseil : poursuivre, étendre, ajuster ou arrêter ; adoption de la feuille de route à 12 mois.

## 22.6 Application : le plan à 90 jours de Lumière des Collines

### Diagnostic synthétique

| N° | Constat | Fait mesuré |
|---|---|---|
| 1 | Données de suivi des élèves non fiables | Trois fichiers divergents ; 23 doublons estimés sur 120 élèves |
| 2 | Pas de règles d'usage du numérique et de l'IA | 4 personnes sur 6 utilisent des assistants gratuits ; aucune règle |
| 3 | Décisions du conseil mal suivies | 5 décisions sur 12 de l'an dernier sans responsable |
| 4 | Charge administrative élevée de la coordinatrice | Environ 12 heures par semaine de tâches administratives répétitives |
| 5 | Dépendance financière | 70 % du budget provient d'un seul bailleur |

Table: Tableau 22.1 : Application : le plan à 90 jours de Lumière des Collines

Maturité numérique (annexe 1) : 2/5 en moyenne ; point faible : données et sécurité.

### Priorités retenues

- **Fondations** : politique d'IA et règles de données ; nettoyage du fichier élèves ; formation socle.
- **Pilote A** : projet de PV et registre des décisions (module 10) : gain rapide.
- **Pilote B** : suivi des élèves dans un tableur modèle avec formules (module 7), avec synthèse mensuelle assistée sur données agrégées.
- **Préparé pour plus tard** : veille de financements et diversification (module 15), lancée au trimestre suivant.

### Calendrier (13 semaines)

| Semaines | Action | Livrable | Jalon |
|---|---|---|---|
| 1–3 | Diagnostic et inventaire des outils et usages | Diagnostic synthétique, registre des outils | S3 : diagnostic validé par la direction |
| 2–5 | Politique d'IA et feu tricolore | Politique d'une page, affiche | S5 : politique adoptée par le CA |
| 3–6 | Formation socle (modules 1–3 et 8) | 6 salariés et 10 bénévoles formés | Néant |
| 4–5 | Nettoyage et pseudonymisation du fichier élèves | Fichier unique, table de correspondance protégée | Néant |
| 5–10 | Pilote A : PV et registre des décisions | 2 PV produits avec la méthode ; registre à jour | Néant |
| 5–10 | Pilote B : tableur de suivi et synthèse mensuelle | Tableur modèle ; 2 synthèses mensuelles | Néant |
| 6–11 | Mesure des indicateurs | Tableau de bord | Néant |
| 10–11 | Évaluation des pilotes | Note d'évaluation | S11 : bilan des pilotes |
| 12–13 | Décision et feuille de route à 12 mois | Feuille de route | S13 : décision du conseil |

Table: Tableau 22.2 : Application : le plan à 90 jours de Lumière des Collines

### Budget (montants fictifs)

| Poste | Calcul | Montant (UM) |
|---|---|---|
| Impression des supports de formation et des affiches | forfait | 60 |
| Disque externe pour la sauvegarde 3-2-1 | 1 × 80 | 80 |
| Abonnement à une suite professionnelle avec assistant (2 comptes, 3 mois) | 2 × 3 × 15 | 90 |
| Temps interne valorisé (pilotage, formation, nettoyage, pilotes) | 60 h × 10 | 600 |
| **Total** | 60 + 80 + 90 + 600 | **830** |

Table: Tableau 22.3 : Application : le plan à 90 jours de Lumière des Collines

*Le montant de l'abonnement est fictif : consultez les tarifs et les éventuels programmes destinés aux organisations à but non lucratif à la date de votre projet.*

### Matrice des responsabilités (RACI)

| Activité | Coordinatrice (Amina) | Président | Trésorier | Bénévole référent numérique | Équipe |
|---|---|---|---|---|---|
| Pilotage du plan | R | A | I | C | I |
| Politique d'IA | R | A (adoption par le CA) | C | C | C |
| Nettoyage du fichier élèves | A | I | I | R | C |
| Formation socle | R | I | I | C | : (participants) |
| Pilote A (PV, registre) | C | A | I | R | I |
| Pilote B (suivi élèves) | A | I | I | R | C |
| Évaluation et décision | R | A | C | C | I |

Table: Tableau 22.4 : Application : le plan à 90 jours de Lumière des Collines

*R = réalise ; A = autorité / décide ; C = consulté ; I = informé.*

### Indicateurs

| Indicateur | Départ | Cible à 90 jours | Source |
|---|---|---|---|
| Politique d'IA adoptée | Non | Oui | PV du CA |
| Personnes formées (salariés / bénévoles) | 0 / 0 | 6 / 10 | Feuilles de présence |
| Doublons dans le fichier élèves | ≈ 23 | 0 | Contrôle du tableur |
| Délai de diffusion du projet de PV | ≈ 30 jours | ≤ 7 jours | Registre |
| Décisions avec responsable et échéance | 7 / 12 | 100 % | Registre |
| Temps administratif répétitif de la coordinatrice | ≈ 12 h/semaine | ≤ 9 h/semaine | Journal des tâches (2 semaines) |
| Incidents liés aux données | inconnu | 0 incident rouge | Registre des incidents |

Table: Tableau 22.5 : Application : le plan à 90 jours de Lumière des Collines

### Politique, évaluation et décision

La politique d'une page est adoptée en semaine 5. En semaine 11, la note d'évaluation compare les résultats aux cibles et relève les effets inattendus (par exemple : le temps de relecture des PV a été sous-estimé). En semaine 13, le conseil décide de poursuivre les deux pilotes, de lancer la veille de financements, et adopte une feuille de route à 12 mois (annexe 17).

### Solutions selon le niveau

| Niveau | Contenu typique d'un plan à 90 jours |
|---|---|
| Débutant | Politique, feu tricolore, formation socle, nettoyage d'un fichier clé, 1 à 2 pilotes avec assistant et tableur |
| Intermédiaire | En plus : outil professionnel validé, référent désigné, registres, automatisation d'un processus, tableau de bord |
| Avancé | En plus : feuille de route SI/IA, gouvernance par comité, préparation d'un projet intégré (RAG, ERP), audit des systèmes existants |

Table: Tableau 22.6 : Application : le plan à 90 jours de Lumière des Collines

## 22.7 Prompt prêt à l'emploi

### Fiche P22.1 : Construire la feuille de route à 90 jours

**A. Titre.** Plan de transformation à 90 jours.

**B. Objectif.** Transformer un diagnostic et des priorités en plan daté, budgété, attribué et mesurable.

**C. Contexte d'utilisation.** Direction ; après les travaux des modules 5, 6 et 8.

**D. Données nécessaires.** Constats prioritaires avec faits ; cas d'usage retenus ; ressources (personnes, temps, budget) ; contraintes ; calendrier institutionnel.

**E. Prompt complet.**

```text
Contexte : [NOM DE L'ASBL], [TAILLE], niveau de maturité numérique
[X/5]. Ressources : [PERSONNES ET TEMPS DISPONIBLE], budget [MONTANT].
Contraintes : [CONNECTIVITÉ, CALENDRIER, RÉUNIONS DU CA].
Constats : <constats>[5 CONSTATS AVEC FAITS]</constats>
Priorités retenues : <priorites>[FONDATIONS, PILOTES, PROJET À
PRÉPARER]</priorites>
Tâche : construis un plan à 13 semaines.
Résultat attendu :
1. Tableau « Semaines | Action | Livrable | Responsable (fonction) |
   Jalon ».
2. Budget : postes et méthode de calcul (sans inventer de prix ;
   laisse « à chiffrer » si nécessaire).
3. Matrice RACI.
4. Indicateurs : « Indicateur | Départ | Cible | Source ».
5. Risques du plan et mesures.
6. Modalités d'évaluation (semaine 11) et de décision (semaine 13).
Règles : pas plus de 2 pilotes ; charge compatible avec le temps
disponible indiqué ; la politique d'IA doit être adoptée avant le
démarrage des pilotes impliquant des données internes.
```

**F. Instructions d'utilisation.** Ajustez le plan avec l'équipe ; chiffrez le budget avec des données réelles ; faites adopter le plan par la direction et présentez-le au conseil.

**G. Résultat attendu.** Un plan complet de deux à trois pages.

**H. Exemple d'application.** Le plan de Lumière des Collines présenté ci-dessus.

**I. Méthode de vérification.** Réalisme de la charge (somme des heures par personne) ; cohérence des dépendances (politique avant pilotes) ; indicateurs avec valeur de départ ; budget recalculé au tableur.

**J. Précautions.** Données orange (plan interne).

**K. Amélioration.** « Prolonge ce plan en une feuille de route à 12 mois, en distinguant ce qui sera généralisé, ce qui sera testé et ce qui sera préparé. »

## 22.8 Résultats attendus

Un plan adopté, des fondations posées, deux pilotes évalués, une décision documentée, une feuille de route à 12 mois.

## 22.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** : Le plan est arbitré par la direction ; la politique d'IA est adoptée par le conseil ; la décision de fin de période (poursuivre, étendre, ajuster, arrêter) est prise par les organes compétents au vu d'une évaluation factuelle.

## 22.10 Risques et erreurs à éviter

- Plan trop ambitieux pour le temps disponible.
- Pilotes lancés avant les règles.
- Indicateurs sans valeur de départ.
- Absence de décision à l'issue des 90 jours.
- Plan porté par une seule personne.

## 22.11 Exercice pratique : Votre plan

**Consigne (une demi-journée).** Construisez le plan à 90 jours de votre organisation avec la fiche P22.1 et les annexes 1, 3, 7, 10, 15 et 17. Présentez-le à votre direction.

**Éléments de correction.** Le plan est réussi s'il comporte : au plus cinq constats étayés ; au plus deux pilotes ; une politique d'IA adoptée avant les pilotes ; un budget incluant le temps interne ; une matrice RACI ; des indicateurs avec départ, cible et source ; une date de décision.

## 22.12 Synthèse

- Un plan efficace part de constats mesurés et retient peu de priorités.
- Treize semaines suffisent pour poser les fondations, tester et décider.
- Budget, responsabilités et indicateurs rendent le plan pilotable.
- La politique d'IA encadre les pilotes.
- La décision de fin de période est un acte de gouvernance.

## 22.13 QCM : Module 22

**Q1.** (une seule réponse) Un bon plan à 90 jours comprend au maximum :

a) dix pilotes.
b) deux pilotes, avec des chantiers de fondation.
c) aucun pilote.
d) un projet avancé unique.

**Q2.** (une seule réponse) Dans une matrice RACI, la lettre A désigne :

a) l'autorité qui décide et rend compte.
b) l'assistant.
c) l'auditeur.
d) l'acheteur.

**Q3.** (une ou plusieurs réponses) Un indicateur bien défini comporte :

a) une valeur de départ.
b) une cible.
c) une source.
d) une formulation vague.

**Q4.** (une seule réponse) La politique d'IA doit être adoptée :

a) après les pilotes.
b) seulement si un incident survient.
c) avant le démarrage des pilotes impliquant des données internes.
d) jamais dans une petite structure.

**Q5.** (une seule réponse) Dans le budget de Lumière des Collines, le total est de :

a) 230 UM
b) 830 UM
c) 600 UM
d) 900 UM

**Q6.** (une ou plusieurs réponses) Les jalons du plan de Lumière des Collines comprennent :

a) le diagnostic validé en semaine 3.
b) la politique adoptée en semaine 5.
c) la décision du conseil en semaine 13.
d) l'achat d'un ERP en semaine 2.

**Q7.** (mise en situation, une seule réponse) Au bout de 90 jours, un pilote n'atteint pas ses cibles. Que faites-vous ?

a) Ne rien dire.
b) Modifier les cibles a posteriori.
c) Lancer trois nouveaux pilotes.
d) Analyser les causes et proposer au conseil d'ajuster ou d'arrêter, sur la base de l'évaluation.

**Q8.** (mise en situation, une seule réponse) Le plan prévoit 40 heures de travail pour une coordinatrice qui n'a que 3 heures libres par semaine. Que faites-vous ?

a) Maintenir le plan.
b) Demander à l'IA de faire le travail.
c) Réduire le périmètre ou répartir la charge, et vérifier la faisabilité.
d) Repousser le plan d'un an.

**Q9.** (une seule réponse) Le temps interne dans le budget :

a) est gratuit et ne doit pas apparaître.
b) doit être estimé, car c'est souvent la ressource la plus rare.
c) ne concerne que les bénévoles.
d) est payé par le bailleur.

**Q10.** (une ou plusieurs réponses) La feuille de route à 12 mois distingue :

a) ce qui sera généralisé.
b) ce qui sera testé.
c) ce qui sera préparé.
d) ce qui sera caché au conseil.

## 22.14 Corrigé détaillé : Module 22

**Q1 : b.** Peu de pilotes, bien suivis, et des fondations solides.

**Q2 : a.** L'autorité décide et rend compte.

**Q3 : a, b, c.** Une formulation vague (d) empêche la mesure.

**Q4 : c.** Les règles encadrent les pilotes.

**Q5 : b.** 60 + 80 + 90 + 600 = 830.

**Q6 : a, b, c.** Aucun achat d'ERP n'est prévu (d).

**Q7 : d.** L'évaluation fonde la décision ; on ne modifie pas les cibles après coup (b).

**Q8 : c.** Un plan irréaliste échoue ; la charge doit être compatible avec les ressources.

**Q9 : b.** Le temps interne est un coût réel.

**Q10 : a, b, c.** La transparence envers le conseil est la règle (d).

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.


# Conclusion générale {#h29 .unnumbered}

Au début de ce livre, une trésorière cherchait une facture à 18 h 40, un coordinateur recopiait trois fois les mêmes chiffres, une chargée de communication s'interrogeait sur des consentements, un président se demandait si son organisation était en retard.

Vous savez désormais que la réponse à leurs difficultés ne se trouve pas d'abord dans un outil. Elle commence par une compréhension lucide de ce qu'est l'intelligence artificielle (un ensemble de techniques statistiques puissantes, utiles pour des tâches précises, sujettes à l'erreur, et dépourvues de jugement. Elle se poursuit par une connaissance fine de son organisation : ses processus réels, ses causes profondes de dysfonctionnement, ses risques, ses personnes. Elle exige des fondations : des données ordonnées, des règles éthiques et de sécurité, des outils proportionnés. Elle se concrétise, métier par métier, dans des processus où chacun sait ce que fait l'IA, ce que fait le logiciel, ce que fait le professionnel) et ce qui doit être vérifié. Elle ne dure que si elle est accompagnée, gouvernée, maintenue et évaluée.

Trois convictions traversent l'ouvrage.

**La première : le problème avant l'outil.** Les projets réussis partent d'un problème mesuré et de ses causes. Souvent, une règle, un modèle de document ou une réorganisation suffisent. L'IA intervient là où les documents, le langage et la variabilité rendent les règles impossibles à écrire.

**La deuxième : l'humain reste responsable.** L'IA propose, signale, rédige, résume, classe. Elle ne valide pas une écriture, n'approuve pas un paiement, ne recrute pas, n'attribue pas une aide, ne traite pas un signalement d'abus. Ces décisions engagent des personnes et l'organisation ; elles restent humaines, motivées, contestables.

**La troisième : commencer petit, mesurer, décider.** Un plan de quatre-vingt-dix jours, deux pilotes bien suivis, des indicateurs avec une valeur de départ et une décision explicite valent mieux qu'une transformation spectaculaire annoncée et jamais réalisée.

Les outils changeront : probablement très vite. Les fonctionnalités décrites aujourd'hui comme avancées deviendront banales, et de nouveaux risques apparaîtront. Les méthodes de ce livre, elles, resteront valables : diagnostiquer, prioriser, protéger, expérimenter, contrôler, apprendre.

Le moment est venu de passer à l'action. Ouvrez l'annexe 1, réalisez votre autodiagnostic, réunissez deux ou trois collègues, et construisez votre plan. Votre organisation n'a pas besoin de devenir une entreprise technologique. Elle a besoin de rester fidèle à sa mission, avec un peu plus de temps, un peu plus de rigueur, et un peu plus de moyens pour les personnes qu'elle sert.

# Feuille de route de transformation {#h30 .unnumbered}

La feuille de route ci-dessous résume le parcours proposé. Elle se lit comme une boussole : chaque organisation l'adapte à sa taille, à ses moyens et à son contexte.

| Horizon | Objectif | Actions clés | Modules et annexes |
|---|---|---|---|
| **Mois 1** | Comprendre et encadrer | Sensibiliser la gouvernance ; recenser les usages ; adopter des règles provisoires ; former le socle commun | M1–M3, M8 ; annexes 10, 11, 12 |
| **Mois 1–2** | Diagnostiquer | Autodiagnostic de maturité ; cartographie de 2 ou 3 processus clés ; arbre des causes | M4, M5 ; annexes 1, 2, 6 |
| **Mois 2** | Prioriser | Fiches d'opportunité ; matrice de sélection ; choix de deux pilotes | M6 ; annexes 3, 4 |
| **Mois 2–3** | Poser les fondations | Plan de classement ; nettoyage des données clés ; sauvegarde ; politique d'IA adoptée | M7, M8 ; annexes 9, 10, 11 |
| **Mois 3** | Expérimenter | Pilotes avec contrôles humains et indicateurs ; bibliothèque de prompts | M9–M18 ; annexes 13, 14, 18 |
| **Fin du mois 3** | Décider | Évaluation des pilotes ; décision du conseil ; feuille de route à 12 mois | M19, M22 ; annexes 17, 21 |
| **Mois 4–12** | Généraliser et structurer | Déploiement des pilotes concluants ; projet structurant (assistant documentaire, intégration comptable) ; gouvernance de l'IA | M19, M20 ; annexes 5, 7, 8, 15, 16, 22 |
| **Chaque année** | Évaluer et améliorer | Bilan au conseil ; audit des systèmes ; mise à jour de la politique et des registres | M13, M20 ; annexes 19, 20, 21 |

Table: Tableau 0.1 : Pages liminaires



# Bibliographie {#h31 .unnumbered}

## Normes, cadres et instruments internationaux {.unnumbered}

Committee of Sponsoring Organizations of the Treadway Commission. (2013). *Internal control : Integrated framework*. COSO.

Conseil de l'Europe. (2018). *Protocole d'amendement à la Convention pour la protection des personnes à l'égard du traitement automatisé des données à caractère personnel* (STCE n° 223).

Conseil de l'Europe. (2024). *Convention-cadre du Conseil de l'Europe sur l'intelligence artificielle et les droits de l'homme, la démocratie et l'État de droit* (STCE n° 225).

CHS Alliance, Groupe URD, & Sphere. (2024). *Core humanitarian standard on quality and accountability* (édition 2024).

International Non-Profit Reporting Foundation. (2025). *International non-profit accounting standard (INPAS)*. Projet IFR4NPO, CIPFA et Humentum.

ISO/IEC. (2023). *ISO/IEC 42001:2023, Information technology, Artificial intelligence : Management system*. Organisation internationale de normalisation et Commission électrotechnique internationale.

National Institute of Standards and Technology. (2023). *Artificial intelligence risk management framework (AI RMF 1.0)* (NIST AI 100-1). https://doi.org/10.6028/NIST.AI.100-1

National Institute of Standards and Technology. (2024). *Artificial intelligence risk management framework: Generative artificial intelligence profile* (NIST AI 600-1). https://doi.org/10.6028/NIST.AI.600-1

OCDE. (2019, révisée en 2024). *Recommandation du Conseil sur l'intelligence artificielle* (OECD/LEGAL/0449).

OCDE, Réseau du CAD sur l'évaluation du développement. (2019). *Better criteria for better evaluation: Revised evaluation criteria definitions and principles for use*. OCDE.

OCDE. (2021). *Applying evaluation criteria thoughtfully*. Éditions OCDE.

OWASP Foundation. (2024). *OWASP top 10 for large language model applications* (version 2025).

Project Management Institute. (2025). *A guide to the project management body of knowledge (PMBOK® guide)* (8e éd.).

Règlement (UE) 2016/679 du Parlement européen et du Conseil du 27 avril 2016 relatif à la protection des personnes physiques à l'égard du traitement des données à caractère personnel et à la libre circulation de ces données (règlement général sur la protection des données). *Journal officiel de l'Union européenne*, L 119.

Règlement (UE) 2024/1689 du Parlement européen et du Conseil du 13 juin 2024 établissant des règles harmonisées concernant l'intelligence artificielle. *Journal officiel de l'Union européenne*, 12 juillet 2024.

Règlement (UE) 2026/1744 modifiant le règlement (UE) 2024/1689 (« omnibus numérique sur l'IA »). *Journal officiel de l'Union européenne*, 24 juillet 2026. [Référence à confirmer sur EUR-Lex avant publication.]

The Institute of Internal Auditors. (2024). *Global internal audit standards*.

UNESCO. (2021). *Recommandation sur l'éthique de l'intelligence artificielle*.

W3C. (2023, mise à jour 2024). *Web content accessibility guidelines (WCAG) 2.2*. World Wide Web Consortium.

## Publications scientifiques et rapports {.unnumbered}

Agence internationale de l'énergie. (2025). *Energy and AI*. AIE.

Association of Certified Fraud Examiners. (2024). *Occupational fraud 2024: A report to the nations*. ACFE.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency* (pp. 610–623). https://doi.org/10.1145/3442188.3445922

Brynjolfsson, E., Li, D., & Raymond, L. R. (2025). Generative AI at work. *The Quarterly Journal of Economics, 140*(2), 889–942.

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly, 13*(3), 319–340. https://doi.org/10.2307/249008

Dell'Acqua, F., McFowland III, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). *Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge worker productivity and quality* (Working Paper No. 24-013). Harvard Business School. [Publié ultérieurement dans *Organization Science*.]

Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J., Madotto, A., & Fung, P. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys, 55*(12), article 248.

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems, 33*.

Marelli, M. (Dir.). (2024). *Handbook on data protection in humanitarian action* (3e éd.). Cambridge University Press ; Comité international de la Croix-Rouge. https://doi.org/10.1017/9781009414630

Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*.

Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. *MIS Quarterly, 27*(3), 425–478. https://doi.org/10.2307/30036540

## Méthodologie éditoriale {.unnumbered}

American Psychological Association. (2020). *Publication manual of the American Psychological Association* (7e éd.).

## Inspiration éditoriale {.unnumbered}

Clear, J. (2018). *Atomic habits*. Avery.

Gawande, A. (2009). *The checklist manifesto: How to get things right*. Metropolitan Books.

Heath, C., & Heath, D. (2007). *Made to stick: Why some ideas survive and others die*. Random House.

Minto, B. *The pyramid principle: Logic in writing and thinking*. [Édition à préciser selon l'exemplaire consulté.]

Mollick, E. (2024). *Co-intelligence: Living and working with AI*. Portfolio/Penguin.

Zinsser, W. *On writing well*. Harper. [Première édition 1976 ; édition à préciser.]

# Webographie {#h32 .unnumbered}

| Ressource | Institution | Adresse |
|---|---|---|
| Principes de l'OCDE sur l'IA | OCDE | https://oecd.ai/en/principles |
| Instrument OECD/LEGAL/0449 | OCDE | https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449 |
| Cadre de gestion des risques de l'IA (AI RMF) | NIST | https://www.nist.gov/itl/ai-risk-management-framework |
| ISO/IEC 42001:2023 (fiche de la norme) | ISO | https://www.iso.org/standard/42001 |
| Règlement (UE) 2024/1689 | EUR-Lex | https://eur-lex.europa.eu/eli/reg/2024/1689/oj |
| Règlement (UE) 2016/679 | EUR-Lex | https://eur-lex.europa.eu/eli/reg/2016/679/oj |
| Convention-cadre sur l'IA | Conseil de l'Europe | https://www.coe.int/fr/web/artificial-intelligence |
| Recommandation sur l'éthique de l'IA | UNESCO | https://unesdoc.unesco.org/ark:/48223/pf0000381137 |
| Global Internal Audit Standards | IIA | https://www.theiia.org/en/standards/2024-standards/global-internal-audit-standards/ |
| Critères d'évaluation du CAD | OCDE | https://www.oecd.org/en/publications/better-criteria-for-better-evaluation_15a9c26b-en.html |
| Core Humanitarian Standard | CHS Alliance | https://www.corehumanitarianstandard.org |
| Handbook on Data Protection in Humanitarian Action | CICR / Cambridge University Press | https://doi.org/10.1017/9781009414630 |
| OWASP Top 10 for LLM Applications | OWASP | https://genai.owasp.org/llm-top-10/ |
| WCAG 2.2 | W3C | https://www.w3.org/TR/WCAG22/ |
| Energy and AI | AIE | https://www.iea.org/reports/energy-and-ai |
| Occupational Fraud 2024 | ACFE | https://legacy.acfe.com/report-to-the-nations/2024/ |
| IFR4NPO / INPAS | CIPFA et Humentum | https://www.ifr4npo.org |
| AI Ethics for Nonprofits : Toolkit | NetHope (catalogue OCDE.AI) | https://oecd.ai/en/catalogue/tools/artificial-intelligence-ai-ethics-for-nonprofits |

Table: Tableau 0.1 : Inspiration éditoriale

# Index alphabétique {#index-alpha .unnumbered}

*Les renvois indiquent les modules (M) où la notion est principalement traitée ; « Glossaire » renvoie aux pages liminaires.*

::: index
**agent IA** : M2, M6, M9, M21

**AI Act** : Glossaire, M8, M14

**anonymisation** : M8

**API** : Glossaire, M7, M9

**apprentissage automatique** : Glossaire, M1, M2

**apprentissage profond** : M1, M2

**arbre à problèmes** : M11

**assistant conversationnel** : M1, M2, M3, M9

**audit interne** : M13

**bailleur** : Glossaire, M1, M3, M4, M5, M7, M8, M9, M10, M11, M12, M15, M16, M17, M18, M21, M22

**base de connaissances** : Glossaire, M2, M14

**bénévole** : Glossaire, M1, M2, M4, M7, M8, M10, M14, M20, M21, M22

**biais** : M1, M2, M8, M12, M14

**budget** : Glossaire, M4, M5, M6, M8, M9, M11, M12, M15, M16, M19, M20, M21, M22

**CADRE** : M3

**cadre logique** : M11, M15

**cahier des charges** : M19

**chaîne de résultats** : M11

**cloud** : M9

**consentement** : M4, M8, M10, M15, M17, M21

**contrôle interne** : Glossaire, M4, M5, M12, M13

**COSO** : M5, M13

**cybersécurité** : Glossaire, M8

**donnée personnelle** : Glossaire

**droit d'auteur** : Glossaire, M2, M8

**éligibilité** : M11, M12, M15, M18

**extraction** : M5, M6, M9, M10, M12, M13, M16, M21

**faible connectivité** : Glossaire, M9, M18

**faux positif** : M13

**feu tricolore** : M8, M21, M22

**fonds affectés** : M12

**fractionnement** : M13, M21

**gouvernance** : Glossaire, M1, M3, M4, M8, M10, M12, M13, M20, M22

**hallucination** : M1, M2

**immobilisation** : M16

**imputation** : M6, M12

**indicateur** : Glossaire, M3, M4, M5, M6, M7, M10, M11, M12, M13, M14, M15, M16, M17, M18, M19, M20, M21, M22

**injection de prompt** : M2

**inventaire** : M16

**ISO/IEC 42001** : M8, M20

**jeu de tests** : M19, M20

**matrice de sélection** : M6

**minimisation** : M8, M18

**NIST** : M2, M8, M20

**no-code** : Glossaire, M9

**OCDE** : Glossaire, M1, M8, M11

**OCR** : Glossaire, M1, M2

**pilote** : M6, M9, M12, M19, M22

**piste d'audit** : Glossaire, M12

**plainte** : M18

**plan de classement** : M5, M7, M21

**procès-verbal** : M10, M16

**prompt** : Glossaire, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14, M15, M16, M17, M18, M19, M20, M22

**pseudonymisation** : Glossaire, M7

**RACI** : M22

**RAG** : Glossaire, M2, M6, M7, M9, M10, M11, M12, M14, M15, M19

**rapprochement à trois voies** : M12, M16

**rapprochement bancaire** : M12

**recrutement** : M4, M8, M14

**registre des décisions** : M10, M22

**réversibilité** : M9

**RGPD** : Glossaire, M8, M14

**RPA** : Glossaire, M2

**sauvegarde** : M7, M21

**séparation des tâches** : Glossaire, M5, M12, M13, M16

**supervision humaine** : M8

**tableau de bord** : M12, M13, M18, M20, M21, M22

**traduction** : M1, M3, M6, M17, M18

**transparence** : M8, M17

**trésorerie** : M5, M6, M12

**UNESCO** : M1, M8

**WCAG** : M9, M17

:::

# Liste des illustrations {#liste-illustrations .unnumbered}

::: listeillus
- [Figure 0.1 : Carte des parcours de lecture](#fig-0-1)
- [Figure 1.1 : Repères historiques de l'intelligence artificielle](#fig-1-1)
- [Figure 1.2 : Les grandes familles d'intelligence artificielle](#fig-1-2)
- [Figure 2.1 : Du jeu de données au modèle, puis à la prédiction](#fig-2-1)
- [Figure 2.2 : Architecture RAG (génération augmentée par la recherche)](#fig-2-2)
- [Figure 3.1 : Anatomie d'un prompt efficace : la méthode CADRE](#fig-3-1)
- [Figure 3.2 : La boucle de vérification d'une réponse d'IA](#fig-3-2)
- [Figure 4.1 : Organigramme type d'une ASBL de taille moyenne](#fig-4-1)
- [Figure 4.2 : Les cycles de fonctionnement d'une ASBL](#fig-4-2)
- [Figure 5.2 : Arbre des causes : retards de reporting financier](#fig-5-2)
- [Figure 5.1 : Cartographie « tel quel » du circuit des dépenses](#fig-5-1)
- [Figure 6.2 : Arbre de décision : faut-il de l'IA, une automatisation classique ou rien ?](#fig-6-2)
- [Figure 6.1 : Matrice de priorisation valeur × faisabilité](#fig-6-1)
- [Figure 7.2 : Exemple d'arborescence documentaire et de règle de nommage](#fig-7-2)
- [Figure 7.1 : Le cycle de vie des données](#fig-7-1)
- [Figure 8.1 : Le feu tricolore de classification des données](#fig-8-1)
- [Figure 8.2 : Trois modes de supervision humaine](#fig-8-2)
- [Figure 9.1 : Trois niveaux d'implémentation](#fig-9-1)
- [Figure 10.1 : De la réunion au suivi des décisions](#fig-10-1)
- [Figure 11.1 : De l'arbre à problèmes à l'arbre à objectifs](#fig-11-1)
- [Figure 11.2 : Chaîne de résultats et indicateurs](#fig-11-2)
- [Figure 12.1 : Traitement d'une facture en 14 étapes : qui fait quoi ?](#fig-12-1)
- [Figure 12.2 : Tableau de bord fictif : exécution budgétaire par ligne](#fig-12-2)
- [Figure 13.2 : Carte thermique des risques](#fig-13-2)
- [Figure 13.1 : Entonnoir des tests analytiques assistés](#fig-13-1)
- [Figure 14.1 : Recrutement assisté : où l'IA aide, où l'humain décide](#fig-14-1)
- [Figure 15.1 : Entonnoir des opportunités de financement](#fig-15-1)
- [Figure 16.1 : Circuit achats et logistique](#fig-16-1)
- [Figure 17.1 : La chaîne éditoriale assistée](#fig-17-1)
- [Figure 18.1 : La boucle de redevabilité envers les communautés](#fig-18-1)
- [Figure 19.1 : Cycle de vie d'un projet IA dans une ASBL](#fig-19-1)
- [Figure 20.2 : Facteurs d'adoption d'un nouvel outil](#fig-20-2)
- [Figure 20.1 : Gouvernance de l'IA dans l'ASBL](#fig-20-1)
- [Figure 21.1 : Les dix études de cas et leurs modules de référence](#fig-21-1)
- [Figure 22.1 : Plan de transformation sur 90 jours](#fig-22-1)
:::

# Liste des tableaux {#liste-tableaux .unnumbered}

*Les tableaux sont numérotés par module ; le numéro 0 désigne les pages liminaires.*

- Tableau 0.1 : Présentation de l'ouvrage
- Tableau 0.2 : Présentation de l'ouvrage
- Tableau 0.3 : Guide de lecture
- Tableau 0.4 : Liste des abréviations
- Tableau 1.1 : Explications détaillées
- Tableau 1.2 : Explications détaillées
- Tableau 1.3 : Explications détaillées
- Tableau 1.4 : Application professionnelle : expliquer l'IA à son conseil d'administration
- Tableau 2.1 : Notions et définitions
- Tableau 2.2 : Explications détaillées
- Tableau 2.3 : Application professionnelle : tester un assistant avant de l'adopter
- Tableau 2.4 : Prompt prêt à l'emploi
- Tableau 3.1 : Explications détaillées
- Tableau 3.2 : Application professionnelle : trois usages quotidiens maîtrisés
- Tableau 4.1 : Explications détaillées
- Tableau 4.2 : Explications détaillées
- Tableau 4.3 : Application professionnelle : radiographie d'Horizons Partagés
- Tableau 4.4 : Application professionnelle : radiographie d'Horizons Partagés
- Tableau 5.1 : Explications détaillées
- Tableau 5.2 : Explications détaillées
- Tableau 5.3 : Application professionnelle : diagnostic du circuit des dépenses d'Horizons Partagés
- Tableau 6.1 : Explications détaillées
- Tableau 6.2 : Explications détaillées
- Tableau 6.3 : Explications détaillées
- Tableau 6.4 : Explications détaillées
- Tableau 6.5 : Application professionnelle : sélectionner deux projets pilotes
- Tableau 7.1 : Explications détaillées
- Tableau 7.2 : Explications détaillées
- Tableau 7.3 : Application professionnelle : remettre en ordre le suivi des élèves de Lumière des Collines
- Tableau 8.1 : Explications détaillées
- Tableau 8.2 : Explications détaillées
- Tableau 8.3 : Explications détaillées
- Tableau 8.4 : Explications détaillées
- Tableau 8.5 : Explications détaillées
- Tableau 8.6 : Application professionnelle : refonder le projet de Thomas
- Tableau 8.7 : Application professionnelle : refonder le projet de Thomas
- Tableau 9.1 : Explications détaillées
- Tableau 9.2 : Explications détaillées
- Tableau 9.3 : Explications détaillées
- Tableau 9.4 : Explications détaillées
- Tableau 9.5 : Application professionnelle : choisir un outil pour Horizons Partagés
- Tableau 9.6 : Application professionnelle : choisir un outil pour Horizons Partagés
- Tableau 10.1 : Explications détaillées
- Tableau 10.2 : Application métier : de la réunion au suivi des décisions à Horizons Partagés
- Tableau 11.1 : Explications détaillées
- Tableau 11.2 : Explications détaillées
- Tableau 11.3 : Explications détaillées
- Tableau 11.4 : Application métier : de l'alerte communautaire au projet financé
- Tableau 12.1 : Explications détaillées
- Tableau 12.2 : Explications détaillées
- Tableau 12.3 : Explications détaillées
- Tableau 12.4 : Application métier : automatiser le traitement des pièces à Horizons Partagés
- Tableau 13.1 : Explications détaillées
- Tableau 13.2 : Explications détaillées
- Tableau 13.3 : Explications détaillées
- Tableau 13.4 : Explications détaillées
- Tableau 13.5 : Application métier : revue des dépenses du premier trimestre au RCE
- Tableau 14.1 : Application métier : recruter un(e) chargé(e) de suivi-évaluation
- Tableau 15.1 : Explications détaillées
- Tableau 15.2 : Explications détaillées
- Tableau 15.3 : Application métier : de l'appel à projets à la note conceptuelle
- Tableau 16.1 : Explications détaillées
- Tableau 16.2 : Explications détaillées
- Tableau 16.3 : Application métier : de la demande d'achat à l'inventaire au RCE
- Tableau 17.1 : Application métier : du programme décrit au calendrier éditorial de trois mois
- Tableau 18.1 : Application métier : un mécanisme de plaintes multilingue à Horizons Partagés
- Tableau 19.1 : Explications détaillées
- Tableau 19.2 : Application : l'assistant de procédures d'Horizons Partagés
- Tableau 20.1 : Explications détaillées
- Tableau 20.2 : Application : relancer l'assistant de procédures
- Tableau 20.3 : Application : relancer l'assistant de procédures
- Tableau 22.1 : Application : le plan à 90 jours de Lumière des Collines
- Tableau 22.2 : Application : le plan à 90 jours de Lumière des Collines
- Tableau 22.3 : Application : le plan à 90 jours de Lumière des Collines
- Tableau 22.4 : Application : le plan à 90 jours de Lumière des Collines
- Tableau 22.5 : Application : le plan à 90 jours de Lumière des Collines
- Tableau 22.6 : Application : le plan à 90 jours de Lumière des Collines
- Tableau 0.1 : Pages liminaires
- Tableau 0.1 : Inspiration éditoriale
- Tableau 0.2 : Inspiration éditoriale

# Annexes et modèles téléchargeables {#h33 .unnumbered}

Les vingt-deux annexes opérationnelles sont fournies sous forme de fichiers modifiables (documents et tableurs) dans le dossier `04_ANNEXES` livré avec l'ouvrage, et regroupées dans l'archive `ANNEXES.zip`. Chaque annexe comporte des consignes, des champs à remplir et un exemple. Le tableau ci-dessous les présente et indique les modules associés.

| N° | Annexe | Usage | Modules |
|---|---|---|---|
| 1 | Questionnaire de diagnostic de maturité numérique | Se situer sur six dimensions | 5, 22 |
| 2 | Matrice d'identification des problèmes | Symptômes, causes, impacts | 5 |
| 3 | Matrice de sélection des cas d'usage IA | Priorisation pondérée | 6 |
| 4 | Fiche de cadrage d'un projet IA | Cas d'usage structuré | 6, 19 |
| 5 | Cahier des charges fonctionnel simplifié | Spécifier le besoin | 19 |
| 6 | Modèle de cartographie de processus | Processus « tel quel » et cible | 5, 19 |
| 7 | Matrice des responsabilités (RACI) | Qui fait quoi | 19, 22 |
| 8 | Registre des risques IA | Identifier, évaluer, traiter | 8, 13, 20 |
| 9 | Registre des outils IA utilisés | Inventaire et validation | 8, 9, 20 |
| 10 | Politique interne d'utilisation de l'IA | Règles communes | 8, 20, 21 |
| 11 | Fiche de classification des données | Feu tricolore | 7, 8 |
| 12 | Checklist de protection des données | Avant tout traitement | 8 |
| 13 | Modèle de validation humaine | Tracer les validations | 8, 12 |
| 14 | Fiche de contrôle des productions IA | Vérifier une sortie | 3 |
| 15 | Modèle de tableau de bord | Suivre les indicateurs | 12, 20, 22 |
| 16 | Plan de formation | Former par rôle | 20 |
| 17 | Feuille de route sur 90 jours | Planifier | 22 |
| 18 | Bibliothèque de prompts par métier | Réutiliser les fiches | 3, 10–18 |
| 19 | Modèle de suivi des anomalies | Traiter les alertes | 12, 13 |
| 20 | Modèle de suivi des recommandations | Suivre la mise en œuvre | 10, 13 |
| 21 | Modèle de mesure des performances | Avant / après | 6, 19, 22 |
| 22 | Checklist de mise en production d'une solution IA | Décider du déploiement | 19 |

Table: Tableau 0.2 : Inspiration éditoriale

Données d'exercice : `04_ANNEXES/donnees_exercices/` (fichier fictif de 40 dépenses du module 13, fichier fournisseurs, résultats des tests).

# Vous souhaitez transformer votre ASBL grâce à l'intelligence artificielle ? {#h34 .unnumbered}

Comprendre les possibilités de l'intelligence artificielle est une première étape. La véritable transformation commence lorsque ces connaissances sont intégrées aux processus, aux outils et aux pratiques quotidiennes de votre organisation.

Nous accompagnons les organisations à but non lucratif dans la modernisation et l'amélioration de leur pratique de gestion.

Les accompagnements proposés portent notamment sur :

- le diagnostic organisationnel et numérique ;
- la sélection et l'implémentation des outils d'IA ;
- la digitalisation et l'amélioration des processus ;
- le renforcement de la gouvernance ;
- l'amélioration des systèmes comptables et financiers ;
- le renforcement du contrôle interne ;
- la formation et l'accompagnement des équipes.

## L'auteur {.unnumbered}

**Verdi Imbole**, auteur indépendant, auditeur financier et consultant freelance en intelligence artificielle.

## Coordonnées {.unnumbered}

verdiimbole0@gmail.com
