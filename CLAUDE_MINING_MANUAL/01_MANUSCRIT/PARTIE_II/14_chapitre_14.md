## Chapitre 14. Utiliser Claude pour la recherche, la documentation et la vérification des sources

### A. Mise en situation professionnelle

Clarisse Mpoyi, responsable ESG et conformité de la chaîne d'approvisionnement, doit préparer pour le conseil d'administration une note sur les exigences internationales applicables au cobalt de MCC : devoir de diligence, transparence, gestion des résidus, reporting de durabilité. Le conseil veut des références précises. Clarisse sait que Claude peut rechercher sur le Web ; elle sait aussi, depuis le chapitre 5, qu'une référence produite par une IA doit être vérifiée. Comment tirer parti de la recherche assistée sans importer d'erreurs dans une note destinée au conseil ?

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Distinguer** les connaissances internes du modèle, la recherche Web et la recherche approfondie (Research).
2. **Formuler** une demande de recherche précise, avec exigence de sources.
3. **Évaluer** la fiabilité d'une source selon une hiérarchie adaptée au sujet.
4. **Vérifier** une référence (existence, auteur, date, contenu) avant de la citer.
5. **Tenir** un registre de sources et citer selon les normes APA.

### C. Comprendre avant de pratiquer

#### C.1. Trois niveaux de « recherche »

| Niveau | Ce que fait Claude | Fiabilité pour les faits récents ou précis |
|---|---|---|
| Connaissances internes | Répond à partir de son entraînement (date limite) | Faible : aucune source vérifiable, risque d'hallucination |
| Recherche Web | Interroge le Web pendant la conversation et cite les pages consultées | Moyenne à bonne, selon les sources trouvées |
| Recherche approfondie (*Research*) | Conduit plusieurs recherches successives sur le Web et dans les outils connectés, puis rédige un rapport avec sources | Bonne base de travail, à vérifier |

La recherche Web est disponible sur toutes les offres, y compris gratuite ; la recherche approfondie est réservée aux offres payantes [@ANT-PLANS]. Selon le centre d'aide, la recherche approfondie nécessite que la recherche Web soit activée, peut utiliser les connecteurs activés (sauf lorsqu'elle est lancée depuis l'application mobile, où elle se limite au Web, sans avertissement), consomme davantage d'utilisation qu'une conversation ordinaire et s'exécute sur Claude Opus 5.5 [@ANT-HC-RESEARCH].

Pour les développeurs, l'API propose une fonction de **citations** qui ancre les réponses dans des passages précis des documents fournis [@ANT-CITE].

#### C.2. Une source n'est pas une preuve tant qu'elle n'est pas vérifiée

Une page citée par Claude peut :

- ne pas exister (lien erroné) ;
- exister mais ne pas dire ce que Claude lui attribue ;
- être ancienne, ou remplacée par une version plus récente ;
- être peu fiable (blog anonyme, contenu promotionnel) ;
- être une source secondaire qui déforme la source primaire.

![Figure 14.1. Hiérarchie de fiabilité des sources. Une réponse de Claude sans source n'est qu'un point de départ. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig14_1_pyramide_sources.png){width=80%}

#### C.3. Remonter à la source primaire

