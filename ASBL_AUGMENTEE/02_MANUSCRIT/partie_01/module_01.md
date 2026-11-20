# Partie I : Comprendre l'intelligence artificielle {.partie}

*Avant de transformer des processus, il faut comprendre l'outil. Cette première partie explique ce qu'est l'intelligence artificielle, comment elle fonctionne réellement et comment l'utiliser de façon efficace et sûre. Aucune connaissance technique préalable n'est nécessaire.*

# Module 1 : L'intelligence artificielle : comprendre une révolution qui nous concerne tous

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

![Figure 1.1 : Repères historiques de l'intelligence artificielle](03_ILLUSTRATIONS/figures/fig_1_1.svg)

L'histoire de l'IA n'est pas une progression régulière. Elle alterne promesses et désillusions.

- **Les fondations (années 1950).** En 1950, le mathématicien Alan Turing pose la question de savoir si une machine peut penser et propose un test pour en juger. En 1956, une conférence organisée au Dartmouth College, aux États-Unis, popularise l'expression « intelligence artificielle ».
- **Les systèmes à règles (années 1970–1980).** On tente de reproduire l'expertise humaine sous forme de règles « si… alors… ». Ces « systèmes experts » fonctionnent dans des domaines étroits, mais deviennent ingérables quand les règles se multiplient. Les promesses non tenues entraînent des périodes de désintérêt et de baisse des financements, que l'on appelle les « hivers de l'IA ».
- **L'apprentissage à partir des données (années 1990–2010).** Plutôt que d'écrire les règles, on laisse la machine les déduire d'exemples. En 1997, un ordinateur bat le champion du monde d'échecs. À partir de 2012 environ, l'**apprentissage profond**, rendu possible par la puissance de calcul et l'abondance de données, fait progresser spectaculairement la reconnaissance d'images et de la parole.
- **L'ère des modèles de langage (depuis 2017).** En 2017, des chercheurs publient l'architecture « Transformer » (Vaswani et al., 2017), qui permet d'entraîner des modèles de langage beaucoup plus grands. Fin 2022, les assistants conversationnels deviennent accessibles au grand public et se diffusent à une vitesse inédite.
- **L'ère de l'encadrement (depuis le début des années 2020).** Les organisations internationales et les États adoptent des cadres : la Recommandation de l'UNESCO sur l'éthique de l'IA (2021), la révision des Principes de l'OCDE (2024), le cadre de gestion des risques du NIST (2023), la norme ISO/IEC 42001 (2023), le règlement européen sur l'IA (2024) et la Convention-cadre du Conseil de l'Europe sur l'IA (2024). Le module 8 y revient en détail.

Pourquoi cette histoire vous concerne-t-elle ? Parce qu'elle enseigne la prudence. Les annonces spectaculaires ont souvent été suivies de déceptions. Les outils actuels sont réellement utiles, mais pour des tâches précises, avec des limites précises.

### Les grandes familles d'IA

![Figure 1.2 : Les grandes familles d'intelligence artificielle](03_ILLUSTRATIONS/figures/fig_1_2.svg)

On peut se représenter les familles d'IA comme des ensembles emboîtés.

| Famille | Principe | Exemple dans une ASBL | Ce qu'il faut savoir |
|---|---|---|---|
| **Systèmes à règles** | Des règles écrites par des humains | « Si une dépense dépasse 500 UM, demander une seconde signature » | Prévisibles et explicables, mais rigides. Ce n'est pas toujours qualifié d'« IA » aujourd'hui, mais c'est souvent la meilleure solution. |
| **Apprentissage automatique** | Le système apprend à partir d'exemples | Estimer quels élèves risquent d'abandonner à partir des absences et des notes | Exige des données historiques fiables et suffisantes ; risque de biais. |
| **Apprentissage profond** | Réseaux de neurones à nombreuses couches | Lire une facture photographiée (OCR moderne) ; transcrire une réunion | Très performant sur les images, le son et le texte ; peu explicable. |
| **IA générative** | Produit de nouveaux contenus | Rédiger un projet de lettre, résumer un rapport, traduire un support | Fluide et polyvalente ; peut produire des erreurs plausibles (« hallucinations »). |

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
