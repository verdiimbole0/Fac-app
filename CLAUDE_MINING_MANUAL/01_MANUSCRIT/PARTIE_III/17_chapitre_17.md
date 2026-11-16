## Chapitre 17 — Claude appliqué à la géologie et à l'exploration minière

### A. Mise en situation professionnelle

Patrick Ilunga, géologue principal de MCC, prépare la campagne d'exploration 2027 de l'extension « Mbiyo Profond ». Sur son bureau : dix ans de rapports internes, 412 journaux de sondage, des centaines de photos de carottes, des notes de terrain manuscrites numérisées, deux rapports de consultants et une pile d'articles sur les gisements stratiformes du Copperbelt. Il doit produire en trois semaines une note de synthèse, une proposition de programme de sondages et un budget. Le temps manque, non pour réfléchir, mais pour **retrouver, lire et mettre en forme** l'information.

![Figure 17.1 — Foreuse d'exploration en opération au lever du jour. Photographie : ExplorationGeologist, « Where the Earth Meets the Sky », Wikimedia Commons, licence CC BY 4.0, https://commons.wikimedia.org/wiki/File:Where_the_Earth_Meets_the_Sky.jpg (consulté le 16/11/2026). Photographie d'illustration ; elle ne représente pas le site fictif de MCC.](02_ILLUSTRATIONS/PHOTOGRAPHIES/photo_foreuse_exploration.jpg){width=80%}

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Identifier** les tâches documentaires de la géologie d'exploration qui peuvent être assistées par Claude.
2. **Faire synthétiser** un corpus de rapports d'exploration avec traçabilité des sources.
3. **Structurer** des descriptions de sondages et des notes de terrain en tableaux exploitables.
4. **Préparer** une proposition de programme d'exploration et son argumentaire.
5. **Reconnaître** les limites de Claude en interprétation géologique.

### C. Comprendre avant de pratiquer — Profil du métier

*Tableau 17.1 — Profil du géologue d'exploration.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Découvrir et caractériser des minéralisations ; concevoir et superviser les campagnes ; interpréter la géologie ; contribuer à l'estimation des ressources |
| Tâches quotidiennes | Cartographie, description des carottes (*logging*), supervision des foreuses, échantillonnage, saisie et validation des données, interprétation, rédaction |
| Difficultés récurrentes | Volume de données hétérogènes ; historique dispersé ; délais courts ; rapports chronophages ; transfert de connaissances lors des rotations |
| Documents manipulés | Journaux de sondage, certificats d'analyse, cartes, sections, rapports internes et de consultants, publications scientifiques, permis |
| Données exploitées | Collets et orientations des sondages, analyses chimiques, lithologies, structures, densités, photos de carottes, géophysique |
| Livrables | Rapports d'exploration trimestriels et annuels, programmes de sondages, budgets, notes techniques, contributions aux rapports de ressources |
| Tâches assistables par Claude | Synthèse documentaire ; structuration des notes et des logs ; contrôles de cohérence des bases ; premiers jets de rapports ; préparation de programmes et de budgets ; vulgarisation pour la direction |
| Limites | Interprétation géologique et modélisation 3D (logiciels spécialisés et jugement du géologue) ; observations de terrain ; choix des cibles ; attestation des résultats |

::: retenir
En géologie, Claude est un **assistant documentaire et analytique**, pas un géologue. Il accélère la lecture, la structuration et la rédaction ; il ne remplace ni l'observation des carottes, ni la modélisation, ni le jugement sur les cibles.
:::

![Figure 17.2 — Exploration : du terrain au rapport. Les étapes d'observation, d'interprétation et de signature restent humaines. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig17_2_workflow_exploration.png){width=100%}

### D. Démonstration guidée — Cas d'usage

#### Cas d'usage 17.1 — Synthèse d'un corpus de rapports historiques

**1. Problème professionnel.** Patrick doit connaître, en quelques jours, tout ce qui a été écrit sur la zone « Mbiyo Profond » dans 24 rapports internes et de consultants (2015-2025), soit environ 1 800 pages.

