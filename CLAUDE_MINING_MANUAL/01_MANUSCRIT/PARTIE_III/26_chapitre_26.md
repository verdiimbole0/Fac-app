## Chapitre 26 — Claude appliqué aux achats, aux approvisionnements et à la logistique minière

### A. Mise en situation professionnelle

Amina Lukusa, responsable supply chain de MCC, prépare trois dossiers en parallèle : la renégociation du contrat d'acide sulfurique (livraisons insuffisantes en mars, hausse de prix contestable), l'appel d'offres pour le transport des cathodes vers Dar es Salaam, et la revue annuelle des dépenses par fournisseur demandée par le directeur financier. Elle doit aussi rendre compte de la part des achats réalisés auprès d'entreprises locales, sujet très attendu par les communautés et l'administration.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Analyser** les dépenses par fournisseur, catégorie et délai, et repérer les anomalies.
2. **Lire** un contrat d'approvisionnement avec Claude et préparer une réclamation fondée.
3. **Rédiger** un cahier des charges et une grille d'évaluation des offres.
4. **Structurer** la documentation logistique d'une expédition à l'export.
5. **Préparer** un rapport sur les achats locaux à partir de données vérifiées.

### C. Comprendre avant de pratiquer — Profil du métier

*Tableau 26.1 — Profil de la fonction achats, approvisionnements et logistique.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Sourcing, contrats, approvisionnement en réactifs, pièces et services, gestion des stocks, transport amont et aval, conformité |
| Tâches quotidiennes | Demandes d'achat, consultations, commandes, relances, réceptions, litiges, suivi des expéditions |
| Difficultés | Délais longs (sites isolés, corridors routiers) ; ruptures critiques (pièces, réactifs) ; fraude et fractionnement ; documentation douanière ; exigences de contenu local |
| Documents | Demandes d'achat, bons de commande, contrats, offres, factures, bons de livraison, documents de transport et de douane |
| Données | Historique des commandes, prix, délais, stocks, performance des fournisseurs, suivi des camions |
| Livrables | Analyses de dépenses, dossiers d'appel d'offres, contrats, rapports de performance, rapports de contenu local |
| Assistables par Claude | Analyse des dépenses (code) ; lecture de contrats ; cahiers des charges ; grilles d'évaluation ; projets de courriers ; check-lists documentaires |
| Limites | Attribution des marchés ; négociation ; signature ; décisions de litige ; conformité douanière (spécialistes et transitaires) |

::: attention
L'évaluation et l'attribution des marchés exigent impartialité et traçabilité. Claude peut structurer une grille et vérifier la cohérence d'une notation ; il ne choisit pas le fournisseur. Ne transmettez jamais les offres confidentielles d'un soumissionnaire hors de l'environnement autorisé.
:::

### D. Démonstration guidée — Cas d'usage

#### Cas d'usage 26.1 — Revue annuelle des dépenses et détection d'anomalies

**1. Problème.** Le directeur financier veut une vue claire des dépenses par fournisseur et catégorie, et l'assurance que les règles d'approbation sont respectées.

**2. Méthode habituelle.** Exports de l'ERP retraités dans un tableur ; contrôles d'anomalies rares.

**3. Contribution de Claude.** Analyse des dépenses par code, concentration des fournisseurs, délais moyens, détection des fractionnements potentiels et des doublons.

**4. Données.** `MCC_bons_de_commande.csv` ; seuil d'approbation du chef de service : 10 000 USD.

**5–6. Procédure et prompt.**

```text
Fichier joint : MCC_bons_de_commande.csv. Avec l'exécution de code :
1. Dépenses totales par fournisseur et par article ; part des 3 premiers fournisseurs.
2. Délai de livraison moyen et maximal par fournisseur.
3. Signalements : (a) commandes d'un même fournisseur le même jour dont la somme dépasse
   10 000 USD alors que chacune est inférieure ; (b) commandes identiques (fournisseur, article,
   quantité, prix, date) ; (c) prix unitaires s'écartant de plus de 15 % de la médiane de l'article.
4. Histogramme des montants autour du seuil de 10 000 USD.
Les signalements sont des points à vérifier, pas des conclusions.
```

