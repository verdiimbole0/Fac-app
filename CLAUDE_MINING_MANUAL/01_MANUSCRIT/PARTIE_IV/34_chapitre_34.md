## Chapitre 34 — Produire des livrables professionnels avec Claude

### A. Mise en situation professionnelle

Thomas Kayembe doit produire, en une semaine, le rapport trimestriel au conseil d'administration (25 pages), sa présentation (15 diapositives) et une note de synthèse en anglais pour l'actionnaire de référence. Il a déjà constaté qu'un « rapport écrit par Claude » se reconnaît vite : phrases génériques, structure attendue, affirmations vagues. Il veut l'inverse : des livrables **au standard de MCC**, précis, sourcés, au ton juste — produits plus vite, sans perte de qualité.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Appliquer** le cycle de production d'un livrable : cadrer, structurer, rédiger, vérifier, relire, valider.
2. **Imposer** à Claude les standards de l'entreprise (modèles, charte rédactionnelle, glossaire).
3. **Produire** des documents Word, présentations et tableaux exploitables.
4. **Éviter** les défauts typiques des textes générés (généralités, remplissage, ton inadapté).
5. **Assurer** la traçabilité des sources et des versions.

### C. Comprendre avant de pratiquer

![Figure 34.1 — Le cycle de production d'un livrable professionnel avec Claude. La structure est validée avant la rédaction ; la vérification et la relecture sont humaines. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig34_1_cycle_livrable.png){width=100%}

#### C.1. Les cinq règles d'un livrable de qualité

1. **Valider le plan avant la rédaction.** Un plan juste évite 80 % des réécritures.
2. **Rédiger par sections**, chacune à partir de sources identifiées — pas « tout le rapport d'un coup ».
3. **Imposer les standards** : modèle de document, charte rédactionnelle, glossaire, exemples de bons livrables.
4. **Vérifier chaque fait et chaque chiffre** (chapitres 5, 13, 14).
5. **Assumer** : le livrable est signé par son auteur, qui doit pouvoir le défendre ligne à ligne.

#### C.2. Les défauts typiques et leurs corrections

| Défaut | Symptôme | Correction |
|---|---|---|
| Généralités | « Dans un contexte en constante évolution… » | Exiger des faits, chiffres et exemples tirés des sources |
| Remplissage | Paragraphes qui répètent la même idée | Fixer une longueur par section ; demander la suppression des redites |
| Ton inadapté | Trop commercial, trop familier, trop affirmatif | Fournir la charte rédactionnelle et un exemple |
| Structure standard | Introduction-développement-conclusion vide | Imposer le modèle de l'entreprise |
| Affirmations vagues | « Des progrès significatifs ont été réalisés » | Exiger la quantification ou la suppression |
| Listes à puces excessives | Tout est découpé en puces | Demander une prose structurée où c'est pertinent |

#### C.3. Les formats

Avec la création de fichiers activée, Claude produit des documents Word, des classeurs Excel, des présentations et des PDF ; les modèles d'artefacts Docs, Slides et Sheets permettent d'éditer et de partager dans l'application, et les présentations Slides s'exportent en PowerPoint ou en PDF [@ANT-HC-ARTIFACTS; @ANT-HC-SKILLS]. Pour respecter la charte graphique de l'entreprise, fournissez le modèle (fichier Word ou PowerPoint) ou, dans les organisations qui l'ont configuré, utilisez le système de design de l'entreprise.

### D. Démonstration guidée — Le rapport trimestriel au conseil

**1. Cadrer** (prompt 34.1) : destinataires, objectifs, messages clés, sources, longueur, modèle.

**2. Structurer** : Claude propose un plan détaillé avec, pour chaque section, les messages, les sources et la longueur. Thomas le corrige (il fusionne deux sections et ajoute une section « décisions demandées au conseil »), puis le valide.

**3. Rédiger section par section** (prompt 34.2), dans un projet contenant le modèle, la charte rédactionnelle et les sources validées.

**4. Vérifier** : prompt de vérification par citation (chapitre 5) sur chaque section ; contrôle des chiffres contre la synthèse mensuelle validée.

**5. Relire** : grille de qualité (prompt 34.3), puis relecture par le directeur général.

**6. Décliner** : présentation (artefact Slides) et note en anglais **à partir du rapport validé**, et non de zéro.

**7. Valider et archiver** : version signée, numérotée, archivée dans le système documentaire.

### E. Prompts commentés

**Prompt 34.1 — Cadrage d'un livrable**

```text
Je prépare [livrable] pour [destinataires], qui doivent [décider / être informés de / approuver] [objet].
Messages clés que je veux faire passer : [3 à 5 messages].
Sources validées (connaissances du projet) : [liste].
Contraintes : [longueur], modèle [joint], charte rédactionnelle [jointe], ton [sobre, factuel].
Propose un plan détaillé : pour chaque section, titre, objectif, messages, sources utilisées,
longueur cible, graphiques ou tableaux prévus. N'écris pas encore le texte.
```

**Prompt 34.2 — Rédaction d'une section**

```text
Rédige la section [n° et titre] du plan validé ci-dessous.
Règles : uniquement les sources indiquées pour cette section ; chaque chiffre suivi de sa source
entre crochets [source, page] (je les retirerai à la mise en page finale) ; pas de phrase générique
d'introduction ; [N] mots maximum ; prose structurée, listes seulement pour les énumérations.
Respecte la charte rédactionnelle jointe (vocabulaire, unités, ton).
```

*Commentaire.* Les sources entre crochets pendant la rédaction rendent la vérification rapide ; elles sont supprimées à la mise en page.

**Prompt 34.3 — Grille de qualité**

```text
Évalue le projet de document selon cette grille (1 à 5) et propose des corrections précises :
1. Exactitude (chaque fait est-il sourcé ?) ; 2. Pertinence pour le destinataire ;
3. Clarté et concision (redites, généralités) ; 4. Équilibre (risques et points négatifs présents ?) ;
5. Conformité au modèle et à la charte ; 6. Actionnabilité (décisions et prochaines étapes claires ?).
Liste aussi les phrases génériques ou creuses à supprimer.
```

### F. Exercices pratiques

**Exercice 34.1 (guidé).** À partir des documents d'exercice de mars 2026, produisez une note de 2 pages au directeur général en suivant les 7 étapes. Mesurez le temps passé et comparez à votre méthode habituelle.

**Exercice 34.2 (guidé).** Prenez un livrable généré sans méthode (par exemple « Rédige un rapport sur la sécurité à la mine ») et appliquez-lui le prompt 34.3. Combien de phrases creuses relevez-vous ?

**Exercice 34.3 (autonome).** Rédigez la charte rédactionnelle de votre service (vocabulaire, unités, ton, formats) et testez son effet sur un livrable.

### G. Livrable professionnel

**Un livrable complet** de votre métier, produit selon le cycle, avec son dossier : plan validé, sources, versions, grille de qualité remplie, validation.

### H. Vérification des résultats

::: controle
- Le plan a été validé avant la rédaction.
- Chaque fait et chaque chiffre est rattaché à une source vérifiée.
- Aucune phrase générique ou affirmation vague ne subsiste.
- Le livrable respecte le modèle et la charte de l'entreprise.
- L'auteur peut défendre chaque ligne ; la version finale est signée et archivée.
:::

::: setrompe
Dans la version anglaise d'une note, Claude traduit « réserves probables » par une expression qui ne correspond pas au terme consacré du code de déclaration utilisé par l'entreprise. Dans un document destiné à un actionnaire, l'écart peut être lourd de sens. **Contre-mesure** : fournir un glossaire bilingue des termes réglementés.
:::

### I. Limites et précautions

- La signature engage l'auteur, pas l'outil.
- Les livrables destinés à l'extérieur (actionnaires, autorités, public) suivent un circuit de validation renforcé.
- Les informations privilégiées ne doivent circuler que dans les cercles autorisés.

### J. Boîte à outils

- Prompts 34.1, 34.2, 34.3.
- Check-list « avant envoi » : destinataire ; messages ; sources ; chiffres ; ton ; modèle ; version ; validation.
- Glossaire bilingue des termes réglementés (Annexe A).

### K. Quiz

1. **(Vrai ou faux)** Il est plus efficace de demander à Claude le rapport complet en une seule instruction.
2. **(Compréhension)** Pourquoi valider le plan avant la rédaction ?
3. **(QCM)** Quel défaut correspond à « Dans un contexte en constante évolution… » ? a) généralité ; b) erreur de calcul ; c) hallucination ; d) injection.
4. **(Application)** Rédigez la règle qui impose des sources entre crochets pendant la rédaction.
5. **(Mise en situation)** La présentation et la note en anglais divergent du rapport. Quelle erreur de méthode a été commise ?
6. **(Vrai ou faux)** Un glossaire bilingue est utile pour les termes réglementés.
7. **(Compréhension)** Citez trois critères de la grille de qualité.
8. **(Analyse critique)** Pourquoi l'auteur doit-il pouvoir défendre chaque ligne ?
9. **(QCM)** Quel modèle d'artefact permet d'exporter une présentation en PowerPoint ? a) Docs ; b) Slides ; c) Whiteboards ; d) Data.
10. **(Application)** Proposez deux moyens d'imposer la charte graphique de l'entreprise à un livrable.

<div class="carnet" titre="Chapitre 34 — Produire des livrables professionnels avec Claude"></div>
