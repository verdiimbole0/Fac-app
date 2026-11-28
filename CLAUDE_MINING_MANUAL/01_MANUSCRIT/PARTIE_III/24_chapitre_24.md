## Chapitre 24. Claude appliqué à la gestion environnementale, à l'eau, aux résidus miniers et à la fermeture des mines

### A. Mise en situation professionnelle

Esther Kalala, responsable environnement de MCC, constate dans le rapport de laboratoire de mars 2026 que la concentration de cuivre dissous au point de rejet ST-02 a atteint 0,548 mg/L, au-dessus de la limite retenue pour l'exercice (0,5 mg/L), après une hausse déjà sensible en février. Elle doit informer la direction, vérifier les obligations de notification, comprendre l'origine possible et préparer les actions. La même semaine, elle doit aussi mettre à jour le plan de fermeture, exigé tous les trois ans, et préparer la revue annuelle du parc à résidus Kilima avec l'ingénieur responsable.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Analyser** des séries de suivi environnemental et détecter les dépassements de manière traçable.
2. **Préparer** une note d'alerte et un plan d'investigation sans conclure prématurément.
3. **Synthétiser** des études environnementales longues (EIES, plans de gestion) avec citations.
4. **Contribuer** à la documentation de la gestion des résidus dans le respect des responsabilités définies par les référentiels.
5. **Structurer** la mise à jour d'un plan de fermeture.

### C. Comprendre avant de pratiquer : Profil du métier

Les référentiels internationaux encadrent fortement ce domaine : les **Normes de performance** de la SFI (évaluation et gestion environnementale et sociale, utilisation rationnelle des ressources et prévention de la pollution, biodiversité…) [@IFC-PS] ; la **Norme mondiale de l'industrie sur la gestion des résidus miniers (GISTM)**, publiée en août 2020 à l'issue d'un processus co-organisé par l'ICMM, le PNUE et les PRI, qui couvre notamment la connaissance du site, la conception, la construction, l'exploitation et la surveillance des installations, la gouvernance, la préparation aux urgences et la transparence [@GISTM-2020; @ICMM-TAIL].

*Tableau 24.1. Profil de l'équipe environnement.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Conformité environnementale, suivi de l'eau, de l'air, des sols et de la biodiversité, gestion des déchets, contribution à la gestion des résidus, plan de fermeture |
| Tâches quotidiennes | Prélèvements, interprétation des analyses, inspections, rapports réglementaires, relations avec l'administration et les communautés |
| Difficultés | Volume de données ; délais de notification ; rapports réglementaires longs ; coordination avec l'exploitation ; attentes des communautés |
| Documents | EIES, plan de gestion environnementale et sociale, permis, rapports de laboratoire, rapports réglementaires, plan de fermeture, rapports de surveillance du parc à résidus |
| Données | Qualité des eaux (pH, sulfates, métaux, matières en suspension), débits, piézométrie, poussières, bruit, données de biodiversité |
| Livrables | Rapports mensuels et réglementaires, notes d'alerte, plans d'action, plan de fermeture et estimation des coûts |
| Assistables par Claude | Analyse de séries (code) ; détection des dépassements ; synthèse d'études ; premiers jets de rapports ; matrices d'obligations ; communications à valider |
| Limites | Interprétation hydrogéologique, sécurité des digues, décisions de notification, engagements envers l'administration, conception des mesures correctives |

::: attention
**Parc à résidus.** La stabilité des digues, l'interprétation de l'auscultation (piézomètres, inclinomètres, radars), la classification de conséquence et les décisions d'exploitation relèvent de l'ingénieur responsable et des experts désignés, avec les revues indépendantes prévues par les référentiels comme la GISTM. Claude peut aider à organiser la documentation et les rapports ; il ne se prononce jamais sur la sécurité d'un ouvrage.
:::

