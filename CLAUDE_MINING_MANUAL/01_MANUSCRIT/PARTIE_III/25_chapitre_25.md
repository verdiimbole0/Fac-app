## Chapitre 25 — Claude appliqué aux relations communautaires et à la performance sociale

### A. Mise en situation professionnelle

Joseph Banza, responsable des relations communautaires de MCC, gère un registre de 95 plaintes reçues depuis mars 2025 de trois villages riverains. Vingt et une sont « escaladées », vingt-cinq toujours « en cours ». Le comité local de suivi se réunit dans deux semaines, et les chefs de Lupanda — le village le plus concerné — attendent des réponses sur la poussière, la sécurité routière et le forage d'eau potable promis dans le cahier des charges. Joseph a appris de l'épisode du courrier « trop généreux » (chapitre 10) : Claude peut l'aider, mais la relation avec les communautés reste une affaire humaine.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Analyser** un registre de plaintes (thèmes, villages, délais, escalades) de manière traçable.
2. **Préparer** des réponses écrites respectueuses, exactes et sans engagement non autorisé.
3. **Préparer** une réunion de consultation : dossier, messages, questions, compte rendu.
4. **Rendre accessibles** des informations techniques (langage simple, traductions à valider).
5. **Respecter** la confidentialité et la dignité des personnes dans l'usage de l'IA.

### C. Comprendre avant de pratiquer — Profil du métier

Les Normes de performance de la SFI exigent notamment un mécanisme de gestion des plaintes accessible aux communautés affectées, la consultation et la participation éclairée, et traitent de la santé et de la sécurité des communautés et de la réinstallation [@IFC-PS]. Les principes et attentes de performance de l'ICMM couvrent également l'engagement avec les communautés et le respect des droits humains [@ICMM-PRINC].

*Tableau 25.1 — Profil de l'équipe relations communautaires.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Dialogue avec les communautés, mécanisme de plaintes, cahier des charges, investissement social, suivi de la réinstallation, prévention des conflits |
| Tâches quotidiennes | Visites de terrain, réunions, réception et suivi des plaintes, coordination avec les services, rapports |
| Difficultés | Attentes élevées ; délais de réponse des autres services ; langues locales ; traçabilité des engagements ; tensions |
| Documents | Registre des plaintes, comptes rendus, cahier des charges, accords, plans de réinstallation, rapports sociaux |
| Données | Plaintes (thèmes, villages, délais), suivi des engagements, emplois locaux, achats locaux, indicateurs de projets sociaux |
| Livrables | Réponses aux plaintes, comptes rendus, rapports trimestriels, supports d'information, plans d'action |
| Assistables par Claude | Analyse du registre (code) ; projets de réponses ; préparation de réunions ; comptes rendus ; vulgarisation ; projets de traduction à faire valider |
| Limites | Relation humaine, négociation, engagements de l'entreprise, évaluation des préjudices, indemnisations, gestion des tensions |

::: attention
Les plaintes contiennent des **données personnelles** (noms, situations familiales, parcelles) et parfois des informations sensibles (santé, conflits). Pseudonymisez avant tout traitement non indispensable, appliquez la classification des données (chapitre 37) et n'utilisez jamais un outil non autorisé par l'entreprise.
:::

