## Chapitre 30. Claude appliqué aux ressources humaines et au développement des compétences

### A. Mise en situation professionnelle

Béatrice Musau, responsable RH de MCC, doit présenter au comité de direction l'état des habilitations obligatoires : à la date du 16 novembre 2026, 27 habilitations sont expirées et 46 expireront dans les 90 jours, sur 360 suivies pour 120 salariés d'un échantillon de postes à risque. Elle prépare aussi le recrutement de 35 conducteurs pour l'extension « Mbiyo Profond », dont une part doit venir des villages riverains, et l'adaptation du plan de formation à l'arrivée de l'IA dans les métiers. Elle sait que les données RH sont parmi les plus sensibles de l'entreprise.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Analyser** une matrice de formations et d'habilitations et produire un plan de rattrapage.
2. **Rédiger** des fiches de poste, annonces et grilles d'entretien inclusives et conformes.
3. **Concevoir** des supports de formation et d'évaluation avec Claude.
4. **Identifier** les usages interdits ou à haut risque de l'IA en RH (décisions individuelles, données sensibles, biais).
5. **Accompagner** les équipes dans l'évolution des compétences liée à l'IA.

### C. Comprendre avant de pratiquer : Profil du métier

*Tableau 30.1. Profil de la fonction RH.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Recrutement, formation et habilitations, gestion des carrières, rémunération, relations sociales, conformité au droit du travail |
| Tâches quotidiennes | Gestion administrative, entretiens, plans de formation, suivi des habilitations, dialogue social, réponses aux salariés |
| Difficultés | Nombreuses habilitations à suivre ; emploi local ; turnover des sous-traitants ; données sensibles ; égalité de traitement |
| Documents | Fiches de poste, contrats, conventions, plans de formation, évaluations, procédures disciplinaires |
| Données | Effectifs, habilitations et dates d'expiration, formations, absences, rémunérations, données personnelles |
| Livrables | Plans de recrutement et de formation, tableaux de bord, supports de formation, politiques RH |
| Assistables par Claude | Analyse des habilitations (code, sur données pseudonymisées) ; fiches de poste ; annonces ; grilles d'entretien ; supports de formation et quiz ; FAQ RH ; projets de politiques |
| Limites | Toute décision individuelle (recrutement, sanction, promotion, licenciement, aptitude) ; tri automatisé des candidatures ; données de santé ; avis juridiques |

::: attention
**Usages à haut risque.** Le règlement européen sur l'intelligence artificielle classe parmi les usages à haut risque les systèmes d'IA utilisés pour le recrutement, la sélection et les décisions affectant les relations de travail [@EU-AIACT]. Même lorsque ce règlement ne s'applique pas directement, il donne un repère utile. À MCC, la charte IA **interdit** l'usage de Claude pour trier, classer ou évaluer des candidats ou des salariés individuellement, et pour traiter des données de santé.
:::

### D. Démonstration guidée : Cas d'usage

#### Cas d'usage 30.1. Plan de rattrapage des habilitations

**1. Problème.** Des habilitations obligatoires (travail en hauteur, produits chimiques, consignation…) sont expirées ou proches de l'expiration ; des personnes peuvent travailler sans habilitation valide.

**2. Méthode habituelle.** Extraction du logiciel RH, tri manuel, relances par courriel.

**3. Contribution de Claude.** Analyse par code sur données **pseudonymisées** (matricules), tableau par formation et par poste, priorisation selon le niveau de risque fourni, calendrier de sessions, messages aux managers.

**4. Données.** `MCC_matrice_formations.csv` (matricules, postes, formations, dates) ; capacité des sessions ; niveau de risque par formation (fourni par le HSE).

**5–6. Procédure et prompt.**