**2. Méthode habituelle.** Lecture en diagonale des résumés, recherche par mots-clés, notes manuscrites ; risque d'oublier des informations enfouies dans les annexes.

**3. Contribution de Claude.** Lecture systématique de chaque rapport, extraction structurée (résultats, interprétations, recommandations, questions ouvertes) avec citations et pages, puis synthèse transversale.

**4. Données nécessaires.** Les rapports en PDF (classification « confidentiel » à MCC : usage autorisé uniquement dans l'espace d'entreprise), une liste des sondages de la zone.

**5. Procédure.**
1. Créer un projet « Exploration Mbiyo Profond » ; y déposer les rapports (au besoin découpés pour respecter les limites de taille).
2. Pour chaque rapport, lancer l'extraction structurée (prompt 17.1) dans une conversation du projet.
3. Compiler les fiches ; vérifier un échantillon de citations.
4. Demander la synthèse transversale (prompt 17.2).
5. Relire, corriger, compléter avec les connaissances de terrain.

**6. Prompt.**

```text
Projet : exploration de l'extension « Mbiyo Profond » (gisement stratiforme Cu-Co).
Document : [titre du rapport, auteur, année] (joint).

Extrais une fiche structurée :
1. Objet et période des travaux.
2. Travaux réalisés (type, nombre, métrage de sondages, analyses).
3. Principaux résultats (intersections, teneurs) — avec page et citation exacte.
4. Interprétations géologiques proposées par les auteurs (marquées comme interprétations).
5. Recommandations des auteurs.
6. Limites, incertitudes ou problèmes de données signalés par les auteurs.
7. Éléments en contradiction apparente avec d'autres informations du document.
Règles : n'utilise que ce document ; n'ajoute aucune interprétation personnelle ;
écris « non mentionné » si une rubrique est vide.
```

**7. Échanges successifs.** Patrick demande ensuite : « Liste les sondages cités dans ce rapport qui ne figurent pas dans la liste jointe » (contrôle de cohérence de la base) ; puis, après les 24 fiches : « Quelles recommandations ont été répétées dans plusieurs rapports sans avoir été mises en œuvre ? »

**8. Exemple de résultat (extrait, fictif).**

| Rapport | Résultat clé (citation, page) | Recommandation |
|---|---|---|
| Consultant A, 2018 | « MBS-012 a intersecté 14 m à 3,1 % Cu sous la zone oxydée » (p. 47) | Tester l'extension en profondeur vers le sud-est |
| Interne, 2021 | « La transition oxydé/sulfuré se situe entre 90 et 120 m » (p. 12) | Densités à mesurer sur les sulfures |
| Interne, 2024 | « Aucune mesure de densité sur sulfures à ce jour » (p. 8) | Idem 2021 (non mise en œuvre) |

**9. Contrôle qualité.** Vérification de 20 % des citations dans les PDF ; contrôle de toutes les teneurs reprises dans la note finale ; relecture des interprétations par un second géologue.

**10. Erreurs possibles.** Confusion entre deux sondages au nom proche (MBS-012 / MBS-021) ; teneur de la mauvaise colonne d'un tableau ; interprétation d'un auteur présentée comme un fait.

**11. Limites et précautions.** Les rapports anciens scannés peuvent être mal lus ; les figures des rapports de plus de 100 pages ne sont pas analysées (découper) ; Claude ne juge pas la qualité géologique d'une interprétation.

**12. Livrable final.** Note de synthèse historique (10 pages) avec tableau des fiches en annexe, chaque information sourcée par rapport et page, validée par Patrick.

#### Cas d'usage 17.2 — Structurer des descriptions de sondages

**1. Problème.** Les géologues de terrain rédigent leurs descriptions de carottes en texte libre, de style variable ; la base de données exige des codes normalisés (lithologie, altération, minéralisation, structure).

**2. Méthode habituelle.** Recodage manuel par un géologue junior, long et source d'erreurs.

**3. Contribution de Claude.** Conversion des descriptions libres en enregistrements codés selon le dictionnaire de codes de MCC, avec signalement des descriptions ambiguës.

**4. Données.** Descriptions textuelles ; dictionnaire de codes (lithologies RAT, CMN, RSF, RSC, SD… du scénario) ; exemples déjà codés.

