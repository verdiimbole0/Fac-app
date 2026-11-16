## Chapitre 32 — Claude appliqué à l'ESG, à la traçabilité minérale et à l'approvisionnement responsable

### A. Mise en situation professionnelle

Un acheteur européen de l'hydroxyde de cobalt de MCC envoie un questionnaire de devoir de diligence de 140 questions : origine du minerai, risques liés à l'exploitation artisanale voisine, droits humains, gestion des résidus, émissions de gaz à effet de serre, transparence des paiements. Il demande aussi le rapport de durabilité annuel conforme aux normes de reporting applicables. Clarisse Mpoyi, responsable ESG et conformité de la chaîne d'approvisionnement, a trois semaines. L'enjeu est commercial (le contrat de vente en dépend) et réputationnel : toute affirmation inexacte pourrait être qualifiée d'écoblanchiment.

### B. Objectifs d'apprentissage

À la fin de ce chapitre, vous serez capable de :

1. **Expliquer** les principaux référentiels de devoir de diligence et de reporting applicables à un producteur de cobalt.
2. **Répondre** à un questionnaire de diligence avec des réponses fondées sur des preuves.
3. **Structurer** l'analyse des risques de la chaîne d'approvisionnement selon le cadre de l'OCDE.
4. **Préparer** un rapport de durabilité traçable et prudent.
5. **Prévenir** l'écoblanchiment et les affirmations non étayées.

### C. Comprendre avant de pratiquer — Profil du métier

Plusieurs référentiels encadrent ce domaine :

- le **Guide de l'OCDE sur le devoir de diligence** pour des chaînes d'approvisionnement responsables en minerais provenant de zones de conflit ou à haut risque, qui propose un cadre en cinq étapes [@OECD-DDG] ;
- la **Norme ITIE 2023**, pour la transparence des revenus, des contrats et de la propriété effective [@EITI-2023] ;
- les **Normes de performance** de la SFI [@IFC-PS] ;
- la **GISTM** pour les résidus [@GISTM-2020].

La place de la RDC dans la production mondiale de cobalt — environ 73 % de la production minière en 2025 selon l'USGS [@USGS-MCS2026] — explique l'attention particulière portée à la traçabilité de ce métal, notamment au regard de l'exploitation artisanale.

*Tableau 32.1 — Profil de la fonction ESG et conformité de la chaîne d'approvisionnement.*

| Dimension | Contenu |
|---|---|
| Responsabilités | Politique ESG, devoir de diligence, traçabilité, reporting de durabilité, réponses aux clients et investisseurs |
| Tâches quotidiennes | Collecte de données ESG, questionnaires, audits, analyses de risques, rapports |
| Difficultés | Multiplicité des référentiels ; données dispersées ; preuves ; attentes élevées ; risque d'écoblanchiment |
| Documents | Politiques, rapports de diligence, rapports d'audit tiers, rapports de durabilité, questionnaires clients, données ITIE |
| Données | Origine du minerai, chaîne de possession, indicateurs environnementaux et sociaux, émissions, incidents |
| Livrables | Réponses aux questionnaires, rapport annuel de diligence, rapport de durabilité, tables de correspondance |
| Assistables par Claude | Pré-remplissage à partir de preuves ; tables de correspondance entre référentiels ; contrôle de cohérence ; rédaction prudente ; détection des affirmations non étayées |
| Limites | Évaluation des risques en droits humains (terrain, experts), audits indépendants, engagements publics, certification |

![Figure 32.1 — Le cadre en cinq étapes du devoir de diligence de l'OCDE et l'appui possible de Claude. Étapes d'après OCDE (2016) ; rôles de Claude : proposition de l'auteur. Illustration réalisée pour cet ouvrage.](02_ILLUSTRATIONS/SCHEMAS/fig32_1_devoir_diligence_ocde.png){width=100%}

::: attention
**Écoblanchiment.** Une affirmation ESG sans preuve (« zéro risque de travail des enfants », « production neutre en carbone ») peut engager la responsabilité de l'entreprise et détruire sa crédibilité. Avec Claude, la règle est absolue : **pas de preuve, pas d'affirmation**.
:::

### D. Démonstration guidée — Cas d'usage

#### Cas d'usage 32.1 — Réponse au questionnaire de devoir de diligence

**1. Problème.** 140 questions, trois semaines, des preuves dispersées dans plusieurs services.

**2. Méthode habituelle.** Copier-coller de réponses antérieures, risque d'incohérence et de réponses non étayées.

**3. Contribution de Claude.** Classement des questions par thème et par service ; pré-remplissage **à partir de la bibliothèque de preuves** fournie ; marquage des réponses sans preuve ; contrôle de cohérence avec les réponses précédentes et le rapport de durabilité.

