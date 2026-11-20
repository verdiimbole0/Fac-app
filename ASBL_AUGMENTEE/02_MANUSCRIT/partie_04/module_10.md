# Partie IV — Implémenter l'IA dans chaque métier et processus {.partie}

*Le terrain est préparé : vous connaissez l'IA, votre organisation, vos priorités, vos règles et vos outils. Place aux métiers. Chaque module de cette partie part d'un processus réel et montre, étape par étape, ce que fait l'IA, ce que fait le logiciel, ce que fait le professionnel — et ce qui doit être contrôlé.*

# Module 10 — Gouvernance, direction générale et administration

## 10.1 Mise en situation

Lors du conseil d'administration de mars, le CA d'Horizons Partagés a décidé de réviser la politique de voyage, de lancer un audit du bureau régional et de renouveler le mandat de deux administrateurs avant l'assemblée générale. En septembre, personne ne se souvient précisément de ce qui a été décidé : le procès-verbal, rédigé à la main par la secrétaire bénévole, a été adopté avec deux mois de retard, et aucune décision n'avait de responsable ni d'échéance. Les mandats des deux administrateurs ont expiré sans renouvellement, ce qui fragilise la validité de certaines décisions ultérieures.

Ce scénario est courant. Il ne résulte pas d'un manque de bonne volonté, mais d'une absence de **système de suivi de la gouvernance**.

## 10.2 Problématique

La qualité de la gouvernance repose sur des documents fiables (ordres du jour, PV, registres), une information qui circule à temps, des décisions suivies et une continuité institutionnelle malgré le renouvellement des personnes. Ces tâches sont lourdes, souvent assurées par des bénévoles, et leur défaillance expose l'organisation à des risques juridiques et de réputation.

## 10.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. préparer un ordre du jour et un dossier de séance avec l'aide de l'IA ;
2. produire un projet de procès-verbal à partir de notes ou d'une transcription, et le contrôler ;
3. extraire les décisions, leur attribuer un responsable et une échéance, et en organiser le suivi ;
4. suivre les mandats et les obligations institutionnelles ;
5. organiser l'archivage et la circulation de l'information ;
6. concevoir un assistant de gouvernance adapté à la taille de l'organisation.

## 10.4 Notions et définitions

- **Ordre du jour** : liste des points soumis à une réunion, communiquée à l'avance selon les statuts.
- **Dossier de séance** : documents nécessaires aux délibérations (rapports, projets de décision, annexes).
- **Procès-verbal (PV)** : document officiel qui consigne le déroulement d'une réunion et les décisions adoptées ; il est approuvé selon les règles statutaires, généralement lors de la réunion suivante, et signé.
- **Quorum** : nombre minimal de membres présents ou représentés pour que l'organe délibère valablement.
- **Registre des décisions** : tableau de suivi listant chaque décision, son responsable, son échéance et son état d'avancement.
- **Mandat** : fonction confiée pour une durée déterminée (administrateur, président, trésorier).

> **⚖️ Adaptation réglementaire** — Les règles de convocation, de quorum, de majorité, de rédaction et de signature des PV, ainsi que la tenue de registres obligatoires, dépendent de la loi applicable et des statuts. L'enregistrement des réunions peut aussi être encadré. Vérifiez-les avant de modifier vos pratiques.

## 10.5 Explications détaillées

![Figure 10.1 — De la réunion au suivi des décisions](03_ILLUSTRATIONS/figures/fig_10_1.svg)

### Le cycle complet d'une réunion de gouvernance