**5. Procédure.** Fournir le dictionnaire et 5 exemples codés ; traiter les descriptions par lots de 50 ; contrôler un échantillon ; importer après validation.

**6. Prompt.**

```text
Tu codes des descriptions de carottes selon le dictionnaire de MCC ci-dessous.
<dictionnaire> [codes et définitions] </dictionnaire>
<exemples> [5 descriptions avec leur codage validé] </exemples>
<descriptions> [lot de descriptions : sondage ; de ; à ; texte] </descriptions>
Sortie : tableau sondage | de | a | litho | alteration | mineralisation | structure | confiance | remarque.
Règles : utilise uniquement les codes du dictionnaire ; si la description ne permet pas
de choisir, mets « ? » et confiance « basse » ; ne modifie jamais les profondeurs.
```

**7. Échanges.** « Liste les descriptions où la minéralisation décrite (par exemple malachite abondante) semble incohérente avec la lithologie codée. »

**8. Exemple de résultat.** Sur 50 descriptions (fictives), 44 codées avec confiance haute, 6 signalées pour revue (termes locaux non définis dans le dictionnaire).

**9. Contrôle qualité.** Double codage humain de 10 % du lot ; écarts analysés et dictionnaire enrichi.

**10. Erreurs possibles.** Synonymes mal interprétés ; profondeurs recopiées avec erreur (d'où la règle de ne pas les modifier et l'import par jointure sur les identifiants).

**11. Limites.** Le codage reste une **proposition** ; la responsabilité de la base revient au géologue responsable des données.

**12. Livrable.** Fichier codé validé, prêt à l'import, avec journal des corrections.

#### Cas d'usage 17.3 — Préparer un programme d'exploration (version condensée)

Patrick fournit la synthèse historique, les objectifs de la direction et les coûts unitaires (forage, analyses, logistique). Claude propose une **structure de programme** (objectifs, phases, nombre et métrage de sondages par phase, critères de passage d'une phase à l'autre, budget, risques), **calcule le budget par programme** à partir des coûts unitaires et rédige l'argumentaire. Les cibles, l'implantation et les métrages sont **décidés par Patrick** ; Claude n'en propose que si on lui fournit les critères, et ses propositions sont discutées comme des hypothèses. Contrôle : recalcul du budget, cohérence entre texte et tableaux, revue par la direction technique.

#### Cas d'usage 17.4 — Vulgariser pour la direction et les communautés (version condensée)

Claude transforme une note technique en résumé pour le comité de direction (enjeux, coûts, décisions attendues) et en fiche d'information pour les communautés riveraines (où, quand, quels travaux, quelles nuisances, qui contacter), en français simple, à faire valider par le responsable des relations communautaires. Règle : aucune information sur des teneurs ou des ressources dans les communications externes sans validation de la direction (informations potentiellement sensibles).

### E. Prompts commentés

**Prompt 17.2 — Synthèse transversale**

```text
Voici les 24 fiches d'extraction (une par rapport) : <fiches> … </fiches>
Rédige une synthèse transversale :
1. Chronologie des travaux.
2. Ce qui est établi (résultats répétés et cohérents, avec références aux fiches).
3. Ce qui est incertain ou contradictoire.
4. Les recommandations répétées et leur état de mise en œuvre.
5. Les lacunes de données à combler avant la campagne 2027.
Distingue systématiquement faits, interprétations des auteurs et questions ouvertes.
```

*Commentaire.* La synthèse ne travaille que sur les fiches déjà contrôlées : on limite ainsi la propagation d'erreurs.

**Prompt 17.3 — Analyse d'une photo de carotte**

```text
Photo jointe : caisse de carottes du sondage [ID], de [x] à [y] m, éclairage naturel,
mire de couleur présente. Décris les variations visibles (couleur, texture, veines,
fractures) intervalle par intervalle, en distinguant observations et hypothèses.
Ne propose ni lithologie définitive, ni teneur. Liste ce qu'un géologue devrait vérifier sur la carotte réelle.
```

### F. Exercices pratiques

