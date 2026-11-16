## Chapitre 27 — Claude appliqué au droit minier, à la réglementation et à la conformité

### A. Mise en situation professionnelle

Me Henriette Ngoy, juriste principale de MCC, doit mettre à jour le **registre des obligations légales** de l'entreprise : obligations issues du Code minier tel que modifié en 2018, du règlement minier, des textes environnementaux, fiscaux, sociaux, du permis d'exploitation, de la convention avec l'État et des engagements de transparence (ITIE). Elle doit aussi revoir vingt contrats de sous-traitance avant leur renouvellement et répondre à un courrier de l'administration des mines. Me Ngoy connaît le droit ; elle manque de temps pour l'extraction systématique, la comparaison et la mise en forme.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Construire** un registre des obligations à partir de textes officiels, avec citations vérifiables.
2. **Revoir** un contrat au regard d'une liste de contrôle interne.
3. **Organiser** une veille réglementaire assistée.
4. **Préparer** une correspondance avec l'administration.
5. **Identifier** les limites de l'usage de l'IA dans le travail juridique (secret, responsabilité, actualité des textes).

### C. Comprendre avant de pratiquer — Profil du métier

Le cadre minier congolais repose notamment sur la loi n° 007/2002 portant Code minier, modifiée et complétée par la loi n° 18/001 du 9 mars 2018, publiée au Journal officiel (numéro spécial du 28 mars 2018), et sur le règlement minier, lui-même modifié en 2018 [@RDC-CODE-2018]. S'y ajoutent les obligations de transparence de la Norme ITIE 2023, mise en œuvre en RDC [@EITI-2023; @EITI-RDC], et, pour la chaîne d'approvisionnement, le guide de l'OCDE sur le devoir de diligence [@OECD-DDG].

*Tableau 27.1 — Profil de la fonction juridique et conformité.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Sécurité juridique des titres et des activités, contrats, contentieux, conformité, relations juridiques avec l'administration |
| Tâches quotidiennes | Rédaction et revue de contrats, avis juridiques, veille, correspondances, suivi des obligations, appui aux opérations |
| Difficultés | Volume et dispersion des textes ; versions consolidées pas toujours disponibles ; délais ; nombreuses obligations déclaratives |
| Documents | Textes législatifs et réglementaires, titres miniers, conventions, contrats, correspondances, décisions administratives |
| Données | Registre des obligations, échéancier, contentieux, contrats en cours |
| Livrables | Avis, contrats, registre des obligations, notes de veille, courriers |
| Assistables par Claude | Extraction d'obligations avec citations ; comparaison de contrats à un standard ; synthèses de textes ; premiers jets de courriers ; échéanciers |
| Limites | Interprétation engageante ; stratégie contentieuse ; avis juridiques signés ; secret professionnel ; actualité des textes |

::: attention
**Secret et confidentialité.** Les documents juridiques sont parmi les plus sensibles de l'entreprise (stratégie, contentieux, négociations). Leur traitement avec Claude n'est envisageable que dans un environnement d'entreprise autorisé par la charte, et parfois pas du tout (documents « restreints »). En cas de doute, abstenez-vous.
:::

::: attention
**Actualité des textes.** Un modèle de langage peut ignorer une modification récente ou confondre des versions. Travaillez **toujours** à partir du texte officiel fourni, dans sa version en vigueur, et vérifiez qu'aucun texte postérieur ne l'a modifié.
:::

