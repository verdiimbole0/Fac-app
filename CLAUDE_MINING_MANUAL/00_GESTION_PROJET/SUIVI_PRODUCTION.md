# Suivi de production

> Mettre à jour après chaque étape. En cas de reprise : lire « Prochain travail ».

## État au 16/11/2026 — manuscrit complet

| Élément | État |
|---|---|
| Phase 1 — Préparation (structure, scénario, charte, compétences, plan) | ✅ |
| Phase 2 — Recherches documentaires (70 sources au registre ; ◆ consultation directe / ◇ recherche documentaire) | ✅ |
| Phase 3 — Rédaction : liminaires + 43 chapitres + 6 fichiers de corrigés | ✅ |
| Phase 4 — Annexes A à M (I générée depuis le registre) | ✅ |
| Phase 5 — Contrôle qualité automatique (0 anomalie structurelle) + corrections de cohérence | ✅ — relecture humaine éditeur à faire |
| Phase 6 — Assemblage : DOCX (≈ 11 Mo) + PDF (391 pages) dans `06_PRODUCTION_FINALE/` | ✅ |

## Chiffres clés
- ≈ 99 500 mots (chapitres, corrigés, annexes) ; ≈ 105 000 mots avec liminaires et bibliographie.
- 430 questions de quiz, toutes corrigées et expliquées.
- 131 prompts commentés dans les chapitres + 124 prompts dans l'Annexe B.
- 62 figures originales (PNG + SVG) ; 10 photographies sous licence libre intégrées (crédits complets, Annexe M.5).
- 10 CSV, 3 XLSX, 4 DOCX, 3 PDF d'exercice + corrigé des anomalies.

## Chapitres
| Partie | Chapitres | État |
|---|---|---|
| I | 1–6 + corrigés | ✅ |
| II | 7–16 + corrigés | ✅ |
| III | 17–32 + corrigés | ✅ |
| IV | 33–36 + corrigés | ✅ |
| V | 37–40 + corrigés | ✅ |
| VI | 41–43 + corrigés | ✅ |
| Annexes | A–M | ✅ |

## Décisions éditoriales
- Format A4 ; corps Cambria (Caladea au rendu PDF) ; titres Calibri (Carlito) ; palette marine/or/turquoise.
- Partie = Titre 1 ; Chapitre = Titre 2 ; sections A–L = Titre 3.
- Citations `[@ID]` converties en APA ; clé inconnue = construction bloquée.
- Carnet de réflexion généré par gabarit (2 pages par chapitre).
- Interface Claude : illustrations schématiques uniquement.
- Photographies : Wikimedia Commons, licences libres ; fichiers fournis par l'éditeur (ZIP) et intégrés par `08_OUTILS/integrer_photos.py`.

## Difficultés techniques rencontrées
- Réseau restreint : environnement dédié créé ; certains sites restent bloqués (403) → références ◇.
- Wikimedia : téléchargement automatisé refusé (politique anti-robots exigeant un contact dans l'User-Agent) → script `08_OUTILS/photos.py telecharger "<UA avec contact>"` à lancer par l'éditeur.
- Champ TOC Word non converti par LibreOffice → index natif inséré par le script UNO ; le DOCX demande la mise à jour du sommaire à l'ouverture.

## Prochain travail (révision éditoriale)
1. ✅ Photographies intégrées (10/10).
2. Relecture humaine complète ; validation par des praticiens et un juriste (voir `07_CONTROLE_QUALITE`).
3. Revalidation des informations datées sur Claude avant publication.
4. Reconstruction : `python3 08_OUTILS/construire_livre.py` puis `python3 08_OUTILS/controle_qualite.py`.
