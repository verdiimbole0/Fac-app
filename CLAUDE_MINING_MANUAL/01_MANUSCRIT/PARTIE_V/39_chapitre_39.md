## Chapitre 39 — Éthique, responsabilité et transformation du travail

### A. Mise en situation professionnelle

Lors d'une réunion avec les délégués du personnel, une question directe est posée à Béatrice Musau : « Est-ce que l'IA va supprimer des postes à MCC ? » Un autre délégué ajoute : « Et si l'IA écrit un rapport faux qui conduit à un accident, qui est responsable ? » Le lendemain, un chef de village demande à Joseph Banza si « la machine qui écrit » va décider des indemnisations. Ces questions ne sont pas techniques ; elles sont éthiques, sociales et politiques. Elles méritent des réponses honnêtes.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Identifier** les principaux enjeux éthiques de l'usage de l'IA dans une entreprise minière.
2. **Expliquer** les principes de responsabilité humaine et de transparence.
3. **Analyser** les effets possibles de l'IA sur les métiers et proposer des mesures d'accompagnement.
4. **Intégrer** les parties prenantes (salariés, représentants, communautés) dans la démarche.
5. **Argumenter** de façon honnête, sans alarmisme ni promesse excessive.

### C. Comprendre avant de pratiquer

#### C.1. Les repères internationaux

La **Recommandation de l'UNESCO sur l'éthique de l'intelligence artificielle**, adoptée en novembre 2021 par les 193 États membres, constitue le premier instrument normatif mondial en la matière ; elle met notamment en avant la protection des droits humains et de la dignité, la transparence, la responsabilité, la non-discrimination, la protection de l'environnement et la supervision humaine [@UNESCO-2021]. Le cadre du NIST insiste sur des systèmes d'IA dignes de confiance — valides et fiables, sûrs, sécurisés, responsables et transparents, explicables, respectueux de la vie privée et équitables [@NIST-RMF].

#### C.2. Cinq questions éthiques pour une mine

| Enjeu | Question | Réponse de principe à MCC |
|---|---|---|
| Responsabilité | Qui répond d'une erreur ? | L'humain qui valide et signe ; l'organisation qui a fixé les règles. L'outil n'est jamais « responsable ». |
| Transparence | Doit-on dire qu'un document a été préparé avec l'IA ? | Oui, selon la charte, lorsque cela est pertinent pour le destinataire (documents externes, relations avec les communautés). |
| Équité | L'IA peut-elle discriminer ? | Oui, par des biais ; d'où l'exclusion des décisions individuelles et les relectures anti-biais. |
| Dignité | Peut-on traiter des personnes vulnérables par l'IA ? | Avec la plus grande prudence : minimisation, relation humaine, aucune décision automatisée. |
| Environnement | L'IA a-t-elle une empreinte ? | Oui (calcul, énergie) : usage proportionné, choix de modèles adaptés à la tâche. |

#### C.3. L'IA et le travail : ce que l'on sait, ce que l'on ne sait pas

La numérisation et l'automatisation transforment depuis plusieurs décennies le secteur minier, avec des effets sur l'emploi local, les compétences demandées et l'approvisionnement local. Anthropic publie un **Economic Index** qui mesure les usages observés de Claude par types de tâches professionnelles ; ces données décrivent des **usages**, et ne permettent pas, à elles seules, de conclure sur les suppressions ou créations d'emplois [@ANT-ECON].

Pour une entreprise comme MCC, l'analyse honnête est la suivante (interprétation de l'auteur) :

- l'IA générative transforme surtout des **tâches** (rédaction, synthèse, analyse documentaire), plus que des **métiers entiers** ;
- elle peut libérer du temps pour le terrain, l'analyse, la relation — si l'organisation le décide ;
- certaines fonctions très documentaires peuvent évoluer fortement ;
- de nouvelles compétences deviennent nécessaires : formulation, vérification, gestion des données, gouvernance ;
- les effets dépendent des **choix de l'entreprise**, pas de la technologie seule.

::: retenir
« L'IA va-t-elle supprimer des postes ? » La réponse honnête n'est ni « non, jamais » ni « oui, beaucoup », mais : « Cela dépend des décisions que nous prenons ensemble ; voici nos engagements, voici comment nous mesurons, voici comment nous vous associons. »
:::

#### C.4. Les communautés et la fracture numérique

Dans les villages riverains, l'accès au numérique est souvent limité. L'usage de l'IA par l'entreprise ne doit pas créer de nouvelle asymétrie : les communautés doivent pouvoir comprendre comment leurs plaintes sont traitées, obtenir une réponse humaine et contester. Les décisions qui les concernent (indemnisations, emplois, projets) restent des décisions humaines, prises selon les procédures et dans le dialogue.

### D. Démonstration guidée — Préparer le dialogue social

Béatrice prépare la réunion avec les délégués du personnel :

