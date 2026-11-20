# Registre des sources : ASBL AUGMENTÉE

Date d'établissement : 20 novembre 2026
Responsable éditorial : Verdi Imbole (validation finale requise)

## 1. Méthode

Chaque source a été recherchée en ligne le 20 novembre 2026 afin de confirmer son existence, son titre, sa date, son éditeur, son identifiant (URL officielle, DOI ou ISBN) et sa nature. Le fichier `sources_verifiees.csv` contient les champs exigés par le cahier des charges (auteur, titre exact, date, éditeur, URL/DOI, nature, statut normatif, date de consultation, affirmations soutenues, modules).

**Limite de la session de production.** L'environnement de production ne permettait pas de télécharger directement les pages officielles : la vérification s'est appuyée sur un moteur de recherche et sur la concordance de plusieurs sources (site de l'institution émettrice, communiqués officiels, catalogues de bibliothèques, éditeurs). Le texte intégral des normes payantes (ISO/IEC 42001, COSO) n'a pas été consulté et n'est jamais reproduit. Aucune citation littérale longue n'est utilisée dans le manuscrit : les références sont paraphrasées et doivent être relues par l'auteur avant publication.

### Niveaux de vérification

| Code | Signification | Usage autorisé dans le manuscrit |
|---|---|---|
| **V2** | Existence et métadonnées principales confirmées par au moins deux sources concordantes, dont idéalement l'institution émettrice | Citation dans le texte et la bibliographie |
| **V1** | Existence confirmée, mais un élément (DOI, ISBN, éditeur, référence officielle) reste à vérifier | Citation possible avec mention prudente ; élément manquant signalé dans le contrôle bibliographique |
| **Écartée** | Source introuvable, incertaine ou ne soutenant pas l'affirmation visée | Interdite |

## 2. Sources écartées ou non retenues

| Élément envisagé | Motif d'exclusion |
|---|---|
| Code de document « SHS/BIO/PI/2021/1 » pour la Recommandation UNESCO | Non confirmé par la recherche ; seule la référence UNESDOC est conservée |
| Statistiques générales d'adoption de l'IA par les ONG issues d'enquêtes commerciales | Périmètres et méthodologies non vérifiables dans le cadre de cette session ; aucun pourcentage d'adoption n'est cité |
| Chiffres de « gains de productivité » génériques | Écartés ; seuls les résultats de S25 et S26 sont évoqués, de façon qualitative et avec leur périmètre |
| « Code de conduite humanitaire de l'IA » (NetHope) | Processus en cours selon les sources ; aucune version finale identifiée |
| Prix d'abonnement des outils d'IA | Non cités : les prix changent fréquemment ; le lecteur est invité à consulter les pages tarifaires officielles à la date de son projet |
| Fonctionnalités détaillées d'outils commerciaux nommés | Non décrites de façon nominative ; l'ouvrage décrit des **catégories d'outils** et des critères de choix, afin de ne pas présenter des fonctionnalités non vérifiées ou obsolètes |

## 3. Correspondance affirmations ↔ sources (extrait des affirmations sensibles)

| Affirmation dans le manuscrit | Source | Module |
|---|---|---|
| La Recommandation de l'UNESCO sur l'éthique de l'IA a été adoptée en novembre 2021 par les États membres | S01 | M1, M8 |
| Les Principes de l'OCDE sur l'IA (2019) ont été révisés en mai 2024, notamment pour tenir compte de l'IA générative | S02 | M1, M8 |
| Le NIST AI RMF 1.0 (janvier 2023) est volontaire et s'organise en quatre fonctions : gouverner, cartographier, mesurer, gérer | S03 | M8, M20 |
| Le profil IA générative du NIST (juillet 2024) identifie 12 risques | S04 | M8 |
| ISO/IEC 42001:2023 spécifie les exigences d'un système de management de l'IA et est certifiable | S05 | M8, M20 |
| Le règlement (UE) 2024/1689 est entré en vigueur le 1er août 2024 ; ses obligations s'appliquent de façon échelonnée | S06 | M8 |
| Un règlement « omnibus » de 2026 a reporté certaines obligations relatives aux systèmes à haut risque | S07 (V1) | M8 : formulation prudente |
| Le cadre COSO 2013 comprend cinq composantes et dix-sept principes | S11 | M5, M13 |
| Les Normes internationales d'audit interne de l'IIA sont en vigueur depuis le 9 janvier 2025 | S12 | M13 |
| Un référentiel comptable international pour les OSBL (INPAS) a été lancé en octobre 2025 ; il est volontaire sauf adoption locale | S13 | M12 |
| Les critères d'évaluation du CAD de l'OCDE sont au nombre de six depuis 2019 | S14 | M11 |
| Dans l'étude ACFE 2024 (1 921 cas, 138 pays et territoires, janv. 2022–sept. 2023), 43 % des fraudes ont été détectées par un signalement | S30 | M13 |
| Selon l'AIE, les centres de données ont consommé environ 415 TWh en 2024 (≈ 1,5 % de l'électricité mondiale), avec une projection d'environ 945 TWh en 2030 dans le scénario de base | S31 | M8 |
| L'injection de prompt figure au premier rang du Top 10 OWASP pour les applications LLM (version 2025) | S32 | M8, M9 |
| Les grands modèles de langage reposent sur l'architecture Transformer introduite en 2017 | S21 | M2 |
| Le RAG associe un modèle génératif et une recherche dans une base documentaire | S22 | M2 |
| Les hallucinations désignent des contenus générés non fidèles à la source ou aux faits | S23 | M2 |
| Dans une expérience menée auprès de 758 consultants, l'IA a amélioré la performance sur certaines tâches et l'a dégradée sur d'autres | S25 | M1, M3 |

## 4. Points à confirmer par l'auteur avant publication

1. S07 : référence ELI exacte et dates définitives du règlement (UE) 2026/1744, y compris le calendrier de l'article 50.
2. S08 : relecture de l'article 22 du RGPD avant toute paraphrase détaillée.
3. S09 et S10 : état des ratifications et d'entrée en vigueur à la date de publication.
4. S13 : adresse officielle du site de l'INPRF et intitulé exact des documents d'accompagnement.
5. S15, S23, S26, S29 : confirmation des DOI.
6. S34 à S38 : ISBN et éditeurs des éditions effectivement consultées (ouvrages d'inspiration, non cités comme preuves).

## 5. Règle de mise à jour

Toute nouvelle source ajoutée au manuscrit doit d'abord être inscrite dans `sources_verifiees.csv` avec son niveau de vérification. Une source V1 ne peut pas être la seule base d'une affirmation chiffrée.
