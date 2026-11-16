## Chapitre 40 — Déployer une politique d'utilisation de l'intelligence artificielle dans une entreprise minière

### A. Mise en situation professionnelle

Janvier 2026 : Aline Mujinga lance le programme « MCC-IA 2026 ». Elle sait que des salariés utilisent déjà des assistants d'IA, parfois avec leurs comptes personnels. Interdire n'empêcherait pas l'usage ; laisser faire exposerait l'entreprise. Elle confie à un comité de pilotage la mission de construire une **politique** : gouvernance, charte, classification, outils autorisés, formation, déploiement progressif, contrôle. Ce chapitre retrace la démarche, que vous pourrez adapter à votre entreprise.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Concevoir** la gouvernance de l'IA d'une entreprise (rôles, instances, décisions).
2. **Rédiger** une charte d'utilisation adaptée au secteur minier.
3. **Planifier** un déploiement progressif (pilote, évaluation, extension).
4. **Définir** les indicateurs de suivi et le dispositif de contrôle.
5. **S'appuyer** sur les cadres de référence (NIST AI RMF, ISO/IEC 42001, réglementations applicables, politique d'utilisation du fournisseur).

### C. Comprendre avant de pratiquer

#### C.1. Les cadres de référence

- **NIST AI RMF** : quatre fonctions — gouverner (culture, rôles, politiques), cartographier (contextes et risques), mesurer (évaluation), gérer (traitement des risques) [@NIST-RMF] ; complété par un profil spécifique à l'IA générative [@NIST-GAI].
- **ISO/IEC 42001:2023** : exigences d'un système de management de l'IA, certifiable [@ISO-42001].
- **Règlement (UE) 2024/1689** sur l'intelligence artificielle : approche par niveaux de risque ; pertinent pour les entreprises qui opèrent avec l'Union européenne ou y vendent [@EU-AIACT].
- **Politique d'utilisation d'Anthropic** : normes d'usage universelles et exigences supplémentaires pour les cas d'usage à haut risque, applicables aux utilisateurs de Claude [@ANT-AUP].
- **Recommandation de l'UNESCO** pour les principes éthiques [@UNESCO-2021].

#### C.2. La gouvernance

![Figure 40.1 — Gouvernance de l'IA à MCC : conseil, comité de pilotage, référent IA, informatique, juridique, propriétaires métier et audit interne. Organisation fictive inspirée de la fonction « Gouverner » du NIST AI RMF. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig40_1_gouvernance_ia.png){width=100%}

#### C.3. Les composants de la politique

| Composant | Contenu | Annexe |
|---|---|---|
| Charte d'utilisation | Principes, usages autorisés, interdits, responsabilités, sanctions | F |
| Classification des données | 4 niveaux, règles par niveau | G |
| Outils autorisés | Offres, comptes, connecteurs, extensions validés | — |
| Registre des cas d'usage | Cas validés, propriétaires, risques, contrôles | — |
| Formation | Parcours obligatoire avant accès ; parcours avancés | J, K |
| Gestion des incidents | Signalement, analyse, correction | — |
| Contrôle | Indicateurs, audits, revue annuelle | — |

#### C.4. Le déploiement progressif

![Figure 40.2 — Feuille de route type de déploiement (calendrier illustratif). Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig40_2_feuille_de_route.png){width=95%}

1. **Cadrage (mois 0-2)** : gouvernance, charte, classification, choix de l'offre, contrat.
2. **Pilote (mois 2-6)** : 40 utilisateurs, 8 services, cas d'usage à faible risque, mesures avant/après.
3. **Évaluation (mois 7)** : gains mesurés, incidents, satisfaction, conformité.
4. **Extension par vagues (mois 8-14)** : nouveaux services, assistants spécialisés, premiers workflows.
5. **Amélioration continue** : revue annuelle, audit interne, mise à jour des règles.

### D. Démonstration guidée — Construire la politique de MCC

1. **Constat** : enquête anonyme auprès des cadres sur les usages actuels de l'IA (dont l'usage de comptes personnels).
2. **Comité de pilotage** : DG, DAF, HSE, juridique, informatique, RH ; référent IA désigné.
3. **Charte** : rédigée avec l'aide de Claude à partir du modèle de l'Annexe F, puis débattue, adaptée et validée (prompt 40.1).
4. **Classification** : adoptée (Annexe G) ; liste des usages interdits (décisions de sécurité critiques, décisions individuelles RH, données de niveau 4).
5. **Outils** : offre d'entreprise, SSO, connecteurs désactivés par défaut, activation sur demande documentée.
6. **Formation** : module obligatoire de 4 heures (parties I, II et V de ce manuel) avant l'ouverture des accès.
7. **Pilote et mesures** ; **bilan** au comité ; **décision** d'extension.
8. **Contrôle** : indicateurs trimestriels ; audit interne de la charte à 12 mois (chapitre 29).

