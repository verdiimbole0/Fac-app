# Suivi de production

> Mettre à jour après chaque étape. En cas d'interruption : reprendre au « Prochain travail ».

## État au 16/11/2026

| Élément | État |
|---|---|
| Phase 1 — Préparation (structure, scénario, charte, compétences) | ✅ Terminée |
| Phase 2 — Recherches documentaires (registre `08_OUTILS/sources.py`) | ✅ Socle constitué (69 sources) ; complété au fil de la rédaction |
| Chaîne de production (reference.docx, filtre Lua, construction DOCX/PDF, sommaire) | ✅ Validée sur la partie I |
| Figures parties I-II | ✅ 30 figures |
| Données d'exercice | ✅ 10 CSV, 3 XLSX, 4 DOCX, 3 PDF + corrigé des anomalies |
| Liminaires | ✅ |
| Partie I | 🔄 ch. 1 terminé |

## Chapitres

| Ch. | Titre court | État |
|---|---|---|
| 1 | Industrie minière et IA | ✅ |
| 2–6 | Fondamentaux IA, LLM, Claude, limites, expertise | ⏳ |
| 7–16 | Partie II | ⏳ |
| 17–32 | Partie III | ⏳ |
| 33–36 | Partie IV | ⏳ |
| 37–40 | Partie V | ⏳ |
| 41–43 | Partie VI | ⏳ |
| Annexes A–M | | ⏳ |

## Décisions éditoriales
- Format A4, corps Cambria (Caladea au rendu PDF), titres Calibri (Carlito), palette marine/or/turquoise.
- Hiérarchie : Partie = Titre 1 ; Chapitre = Titre 2 ; sections A–L = Titre 3 ; sous-sections = Titre 4.
- Citations : clés `[@ID]` converties automatiquement en APA ; une clé absente du registre bloque la construction.
- Carnet de réflexion : généré par le gabarit `<div class="carnet" titre="…">` (2 pages : rubriques + zone libre).
- Corrigés des quiz : un fichier `99_corriges_partie_X.md` à la fin de chaque partie.
- Interface Claude : illustrations schématiques uniquement (pas d'accès authentifié à claude.ai depuis l'environnement de production → aucune capture authentique possible).
- Photographies : Wikimedia Commons, licences libres uniquement, crédits complets en légende.

## Difficultés techniques
- Réseau restreint : environnement dédié créé (hôtes institutionnels autorisés). OCDE, OIT (normlex), ISO, OWASP, JORC, CRIRSCO, UNESCO, GRI restent bloqués (403) → références vérifiées par recherche documentaire (« ◇ »).
- Le champ TOC Word n'est pas converti par LibreOffice → index natif inséré par le script UNO.

## Prochain travail
Chapitres 2 à 6, corrigés partie I, puis partie II.