```text
[C] Responsable RH de MCC. Date de référence : 16/11/2026.
[A] Analyse l'état des habilitations et propose un plan de rattrapage.
[D] MCC_matrice_formations.csv (pseudonymisé). Capacité : 12 personnes par session ;
2 sessions par semaine par formation. Priorité HSE : 1) Consignation, Travail en hauteur,
Produits chimiques ; 2) Premiers secours, Conduite défensive ; 3) Induction.
[R] Exécution de code. Aucune donnée nominative dans la sortie. Ne te prononce pas sur l'aptitude
d'une personne à travailler : signale seulement les habilitations expirées.
[E] 1) Tableau : formation × statut (expirée, < 90 jours, valide) ; 2) graphique ; 3) calendrier
de sessions sur 8 semaines, par priorité ; 4) message type aux managers (100 mots).
```

**7. Échanges.** « Liste, par poste, les matricules ayant au moins une habilitation prioritaire expirée, pour transmission confidentielle aux managers concernés. »

**8. Exemple de résultat (données fictives).** 27 habilitations expirées (dont 8 pour le travail en hauteur et 6 pour la manipulation de produits chimiques) concernant 26 matricules, et 46 expirant dans les 90 jours.

![Figure 30.1. État des formations obligatoires au 16/11/2026 (données fictives MCC, 360 habilitations suivies). Graphique réalisé pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig30_1_formations.png){width=90%}

**9. Contrôle.** Vérification de 10 lignes dans le logiciel RH ; validation des priorités par le HSE.

**10. Erreurs possibles.** Formats de dates mal lus (jour/mois) ; doublons de formations.

**11. Limites.** La décision d'affecter ou non une personne à une tâche relève du manager et du HSE, selon la procédure.

**12. Livrable.** Plan de rattrapage et messages aux managers.

#### Cas d'usage 30.2. Recrutement de conducteurs : annonce et grille d'entretien

**1. Problème.** Recruter 35 conducteurs, en favorisant l'emploi local, avec un processus équitable.

**2. Méthode habituelle.** Reprise d'anciennes annonces ; grilles d'entretien hétérogènes.

**3. Contribution de Claude.** Fiche de poste, annonce en français simple, grille d'entretien structurée, questions comportementales liées à la sécurité, relecture anti-biais.

**4. Données.** Référentiel de compétences, conditions du poste, politique d'emploi local, procédure de recrutement.

**5–6. Procédure et prompt.**

```text
Rédige pour le poste de conducteur de camion minier (90 t), à partir du référentiel joint :
1) une annonce en français simple, diffusable dans les villages riverains (canaux : radio locale,
affichage), précisant les critères objectifs et la procédure ;
2) une grille d'entretien structurée : 6 questions comportementales (sécurité, travail en équipe,
respect des règles), avec pour chacune des exemples de réponses attendues et un barème descriptif.
Règles : aucun critère sans lien avec le poste (âge, sexe, origine, situation familiale, religion) ;
langage inclusif. Termine par une relecture listant tout passage potentiellement discriminant.
```

**7. Échanges.** « Prépare une version courte de l'annonce lisible à la radio (60 secondes). »

**8. Exemple de résultat.** Annonce claire (conditions, critères, pièces, dates, lieu des tests) ; grille de 6 questions avec barème descriptif.

**9. Contrôle.** Revue par la RH et le juridique (conformité au droit du travail) ; vérification des critères.

**10. Erreurs possibles.** Critère indirectement discriminant (« jeune et dynamique ») ; exigences sans lien avec le poste.

**11. Limites.** L'évaluation des candidats est réalisée par des personnes, avec la grille ; **Claude ne reçoit ni ne trie les candidatures**.

**12. Livrable.** Annonce, fiche de poste et grille validées.

#### Cas d'usage 30.3. Supports de formation et quiz (condensé)

À partir d'une procédure validée (par exemple la consignation), Claude produit un module de formation : objectifs, déroulé, supports simples, cas pratiques tirés d'incidents anonymisés, quiz de 10 questions avec corrigé. Le formateur et le HSE valident le contenu technique ; le module est testé avec un groupe pilote.

#### Cas d'usage 30.4. Accompagner l'évolution des métiers avec l'IA (condensé)