![Figure 25.1 — Mécanisme de gestion des plaintes : la réception, l'évaluation et la clôture restent humaines ; Claude assiste l'enregistrement, la rédaction et l'analyse. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig25_2_mecanisme_plaintes.png){width=100%}

### D. Démonstration guidée — Cas d'usage

#### Cas d'usage 25.1 — Analyse du registre des plaintes avant le comité local

**1. Problème.** Joseph doit présenter une vue claire des plaintes : thèmes, villages, délais, escalades, engagements en suspens.

**2. Méthode habituelle.** Tableau croisé manuel, souvent en retard sur les données.

**3. Contribution de Claude.** Statistiques par code, graphiques, liste des plaintes anciennes non clôturées, synthèse des thèmes récurrents à partir des résumés.

**4. Données.** `MCC_registre_plaintes.csv` (95 plaintes, pseudonymisées) ; procédure du mécanisme de plaintes (délai cible de traitement).

**5–6. Procédure et prompt.**

```text
[C] Responsable des relations communautaires de MCC ; réunion du comité local de suivi dans deux semaines.
[A] Analyse le registre des plaintes.
[D] Fichier MCC_registre_plaintes.csv (pseudonymisé). Délai cible de la procédure : 30 jours.
[R] Calculs par exécution de code. Aucune interprétation des motivations des plaignants.
Ne cite aucune plainte individuellement dans la synthèse destinée au comité.
[E] 1) Tableau par catégorie et par village ; 2) répartition des statuts ; 3) délai de traitement
des plaintes clôturées (moyenne, médiane, % dans le délai cible) ; 4) liste interne des plaintes
non clôturées de plus de 60 jours ; 5) synthèse de 200 mots des thèmes, pour le comité.
```

**7. Échanges successifs.** « Quelles catégories sont le plus souvent escaladées ? » ; « Prépare pour chaque catégorie la question à poser au service concerné. »

**8. Exemple de résultat (données fictives).** 95 plaintes : Lupanda 38, Kasongo-Mbiyo 29, Mwinda 28 ; catégories principales : sécurité routière (16), bruit (15), cahier des charges, indemnisation et poussière (14 chacune) ; statuts : 49 clôturées, 25 en cours, 21 escaladées. Délai de clôture : moyenne d'environ 46 jours, médiane de 37 jours — au-delà du délai cible de 30 jours.

![Figure 25.2 — Plaintes communautaires par catégorie et par village (données fictives MCC). Graphique réalisé pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig25_1_plaintes.png){width=90%}

**9. Contrôle.** Totaux vérifiés dans le registre ; contrôle de 5 plaintes au hasard.

**10. Erreurs possibles.** Délais calculés sur des plaintes non clôturées ; doublons de plaintes collectives.

**11. Limites.** Les chiffres ne disent pas la gravité vécue ; les visites de terrain restent indispensables.

**12. Livrable.** Tableau de bord du mécanisme de plaintes et synthèse pour le comité local.

#### Cas d'usage 25.2 — Répondre à une plainte collective

**1. Problème.** Le chef de Lupanda a écrit au nom du village sur la vitesse des camions et la poussière.

**2. Méthode habituelle.** Courrier rédigé par Joseph, validé par la direction ; risque de promesse non autorisée ou de ton inadapté.

**3. Contribution de Claude.** Projet de réponse fondé uniquement sur les faits et mesures **décidées**, ton respectueux, proposition de rencontre, liste des vérifications avant envoi.

**4. Données.** Plainte (pseudonymisée si diffusée), mesures en place et décisions validées par la direction, procédure.

**5–6. Procédure et prompt.** Utilisez le prompt CADRE du chapitre 10 (section C.7), en ajoutant :

```text
Ajoute une version courte (5 phrases) destinée à être lue à voix haute lors d'une réunion
au village, en français simple. Signale les mots ou expressions qui pourraient être mal
compris et méritent une explication orale. Je ferai traduire en langue locale par un
traducteur de l'équipe : ne propose pas de traduction.
```

**7. Échanges.** « Relis le projet en te mettant à la place du chef du village : quelles phrases pourraient être perçues comme condescendantes, évasives ou comme une promesse ? »

**8. Exemple de résultat.** Courrier d'une page et version orale de cinq phrases, sans promesse nouvelle, avec proposition de réunion et rappel du mécanisme de plaintes.

**9. Contrôle.** Validation par Joseph et par la direction ; traduction par une personne qualifiée ; vérification que chaque mesure citée est décidée.

**10. Erreurs possibles.** Promesse implicite (« nous ferons tout pour… ») ; termes techniques ; ton administratif froid.

**11. Limites.** La qualité de la relation dépend des personnes et de la cohérence des actes, pas de la qualité d'un courrier.

**12. Livrable.** Courrier validé, version orale, inscription dans le registre.

#### Cas d'usage 25.3 — Préparer et documenter une réunion de consultation (condensé)

Claude prépare l'ordre du jour, un dossier d'information en langage simple (projet d'extension Mbiyo Profond : calendrier, travaux, nuisances, mesures), une liste de questions probables avec les réponses **disponibles** (et celles à apporter plus tard), puis, à partir des notes de séance, un projet de compte rendu distinguant questions, réponses données et engagements pris — à valider avec les représentants des communautés.

#### Cas d'usage 25.4 — Suivi du cahier des charges (condensé)

À partir du cahier des charges signé en 2021 et des rapports d'avancement des projets, Claude construit une matrice des engagements (projet, échéance, statut, preuves) et prépare le rapport d'avancement à présenter aux communautés. Exemple fictif : le forage d'eau potable promis à Lupanda, en retard, apparaît comme l'engagement le plus sensible — information à remonter à la direction.

### E. Prompts commentés

**Prompt 25.1 — Lecture critique d'un projet de réponse**

```text
Voici un projet de réponse à une plainte communautaire. Relis-le du point de vue
du destinataire (chef de village, non spécialiste, attentes fortes) et signale :
- les promesses explicites ou implicites ;
- les formulations évasives ou condescendantes ;
- les termes techniques ou juridiques à simplifier ;
- les informations qui pourraient être inexactes au regard des faits fournis.
Propose des reformulations, sans ajouter d'engagement.
```

*Commentaire.* Ce prompt utilise Claude comme « miroir » : il aide Joseph à voir son texte avec les yeux du destinataire, sans lui confier la relation.

### F. Exercices pratiques

**Exercice 25.1 (guidé).** Réalisez le cas 25.1 ; vérifiez à la main le nombre de plaintes escaladées.

**Exercice 25.2 (guidé).** Rédigez la réponse à la plainte collective de Lupanda (cas 25.2), puis appliquez le prompt 25.1 à votre propre version.

**Exercice 25.3 (autonome).** Préparez le dossier d'une réunion de consultation sur un projet de votre site (cas 25.3).

### G. Livrable professionnel

**Dossier du comité local de suivi** : tableau de bord des plaintes, état du cahier des charges, réponses validées aux plaintes collectives, ordre du jour, dossier d'information en langage simple.

### H. Vérification des résultats

::: controle
- Aucun engagement n'apparaît sans décision validée de la direction.
- Les données personnelles sont minimisées et protégées.
- Les traductions sont réalisées ou vérifiées par des personnes qualifiées.
- Les statistiques du registre sont recontrôlées.
- Les comptes rendus ont été validés avec les représentants des communautés.
:::

::: setrompe
Dans un projet de réponse, Claude écrit « l'entreprise s'engage à installer des ralentisseurs dans les meilleurs délais », extrapolé d'une simple discussion interne mentionnée dans les notes. **Contre-mesure** : fournir la liste des seules mesures **décidées** et la règle « aucun engagement non listé ».
:::

### I. Limites et précautions

- Claude ne remplace ni la présence sur le terrain, ni l'écoute, ni la négociation.
- Les traductions automatiques en langues locales peuvent être imprécises : elles doivent être faites ou vérifiées par des locuteurs qualifiés.
- Toute communication externe suit le circuit de validation de l'entreprise.

### J. Boîte à outils

- Prompts des cas 25.1, 25.2 et prompt 25.1.
- Règle d'or : « faits vérifiés, mesures décidées, ton respectueux, aucune promesse non autorisée ».
- Modèle de compte rendu de consultation : participants, questions, réponses données, engagements, points en suspens, prochaine réunion.

### K. Quiz

1. **(Vrai ou faux)** Claude peut négocier directement avec un comité de village par messagerie.
2. **(Application)** Dans les données d'exercice, quel village a déposé le plus de plaintes ?
3. **(Compréhension)** Pourquoi la médiane est-elle utile en plus de la moyenne pour les délais de traitement ?
4. **(QCM)** Quelle norme de la SFI exige un mécanisme de gestion des plaintes ? a) aucune ; b) les Normes de performance (notamment NP1) ; c) une norme comptable ; d) la GISTM uniquement.
5. **(Mise en situation)** Claude a ajouté « nous ferons tout notre possible pour indemniser les familles ». Pourquoi est-ce problématique ?
6. **(Vrai ou faux)** Il faut pseudonymiser les plaintes avant tout traitement non indispensable.
7. **(Compréhension)** Pourquoi ne pas demander à Claude de traduire directement en langue locale un courrier officiel ?
8. **(Application)** Quel pourcentage des plaintes du registre est escaladé ?
9. **(Analyse critique)** En quoi un excellent courrier ne suffit-il pas à résoudre une crise de confiance ?
10. **(Compréhension)** Quelles rubriques doit contenir un compte rendu de consultation ?

<div class="carnet" titre="Chapitre 25 — Claude appliqué aux relations communautaires et à la performance sociale"></div>