![Figure 27.1 — Veille réglementaire et conformité assistées : les sources officielles et l'interprétation restent du ressort du juriste. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig27_1_veille_reglementaire.png){width=100%}

### D. Démonstration guidée — Cas d'usage

#### Cas d'usage 27.1 — Registre des obligations à partir des textes officiels

**1. Problème.** Le registre des obligations est incomplet et non sourcé.

**2. Méthode habituelle.** Lecture intégrale des textes, saisie manuelle des obligations.

**3. Contribution de Claude.** Extraction systématique, titre par titre, des obligations du titulaire d'un permis d'exploitation, avec article et citation exacte, échéance et fréquence, service concerné proposé.

**4. Données.** Textes officiels (Journal officiel, versions consolidées publiées), permis, convention.

**5. Procédure.** Découper les textes par titre ou chapitre ; extraire ; fusionner ; contrôler par échantillonnage ; faire valider l'applicabilité par la juriste ; affecter les responsables.

**6. Prompt.**

```text
[C] Juriste d'une société titulaire d'un permis d'exploitation (cuivre-cobalt) en RDC.
[A] Extrais toutes les obligations à la charge du titulaire d'un permis d'exploitation
contenues dans le texte joint.
[D] <texte_officiel> [titre ou chapitre du Code minier, version consolidée publiée] </texte_officiel>
[R] Uniquement le texte fourni. Cite exactement chaque disposition (article, alinéa).
Si une obligation renvoie à un texte d'application non fourni, indique-le.
N'interprète pas l'applicabilité à MCC (décision de la juriste).
[E] Tableau : n° | article | obligation (citation) | fréquence/échéance | sanction mentionnée |
renvoi à un autre texte | service concerné (proposition).
```

**7. Échanges successifs.** « Repère les obligations déclaratives périodiques et construis l'échéancier annuel » ; « Liste les renvois à des textes d'application, pour que je les obtienne. »

**8. Exemple de résultat (forme).**

| N° | Article | Obligation (citation) | Échéance | Renvoi | Service |
|---|---|---|---|---|---|
| 1 | [art.] | « … » | annuelle | décret d'application | Juridique / Finance |
| 2 | [art.] | « … » | avant le début des travaux | — | Environnement |

*(Les cellules sont remplies à partir du texte officiel fourni lors de l'exercice ; le livre ne reproduit pas d'article non vérifié.)*

**9. Contrôle.** Vérification de 100 % des citations par une seconde lecture humaine pour les obligations retenues ; contrôle de l'absence de modification ultérieure du texte.

**10. Erreurs possibles.** Article mal numéroté ; confusion entre texte initial et texte modifié ; obligation d'une autre catégorie de titulaire attribuée à tort.

**11. Limites.** L'applicabilité, l'interprétation et la priorisation relèvent de la juriste.

**12. Livrable.** Registre des obligations sourcé, validé, avec échéancier et responsables.

#### Cas d'usage 27.2 — Revue des contrats de sous-traitance

**1. Problème.** Vingt contrats de sous-traitance à revoir avant renouvellement, au regard du contrat type et de la politique de l'entreprise (HSE, droits humains, confidentialité, contenu local, anticorruption).

**2. Méthode habituelle.** Lecture contrat par contrat, notes manuscrites.

**3. Contribution de Claude.** Comparaison de chaque contrat avec la liste de contrôle et le contrat type, tableau des écarts avec citations, priorisation proposée.

**4. Données.** Contrats (environnement autorisé), contrat type, liste de contrôle juridique.

**5–6. Procédure et prompt.**

```text
Compare le contrat joint à notre liste de contrôle <liste> … </liste>
et à notre contrat type <type> … </type>.
Pour chaque point de la liste : présent / absent / différent ; citation de la clause du contrat
(article) ; écart par rapport au contrat type ; niveau d'attention proposé (élevé/moyen/faible) avec justification.
N'émets pas d'avis sur la validité juridique ; signale les clauses inhabituelles.
```

**7. Échanges.** « Prépare, pour les écarts d'attention élevée, une proposition de rédaction alignée sur le contrat type. »

**8. Exemple de résultat.** Pour un contrat de transport (fictif) : clause HSE présente mais sans obligation de déclaration des incidents ; clause anticorruption absente ; confidentialité conforme.

**9. Contrôle.** Revue de chaque écart « élevé » par la juriste.

**10. Erreurs possibles.** Clause présente dans une annexe non fournie, signalée à tort « absente ».

**11. Limites.** La négociation et la décision de signer relèvent de la juriste et de la direction.

**12. Livrable.** Fiche de revue par contrat et tableau de synthèse des vingt contrats.

#### Cas d'usage 27.3 — Note de veille sur un nouveau texte (condensé)

Lorsqu'un nouveau texte est publié, Claude produit, à partir du texte officiel fourni : résumé, dispositions nouvelles, dispositions modifiées (comparaison avec l'ancienne version fournie), obligations nouvelles et échéances, services concernés, questions d'interprétation à instruire. La juriste valide et diffuse.

#### Cas d'usage 27.4 — Réponse à un courrier de l'administration (condensé)