![Figure 24.1. Digue de stockage des résidus et usine de traitement (photographie historique). Titre original : « StateLibQld 2 257026 Tailings storage dam, Mt. Isa Mines, 1932 ». Auteur : L. Plass (State Library of Queensland). Source : Wikimedia Commons, [https://commons.wikimedia.org/wiki/File:StateLibQld_2_257026_Tailings_storage_dam,_Mt._Isa_Mines,_1932.jpg](https://commons.wikimedia.org/wiki/File:StateLibQld_2_257026_Tailings_storage_dam,_Mt._Isa_Mines,_1932.jpg) (consulté le 16/11/2026). Licence : domaine public. Photographie d'illustration, sans lien avec l'entreprise fictive MCC.](02_ILLUSTRATIONS/PHOTOGRAPHIES/photo_parc_residus_mt_isa.jpg){width=78%}

### D. Démonstration guidée : Cas d'usage

#### Cas d'usage 24.1. Détecter et documenter un dépassement au point de rejet

**1. Problème.** Le cuivre dissous à ST-02 dépasse la limite en mars 2026 ; il faut documenter rapidement le constat et préparer l'investigation.

**2. Méthode habituelle.** Lecture des certificats d'analyse, tableur, note manuscrite.

**3. Contribution de Claude.** Analyse des séries par station (code), comparaison aux limites **fournies**, graphiques, mise en évidence de l'évolution amont-aval, projet de note d'alerte et plan d'investigation.

**4. Données.** `MCC_suivi_qualite_eau.csv` (4 stations, 18 mois) ; limites de rejet applicables (ici, limite fictive de l'exercice) ; procédure interne d'alerte.

**5. Procédure.** Analyse → vérification des certificats de laboratoire → décision d'Esther sur la notification (selon la réglementation et le permis) → note d'alerte → investigation.

**6. Prompt.**

```text
[C] Responsable environnement de MCC. Le suivi de mars 2026 montre une valeur élevée
de cuivre dissous au point de rejet ST-02.
[A] Analyse les séries de suivi et prépare une note d'alerte interne et un plan d'investigation.
[D] Fichier MCC_suivi_qualite_eau.csv (stations ST-01 amont, ST-02 rejet, ST-03 aval 2 km,
PZ-04 piézomètre du parc). Limite applicable pour l'exercice : Cu dissous 0,5 mg/L au point de rejet.
[R] Calculs et graphiques par exécution de code. Compare uniquement aux limites fournies.
Ne conclus pas sur l'origine ; ne te prononce pas sur l'obligation de notification
(décision de la responsable environnement selon le permis et la réglementation).
[E] 1) Tableau des valeurs dépassant ou approchant la limite (≥ 80 %) ; 2) graphique Cu par station ;
3) évolution des autres paramètres à ST-02 (pH, sulfates) sur les mêmes mois ; 4) note d'alerte (1/2 page) ;
5) plan d'investigation : hypothèses, prélèvements et vérifications, responsables.
```

**7. Échanges successifs.** « Le pH a-t-il baissé à ST-02 en février-mars ? » ; « La station aval ST-03 montre-t-elle une hausse décalée dans le temps ? » ; « Rédige la demande de contre-analyse au laboratoire. »

**8. Exemple de résultat (données fictives).** ST-02 : 0,50 mg/L en février (au seuil) et 0,548 mg/L en mars 2026 (au-dessus de la limite de l'exercice) ; retour à des valeurs habituelles (≈ 0,1 mg/L) à partir d'avril. Hypothèses à vérifier : épisode de fortes pluies et débordement d'un bassin, dysfonctionnement d'un traitement, erreur de prélèvement ou d'analyse.

![Figure 24.2. Suivi mensuel du cuivre dissous aux quatre stations de MCC (données fictives) : hausse au point de rejet en février et dépassement en mars 2026. Graphique réalisé pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig24_1_suivi_eau_cuivre.png){width=92%}

**9. Contrôle.** Vérification des valeurs sur les certificats du laboratoire ; vérification de la limite dans le permis réel ; relecture de la note par la direction.

**10. Erreurs possibles.** Unités (mg/L vs µg/L) ; confusion entre métal total et dissous ; limite d'un autre texte appliquée par erreur.

**11. Limites.** L'origine du dépassement est établie par investigation de terrain ; les relations avec l'administration relèvent des personnes habilitées.

**12. Livrable.** Note d'alerte interne, plan d'investigation et, si la décision est prise, projet de notification à l'administration validé par la direction et le juridique.

#### Cas d'usage 24.2. Synthèse et matrice des engagements de l'EIES

**1. Problème.** L'EIES de 2019 et le plan de gestion environnementale et sociale contiennent des centaines d'engagements dispersés ; MCC doit démontrer leur suivi.

**2. Méthode habituelle.** Tableur constitué à la main, incomplet.

**3. Contribution de Claude.** Extraction systématique des engagements avec citation et page, classement par thème, responsable et échéance proposés, statut à renseigner.

**4. Données.** EIES et plan de gestion (PDF, découpés si nécessaire pour respecter les limites de pages et analyser les tableaux).

**5–6. Procédure et prompt.**

```text
Document joint : [chapitre X de l'EIES]. Extrais tous les engagements de l'entreprise
(mesures d'atténuation, de suivi, de compensation, de consultation).
Tableau : n° | engagement (citation exacte) | page | thème (eau, air, bruit, biodiversité,
sols, déchets, social, fermeture) | fréquence ou échéance mentionnée | indicateur de suivi mentionné.
N'ajoute aucun engagement ; si une formulation est ambiguë, indique « ambigu ».
```

**7. Échanges.** Traitement chapitre par chapitre ; puis « Fusionne les tableaux et repère les doublons » ; « Quels engagements n'ont ni fréquence ni indicateur ? »

**8. Exemple de résultat.** Matrice de 180 engagements (fictifs), dont 22 sans indicateur de suivi : à compléter par l'équipe.

**9. Contrôle.** Échantillon de 15 % vérifié dans le document ; validation des responsables et échéances en réunion.

**10. Erreurs possibles.** Engagement omis dans une annexe ; recommandation d'un consultant confondue avec un engagement de l'entreprise.

**11. Limites.** La matrice n'a pas de valeur juridique tant qu'elle n'est pas validée.

**12. Livrable.** Registre des engagements environnementaux et sociaux, validé, avec responsables et échéances.

#### Cas d'usage 24.3. Documentation du parc à résidus (condensé)

Claude aide l'ingénieur responsable à organiser la documentation exigée par les référentiels : tableau de correspondance entre les exigences de la GISTM et les documents existants de MCC, identification des documents manquants, mise en forme du rapport annuel de surveillance **à partir des données et conclusions fournies par l'ingénieur**, et préparation de la version publique des informations dont la divulgation est prévue. Aucun avis sur la stabilité n'est demandé à Claude.

#### Cas d'usage 24.4. Mise à jour du plan de fermeture (condensé)

À partir du plan de fermeture précédent, des changements intervenus (nouvelles installations, extension Mbiyo Profond, attentes des communautés), Claude propose une structure de mise à jour, un tableau des modifications, la liste des hypothèses de coût à réviser et un projet de résumé non technique pour la consultation des communautés. L'estimation des coûts de fermeture et les choix techniques relèvent des spécialistes ; la provision comptable (88 MUSD dans le scénario) relève de la finance et des auditeurs.

![Figure 24.3. Revégétalisation d'un site dégradé. Titre original : « CSIRO ScienceImage 924 Revegetation project ». Auteur : Nick Pitsas, CSIRO. Source : Wikimedia Commons, [https://commons.wikimedia.org/wiki/File:CSIRO_ScienceImage_924_Revegetation_project.jpg](https://commons.wikimedia.org/wiki/File:CSIRO_ScienceImage_924_Revegetation_project.jpg) (consulté le 16/11/2026). Licence : [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/deed.fr) ; image redimensionnée pour l'édition. Photographie d'illustration, sans lien avec l'entreprise fictive MCC.](02_ILLUSTRATIONS/PHOTOGRAPHIES/photo_revegetation_csiro.jpg){width=78%}

### E. Prompts commentés

**Prompt 24.1. Rapport réglementaire à partir de données validées**

```text
Rédige le projet de rapport trimestriel de suivi de la qualité des eaux, selon le modèle joint.
Données validées : <donnees> … </donnees>. Limites applicables : <limites> … </limites>.
Règles : chaque valeur citée provient des données ; chaque comparaison utilise la limite fournie ;
tout dépassement est signalé avec les actions engagées (fournies), sans en ajouter.
Termine par la liste des pièces justificatives à annexer.
```

*Commentaire.* Dans un document destiné à l'administration, l'exactitude est une obligation : les règles interdisent tout ajout non fondé.

### F. Exercices pratiques

**Exercice 24.1 (guidé).** Réalisez le cas 24.1 avec le fichier d'exercice. Identifiez le mois du dépassement et l'évolution du pH à ST-02.

**Exercice 24.2 (guidé).** Avec un chapitre d'une étude d'impact publique de votre choix, construisez la matrice des engagements (cas 24.2) et vérifiez 10 citations.

**Exercice 24.3 (autonome).** Préparez la structure de mise à jour d'un plan de fermeture (cas 24.4) pour le scénario MCC, en distinguant ce qui relève de Claude, des spécialistes et de la direction.

### G. Livrable professionnel

**Dossier environnemental mensuel** : analyse des suivis, alertes et investigations, matrice des engagements à jour, état d'avancement du plan de fermeture.

### H. Vérification des résultats

::: controle
- Les valeurs et limites citées ont été vérifiées sur les certificats et dans le permis.
- Les unités et formes (dissous/total) sont cohérentes.
- Aucun avis sur la sécurité du parc à résidus n'a été produit par Claude.
- Les engagements extraits sont vérifiés par échantillonnage et validés.
- Les documents destinés à l'administration ou au public ont suivi le circuit de validation.
:::

::: setrompe
Interrogé sans document de référence sur la « limite de rejet du cuivre en RDC », un assistant peut fournir une valeur plausible tirée d'un autre pays ou d'un autre type de rejet. **Contre-mesure** : ne jamais utiliser une limite qui ne provient pas du permis ou du texte réglementaire applicable, fourni et vérifié.
:::

### I. Limites et précautions

- Les décisions de notification et les engagements envers l'administration relèvent des personnes habilitées.
- Les données environnementales peuvent être sensibles (litiges, communautés, investisseurs).
- Les référentiels (GISTM, Normes de performance) exigent des revues indépendantes que l'IA ne remplace pas.

### J. Boîte à outils

- Prompts des cas 24.1, 24.2 et prompt 24.1.
- Gabarit de matrice des engagements : n° | engagement | source/page | thème | responsable | échéance | indicateur | statut | preuve.
- Check-list « dépassement » : vérifier la valeur ; vérifier la limite ; informer ; décider de la notification ; investiguer ; tracer.

### K. Quiz

1. **(QCM)** La GISTM a été publiée en : a) 2015 ; b) 2018 ; c) 2020 ; d) 2024.
2. **(Vrai ou faux)** Claude peut évaluer la stabilité d'une digue à partir des données d'auscultation.
3. **(Application)** Dans les données d'exercice, en quel mois la limite est-elle dépassée à ST-02 ?
4. **(Compréhension)** Pourquoi distinguer métal dissous et métal total ?
5. **(Mise en situation)** Claude propose une limite de rejet « standard ». Que faites-vous ?
6. **(QCM)** Qui décide de notifier un dépassement à l'administration ? a) Claude ; b) le laboratoire ; c) la personne habilitée selon le permis et la réglementation ; d) le fournisseur.
7. **(Compréhension)** Qu'est-ce qu'une matrice des engagements de l'EIES et à quoi sert-elle ?
8. **(Vrai ou faux)** La recommandation d'un consultant dans une EIES est toujours un engagement de l'entreprise.
9. **(Analyse critique)** Pourquoi le retour à la normale en avril ne clôt-il pas le sujet ?
10. **(Compréhension)** Citez deux Normes de performance de la SFI pertinentes pour l'environnement minier.

<div class="carnet" titre="Chapitre 24. Claude appliqué à la gestion environnementale, à l'eau, aux résidus et à la fermeture"></div>
