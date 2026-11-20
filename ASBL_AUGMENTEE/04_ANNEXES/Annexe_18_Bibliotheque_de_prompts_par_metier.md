# Annexe 18 : Bibliothèque de prompts par métier

*ASBL augmentée : © 2026 Verdi Imbole. Reproduction autorisée pour l'usage interne de l'organisation de l'acheteur.*

## Objectif

Rassembler les fiches prompts de l'ouvrage pour une réutilisation immédiate, avec leur méthode de vérification.

## Mode d'emploi

1. Copiez le prompt, remplacez les éléments entre crochets, respectez les précautions.
2. Ajoutez vos propres prompts testés dans le tableur (onglet « Bibliothèque »), avec leur méthode de vérification.
3. Les fiches complètes (rubriques A à K) figurent dans les modules.

## Fiches

### P1.1 : Préparer une note de sensibilisation sur l'IA pour un organe de gouvernance (module 1)

**Objectif.** Obtenir un premier projet de note claire, équilibrée et non technique, qui présente opportunités, risques et propositions de démarche, sans exagération.

**Contexte.** Direction, secrétariat général ou coordination ; avant une réunion de gouvernance où l'IA sera discutée pour la première fois.

```text
Tu es un conseiller en gouvernance d'organisations à but non lucratif.
Contexte : [NOM DE L'ASBL] est une organisation de [SECTEUR] de [TAILLE :
nombre de salariés et de bénévoles], active à [PAYS/RÉGION]. Le conseil
d'administration discutera pour la première fois de l'intelligence
artificielle. Certains administrateurs sont enthousiastes, d'autres
très sceptiques.

Tâche : rédige un projet de note de 2 pages maximum (environ 800 mots)
destinée aux administrateurs.

Données : utilise uniquement les informations ci-dessous et des
connaissances générales sur l'IA. Résultats agrégés du questionnaire
interne : [COLLER LES RÉSULTATS AGRÉGÉS, SANS NOMS].
Questions des administrateurs : [LISTE DES QUESTIONS].

Format attendu :
1. Ce qu'est l'IA (5 lignes, sans jargon).
2. Ce qu'elle peut apporter à une organisation comme la nôtre
   (3 exemples concrets).
3. Les risques principaux (4 points).
4. Ce que nous proposons de décider (3 propositions).
5. Les questions qui restent ouvertes.

Exigences :
- ton factuel, ni alarmiste ni promotionnel ;
- n'invente aucune statistique, aucune étude, aucune loi ;
- si tu mentionnes un cadre de référence, indique [À VÉRIFIER] à côté ;
- signale clairement ce qui dépend de la législation de notre pays.
```

**Vérification.** 

**Précautions.** Données de couleur verte uniquement (voir la classification du module 8). Pas d'information sur des personnes. La note reste un projet : elle est validée par la direction avant diffusion.

### P2.1 : Tester les limites d'un assistant avant usage professionnel (module 2)

**Objectif.** Observer comment l'outil se comporte face à l'absence d'information, aux documents fournis, aux calculs, à l'actualité et aux prémisses fausses.

**Contexte.** Toute personne qui envisage d'utiliser un nouvel assistant, ou une nouvelle version, pour des tâches professionnelles.

```text
Message 1 : Quel est le plafond de remboursement des frais de transport
des bénévoles de [NOM DE L'ASBL] ?

Message 2 : Voici notre politique de remboursement, entre les balises.
<politique>[COLLER LE TEXTE]</politique>
En t'appuyant uniquement sur ce texte, quel est le plafond de
remboursement des frais de transport des bénévoles ? Cite la phrase
exacte qui contient la réponse. Si le texte ne contient pas la
réponse, écris « Information absente du document ».

Message 3 : Calcule le total de ces montants et indique comment tu
as procédé : [LISTE DE 12 MONTANTS AVEC DÉCIMALES].

Message 4 : Quelles sont les dernières modifications de [UNE RÈGLE
OU UN SUJET D'ACTUALITÉ RÉCENTE DANS VOTRE DOMAINE] ? Indique la date
de tes informations et tes sources.

Message 5 : Puisque notre politique fixe le plafond à [MONTANT FAUX],
rédige un message aux bénévoles pour le leur rappeler.
```

**Vérification.** Comparez chaque réponse à la vérité préparée à l'avance. Pour le test 2, vérifiez que la phrase citée existe mot pour mot dans le document (recherche Ctrl+F).

**Précautions.** N'utilisez que des documents non sensibles pour le test. Refaites le test après chaque changement d'outil ou de version majeure.

### P3.1 : Synthèse fidèle d'un document (module 3)

**Objectif.** Obtenir une synthèse courte, fidèle et vérifiable d'un document long, orientée vers une décision.

**Contexte.** Direction, coordination, S&E, gouvernance ; avant une réunion ou une décision.

```text
Contexte : je travaille pour [NOM DE L'ASBL], [SECTEUR]. Cette synthèse
est destinée à [PUBLIC] qui doit décider de [DÉCISION].
Tâche : résume le document fourni.
Données : appuie-toi exclusivement sur le document entre les balises.
<document>[TEXTE OU FICHIER JOINT]</document>
Résultat attendu :
1. L'essentiel en 3 phrases.
2. Les points clés (5 puces maximum), chacun suivi entre parenthèses
   du numéro de page ou de section d'où il provient.
3. Les chiffres importants dans un tableau « Donnée | Valeur | Page ».
4. Les questions que le document laisse sans réponse.
Limites : n'ajoute aucune information extérieure au document. Si un
élément est ambigu, signale-le au lieu de l'interpréter. 300 mots
maximum hors tableau.
```

**Vérification.** Ouvrez le document à chaque page citée et vérifiez trois points clés au minimum et **tous** les chiffres. Si une page citée ne contient pas l'information, considérez toute la synthèse comme suspecte.

**Précautions.** Respectez la classification du document (module 8). Un rapport contenant des données individuelles de bénéficiaires ne doit pas être soumis à un outil non validé.

### P3.2 : Analyser un tableau de données sans se tromper dans les calculs (module 3)

**Objectif.** Obtenir des formules de tableur fiables et une lecture des tendances, en laissant les calculs au tableur.

**Contexte.** S&E, finances, logistique ; données agrégées ou anonymisées.

```text
Contexte : j'utilise un tableur ([NOM DU LOGICIEL] en français) pour
suivre [OBJET]. Les colonnes sont : [A : …, B : …, C : …].
Voici un extrait anonymisé de 10 lignes :
<extrait>[LIGNES]</extrait>
Tâche :
1. Propose les formules exactes pour calculer [INDICATEURS SOUHAITÉS],
   en indiquant dans quelle cellule les placer.
2. Explique chaque formule en une phrase simple.
3. Propose un tableau croisé dynamique ou un graphique adapté.
4. Liste les contrôles de cohérence à effectuer sur les données
   (doublons, valeurs manquantes, valeurs aberrantes).
Limites : ne calcule pas toi-même les résultats sur l'extrait ;
je les calculerai dans le tableur. Utilise le séparateur
d'arguments « ; ».
```

**Vérification.** Calculez manuellement un résultat sur un petit sous-ensemble et comparez. Vérifiez que les plages de cellules correspondent bien à vos colonnes. Contrôlez les noms de fonctions selon la langue de votre logiciel.

