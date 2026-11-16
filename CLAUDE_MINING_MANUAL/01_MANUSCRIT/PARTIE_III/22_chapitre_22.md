## Chapitre 22 — Claude appliqué à la maintenance et à la gestion des équipements

### A. Mise en situation professionnelle

Didier Mukendi, responsable maintenance de MCC, est convoqué par le directeur des opérations après l'incident de la rampe R3 : le camion CAM-07 a glissé au freinage, et la maintenance a trouvé une fuite sur un flexible du circuit de freinage. « Ce camion a eu combien d'interventions hydrauliques cette année ? Pourquoi n'a-t-on rien vu venir ? » Didier sait que la réponse est dans la GMAO — 420 ordres de travail en dix mois, avec des descriptions en texte libre de qualité variable. Il lui faut une analyse fiable, rapide, et un plan d'action argumenté.

![Figure 22.1 — Camion de transport minier en réparation dans un atelier de maintenance. Titre original : « Haul truck under repair at Brockman 4, September 2018 ». Auteur : Calistemon. Source : Wikimedia Commons, [https://commons.wikimedia.org/wiki/File:Haul_truck_under_repair_at_Brockman_4,_September_2018.jpg](https://commons.wikimedia.org/wiki/File:Haul_truck_under_repair_at_Brockman_4,_September_2018.jpg) (consulté le 16/11/2026). Licence : [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr) ; image redimensionnée pour l'édition. Photographie d'illustration, sans lien avec l'entreprise fictive MCC.](02_ILLUSTRATIONS/PHOTOGRAPHIES/photo_camion_maintenance.jpg){width=78%}

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Analyser** un historique de maintenance (Pareto, défaillances répétitives, coûts) avec calculs traçables.
2. **Exploiter** les descriptions en texte libre des ordres de travail pour classer les défaillances.
3. **Préparer** un dossier d'analyse de défaillance sans en déléguer la conclusion.
4. **Rédiger** des gammes de maintenance et des ordres de travail clairs.
5. **Articuler** Claude avec les outils existants (GMAO, maintenance prédictive).

### C. Comprendre avant de pratiquer — Profil du métier

*Tableau 22.1 — Profil du responsable et du planificateur de maintenance.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Disponibilité et fiabilité des équipements ; sécurité des interventions ; coûts ; pièces de rechange ; plans de maintenance |
| Tâches quotidiennes | Planification et ordonnancement, suivi des pannes, coordination avec la production, gestion des sous-traitants, analyses de défaillance |
| Difficultés | Données GMAO incomplètes ; descriptions libres hétérogènes ; urgence permanente ; arbitrage préventif / correctif ; savoir-faire tacite |
| Documents | Ordres de travail, historiques, manuels constructeurs, gammes, analyses de défaillance, procédures de consignation |
| Données | Heures de marche, arrêts, coûts, pièces, alarmes et mesures des capteurs, résultats d'analyses d'huile |
| Livrables | Plans de maintenance, rapports de disponibilité et de fiabilité, analyses de défaillance, budgets |
| Assistables par Claude | Analyses d'historique par code ; classement des descriptions libres ; synthèse des manuels ; rédaction des gammes et rapports ; préparation des analyses de défaillance |
| Limites | Diagnostic sur l'équipement ; décisions de remise en service ; consignation ; validation des gammes de sécurité |

::: attention
La **consignation** (mise en sécurité des énergies avant intervention) et la **remise en service** d'un équipement intéressant la sécurité (freinage, direction, systèmes de levage) relèvent de procédures strictes et de personnes habilitées. Claude peut aider à rédiger ou relire une procédure ; il ne remplace ni la procédure validée ni la vérification sur l'équipement.
:::

### D. Démonstration guidée — Cas d'usage

#### Cas d'usage 22.1 — Analyse de l'historique et Pareto des arrêts

**1. Problème.** Identifier les systèmes et équipements qui concentrent les arrêts, et les défaillances répétitives (cas du CAM-07).

**2. Méthode habituelle.** Extractions GMAO, tableaux croisés manuels, analyses ponctuelles.

**3. Contribution de Claude.** Profil des données, Pareto des heures d'arrêt par système, focus par équipement, détection des répétitions, graphiques, commentaire.

**4. Données.** `MCC_maintenance_ordres_travail.csv` (420 ordres de travail, juillet 2025 à avril 2026).

**5–6. Procédure et prompt.**

```text
Fichier joint : MCC_maintenance_ordres_travail.csv (séparateur ;, ligne 1 = bandeau).
Avec l'exécution de code :
1. Profil des données : nombre d'OT, période, valeurs aberrantes (durées négatives ou nulles, coûts nuls).
2. Pareto des heures d'arrêt en maintenance corrective par système, avec % cumulé.
3. Pour le camion CAM-07 : chronologie des interventions, regroupement par système,
   intervalle moyen entre deux interventions hydrauliques, heures d'arrêt et coût cumulés.
4. Liste des équipements ayant au moins 3 interventions correctives sur le même système
   en moins de 90 jours (défaillances répétitives).
Affiche les tableaux, deux graphiques et le code. Signale les OT exclus et pourquoi.
```

**7. Échanges successifs.** « Compare la part du préventif sur les camions avec celle des pelles » ; « Quelles informations manquent dans les OT pour faire une vraie analyse de fiabilité (heures moteur, pièce changée, cause) ? »

**8. Exemple de résultat (données fictives).** Sur les OT correctifs, le système hydraulique concentre environ 26 % des heures d'arrêt, devant les pneumatiques (≈ 15 %) et le moteur (≈ 14 %). Le CAM-07 compte 18 interventions, dont 11 hydrauliques, soit environ 63 heures d'arrêt et 29 700 USD sur la période. L'OT-25077, à durée négative, est exclu et signalé.

![Figure 22.2 — Pareto des heures d'arrêt en maintenance corrective par système (données fictives MCC). Graphique réalisé pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig22_2_pareto_maintenance.png){width=92%}

**9. Contrôle.** Vérification dans la GMAO du nombre d'OT du CAM-07 et des deux plus gros coûts ; correction de l'OT-25077 à la source.

**10. Erreurs possibles.** Mélange préventif / correctif ; double comptage d'OT liés ; durées d'arrêt confondues avec les durées d'intervention.

**11. Limites.** Le Pareto montre **où** regarder ; il n'explique pas **pourquoi**.

**12. Livrable.** Rapport mensuel de fiabilité avec Pareto, défaillances répétitives et plan d'analyse.

#### Cas d'usage 22.2 — Préparer l'analyse de défaillance du circuit de freinage du CAM-07

**1. Problème.** Une analyse de défaillance (analyse des causes racines) doit être menée par l'équipe maintenance après l'incident.

**2. Méthode habituelle.** Réunion d'analyse, souvent sans préparation documentaire complète.

**3. Contribution de Claude.** Dossier de préparation : chronologie des interventions, extraits des manuels pertinents (fournis), liste des hypothèses à vérifier, plan de collecte de données, trame du rapport.

**4. Données.** Historique OT du CAM-07 ; déclarations de l'incident (`MCC_declarations_incident_INC-2026-0412`) ; extraits du manuel constructeur (fournis par la maintenance) ; résultats d'analyses d'huile (s'il y en a).

**5–6. Procédure et prompt.**

```text
[C] Responsable maintenance de MCC. Après le presque-accident du 14/04/2026 (CAM-07,
glissade au freinage sur rampe R3, fuite constatée sur un flexible du circuit de freinage
avant gauche), nous préparons une analyse de défaillance.
[A] Prépare le dossier de la réunion d'analyse.
[D] Historique OT du CAM-07 (joint), éléments bruts de l'incident (joint), extraits du manuel (joint).
[R] Ne détermine pas la cause racine. Distingue faits établis, hypothèses et informations manquantes.
Ne propose aucune consigne de remise en service.
[E] 1) Chronologie ; 2) faits établis ; 3) hypothèses de causes à vérifier, chacune avec la donnée
ou l'inspection qui permettrait de la confirmer ; 4) plan de collecte ; 5) trame du rapport
d'analyse au format MCC ; 6) questions à poser au constructeur.
```

**7. Échanges.** « Ajoute une rubrique sur les facteurs organisationnels (planification du préventif, pièces de rechange disponibles, délai entre détection et réparation). »

**8. Exemple de résultat (extrait).** Hypothèses à vérifier : usure ou mauvais montage du flexible ; flexibles non conformes au référentiel constructeur ; frottement contre une pièce du châssis ; pression anormale du circuit ; inspection préventive insuffisante. Pour chacune : inspection, pièce à expertiser, données à extraire.

**9. Contrôle.** L'équipe d'analyse valide la liste d'hypothèses et la complète avec ses observations sur l'équipement.

**10. Erreurs possibles.** Hypothèse présentée comme conclusion ; extrait de manuel d'un autre modèle de camion.

**11. Limites.** La cause racine est établie par l'équipe, à partir d'inspections, d'expertises et de données ; la remise en service suit la procédure.

**12. Livrable.** Dossier préparatoire, puis rapport d'analyse de défaillance rédigé avec l'aide de Claude à partir des conclusions de l'équipe.

#### Cas d'usage 22.3 — Classer les descriptions libres des OT (condensé)

Claude classe les descriptions en texte libre (« fuite flexible vérin benne », « bruit pont arrière ») selon une liste fermée de modes de défaillance fournie par la maintenance, avec un niveau de confiance et un signalement des cas ambigus, sur le modèle de l'apprentissage par l'exemple (chapitre 11). Résultat : une base plus exploitable pour les analyses de fiabilité. Contrôle par double codage d'un échantillon.

#### Cas d'usage 22.4 — Rédiger une gamme de maintenance préventive (condensé)

À partir du manuel constructeur (extraits fournis), des retours d'expérience et des défaillances répétitives, Claude rédige un projet de gamme (opérations, fréquences proposées **par le manuel**, outillage, pièces, points de contrôle, critères d'acceptation). Toute valeur (couple de serrage, pression, intervalle) doit provenir du manuel ; sinon elle est marquée « à confirmer ». Validation par le responsable maintenance et, pour les systèmes de sécurité, par le constructeur ou l'ingénieur compétent.

### E. Prompts commentés

**Prompt 22.1 — Ordre de travail clair à partir d'un signalement**

```text
Signalement d'un conducteur : « [texte] ». Rédige un projet d'ordre de travail :
équipement, symptôme décrit (citation), urgence proposée (à valider par le planificateur)
selon la grille suivante <grille> … </grille>, vérifications initiales suggérées,
risques pour la sécurité à signaler immédiatement. N'indique aucune cause.
```

*Commentaire.* L'urgence est **proposée** selon une grille fournie, puis validée : Claude accélère le tri sans décider.

### F. Exercices pratiques

**Exercice 22.1 (guidé).** Réalisez le cas 22.1 avec le fichier d'exercice. Retrouvez-vous les 11 interventions hydrauliques du CAM-07 ?

**Exercice 22.2 (guidé).** Réalisez le cas 22.2 en utilisant le document d'incident fourni. Combien d'hypothèses de causes l'équipe devra-t-elle vérifier ?

**Exercice 22.3 (autonome).** Pour un équipement de votre site, préparez un projet de gamme préventive (cas 22.4) en marquant toutes les valeurs à confirmer.

### G. Livrable professionnel

**Rapport de fiabilité mensuel** (Pareto, défaillances répétitives, coûts) et **dossier d'analyse de défaillance** préparé, prêt pour la réunion de l'équipe.

### H. Vérification des résultats

::: controle
- Les OT exclus ou corrigés sont listés et corrigés à la source (GMAO).
- Les chiffres clés (nombre d'OT, heures, coûts) ont été vérifiés dans la GMAO.
- Aucune cause racine n'est affirmée sans validation de l'équipe d'analyse.
- Les valeurs techniques des gammes proviennent du manuel constructeur.
:::

::: setrompe
Sollicité pour un intervalle de remplacement de flexibles hydrauliques, un assistant peut proposer un intervalle « standard » plausible (en heures ou en mois) sans lien avec le manuel du constructeur, les conditions du site ou l'historique. **Contre-mesure** : exiger la source de toute valeur technique et la confronter au manuel.
:::

### I. Limites et précautions

- Claude ne voit pas l'équipement : le diagnostic se fait sur site.
- Les données de la GMAO sont souvent incomplètes ; la qualité de l'analyse en dépend.
- Les recommandations de remise en service relèvent des procédures et des personnes habilitées.

### J. Boîte à outils

- Prompts des cas 22.1, 22.2 et prompt 22.1.
- Définitions à fournir à Claude : disponibilité, temps moyen entre défaillances (MTBF), temps moyen de réparation (MTTR), selon la méthode de l'entreprise.
- Trame de rapport d'analyse de défaillance (Annexe D).

### K. Quiz

1. **(QCM)** Un Pareto des heures d'arrêt sert à : a) établir la cause racine ; b) identifier où concentrer l'effort d'analyse ; c) remettre en service un engin ; d) calculer la paie.
2. **(Vrai ou faux)** Claude peut décider de la remise en service d'un camion après réparation du freinage.
3. **(Compréhension)** Pourquoi faut-il exclure et signaler l'OT à durée négative ?
4. **(Application)** Dans les données d'exercice, quel système concentre la plus grande part des heures d'arrêt correctives ?
5. **(Mise en situation)** Claude conclut que « la cause est l'usure du flexible ». Comment reformulez-vous la demande ?
6. **(Vrai ou faux)** Les valeurs d'une gamme préventive doivent provenir du manuel constructeur ou être marquées « à confirmer ».
7. **(Compréhension)** Citez deux facteurs organisationnels à examiner dans une analyse de défaillance.
8. **(QCM)** Pour classer les descriptions libres des OT, la meilleure technique est : a) une liste fermée de modes de défaillance et des exemples ; b) laisser Claude inventer des catégories ; c) un résumé global ; d) une traduction.
9. **(Analyse critique)** Pourquoi le Pareto ne suffit-il pas à décider d'un plan d'action ?
10. **(Application)** Rédigez la règle qui empêche Claude de fixer l'urgence d'un ordre de travail.

<div class="carnet" titre="Chapitre 22 — Claude appliqué à la maintenance et à la gestion des équipements"></div>