Claude aide à analyser, pour chaque métier, les tâches susceptibles d'être assistées, les compétences nouvelles nécessaires (formulation d'instructions, vérification, gestion des données) et les besoins de formation, en s'appuyant sur les cartes d'opportunités produites par les services (chapitre 1). Les décisions d'organisation font l'objet d'un dialogue avec les représentants du personnel (chapitre 39).

### E. Prompts commentés

**Prompt 30.1. Relecture d'une politique RH**

```text
Relis le projet de politique « [titre] » joint. Signale : les ambiguïtés ; les dispositions qui
pourraient entraîner une inégalité de traitement ; les points à vérifier au regard du droit du travail
applicable (sans te prononcer sur la conformité) ; les termes à définir. Propose des reformulations.
```

*Commentaire.* Claude relit et questionne ; le service juridique tranche sur la conformité.

### F. Exercices pratiques

**Exercice 30.1 (guidé).** Réalisez le cas 30.1 ; retrouvez les 27 habilitations expirées et les deux formations les plus concernées.

**Exercice 30.2 (guidé).** Réalisez le cas 30.2 pour un poste de votre choix ; faites relire la grille par un collègue.

**Exercice 30.3 (autonome).** Créez le module de formation « Utiliser Claude en sécurité » pour votre service (2 heures), avec quiz.

### G. Livrable professionnel

**Tableau de bord des habilitations** et plan de rattrapage, **kit de recrutement** (fiche de poste, annonce, grille), **un module de formation** validé.

### H. Vérification des résultats

::: controle
- Les données utilisées sont pseudonymisées, et seules les données nécessaires ont été transmises.
- Aucune décision individuelle n'a été produite ou suggérée par Claude.
- Les documents de recrutement ne contiennent aucun critère discriminant.
- Les contenus de formation technique sont validés par les experts.
:::

::: setrompe
Sollicité pour « classer les 200 CV reçus », un assistant peut produire un classement argumenté en apparence objectif, mais influencé par des éléments sans lien avec le poste (style, nom, parcours). C'est précisément le type d'usage exclu par la charte de MCC. **Contre-mesure** : ne jamais confier de tri ou d'évaluation de personnes à l'IA.
:::

### I. Limites et précautions

- Les données personnelles et de santé exigent le niveau de protection le plus élevé.
- Le droit du travail applicable et les conventions collectives priment sur toute proposition de Claude.
- Le dialogue social est indispensable à toute évolution des métiers liée à l'IA.

### J. Boîte à outils

- Prompts des cas 30.1, 30.2 et prompt 30.1.
- Liste des usages RH interdits à MCC : tri de candidatures ; évaluation individuelle ; décision disciplinaire ; traitement de données de santé ; surveillance des salariés.
- Modèle de grille d'entretien structurée (Annexe D).

### K. Quiz

1. **(Vrai ou faux)** Claude peut classer les CV reçus si on lui fournit des critères objectifs.
2. **(Application)** Combien d'habilitations sont expirées dans les données d'exercice au 16/11/2026 ?
3. **(Compréhension)** Pourquoi pseudonymiser la matrice des formations avant analyse ?
4. **(QCM)** Le règlement européen sur l'IA classe les systèmes utilisés pour le recrutement comme : a) interdits ; b) à haut risque ; c) sans risque ; d) non concernés.
5. **(Mise en situation)** Un manager demande à Claude si un salarié « est apte » à reprendre le travail. Que répondez-vous ?
6. **(Compréhension)** Citez deux critères qui ne doivent jamais figurer dans une annonce.
7. **(Vrai ou faux)** Un module de formation technique produit avec Claude doit être validé par un expert.
8. **(Analyse critique)** Pourquoi un classement de candidats « argumenté » par une IA peut-il être trompeur ?
9. **(Application)** Rédigez la règle anti-discrimination à inclure dans un prompt de recrutement.
10. **(Compréhension)** Quel rôle joue le dialogue social dans l'évolution des métiers liée à l'IA ?

<div class="carnet" titre="Chapitre 30. Claude appliqué aux ressources humaines et au développement des compétences"></div>
