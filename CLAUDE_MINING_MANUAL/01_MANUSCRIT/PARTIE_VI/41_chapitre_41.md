## Chapitre 41 — Ateliers pratiques transversaux

### A. Mise en situation professionnelle

Lundi 4 mai 2026. À MCC, une semaine ordinaire n'existe pas : un dépassement au point de rejet a été constaté en mars, le presque-accident de la rampe R3 est en cours d'enquête, le budget des réactifs dérape, le village de Lupanda attend une réponse et l'acheteur européen relance son questionnaire. Ces sujets ne sont pas cloisonnés : ils touchent plusieurs services à la fois. Les six ateliers de ce chapitre reproduisent cette réalité. Chacun mobilise plusieurs compétences et plusieurs chapitres du manuel.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Conduire** un travail transversal mobilisant plusieurs services et plusieurs sources.
2. **Combiner** les techniques du manuel (CADRE, chaînage, données, vérification, sécurité).
3. **Produire** des livrables complets dans un temps limité.
4. **Évaluer** votre travail avec une grille objective.
5. **Animer** un atelier en équipe (pour les formateurs et managers).

### C. Comprendre avant de pratiquer — Mode d'emploi des ateliers

Chaque atelier précise : la situation, les fichiers d'exercice, la durée indicative, les étapes, les livrables et la grille d'évaluation. Les ateliers peuvent être réalisés seuls ou en groupe de 3 à 5 personnes (idéalement de services différents). Un corrigé indicatif figure à l'Annexe L ; les anomalies insérées dans les données sont listées dans `ANOMALIES_ATTENDUES.md` (à consulter **après** l'atelier).

*Grille d'évaluation commune (sur 20).*

| Critère | Points |
|---|---|
| Qualité des instructions (CADRE, règles de vérité, limites de rôle) | 4 |
| Exactitude des faits et des calculs (vérifiés) | 5 |
| Détection des anomalies et des pièges | 3 |
| Qualité et pertinence du livrable | 4 |
| Respect des règles de sécurité et de confidentialité | 2 |
| Traçabilité (sources, versions, contrôles documentés) | 2 |

### D. Démonstration guidée — Les six ateliers

#### Atelier 1 — Le dossier de l'incident de la rampe R3 (HSE, maintenance, production) — 2 h

*Fichiers :* `MCC_declarations_incident_INC-2026-0412`, `MCC_maintenance_ordres_travail.csv`, `MCC_incidents_HSE_2025_2026.csv`.

*Étapes :* (1) rapport préliminaire (ch. 23) ; (2) historique du CAM-07 et préparation de l'analyse de défaillance (ch. 22) ; (3) analyse des événements « circulation » du registre (ch. 23) ; (4) causerie pour les conducteurs (ch. 20) ; (5) note d'une page au directeur des opérations.

*Livrables :* rapport préliminaire ; dossier préparatoire d'analyse de défaillance ; causerie ; note.

*Pièges :* formulations qui anticipent les causes ; OT à durée négative ; heures approximatives présentées comme exactes.

#### Atelier 2 — Le dépassement au point de rejet (environnement, communautés, juridique, direction) — 2 h

*Fichiers :* `MCC_suivi_qualite_eau.csv`, `MCC_registre_plaintes.csv`.

*Étapes :* (1) analyse des séries et note d'alerte (ch. 24) ; (2) recherche dans le registre de plaintes de signalements liés à l'eau à la même période (ch. 25) ; (3) liste des questions juridiques sur la notification (ch. 27) ; (4) projet d'information aux communautés, **à valider** (ch. 25) ; (5) synthèse pour la direction (ch. 31).

*Pièges :* limite de rejet non fournie par un texte officiel (ne pas en inventer) ; confusion entre corrélation et cause ; promesses dans le message aux communautés.

#### Atelier 3 — Le dérapage des réactifs (usine, achats, finance, juridique) — 2 h 30

*Fichiers :* `MCC_budget_reel_S1_2026.xlsx`, `MCC_contrat_fourniture_acide_extrait`, `MCC_rapport_mensuel_production_mars_2026`, `MCC_bons_de_commande.csv`.

*Étapes :* (1) décomposition de l'écart (ch. 21, 28) ; (2) analyse contractuelle de la hausse de prix et de la pénalité de mars (ch. 26) ; (3) revue des commandes d'acide (ch. 26) ; (4) note d'écarts au comité ; (5) projet de courrier au fournisseur, à valider par le juriste.

*Pièges :* attribuer tout l'écart à l'acide ; ignorer le plafond de révision de 15 % ; conclure sur un extrait de contrat.