### E. Prompts commentés

**Prompt 40.1 — Adapter la charte modèle**

```text
Voici notre modèle de charte d'utilisation de l'IA (Annexe F) et notre contexte : [taille, activités,
pays, offres utilisées, organisation]. Adapte la charte : vérifie qu'elle couvre gouvernance,
usages autorisés et interdits, classification des données, responsabilités, sécurité, formation,
incidents, contrôle et sanctions. Signale les dispositions qui doivent être vérifiées par le juridique
au regard du droit applicable (travail, données personnelles, réglementation boursière).
Présente les modifications en mode révision.
```

**Prompt 40.2 — Indicateurs de pilotage**

```text
Propose 10 indicateurs de pilotage d'un programme d'IA générative dans une entreprise minière,
répartis en adoption, valeur (mesurée), risques et conformité, compétences. Pour chacun :
définition, source de la donnée, fréquence, cible indicative à valider. Aucun indicateur
de valeur ne doit reposer sur une estimation non mesurée.
```

### F. Exercices pratiques

**Exercice 40.1 (guidé).** Adaptez la charte de l'Annexe F à votre entreprise avec le prompt 40.1 ; listez les points à valider par le juridique.

**Exercice 40.2 (guidé).** Construisez le tableau de bord du programme IA avec le prompt 40.2.

**Exercice 40.3 (autonome).** Rédigez la feuille de route de déploiement de votre entreprise (ou de votre service) sur 18 mois.

### G. Livrable professionnel

**Dossier de politique IA** : gouvernance, charte adaptée, classification, liste des outils autorisés, registre des cas d'usage, plan de formation, feuille de route, indicateurs, dispositif de contrôle.

### H. Vérification des résultats

::: controle
- Les rôles et instances de gouvernance sont désignés.
- La charte couvre usages autorisés et interdits, données, responsabilités, incidents, contrôle.
- Aucun accès n'est ouvert sans formation préalable.
- Les cas d'usage sont enregistrés avec propriétaire, risques et contrôles.
- Les indicateurs de valeur reposent sur des mesures.
- Une revue annuelle et un audit sont planifiés.
:::

::: setrompe
Un projet de charte rédigé par un assistant d'IA peut citer des obligations « légales » inexistantes ou mal rattachées à un texte (« conformément à l'article X de la loi sur… »). Une charte est un document engageant : chaque référence juridique doit être vérifiée par le service juridique.
:::

### I. Limites et précautions

- Une politique trop restrictive pousse à l'« IA de l'ombre » ; une politique trop laxiste expose l'entreprise.
- Les réglementations sur l'IA évoluent rapidement : veille juridique indispensable.
- La politique doit être revue à chaque évolution majeure des outils.

### J. Boîte à outils

- Prompts 40.1, 40.2.
- Annexes F (charte), G (classification), J (programme 30 jours), K (grille d'évaluation).
- Feuille de route type (figure 40.2).

### K. Quiz

1. **(QCM)** Quelle norme définit les exigences d'un système de management de l'IA ? a) ISO 9001 ; b) ISO/IEC 42001 ; c) ISO 14001 ; d) ISO 45001.
2. **(Vrai ou faux)** Interdire totalement l'IA est la manière la plus sûre d'éviter les risques.
3. **(Compréhension)** Pourquoi exiger une formation avant l'ouverture des accès ?
4. **(QCM)** Combien de fonctions comporte le NIST AI RMF ? a) 2 ; b) 4 ; c) 6 ; d) 8.
5. **(Mise en situation)** Vous découvrez que des cadres utilisent leurs comptes personnels. Que proposez-vous ?
6. **(Compréhension)** Qu'est-ce qu'un registre des cas d'usage ?
7. **(Vrai ou faux)** Les références juridiques d'une charte rédigée avec Claude doivent être vérifiées par le juridique.
8. **(Application)** Citez deux indicateurs de risque et conformité pour un programme IA.
9. **(Analyse critique)** Pourquoi le déploiement progressif est-il préférable à un déploiement général immédiat ?
10. **(Compréhension)** À quelles entreprises le règlement européen sur l'IA est-il particulièrement pertinent ?

<div class="carnet" titre="Chapitre 40 — Déployer une politique d'utilisation de l'intelligence artificielle dans une entreprise minière"></div>
