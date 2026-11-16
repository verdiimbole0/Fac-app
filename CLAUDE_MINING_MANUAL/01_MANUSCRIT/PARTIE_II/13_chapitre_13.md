## Chapitre 13 — Travailler avec les documents et les fichiers

### A. Mise en situation professionnelle

Le directeur des opérations de MCC demande à Thomas Kayembe, directeur financier, une analyse du rapport mensuel de production de mars 2026 (PDF), croisée avec le fichier Excel du budget et le tableau journalier de production. Il ajoute une photo, prise au téléphone, du tableau blanc de la salle de contrôle où figurent les arrêts de l'usine. Quatre formats, quatre sources, une échéance à 17 heures. Thomas se demande ce que Claude peut lire, comment le lui faire lire, et comment s'assurer qu'il a bien lu.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Identifier** les formats de fichiers acceptés et les limites applicables.
2. **Préparer** un document avant de le transmettre (confidentialité, lisibilité, découpage).
3. **Faire extraire** des informations d'un PDF, d'un document Word, d'un tableur ou d'une image, de manière traçable.
4. **Faire produire** des fichiers (Word, Excel, présentations, graphiques).
5. **Vérifier** systématiquement les extractions et les calculs.

### C. Comprendre avant de pratiquer

#### C.1. Formats acceptés et limites (état au 16 novembre 2026)

D'après le centre d'aide [@ANT-HC-UPLOAD] :

*Tableau 13.1 — Fichiers acceptés dans l'application.*

| Catégorie | Formats | Remarque |
|---|---|---|
| Documents | PDF, DOCX, CSV, TXT, HTML, ODT, RTF, EPUB, JSON, XLSX | L'import de fichiers XLSX nécessite l'activation de l'exécution de code et de la création de fichiers |
| Images | JPEG, PNG, GIF, WebP | Préférer des images d'au moins 1 000 × 1 000 pixels |

*Tableau 13.2 — Limites indiquées par le centre d'aide.*

| Limite | Valeur |
|---|---|
| Taille par fichier (conversation) | 500 Mo |
| Nombre de fichiers par conversation | 20 |
| Dimensions maximales d'une image | 8 000 × 8 000 pixels |
| Pages d'un PDF | 1 000 pages maximum |
| Analyse des éléments visuels d'un PDF (graphiques, images) | PDF de 100 pages ou moins ; au-delà (101 à 1 000 pages), texte seulement |
| Fichiers de projet | 30 Mo par fichier |

Deux précisions importantes du centre d'aide : pour les documents autres que PDF, Claude **extrait uniquement le texte** (les images intégrées ne sont pas interprétées) ; pour désigner une page d'un PDF, utilisez la numérotation **de votre lecteur PDF**, et non celle imprimée sur le document [@ANT-HC-UPLOAD]. Des limites supplémentaires liées au nombre de tokens peuvent s'appliquer selon la longueur du contenu extrait.

::: terrain
Votre rapport de 180 pages contient des graphiques essentiels aux pages 40 à 60 ? Extrayez ces pages dans un PDF séparé de moins de 100 pages : Claude pourra alors analyser les graphiques, et pas seulement le texte.
:::

#### C.2. Préparer un document : la règle des trois « C »

1. **Classification** : quel est le niveau de confidentialité ? Est-il autorisé dans l'outil utilisé (chapitre 37) ?
2. **Clarté** : le fichier est-il lisible ? Un scan penché ou de faible résolution, un tableau en image dans un document Word, des cellules fusionnées complexes dans Excel dégradent fortement l'extraction.
3. **Ciblage** : faut-il vraiment tout le document ? Un extrait ciblé améliore la précision et réduit la consommation.

#### C.3. Les quatre opérations de base

| Opération | Exemple | Exigence clé |
|---|---|---|
| **Résumer** | Synthèse d'une étude d'impact | Préciser le public, la longueur, les sujets prioritaires |
| **Extraire** | Obligations d'un contrat, valeurs d'un tableau | Exiger page/section et citation exacte |
| **Comparer** | Deux versions d'une procédure | Demander un tableau des différences |
| **Analyser** | Écarts budget/réel | Calculs par exécution de code, méthode explicite |

#### C.4. Tableurs et fichiers de données

Pour les fichiers Excel et CSV, Claude utilise l'**exécution de code** : il écrit et exécute un programme qui lit le fichier, calcule et produit des tableaux ou des graphiques. C'est ce qui rend les calculs fiables et vérifiables (chapitre 3). Bonnes pratiques :

- indiquez la structure : séparateur, ligne d'en-tête, unités, signification des colonnes ;
- demandez d'abord un **profil du fichier** (nombre de lignes, colonnes, valeurs manquantes, valeurs aberrantes) avant toute analyse ;
- demandez le code et le nombre de lignes traitées.