1. Elle rassemble les faits : périmètre du pilote, usages autorisés et interdits (charte), mesures de gains (chapitre 36), plan de formation.
2. Elle demande à Claude d'identifier les questions et inquiétudes probables des délégués (prompt 39.1).
3. Elle prépare, avec la direction, des **engagements** réalistes : aucune décision individuelle par l'IA ; formation de tous les utilisateurs ; information préalable sur tout nouveau cas d'usage ; bilan annuel partagé ; dispositif de signalement.
4. Elle rédige avec Claude un support clair, puis le relit pour s'assurer qu'aucune promesse non décidée n'y figure.
5. La réunion débouche sur la création d'un point annuel « IA et travail » au sein des instances de dialogue social.

### E. Prompts commentés

**Prompt 39.1 — Anticiper les préoccupations des parties prenantes**

```text
Nous présentons notre programme d'IA générative (pilote de 40 utilisateurs, usages documentaires,
décisions individuelles exclues) aux représentants du personnel d'une mine.
Liste les 12 préoccupations les plus probables (emploi, surveillance, responsabilité, compétences,
charge de travail, équité…), et pour chacune : les faits dont nous disposons, ce que nous ne savons pas,
et les questions à leur retourner. Ne propose pas d'engagement : la direction les décidera.
```

*Commentaire.* Distinguer « ce que nous savons » et « ce que nous ne savons pas » est la base d'un dialogue honnête.

**Prompt 39.2 — Analyse éthique d'un cas d'usage**

```text
Analyse le cas d'usage suivant selon cinq dimensions : responsabilité, transparence, équité,
dignité des personnes, environnement. Pour chacune : risques, personnes concernées, mesures,
questions à soumettre au comité. Cas : [description].
```

### F. Exercices pratiques

**Exercice 39.1 (guidé).** Appliquez le prompt 39.2 à trois cas d'usage : rapport d'incident (ch. 23), réponse aux plaintes (ch. 25), annonce de recrutement (ch. 30). Comparez les risques.

**Exercice 39.2 (guidé).** Rédigez la réponse orale (2 minutes) à la question « L'IA va-t-elle supprimer des postes ? », en vous appuyant sur l'encadré « À retenir ».

**Exercice 39.3 (autonome).** Proposez trois engagements de votre entreprise envers les salariés et trois envers les communautés concernant l'usage de l'IA.

### G. Livrable professionnel

**Note éthique du programme IA** : principes, usages exclus, engagements envers les salariés et les communautés, dispositif de signalement et de recours, bilan annuel.

### H. Vérification des résultats

::: controle
- Chaque cas d'usage a été analysé selon les cinq dimensions.
- Aucune décision individuelle concernant une personne n'est confiée à l'IA.
- Les engagements annoncés sont décidés, réalistes et suivis.
- Un dispositif de signalement et de recours existe et est connu.
:::

::: setrompe
Interrogé sur « l'impact de l'IA sur l'emploi minier », un assistant peut produire des pourcentages précis de postes « menacés », sans source vérifiable. Ce type de chiffre, repris dans une réunion sociale, peut provoquer des tensions graves. Ne citez que des données sourcées, et présentez-les avec leurs limites.
:::

### I. Limites et précautions

- L'éthique ne se délègue pas à une check-list : elle suppose délibération et responsabilité.
- Les engagements non tenus détruisent la confiance plus sûrement que l'absence d'engagement.
- La transparence vis-à-vis des communautés doit être adaptée (langue, canaux, accessibilité).

### J. Boîte à outils

- Prompts 39.1, 39.2.
- Grille éthique à cinq dimensions (tableau C.2).
- Formule de réponse honnête sur l'emploi (encadré « À retenir »).

### K. Quiz

1. **(QCM)** En quelle année la Recommandation de l'UNESCO sur l'éthique de l'IA a-t-elle été adoptée ? a) 2017 ; b) 2019 ; c) 2021 ; d) 2024.
2. **(Vrai ou faux)** En cas d'erreur d'un rapport préparé avec Claude, la responsabilité incombe à l'outil.
3. **(Compréhension)** Pourquoi l'IA transforme-t-elle plutôt des tâches que des métiers entiers ?
4. **(Mise en situation)** Un chef de village demande si « la machine » décidera des indemnisations. Que répondez-vous ?
5. **(Vrai ou faux)** Les données d'usage de l'Anthropic Economic Index permettent de conclure directement sur les suppressions d'emplois.
6. **(Compréhension)** Citez trois caractéristiques d'une IA digne de confiance selon le NIST.
7. **(Application)** Proposez un engagement envers les salariés concernant l'IA.
8. **(Analyse critique)** Pourquoi un engagement non tenu est-il pire qu'une absence d'engagement ?
9. **(Compréhension)** Pourquoi l'empreinte environnementale de l'IA est-elle un enjeu éthique ?
10. **(Application)** Rédigez la réponse honnête à « L'IA va-t-elle supprimer des postes ? » en trois phrases.

<div class="carnet" titre="Chapitre 39 — Éthique, responsabilité et transformation du travail"></div>
