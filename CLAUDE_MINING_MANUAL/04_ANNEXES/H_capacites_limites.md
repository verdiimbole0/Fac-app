## Annexe H — Tableau récapitulatif des capacités et limites de Claude

*État au 16 novembre 2026, d'après la documentation officielle d'Anthropic (voir Annexe I). Les valeurs chiffrées évoluent : vérifiez-les avant toute décision.*

### H.1. Caractéristiques techniques des modèles actuels

| Élément | Valeur documentée | Source |
|---|---|---|
| Modèles actuels | Claude Fable 5.2, Opus 5.5, Sonnet 5.5, Haiku 5.5 | [@ANT-MODELS] |
| Modèle conseillé par défaut | Claude Opus 5.5 | [@ANT-MODELS] |
| Entrées / sorties | Texte et images en entrée ; texte en sortie ; multilingue ; utilisation d'outils | [@ANT-MODELS] |
| Fenêtre de contexte | 1 million de tokens (≈ 555 000 mots) | [@ANT-MODELS] |
| Sortie maximale (API synchrone) | 128 000 tokens | [@ANT-MODELS] |
| Date limite des connaissances fiables | Juin 2026 | [@ANT-MODELS] |
| Réflexion | Adaptative (toujours active sur Opus 5.5 et Fable 5.2) | [@ANT-MODELS; @ANT-THINK] |
| Niveaux d'effort | low, medium, high, xhigh, max ; défaut API : medium (Opus 5.5, Haiku 5.5), high (Fable 5.2, Sonnet 5.5) | [@ANT-EFFORT] |
| Prix API (entrée / sortie, USD/MTok) | Fable 5.2 : 8 / 40 ; Opus 5.5 : 4 / 20 ; Sonnet 5.5 : 2 / 10 ; Haiku 5.5 : à partir de 0,10 / 0,50 | [@ANT-MODELS] |

### H.2. Fichiers dans l'application

| Élément | Valeur documentée | Source |
|---|---|---|
| Formats de documents | PDF, DOCX, CSV, TXT, HTML, ODT, RTF, EPUB, JSON, XLSX (XLSX : exécution de code requise) | [@ANT-HC-UPLOAD] |
| Formats d'images | JPEG, PNG, GIF, WebP | [@ANT-HC-UPLOAD] |
| Taille par fichier / nombre par conversation | 500 Mo / 20 fichiers | [@ANT-HC-UPLOAD] |
| PDF | 1 000 pages max ; éléments visuels analysés jusqu'à 100 pages | [@ANT-HC-UPLOAD] |
| Fichiers de projet | 30 Mo par fichier | [@ANT-HC-UPLOAD] |

### H.3. Ce que Claude fait bien — et à quelles conditions

| Capacité | Condition de fiabilité |
|---|---|
| Rédiger, reformuler, structurer | Données fournies, règles de vérité, relecture |
| Résumer de longs documents | Demande de citations, contrôle des omissions |
| Extraire des informations | Citations et pages, contrôle par échantillonnage |
| Calculer, analyser des données | Exécution de code, formules et nombre de lignes affichés |
| Comparer des documents | Tableau des différences avec citations |
| Rechercher sur le Web | Sources primaires, cinq contrôles |
| Analyser des images | Images nettes, contexte, prudence d'interprétation |
| Programmer | Tests, revue du code |
| Critiquer un document | Grille explicite ; ne remplace pas une revue indépendante |

### H.4. Ce que Claude ne fait pas (ou ne doit pas faire)

| Limite | Conséquence pratique |
|---|---|
| Ne connaît pas ce qu'il n'a pas vu (documents internes, faits postérieurs à juin 2026) | Fournir les sources ; rechercher et vérifier |
| Peut produire des contenus faux et plausibles | Vérification systématique des faits et références |
| Peut se tromper dans des calculs non outillés | Exécution de code obligatoire |
| N'observe pas le terrain | Mesures et inspections humaines |
| N'assume aucune responsabilité | Validation et signature humaines |
| Peut être influencé par des instructions cachées | Contenus lus = données ; validation des actions |
| Ne doit pas décider en sécurité critique | Lignes rouges (Annexe E.6, Annexe F art. 4) |
| Ne doit pas prendre de décisions individuelles sur des personnes | Interdiction (Annexe F art. 4) |
