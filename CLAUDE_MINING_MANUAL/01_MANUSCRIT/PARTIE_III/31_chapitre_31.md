## Chapitre 31 — Claude appliqué au management, à l'administration, à la gouvernance et au reporting

### A. Mise en situation professionnelle

Aline Mujinga, directrice générale de MCC, reçoit chaque mois une quarantaine de rapports : production, usine, maintenance, HSE, environnement, communautés, finance, achats, RH. Elle doit en extraire l'essentiel pour le comité de direction, préparer le rapport trimestriel au conseil d'administration, suivre les décisions et piloter le programme « MCC-IA 2026 ». Son temps est la ressource la plus rare de l'entreprise. Elle veut que Claude l'aide à **voir plus vite et plus juste**, sans jamais déléguer son jugement.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Consolider** plusieurs rapports en une synthèse de direction fiable et traçable.
2. **Préparer** un comité ou un conseil : ordre du jour, dossier, notes de décision, comptes rendus.
3. **Suivre** les décisions et les actions avec un registre structuré.
4. **Préparer** des communications internes claires.
5. **Piloter** un programme de transformation (comme l'adoption de l'IA) avec des indicateurs pertinents.

### C. Comprendre avant de pratiquer — Profil du métier

*Tableau 31.1 — Profil des managers et de l'administration de direction.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Stratégie, performance, arbitrages, conformité, relations avec les actionnaires, l'État et les parties prenantes |
| Tâches quotidiennes | Lecture de rapports, réunions, décisions, communication, représentation |
| Difficultés | Surcharge d'information ; informations contradictoires entre services ; suivi des décisions ; temps |
| Documents | Rapports mensuels, tableaux de bord, notes de décision, procès-verbaux, rapports au conseil, plans stratégiques |
| Données | Indicateurs consolidés (production, coûts, sécurité, environnement, social, finances) |
| Livrables | Synthèses, décisions, comptes rendus, rapports au conseil, communications |
| Assistables par Claude | Synthèses multi-rapports ; notes de décision ; ordres du jour ; comptes rendus ; registre des décisions ; communications ; préparation des questions |
| Limites | Décisions, arbitrages, engagements, communications sensibles (marchés, autorités, crises) |

![Figure 31.1 — Du terrain au conseil : la chaîne de reporting assistée. Les arbitrages et décisions restent ceux de la direction et du conseil. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig31_1_reporting_direction.png){width=100%}

### D. Démonstration guidée — Cas d'usage

#### Cas d'usage 31.1 — Synthèse mensuelle de direction

**1. Problème.** Quarante rapports, deux heures de lecture disponibles.

**2. Méthode habituelle.** Lecture des résumés, appels aux directeurs, synthèse rédigée par l'assistante de direction.

**3. Contribution de Claude.** Lecture de tous les rapports (dans un projet « Direction — reporting mensuel »), extraction des faits marquants avec sources, détection des incohérences entre rapports, synthèse d'une page, liste des décisions à prendre.

**4. Données.** Rapports mensuels validés des services (classification « usage interne » ou « confidentiel » selon le cas, dans l'environnement d'entreprise).

**5–6. Procédure et prompt.**

```text
[C] Directrice générale de MCC ; comité de direction mardi.
[A] Prépare la synthèse mensuelle de direction à partir des rapports joints.
[D] Rapports de [mois] : production, usine, maintenance, HSE, environnement, communautés,
finance, achats, RH (joints, validés par les services).
[R] Chaque fait cité renvoie au rapport source (nom du rapport). Ne retiens que les éléments
significatifs (seuils : écart > 5 % au budget, tout événement HSE grave, toute alerte environnementale,
toute plainte escaladée). Signale les incohérences de chiffres entre rapports, sans trancher.
[E] 1 page : 5 faits marquants ; 3 risques ; tableau des indicateurs clés (réel, budget, écart) ;
décisions à prendre (avec le service concerné) ; incohérences à résoudre avant le comité.
```

**7. Échanges successifs.** « Pour chaque décision à prendre, prépare une note de décision d'une demi-page (contexte, options, avantages et inconvénients, recommandation du service) » ; « Quelles questions les administrateurs poseront-ils sur ce mois ? »

**8. Exemple de résultat (extrait, fictif).** Faits marquants : minerai traité inférieur au budget (saison des pluies) ; dépassement des réactifs ; dépassement ponctuel au point de rejet ST-02 en mars ; presque-accident sur la rampe R3 ; délais de traitement des plaintes au-delà de l'objectif. Incohérence relevée : le rapport de production annonce 189 kt traitées en mars, la somme des données journalières transmise par l'usine donne environ 186,5 kt — à réconcilier.

**9. Contrôle.** L'assistante de direction vérifie chaque chiffre de la synthèse dans les rapports sources ; les incohérences sont renvoyées aux services.

**10. Erreurs possibles.** Chiffre d'un mois précédent ; omission d'un événement grave mentionné en annexe d'un rapport.

**11. Limites.** La hiérarchisation finale des sujets et les décisions appartiennent à la direction.

**12. Livrable.** Synthèse mensuelle de direction validée, notes de décision.

#### Cas d'usage 31.2 — Compte rendu et registre des décisions

**1. Problème.** Les décisions du comité sont mal tracées ; les actions se perdent.

**2. Méthode habituelle.** Compte rendu rédigé plusieurs jours après, sans registre consolidé.

**3. Contribution de Claude.** À partir des notes de séance, projet de compte rendu (décisions, actions, responsables, échéances) et mise à jour du registre des décisions ; relances préparées.