#### C.5. Images, photos et plans

Claude peut décrire et analyser des images : graphiques, schémas, photos de pièces, plans, tableaux photographiés [@ANT-VISION]. Pour de bons résultats, fournissez une image nette, cadrée, avec une échelle ou un repère, et précisez ce que vous cherchez. Distinguez toujours **observation** et **interprétation**.

#### C.6. Produire des fichiers

Avec l'exécution de code et la création de fichiers activées, Claude peut produire des documents Word, des classeurs Excel, des présentations et des PDF, ainsi que des graphiques ; les compétences (*Skills*) fournies par Anthropic pour la création de documents bureautiques sont invoquées automatiquement lorsque c'est pertinent [@ANT-HC-SKILLS]. Les artefacts (chapitre 15) permettent en outre de créer des documents, présentations et tableaux de bord modifiables dans l'application [@ANT-HC-ARTIFACTS].

![Figure 13.1 — Circuit de travail sur un document. La préparation et la vérification encadrent toujours le travail de Claude. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig13_1_circuit_documentaire.png){width=100%}

### D. Démonstration guidée — L'analyse de Thomas

**Étape 1 — Préparer.** Thomas vérifie que les trois fichiers sont de niveau « usage interne » (autorisés dans l'espace MCC). Il recadre la photo du tableau blanc et la recopie partiellement à la main pour les valeurs illisibles.

**Étape 2 — Profiler les données.** Il joint `MCC_production_journaliere_S1_2026.xlsx` et demande un profil (prompt 13.1). Claude signale : une journée manquante (11 avril), une récupération de 121,4 % le 15 février, une production de cathode anormalement élevée le 1er juin. Ce sont les anomalies volontairement insérées dans le jeu de données.

**Étape 3 — Extraire du PDF.** Il joint `MCC_rapport_mensuel_production_mars_2026.pdf` et demande l'extraction des chiffres clés avec citation (prompt 13.2).

**Étape 4 — Croiser.** Il demande la réconciliation entre le rapport (189 kt traitées, 2,41 % Cu, 87,9 % de récupération, 4 007 t de cathode) et les données journalières de mars, avec calcul par programme (prompt 13.3). Claude calcule que 189 000 t × 2,41 % × 87,9 % ≈ 4 004 t, cohérent avec les 4 007 t annoncées à l'arrondi près, et compare aux totaux journaliers.

**Étape 5 — Lire l'image.** Il joint la photo du tableau blanc et demande la transcription des arrêts, en marquant les éléments illisibles.

**Étape 6 — Produire.** Il demande une note Word de deux pages avec un tableau et un graphique, puis la relit, corrige un libellé et ajoute son commentaire.

### E. Prompts commentés

**Prompt 13.1 — Profil d'un fichier de données**

```text
Fichier joint : MCC_production_journaliere_S1_2026.xlsx (ligne 1 = bandeau, ligne 2 = en-têtes).
Avec l'exécution de code, établis le profil du fichier :
- nombre de lignes et de colonnes ; période couverte ; dates manquantes ;
- pour chaque colonne numérique : minimum, maximum, moyenne, valeurs manquantes ;
- valeurs physiquement impossibles ou aberrantes (par exemple récupération > 100 %) ;
- doublons éventuels.
Présente un tableau de synthèse et la liste des anomalies, avec la ligne concernée.
Ne corrige rien : signale seulement.
```

*Commentaire.* Le profil précède toute analyse : il évite de bâtir un raisonnement sur des données défectueuses. La consigne « ne corrige rien » préserve votre contrôle sur les données.

**Prompt 13.2 — Extraction traçable d'un PDF**

```text
Document joint : rapport mensuel de production de mars 2026.
Extrais dans un tableau : indicateur | valeur | unité | page | citation exacte.
Indicateurs : minerai traité, teneur d'alimentation, récupération, cathode produite,
consommation d'acide, coût unitaire, arrêts non planifiés.
Si un indicateur est absent, écris « absent ». N'effectue aucun calcul à ce stade.
```

**Prompt 13.3 — Réconciliation entre sources**

```text
Compare les chiffres extraits du rapport (tableau précédent) avec le fichier journalier
pour le mois de mars 2026. Avec l'exécution de code :
1. calcule les totaux et moyennes pondérées de mars à partir du fichier journalier ;
2. calcule la production théorique = minerai traité × teneur × récupération ;
3. présente un tableau rapport / fichier / écart / écart %.
Commente uniquement les écarts supérieurs à 1 %. Affiche le code.
```

**Prompt 13.4 — Lecture d'une photo**

```text
Photo jointe : tableau blanc de la salle de contrôle (arrêts de l'usine).
Transcris les informations dans un tableau : date | équipement | durée | cause notée.
Mets [illisible] pour tout élément que tu ne peux pas lire avec certitude.
Ne déduis aucune valeur manquante.
```

### F. Exercices pratiques

**Exercice 13.1 (guidé) — Profil et anomalies**

Réalisez l'étape 2 de la démonstration avec le fichier de production. Retrouvez-vous les trois anomalies ? Comparez avec `ANOMALIES_ATTENDUES.md`.

**Exercice 13.2 (guidé) — Le contrat**

Avec `MCC_contrat_fourniture_acide_extrait.pdf`, extrayez toutes les obligations du fournisseur et de l'acheteur avec l'article et la citation. Puis demandez : « Quelle pénalité pour une livraison de 5 100 t en mars, si la facturation mensuelle est de 1 020 000 USD ? » Vérifiez le calcul vous-même : (5 400 − 5 100) × 8 = 2 400 USD, sous le plafond de 5 % (51 000 USD).

**Exercice 13.3 (autonome) — Votre document réel**

Choisissez un document de votre travail autorisé par la charte. Appliquez le circuit complet de la figure 13.1 et documentez chaque contrôle.

### G. Livrable professionnel

**Note d'analyse croisée** (2 pages) : tableau des indicateurs extraits avec sources, tableau de réconciliation, anomalies détectées, commentaire, liste des contrôles effectués.

### H. Vérification des résultats

::: controle
**Check-list d'extraction**

- Échantillon d'au moins 10 % des valeurs extraites (et toutes les valeurs critiques) contrôlé dans le document source.
- Les citations correspondent mot pour mot.
- Les numéros de page correspondent à ceux du lecteur PDF.
- Le nombre de lignes traitées correspond au nombre de lignes du fichier.
- Les unités sont cohérentes (t / kt, % / ppm, USD / MUSD).
- Les éléments illisibles sont signalés, pas devinés.
:::

::: setrompe
Dans un tableau PDF à colonnes serrées, Claude décale une valeur d'une colonne (la teneur en cobalt attribuée au cuivre). Le tableau extrait paraît propre. **Contre-mesure** : demandez la citation de la ligne complète du tableau source pour chaque valeur critique, et vérifiez la vraisemblance (une teneur en Co de 2,4 % sur ce gisement serait anormale).
:::

### I. Limites et précautions

- Les scans de mauvaise qualité, l'écriture manuscrite et les tableaux complexes restent des sources d'erreur.
- Au-delà de 100 pages, les graphiques des PDF ne sont pas analysés : découpez le document.
- Ne joignez pas de documents dont la classification n'autorise pas l'usage de l'outil.
- Vérifiez toujours les fichiers produits (formules, mise en forme, données) avant diffusion.

### J. Boîte à outils

**Les cinq demandes systématiques**

1. « Établis d'abord le profil du fichier. »
2. « Cite la page et le passage exact. »
3. « Calcule avec l'exécution de code et affiche le code. »
4. « Indique le nombre d'éléments traités. »
5. « Signale ce qui est illisible ou absent ; ne devine pas. »

### K. Quiz

1. **(QCM)** Selon le centre d'aide, jusqu'à combien de pages Claude analyse-t-il aussi les éléments visuels d'un PDF ? a) 10 ; b) 100 ; c) 500 ; d) 1 000.
2. **(Vrai ou faux)** Claude interprète les images intégrées dans un document Word.
3. **(Compréhension)** Quelle condition est nécessaire pour importer un fichier XLSX ?
4. **(QCM)** Combien de fichiers peut-on joindre au maximum par conversation selon le centre d'aide ? a) 5 ; b) 10 ; c) 20 ; d) illimité.
5. **(Application)** Calculez la pénalité contractuelle pour 5 100 t livrées (article 9 : 8 USD/t manquante sous 5 400 t).
6. **(Mise en situation)** Votre rapport de 300 pages contient des graphiques clés. Comment procédez-vous ?
7. **(Vrai ou faux)** Il faut citer les numéros de page imprimés sur le document plutôt que ceux du lecteur PDF.
8. **(Compréhension)** Pourquoi demander un profil du fichier avant l'analyse ?
9. **(Analyse critique)** Une extraction « propre » peut-elle contenir des erreurs ? Donnez un exemple.
10. **(Application)** Rédigez la consigne qui empêche Claude de deviner les éléments illisibles d'une photo.

<div class="carnet" titre="Chapitre 13 — Travailler avec les documents et les fichiers"></div>