#### Atelier 4 — L'audit éclair des achats (audit, achats, contrôle interne) — 1 h 30

*Fichier :* `MCC_bons_de_commande.csv`.

*Étapes :* tests de population T1 à T4 (ch. 29) ; papier de travail ; constats CCCRR ; demande de pièces.

*Pièges :* qualifier de fraude un simple signalement ; test « doublons » inopérant à cause des types de données.

#### Atelier 5 — Le questionnaire du client européen (ESG, opérations, communautés, RH) — 2 h

*Matériel :* 15 questions de diligence rédigées par l'animateur ; bibliothèque de preuves fictives.

*Étapes :* (1) classement des questions par service ; (2) projet de réponses fondées sur les preuves (ch. 32) ; (3) détection des affirmations non étayées ; (4) liste des preuves manquantes.

*Pièges :* formulations absolues ; politique présentée comme preuve d'application.

#### Atelier 6 — La procédure piégée (sécurité de l'IA) — 45 min

*Fichier :* `MCC_procedure_reception_reactifs_PIEGE.docx`.

*Étapes :* (1) analyse naïve ; (2) analyse défensive (prompt 38.1) ; (3) rédaction de la règle de protection pour tous les assistants ; (4) fiche de sensibilisation pour les utilisateurs.

### E. Prompts commentés

**Prompt 41.1 — Plan de travail d'un atelier transversal**

```text
Nous sommes une équipe de [n] personnes ([services]). Atelier : [titre], durée [x] h.
Fichiers disponibles : [liste]. Livrables attendus : [liste].
Propose un plan de travail : étapes, répartition entre membres, prompts à utiliser à chaque étape
(selon la méthode CADRE), points de contrôle, minutage. Signale les pièges probables de chaque étape.
```

*Commentaire.* Utiliser Claude pour organiser le travail d'équipe est un usage simple, sans risque, et souvent très rentable.

### F. Exercices pratiques

Les six ateliers constituent les exercices de ce chapitre. Recommandation : réalisez au moins les ateliers 1, 3 et 6 ; les formateurs peuvent organiser une journée complète avec les ateliers 1 à 4.

### G. Livrable professionnel

**Portfolio d'ateliers** : pour chaque atelier réalisé, les livrables, les prompts utilisés, les contrôles effectués et l'autoévaluation sur la grille commune.

### H. Vérification des résultats

::: controle
- Toutes les anomalies de `ANOMALIES_ATTENDUES.md` liées à l'atelier ont-elles été détectées ?
- Chaque livrable respecte-t-il les limites de rôle (aucune cause, aucune décision, aucune promesse) ?
- Les calculs clés ont-ils été recalculés indépendamment ?
:::

::: setrompe
Dans un atelier transversal, l'erreur la plus fréquente n'est pas une hallucination isolée, mais une **incohérence entre livrables** : la note à la direction reprend un chiffre de la première version du rapport, corrigé depuis. **Contre-mesure** : un tableau unique des chiffres de référence pour l'ensemble de l'atelier.
:::

### I. Limites et précautions

- Les ateliers utilisent des données fictives ; transposez avec prudence à vos données réelles (classification, autorisations).
- La grille d'évaluation est indicative ; adaptez les pondérations à vos objectifs.

### J. Boîte à outils

- Grille d'évaluation commune ; prompt 41.1 ; `ANOMALIES_ATTENDUES.md` ; Annexe L (corrigés).

### K. Quiz

1. **(Compréhension)** Pourquoi les ateliers associent-ils plusieurs services ?
2. **(Vrai ou faux)** Il est recommandé de consulter la liste des anomalies avant l'atelier.
3. **(Application)** Dans l'atelier 3, quel élément du contrat est déterminant pour la hausse de prix ?
4. **(QCM)** Quelle erreur est la plus fréquente dans un atelier transversal ? a) une faute de frappe ; b) une incohérence entre livrables ; c) une panne ; d) un modèle trop rapide.
5. **(Mise en situation)** Dans l'atelier 2, votre message aux communautés promet « une eau parfaitement saine ». Qu'en pensez-vous ?
6. **(Compréhension)** Combien de points la grille attribue-t-elle à l'exactitude ?
7. **(Vrai ou faux)** Dans l'atelier 4, un signalement de fractionnement peut être présenté comme une fraude.
8. **(Application)** Citez deux pièges de l'atelier 1.
9. **(Analyse critique)** Pourquoi un tableau unique des chiffres de référence est-il utile ?
10. **(Compréhension)** Quel est l'objectif de l'atelier 6 ?

<div class="carnet" titre="Chapitre 41 — Ateliers pratiques transversaux"></div>