**4. Données.** Questionnaire ; bibliothèque de preuves (politiques, rapports d'audit tiers, procédures, données, rapport ITIE) ; réponses de l'année précédente.

**5. Procédure.** Projet « ESG — Questionnaires clients » ; bibliothèque de preuves en connaissances du projet ; traitement par thème ; validation par chaque service ; validation finale par Clarisse et la direction.

**6. Prompt.**

```text
[C] Responsable ESG de MCC (cuivre-cobalt, RDC). Un client nous adresse un questionnaire de devoir de diligence.
[A] Prépare un projet de réponse pour les questions du thème « [thème] ».
[D] Questions : <questions> … </questions>. Bibliothèque de preuves (connaissances du projet).
[R] Chaque réponse doit citer le document de preuve (titre, date, section). Si aucune preuve n'existe,
réponds « [À instruire — aucune preuve disponible] » et propose la preuve à rechercher.
N'utilise aucune formulation absolue (« aucun », « zéro », « totalement ») sans preuve explicite.
Ne déduis pas une pratique d'une politique : une politique n'est pas la preuve de son application.
[E] Tableau : n° | question | projet de réponse | preuve citée | service à valider | statut.
```

**7. Échanges successifs.** « Compare ces réponses avec celles de l'an dernier et signale les changements » ; « Liste les questions pour lesquelles notre seule preuve est une politique, sans preuve d'application. »

**8. Exemple de résultat (extrait, fictif).**

| N° | Question | Projet de réponse | Preuve | Statut |
|---|---|---|---|---|
| 37 | Le minerai artisanal peut-il entrer dans vos flux ? | L'usine n'est alimentée que par les fosses de MCC ; des contrôles d'accès et un rapprochement des tonnages sont en place… | Procédure de contrôle des flux (2025, § 3) ; rapport d'audit tiers 2025 (§ 4.2) | À valider (Opérations) |
| 52 | Réalisez-vous des évaluations d'impact sur les droits humains ? | [À instruire — aucune preuve disponible] ; rechercher : évaluation 2024 ? | — | Bloquant |

**9. Contrôle.** Chaque service valide ses réponses ; Clarisse vérifie que chaque preuve citée dit bien ce qui est affirmé.

**10. Erreurs possibles.** Réponse affirmative fondée sur une simple politique ; preuve obsolète ; chiffre d'une année antérieure.

**11. Limites.** Les engagements et déclarations envoyés au client sont signés par la direction.

**12. Livrable.** Questionnaire complété, avec index des preuves.

#### Cas d'usage 32.2 — Table de correspondance entre référentiels

**1. Problème.** Les mêmes données servent à plusieurs référentiels (normes de reporting de durabilité, ITIE, exigences clients, ICMM), sous des formulations différentes.

**2. Méthode habituelle.** Tableaux ad hoc, doublons de collecte.

**3. Contribution de Claude.** À partir des listes d'exigences **fournies** (extraits des référentiels), table de correspondance exigence → donnée → source → responsable, et repérage des données manquantes.

**4. Données.** Extraits officiels des référentiels ; inventaire des données ESG de MCC.

**5–6. Prompt.**

```text
Voici trois listes d'exigences extraites des référentiels (textes officiels fournis) :
<reporting> … </reporting> <itie> … </itie> <client> … </client>.
Voici notre inventaire de données ESG : <inventaire> … </inventaire>.
Construis une table : exigence (référentiel, numéro) | donnée de l'inventaire correspondante |
source | responsable | statut (disponible / partielle / manquante).
Ne crée pas d'exigence qui ne figure pas dans les extraits.
```

**7. Échanges.** « Regroupe les exigences qui portent sur la même donnée, pour une collecte unique. »

**8. Exemple de résultat.** Table de 120 lignes, dont 18 données manquantes (par exemple, un indicateur de biodiversité non suivi).

**9. Contrôle.** Revue des correspondances par l'équipe ESG ; vérification des numéros d'exigences dans les textes officiels.

**10. Erreurs possibles.** Correspondance approximative entre exigences voisines mais différentes.

**11. Limites.** L'interprétation d'une exigence de norme relève de l'équipe ESG (et, le cas échéant, des auditeurs).

**12. Livrable.** Table de correspondance, plan de collecte unifié.

#### Cas d'usage 32.3 — Rapport annuel de diligence et de durabilité (condensé)

Claude rédige les sections à partir des données validées et de la table de correspondance, en appliquant une **vérification d'affirmations** : chaque phrase factuelle est rattachée à une preuve, sinon supprimée ou reformulée (technique de vérification par citation, chapitre 5). Il signale les formulations promotionnelles. Les tiers vérificateurs et la direction valident.

#### Cas d'usage 32.4 — Surveillance documentaire des risques (condensé)

Claude aide à structurer la veille des risques (rapports d'organisations, presse, décisions publiques) concernant la zone d'approvisionnement : résumé, source, date, pertinence pour MCC, action proposée. Chaque information est vérifiée à la source ; les évaluations de risques en droits humains reposent sur des enquêtes de terrain et des experts.

### E. Prompts commentés

**Prompt 32.1 — Détecteur d'affirmations non étayées**

```text
Relis le projet de rapport de durabilité ci-dessous. Pour chaque phrase contenant une affirmation
factuelle, indique : affirmation | preuve citée (oui/non) | caractère absolu ou promotionnel (oui/non) |
reformulation prudente proposée. Termine par la liste des affirmations à supprimer faute de preuve.
<projet> … </projet>
```

*Commentaire.* Ce prompt transforme Claude en relecteur anti-écoblanchiment, l'un de ses usages les plus utiles et les moins risqués en ESG.

### F. Exercices pratiques

**Exercice 32.1 (guidé).** Rédigez dix questions de diligence (origine, artisanal, droits humains, résidus, transparence) et une mini-bibliothèque de preuves fictives ; appliquez le cas 32.1.

**Exercice 32.2 (guidé).** Appliquez le prompt 32.1 au rapport de durabilité public d'une entreprise minière de votre choix (rapport publié) : combien d'affirmations sont absolues ou non étayées dans le texte même ?

**Exercice 32.3 (autonome).** Construisez la table de correspondance (cas 32.2) pour cinq indicateurs environnementaux de votre site.

### G. Livrable professionnel

**Dossier ESG** : questionnaire client complété avec index des preuves, table de correspondance des référentiels, rapport annuel avec vérification d'affirmations.

### H. Vérification des résultats

::: controle
- Chaque affirmation est rattachée à une preuve vérifiée, datée et pertinente.
- Aucune formulation absolue sans preuve.
- Les politiques ne sont pas présentées comme preuves de leur application.
- Les numéros d'exigences des référentiels ont été vérifiés dans les textes officiels.
- Les engagements publics sont validés par la direction.
:::

::: setrompe
Pour combler une réponse vide, un assistant peut écrire : « MCC applique une politique de tolérance zéro et aucun cas n'a été identifié. » La phrase est plausible, rassurante… et sans preuve. C'est exactement ce que la règle « pas de preuve, pas d'affirmation » doit empêcher.
:::

### I. Limites et précautions

- Les évaluations de risques en droits humains exigent des enquêtes de terrain et des experts.
- Les audits tiers et la vérification indépendante des rapports ne peuvent être remplacés par l'IA.
- Les données ESG sensibles (incidents, litiges, communautés) suivent la classification de l'entreprise.

### J. Boîte à outils

- Prompts des cas 32.1, 32.2 et prompt 32.1.
- Règle d'or : « pas de preuve, pas d'affirmation ».
- Gabarit d'index des preuves : n° | document | date | section | ce qu'il prouve | validité | responsable.

### K. Quiz

1. **(QCM)** Combien d'étapes comporte le cadre de devoir de diligence de l'OCDE ? a) 3 ; b) 5 ; c) 7 ; d) 10.
2. **(Vrai ou faux)** Une politique écrite suffit à prouver qu'une pratique est appliquée.
3. **(Compréhension)** Qu'est-ce que l'écoblanchiment, et comment Claude peut-il aider à le prévenir ?
4. **(QCM)** Quelle norme internationale porte sur la transparence des revenus, des contrats et de la propriété effective dans les industries extractives ? a) la GISTM ; b) la Norme ITIE ; c) le code JORC ; d) l'ISO/IEC 42001.
5. **(Mise en situation)** Claude propose « aucun risque de minerai artisanal ». Que faites-vous ?
6. **(Vrai ou faux)** L'audit tiers d'un rapport de diligence peut être remplacé par une relecture de Claude.
7. **(Compréhension)** À quoi sert une table de correspondance entre référentiels ?
8. **(Application)** Quelle part de la production minière mondiale de cobalt la RDC représentait-elle en 2025 selon l'USGS ?
9. **(Analyse critique)** Pourquoi les formulations absolues sont-elles dangereuses dans un rapport ESG ?
10. **(Application)** Rédigez la règle qui impose une preuve pour chaque réponse d'un questionnaire.

<div class="carnet" titre="Chapitre 32 — Claude appliqué à l'ESG, à la traçabilité minérale et à l'approvisionnement responsable"></div>