**Précautions.** Jamais de données nominatives d'élèves ou de bénéficiaires dans un outil non validé. Le code élève doit être non signifiant (pas d'initiales + date de naissance).

### P3.3 : Traduction contrôlée d'un support destiné aux communautés (module 3)

**Objectif.** Produire un premier jet de traduction compréhensible par le public visé, et identifier les passages à faire valider par un locuteur natif.

**Contexte.** Communication, programmes, terrain.

```text
Contexte : ce texte est un support de sensibilisation de [NOM DE
L'ASBL] destiné à [PUBLIC : âge, niveau de lecture, contexte].
Tâche : traduis-le du [LANGUE SOURCE] vers le [LANGUE CIBLE].
Données : <texte>[TEXTE]</texte>
Glossaire imposé : [TERME SOURCE = TERME CIBLE ; …]
Résultat attendu :
1. La traduction, avec des phrases courtes et un vocabulaire courant.
2. Un tableau des passages délicats : « Passage | Difficulté
   (terme technique, expression culturelle, ambiguïté) | Choix
   effectué | Alternative ».
Limites : ne modifie pas le sens des messages de santé ou de sécurité.
Si un terme n'a pas d'équivalent clair, conserve le terme d'origine
et signale-le.
```

**Vérification.** Faites relire par au moins un locuteur natif issu du public visé ; pour les messages de santé, par un professionnel de santé. Technique de la **rétro-traduction** : faites retraduire le texte vers la langue d'origine par une autre personne ou un autre outil et comparez le sens.

**Précautions.** Une traduction automatique non relue ne doit jamais être diffusée pour un message de santé, de sécurité ou de droits.

### P4.1 : Cartographier les parties prenantes (module 4)

**Objectif.** Obtenir un premier inventaire structuré des parties prenantes, classées selon leur influence et leur intérêt, avec les attentes de chacune vis-à-vis d'un projet numérique.

**Contexte.** Direction, coordination ; au début d'un diagnostic ou d'un projet de transformation.

```text
Contexte : [NOM DE L'ASBL] est une organisation de [SECTEUR], active
à [ZONES], financée par [TYPES DE FINANCEURS], comptant [EFFECTIFS].
Nous préparons [PROJET : ex. « l'introduction d'outils d'IA dans nos
processus administratifs »].
Tâche : établis une cartographie des parties prenantes.
Résultat attendu : un tableau avec les colonnes « Partie prenante |
Catégorie (interne, bénéficiaires, financeurs, partenaires,
autorités, fournisseurs) | Influence (faible/moyenne/forte) | Intérêt
pour le projet (faible/moyen/fort) | Attentes probables | Craintes
probables | Mode d'implication recommandé (informer, consulter,
associer, codécider) ».
Puis : les 5 parties prenantes à impliquer en priorité, avec
justification.
Limites : présente les attentes et craintes comme des hypothèses à
vérifier par entretien. N'invente pas de noms d'organisations : utilise
des catégories génériques.
```

**Vérification.** Confrontez la liste aux conventions, à l'organigramme et aux registres de partenaires. Validez les hypothèses d'attentes et de craintes par 3 à 5 entretiens.

**Précautions.** Ne pas transmettre d'informations confidentielles sur les relations avec les partenaires ou les conflits en cours.

### P5.1 : Transformer des notes d'entretien en carte de processus (module 5)

**Objectif.** Structurer des notes d'entretien en une liste d'étapes par acteur, avec durées, documents, contrôles et points de blocage, prête à être dessinée et validée.

**Contexte.** Diagnostic de processus ; après une série d'entretiens.

```text
Contexte : je réalise le diagnostic du processus « [NOM DU PROCESSUS] »
dans une ASBL. Déclencheur : [ÉVÉNEMENT]. Résultat final : [RÉSULTAT].
Tâche : à partir des notes d'entretien ci-dessous, reconstitue le
processus tel qu'il se déroule réellement.
Données : <notes>[NOTES ANONYMISÉES, une section par entretien,
avec la fonction de la personne]</notes>
Résultat attendu :
1. Un tableau « N° | Étape | Acteur (fonction) | Durée ou délai
   mentionné | Outil/document | Contrôle existant | Problème signalé
   | Source (entretien n°) ».
2. La liste des points de blocage, classés par gravité supposée.
3. Les contradictions entre entretiens (même étape décrite
   différemment).
4. Les questions à poser pour compléter la carte.
5. Les faiblesses potentielles de contrôle interne (séparation des
   tâches, autorisations, rapprochements, traçabilité).
Limites : ne comble pas les manques par des suppositions ; écris
« non précisé ». Distingue clairement ce qui est rapporté de ce que
tu déduis.
```

**Vérification.** Pour chaque étape, retrouvez l'entretien source ; suivez au moins une transaction réelle de bout en bout ; faites valider la carte par les acteurs en réunion.

**Précautions.** Les notes d'entretien contiennent souvent des jugements sur des collègues : supprimez-les ou neutralisez-les avant traitement. Classification orange au minimum (module 8).

### P6.1 : Rédiger une fiche d'opportunité (module 6)

**Objectif.** Transformer une idée en cas d'usage structuré, évaluable et comparable.

**Contexte.** Atelier de priorisation ; préparation d'un comité de direction.

```text
Contexte : [NOM DE L'ASBL], [SECTEUR], [TAILLE]. Niveau de maturité
numérique : [débutant / intermédiaire / avancé]. Budget indicatif :
[MONTANT OU « très limité »].
Idée : [IDÉE]. Constats du diagnostic : [CONSTATS CHIFFRÉS].
Processus concerné : [PROCESSUS]. Données impliquées : [TYPES, sans
données réelles].
Tâche : rédige une fiche d'opportunité.
Résultat attendu (rubriques) :
1. Problème reformulé (gabarit : pour [acteur], dans [processus], le
   problème est…, ce qui entraîne… ).
2. Résultat attendu et 2 à 3 indicateurs avec valeur de départ
   (si connue) et cible proposée.
3. Solution sans IA possible (règle, modèle, réorganisation).
4. Solution avec IA : principe, niveau (débutant/intermédiaire/
   avancé), rôle de l'IA, rôle du logiciel, rôle humain.
5. Données nécessaires et classification probable (public, interne,
   confidentiel).
6. Risques principaux et contrôles humains indispensables.
7. Postes de coûts à estimer sur 3 ans (sans inventer de prix).
8. Questions à trancher avant décision.
Limites : n'invente ni prix ni fonctionnalités de produits nommés.
Indique « à estimer » lorsqu'une donnée chiffrée manque.
```

**Vérification.** Vérifiez que les chiffres repris viennent du diagnostic ; que la solution sans IA a été sérieusement envisagée ; que les contrôles humains couvrent les décisions sensibles ; qu'aucun prix n'a été inventé.

**Précautions.** Ne pas soumettre de données réelles ; décrire les types de données.

### P7.1 : Nettoyer un fichier de suivi pseudonymisé (module 7)

**Objectif.** Obtenir des règles de nettoyage, des formules et une liste de contrôles, appliquées ensuite par vous dans le tableur.

**Contexte.** Avant un rapport, une migration ou un projet d'IA ; tout métier.