| Étape | Ce qui se passe | Rôle de l'IA | Rôle du logiciel | Rôle humain |
|---|---|---|---|---|
| 1. Préparation de l'ordre du jour | Recensement des points, vérification des échéances statutaires | Proposer un projet d'ordre du jour à partir du registre des décisions et du calendrier | Calendrier, registre | Président et direction arrêtent l'ordre du jour |
| 2. Dossier de séance | Rassemblement des documents | Synthèses d'une page des rapports longs | Espace documentaire partagé | Vérification des synthèses par les auteurs des rapports |
| 3. Convocation | Envoi dans les délais statutaires | — | Messagerie, rappel automatique | Secrétaire |
| 4. Réunion | Débats et votes | Transcription (si consentement de tous) | Visioconférence, enregistreur | Président anime ; secrétaire prend des notes |
| 5. Projet de PV | Rédaction | Projet structuré à partir des notes ou de la transcription ; extraction des décisions | Traitement de texte | Secrétaire vérifie et corrige |
| 6. Relecture | Contrôle | — | Suivi des modifications | Président et membres concernés |
| 7. Adoption et signature | Approbation formelle | — | Signature (manuscrite ou électronique selon le droit applicable) | Organe compétent |
| 8. Registre des décisions | Mise à jour | Pré-remplissage des lignes à partir du PV adopté | Tableur ou base | Secrétaire valide |
| 9. Suivi | Rappels, avancement | Synthèse de l'état d'avancement | Rappels automatiques | Responsables de chaque décision |
| 10. Archivage | Conservation | Indexation (mots clés, résumé) | Gestion documentaire | Secrétaire |

### Le procès-verbal : ce que l'IA peut faire… et ne doit pas faire

Un projet de PV généré par l'IA peut faire gagner plusieurs heures. Mais un PV est un **document juridique**. Il doit refléter fidèlement les décisions adoptées, les votes, les présents et représentés, le quorum, les éventuels conflits d'intérêts déclarés. Un assistant peut :

- structurer les notes selon le modèle de PV de l'organisation ;
- repérer les décisions, les votes et les actions ;
- signaler les informations manquantes (heure de clôture, résultat d'un vote) ;
- proposer une formulation neutre et concise.

Il ne doit pas :

- **inventer** un résultat de vote, une présence, une décision ;
- **interpréter** une discussion non conclusive comme une décision ;
- **reformuler** une décision au point d'en changer la portée.

> **🔎 À retenir** — Le PV adopté et signé fait foi ; le projet généré par l'IA n'est qu'un brouillon. Le secrétaire en est l'auteur et le garant.

### Transcription des réunions : précautions

L'enregistrement et la transcription automatique d'une réunion supposent : l'information préalable et le consentement des participants ; un outil autorisé pour des données orange (un CA évoque souvent des sujets confidentiels — personnel, litiges, finances) ; une durée de conservation courte de l'enregistrement (suppression après adoption du PV, sauf règle contraire) ; la possibilité de suspendre l'enregistrement pour les points confidentiels (huis clos, conflits d'intérêts, questions de personnel).

### Suivi des décisions et des mandats

Le **registre des décisions** (annexe 20 pour les recommandations, sur le même modèle) est l'outil central. Chaque ligne comporte : numéro, date de la réunion, organe, intitulé de la décision, responsable, échéance, état (à faire / en cours / réalisé / reporté / abandonné), commentaire, référence du document de preuve. Il est présenté à chaque réunion.

Le **registre des mandats** comporte : nom, fonction, date de début, durée, date d'échéance, organe qui renouvelle, et une alerte automatique trois mois avant l'échéance. C'est typiquement une automatisation classique (une formule de date et un rappel), pas de l'IA.

### Obligations institutionnelles

