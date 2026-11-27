# Rapport de contrôle éditorial et technique

**Ouvrage :** *L'archivistique : principes et pratiques du métier d'archiviste*, Verdi Imbole, 2026
**Date :** 27 novembre 2026

## 1. Fichiers produits (dossier `07_LIVRABLES`)

| Fichier | Contenu | Vérification |
|---|---|---|
| `Archivistique_Verdi_Imbole_interieur.pdf` | Intérieur du livre, A4, 112 pages | Ouvert et contrôlé page par page (rendu visuel) |
| `Archivistique_Verdi_Imbole_complet_avec_couvertures.pdf` | Couverture avant + intérieur + couverture arrière (114 pages) | Ouvert, assemblage contrôlé |
| `Archivistique_Verdi_Imbole.docx` | Version Word intégralement modifiable | Ouverte avec python-docx et convertie par LibreOffice : 19 images, 165 tableaux, encadrés, en-têtes et pieds de page |
| `Couverture_avant.pdf` / `.png` · `Couverture_arriere.pdf` / `.png` | Couvertures A4 (PNG 200 ppp) | Contrôle visuel |
| `Annexes_modeles/` | 10 modèles Word (A à J) + `Registre_suivi_documentaire.xlsx` | Ouverts et convertis ; listes déroulantes, formule d'échéance, contrôle des doublons |
| `Manuscrit_source/` | Manuscrit Markdown, un fichier par chapitre | Source unique du PDF et du DOCX |
| `Illustrations/` | 19 schémas SVG + PNG, couvertures, dossiers `images_libres` et `images_ia` (vides, justifiés) | Voir IMAGE_SOURCES.md |
| `IMAGE_SOURCES.md`, `BIBLIOGRAPHIE.md` | Registre des images, bibliographie datée | |
| `RAPPORT_VERIFICATION_SCIENTIFIQUE.md`, ce rapport | Contrôles | |
| `Polices/` | Montserrat et Source Sans 3 (licence OFL) à installer pour un rendu fidèle du DOCX | |

## 2. Volumétrie réelle

