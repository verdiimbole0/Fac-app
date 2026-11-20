# Partie III : Préparer et sécuriser l'adoption de l'IA {.partie}

*Vous avez identifié vos priorités. Avant d'agir, trois conditions doivent être réunies : des données organisées et fiables, des règles éthiques et de sécurité claires, et des outils adaptés à vos moyens. Cette partie pose ces fondations, sans lesquelles l'IA amplifie les problèmes au lieu de les résoudre.*

# Module 7 : Les données, le carburant des systèmes intelligents

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

> **🔎 À retenir** : Il est beaucoup plus économique d'empêcher les erreurs à la saisie (listes déroulantes, champs obligatoires, formats imposés) que de les corriger ensuite.

### Organiser les documents : plan de classement et règle de nommage

![Figure 7.2 : Exemple d'arborescence documentaire et de règle de nommage](03_ILLUSTRATIONS/figures/fig_7_2.svg)

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

![Figure 7.1 : Le cycle de vie des données](03_ILLUSTRATIONS/figures/fig_7_1.svg)

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