Les obligations institutionnelles (dépôt des comptes, déclarations aux autorités, renouvellement d'agréments, rapports annuels aux bailleurs, assemblées statutaires) sont rassemblées dans un **calendrier des obligations**. L'IA peut aider à extraire ces obligations des statuts, des conventions et des textes applicables, mais chaque obligation doit être vérifiée sur la source officielle par une personne compétente.

### Archivage et circulation de l'information

- Archivage : un dossier « 01_GOUVERNANCE » structuré par organe et par année ; PV signés en PDF ; règle de nommage (module 7).
- Circulation : après chaque réunion, une **note de synthèse** d'une page aux équipes (décisions qui les concernent), distincte du PV ; l'IA peut en préparer le projet à partir du PV adopté.

### L'assistant de gouvernance

Pour les organisations de niveau intermédiaire ou avancé, un **assistant de gouvernance** peut répondre à des questions comme : « Quelles décisions le CA a-t-il prises sur la politique de voyage depuis 2024 ? » ou « Quand expire le mandat de la trésorière ? ». Il s'appuie sur une base documentaire (statuts, règlement intérieur, PV adoptés, registres) via un dispositif RAG, avec citation des sources. Conditions : base documentaire propre (uniquement les versions adoptées) ; droits d'accès réservés aux administrateurs et à la direction ; réponses toujours sourcées et vérifiables.

### Continuité institutionnelle

Lors du renouvellement d'un président, d'un trésorier ou d'un directeur, un **dossier de passation** réduit la perte de mémoire : statuts, délégations, registres, calendrier des obligations, dossiers en cours, contacts clés, accès (transmis selon une procédure sécurisée). L'IA peut aider à produire une synthèse des dossiers en cours à partir des PV et du registre.

## 10.6 Application métier : de la réunion au suivi des décisions à Horizons Partagés

**A. Contexte.** CA de neuf membres bénévoles, quatre réunions par an ; secrétaire bénévole ; direction salariée.
**B. Problème.** Décisions non suivies ; PV adoptés tardivement ; mandats expirés.
**C. Symptômes.** PV adoptés avec deux mois de retard ; décisions sans responsable ; découverte tardive de mandats expirés.
**D. Causes profondes.** Pas de modèle de PV ; pas de registre des décisions ; pas de calendrier des mandats ; charge excessive pour une secrétaire bénévole.
**E. Processus actuel.** Notes manuscrites → rédaction en plusieurs semaines → adoption à la réunion suivante → classement.
**F. Points de faiblesse.** Aucune trace structurée des actions ; dépendance à une personne ; risque juridique sur la validité des décisions.
**G. Résultat recherché.** Projet de PV diffusé sous 5 jours ouvrables ; 100 % des décisions inscrites au registre avec responsable et échéance ; aucun mandat expiré non renouvelé.
**H. Pertinence de l'IA.** Forte pour la rédaction du projet de PV et l'extraction des décisions (texte, variabilité) ; inutile pour les alertes de mandats (règle simple).
**I. Alternatives sans IA.** Modèle de PV à compléter en séance ; registre tenu manuellement ; rappels de calendrier.
**J. Solution recommandée.** Modèle de PV + prise de notes structurée en séance + projet de PV assisté par l'IA + registre des décisions + rappels automatiques.
**K. Niveau.** Débutant à Intermédiaire.
**L. Outils.** Traitement de texte, tableur partagé, calendrier avec rappels ; assistant d'IA autorisé pour des données orange ; éventuellement outil de transcription validé.
**M. Étapes détaillées.**

1. Adopter un **modèle de PV** (en-tête, présents, représentés, excusés, quorum, ordre du jour, points traités avec « exposé — débat — décision — vote », actions, clôture).
2. Préparer l'**ordre du jour** avec la fiche P10.3, à partir du registre et du calendrier.
3. Pendant la séance, la secrétaire prend des **notes structurées** selon le modèle, en notant mot pour mot le texte des décisions et les résultats des votes.
4. Dans les 48 heures, elle soumet les notes à l'assistant avec la fiche P10.1 (outil autorisé pour données orange ; noms des personnes extérieures remplacés si nécessaire).
5. Elle **vérifie** le projet ligne par ligne contre ses notes, en particulier les décisions et les votes.
6. Le président relit ; le projet est diffusé aux membres sous 5 jours ouvrables.
7. Les décisions extraites (fiche P10.2) sont inscrites au **registre** après validation.
8. Des **rappels automatiques** sont programmés pour chaque échéance.
9. Le PV est **adopté** à la réunion suivante, signé et archivé.
10. Le registre des décisions est **présenté** en ouverture de chaque réunion.

**N. Prompts.** Fiches P10.1, P10.2, P10.3.
**O. Exemple de résultat.** Voir les fiches ci-dessous.
**P. Méthode de vérification.** Contrôle croisé notes ↔ projet de PV pour chaque décision et chaque vote ; vérification du quorum ; relecture par le président.
**Q. Contrôles humains.** Rédaction finale par la secrétaire ; relecture par le président ; adoption par l'organe ; validation des lignes du registre.
**R. Risques et précautions.** Décision mal retranscrite ; confidentialité des débats ; dépendance à l'outil. Précaution : le texte des décisions est toujours repris des notes, jamais de la reformulation de l'IA.
**S. Coûts et maintenance.** Niveau Débutant : temps de mise en place (une demi-journée) ; abonnement éventuel à une suite professionnelle. Maintenance : mise à jour du registre après chaque réunion.
**T. Indicateurs.** Délai de diffusion du projet de PV ; pourcentage de décisions avec responsable et échéance ; taux de décisions réalisées dans les délais ; nombre de mandats expirés non renouvelés (cible : 0).
**U. Amélioration continue.** Revue annuelle du modèle de PV et du registre ; questionnaire de satisfaction des administrateurs.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Modèle de PV, notes structurées, projet de PV assisté (données anonymisées ou outil validé), registre en tableur, rappels de calendrier | Traitement de texte, tableur, calendrier, assistant | Faibles | Saisie manuelle du registre |
| Intermédiaire | Transcription validée avec consentement, suite collaborative avec assistant intégré, registre partagé avec rappels automatiques, espace documentaire du CA avec droits restreints | Suite professionnelle, outil de transcription, plateforme d'automatisation | Abonnements | Paramétrage de la confidentialité |
| Avancé | Portail de gouvernance (convocations, votes, signatures électroniques selon le droit applicable), assistant de gouvernance RAG sur les documents adoptés, tableau de bord des décisions et des obligations | Logiciel de gestion de conseil, RAG | Licences, intégration | Coût ; vérification de la valeur juridique des signatures et votes électroniques |

## 10.7 Prompts prêts à l'emploi

### Fiche P10.1 — Projet de procès-verbal à partir de notes

**A. Titre.** Projet de PV structuré et vérifiable.

**B. Objectif.** Transformer des notes de séance en projet de PV conforme au modèle de l'organisation, sans rien inventer.

**C. Contexte d'utilisation.** Secrétariat d'un CA, d'une AG, d'un comité ; dans les 48 heures suivant la réunion.

**D. Données nécessaires.** Modèle de PV ; liste des présents, représentés et excusés ; ordre du jour ; notes structurées ou transcription ; texte exact des décisions et résultats des votes.

**E. Prompt complet.**

```text
Contexte : je suis secrétaire de [ORGANE] de [NOM DE L'ASBL]. Je
prépare le projet de procès-verbal de la réunion du [DATE].
Tâche : rédige le projet de PV en suivant exactement le modèle fourni.
Données :
<modele>[MODÈLE DE PV]</modele>
<presences>[PRÉSENTS / REPRÉSENTÉS (avec mandataire) / EXCUSÉS]
</presences>
<ordre_du_jour>[ORDRE DU JOUR]</ordre_du_jour>
<notes>[NOTES STRUCTURÉES OU TRANSCRIPTION]</notes>
Règles impératives :
1. Pour chaque point : « Exposé » (2 à 4 phrases), « Débat »
   (principaux arguments, sans attribuer de propos à une personne sauf
   si les notes l'indiquent explicitement), « Décision » (reprendre
   MOT POUR MOT le texte de la décision figurant dans les notes),
   « Vote » (pour/contre/abstention tels que notés).
2. Si une décision, un vote, une heure ou un quorum ne figure pas dans
   les notes, écris [À COMPLÉTER] — n'invente rien.
3. Si une discussion n'a pas abouti à une décision, écris « Aucune
   décision n'a été prise sur ce point ».
4. Termine par un tableau « N° | Décision | Responsable | Échéance »
   en reprenant uniquement ce qui figure dans les notes ; [À
   COMPLÉTER] sinon.
5. Liste à part les incohérences repérées dans les notes.
Style : neutre, concis, au passé composé.
```

**F. Instructions d'utilisation.** Vérifiez que l'outil est autorisé pour des données orange ; si des points confidentiels ont été traités à huis clos, ne les soumettez pas et rédigez-les manuellement. Comparez le projet aux notes avant toute diffusion.

**G. Résultat attendu.** Un projet de PV complet au format de l'organisation, avec des marqueurs [À COMPLÉTER] là où l'information manque, un tableau des actions et une liste d'incohérences.

**H. Exemple d'application (illustratif).** Extrait de projet obtenu pour le point « Politique de voyage » :

> **Point 3 — Révision de la politique de voyage.**
> *Exposé.* La directrice a présenté les écarts constatés entre les frais de mission et les plafonds en vigueur, ainsi qu'un projet de politique révisée.
> *Débat.* Les administrateurs ont discuté du plafond d'hébergement dans les capitales et de la procédure d'autorisation préalable.
> *Décision.* « Le conseil adopte la politique de voyage révisée, sous réserve de l'ajout d'un plafond spécifique pour les capitales, à proposer par la direction avant le 30 avril. »
> *Vote.* Pour : 7 ; contre : 0 ; abstention : 1.
>
> Incohérence signalée : « Les notes indiquent 8 votants alors que la liste de présence mentionne 7 présents et 2 représentés (9 voix possibles). [À VÉRIFIER] »

**I. Méthode de vérification.** (1) Comparez le texte de chaque décision aux notes, caractère par caractère. (2) Vérifiez les votes et le quorum. (3) Traitez tous les [À COMPLÉTER] et incohérences. (4) Faites relire par le président.

**J. Précautions.** Ne pas soumettre les points à huis clos, les questions individuelles de personnel ni les informations sur des bénéficiaires identifiables. Supprimer l'enregistrement et la transcription après adoption, selon la règle fixée.

**K. Amélioration.** *V1* : « Fais un PV avec ces notes. » → l'outil invente une heure de clôture, reformule les décisions et attribue des propos. *V2* : la fiche ci-dessus. *Si le PV est trop long* : « Limite l'exposé et le débat de chaque point à 60 mots, sans toucher au texte des décisions. »

### Fiche P10.2 — Alimenter le registre des décisions

**A. Titre.** Extraction des décisions et actions d'un PV adopté.

**B. Objectif.** Produire les lignes du registre des décisions à partir d'un PV adopté.

**C. Contexte d'utilisation.** Après l'adoption d'un PV.

**D. Données nécessaires.** PV adopté ; colonnes du registre ; liste des fonctions (responsables possibles).

**E. Prompt complet.**

```text
Tâche : à partir du procès-verbal adopté ci-dessous, produis les lignes
à ajouter au registre des décisions.
Colonnes : N° | Date de réunion | Organe | Décision (texte exact) |
Type (adoption, mandat, action, information) | Responsable (fonction)
| Échéance (AAAA-MM-JJ) | État initial (« à faire ») | Référence
(point n° du PV).
Données : <pv>[PV ADOPTÉ]</pv>
Règles : reprends le texte exact des décisions ; si le responsable
ou l'échéance ne sont pas indiqués, écris « NON DÉFINI » (ne les
déduis pas). Produis le tableau au format CSV avec « ; » comme
séparateur.
```

**F. Instructions d'utilisation.** Collez le résultat dans le tableur du registre ; complétez les « NON DÉFINI » avec la direction ; programmez les rappels.

**G. Résultat attendu.** Lignes au format CSV, une par décision.

**H. Exemple d'application (illustratif).**

```text
2026-07;2026-03-18;CA;"Le conseil adopte la politique de voyage
révisée, sous réserve de l'ajout d'un plafond spécifique pour les
capitales, à proposer par la direction avant le 30 avril.";action;
Direction exécutive;2026-04-30;à faire;Point 3
```

**I. Méthode de vérification.** Nombre de lignes = nombre de décisions du PV ; textes identiques ; aucune échéance inventée.

**J. Précautions.** Le registre est un document orange ; droits d'accès limités au CA et à la direction.

**K. Amélioration.** « Ajoute une colonne "dépendances" indiquant si une décision dépend d'une autre décision du registre. »

### Fiche P10.3 — Préparer l'ordre du jour

**A. Titre.** Projet d'ordre du jour fondé sur le registre et le calendrier.

**B. Objectif.** Ne rien oublier : décisions à échéance, obligations statutaires, mandats, rapports attendus.

**C. Contexte d'utilisation.** Trois à quatre semaines avant une réunion.

**D. Données nécessaires.** Registre des décisions (extraits en cours) ; calendrier des obligations ; registre des mandats ; demandes reçues.

**E. Prompt complet.**

```text
Contexte : réunion de [ORGANE] de [NOM DE L'ASBL] prévue le [DATE],
durée [DURÉE].
Données :
<registre>[DÉCISIONS EN COURS OU À ÉCHÉANCE]</registre>
<obligations>[OBLIGATIONS DES 6 PROCHAINS MOIS]</obligations>
<mandats>[MANDATS EXPIRANT DANS LES 6 MOIS]</mandats>
<demandes>[POINTS DEMANDÉS PAR LES MEMBRES OU LA DIRECTION]</demandes>
Tâche : propose un ordre du jour.
Résultat attendu : tableau « N° | Point | Nature (pour décision /
pour information / pour débat) | Rapporteur (fonction) | Durée |
Documents à joindre | Source (registre, obligation, mandat,
demande) ». Puis liste des points écartés ou reportés avec la raison.
Règles : la durée totale ne doit pas dépasser [DURÉE] ; commence par
l'approbation du PV précédent et le suivi du registre ; place les
points pour décision avant les points pour information.
```

**F. Instructions d'utilisation.** Le président et la direction arrêtent l'ordre du jour définitif.

**G. Résultat attendu.** Un ordre du jour minuté, sourcé, avec la liste des documents à préparer.

**H. Exemple d'application (illustratif).** Le projet obtenu inscrit automatiquement « Renouvellement des mandats de deux administrateurs (échéance : 2026-06-30) — pour décision » — le point qui avait été oublié l'année précédente.

**I. Méthode de vérification.** Confrontez chaque point aux sources ; vérifiez les délais de convocation statutaires.

**J. Précautions.** Données orange.

**K. Amélioration.** « Pour chaque point pour décision, propose une formulation de projet de décision à soumettre au vote. »

## 10.8 Résultats attendus

PV diffusés rapidement et fidèles ; registre des décisions à jour ; mandats et obligations suivis ; information diffusée aux équipes ; mémoire de la gouvernance préservée.

## 10.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** — Le texte des décisions, les votes, le quorum et les présences sont vérifiés par le secrétaire sur ses notes. Le PV n'a de valeur qu'une fois adopté et signé par l'organe compétent. Aucune décision ne figure au registre sans validation humaine.

## 10.10 Risques et erreurs à éviter

- Diffuser un projet de PV généré sans relecture.
- Enregistrer une réunion sans le consentement de tous.
- Soumettre à un outil non validé les débats sur des personnes ou des litiges.
- Confondre note de synthèse aux équipes et PV officiel.
- Alimenter un assistant de gouvernance avec des projets non adoptés.

## 10.11 Exercice pratique

**Consigne (90 minutes).** À partir de notes fictives d'une réunion de 45 minutes (rédigez-les vous-même, avec trois décisions dont une sans échéance, et un vote incohérent) : (1) appliquez la fiche P10.1 ; (2) repérez si l'outil a correctement signalé l'échéance manquante et l'incohérence du vote ; (3) produisez les lignes du registre avec la fiche P10.2 ; (4) programmez les rappels dans votre calendrier.

**Éléments de correction.** Le projet de PV ne doit contenir aucune information absente des notes ; l'échéance manquante doit apparaître en [À COMPLÉTER] ou « NON DÉFINI » ; l'incohérence de vote doit être signalée. Si l'outil a comblé un manque, l'exercice démontre la nécessité de la vérification.

## 10.12 Synthèse

- Le cycle de gouvernance va de l'ordre du jour au suivi des décisions.
- L'IA prépare des projets (ordre du jour, PV, synthèses, lignes de registre) ; le secrétaire et l'organe en sont garants.
- Le texte des décisions et les votes ne sont jamais reformulés par l'IA.
- Les mandats et obligations relèvent d'automatisations simples (dates, rappels).
- Un assistant de gouvernance n'est fiable que sur une base documentaire de documents adoptés.

## 10.13 QCM — Module 10

**Q1.** (une seule réponse) Un projet de PV généré par l'IA :

a) fait foi dès sa génération.
b) est un brouillon dont le secrétaire est l'auteur et le garant.
c) peut être signé sans relecture s'il est bien rédigé.
d) remplace l'adoption par l'organe.

