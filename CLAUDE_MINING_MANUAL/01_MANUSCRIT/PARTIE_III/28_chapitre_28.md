## Chapitre 28 — Claude appliqué à la comptabilité, à la finance, à la fiscalité et au contrôle de gestion

### A. Mise en situation professionnelle

Fin de semestre chez MCC. Thomas Kayembe, directeur administratif et financier, coordonne trois chantiers : Ruth Mbuyi, comptable principale, prépare la clôture et constate que la balance générale 2025 transmise par un consultant ne s'équilibre pas ; Nadine Kapinga, contrôleuse de gestion, doit expliquer un dépassement de 3,8 MUSD sur le poste réactifs ; Olivier Kanku, fiscaliste, prépare le dossier de calcul des redevances minières et les données de la déclaration ITIE. Le comité d'audit se réunit dans dix jours.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Contrôler** une balance générale et réaliser une revue analytique avec Claude, par calculs programmés.
2. **Expliquer** des écarts budgétaires de manière chiffrée, traçable et nuancée.
3. **Préparer** un dossier de calcul fiscal (redevances) en distinguant calcul, hypothèses et textes applicables.
4. **Produire** des notes de gestion et des synthèses pour la direction et le comité d'audit.
5. **Appliquer** les règles de confidentialité et de séparation des tâches propres à la fonction financière.

### C. Comprendre avant de pratiquer — Profil du métier

En RDC, État membre de l'OHADA, la comptabilité des entreprises s'inscrit dans le cadre de l'Acte uniforme relatif au droit comptable et à l'information financière, adopté en 2017, et du système comptable révisé qui l'accompagne [@OHADA-AUDCIF]. Les entreprises extractives sont par ailleurs concernées par les exigences de déclaration des paiements aux États prévues par la Norme ITIE [@EITI-2023].

*Tableau 28.1 — Profil de la fonction finance.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Tenue des comptes, clôtures, états financiers, trésorerie, budget, contrôle de gestion, fiscalité, relations avec les auditeurs et l'administration fiscale |
| Tâches quotidiennes | Saisies et rapprochements, contrôles, analyses d'écarts, prévisions, déclarations, réponses aux auditeurs |
| Difficultés | Volumes ; délais de clôture ; réglementation fiscale minière complexe et évolutive ; multiples devises ; justification des écarts |
| Documents | Balances, grands livres, rapprochements, budgets, déclarations fiscales, contrats de vente, rapports ITIE, notes aux comités |
| Données | Écritures, budgets, prix des métaux, taux de change, volumes de production et de ventes |
| Livrables | États financiers, reportings mensuels, analyses d'écarts, déclarations, notes de gestion |
| Assistables par Claude | Contrôles de cohérence et revues analytiques (code) ; analyse d'écarts ; dossiers de calcul ; notes et synthèses ; préparation des questions des auditeurs |
| Limites | Comptabilisation définitive, arrêté des comptes, opinions, positions fiscales, déclarations signées ; données nominatives et bancaires |

::: attention
**Séparation des tâches et traçabilité.** Claude ne passe aucune écriture et n'a pas accès aux systèmes comptables en écriture. Toute analyse réalisée avec Claude qui sert de justification doit être conservée (données, prompt, résultat, contrôles) dans le dossier de travail, comme n'importe quel papier de travail.
:::

### D. Démonstration guidée — Cas d'usage

#### Cas d'usage 28.1 — Contrôle de la balance générale et revue analytique

**1. Problème.** La balance générale 2025 transmise ne s'équilibre pas ; Ruth doit trouver l'origine et réaliser une revue analytique avant la clôture.

**2. Méthode habituelle.** Totaux dans le tableur, pointage ligne par ligne.

**3. Contribution de Claude.** Contrôle d'équilibre par code, contrôles de cohérence (comptes de bilan et de gestion, sens des soldes), revue analytique (ratios, comparaisons avec le budget et l'activité), liste de questions.

**4. Données.** `MCC_balance_generale_2025.xlsx` (montants en MUSD, fictifs) ; chiffres d'activité du scénario.

**5–6. Procédure et prompt.**

```text
[C] Comptable principale de MCC ; clôture 2025.
[A] Contrôle la balance générale jointe et réalise une revue analytique.
[D] MCC_balance_generale_2025.xlsx (MUSD). Activité 2025 : ≈ 50 kt de cathodes, ≈ 4,5 kt Co ;
redevances calculées selon le dossier fiscal : 24 MUSD.
[R] Exécution de code. Ne propose aucune écriture de correction : liste des constats et questions.
[E] 1) Totaux débit/crédit et écart ; 2) comptes au solde inhabituel (sens, montant) ;
3) cohérences : chiffre d'affaires / production, redevances / chiffre d'affaires, dotation
aux amortissements / immobilisations ; 4) hypothèses d'origine de l'écart d'équilibre à vérifier ;
5) liste de questions au consultant.
```