| Partie | Pages (PDF) | Cible du cahier des charges |
|---|---|---|
| Pages préliminaires (titre, mentions, auteur, préface, avant-propos, mode d'emploi, parcours, sommaire) | 8 (p. 1-8) | 8 |
| Chapitre 1 | 10 (p. 9-18) | 8 |
| Chapitre 2 | 9 (p. 19-27) | 9 |
| Chapitre 3 | 9 (p. 28-36) | 10 |
| Chapitre 4 | 9 (p. 37-45) | 11 |
| Chapitre 5 | 9 (p. 46-54) | 11 |
| Chapitre 6 | 9 (p. 55-63) | 10 |
| Chapitre 7 | 9 (p. 64-72) | 11 |
| Chapitre 8 | 9 (p. 73-81) | 11 |
| Chapitre 9 | 9 (p. 82-90) | 10 |
| Chapitre 10 | 9 (p. 91-99) | 10 |
| Conclusion générale | 2 (p. 100-101) | 2 |
| Annexes A à J | 8 (p. 102-109) | 6 |
| Glossaire | 1 (p. 110) | 1 |
| Bibliographie et webographie | 2 (p. 111-112) | au moins 1 |
| **Total intérieur** | **112** | **130 maximum** |

Chaque chapitre compte une page d'ouverture pleine page. Les chapitres sont légèrement plus courts que les cibles indicatives : conformément à la consigne « ne remplis pas artificiellement », aucun contenu de remplissage n'a été ajouté. La version DOCX, mise en page par le traitement de texte, compte environ 121 pages sous LibreOffice (le nombre exact varie selon le logiciel et les polices installées) ; le contenu est identique.

Volume rédactionnel : environ 27 000 mots pour les dix chapitres, 37 000 mots au total.

## 3. Contrôle pédagogique

- Structure imposée respectée dans les 10 chapitres : titre, situation problématique, objectifs, développement, explications, approfondissements, exemples professionnels, tableaux et schémas, cas pratique corrigé, erreurs fréquentes, « À retenir », QCM de 6 questions et corrigé expliqué.
- Rubrique « Comment utiliser ce manuel » : mentions exigées sur les chapitres 1 à 6 (à lire impérativement), 7 à 9 (à approfondir), 10 et annexes (indispensables pour la mise en œuvre), et règle de ne pas aborder les chapitres spécialisés avant les fondamentaux.
- Fil rouge « Organisation Horizon » présent dans tous les chapitres, toujours signalé comme **cas fictif**, avec des noms, services, codes et situations constants ; système final présenté au chapitre 10.
- 6 prompts d'IA (ch. 9) structurés en objectif, données nécessaires, résultat attendu, précautions.
- Feuille de route des 30 premiers jours (ch. 10) : tableau et diagramme.
- Chaque annexe est accompagnée d'un exemple d'utilisation ou d'une règle d'emploi.

## 4. Contrôle rédactionnel

| Contrôle | Résultat |
|---|---|
| Caractère « — » dans le corps du texte | 0 occurrence (contrôle automatique) ; les cellules vides d'une matrice ont été remplacées par « 0 » |
| Formules proscrites (« Dans un monde en constante évolution », « À l'ère du numérique », « Il convient de noter que », « Il est important de souligner que ») | 0 occurrence |
| Ouvertures de chapitres | Toutes différentes (audit de bailleur, double paiement, bureau hérité, recherche orale, cave inondée, entrepôt, serveur saturé, fuite de rapport, test d'IA, prise de poste) |
| Termes techniques | Définis à la première apparition (encadrés « Définitions ») et repris au glossaire (33 entrées) |
| Orthographe et accords | Relecture complète ; corrections apportées (accord « une archive n'est pas définie »). Une dernière relecture humaine reste recommandée avant impression commerciale |
| Texte justifié | Oui, avec césure française automatique (PDF) et alignement justifié (DOCX) ; tableaux et titres alignés à gauche pour la lisibilité |

## 5. Contrôle graphique

- Palette (révision du 27/11/2026, à la demande de l'auteur) : gris foncé #33373D, vert forêt #2D5A3B, bordeaux #7B1E30, avec gris clair #F2F3F4 pour les fonds ; teintes claires dérivées (vert #8DBB9A, bordeaux #D98A98) pour la lisibilité sur fond sombre. Aucune couleur dorée.
- Polices : Montserrat (titres, tableaux d'en-tête), Source Sans 3 (corps 10,5 pt, interligne 1,25 ; tableaux 9,4 pt). Titres de chapitre 25 pt, sous-titres 12,5 pt.
- Inspiration de la plaquette fournie : bandeaux de section pleine largeur sur fond sombre, carrés numérotés de couleur accent, grands titres en graisse fine, grilles de pictogrammes, pages d'ouverture pleine page sombre avec visuel.
- Encadrés différenciés (situation, objectifs, définitions, exemple, fil rouge, attention, cas pratique, corrigé, QCM, prompt, modèle, à retenir).
- En-têtes courants (titre du chapitre, nom de l'ouvrage), pieds de page avec numérotation en pavé marine, pages paires/impaires différenciées ; pagination en chiffres romains pour les préliminaires.
- Légendes numérotées « Figure n.n » et « Tableau n.n ».

## 6. Contrôle technique

| Point | Résultat |
|---|---|
| 130 pages maximum | 112 pages intérieures |
| Sommaire automatique | PDF : numéros de page calculés automatiquement et liens cliquables ; DOCX : champ Table des matières, mis à jour à l'ouverture (ou clic droit > Mettre à jour les champs) |
| Signets PDF | 37 entrées de navigation |
| Liens | 18 liens externes, tous vers des pages officielles (ISO, ICA, NIST, LoC, FADGI, Légifrance, EUR-Lex, OHADA) ; liens internes du sommaire fonctionnels |
| Images intégrées | 19 schémas intégrés en vectoriel dans le PDF, en PNG dans le DOCX ; aucun lien d'image externe |
| Pages blanches involontaires | Aucune (contrôle automatique et visuel) |
| Débordements | Aucun après corrections (voir section 7) |
| Correspondance DOCX et PDF | Même source Markdown, même ordre, même contenu ; la mise en page diffère par nature (traitement de texte) |

## 7. Anomalies détectées et corrigées

1. Pied de page des pages paires compressé dans une colonne étroite : largeur des zones de pied fixée.
2. Attributs techniques de légendes de tableaux affichés en clair (`{#tbl-…}`) : supprimés.
3. Chapitre 1 trop long (12 pages au premier rendu) : resserrage typographique global (marges, espacements, corps 10,5 pt).
4. Pages préliminaires débordant sur 10 pages et sommaire sur 2 pages : contenus resserrés, sommaire sur une page en deux colonnes ; préliminaires ramenés à 8 pages.
5. Numéros de page du sommaire affichés « 0 » : liens internes corrigés, numéros désormais calculés.
6. Tableau de l'annexe C (14 colonnes) débordant de la page : réduit à 9 colonnes dans le livre, version complète dans le fichier Excel.
7. Colonnes de tableaux à largeur fixe trop étroites dans les annexes : largeur automatique selon le contenu.
8. Glossaire débordant d'une ligne sur une page supplémentaire : mise en deux colonnes.
9. Caractères absents de la police (flèches, coches, cases à cocher, arborescence) : remplacés dans les schémas ou rendus par une police de secours.
10. Deux schémas non convertis dans le DOCX : corrigé, 19 images présentes.
11. Tableaux imbriqués dans les encadrés du DOCX sans bordures : bordures et en-têtes appliqués.
12. Lignes justifiées terminées par un retour à la ligne étirées dans Word : option de compatibilité activée.
13. En-tête de section d'annexe isolé en bas de page : modèles maintenus d'un seul tenant.

## 8. Points laissés à l'appréciation de l'auteur

- **Titre** : voir la section 7 du rapport de vérification scientifique (formulation identique au sous-titre de l'*Abrégé d'archivistique* de l'AAF).
- **ISBN et dépôt légal** : non renseignés, conformément à la consigne. À ajouter dans les mentions légales le cas échéant.
- **Couverture pour l'impression** : les couvertures sont au format A4 sans fond perdu. Pour un imprimeur, prévoir l'ajout de 3 mm de fond perdu et le calcul du dos selon le papier et le nombre de pages.
- **Polices du DOCX** : installer Montserrat et Source Sans 3 (dossier `Polices/`) pour retrouver la typographie du PDF.

## 9. Révision du 27 novembre 2026 (design de la plaquette de référence)

Demandes de l'auteur appliquées :

1. **Design de la plaquette jointe** appliqué à l'ensemble du livre :
   - bandeaux de section centrés en capitales sur fond sombre, avec carré numéroté or décalé sur l'angle ;
   - encadrés en cartes portant un carré or décalé avec pictogramme au trait (13 pictogrammes originaux) ;
   - carte « Objectifs pédagogiques » ardoise à texte blanc, comme les cartes numérotées de la plaquette ;
   - puces triangulaires or ;
   - pages d'ouverture : filet vertical or devant l'accroche, rangée de chiffres clés avec pictogrammes (sections, schémas, tableaux, questions QCM, calculés automatiquement), panneau en biais à filet or ;
   - schéma du cycle de vie (figure 2.1) redessiné en roue de processus : arcs gris, pictogrammes, légendes en renvoi ;
   - couverture avant : coupe en biais à filet or entre l'illustration et le bloc titre.
2. **Bibliographie et webographie** : phrase introductive supprimée du livre. Les dates de consultation restent consignées dans BIBLIOGRAPHIE.md.
3. **Couverture avant** : mentions « 10 chapitres », « 10 modèles prêts à l'emploi » et « Papier · Numérique · IA » supprimées.

Effet sur la pagination : 112 pages intérieures (contre 108), toujours sous la limite de 130. Les préliminaires restent sur 8 pages et aucune page blanche n'apparaît.

## 10. Révision du 27 novembre 2026 (palette et coins arrondis)

Demandes de l'auteur appliquées :

1. **Coins arrondis** sur toutes les cases et tous les tableaux : encadrés (rayon 3 mm), bandeaux de section, carrés numérotés et carrés à pictogramme, tableaux (bordure arrondie, en-tête et dernière ligne arrondis), blocs de code, filets ; dans les 19 schémas, tous les rectangles sont arrondis.
2. **Palette intérieure** : gris foncé (bandeaux, en-têtes de tableaux, pages d'ouverture, « À retenir »), vert forêt (carte « Objectifs », pictogrammes, puces, filets, fil rouge Horizon), bordeaux (numéros de section, étiquettes « Situation », « Attention », « Cas pratique », « QCM », légendes de figures et tableaux, carrés des ouvertures).
3. **Suppression de tout le doré** : feuille de style, pages d'ouverture, page de titre, 19 schémas, couvertures avant et arrière, version Word, modèles Word et Excel. Les cartons de l'illustration de couverture, de teinte kraft, sont passés en gris, vert et bordeaux, et la lumière du couloir est devenue blanche.

Contrôle : analyse colorimétrique automatique de toutes les pages du PDF et des deux couvertures, sans aucun pixel de teinte dorée détecté ; recherche des codes couleur dorés dans les fichiers DOCX et XLSX, sans résultat.

Limite : Word ne sait pas arrondir les coins des tableaux ni des encadrés construits en tableaux. Dans la version DOCX, couleurs et contenus sont identiques au PDF, mais les angles restent droits.

Pagination inchangée : 112 pages intérieures.

## 10. Révision du 27 novembre 2026 (palette et coins arrondis)

Demandes de l'auteur appliquées :

1. **Contours arrondis** : encadrés, cartes, bandeaux de section, carrés numérotés, tableaux (y compris en-têtes), figures, pastilles des ouvertures et blocs des 19 schémas ont des coins arrondis dans le PDF. Limite technique : Word ne sait pas arrondir les cellules de tableau ; dans le DOCX, les encadrés gardent des angles droits.
2. **Palette intérieure** : bleu marine (titres, bandeaux, en-têtes de tableaux, ouvertures), vert forêt (objectifs, définitions, exemples, puces, chiffres clés, éléments positifs), bordeaux (numéros de section, situations, cas pratiques, avertissements, risques). Les gris intermédiaires d'une version de travail ont été remplacés par des tons marine et des gris bleutés.
3. **Suppression du doré** : contrôle automatique sur les sources, les 19 schémas, la page de titre, les ouvertures, les deux couvertures, le DOCX et les 10 modèles Word : aucune teinte dorée restante.

Règles de design respectées : une couleur dominante et deux couleurs d'accent à rôles fixes ; contrastes suffisants pour le texte blanc sur marine, vert et bordeaux ; neutres froids cohérents avec le marine ; rayons d'arrondi homogènes.

Pagination inchangée : 112 pages intérieures, préliminaires sur 8 pages, aucune page blanche.

## 10. Révision : palette intérieure et arrondis

Palette appliquée à l'intérieur selon des rôles fixes, pour une lecture cohérente :

| Rôle | Couleur |
|---|---|
| Structure : bandeaux de section, en-têtes de tableaux, « À retenir », ouvertures | Bleu marine #0A1E3F |
| Fonds doux : situation, exemple, prompt, lignes alternées des tableaux | Bleu pastel #DCE9F7 / #EFF5FC |
| Numérotation, puces, filets, fil rouge Horizon, définitions, modèles | Moutarde #D9A520 (texte en ocre #A8761A pour la lisibilité) |
| Avertissements : encadrés « Attention » et erreurs | Orange #E07B39 (texte #B65A1F) |
| Exercices : cas pratiques, QCM, corrigés | Bordeaux #7B1E30 |

- Coins arrondis sur tous les encadrés (3 mm), les tableaux (3 mm), les bandeaux de titre, les carrés numérotés et pictogrammes, les blocs de code et les cases des schémas.
- Les 19 schémas ont été recolorés dans la même palette (échelle de risque : bleu pastel, moutarde, orange, bordeaux).
- Contraste : le texte courant reste marine ou blanc sur fond marine ; le moutarde n'est jamais utilisé pour du texte de petite taille sur fond blanc (l'ocre le remplace).
- DOCX : couleurs alignées sur les mêmes rôles. Word ne gère pas les coins arrondis des tableaux et des cellules : ils restent droits dans la version modifiable.
- Couvertures inchangées (la demande portait sur le design intérieur).
- Pagination inchangée : 112 pages intérieures, aucune page blanche.