**7. Échanges.** « Pour les signalements (a), prépare la demande de justification au service demandeur » ; « Quelle part des dépenses va à des fournisseurs enregistrés en RDC ? » (si l'information est disponible dans les données).

**8. Exemple de résultat (données fictives).** Trois commandes de 9 800 USD passées le 14 mars 2026 à un même prestataire, pour un total de 29 400 USD ; une commande en double (BC-60999 identique à BC-60012).

![Figure 26.1 — Distribution des montants de commandes autour du seuil d'approbation (données fictives MCC). Graphique réalisé pour cet ouvrage.](02_ILLUSTRATIONS/GRAPHIQUES/fig26_1_commandes_seuil.png){width=90%}

**9. Contrôle.** Vérification des pièces dans l'ERP ; entretien avec le demandeur ; transmission à l'audit interne si nécessaire (chapitre 29).

**10. Erreurs possibles.** Faux positifs (commandes légitimement distinctes) ; prix unitaires comparés entre unités différentes.

**11. Limites.** Un signalement n'est pas une fraude ; l'instruction suit la procédure de l'entreprise.

**12. Livrable.** Revue des dépenses avec annexe des signalements et suites données.

#### Cas d'usage 26.2 — Réclamation au fournisseur d'acide

**1. Problème.** En mars 2026, Kat-Chem (fictif) n'a livré que 5 100 t au lieu du minimum contractuel de 5 400 t ; par ailleurs, le prix facturé à partir d'avril (228 USD/t) représente une hausse de 23 % par rapport au prix de base (185 USD/t).

**2. Méthode habituelle.** Lecture du contrat, calcul manuel, courrier rédigé avec le juridique.

**3. Contribution de Claude.** Extraction des clauses applicables avec citations, calcul de la pénalité, comparaison de la hausse avec le plafond de révision, projet de courrier.

**4. Données.** `MCC_contrat_fourniture_acide_extrait` ; bons de livraison de mars ; factures d'avril.

**5–6. Procédure et prompt.**

```text
[C] Responsable supply chain de MCC. Le fournisseur d'acide a livré 5 100 t en mars 2026
et facture 228 USD/t depuis avril (prix de base 185 USD/t).
[A] Prépare l'analyse contractuelle et un projet de courrier de réclamation.
[D] Contrat joint (extrait). Facturation de mars : 1 020 000 USD.
[R] Cite exactement les articles utilisés. Calcule la pénalité selon l'article 9 et vérifie
le plafond. Pour la révision de prix, indique ce que dit l'article 5 et ce qui manque pour conclure
(valeurs de l'indice S). Ton ferme et courtois ; aucune menace juridique ; validation par le juriste.
[E] 1) Tableau des clauses ; 2) calculs ; 3) points à vérifier ; 4) projet de courrier d'une page.
```

**7. Échanges.** « Quels arguments le fournisseur pourrait-il avancer (force majeure, pénurie) et que dit l'article 12 ? »

**8. Exemple de résultat.** Pénalité : (5 400 − 5 100) × 8 = 2 400 USD, sous le plafond de 5 % de la facturation mensuelle (51 000 USD). Révision de prix : l'article 5 plafonne la révision à ± 15 % par trimestre ; une hausse de 23 % dépasse ce plafond, sauf si plusieurs révisions trimestrielles successives sont intervenues — point à vérifier avec l'historique des prix et les valeurs de l'indice. L'article 12 précise que les pénuries chez les sous-traitants du fournisseur ne constituent pas un cas de force majeure.

**9. Contrôle.** Relecture du contrat complet (l'extrait peut omettre des clauses pertinentes) ; validation par Me Ngoy.

**10. Erreurs possibles.** Raisonner sur un extrait incomplet ; mauvaise assiette de la pénalité.

**11. Limites.** L'analyse juridique engageante et l'envoi du courrier relèvent du juriste et de la direction.

**12. Livrable.** Note d'analyse contractuelle et courrier validé.

#### Cas d'usage 26.3 — Appel d'offres pour le transport des cathodes (condensé)

Claude rédige le projet de cahier des charges (périmètre : site → Dar es Salaam via la frontière zambienne ; exigences de sécurité routière, de suivi des camions, d'assurance, de documentation ; indicateurs de performance), une grille d'évaluation pondérée (technique, sécurité, prix, contenu local) et la liste des pièces à exiger. Après réception des offres, il peut vérifier la complétude de chaque dossier par rapport à la liste et la cohérence arithmétique des grilles remplies par le comité. Le comité d'évaluation note et décide.

#### Cas d'usage 26.4 — Dossier documentaire d'une expédition à l'export (condensé)

Claude produit une check-list des documents d'une expédition de cathodes (contrat de vente, facture, liste de colisage, certificats d'analyse et de poids, documents de transport, déclarations et autorisations d'exportation applicables) et vérifie la **cohérence** des documents fournis entre eux (poids, nombre de lots, références). La liste exacte des documents réglementaires est validée par le transitaire et le service juridique.

### E. Prompts commentés

**Prompt 26.1 — Grille d'évaluation des offres**

```text
Propose une grille d'évaluation des offres pour [objet du marché], avec : critères, sous-critères,
pondérations (total 100), barème de notation par critère (avec description des niveaux),
critères éliminatoires. Contraintes de l'entreprise : sécurité ≥ 25 % ; prix ≤ 40 % ;
contenu local évalué. Justifie chaque pondération en une phrase.
```

*Commentaire.* Les contraintes de pondération viennent de la politique d'achats de l'entreprise ; Claude organise et justifie, il ne fixe pas la politique.

### F. Exercices pratiques

**Exercice 26.1 (guidé).** Réalisez le cas 26.1 ; retrouvez les deux types d'anomalies insérées dans les données.

**Exercice 26.2 (guidé).** Réalisez le cas 26.2 ; vérifiez à la main la pénalité et le pourcentage de hausse du prix.

**Exercice 26.3 (autonome).** Préparez le cahier des charges et la grille d'évaluation d'un marché de votre site.

### G. Livrable professionnel

**Dossier supply chain trimestriel** : revue des dépenses et signalements, analyse des contrats clés, état des appels d'offres, rapport sur les achats locaux.

### H. Vérification des résultats

::: controle
- Les calculs (pénalités, pourcentages, totaux) sont recalculés.
- Les clauses citées sont vérifiées dans le contrat complet.
- Les signalements d'anomalies sont instruits selon la procédure, sans accusation.
- La confidentialité des offres est respectée.
:::

::: setrompe
Sur la base d'un extrait de contrat, Claude conclut que « le fournisseur doit rembourser l'intégralité de la hausse ». Or l'extrait ne contient ni les valeurs de l'indice, ni d'éventuels avenants. **Contre-mesure** : demander explicitement « ce qui manque pour conclure ».
:::

### I. Limites et précautions

- Les décisions d'attribution, de résiliation et de litige relèvent des instances habilitées.
- Les règles douanières et fiscales évoluent : vérifiez-les auprès des autorités et des transitaires.
- Les données fournisseurs et les offres sont confidentielles.

### J. Boîte à outils

- Prompts des cas 26.1, 26.2 et prompt 26.1.
- Tests d'anomalies d'achats : fractionnement, doublons, prix atypiques, fournisseurs récents à fort volume, commandes postérieures aux factures.
- Modèle de courrier de réclamation (Annexe D).

### K. Quiz

1. **(Calcul)** Quelle pénalité pour 5 100 t livrées (minimum 5 400 t ; 8 USD/t) ?
2. **(Calcul)** De combien de pour cent le prix de l'acide a-t-il augmenté (185 → 228 USD/t) ?
3. **(Vrai ou faux)** Trois commandes de 9 800 USD au même fournisseur le même jour prouvent une fraude.
4. **(QCM)** Qui attribue un marché ? a) Claude selon la grille ; b) le comité d'évaluation selon la procédure ; c) le soumissionnaire le moins cher automatiquement ; d) le transitaire.
5. **(Compréhension)** Pourquoi faut-il relire le contrat complet et pas seulement l'extrait ?
6. **(Mise en situation)** Le fournisseur invoque une pénurie chez son propre fournisseur. Que dit l'article 12 ?
7. **(Application)** Citez trois documents d'une expédition de cathodes à l'export.
8. **(Vrai ou faux)** Une grille d'évaluation doit comporter des critères éliminatoires explicites.
9. **(Analyse critique)** Pourquoi comparer des prix unitaires peut-il produire de faux signalements ?
10. **(Compréhension)** Qu'apporte Claude dans la vérification d'un dossier d'expédition ?

<div class="carnet" titre="Chapitre 26 — Claude appliqué aux achats, aux approvisionnements et à la logistique minière"></div>