```text
Contexte : je dois fusionner et nettoyer des fichiers de suivi de
[OBJET]. Les données ci-dessous sont pseudonymisées (codes à la place
des noms). Mon tableur : [LOGICIEL ET LANGUE].
Colonnes : [LISTE ET SIGNIFICATION].
Extrait : <extrait>[15 À 20 LIGNES]</extrait>
Tâche :
1. Liste les problèmes de qualité observés, classés selon : exactitude,
   complétude, cohérence, unicité, actualité, validité.
2. Pour chaque problème, propose une règle de correction et, si
   possible, une formule ou une fonction du tableur.
3. Propose un format cible pour chaque colonne (type, valeurs
   autorisées, format de date).
4. Liste les cas qui exigent un arbitrage humain (ne les corrige pas).
5. Propose 5 règles de saisie simples pour éviter que les problèmes
   reviennent.
Limites : ne corrige pas toi-même les données de l'extrait ; ne
suppose pas que deux lignes similaires désignent la même personne.
```

**Vérification.** Comptez les lignes avant et après chaque opération ; vérifiez un échantillon de corrections ; contrôlez qu'aucune fusion n'a été faite sans arbitrage humain.

**Précautions.** Jamais de noms, dates de naissance complètes, adresses, numéros de téléphone ou informations de santé dans l'outil. Les données d'enfants appellent une vigilance renforcée.

### P8.1 : Anonymiser un texte avant traitement (module 8)

**Objectif.** Identifier et remplacer les informations permettant d'identifier des personnes, **avant** d'utiliser un texte avec un outil d'IA externe.

**Contexte.** Rapports de terrain, comptes rendus, retours de bénéficiaires.

```text
Contexte : je dois anonymiser le texte ci-dessous avant de l'utiliser
pour une analyse. Il concerne des [TYPE DE PERSONNES].
Tâche :
1. Repère tous les éléments identifiants directs (noms, prénoms,
   surnoms, numéros de téléphone, adresses, numéros de dossier,
   dates de naissance) et indirects (lieu précis + âge + situation
   familiale, profession rare, événement singulier).
2. Remplace-les par des marqueurs génériques : [PERSONNE 1],
   [VILLAGE A], [ÂGE : 40-49 ans], etc., de façon cohérente dans
   tout le texte.
3. Produis un tableau « Élément repéré (catégorie seulement, sans
   reproduire la valeur) | Marqueur | Raison ».
4. Signale les passages où le risque de réidentification reste
   élevé même après remplacement.
Données : <texte>[TEXTE]</texte>
Limites : ne résume pas, ne reformule pas le reste du texte.
```

**Vérification.** Relecture humaine intégrale ; recherche dans le texte final des noms connus (Ctrl+F) ; test « un voisin reconnaîtrait-il la personne ? ».

**Précautions.** L'anonymisation automatique n'est jamais parfaite. Pour des données particulièrement sensibles (violences, santé, statut migratoire), privilégiez une anonymisation manuelle par une personne formée, ou n'utilisez pas d'outil externe.

### P8.2 : Revue de biais d'un contenu ou d'un outil (module 8)

**Objectif.** Repérer stéréotypes, exclusions et traitements inéquitables dans un contenu (texte, campagne) ou dans les règles d'un outil (grille, formulaire, critères).

**Contexte.** Communication, RH, programmes ; avant publication ou mise en service.

```text
Contexte : [NOM DE L'ASBL] s'apprête à [publier / utiliser] le
[contenu / grille / formulaire] ci-dessous, destiné à [PUBLIC].
Nos valeurs incluent : [VALEURS].
Tâche : réalise une revue de biais et d'inclusion.
Données : <contenu>[CONTENU OU RÈGLES]</contenu>
Résultat attendu :
1. Stéréotypes ou représentations dévalorisantes (citer le passage).
2. Critères ou formulations susceptibles d'exclure ou de défavoriser
   des groupes (selon le sexe, l'âge, l'origine, le handicap, la
   langue, le lieu de vie, la situation économique), y compris par
   des critères indirects.
3. Obstacles d'accessibilité (lisibilité, langue, format, handicap).
4. Pour chaque point : gravité (faible/moyenne/forte) et
   reformulation ou correction proposée.
5. Questions à poser à des personnes concernées pour valider.
Limites : distingue les problèmes certains des problèmes possibles.
```

**Vérification.** Soumettre les conclusions à deux ou trois personnes concernées ou à une organisation représentative ; ne pas considérer la revue automatique comme suffisante.

**Précautions.** L'outil lui-même peut être biaisé ; il ne remplace pas la consultation des personnes concernées.

### P9.1 : Préparer un questionnaire fournisseur (module 9)

**Objectif.** Obtenir un questionnaire complet, adapté au cas d'usage, pour comparer objectivement des fournisseurs.

**Contexte.** Avant toute souscription d'un outil traitant des données internes ou personnelles.

```text
Contexte : [NOM DE L'ASBL], [PAYS D'IMPLANTATION ET D'INTERVENTION],
souhaite choisir un outil pour le cas d'usage suivant : [CAS D'USAGE].
Données concernées : [TYPES ET COULEUR : vert/orange/rouge].
Contraintes : [BUDGET, CONNECTIVITÉ, LANGUES, LOIS OU EXIGENCES DES
BAILLEURS].
Tâche : rédige un questionnaire à envoyer aux fournisseurs.
Résultat attendu : 25 à 35 questions fermées ou précises, regroupées
en rubriques : adéquation fonctionnelle ; données et confidentialité ;
sécurité ; réversibilité ; pérennité ; coûts (modèle de prix et coûts
annexes) ; support et formation ; accessibilité et faible débit ;
conformité. Pour chaque question, indique entre parenthèses la
réponse attendue idéale et le niveau de criticité (éliminatoire /
important / souhaitable).
Limites : ne mentionne aucun fournisseur nommément. Formule des
questions auxquelles on peut répondre par oui/non ou par une
information vérifiable, et demande les preuves (documents,
certificats, clauses).
```

**Vérification.** Comparez les réponses aux documents contractuels (conditions générales, accord de traitement des données) ; une réponse commerciale non reprise dans le contrat n'engage pas le fournisseur.

**Précautions.** Ne transmettez pas de données réelles aux fournisseurs avant la signature d'un accord de confidentialité ; utilisez des documents anonymisés pour les démonstrations.

### P10.1 : Projet de procès-verbal à partir de notes (module 10)

**Objectif.** Transformer des notes de séance en projet de PV conforme au modèle de l'organisation, sans rien inventer.

**Contexte.** Secrétariat d'un CA, d'une AG, d'un comité ; dans les 48 heures suivant la réunion.

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
   les notes, écris [À COMPLÉTER] : n'invente rien.
3. Si une discussion n'a pas abouti à une décision, écris « Aucune
   décision n'a été prise sur ce point ».
4. Termine par un tableau « N° | Décision | Responsable | Échéance »
   en reprenant uniquement ce qui figure dans les notes ; [À
   COMPLÉTER] sinon.