**Exercice 17.1 (guidé).** Avec `MCC_sondages_collets.csv` et `MCC_sondages_analyses.csv`, demandez à Claude (exécution de code) : (a) le métrage total foré par fosse ; (b) la liste des sondages dont la profondeur déclarée ne correspond pas à la dernière passe analysée ; (c) les meilleures intersections au-dessus de 1,5 % Cu sur au moins 6 m (calcul pondéré). Vérifiez un résultat à la main.

**Exercice 17.2 (guidé).** Rédigez cinq descriptions de carottes « à la manière d'un géologue de terrain » et un mini-dictionnaire de codes ; testez le cas d'usage 17.2.

**Exercice 17.3 (autonome).** À partir d'un rapport d'exploration public (par exemple un rapport technique déposé par une société cotée), produisez une fiche d'extraction complète et vérifiez toutes les citations.

### G. Livrable professionnel

**Note de synthèse d'exploration** comprenant : synthèse historique sourcée, état des données, lacunes, proposition de programme (décidée par le géologue), budget recalculé, résumé pour la direction.

### H. Vérification des résultats

::: controle
- Toutes les teneurs et intersections citées ont été vérifiées dans la base de données ou le certificat d'analyse.
- Les calculs d'intersections pondérées ont été réalisés par programme et recontrôlés.
- Faits, interprétations des auteurs et hypothèses sont clairement distingués.
- Aucune information sensible (teneurs, ressources) n'est diffusée hors du cercle autorisé.
:::

::: setrompe
Interrogé sur « la géologie du Copperbelt congolais », un assistant d'IA peut produire une synthèse très convaincante mêlant des noms de formations, des âges et des auteurs, dont certains inexacts. Pour toute information géologique régionale citée dans un rapport, revenez aux publications et aux cartes géologiques de référence.
:::

### I. Limites et précautions

- Claude ne remplace ni les logiciels de modélisation géologique, ni la géostatistique, ni l'observation des carottes.
- Les résultats d'exploration d'une société cotée peuvent être des **informations privilégiées** : respectez strictement les règles de confidentialité et de communication.
- Les photos de carottes ne permettent pas d'estimer une teneur.

### J. Boîte à outils

- Prompt 17.1 — fiche d'extraction de rapport ; prompt 17.2 — synthèse transversale ; prompt 17.3 — photo de carotte.
- Check-list « avant de transmettre une note d'exploration » : sources vérifiées ; calculs recontrôlés ; validation du géologue principal ; classification respectée.
- Modèle de fiche d'extraction (Annexe D).

### K. Quiz

1. **(QCM)** Quel rôle Claude joue-t-il le plus utilement en exploration ? a) choisir les cibles de forage ; b) assistant documentaire et analytique ; c) remplacer le logiciel de modélisation ; d) estimer les teneurs à partir de photos.
2. **(Vrai ou faux)** Une interprétation géologique proposée par un auteur peut être présentée comme un fait dans la synthèse.
3. **(Compréhension)** Pourquoi faut-il interdire à Claude de modifier les profondeurs lors du codage des descriptions ?
4. **(Application)** Calculez la teneur pondérée de trois passes : 2 m à 3,0 % ; 1 m à 1,0 % ; 3 m à 2,0 %.
5. **(Mise en situation)** Claude confond MBS-012 et MBS-021. Quel contrôle aurait détecté l'erreur ?
6. **(Vrai ou faux)** Les résultats d'exploration d'une société cotée peuvent être des informations privilégiées.
7. **(QCM)** Pour qu'un rapport de 300 pages soit analysé y compris ses figures, il faut : a) le joindre tel quel ; b) le découper en documents de 100 pages ou moins ; c) le convertir en Word ; d) c'est impossible.
8. **(Analyse critique)** Quels risques présente une fiche d'information aux communautés rédigée par Claude sans validation ?
9. **(Compréhension)** Citez trois livrables typiques du géologue d'exploration.
10. **(Application)** Rédigez la règle qui distingue faits et interprétations dans un prompt de synthèse.

<div class="carnet" titre="Chapitre 17 — Claude appliqué à la géologie et à l'exploration minière"></div>