**7. Échanges.** « Vérifie si l'écart correspond au montant d'un compte, au double d'un compte, ou à une inversion de sens » (techniques classiques de recherche d'écart).

**8. Exemple de résultat (fictif).** Total débit 980,4 MUSD, total crédit 997,1 MUSD : écart de 16,7 MUSD. Claude teste les hypothèses classiques (compte omis, compte saisi dans le mauvais sens — une inversion produirait un écart égal au double du solde —, erreur de transposition) et liste les comptes candidats ; Ruth vérifie dans le grand livre. Revue analytique : redevances de 24 MUSD pour un chiffre d'affaires de 549 MUSD, soit 4,4 % — cohérent avec le dossier fiscal.

**9. Contrôle.** Recalcul des totaux dans le tableur ; vérification des hypothèses dans le grand livre.

**10. Erreurs possibles.** Ligne « TOTAL » incluse dans les sommes (double comptage) ; confusion des unités (USD / MUSD).

**11. Limites.** Les corrections sont décidées et passées par la comptabilité selon les procédures.

**12. Livrable.** Note de contrôle de la balance et revue analytique, versées au dossier de clôture.

#### Cas d'usage 28.2 — Expliquer les écarts budgétaires du semestre

**1. Problème.** Les coûts du S1 2026 dépassent le budget ; le comité de direction veut des explications par centre de coût.

**2. Méthode habituelle.** Tableau d'écarts et commentaires recueillis auprès des responsables.

