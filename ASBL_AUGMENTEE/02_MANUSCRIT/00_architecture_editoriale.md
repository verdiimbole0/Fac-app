# Architecture éditoriale détaillée : ASBL AUGMENTÉE

*Document de travail interne. Il n'est pas inclus dans le manuscrit compilé.*

## 1. Promesse, lecteur et principe directeur

**Promesse :** permettre à tout acteur d'une ASBL, même sans formation informatique, de comprendre l'IA, de savoir l'utiliser et de participer concrètement à la transformation de son organisation.

**Principe directeur (ligne éditoriale) :** *problème → méthode → application → contrôle.* Aucune fonctionnalité n'est annoncée sans montrer : les données d'entrée, les étapes, le partage des rôles (IA / logiciel / humain), les contrôles et les risques.

**Choix structurants :**

1. **Monnaie neutre.** Tous les montants sont exprimés en « UM » (unité monétaire fictive) pour garder une portée internationale.
2. **Outils décrits par catégories.** Les outils sont décrits par familles (assistant conversationnel, tableur, plateforme d'automatisation sans code, OCR, ERP, etc.). Les noms commerciaux ne sont cités qu'à titre d'exemples notoires, sans prix ni promesse de fonctionnalité, car l'offre évolue très vite.
3. **Résultats hypothétiques signalés.** Toute réponse d'IA reproduite est marquée « exemple de résultat attendu (illustratif) ». Aucune n'est présentée comme une sortie réellement obtenue.
4. **Quatre organisations fictives servent de fil rouge** (voir § 3).
5. **Trois niveaux d'implémentation** (Débutant / Intermédiaire / Avancé) présentés dans un tableau normalisé.
6. **Encadrés normalisés** (sans surcharge) :
   - 🔎 *À retenir*
   - ⚖️ *Adaptation réglementaire* (limites territoriales)
   - 🛑 *Contrôle humain obligatoire*
   - 📶 *Faible connectivité*

## 2. Gabarits

### 2.1 Gabarit de module (18 rubriques du cahier des charges)

1. Mise en situation · 2. Problématique · 3. Objectifs d'apprentissage · 4. Notions et définitions · 5. Explications détaillées · 6. Illustrations · 7. Application professionnelle (méthode A→U) · 8. Processus de mise en œuvre · 9. Solutions par niveau · 10. Outils nécessaires · 11. Prompts prêts à l'emploi (fiche A→K) · 12. Résultats attendus · 13. Contrôles humains · 14. Risques et erreurs à éviter · 15. Exercice pratique · 16. Synthèse · 17. QCM (≥ 10 questions) · 18. Corrigé détaillé et barème.

Pour éviter la redondance dans les modules théoriques (1, 2, 4), les rubriques 7 à 12 peuvent être regroupées en une seule section « Application » lorsque cela sert la clarté ; aucune n'est supprimée.

### 2.2 Gabarit « Fiche prompt » (A→K)

A. Titre · B. Objectif · C. Contexte d'utilisation · D. Données nécessaires · E. Prompt complet · F. Instructions d'utilisation · G. Résultat attendu · H. Exemple d'application · I. Méthode de vérification · J. Précautions · K. Amélioration (version 1 → défauts → version 2).

### 2.3 Gabarit « Application métier » (A→U)

A. Contexte · B. Problème · C. Symptômes · D. Causes profondes · E. Processus actuel · F. Faiblesses · G. Résultat recherché · H. Pertinence de l'IA · I. Alternatives sans IA · J. Solution · K. Niveau · L. Outils · M. Étapes · N. Prompt/automatisation · O. Exemple de résultat · P. Vérification · Q. Contrôles humains · R. Risques · S. Coûts et maintenance · T. Indicateurs · U. Amélioration continue.

### 2.4 Règles du QCM

10 questions minimum, 4 propositions (a–d), consigne indiquant « une seule » ou « une ou plusieurs » bonnes réponses ; corrigé regroupé après les questions ; 2 points par question (barème /20) ; tout ou rien pour les questions à réponses multiples ; niveaux : 0–9 à consolider, 10–13 en progression, 14–17 maîtrise opérationnelle, 18–20 maîtrise avancée.

## 3. Organisations fictives (fil rouge)

| Nom | Taille | Contexte | Usage dans l'ouvrage |
|---|---|---|---|
| **Lumière des Collines** | 6 salariés, 30 bénévoles, budget ≈ 180 000 UM | Soutien scolaire, zone semi-rurale, connexion intermittente, un ordinateur partagé, smartphones | Solutions de niveau Débutant ; faible connectivité |
| **Fondation Horizons Partagés** | 60 salariés, 4 bureaux, budget ≈ 3,2 M UM, 5 bailleurs | Santé communautaire, multiprojets, comptabilité sur logiciel, reporting lourd | Fil rouge principal ; niveau Intermédiaire |
| **Réseau Citoyen pour l'Eau (RCE)** | 300 salariés, 3 pays, ERP | Eau et assainissement, achats importants, audits multiples | Niveau Avancé ; contrôle interne, achats, RAG |
| **Maison des Aînés Solidaires** | 12 salariés, 80 bénévoles | Services aux personnes âgées, ville d'un pays à revenu élevé, réglementation stricte des données | Bénévoles, données sensibles, communication |

## 4. Sommaire détaillé et cas pratiques

| Module | Démonstration principale | Fiches prompts | Figures |
|---|---|---|---|
| **Liminaires** | Parcours de lecture | Néant | Fig. 0.1 Carte des parcours |
| **M1** IA : comprendre une révolution | Une journée de Mariam, coordinatrice, avant/après | P1.1 Expliquer l'IA à son conseil | 1.1 Frise ; 1.2 Familles d'IA |
| **M2** Fonctionnement réel | Suivre une question à travers un LLM et un RAG | P2.1 Tester les limites d'un assistant | 2.1 De la donnée au modèle ; 2.2 Architecture RAG |
| **M3** Utiliser et maîtriser les outils | Méthode CADRE de rédaction de prompts | P3.1 Synthèse de document ; P3.2 Analyse de tableur ; P3.3 Traduction contrôlée | 3.1 Anatomie d'un prompt ; 3.2 Boucle de vérification |
| **M4** Comprendre une ASBL moderne | Radiographie d'Horizons Partagés | P4.1 Cartographier les parties prenantes | 4.1 Organigramme type ; 4.2 Cycles |
| **M5** Diagnostiquer et cartographier | Diagnostic du circuit des dépenses | P5.1 Transformer un entretien en carte de processus | 5.1 Processus « as-is » ; 5.2 Arbre des causes |
| **M6** Identifier les opportunités | Matrice de sélection appliquée à 8 cas d'usage | P6.1 Fiche d'opportunité | 6.1 Matrice valeur/faisabilité ; 6.2 Arbre « IA ou pas IA ? » |
| **M7** Les données | Plan de classement et règles de nommage | P7.1 Nettoyer une liste de bénéficiaires | 7.1 Cycle de vie des données ; 7.2 Arborescence |
| **M8** Éthique, sécurité, réglementation | Classification des données et feu tricolore | P8.1 Anonymiser avant envoi ; P8.2 Revue de biais | 8.1 Feu tricolore des données ; 8.2 Supervision humaine |
| **M9** Choisir les outils | Comparaison de 3 architectures | P9.1 Questionnaire fournisseur | 9.1 Trois niveaux ; 9.2 Grille de sélection |
| **M10** Gouvernance | De la réunion au suivi des décisions | P10.1 PV ; P10.2 Registre de décisions ; P10.3 Ordre du jour | 10.1 Flux réunion→décision |
| **M11** Programmes et projets | Du problème communautaire au cadre logique | P11.1 Arbre à problèmes ; P11.2 Cadre logique ; P11.3 Rapport | 11.1 Arbre problèmes/objectifs ; 11.2 Chaîne de résultats |
| **M12** Comptabilité et finances | **Facture en 14 étapes** ; rapprochement ; écarts budgétaires | P12.1 Extraction ; P12.2 Imputation ; P12.3 Écarts | 12.1 Circuit facture ; 12.2 Tableau de bord |
| **M13** Audit et contrôle interne | Fichier de 40 dépenses → anomalies → feuille de travail | P13.1 Tests analytiques ; P13.2 Feuille de travail ; P13.3 Recommandations | 13.1 Tests ; 13.2 Carte des risques |
| **M14** RH et bénévoles | Recrutement d'un(e) chargé(e) S&E ; parcours d'intégration | P14.1 Fiche de poste ; P14.2 Grille d'entretien ; P14.3 Planning bénévoles | 14.1 Recrutement assisté |
| **M15** Financements | Analyse d'un appel à projets fictif → note conceptuelle | P15.1 Éligibilité ; P15.2 Note conceptuelle ; P15.3 Budget | 15.1 Entonnoir d'opportunités |
| **M16** Achats et logistique | Demande d'achat → consultation → tableau comparatif → inventaire | P16.1 Tableau comparatif ; P16.2 Rapprochement réception | 16.1 Circuit achats |
| **M17** Communication | Programme décrit → calendrier éditorial 3 mois | P17.1 Calendrier ; P17.2 Déclinaison multicanal | 17.1 Chaîne éditoriale |
| **M18** Bénéficiaires et terrain | Mécanisme de plaintes multilingue | P18.1 Classification des retours ; P18.2 Rapport de terrain | 18.1 Boucle de redevabilité |
| **M19** Déploiement de bout en bout | Projet « assistant de procédures » d'Horizons Partagés | P19.1 Cahier des charges ; P19.2 Jeu de tests | 19.1 Cycle projet IA |
| **M20** Changement et pérennité | Adoption, gouvernance, maintenance | P20.1 Plan de formation | 20.1 Courbe d'adoption ; 20.2 Comité IA |
| **M21** 10 études de cas | Cas 1 à 10 | Néant | 21.1 Synthèse des cas |
| **M22** Plan de transformation | Plan 90 jours de Lumière des Collines | P22.1 Feuille de route | 22.1 Plan 90 jours |

## 5. Transitions entre parties

- Partie I → II : « Vous savez ce que l'IA peut et ne peut pas faire ; encore faut-il savoir où elle serait utile chez vous. »
- Partie II → III : « Vous avez identifié des priorités ; avant d'agir, il faut des données propres, des règles et des outils adaptés. »
- Partie III → IV : « Le terrain est préparé ; place aux métiers. »
- Partie IV → V : « Une démonstration ne fait pas une solution durable. »
- Partie V → VI : « Passons à l'entraînement sur des cas complets, puis à votre propre plan. »

## 6. Volume cible

Environ 65 000 à 80 000 mots hors annexes, selon les besoins réels de chaque module. Les modules métier (10 à 18) sont les plus développés.