Pour un sujet réglementaire ou normatif, la source primaire est le texte lui-même : le Journal officiel pour une loi congolaise [@RDC-CODE-2018], le site de l'organisme pour une norme (par exemple la Norme ITIE 2023 sur le site de l'ITIE [@EITI-2023]), la publication originale pour un rapport (par exemple les statistiques de l'USGS [@USGS-MCS2026]). Un article de presse ou un blog qui « résume » une norme est une source secondaire : utile pour comprendre, insuffisante pour citer.

#### C.4. Vérifier une référence : la méthode des cinq contrôles

1. **Existence** : le document existe-t-il ? (recherche du titre exact, site de l'éditeur)
2. **Identité** : titre, auteur ou organisme, date et éditeur sont-ils exacts ?
3. **Accès** : l'URL ou le DOI mène-t-il bien au document ?
4. **Contenu** : le document dit-il réellement ce qui lui est attribué ? (lire le passage)
5. **Actualité** : existe-t-il une version plus récente ? (par exemple une nouvelle édition d'une norme)

::: application
C'est la méthode utilisée pour constituer la bibliographie de ce livre : chaque référence a été contrôlée, et toute référence dont l'édition, la date ou le contenu suscitait un doute a été écartée, même lorsqu'elle paraissait plausible.
:::

#### C.5. Citer selon les normes APA

Les normes **APA** (*American Psychological Association*, 7e édition) sont largement utilisées dans les rapports professionnels et académiques. Principe : une citation courte dans le texte, (Auteur, année), renvoie à une référence complète dans la bibliographie.

*Exemples (référence complète) :*

- Rapport institutionnel : U.S. Geological Survey. (2026). *Mineral commodity summaries 2026*. U.S. Geological Survey. https://pubs.usgs.gov/publication/mcs2026
- Page Web sans date : Anthropic. (s.d.). *Effort*. Claude Platform Docs. https://platform.claude.com/docs/en/build-with-claude/effort (consulté le 16 novembre 2026)

Pour les pages Web susceptibles d'évoluer, indiquez toujours la **date de consultation**.

### D. Démonstration guidée : La note de Clarisse

**Étape 1. Cartographier.** Clarisse demande à Claude, sans recherche, la liste des référentiels internationaux pertinents pour un producteur de cobalt (prompt 14.1). Elle obtient une liste de travail (devoir de diligence de l'OCDE, Norme ITIE, GISTM, Normes de performance de la SFI, etc.) qu'elle traite comme une **hypothèse**.

**Étape 2. Rechercher avec sources.** Elle lance une recherche approfondie, en exigeant des sources primaires et la date de chaque document (prompt 14.2).

**Étape 3. Vérifier.** Pour chaque référence, elle applique les cinq contrôles. Elle constate notamment que la norme de l'ITIE en vigueur est l'édition 2023 [@EITI-2023], et écarte une référence de reporting dont deux versions circulaient sans qu'elle puisse établir laquelle était applicable.

**Étape 4. Registre.** Elle consigne chaque source dans un registre (prompt 14.4).

**Étape 5. Rédiger.** Elle rédige la note avec Claude, à partir **uniquement** des sources vérifiées (prompt 14.3), puis relit chaque citation.

### E. Prompts commentés

**Prompt 14.1. Cartographie préliminaire (à vérifier)**

```text
Je prépare une note pour le conseil d'administration d'un producteur de cuivre
et de cobalt en RDC. Liste les principaux référentiels internationaux
(normes, guides, conventions, standards de reporting) applicables à :
devoir de diligence sur la chaîne d'approvisionnement, transparence des revenus,
gestion des résidus, performance environnementale et sociale, reporting de durabilité.
Pour chacun : organisme, objet en une phrase.
Précise que cette liste est préliminaire et doit être vérifiée ; n'indique
ni date, ni numéro de version, ni URL à ce stade.
```

*Commentaire.* En interdisant dates, versions et URL, on évite les détails les plus exposés à l'hallucination à une étape où aucune recherche n'a été faite.

**Prompt 14.2. Recherche avec exigences de sources**

```text
Utilise la recherche pour vérifier et compléter la liste précédente.
Pour chaque référentiel :
- titre exact et version ou édition en vigueur ;
- organisme éditeur ;
- date de publication et, le cas échéant, date d'entrée en vigueur ;
- URL de la page officielle de l'organisme (pas un blog ni un article de presse) ;
- une phrase sur son application à un producteur de cobalt.
Si tu ne trouves pas de source officielle pour un élément, écris « non vérifié ».
Distingue clairement sources primaires et sources secondaires.
```

**Prompt 14.3. Rédiger uniquement à partir de sources vérifiées**

```text
Voici mon registre de sources vérifiées : <sources> … </sources>
Rédige la note (2 pages) en t'appuyant uniquement sur ces sources.
Après chaque affirmation, indique la source entre parenthèses au format (Auteur, année).
N'introduis aucune référence qui ne figure pas dans le registre.
```

**Prompt 14.4. Fiche de registre**

```text
Pour la source suivante [titre / URL], prépare une fiche de registre :
type de document | auteur ou organisme | titre exact | date | éditeur | URL | DOI s'il existe |
date de consultation : [date] | référence complète APA 7e édition | passage utilisé.
Marque chaque champ que tu n'as pas pu vérifier sur la source elle-même.
```

### F. Exercices pratiques

**Exercice 14.1 (guidé) : Les cinq contrôles**

Appliquez les cinq contrôles aux trois références suivantes et notez vos constats : (1) la Norme mondiale de l'industrie sur la gestion des résidus miniers ; (2) le recueil de directives pratiques de l'OIT sur la sécurité et la santé dans les mines à ciel ouvert ; (3) les « Mineral Commodity Summaries » de l'USGS. *Indice : vérifiez l'année et l'édition de chacune [@GISTM-2020; @ILO-OPENCAST; @USGS-MCS2026].*

**Exercice 14.2 (guidé) : Débusquer une référence fragile**

Demandez à Claude, sans recherche, trois références scientifiques sur « l'IA générative appliquée à la maintenance minière ». Vérifiez chacune. Combien existent réellement, avec les bons auteurs et la bonne revue ?

**Exercice 14.3 (autonome) : Votre veille réglementaire**

Pour votre métier, constituez un registre de 8 sources de référence (textes, normes, guides), vérifiées selon les cinq contrôles, avec leur référence APA.

### G. Livrable professionnel

**Registre de sources** (format tableur) et **note documentée** dont chaque affirmation renvoie à une source du registre.

### H. Vérification des résultats

::: controle
- Chaque référence citée figure dans le registre et a passé les cinq contrôles.
- Les sources primaires sont privilégiées pour les sujets réglementaires et normatifs.
- La version ou l'édition en vigueur a été vérifiée.
- Les dates de consultation des pages Web sont indiquées.
- Aucune référence n'a été ajoutée par Claude lors de la rédaction finale.
:::

::: setrompe
Lors d'une recherche, Claude cite une page officielle réelle, mais lui attribue une exigence qui figure en réalité dans un autre document du même organisme. Le lien fonctionne, la source est fiable… mais le contenu attribué est faux. **Contre-mesure** : le contrôle n° 4 (contenu) : lire le passage dans la source.
:::

### I. Limites et précautions

- La recherche Web dépend des pages accessibles : certaines normes sont payantes, certains textes nationaux mal indexés.
- Les résultats de recherche peuvent contenir des pages piégées (injections de prompt, chapitre 38) : restez vigilant sur les instructions inattendues dans une réponse.
- La recherche approfondie consomme davantage d'utilisation : réservez-la aux questions qui le justifient.

### J. Boîte à outils

**Grille d'évaluation rapide d'une source**

| Critère | Question |
|---|---|
| Autorité | Qui publie ? Est-ce l'auteur ou l'organisme de référence ? |
| Primarité | Est-ce le texte original ou un résumé ? |
| Date | Est-ce la version en vigueur ? |
| Objectivité | Y a-t-il un intérêt commercial ou militant ? |
| Traçabilité | Peut-on retrouver le document par un lien stable ou un DOI ? |

### K. Quiz

1. **(QCM)** Quelle fonction conduit plusieurs recherches successives et produit un rapport sourcé ? a) la mémoire ; b) la recherche approfondie (Research) ; c) le mode incognito ; d) les préférences.
2. **(Vrai ou faux)** Une source citée par Claude avec un lien qui fonctionne est forcément exacte.
3. **(Compréhension)** Citez les cinq contrôles de vérification d'une référence.
4. **(Vrai ou faux)** Lancée depuis l'application mobile, la recherche approfondie utilise aussi vos connecteurs.
5. **(QCM)** Quelle est la source primaire pour une loi congolaise ? a) un article de presse ; b) le Journal officiel ; c) un blog juridique ; d) la réponse de Claude.
6. **(Application)** Rédigez la référence APA d'une page Web sans date consultée aujourd'hui.
7. **(Mise en situation)** Claude cite une norme « édition 2018 », mais vous savez qu'une révision existe. Que faites-vous ?
8. **(Compréhension)** Pourquoi interdire les dates et URL lors d'une cartographie préliminaire sans recherche ?
9. **(Analyse critique)** Quelle est la limite d'un article de presse qui résume une norme ?
10. **(Vrai ou faux)** Une référence dont on n'a pas pu vérifier l'édition ou le contenu peut figurer dans une bibliographie si elle paraît plausible.

<div class="carnet" titre="Chapitre 14. Utiliser Claude pour la recherche, la documentation et la vérification des sources"></div>