**Q2.** (une ou plusieurs réponses) Dans un projet de PV, l'IA ne doit pas :

a) inventer un résultat de vote.
b) reformuler une décision au point d'en changer la portée.
c) signaler une information manquante.
d) interpréter une discussion non conclusive comme une décision.

**Q3.** (une seule réponse) Le suivi de l'échéance des mandats relève principalement :

a) de l'IA générative.
b) d'une automatisation simple (dates et rappels).
c) d'un agent autonome.
d) d'une analyse prédictive.

**Q4.** (une ou plusieurs réponses) Une ligne du registre des décisions comporte :

a) le texte de la décision.
b) le responsable.
c) l'échéance.
d) l'avis personnel du secrétaire sur chaque administrateur.

**Q5.** (une seule réponse) Pour enregistrer et transcrire un CA, il faut d'abord :

a) acheter un micro.
b) informer les participants et recueillir leur consentement, avec un outil autorisé.
c) prévenir le bailleur.
d) rien, si la réunion est interne.

**Q6.** (une seule réponse) Un assistant de gouvernance RAG doit être alimenté par :

a) tous les brouillons disponibles.
b) les seuls documents adoptés et à jour.
c) les courriels personnels des administrateurs.
d) des documents trouvés sur internet.

**Q7.** (mise en situation — une seule réponse) Le projet de PV indique « 8 voix pour », alors que vos notes indiquent « 7 voix pour, 1 abstention ». Que faites-vous ?