Claude analyse le courrier (demandes, délais, références citées), dresse la liste des pièces à réunir, et rédige un projet de réponse factuel, structuré point par point, à partir des éléments fournis par les services. La juriste vérifie chaque affirmation et la direction signe.

### E. Prompts commentés

**Prompt 27.1 — Comparer deux versions d'un texte**

```text
Voici l'ancienne version <v1> … </v1> et la nouvelle version <v2> … </v2> d'un texte.
Présente un tableau des différences : article | ancienne rédaction | nouvelle rédaction |
nature (ajout, suppression, modification) | effet potentiel à examiner (formulé comme une question).
Ne conclus pas sur la portée juridique.
```

*Commentaire.* La comparaison mécanique est une tâche où Claude excelle ; la portée juridique reste au juriste, d'où la formulation « comme une question ».

### F. Exercices pratiques

**Exercice 27.1 (guidé).** Avec le texte officiel d'un chapitre du Code minier (version publiée que vous obtiendrez auprès d'une source officielle), réalisez le cas 27.1 et vérifiez toutes les citations.

**Exercice 27.2 (guidé).** Avec le contrat d'acide fourni en exercice et une liste de contrôle de 8 points (à rédiger), réalisez le cas 27.2.

**Exercice 27.3 (autonome).** Construisez l'échéancier annuel des obligations déclaratives de votre entreprise à partir des textes applicables.

### G. Livrable professionnel

**Registre des obligations légales** sourcé et validé, **fiches de revue de contrats**, **procédure de veille** décrivant le rôle de Claude et les validations.

### H. Vérification des résultats

::: controle
- Chaque citation est vérifiée mot pour mot dans le texte officiel en vigueur.
- L'absence de modification ultérieure du texte est vérifiée.
- Les clauses signalées « absentes » ont été recherchées dans les annexes.
- Aucun avis juridique engageant n'est diffusé sans validation et signature.
:::

::: setrompe
C'est l'exemple du chapitre 5 : sans texte fourni, un assistant peut citer un article inexistant avec un numéro et une référence de publication plausibles. En droit, **aucune référence ne doit être utilisée sans avoir été lue dans la source officielle**.
:::

### I. Limites et précautions

- Le travail juridique engage la responsabilité professionnelle du juriste.
- Les textes nationaux sont parfois mal indexés sur le Web : privilégiez les sources officielles et les versions consolidées publiées.
- Certains documents (stratégie contentieuse, négociations sensibles) ne doivent pas être traités par un outil d'IA.

### J. Boîte à outils

- Prompts des cas 27.1, 27.2 et prompt 27.1.
- Gabarit de registre des obligations : n° | texte | article | obligation | fréquence | échéance | responsable | preuve | statut.
- Règle : « texte officiel fourni + citation exacte + validation du juriste ».

### K. Quiz

1. **(QCM)** Quelle loi a modifié le Code minier congolais en 2018 ? a) la loi n° 007/2002 ; b) la loi n° 18/001 du 9 mars 2018 ; c) le décret n° 038/2003 ; d) aucune.
2. **(Vrai ou faux)** Claude peut décider si une obligation s'applique à l'entreprise.
3. **(Compréhension)** Pourquoi faut-il vérifier qu'un texte n'a pas été modifié ultérieurement ?
4. **(Mise en situation)** Claude signale une clause anticorruption « absente ». Que vérifiez-vous avant de conclure ?
5. **(Vrai ou faux)** Les documents de stratégie contentieuse peuvent être traités sans restriction avec n'importe quel compte.
6. **(Application)** Rédigez la règle qui interdit à Claude d'interpréter la portée juridique d'une modification.
7. **(QCM)** Quelle norme internationale porte sur la transparence des revenus des industries extractives ? a) GISTM ; b) Norme ITIE ; c) ISO 45001 ; d) GRI 14.
8. **(Compréhension)** À quoi sert la colonne « renvoi à un autre texte » du registre ?
9. **(Analyse critique)** Pourquoi la comparaison de versions est-elle une bonne tâche pour Claude, et l'avis juridique une mauvaise ?
10. **(Application)** Citez trois rubriques d'une note de veille réglementaire.

<div class="carnet" titre="Chapitre 27 — Claude appliqué au droit minier, à la réglementation et à la conformité"></div>