**4. Données.** Notes de séance (ou transcription si l'enregistrement est autorisé et annoncé), registre existant.

**5–6. Prompt.**

```text
À partir des notes de séance jointes, rédige le projet de compte rendu du comité de direction :
participants ; points traités ; décisions (formulées exactement comme dans les notes) ;
actions (quoi, qui, quand). Signale toute action sans responsable ou sans échéance.
Ne reformule pas une décision de manière à en changer la portée ; en cas d'ambiguïté, écris [à confirmer].
Puis mets à jour le registre des décisions joint (nouvelles lignes, statuts).
```

**7. Échanges.** « Prépare les messages de relance pour les actions échues. »

**8. Exemple de résultat.** Compte rendu d'une page ; 9 actions dont 2 sans échéance signalées.

**9. Contrôle.** Validation par le président de séance avant diffusion.

**10. Erreurs possibles.** Décision « durcie » ou « adoucie » par la reformulation ; responsable mal attribué.

**11. Limites.** L'enregistrement des réunions exige l'information des participants et le respect des règles de confidentialité.

**12. Livrable.** Compte rendu validé et registre à jour.

#### Cas d'usage 31.3 — Rapport trimestriel au conseil (condensé)

Claude assemble, à partir des synthèses mensuelles validées, le projet de rapport trimestriel : performance, risques, projets, ESG, finances, décisions demandées au conseil, avec un résumé exécutif et une présentation (artefact Slides). Les messages, les chiffres et les recommandations sont validés par la direction ; les informations susceptibles d'être privilégiées suivent les règles applicables.

#### Cas d'usage 31.4 — Piloter le programme « MCC-IA 2026 » (condensé)

Claude aide Kevin Mutombo à construire le tableau de bord du programme : utilisateurs actifs, cas d'usage déployés, temps gagné **mesuré** sur échantillons, incidents et non-conformités à la charte, formations réalisées, satisfaction. Il prépare les rapports au comité de pilotage. Les indicateurs de gains sont fondés sur des mesures avant/après, pas sur des estimations de l'outil.

### E. Prompts commentés

**Prompt 31.1 — Note de décision**

```text
Rédige une note de décision d'une demi-page pour le comité de direction sur : [sujet].
Structure : contexte (3 lignes) ; options (2 ou 3) avec coût, délai, risques, effets sur la sécurité,
l'environnement et les communautés ; position du service (citée) ; questions à trancher.
Ne recommande pas d'option toi-même ; présente-les de façon équilibrée.
```

*Commentaire.* En interdisant à Claude de recommander, on garantit une présentation équilibrée et on préserve la délibération du comité.

### F. Exercices pratiques

**Exercice 31.1 (guidé).** Avec les documents d'exercice (rapport de mars, incident, suivi de l'eau, registre des plaintes), produisez la synthèse de direction de mars 2026 (cas 31.1). Retrouvez-vous l'incohérence entre 189 kt et la somme des données journalières ?

**Exercice 31.2 (guidé).** Rédigez des notes de séance fictives d'un comité et appliquez le cas 31.2.

**Exercice 31.3 (autonome).** Concevez le tableau de bord de pilotage de l'adoption de l'IA dans votre service (cas 31.4).

### G. Livrable professionnel

**Kit de gouvernance** : modèle de synthèse mensuelle, modèle de note de décision, modèle de compte rendu, registre des décisions, tableau de bord du programme IA.

### H. Vérification des résultats

::: controle
- Chaque chiffre de la synthèse est rattaché à un rapport source validé.
- Les incohérences entre rapports sont résolues avant le comité.
- Les décisions consignées correspondent exactement à ce qui a été décidé.
- Les gains attribués à l'IA reposent sur des mesures.
:::

::: setrompe
Dans une synthèse, Claude écrit « la production de cathodes est conforme au budget » en s'appuyant sur un rapport de février resté dans le projet, alors que le rapport de mars montre un écart. **Contre-mesure** : une seule période par conversation, et règle « tout chiffre doit citer son rapport et sa période ».
:::

### I. Limites et précautions

- Les informations de direction sont souvent confidentielles ou privilégiées.
- La synthèse ne remplace pas le dialogue avec les directeurs : elle le prépare.
- Les communications de crise suivent un dispositif spécifique, piloté par la direction.

### J. Boîte à outils

- Prompts des cas 31.1, 31.2 et prompt 31.1.
- Gabarit de registre des décisions : n° | date | décision | responsable | échéance | statut | commentaire.
- Indicateurs du programme IA : adoption, cas d'usage, gains mesurés, incidents, formation.

### K. Quiz

1. **(Vrai ou faux)** Claude peut recommander une option au comité dans une note de décision équilibrée.
2. **(Compréhension)** Pourquoi exiger que chaque chiffre de la synthèse cite son rapport et sa période ?
3. **(Application)** Quelle incohérence les données d'exercice de mars 2026 révèlent-elles ?
4. **(Mise en situation)** Le compte rendu « adoucit » une décision du comité. Que faites-vous ?
5. **(QCM)** Comment mesurer les gains du programme IA ? a) estimations de Claude ; b) mesures avant/après sur échantillons ; c) enquêtes uniquement ; d) aucun besoin.
6. **(Vrai ou faux)** L'enregistrement d'une réunion nécessite l'information des participants.
7. **(Compréhension)** Citez trois rubriques d'une note de décision.
8. **(Analyse critique)** Quel risque présente une synthèse de direction non vérifiée ?
9. **(Application)** Proposez deux seuils de significativité pour une synthèse mensuelle.
10. **(Compréhension)** Pourquoi une conversation par période ?

<div class="carnet" titre="Chapitre 31 — Claude appliqué au management, à l'administration, à la gouvernance et au reporting"></div>
