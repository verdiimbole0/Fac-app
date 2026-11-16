## Chapitre 21 — Claude appliqué au traitement des minerais et à la métallurgie

### A. Mise en situation professionnelle

Jean-Luc Tshibangu, métallurgiste en chef de MCC, fait face à deux problèmes. Le poste « réactifs » de l'usine dépasse le budget de plus de 20 % depuis avril 2026, et le directeur financier attend une explication chiffrée. Par ailleurs, la procédure opératoire de l'électrolyse doit être mise à jour avant l'audit de certification, car l'usine a modifié ses équipements de ventilation. Jean-Luc a les données, les contrats, les anciennes procédures ; il lui manque le temps de tout croiser et rédiger.

![Figure 21.1 — Salle d'électrolyse du cuivre (raffinerie de Luilu, près de Kolwezi, photographie historique). Titre original : « Room where copper is electrolyzed at the Gecamines Luilu refinery near Kolwezi ». Auteur : Gécamines. Source : Wikimedia Commons, [https://commons.wikimedia.org/wiki/File:Room_where_copper_is_electrolyzed_at_the_Gecamines_Luilu_refinery_near_Kolwezi.jpg](https://commons.wikimedia.org/wiki/File:Room_where_copper_is_electrolyzed_at_the_Gecamines_Luilu_refinery_near_Kolwezi.jpg) (consulté le 16/11/2026). Licence : domaine public. Photographie d'illustration, sans lien avec l'entreprise fictive MCC.](02_ILLUSTRATIONS/PHOTOGRAPHIES/photo_electrolyse_luilu.jpg){width=78%}

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Produire** un bilan métallurgique mensuel vérifié, avec détection des anomalies de données.
2. **Expliquer** un écart de coût de réactifs en séparant effet prix et effet consommation.
3. **Rédiger ou actualiser** une procédure opératoire avec l'aide de Claude, en garantissant la validation technique et HSE.
4. **Structurer** une démarche de diagnostic d'une baisse de performance sans déléguer les conclusions.
5. **Exploiter** les rapports de laboratoire de façon traçable.

### C. Comprendre avant de pratiquer — Profil du métier

![Figure 21.2 — Schéma de traitement simplifié de l'usine de MCC (fictif) : lixiviation acide, décantation à contre-courant, extraction par solvant et électrolyse pour le cuivre ; précipitation du cobalt. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig21_2_schema_usine.png){width=100%}

*Tableau 21.1 — Profil du métallurgiste et de l'équipe de l'usine.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Performance de l'usine (débit, récupération, qualité), consommation de réactifs et d'énergie, sécurité des procédés, procédures |
| Tâches quotidiennes | Suivi des paramètres, essais, bilans matière, échanges avec le laboratoire, la mine et la maintenance, rapports |
| Difficultés | Variabilité du minerai ; données de laboratoire nombreuses ; coûts des réactifs ; procédures à tenir à jour ; transfert de savoir-faire |
| Documents | Bilans métallurgiques, rapports de laboratoire, procédures opératoires, fiches de données de sécurité, contrats de réactifs, rapports d'essais |
| Données | Débits, teneurs d'alimentation et de résidus, récupérations, consommations (acide, chaux, extractant, énergie), qualité des cathodes |
| Livrables | Bilans journaliers et mensuels, rapports de performance, procédures, analyses d'écarts, rapports d'essais |
| Assistables par Claude | Bilans et graphiques par code ; analyse des écarts de coût ; rédaction et révision de procédures ; structuration de diagnostics ; synthèses de rapports d'essais |
| Limites | Pilotage du procédé ; modifications des paramètres ; sécurité des procédés chimiques (acide, solvants, hydrogène sulfuré éventuel, brouillard acide en électrolyse) : décisions humaines et procédures validées |

### D. Démonstration guidée — Cas d'usage

#### Cas d'usage 21.1 — Bilan métallurgique mensuel avec contrôle des données

**1. Problème.** Le bilan mensuel est construit à partir des données journalières ; des erreurs de saisie faussent les moyennes.

**2. Méthode habituelle.** Tableur alimenté manuellement ; contrôles visuels.

**3. Contribution de Claude.** Profil des données, détection des valeurs physiquement impossibles, calcul des moyennes pondérées, graphiques, commentaire.

**4. Données.** `MCC_production_journaliere_S1_2026.xlsx`.

**5–6. Procédure et prompt.**

```text
Avec l'exécution de code, à partir du fichier joint :
1. Signale les valeurs impossibles ou suspectes (récupération > 100 %, cathode incohérente
   avec traité × teneur × récupération à plus de 5 %, journées manquantes).
2. Pour chaque mois, calcule : minerai traité (somme), teneur moyenne pondérée par le tonnage,
   récupération globale = cathode totale / (Σ traité × teneur), cathode totale.
3. Produis un graphique de la récupération journalière.
4. Rédige un commentaire de 150 mots.
Les valeurs signalées au point 1 sont exclues des calculs ET listées en annexe ;
indique l'effet de leur exclusion sur chaque indicateur.
```

**7. Échanges.** « La récupération baisse-t-elle les jours où la teneur d'alimentation est plus élevée ? Présente la relation et précise ses limites. »

**8. Exemple de résultat.** Détection de la récupération de 121,4 % (15 février) et de la production de cathode ×10 (1er juin) ; effet de leur exclusion chiffré.

![Figure 21.3 — Récupération journalière du cuivre au premier semestre 2026 : une valeur impossible signale une erreur de saisie à corriger à la source. Données fictives MCC. Graphique réalisé pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig21_3_recuperation_journaliere.png){width=92%}

**9. Contrôle.** Retour aux relevés de l'usine pour les valeurs exclues ; vérification d'une moyenne pondérée à la main.

**10. Erreurs possibles.** Moyenne simple des récupérations journalières au lieu de la récupération globale ; exclusion silencieuse de données.

**11. Limites.** Le bilan officiel est validé par le métallurgiste ; les corrections se font dans le système source.

**12. Livrable.** Bilan métallurgique mensuel validé, avec annexe des anomalies.

#### Cas d'usage 21.2 — Expliquer le dépassement du budget des réactifs

**1. Problème.** Le centre de coût « Usine – réactifs » dépasse son budget de 18 à 26 % d'avril à juin 2026.

**2. Méthode habituelle.** Recherche manuelle dans les factures, explication souvent limitée à « hausse des prix ».

**3. Contribution de Claude.** Décomposition de l'écart en **effet prix** et **effet consommation** pour chaque réactif, à partir des données fournies ; lecture du contrat pour vérifier la formule de révision du prix.

**4. Données.** `MCC_budget_reel_S1_2026.xlsx` (onglets « Budget vs réel » et « Hypothèses ») ; contrat de fourniture d'acide (extrait) ; rapport mensuel de mars (consommation d'acide de 31,5 kg/t contre 30 au budget).

**5–6. Procédure et prompt.**

```text
[C] Je suis métallurgiste en chef de MCC ; le directeur financier me demande d'expliquer
le dépassement du budget des réactifs d'avril à juin 2026.
[A] Décompose l'écart du poste acide sulfurique en effet prix et effet consommation,
puis compare-le à l'écart total du centre de coût « Usine – réactifs ».
[D] Fichier MCC_budget_reel_S1_2026.xlsx ; hypothèses : prix budget 185 USD/t, prix réel
avril-juin 228 USD/t, consommation budget 30 kg/t, consommation réelle 31,5 kg/t,
minerai traité 200 kt/mois. Contrat d'acide joint (article 5 : révision trimestrielle plafonnée à ±15 %).
[R] Calculs par exécution de code, formules affichées. Vérifie si la hausse de prix respecte
le plafond contractuel. N'attribue pas le reste de l'écart à une cause non documentée.
[E] Tableau mensuel ; part de l'écart total expliquée par l'acide ; questions à instruire pour le reste.
```

**7. Échanges.** « Prépare la question au service achats sur l'application de l'article 5 » ; « Quelles données faudrait-il pour expliquer le reste de l'écart (extractant, floculant, chaux) ? »

**8. Exemple de résultat (calcul du scénario fictif).**

| Élément (par mois, avril-juin) | Calcul | Montant |
|---|---|---|
| Consommation budget | 200 000 t × 30 kg/t | 6 000 t |
| Coût budget acide | 6 000 t × 185 USD | 1 110 000 USD |
| Effet prix | 6 000 t × (228 − 185) | + 258 000 USD |
| Effet consommation | 300 t × 228 | + 68 400 USD |
| Écart acide total | | ≈ + 0,33 MUSD |
| Écart total du centre de coût (données) | ≈ + 0,9 à + 1,3 MUSD | |

**Constat clé :** l'acide n'explique qu'environ un quart à un tiers de l'écart. Par ailleurs, la hausse de prix de 185 à 228 USD/t représente + 23 %, **au-delà du plafond de révision de 15 % par trimestre** prévu à l'article 5 du contrat : une question à instruire avec les achats et le juridique.

**9. Contrôle.** Recalcul indépendant ; vérification des prix sur les factures ; lecture de l'article 5 par le juriste.

**10. Erreurs possibles.** Attribuer tout l'écart à l'acide ; ignorer le plafond contractuel ; confondre kg/t et t/t.

**11. Limites.** L'interprétation contractuelle relève du service juridique.

**12. Livrable.** Note d'explication des écarts (1 page), avec les questions ouvertes.

#### Cas d'usage 21.3 — Actualiser une procédure opératoire (condensé)

À partir de l'ancienne procédure de l'électrolyse, de la description des nouveaux équipements de ventilation et des fiches de données de sécurité, Claude produit une version révisée **en mode révision** : chaque modification est signalée et justifiée, chaque information nouvelle est rattachée à un document fourni, et les points à confirmer sont marqués. La procédure est ensuite revue par le métallurgiste, le responsable HSE et la maintenance, puis approuvée selon le système documentaire. Claude ne crée **aucune** valeur limite d'exposition, consigne d'équipement de protection ou étape de consignation qui ne figure pas dans un document de référence.

#### Cas d'usage 21.4 — Structurer un diagnostic de baisse de récupération (condensé)

Lorsque la récupération baisse, Claude aide à **organiser** le diagnostic : arbre des causes possibles (minéralogie, granulométrie, conditions de lixiviation, pertes en CCD, extraction par solvant…), données à collecter pour chaque hypothèse, tests à réaliser, responsables. Il ne conclut pas : les essais et le jugement de l'équipe tranchent.

### E. Prompts commentés

**Prompt 21.1 — Arbre de diagnostic**

```text
La récupération du cuivre de notre usine (lixiviation acide, CCD, SX-EW) est passée
de 88 % à 85 % sur deux semaines. Construis un arbre de diagnostic : pour chaque étape
du procédé, les causes possibles, la donnée ou l'analyse qui permettrait de confirmer
ou d'écarter chaque cause, et le service concerné.
Ne classe pas les causes par probabilité : nous ne t'avons pas fourni de données.
Termine par la liste des 10 premières vérifications à faire, de la plus simple à la plus coûteuse.
```

*Commentaire.* La consigne de ne pas classer par probabilité est honnête : sans données, tout classement serait une supposition présentée comme une analyse.

### F. Exercices pratiques

**Exercice 21.1 (guidé).** Réalisez le cas 21.1 avec le fichier d'exercice ; vérifiez la récupération globale de mars par un calcul indépendant.

**Exercice 21.2 (guidé).** Réalisez le cas 21.2. Retrouvez-vous l'effet prix de 258 000 USD par mois ? Que concluez-vous sur l'article 5 du contrat ?

**Exercice 21.3 (autonome).** Choisissez une procédure de votre site ; demandez une révision en mode « modifications signalées » et listez les validations nécessaires.

### G. Livrable professionnel

**Dossier mensuel de performance de l'usine** : bilan métallurgique validé, explication des écarts de coûts, suivi des actions, procédures mises à jour avec leur circuit de validation.

### H. Vérification des résultats

::: controle
- Les récupérations globales sont calculées à partir des totaux, pas en moyenne de pourcentages.
- Chaque écart de coût est décomposé et la somme des effets est contrôlée.
- Les éléments contractuels ont été lus dans le contrat (article cité).
- Toute modification de procédure est tracée et validée par les fonctions compétentes.
:::

::: setrompe
Claude rédige une procédure révisée très propre… dans laquelle il a ajouté une « limite d'exposition au brouillard acide » chiffrée, absente des documents fournis. **Contre-mesure** : exiger que toute valeur numérique de sécurité soit rattachée à un document de référence, sinon marquée « à confirmer par le HSE ».
:::

### I. Limites et précautions

- Claude ne pilote pas le procédé et ne modifie aucun paramètre de conduite.
- Les procédures de sécurité des procédés chimiques sont validées par les experts et le HSE.
- Les données de performance de l'usine sont confidentielles.

### J. Boîte à outils

- Formules : récupération globale = métal récupéré / métal alimenté ; écart de coût = effet prix + effet consommation.
- Prompts des cas 21.1, 21.2 et prompt 21.1.
- Check-list de révision de procédure : modifications tracées ; sources citées ; valeurs de sécurité vérifiées ; validations HSE, maintenance, métallurgie ; formation des opérateurs.

### K. Quiz

1. **(Calcul)** Avec 6 000 t d'acide par mois et une hausse de prix de 43 USD/t, quel est l'effet prix mensuel ?
2. **(Vrai ou faux)** La récupération mensuelle est la moyenne des récupérations journalières.
3. **(Compréhension)** Pourquoi la hausse de 185 à 228 USD/t pose-t-elle question au regard de l'article 5 du contrat ?
4. **(QCM)** Qui valide une procédure opératoire révisée ? a) Claude ; b) les fonctions compétentes (métallurgie, HSE, maintenance) selon le système documentaire ; c) le fournisseur ; d) personne.
5. **(Mise en situation)** Claude conclut que « la baisse de récupération est due à la granulométrie ». Que faites-vous ?
6. **(Calcul)** Quel est l'effet consommation mensuel si la consommation passe de 30 à 31,5 kg/t sur 200 kt, au prix de 228 USD/t ?
7. **(Vrai ou faux)** Claude peut ajouter une limite d'exposition chiffrée dans une procédure si elle lui paraît plausible.
8. **(Compréhension)** Pourquoi faut-il chiffrer l'effet de l'exclusion des valeurs aberrantes ?
9. **(Analyse critique)** Pourquoi est-il honnête de ne pas classer les causes par probabilité sans données ?
10. **(Application)** Quelle part approximative de l'écart des réactifs l'acide explique-t-il dans le scénario ?

<div class="carnet" titre="Chapitre 21 — Claude appliqué au traitement des minerais et à la métallurgie"></div>