**3. Contribution de Claude.** Calcul des écarts cumulés, classement, décomposition (exemple de l'acide : effet prix / effet consommation, chapitre 21), commentaire de gestion distinguant causes établies et pistes.

**4. Données.** `MCC_budget_reel_S1_2026.xlsx` ; explications reçues des responsables.

**5–6. Prompt.** Reprenez le prompt CADRE du chapitre 10 (section D.2) ; ajoutez :

```text
Pour chaque centre de coût dont l'écart cumulé dépasse 0,3 MUSD, présente :
écart, explications reçues des responsables (citées), part chiffrée par les explications,
part non expliquée. Ne comble pas la part non expliquée par une hypothèse.
```

**7. Échanges.** « Prépare pour le comité un graphique des écarts cumulés et trois messages clés. »

**8. Exemple de résultat (fictif).**

![Figure 28.1 — Écarts budgétaires cumulés par centre de coût au premier semestre 2026 (données fictives MCC) : le poste réactifs concentre l'essentiel du dépassement. Graphique réalisé pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig28_1_ecarts_budget.png){width=90%}

Message clé (à valider) : « Le dépassement est concentré sur les réactifs de l'usine (≈ + 3,8 MUSD cumulés, essentiellement d'avril à juin). La hausse du prix de l'acide et une consommation supérieure au budget en expliquent environ 1 MUSD sur le trimestre ; le solde reste à expliquer avec l'usine et les achats (autres réactifs). La conformité de la hausse de prix au contrat est en cours d'examen. »

**9. Contrôle.** Recalcul des écarts ; vérification que la « part expliquée » repose sur des données.

**10. Erreurs possibles.** Additionner des pourcentages ; présenter une hypothèse comme une cause.

**11. Limites.** Les arbitrages (révision budgétaire, mesures d'économie) relèvent de la direction.

**12. Livrable.** Note d'écarts semestrielle et support du comité.

#### Cas d'usage 28.3 — Dossier de calcul des redevances minières (condensé)

Olivier fournit à Claude les textes applicables (Code minier modifié, textes d'application), les données de ventes et les taux retenus **après sa propre analyse**. Claude construit le dossier de calcul par code (assiette, taux, montants par substance et par période), le rapproche des montants comptabilisés et des paiements, et liste les points d'interprétation à confirmer. Dans le scénario (assiette simplifiée de l'exercice) : 3,5 % × 475 MUSD (cuivre) + 10 % × 74 MUSD (cobalt) = 16,6 + 7,4 = **24,0 MUSD**, cohérent avec la balance. Les taux et l'assiette réels doivent être vérifiés dans les textes en vigueur ; la position fiscale et la déclaration relèvent du fiscaliste et de la direction.

#### Cas d'usage 28.4 — Données pour la déclaration ITIE et coût unitaire (condensé)

Claude aide à rassembler, à partir des registres validés, les paiements à déclarer par flux et par entité publique selon le modèle fourni par le secrétariat national, avec rapprochement aux paiements bancaires. En contrôle de gestion, il calcule le coût unitaire (USD par livre de cuivre) à partir des coûts et de la production, et vérifie la cohérence avec les rapports mensuels (par exemple 2,02 USD/lb en mars 2026 contre 1,85 au budget, selon le rapport de mars).

### E. Prompts commentés

**Prompt 28.1 — Préparer les questions du comité d'audit**

```text
Voici le projet de note financière semestrielle : <note> … </note>.
Joue le rôle d'un membre exigeant du comité d'audit. Liste les 10 questions les plus probables,
classées par importance, et pour chacune les éléments de réponse disponibles dans la note
ou l'information manquante. N'invente pas de réponse.
```

*Commentaire.* Anticiper les questions est l'un des usages les plus rentables de Claude : il élargit votre angle de vue sans rien décider.

### F. Exercices pratiques

**Exercice 28.1 (guidé).** Réalisez le cas 28.1 ; calculez l'écart d'équilibre et proposez trois hypothèses d'origine.

**Exercice 28.2 (guidé).** Réalisez le cas 28.2 ; vérifiez à la main l'écart cumulé du poste réactifs.

**Exercice 28.3 (autonome).** Avec des données publiques (un rapport ITIE publié), construisez un tableau des paiements d'une entreprise par flux et commentez-le.

### G. Livrable professionnel

**Dossier financier semestriel** : contrôle de la balance, revue analytique, note d'écarts, dossier de calcul des redevances, questions anticipées du comité d'audit.

### H. Vérification des résultats

::: controle
- Tous les montants sont recalculés indépendamment (tableur) et rapprochés des sources.
- Les unités et devises sont explicites.
- Les explications d'écarts distinguent causes documentées et hypothèses.
- Les taux et assiettes fiscales proviennent des textes en vigueur, validés par le fiscaliste.
- Les analyses servant de justification sont archivées dans les dossiers de travail.
:::

::: setrompe
Interrogé « de mémoire » sur le taux de redevance d'une substance en RDC, un assistant peut citer un taux exact à une date passée, mais modifié depuis, ou confondre substances et catégories. **Contre-mesure** : en fiscalité, Claude calcule à partir des taux que vous lui fournissez après vérification ; il ne les choisit pas.
:::

### I. Limites et précautions

- Les données financières non publiées d'une société peuvent être des informations privilégiées.
- Les données bancaires et nominatives (salaires) exigent un niveau de protection élevé.
- Les opinions comptables, positions fiscales et états financiers relèvent des professionnels habilités et des organes de gouvernance.

### J. Boîte à outils

- Prompts des cas 28.1, 28.2 et prompt 28.1.
- Techniques de recherche d'écart d'équilibre : compte omis, inversion de sens (écart = double du solde), transposition de chiffres (écart divisible par 9).
- Gabarit de note d'écarts : centre | budget | réel | écart | % | explications documentées | part non expliquée | actions.

### K. Quiz

1. **(Calcul)** Quel est l'écart d'équilibre de la balance d'exercice (débit 980,4 ; crédit 997,1) ?
2. **(Compréhension)** Pourquoi une inversion de sens produit-elle un écart égal au double du solde ?
3. **(Vrai ou faux)** Claude peut passer les écritures de correction s'il a accès au système.
4. **(Calcul)** Calculez les redevances du scénario (3,5 % de 475 MUSD et 10 % de 74 MUSD).
5. **(QCM)** Quel référentiel encadre le droit comptable dans les États membres de l'OHADA ? a) GISTM ; b) l'Acte uniforme relatif au droit comptable et à l'information financière ; c) JORC ; d) ISO 42001.
6. **(Mise en situation)** Claude comble la part non expliquée d'un écart par « probablement des effets de change ». Que faites-vous ?
7. **(Vrai ou faux)** Une analyse réalisée avec Claude et servant de justification doit être archivée comme papier de travail.
8. **(Compréhension)** Pourquoi demander à Claude d'anticiper les questions du comité d'audit ?
9. **(Analyse critique)** Quels risques présente l'usage de taux fiscaux fournis de mémoire par Claude ?
10. **(Application)** Quel ratio redevances / chiffre d'affaires obtient-on dans le scénario ?

<div class="carnet" titre="Chapitre 28 — Claude appliqué à la comptabilité, à la finance, à la fiscalité et au contrôle de gestion"></div>
