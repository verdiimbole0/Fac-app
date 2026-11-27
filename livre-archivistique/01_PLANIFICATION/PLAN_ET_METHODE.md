# Planification et méthode de production

## Architecture retenue (conforme au cahier des charges)

| Partie | Contenu | Cible | Réel |
|---|---|---|---|
| Préliminaires | Titre, mentions légales, auteur, préface (mot de l'auteur), avant-propos, mode d'emploi, parcours, sommaire | 8 p. | 8 p. |
| Ch. 1 à 10 | Ordre pédagogique imposé | 101 p. | 87 p. |
| Conclusion, annexes A-J, glossaire, bibliographie | | 10+ p. | 13 p. |
| **Total** | | **≤ 130 p.** | **108 p.** |

## Chaîne de production

1. **Manuscrit** : Markdown, un fichier par partie (`02_MANUSCRIT/`), encadrés pédagogiques en blocs `::: classe`.
2. **Schémas** : `06_MISE_EN_PAGE/figs.py` (SVG originaux + PNG).
3. **PDF** : `06_MISE_EN_PAGE/build.py` (Pandoc → HTML → WeasyPrint, feuille de style `livre.css`).
4. **DOCX** : `06_MISE_EN_PAGE/make_docx.py` (Pandoc + filtre Lua + post-traitement python-docx).
5. **Annexes modifiables** : `06_MISE_EN_PAGE/make_annexes.py` (Word + Excel).
6. **Couvertures** : `06_MISE_EN_PAGE/covers.py`.

Reconstruire tout :

    cd 06_MISE_EN_PAGE && python3 figs.py && python3 build.py && python3 make_docx.py && python3 make_annexes.py && python3 covers.py

## Fil rouge : Organisation Horizon (cas fictif)

ASBL de 42 salariés, siège + 2 antennes, 6 services (DIR, FIN, RHU, PRG, LOG, COM), plan fonctionnel 01 à 07, cote HOR/rubrique/année/numéro, localisation local-travée-tablette-boîte. Personnages : Mireille (directrice), Jonas (RAF), Esther (référente archives), Patrick (comptable), Grâce (RH), Samuel (programmes). Bailleur fictif : Fondation Alizé.

## Stratégie documentaire

Sources officielles uniquement (ISO, ICA, NIST, Library of Congress, FADGI, textes juridiques cités comme exemples contextualisés) et ouvrages de référence confirmés par des notices. Toute référence non confirmée a été écartée (voir `05_RECHERCHE/RAPPORT_VERIFICATION_SCIENTIFIQUE.md`).
