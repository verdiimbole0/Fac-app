# LA TRÉSO SOUS CONTRÔLE : rapport de contrôle qualité

Date du contrôle : 24 novembre 2026. Rendu de référence : PDF exporté par LibreOffice à partir du fichier Word.

## 1. Chiffres clés

| Élément | Résultat |
|---|---|
| Format | A5 (148 × 210 mm), vérifié dans le PDF (419,6 × 595,3 points) |
| Nombre de pages intérieures | **121** (limite : 130 ; cible : 124) |
| Chapitres | 12, répartis en 4 parties |
| QCM | 60 questions (5 par chapitre), 60 corrigés justifiés |
| Rubriques « Votre prochaine action » | 12 |
| Tableaux numérotés / figures | 32 tableaux numérotés ; 12 figures |
| Prompts IA structurés (7 rubriques) | 10 |
| Modèles Excel | 10 modèles, en 10 fichiers séparés et 1 classeur combiné |
| Références bibliographiques | 13, toutes vérifiées par recherche (voir limites) |
| Entrées d'index | 69, numéros de page générés automatiquement à partir du PDF |

## 2. Suivi du nombre de pages

| Section | Cible | Réalisé |
|---|---:|---:|
| Pages liminaires et guide de lecture | 8 | 7 |
| Partie I | 14 | 17 |
| Partie II | 25 | 32 |
| Partie III | 22 | 21 |
| Partie IV | 28 | 28 |
| Conclusion et éléments complémentaires | 27 | 16 |
| **Total** | **124** | **121** |

Détail des éléments complémentaires : conclusion 1 p. (cible 2), plan d'action 2 p. (3), annexes 5 p. (10), glossaire 3 p. (3), bibliographie 2 p. (4), index 2 p. (2), crédits 1 p. (2), auteur 1 p. (1). Les parties I et II dépassent leur cible parce que les méthodes de base (diagnostic, prévisionnel, encaissements, décaissements) exigent des exemples chiffrés complets ; la compensation porte sur des éléments complémentaires plus courts que prévu. Les annexes donnent colonnes, formules, consignes et exemples ; leur version complète est dans les fichiers Excel.

## 3. Tests de cohérence réalisés

- **Fichier central de données** (`data/fil_rouge.py`) : toutes les valeurs du livre sont calculées par ce fichier ; les tableaux chiffrés du livre sont générés à partir de lui, sans saisie manuelle. 11 assertions automatiques vérifient notamment : résultat T4 et passage résultat-trésorerie (+28 000 à -55 000 USD), disponibilités = 15 000 USD, balance âgée = 126 000 USD, dettes = 92 000 USD, cohérence des prévisions de janvier avec le réalisé, rapprochement bancaire équilibré, créances au 31/01, budget du projet ASBL = 50 000 USD.
- **Vérification indépendante par tableur** : les 11 classeurs ont été recalculés par LibreOffice : 0 erreur de formule sur 430 formules (classeur combiné). 100 contrôles comparent les valeurs recalculées aux chiffres du livre (soldes du budget, 13 clôtures et 13 points bas du prévisionnel calculés par SOMME.SI.ENS et MIN.SI.ENS, balance âgée, DSO, rapprochement, indicateurs du tableau de bord, analyse des écarts) : 0 écart.
- **Contrôle du texte** : chiffres cités dans la prose relus contre les sorties du fichier central (points bas -19 513, -16 000, -6 763, -18 930 USD ; scénarios ; mission du chapitre 12). Arrondis harmonisés à l'arrondi commercial.
- **Renvois** : tous les renvois « tableau x.y » pointent vers un tableau existant ; numérotation des figures conforme au registre.
- **Typographie** : aucun tiret cadratin (—) ni demi-cadratin (–) dans le texte ; espaces insécables avant la ponctuation haute et dans les nombres.
- **Mise en page** : détection automatique des titres d'encadrés isolés en bas de page (0 restant) et des pages quasi vides (0) ; revue visuelle de toutes les pages.
- **Fichier Word** : validation du schéma OOXML réussie (« All validations PASSED »).

## 4. Licences des illustrations

12 illustrations, toutes créations originales (schémas et graphiques Matplotlib construits à partir des données fictives du livre). Aucune photographie, aucune image générée par IA : statut des licences sans réserve. Polices sous SIL Open Font License 1.1.

## 5. Limites et anomalies non résolues

1. **Photographies** : l'accès réseau aux banques d'images (Pexels, Wikimedia Commons, Unsplash) était bloqué et l'ouverture de ces hôtes a été refusée ; le livre ne contient donc aucune photographie. Des photographies peuvent être ajoutées ultérieurement, après vérification de leur licence.
2. **Sources officielles** : les sites officiels n'étaient pas accessibles directement ; les références ont été vérifiées par recherche web indexant ces pages. Le texte du SYCEBNL a été contrôlé sur une transcription structurée de l'Acte uniforme. Les documents payants (COSO 2013, ISO 31000) n'ont pas été lus intégralement.
3. **Polices dans le fichier Word** : Montserrat et Source Sans 3 sont intégrées au PDF, mais pas au fichier Word. Elles doivent être installées (gratuites, Google Fonts) pour que Word affiche la mise en page prévue.
4. **Pagination Word** : le sommaire et l'index portent les numéros de page du rendu PDF. Word peut paginer légèrement différemment ; vérifier ces numéros si le fichier Word est réexporté.
5. **Simplifications pédagogiques assumées** et signalées dans le texte : montants hors TVA ; taux d'intérêt, frais bancaires, échéance d'impôt du chapitre 12 et taux de change (2 850 CDF pour 1 USD) fictifs.
6. **Relecture** : relecture humaine professionnelle (orthographe, style) et vérification juridique de la page de droits recommandées avant commercialisation. L'année © 2026 est à ajuster selon la date de publication.
7. **Couverture** : non réalisée, conformément au cahier des charges.