a) Vous gardez la version de l'IA.
b) Vous corrigez selon vos notes et vérifiez le décompte des voix.
c) Vous supprimez le vote du PV.
d) Vous faites la moyenne.

**Q8.** (mise en situation — une seule réponse) Un point à huis clos a porté sur un litige avec un salarié. Comment le traiter ?

a) Soumettre les notes à l'assistant comme le reste.
b) Le rédiger manuellement, sans le soumettre à l'outil.
c) Ne pas le mentionner dans le PV, même s'il y a eu décision.
d) Le publier dans la note aux équipes.

**Q9.** (une seule réponse) La note de synthèse aux équipes après un CA :

a) remplace le PV.
b) est distincte du PV et ne reprend que ce qui concerne les équipes.
c) doit contenir les débats nominatifs.
d) est inutile.

**Q10.** (une ou plusieurs réponses) Indicateurs pertinents pour ce processus :

a) délai de diffusion du projet de PV.
b) pourcentage de décisions avec responsable et échéance.
c) nombre de mandats expirés non renouvelés.
d) nombre de pages des PV.

## 10.14 Corrigé détaillé — Module 10

**Q1 : b.** Seul le PV adopté et signé fait foi.

**Q2 : a, b, d.** Signaler une information manquante (c) est précisément ce qu'on attend de l'outil.

**Q3 : b.** Une formule de date et un rappel suffisent.

**Q4 : a, b, c.** Les avis personnels (d) n'ont pas leur place dans un registre.

**Q5 : b.** Consentement et outil autorisé sont des préalables.

**Q6 : b.** Sinon, l'assistant risque de citer des décisions non adoptées.

**Q7 : b.** Les notes de séance font référence ; le décompte doit être vérifié.

**Q8 : b.** Les informations confidentielles sur des personnes ne sont pas soumises à l'outil. La décision, si elle existe, doit figurer au PV selon les règles applicables (c est faux).

**Q9 : b.** La note aux équipes est un outil de communication, pas un document officiel.

**Q10 : a, b, c.** Le nombre de pages (d) ne mesure pas la qualité.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.