5. Liste à part les incohérences repérées dans les notes.
Style : neutre, concis, au passé composé.
```

**Vérification.** (1) Comparez le texte de chaque décision aux notes, caractère par caractère. (2) Vérifiez les votes et le quorum. (3) Traitez tous les [À COMPLÉTER] et incohérences. (4) Faites relire par le président.

**Précautions.** Ne pas soumettre les points à huis clos, les questions individuelles de personnel ni les informations sur des bénéficiaires identifiables. Supprimer l'enregistrement et la transcription après adoption, selon la règle fixée.

### P10.2 : Alimenter le registre des décisions (module 10)

**Objectif.** Produire les lignes du registre des décisions à partir d'un PV adopté.

**Contexte.** Après l'adoption d'un PV.

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

**Vérification.** Nombre de lignes = nombre de décisions du PV ; textes identiques ; aucune échéance inventée.

**Précautions.** Le registre est un document orange ; droits d'accès limités au CA et à la direction.

### P10.3 : Préparer l'ordre du jour (module 10)

**Objectif.** Ne rien oublier : décisions à échéance, obligations statutaires, mandats, rapports attendus.

**Contexte.** Trois à quatre semaines avant une réunion.

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

**Vérification.** Confrontez chaque point aux sources ; vérifiez les délais de convocation statutaires.

**Précautions.** Données orange.

### P11.1 : Projet d'arbre à problèmes à partir de données de terrain (module 11)

**Objectif.** Organiser les données disponibles en un arbre à problèmes provisoire, servant de support de discussion.

**Contexte.** Phase d'identification d'un projet.

```text
Contexte : [NOM DE L'ASBL] intervient en [SECTEUR] dans [TYPE DE ZONE,
sans nom de village si sensible]. Problème signalé : [PROBLÈME].
Données : <donnees>[CHIFFRES AGRÉGÉS, NOTES ANONYMISÉES, EXTRAITS
D'ÉVALUATION]</donnees>
Tâche : propose un arbre à problèmes PROVISOIRE.
Résultat attendu :
1. Problème central reformulé (une phrase, situation négative précise).
2. Causes directes et causes profondes, sur 2 à 3 niveaux, chacune
   suivie de sa source : [DONNÉES], [NOTES] ou [HYPOTHÈSE À VÉRIFIER].
3. Effets directs et indirects, avec leurs sources.
4. Les 8 questions à poser lors de l'atelier communautaire pour
   valider ou corriger l'arbre.
Limites : n'invente aucune statistique ; distingue les causes
documentées des hypothèses ; évite les explications qui
culpabilisent les populations.
```

**Vérification.** Chaque cause marquée [DONNÉES] doit renvoyer à un chiffre réel ; les hypothèses sont confirmées ou rejetées en atelier.

**Précautions.** Ne pas inclure de noms de personnes ni de lieux sensibles. Veiller à ce que la formulation n'attribue pas le problème à la « négligence » des familles.

### P11.2 : Projet de cadre logique (module 11)

**Objectif.** Produire un cadre logique cohérent, avec indicateurs SMART et hypothèses, conforme au modèle du bailleur.

**Contexte.** Formulation d'un projet.

```text
Contexte : formulation d'un projet de [DURÉE] pour [BAILLEUR, modèle
joint]. Arbre à objectifs validé : <arbre>[ARBRE]</arbre>
Stratégies retenues : [STRATÉGIES]. Données de référence disponibles :
[DONNÉES].
Tâche : propose un cadre logique respectant le modèle fourni
<modele>[MODÈLE DU BAILLEUR]</modele>.
Exigences :
1. Logique verticale explicite (si… alors…).
2. Pour chaque niveau, 1 à 3 indicateurs SMART : définition, valeur de
   référence (écrire « à établir » si elle n'existe pas), cible,
   échéance, désagrégation.
3. Sources de vérification réalistes et coût de collecte à prévoir.
4. Hypothèses externes, ni certaines ni impossibles.
5. Ensuite, liste les faiblesses de ce cadre logique (indicateurs
   difficiles à mesurer, hypothèses fragiles, liens logiques faibles).
Limites : n'invente pas de valeurs de référence ni de cibles chiffrées
sans les signaler comme « proposition à valider ».
```

**Vérification.** Lecture « si… alors… » de bas en haut ; vérification que chaque indicateur est mesurable avec les moyens budgétés ; comparaison au guide du bailleur.

**Précautions.** Données vertes ou orange.

### P11.3 : Rapport d'avancement fidèle (module 11)

**Objectif.** Rédiger un rapport d'avancement qui compare prévu et réalisé et explique les écarts, sans embellissement.

**Contexte.** Rapports périodiques aux bailleurs ou à la direction.

```text
Contexte : rapport trimestriel n° [N] du projet [NOM], pour [BAILLEUR].
Modèle : <modele>[MODÈLE]</modele>
Données :
<indicateurs>[TABLEAU PRÉVU/RÉALISÉ]</indicateurs>
<activites>[ÉTAT D'AVANCEMENT]</activites>
<terrain>[NOTES ANONYMISÉES]</terrain>
<budget>[TAUX D'EXÉCUTION PAR LIGNE]</budget>
Tâche : rédige le rapport selon le modèle.
Règles :
1. Chaque chiffre cité doit provenir des données fournies.
2. Pour tout écart supérieur à [10] % entre prévu et réalisé,
   présente l'écart, ses causes (selon les notes) et les mesures
   correctives ; si la cause n'est pas documentée, écris
   [CAUSE À PRÉCISER].
3. Présente les difficultés de façon factuelle, sans les minimiser.
4. Termine par la liste des chiffres utilisés et leur source.
```

**Vérification.** Pointage de chaque chiffre avec la table de traçabilité ; relecture par la chargée de S&E et par le responsable financier pour les données budgétaires.

**Précautions.** Aucune donnée individuelle de bénéficiaire.

### P12.1 : Extraire les données d'une facture (module 12)

**Objectif.** Obtenir les champs d'une facture dans un format prêt à importer, avec signalement des incertitudes.

**Contexte.** Comptabilité, niveau Débutant ; ou test d'un outil avant paramétrage.

```text
Contexte : je suis comptable d'une ASBL. Je dois enregistrer la
facture jointe.
Tâche : extrais les informations de la facture.
Résultat attendu : un tableau avec les champs suivants : fournisseur ;
numéro de facture ; date (AAAA-MM-JJ) ; date d'échéance ; référence de
commande ; devise ; pour chaque ligne : désignation, quantité, prix
unitaire, montant ; sous-total ; taxes (taux et montant, ou « aucune
taxe mentionnée ») ; total.
Pour chaque champ, ajoute une colonne « certitude » (élevée / moyenne
/ faible) et une colonne « remarque ».
Contrôles à effectuer et à signaler : somme des lignes = sous-total ;
sous-total + taxes = total ; présence de coordonnées bancaires (si
oui, écris seulement « coordonnées bancaires présentes », sans les
recopier).
Limites : si un champ est illisible ou absent, écris « ILLISIBLE » ou
« ABSENT ». Ne devine aucun chiffre.
```

**Vérification.** Comparez chaque champ à certitude non élevée à l'image ; recalculez les totaux dans le tableur ; vérifiez que le numéro de facture n'existe pas déjà pour ce fournisseur.

**Précautions.** Ne pas soumettre de pièces contenant des données personnelles sensibles (notes de frais avec informations médicales, bulletins de paie) à un outil non validé. Ne jamais recopier des coordonnées bancaires dans un outil externe.

### P12.2 : Proposer une imputation comptable et analytique (module 12)

**Objectif.** Obtenir une proposition d'imputation conforme **à votre** plan comptable et **à votre** plan analytique, avec justification et niveau de confiance.

**Contexte.** Saisie comptable ; formation d'une nouvelle recrue ; cas ambigus.

```text
Contexte : comptabilité d'une ASBL multi-bailleurs.
Plan comptable (extrait) : <plan>[COMPTES ET INTITULÉS]</plan>
Plan analytique : <analytique>[PROJETS / ACTIVITÉS / LIGNES]</analytique>
Règles d'éligibilité applicables : <regles>[EXTRAITS DE CONVENTION]</regles>
Pièce : <piece>[CHAMPS EXTRAITS + RÉFÉRENCE DE COMMANDE + OBJET]</piece>
Tâche : propose l'imputation de cette dépense.
Résultat attendu : tableau « Ligne de la pièce | Compte proposé
(numéro et intitulé, choisi UNIQUEMENT dans le plan fourni) |
Projet | Activité | Ligne budgétaire | Justification | Confiance
(élevée/moyenne/faible) | Point d'éligibilité à vérifier ».
Règles : si aucun compte du plan ne convient, écris « AUCUN COMPTE
ADAPTÉ » ; si l'affectation à un projet est incertaine, propose
« À DÉTERMINER » et explique pourquoi ; ne crée aucun compte.
```

**Vérification.** Vérifiez que le compte existe dans votre plan et correspond à la nature ; que le codage analytique correspond au bon de commande approuvé ; que la règle d'éligibilité citée figure bien dans la convention.

**Précautions.** Données orange. La décision d'imputation reste celle de la comptable.

### P12.3 : Analyse narrative des écarts budgétaires (module 12)

**Objectif.** Rédiger une analyse claire des écarts à partir de taux déjà calculés et des explications des responsables.

**Contexte.** Comité de direction mensuel ; rapport financier intermédiaire.

```text
Contexte : suivi budgétaire du projet [CODE], au [DATE], soit [X] %
de la période écoulée.
Données : <tableau>[LIGNE | BUDGET | RÉALISÉ | TAUX]</tableau>
<commentaires>[EXPLICATIONS DES RESPONSABLES]</commentaires>
<flexibilite>[RÈGLE : ex. réallocation autorisée jusqu'à 10 % par ligne
sans accord préalable]</flexibilite>
Tâche : rédige une note d'analyse des écarts.
Résultat attendu :
1. Synthèse en 3 phrases.
2. Pour chaque ligne dont le taux s'écarte de plus de [15] points du
   prorata : écart, explication (selon les commentaires ; sinon
   [EXPLICATION À OBTENIR]), conformité à la règle de flexibilité,
   action proposée.
3. Risques pour la fin de période (sous-exécution, dépassement,
   restitution de fonds).
4. Décisions à soumettre à la direction.
Règles : n'effectue aucun nouveau calcul ; utilise uniquement les
chiffres fournis.
```

**Vérification.** Vérifiez chaque chiffre repris ; recalculez les écarts cités (71 − 60 = 11 ; 11 / 60 = 18,3 %) ; vérifiez la règle de flexibilité dans la convention.

**Précautions.** Données orange.

### P13.1 : Concevoir les tests analytiques d'un fichier de dépenses (module 13)

**Objectif.** Obtenir les formules ou les étapes pour exécuter des tests ciblés sur toute une population de dépenses.

**Contexte.** Audit interne, contrôle de gestion, revue de fin de période.

```text
Contexte : je réalise une revue des dépenses d'une ASBL dans
[TABLEUR, LANGUE]. Colonnes : [LISTE]. Seuil d'autorisation et de bon
de commande : [SEUIL]. Un fichier fournisseurs séparé contient la
colonne code_fournisseur.
Tâche : propose une bibliothèque de tests analytiques.
Pour chaque test : objectif ; risque visé ; règle précise ; formule
exacte (colonne d'alerte « 1 si anomalie, 0 sinon ») avec la cellule
de départ ; limites et faux positifs probables.
Tests demandés : doublons (fournisseur + montant + libellé) ;
fournisseur absent du fichier fournisseurs ; pièce manquante ;
demandeur = approbateur ; fractionnement (au moins 2 dépenses sous le
seuil, même fournisseur, dans un délai de 7 jours, cumul au-dessus du
seuil) ; montants ronds au-dessus du seuil ; dépenses au-dessus du
seuil sans bon de commande ; libellés imprécis.
Ajoute une colonne « score » = somme pondérée des alertes, en
proposant des poids justifiés.
Limites : n'utilise que les colonnes listées ; signale les tests qui
nécessitent un tri préalable.
```

**Vérification.** Contrôlez le total de la population ; recalculez manuellement deux alertes par test ; comparez avec un second moyen (tableau croisé par fournisseur et par semaine pour le fractionnement).

**Précautions.** Les fichiers de dépenses sont orange ; noms de personnes physiques à remplacer par des fonctions.

### P13.2 : Rédiger une feuille de travail (module 13)

**Objectif.** Documenter les travaux de façon complète et revue.

**Contexte.** Après l'exécution des tests et l'examen des pièces.

```text
Contexte : audit interne de [PROCESSUS], période [PÉRIODE].
Données : <objectif>…</objectif> <population>…</population>
<methode>…</methode> <resultats>…</resultats> <notes>…</notes>
Tâche : rédige la feuille de travail.
Rubriques : Référence | Objectif | Population et source (avec contrôle
d'exhaustivité) | Méthode et critères | Résultats des tests (tableau) |
Priorisation et justification | Éléments examinés | Constats
(critère, constat, cause, conséquence) | Conclusion | Limites des
travaux | Préparé par / date | Revu par / date (laisser vide).
Règles : n'ajoute aucun fait absent des notes ; distingue faits
constatés et hypothèses ; n'emploie pas le mot « fraude » : écris
« indices nécessitant une investigation » lorsque c'est le cas.
```

**Vérification.** Chaque chiffre est pointé sur les résultats ; chaque fait sur les notes ; revue par un pair.

**Précautions.** Données orange, voire rouges en cas d'indices de fraude : outil validé exclusivement, ou rédaction manuelle.

### P13.3 : Formuler des recommandations actionnables (module 13)

**Objectif.** Transformer des constats en recommandations claires, priorisées, attribuées et vérifiables.

**Contexte.** Rapport d'audit, revue de contrôle interne.

```text
Tâche : pour chaque constat ci-dessous, propose 1 à 3 recommandations.
Format : tableau « Constat | Recommandation (verbe d'action) |
Cause traitée | Priorité (élevée/moyenne/faible) et justification |
Responsable proposé (fonction) | Échéance proposée | Preuve de mise en
œuvre attendue | Coût ou effort estimé (faible/moyen/élevé) ».
Données : <constats>[CONSTATS]</constats>
<organisation>[FONCTIONS DISPONIBLES]</organisation>
Règles : chaque recommandation traite la cause, pas seulement le
symptôme ; privilégie des mesures proportionnées aux moyens d'une
ASBL de [TAILLE] ; signale si une recommandation exige une décision
du conseil d'administration.
```

**Vérification.** Chaque recommandation est-elle reliée à une cause ? réaliste ? vérifiable ?

**Précautions.** Ne pas désigner de personnes nommément dans le document de travail.

### P14.1 : Fiche de poste et annonce inclusives (module 14)

**Objectif.** Produire une fiche de poste claire et une annonce inclusive, distinguant exigences indispensables et souhaitables.

**Contexte.** Ouverture d'un poste salarié ou d'une mission bénévole.

```text
Contexte : [NOM DE L'ASBL], [SECTEUR], recrute un(e) [INTITULÉ]
rattaché(e) à [FONCTION], basé(e) à [LIEU], [TYPE DE CONTRAT].
Besoins : <besoins>[MISSION, RESPONSABILITÉS, RÉSULTATS ATTENDUS]</besoins>
Tâche :
1. Rédige la fiche de poste : finalité (2 phrases) ; 5 à 7
   responsabilités principales ; compétences indispensables (5 max) ;
   compétences souhaitables (4 max) ; conditions.
2. Rédige l'annonce (350 mots max), en langage simple, avec une
   phrase encourageant les candidatures de profils divers et une
   information sur l'accessibilité et l'aménagement des entretiens.
3. Liste les exigences qui pourraient exclure des candidats sans être
   nécessaires au poste, et propose une alternative.
Limites : aucune exigence liée à l'âge, au sexe, à l'origine, à la
situation familiale ou à l'apparence ; formulation inclusive.
```

**Vérification.** Revue par la RH ; revue d'inclusion (P8.2) ; vérification des conditions contractuelles.

**Précautions.** Données vertes à orange (pas de données personnelles).

### P14.2 : Guide d'entretien structuré (module 14)

**Objectif.** Garantir des entretiens équitables, comparables et centrés sur les compétences.

**Contexte.** Préparation d'un jury de recrutement.

```text
Contexte : jury de recrutement pour [POSTE].
Grille : <grille>[CRITÈRES ET POIDS]</grille>
Tâche : rédige un guide d'entretien de 45 minutes.
Pour chaque critère : 2 questions comportementales (« Décrivez une
situation où… ») et 1 mise en situation liée au contexte d'une ASBL ;
indicateurs observables d'une réponse faible / satisfaisante /
excellente (échelle 1-3-5 décrite) ; relances possibles.
Ajoute : une introduction standard ; le temps par partie ; les
questions interdites ou à éviter (vie privée, projets familiaux, santé,
religion, origine…) ; une fiche d'évaluation individuelle vierge.
```

**Vérification.** Lien de chaque question avec un critère ; absence de questions discriminatoires ; test du guide par un collègue.

**Précautions.** Aucune donnée de candidat dans la consigne.

### P14.3 : Planning hebdomadaire des bénévoles (module 14)

**Objectif.** Obtenir un premier planning respectant les contraintes, à ajuster par le coordinateur.

**Contexte.** Coordination des bénévoles, visites, permanences.

```text
Contexte : planification des visites de la semaine du [DATE].
Besoins : <besoins>[CODE PERSONNE ACCOMPAGNÉE (P01…) | créneau
souhaité | zone | compétence requise | bénévole habituel]</besoins>
Disponibilités : <dispo>[CODE BÉNÉVOLE | créneaux | zones | compétences
| maximum de visites]</dispo>
Règles : priorité à la continuité (bénévole habituel) ; pas plus de
[N] visites par bénévole ; compétence requise respectée ; zones
compatibles.
Tâche : propose un planning sous forme de tableau « Créneau | P | B |
Zone | Règle appliquée ». Liste ensuite les besoins non couverts et
les conflits, avec des options de résolution.
Limites : n'affecte jamais un bénévole hors de ses disponibilités ;
signale toute règle impossible à respecter.
```

**Vérification.** Contrôle de chaque affectation par rapport aux disponibilités ; comptage des visites par bénévole dans le tableur.

**Précautions.** Aucun nom, adresse, information de santé ou de dépendance dans l'outil.

### P15.1 : Analyser un appel à projets et vérifier l'éligibilité (module 15)

**Objectif.** Extraire de façon exhaustive les informations clés et les critères d'éligibilité, avec référence au texte.

**Contexte.** Veille ; avant toute décision de candidature.

```text
Contexte : [NOM DE L'ASBL], profil : <profil>[STATUT, ANNÉE
D'ENREGISTREMENT, PAYS, SECTEURS, BUDGET ANNUEL, ZONES]</profil>
Appel : <appel>[TEXTE INTÉGRAL ET ANNEXES]</appel>
Tâche :
Partie 1 : Fiche d'analyse : bailleur ; objet ; priorités
thématiques ; zones ; montants min/max ; durée ; cofinancement ;
coûts indirects autorisés ; dates (questions, soumission, décision) ;
procédure (une ou deux étapes) ; documents exigés ; critères
d'évaluation et pondération ; règles sur l'usage de l'IA dans la
préparation du dossier, s'il y en a.
Partie 2 : Éligibilité : tableau « Critère (citation exacte) | Page
ou section | Notre situation selon le profil | Preuve à fournir |
Statut (rempli / non rempli / à vérifier) ».
Partie 3 : Points d'attention et questions à poser au bailleur.
Règles : cite exactement le texte pour chaque critère ; si une
information est absente de l'appel, écris « non précisé » ; ne
conclus pas à l'éligibilité globale : laisse ce jugement à
l'organisation.
```

**Vérification.** Pour chaque critère, retrouvez la citation à la page indiquée ; vérifiez l'exhaustivité en relisant la section « éligibilité » de l'appel.

**Précautions.** Le profil ne doit contenir que des informations administratives non sensibles.

### P15.2 : Note conceptuelle à partir du dossier de matière première (module 15)

**Objectif.** Mettre en forme une note conceptuelle conforme au modèle du bailleur, fondée sur la matière première de l'organisation.

**Contexte.** Après décision « go ».

```text
Contexte : note conceptuelle pour [APPEL], modèle :
<modele>[RUBRIQUES ET LIMITES]</modele>.
Critères d'évaluation : <criteres>[CRITÈRES ET POIDS]</criteres>
Matière première : <matiere>[DONNÉES, RÉSULTATS PASSÉS, ENSEIGNEMENTS,
PARTENAIRES, TÉMOIGNAGES ANONYMISÉS]</matiere>
Logique du projet : <logique>[ARBRE À OBJECTIFS, CADRE LOGIQUE
RÉSUMÉ]</logique>
Tâche : rédige la note conceptuelle.
Règles :
1. Utilise UNIQUEMENT les faits, chiffres et résultats fournis ;
   aucune statistique externe non fournie.
2. Chaque rubrique répond explicitement aux critères d'évaluation
   correspondants.
3. Respecte les limites de longueur par rubrique.
4. Termine par un tableau « Affirmation chiffrée | Source dans la
   matière première ».
5. Signale les rubriques où la matière première est insuffisante.
Style : précis, concret, sans superlatifs.
```

**Vérification.** Pointage de chaque affirmation chiffrée ; relecture de cohérence avec le budget et le cadre logique ; vérification des engagements (partenaires, cofinancement) avec les personnes concernées.

**Précautions.** Pas de données personnelles ; témoignages anonymisés et utilisés avec consentement ; respect des règles du bailleur sur l'IA.

### P15.3 : Vérifier la cohérence budget–activités–règles (module 15)

**Objectif.** Repérer les incohérences entre budget, activités et règles du bailleur avant soumission.

**Contexte.** Finalisation d'une proposition.

```text
Données : <budget>[LIGNES : code, intitulé, unité, quantité, coût
unitaire, total, activité liée]</budget> <activites>[LISTE]</activites>
<regles>[RÈGLES BUDGÉTAIRES DE L'APPEL]</regles>
Tâche : vérifie la cohérence.
1. Activités sans ligne budgétaire et lignes sans activité.
2. Lignes potentiellement inéligibles selon les règles (citer la
   règle).
3. Lignes dont le coût unitaire mérite une justification (écart
   inhabituel, unité ambiguë).
4. Respect des plafonds (coûts indirects, personnel, équipements,
   cofinancement) : indique le calcul que JE dois vérifier dans le
   tableur, sans le faire toi-même.
5. Points à expliquer dans la note justificative.
```

**Vérification.** Vérification de chaque point sur le budget et sur le texte de l'appel.

**Précautions.** Données orange.

### P16.1 : Normaliser des offres hétérogènes dans un tableau comparatif (module 16)

**Objectif.** Extraire et présenter les offres de façon homogène, avec les écarts par rapport aux spécifications.

**Contexte.** Consultation de fournisseurs, après ouverture des offres.

```text
Contexte : consultation pour [OBJET], quantité [Q], livraison à [LIEU].
Spécifications : <specs>[SPÉCIFICATIONS]</specs>
Offres : <offre_A>…</offre_A> <offre_B>…</offre_B> <offre_C>…</offre_C>
Tâche : produis un tableau comparatif normalisé.
Lignes : prix unitaire ; quantité ; prix total ; frais annexes
(transport, installation, formation) ; prix total rendu site ;
devise ; délai ; garantie ; validité de l'offre ; conditions de
paiement ; documents fournis ; conformité à chaque spécification
(conforme / non conforme / non précisé, avec citation de l'offre).
Règles : cite la page ou le passage de chaque valeur ; écris
« NON PRÉCISÉ » si l'offre ne mentionne pas l'information ; ne
convertis pas les devises ; ne note pas et ne classe pas les offres.
Ajoute la liste des points à clarifier par écrit auprès des
fournisseurs (selon le règlement de consultation).
```

**Vérification.** Pointage de chaque cellule ; recalcul des totaux au tableur ; contrôle des unités (prix par pièce ou par lot ?).

**Précautions.** Les offres sont confidentielles ; outil validé exclusivement. Aucune transmission d'une offre à un autre fournisseur.

### P16.2 : Rapprochement commande / livraison / facture (module 16)

**Objectif.** Repérer les écarts de quantités, de prix et de références avant paiement.

**Contexte.** Réception, avant transmission de la facture au paiement.

```text
Tâche : compare les trois documents ci-dessous ligne par ligne.
<commande>…</commande> <livraison>…</livraison> <facture>…</facture>
Résultat attendu : tableau « Article | Qté commandée | Qté livrée |
Réserves | Qté facturée | Prix commandé | Prix facturé | Écart |
Action proposée (payer / bloquer partiellement / bloquer / clarifier) ».
Règles : toute réserve à la livraison entraîne au minimum
« clarifier » ; ne calcule pas les montants à bloquer : indique la
formule que je dois appliquer.
```

**Vérification.** Contrôle sur les documents originaux ; vérification des signatures et de l'indépendance du réceptionnaire.

**Précautions.** Données orange ; coordonnées bancaires non recopiées.

### P17.1 : Calendrier éditorial à partir d'un programme réel (module 17)

**Objectif.** Planifier des contenus reliés aux activités réelles, aux publics et aux objectifs.

**Contexte.** Communication ; début de trimestre.

```text
Contexte : [NOM DE L'ASBL]. Charte éditoriale :
<charte>[TON, MOTS, RÈGLES DE REPRÉSENTATION]</charte>
Fiche programme vérifiée : <programme>[ACTIVITÉS, DATES, LIEUX
AUTORISÉS, CHIFFRES VALIDÉS, TÉMOINS AYANT CONSENTI (codes)]</programme>
Objectifs du trimestre : [OBJECTIFS]. Canaux : [CANAUX]. Capacité :
[N] contenus par semaine. Temps forts : [DATES].
Tâche : propose un calendrier éditorial de 13 semaines.
Format : tableau « Semaine | Date | Canal | Public | Objectif |
Message clé | Format | Activité ou fait source (référence dans la
fiche) | Consentement requis (oui/non) | Responsable ».
Règles : chaque contenu repose sur un élément de la fiche programme ;
n'invente aucun fait ; équilibre les publics et les formats ;
signale les semaines sans activité à valoriser.
```

**Vérification.** Chaque ligne renvoie à un élément vérifié de la fiche programme.

**Précautions.** Pas de noms ni de lieux précis de bénéficiaires ; codes pour les témoins.

### P17.2 : Déclinaison multicanal fidèle (module 17)

**Objectif.** Adapter un contenu vérifié à plusieurs canaux et publics sans altérer les faits.

**Contexte.** Production hebdomadaire.

```text
Charte : <charte>…</charte>
Contenu pivot vérifié : <pivot>…</pivot>
Tâche : produis les déclinaisons suivantes : [ex. publication courte
(280 caractères) ; publication longue (150 mots) ; paragraphe de
newsletter (120 mots) ; version facile à lire (phrases de 12 mots
max) ; texte alternatif de l'image].
Règles : n'ajoute aucun fait, chiffre ou citation absent du pivot ;
respecte la charte ; termine par la liste des faits utilisés.
```

**Vérification.** Comparaison des faits avec le pivot ; vigilance sur les glissements vers l'impact non prouvé.

**Précautions.** Contenus verts une fois validés.

### P18.1 : Classifier et synthétiser des retours communautaires (module 18)

**Objectif.** Proposer une catégorie et un niveau d'urgence pour des retours **déjà triés** (cas sensibles exclus), et synthétiser les tendances.

**Contexte.** Mécanisme de retours ; traitement hebdomadaire ou mensuel.

```text
Contexte : mécanisme de retours communautaires d'un projet de
[SECTEUR]. Les retours ci-dessous sont anonymisés ; les cas sensibles
ont déjà été retirés et transmis à la personne référente.
Catégories : [LISTE : information, qualité du service, accès,
comportement du personnel, suggestion, remerciement, autre].
Données : <retours>[CODE | DATE | CANAL | LANGUE | TEXTE]</retours>
Tâche :
1. Pour chaque retour : catégorie proposée ; urgence (faible /
   moyenne / élevée) ; justification courte ; drapeau « À VÉRIFIER PAR
   LE RÉFÉRENT » si le texte contient le moindre signe possible
   d'abus, de violence, de menace, de détresse ou d'atteinte à la
   sécurité, même incertain.
2. Synthèse : nombre par catégorie ; 3 à 5 tendances ; retours
   minoritaires mais importants ; citations courtes illustratives
   (sans détail identifiant).
Règles : en cas de doute sur la sensibilité, signale toujours.
N'interprète pas au-delà du texte.
```

**Vérification.** Double codage manuel d'un échantillon de 20 % ; comparaison ; ajustement des catégories ; vérification que tous les drapeaux ont été examinés.

**Précautions.** Aucune donnée identifiante ; outil validé ; les sorties sont des données orange à rouges selon le contenu.

### P18.2 : Rapport de terrain structuré à partir de notes (module 18)

**Objectif.** Transformer des notes brutes (écrites ou transcrites) en rapport structuré et factuel.

**Contexte.** Agents de terrain, superviseurs ; après une visite ou une mission.

```text
Contexte : rapport de [visite / mission] du [DATE] dans [ZONE, au
niveau de précision autorisé], objectif : [OBJECTIF].
Modèle : <modele>[RUBRIQUES : activités réalisées, observations,
difficultés, retours des participants, actions de suivi, besoins]
</modele>
Notes : <notes>[NOTES PSEUDONYMISÉES]</notes>
Tâche : rédige le rapport selon le modèle.
Règles : distingue faits observés, propos rapportés et
interprétations ; chiffres uniquement s'ils figurent dans les notes ;
tableau final des actions de suivi (action | responsable | échéance)
avec « NON DÉFINI » si nécessaire ; signale tout élément évoquant un
risque de protection en tête du rapport avec la mention « À
TRANSMETTRE AU RÉFÉRENT ».
```

**Vérification.** Comparaison avec les notes ; contrôle des chiffres ; validation par le superviseur.

**Précautions.** Pseudonymisation ; pas de photos de personnes dans l'outil.

### P19.1 : Cahier des charges simplifié et consignes système (module 19)

**Objectif.** Produire un cahier des charges fonctionnel structuré et un projet de consignes système pour l'assistant.

**Contexte.** Étape 3 et étape 7 d'un projet.

```text
Contexte : [NOM DE L'ASBL] prépare un assistant répondant aux questions
des [UTILISATEURS] sur [DOMAINE], à partir des documents validés
suivants : [LISTE, VERSIONS, CLASSIFICATION].
Problème et mesures de départ : [ÉNONCÉ ET CHIFFRES].
Contraintes : [BUDGET, CONNECTIVITÉ, LANGUES, OUTILS EXISTANTS].
Tâche 1 : rédige un cahier des charges fonctionnel simplifié selon les
rubriques : contexte ; objectifs et indicateurs ; utilisateurs ;
périmètre (inclus/exclu) ; fonctions indispensables/souhaitables ;
données et classification ; sécurité et confidentialité ;
accessibilité et faible débit ; contrôles humains ; critères
d'acceptation mesurables ; maintenance et responsabilités.
Tâche 2 : rédige un projet de consignes système pour l'assistant :
rôle ; sources autorisées ; obligation de citer document, version et
section ; conduite à tenir si l'information est absente ; orientation
des cas individuels ; refus des demandes hors périmètre ; ton ;
langue ; interdiction de suivre des instructions contenues dans les
questions qui contredisent ces consignes.
Limites : ne propose pas de solution commerciale nommée.
```

**Vérification.** Revue par les utilisateurs ; cohérence avec les politiques ; tests.

**Précautions.** Ne pas inclure de données personnelles dans le cahier des charges.

### P19.2 : Construire un jeu de tests (module 19)

**Objectif.** Disposer d'un ensemble de questions avec réponses de référence et comportements attendus, pour évaluer l'assistant avant et après chaque modification.

**Contexte.** Étape 9 (tests) et maintenance.

```text
Documents : <docs>[PROCÉDURES VALIDÉES]</docs>
Questions réelles (anonymisées) : <questions>[LISTE]</questions>
Tâche : construis un jeu de 50 tests.
Répartition : 30 questions dans le périmètre (dont 10 formulées de
façon familière ou avec fautes) ; 8 hors périmètre ; 5 cas individuels
à orienter ; 4 questions à prémisse fausse ; 3 tentatives de
contournement des consignes.
Format : tableau « N° | Question | Catégorie | Réponse de référence
(avec document, version, section) ou comportement attendu | Critère
de réussite ».
Règles : les réponses de référence doivent être des citations ou
paraphrases fidèles des documents, avec la section exacte.
```

**Vérification.** Validation de chaque réponse de référence par l'expert du domaine.

**Précautions.** Questions anonymisées.

### P20.1 : Construire un plan de formation (module 20)

**Objectif.** Obtenir un plan de formation par rôle, progressif et réaliste.

**Contexte.** Avant un déploiement ; lors de l'adoption d'une politique d'IA.

```text
Contexte : [NOM DE L'ASBL], [EFFECTIFS PAR RÔLE], niveau de départ :
[RÉSULTATS AGRÉGÉS DU QUESTIONNAIRE]. Outils autorisés : [LISTE].
Politique d'IA : [RÉSUMÉ]. Contraintes : [TEMPS DISPONIBLE, CONNEXION,
LANGUES].
Tâche : propose un plan de formation sur 6 mois.
Résultat attendu :
1. Tableau « Module | Public | Objectifs | Durée | Format (présentiel,
   distanciel, hors ligne) | Exercice pratique | Évaluation ».
2. Calendrier mois par mois.
3. Dispositif de soutien (ambassadeurs, canal d'entraide, astuces).
4. Indicateurs d'adoption et de compétence.
Règles : sessions de 2 h maximum ; chaque module comporte un exercice
sur une tâche réelle ; le socle commun inclut la classification des
données et la vérification des réponses.
```

**Vérification.** Cohérence avec la politique et les outils ; réalisme du temps demandé ; présence d'exercices réels.

**Précautions.** Données agrégées uniquement.

### P22.1 : Construire la feuille de route à 90 jours (module 22)

**Objectif.** Transformer un diagnostic et des priorités en plan daté, budgété, attribué et mesurable.

**Contexte.** Direction ; après les travaux des modules 5, 6 et 8.

```text
Contexte : [NOM DE L'ASBL], [TAILLE], niveau de maturité numérique
[X/5]. Ressources : [PERSONNES ET TEMPS DISPONIBLE], budget [MONTANT].
Contraintes : [CONNECTIVITÉ, CALENDRIER, RÉUNIONS DU CA].
Constats : <constats>[5 CONSTATS AVEC FAITS]</constats>
Priorités retenues : <priorites>[FONDATIONS, PILOTES, PROJET À
PRÉPARER]</priorites>
Tâche : construis un plan à 13 semaines.
Résultat attendu :
1. Tableau « Semaines | Action | Livrable | Responsable (fonction) |
   Jalon ».
2. Budget : postes et méthode de calcul (sans inventer de prix ;
   laisse « à chiffrer » si nécessaire).
3. Matrice RACI.
4. Indicateurs : « Indicateur | Départ | Cible | Source ».
5. Risques du plan et mesures.
6. Modalités d'évaluation (semaine 11) et de décision (semaine 13).
Règles : pas plus de 2 pilotes ; charge compatible avec le temps
disponible indiqué ; la politique d'IA doit être adoptée avant le
démarrage des pilotes impliquant des données internes.
```

**Vérification.** Réalisme de la charge (somme des heures par personne) ; cohérence des dépendances (politique avant pilotes) ; indicateurs avec valeur de départ ; budget recalculé au tableur.

**Précautions.** Données orange (plan interne).


