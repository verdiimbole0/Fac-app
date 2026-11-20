# Module 8 — Éthique, responsabilité, sécurité et réglementation de l'IA

## 8.1 Mise en situation

La Maison des Aînés Solidaires accompagne des personnes âgées isolées. Pour mieux organiser les visites, Thomas, coordinateur des bénévoles, a eu une idée : enregistrer les appels téléphoniques des personnes accompagnées, les faire transcrire et résumer par un assistant gratuit, puis demander à l'outil d'identifier « les personnes qui montrent des signes de déclin cognitif » afin de leur envoyer plus de visites.

L'intention est généreuse. Pourtant, le projet cumule presque tous les risques que ce module va examiner : des données de santé déduites sans base médicale, des personnes vulnérables enregistrées sans consentement éclairé, un outil gratuit dont les conditions de traitement des données n'ont pas été lues, une forme de profilage, et des décisions — l'intensité de l'accompagnement — qui dépendraient d'un résultat automatique non vérifiable.

Ce module ne vise pas à décourager l'innovation. Il vise à donner à chacun les réflexes qui permettent d'innover sans nuire.

## 8.2 Problématique

Les ASBL agissent souvent auprès de personnes en situation de vulnérabilité, dans un rapport de confiance. Une erreur, une fuite ou une discrimination causée par un outil numérique peut avoir des conséquences graves pour ces personnes, et ruiner la confiance des communautés, des bailleurs et du public. En outre, le cadre juridique de l'IA et de la protection des données se renforce rapidement dans de nombreux pays. L'éthique n'est donc pas un supplément d'âme : c'est une condition de légitimité et de durabilité.

## 8.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. expliquer les principes éthiques internationaux applicables à l'IA ;
2. reconnaître les biais et les risques de discrimination ;
3. appliquer les principes de protection des données : minimisation, finalité, base légale, consentement, sécurité ;
4. classer les données selon le « feu tricolore » et choisir l'outil approprié ;
5. organiser la supervision humaine et identifier les décisions qui doivent rester humaines ;
6. prendre en compte la cybersécurité, le droit d'auteur, l'impact environnemental et la protection des personnes vulnérables ;
7. situer votre organisation par rapport aux cadres internationaux et nationaux ;
8. anonymiser un texte avant traitement et conduire une revue de biais.

## 8.4 Notions et définitions

- **Biais algorithmique** : écart systématique dans les résultats d'un système, qui défavorise ou favorise certains groupes.
- **Discrimination** : traitement défavorable d'une personne fondé sur un critère prohibé (sexe, origine, handicap, âge, religion, etc., selon les lois applicables).
- **Transparence** : fait d'informer les personnes qu'un système d'IA est utilisé, à quelles fins et avec quelles limites.
- **Explicabilité** : capacité à donner aux personnes concernées des raisons compréhensibles d'un résultat.
- **Minimisation des données** : ne collecter et ne traiter que les données strictement nécessaires à la finalité.
- **Finalité** : objectif précis et légitime pour lequel des données sont traitées.
- **Consentement éclairé** : accord libre, spécifique, informé et univoque, qui peut être retiré.
- **Profilage** : traitement automatisé visant à évaluer certains aspects d'une personne (comportement, santé, fiabilité…).
- **Supervision humaine** : capacité organisée de personnes compétentes à comprendre, contrôler, corriger, interrompre ou refuser le résultat d'un système.

## 8.5 Explications détaillées

### Les principes internationaux de référence

Plusieurs textes internationaux convergent sur un socle de principes. Il est important de distinguer leur **nature juridique**.

| Texte | Nature | Ce qu'il apporte à une ASBL |
|---|---|---|
| Recommandation de l'UNESCO sur l'éthique de l'IA (2021) | Recommandation adoptée par les États membres ; non contraignante pour les organisations | Socle de valeurs : droits humains et dignité, environnement, diversité et inclusion ; principes de proportionnalité, sûreté, équité, transparence, responsabilité, supervision humaine |
| Principes de l'OCDE sur l'IA (2019, révisés en 2024) | Instrument non contraignant, engagement politique des pays adhérents | Croissance inclusive, droits humains, transparence, robustesse et sécurité, responsabilité ; la révision de 2024 renforce l'attention à la sécurité, à la vie privée, à la propriété intellectuelle et à l'intégrité de l'information |
| NIST AI RMF 1.0 (2023) et profil IA générative (2024) | Cadres volontaires | Démarche de gestion des risques en quatre fonctions : gouverner, cartographier, mesurer, gérer ; liste de risques propres à l'IA générative |
| ISO/IEC 42001:2023 | Norme volontaire, certifiable | Exigences d'un système de management de l'IA : politique, rôles, évaluation des risques et des impacts, contrôles, amélioration continue |
| Convention-cadre du Conseil de l'Europe sur l'IA (2024) | Traité contraignant pour les États qui le ratifient | Obligations des États pour que l'IA respecte les droits humains, la démocratie et l'État de droit |
| Règlement (UE) 2024/1689 (AI Act) | Loi contraignante dans l'Union européenne | Approche par niveaux de risque : pratiques interdites, systèmes à haut risque, obligations de transparence |

Ces textes partagent une idée centrale : **plus un usage de l'IA peut affecter les droits et la sécurité des personnes, plus les exigences de contrôle, de transparence et de supervision humaine doivent être élevées.**

### Droits humains, dignité et équité

Dans une ASBL, ces principes se traduisent par des questions très concrètes :

- **Dignité** : l'usage de l'IA respecte-t-il les personnes ? Utiliser des images générées de « bénéficiaires souffrants » pour une campagne de dons est contraire à la dignité et trompeur. Faire répondre un robot à une personne en détresse sans possibilité de parler à un humain l'est aussi.
- **Équité** : l'outil fonctionne-t-il aussi bien pour tout le monde ? Un système de transcription qui comprend mal certains accents, une traduction médiocre dans les langues minoritaires, un formulaire en ligne inaccessible aux personnes malvoyantes créent des inégalités d'accès.
- **Autonomie** : les personnes gardent-elles la maîtrise des décisions qui les concernent, et peuvent-elles les contester ?

### Biais et discrimination

Les biais peuvent naître à chaque étape :

| Origine | Exemple dans une ASBL |
|---|---|
| Données d'entraînement déséquilibrées | Un modèle de « risque d'abandon scolaire » entraîné sur des données d'un quartier urbain, appliqué à une zone rurale |
| Variables substituts (*proxies*) | Utiliser le code postal, qui peut refléter l'origine ou le niveau social |
| Historique discriminatoire | Un tri de candidatures appris sur des recrutements passés qui favorisaient un profil |
| Conception de l'outil | Formulaire exigeant une adresse fixe, excluant les personnes sans domicile |
| Usage | Appliquer l'outil hors du contexte pour lequel il a été conçu |
| IA générative | Descriptions ou images stéréotypées de certains groupes, de certains métiers |

Parades : interroger la représentativité des données ; tester les résultats par sous-groupes (sexe, âge, langue, zone) ; exclure les variables sensibles et leurs substituts lorsqu'ils ne sont pas justifiés ; impliquer des personnes concernées dans la conception ; conserver une décision humaine motivée ; prévoir un recours.

### Transparence et explicabilité

Les personnes ont le droit de savoir quand un système d'IA intervient dans une interaction ou une décision qui les concerne. Bonnes pratiques :

- signaler qu'un assistant en ligne est automatisé et offrir un contact humain ;
- mentionner, dans les politiques de confidentialité, les traitements assistés par l'IA ;
- indiquer, en interne et selon les règles de l'organisation, quand un document a été produit avec une aide de l'IA ;
- pour toute décision affectant une personne, pouvoir en expliquer les motifs en termes compréhensibles — ce qui suppose que la décision ait été prise par un humain capable de la justifier.

### Confidentialité et protection des données

![Figure 8.1 — Le feu tricolore de classification des données](03_ILLUSTRATIONS/figures/fig_8_1.svg)

Les grands principes de protection des données, communs à de nombreuses législations, sont :

1. **Licéité** : disposer d'une base légale pour traiter les données (consentement, contrat, obligation légale, intérêt légitime, etc., selon les lois applicables).
2. **Finalité** : utiliser les données pour l'objectif annoncé, pas pour un autre.
3. **Minimisation** : seulement les données nécessaires.
4. **Exactitude** : des données à jour et justes.
5. **Limitation de la conservation** : ne pas garder les données plus longtemps que nécessaire.
6. **Sécurité** : protéger contre l'accès non autorisé, la perte, la fuite.
7. **Responsabilité** : pouvoir démontrer le respect de ces principes.

**Le feu tricolore** (annexe 11) traduit ces principes en règle d'usage quotidienne :

| Couleur | Définition | Exemples | Outils autorisés |
|---|---|---|---|
| 🟢 **Vert** | Information publique ou destinée à l'être | Rapport annuel publié, article du site, appel à projets public | Outils grand public autorisés, avec vérification des sorties |
| 🟠 **Orange** | Information interne, non personnelle ou agrégée | Budget non publié, procédures, PV de CA, statistiques agrégées | Outils professionnels validés par l'organisation (contrat prévoyant la confidentialité et l'absence d'utilisation des données pour l'entraînement), après minimisation |
| 🔴 **Rouge** | Données personnelles identifiantes, données sensibles, informations confidentielles | Listes nominatives de bénéficiaires, données de santé, données d'enfants, salaires, dossiers disciplinaires, coordonnées bancaires, signalements d'abus | Interdit dans tout outil non validé spécifiquement. Anonymisation préalable, base légale, accord du responsable, outil sécurisé |

> **⚖️ Adaptation réglementaire** — Les lois de protection des données diffèrent selon les pays : définitions des données sensibles, bases légales, droits des personnes, règles de transfert international, obligations de déclaration. Dans l'Union européenne, le règlement (UE) 2016/679 (RGPD) s'applique ; d'autres pays disposent de lois proches ; certains États ont ratifié la Convention 108+ du Conseil de l'Europe. Lorsque vous utilisez un outil en ligne, vos données peuvent être traitées dans un autre pays : vérifiez la localisation des serveurs et les conditions de transfert.

**Avant d'utiliser un outil en ligne avec des données internes, vérifiez au minimum :**

- les conditions d'utilisation et la politique de confidentialité (les données saisies servent-elles à entraîner les modèles ? peut-on le désactiver ?) ;
- la durée de conservation des conversations et des fichiers ;
- la localisation des traitements ;
- l'existence d'une offre professionnelle avec engagement contractuel de confidentialité ;
- la possibilité de supprimer ses données.

> **🔎 À retenir** — Les offres gratuites ne sont pas nécessairement dangereuses, mais elles n'offrent généralement pas les garanties contractuelles nécessaires pour des données internes ou personnelles. Par défaut : vert uniquement.

### Le consentement

Lorsque le consentement est la base légale (enregistrement d'un entretien, photo d'un bénéficiaire, participation à une enquête), il doit être **libre** (pas de condition d'accès à un service), **spécifique** (pour un usage précis), **éclairé** (expliqué dans une langue et des termes compris), **univoque** et **révocable**. Dans un contexte d'aide, la liberté du consentement est fragile : une personne qui dépend de l'ASBL pour un service peut se sentir obligée d'accepter. Il faut donc proposer une réelle alternative et ne jamais conditionner l'aide au consentement à un traitement non nécessaire.

### Cybersécurité

L'IA introduit des risques de sécurité nouveaux, en plus des risques classiques.

| Risque | Description | Mesures |
|---|---|---|
| Fuite par saisie | Données confidentielles collées dans un outil non validé | Feu tricolore, formation, outils validés |
| Hameçonnage amélioré | Courriels frauduleux très crédibles, imitation de voix d'un dirigeant pour demander un virement | Procédure de vérification par un second canal pour tout paiement inhabituel |
| Injection de prompt | Instructions cachées dans un document ou une page web, qui détournent un assistant ou un agent (premier risque du Top 10 OWASP pour les applications de modèles de langage) | Limiter les droits des agents ; validation humaine des actions ; ne pas faire traiter de contenus non fiables par des agents disposant de droits étendus |
| Comptes compromis | Accès d'un attaquant aux outils et à l'historique des conversations | Double authentification, mots de passe uniques, revue des accès |
| Extensions et applications non vérifiées | Modules complémentaires qui accèdent aux données | Liste des outils autorisés (annexe 9) |

### Supervision humaine et décisions automatisées

![Figure 8.2 — Trois modes de supervision humaine](03_ILLUSTRATIONS/figures/fig_8_2.svg)

La supervision humaine doit être **réelle** : une personne qui valide 200 propositions par heure sans les lire ne supervise rien (c'est le « biais d'automatisation », tendance à faire excessivement confiance à la machine). Elle suppose du temps, des compétences, le droit de refuser, et une trace de la validation.

> **⚖️ Adaptation réglementaire** — Plusieurs textes encadrent les décisions fondées exclusivement sur un traitement automatisé et produisant des effets importants pour les personnes : par exemple l'article 22 du RGPD dans l'Union européenne, ou la Convention 108+. Le règlement européen sur l'IA classe en « haut risque » certains usages, notamment dans l'emploi, l'éducation ou l'accès à des services essentiels, avec des obligations renforcées ; son calendrier d'application a été modifié en 2026 par un règlement dit « omnibus », qui a reporté certaines échéances relatives aux systèmes à haut risque — vérifiez les dates en vigueur sur le site officiel EUR-Lex à la date de votre projet.

**Décisions qui doivent impérativement rester sous contrôle humain dans une ASBL :**

| Domaine | Décisions | Rôle possible de l'IA |
|---|---|---|
| Bénéficiaires | Admission ou refus d'un service, niveau d'aide, sortie d'un programme, signalement de protection | Aide à l'organisation de l'information, jamais la décision |
| Ressources humaines | Recrutement, évaluation, sanction, licenciement, rémunération | Rédaction de supports, organisation des candidatures selon une grille humaine |
| Bénévoles | Acceptation, exclusion | Planification logistique |
| Finances | Approbation de paiements, validation des écritures, choix de fournisseurs | Propositions, contrôles, alertes |
| Gouvernance | Adoption de politiques, de budgets, de comptes | Préparation de documents |
| Communication externe | Publication au nom de l'ASBL | Brouillons |
| Protection | Toute situation d'abus, d'exploitation, de danger | Aucune automatisation du traitement ; orientation immédiate vers un référent humain |

### Hallucinations et responsabilité

L'organisation reste responsable de ce qu'elle publie, transmet ou décide, même si un outil d'IA l'a produit. Un rapport contenant un chiffre inventé engage l'ASBL vis-à-vis du bailleur. D'où la règle : **tout contenu externe est relu et validé par une personne habilitée.**

### Droits d'auteur et propriété intellectuelle

Trois questions se posent :

1. **Ce que l'on fournit à l'outil** : avez-vous le droit d'utiliser ce document (rapport d'un partenaire, article payant, photo d'un tiers) ?
2. **Ce que l'outil produit** : les règles sur la protection des contenus générés par IA et sur les droits du fournisseur varient selon les pays et les conditions d'utilisation des outils. Un contenu généré peut aussi reproduire des éléments protégés.
3. **Ce que vous publiez** : citez vos sources ; ne présentez pas une image générée comme une photo réelle ; vérifiez les conditions d'utilisation commerciale des images générées.

### Sécurité des bénéficiaires et personnes vulnérables

Les enfants, les personnes âgées dépendantes, les personnes en situation de handicap, les personnes déplacées ou réfugiées, les victimes de violences méritent une protection renforcée :

- aucune donnée les concernant dans un outil non validé ;
- prudence extrême sur toute forme de profilage ou de « score » ;
- attention aux risques de réidentification à partir de données apparemment anonymes (un village, un âge et une situation familiale peuvent suffire à identifier une personne) ;
- dans les contextes de crise, prise en compte des risques d'accès aux données par des acteurs hostiles — un enjeu détaillé par le *Handbook on Data Protection in Humanitarian Action* du CICR (Marelli, 2024), y compris pour les données hébergées chez des prestataires de cloud.

### Impact environnemental

L'IA consomme de l'énergie, principalement dans les centres de données. Selon l'Agence internationale de l'énergie, les centres de données ont consommé environ 415 TWh d'électricité en 2024, soit environ 1,5 % de la consommation mondiale, et cette consommation pourrait plus que doubler pour atteindre environ 945 TWh en 2030 dans son scénario de référence, l'IA étant le principal moteur de cette croissance (AIE, 2025). À l'échelle d'une ASBL, la sobriété consiste à : utiliser l'IA lorsqu'elle apporte une valeur réelle ; préférer des outils proportionnés (pas de génération d'images ou de vidéos superflues) ; éviter les requêtes répétées inutiles ; intégrer ce critère dans le choix des fournisseurs lorsque l'information est disponible.

### Réglementation internationale et nationale : comment s'y retrouver

1. **Identifiez les lois applicables** : le pays du siège, les pays d'intervention, le pays de localisation des données, et les règles imposées par vos bailleurs.
2. **Distinguez** : lois contraignantes (protection des données, réglementation de l'IA lorsqu'elle existe, droit du travail, droit d'auteur) ; normes volontaires (ISO/IEC 42001) ; cadres de référence (UNESCO, OCDE, NIST) ; exigences contractuelles des bailleurs.
3. **Désignez une personne responsable** du suivi réglementaire, même à temps partiel.
4. **Consultez un juriste** pour les traitements de données sensibles ou les projets d'envergure.

## 8.6 Application professionnelle : refonder le projet de Thomas

Reprenons la mise en situation et appliquons la démarche.

| Question | Réponse pour le projet initial | Projet révisé |
|---|---|---|
| Quelle finalité ? | Repérer un déclin cognitif | Mieux planifier les visites selon les besoins **exprimés** |
| Données nécessaires ? | Enregistrements d'appels, santé déduite | Fréquence de visite souhaitée, disponibilités, demandes explicites |
| Base légale / consentement ? | Absent | Information claire, consentement recueilli à l'entrée dans le programme pour les seules données nécessaires |
| Outil ? | Gratuit, non vérifié | Tableur ou base de données interne ; l'IA n'intervient que sur des données vertes (planning sans noms) |
| Décision ? | Automatique (score) | Humaine : le coordinateur et l'infirmière référente, si un besoin de santé est exprimé |
| Recours ? | Aucun | Les personnes peuvent demander plus ou moins de visites à tout moment |

Le projet révisé conserve l'objectif — mieux accompagner — sans profilage ni données de santé déduites.

### Processus de mise en œuvre d'un examen éthique simplifié (pour tout nouveau cas d'usage)

1. Décrire le cas d'usage (fiche d'opportunité, module 6).
2. Classer les données (feu tricolore).
3. Identifier les personnes affectées et l'impact d'une erreur.
4. Vérifier finalité, minimisation, base légale, information des personnes.
5. Évaluer les risques de biais ; prévoir un test par sous-groupes si l'outil classe ou évalue.
6. Définir le mode de supervision humaine et les décisions réservées.
7. Vérifier l'outil (contrat, localisation, entraînement, sécurité).
8. Consigner l'analyse dans le registre des risques IA (annexe 8) et le registre des outils (annexe 9).
9. Faire valider par le référent IA et, pour les cas à risque élevé, par la direction.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Politique d'utilisation d'une page, feu tricolore affiché, formation d'une heure, examen éthique simplifié sous forme de checklist | Annexes 10, 11, 12 | Temps | Dépend de la discipline individuelle |
| Intermédiaire | Outils professionnels validés, paramètres de confidentialité configurés par l'administrateur, registre des outils et des risques, référent IA | Suite professionnelle, registres | Abonnements | Exige un suivi régulier |
| Avancé | Système de management de l'IA inspiré d'ISO/IEC 42001 ; analyses d'impact formalisées ; journalisation et surveillance des usages ; prévention des fuites de données | Outils de gouvernance, de sécurité et de journalisation | Élevés | Compétences juridiques et techniques |

## 8.7 Prompts prêts à l'emploi

### Fiche P8.1 — Anonymiser un texte avant traitement

**A. Titre.** Repérage des éléments identifiants dans un texte.

**B. Objectif.** Identifier et remplacer les informations permettant d'identifier des personnes, **avant** d'utiliser un texte avec un outil d'IA externe.

**C. Contexte d'utilisation.** Rapports de terrain, comptes rendus, retours de bénéficiaires.

**D. Données nécessaires.** Le texte. **Important :** cette fiche s'utilise avec un outil **validé par l'organisation** pour des données orange ou rouges (outil interne, offre professionnelle avec garanties) — ou bien elle sert de liste de contrôle pour une anonymisation manuelle. Elle ne doit pas être utilisée avec un outil grand public sur un texte contenant des données personnelles : ce serait divulguer précisément ce que l'on veut protéger.

**E. Prompt complet.**

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

**F. Instructions d'utilisation.** Vérifiez d'abord que l'outil est autorisé pour ce niveau de données. Conservez l'éventuelle table de correspondance séparément, en accès restreint, ou détruisez-la si elle n'est pas nécessaire (anonymisation réelle).

**G. Résultat attendu.** Le texte avec marqueurs, un tableau des catégories remplacées, une alerte sur les passages à risque.

**H. Exemple d'application (illustratif).** Un rapport de visite mentionne « la grand-mère de 87 ans qui vit seule près de l'ancienne école de [village], dont le fils est le seul pharmacien du canton ». L'outil remplace les éléments et signale que la combinaison « seul pharmacien du canton » reste identifiante ; la phrase est réécrite manuellement : « une personne âgée vivant seule, dont un proche réside dans la commune ».

**I. Méthode de vérification.** Relecture humaine intégrale ; recherche dans le texte final des noms connus (Ctrl+F) ; test « un voisin reconnaîtrait-il la personne ? ».

**J. Précautions.** L'anonymisation automatique n'est jamais parfaite. Pour des données particulièrement sensibles (violences, santé, statut migratoire), privilégiez une anonymisation manuelle par une personne formée, ou n'utilisez pas d'outil externe.

**K. Amélioration.** Si des identifiants indirects subsistent : « Applique une généralisation plus forte : remplace les âges par des tranches de 20 ans et les lieux par la région. »

### Fiche P8.2 — Revue de biais d'un contenu ou d'un outil

**A. Titre.** Revue de biais et d'inclusion.

**B. Objectif.** Repérer stéréotypes, exclusions et traitements inéquitables dans un contenu (texte, campagne) ou dans les règles d'un outil (grille, formulaire, critères).

**C. Contexte d'utilisation.** Communication, RH, programmes ; avant publication ou mise en service.

**D. Données nécessaires.** Le contenu ou la description des règles ; le public visé.

**E. Prompt complet.**

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

**F. Instructions d'utilisation.** Utilisable avec des contenus verts ou orange. Pour une grille RH, décrivez les critères sans données de candidats.

**G. Résultat attendu.** Une liste argumentée de points, avec gravité et propositions.

**H. Exemple d'application (illustratif).** Une annonce de bénévolat exigeant « permis de conduire et disponibilité en journée » est signalée comme excluant les personnes en emploi et celles sans permis, alors que seules deux missions sur dix l'exigent. L'annonce est scindée par type de mission.

**I. Méthode de vérification.** Soumettre les conclusions à deux ou trois personnes concernées ou à une organisation représentative ; ne pas considérer la revue automatique comme suffisante.

**J. Précautions.** L'outil lui-même peut être biaisé ; il ne remplace pas la consultation des personnes concernées.

**K. Amélioration.** « Réalise la même revue du point de vue d'une personne [PROFIL PRÉCIS], puis compare. »

## 8.8 Résultats attendus

Une politique d'utilisation de l'IA (annexe 10), une classification des données comprise par tous, une liste des outils autorisés, un examen éthique pour chaque nouveau cas d'usage, des décisions réservées identifiées, des personnes formées.

## 8.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** — Toute décision qui affecte les droits, l'accès à un service, l'emploi, la sécurité ou la réputation d'une personne est prise par un humain compétent, qui peut l'expliquer, et contre laquelle un recours est possible. Toute situation de protection (abus, exploitation, danger) est traitée immédiatement par un référent humain, en dehors de tout circuit automatisé.

## 8.10 Risques et erreurs à éviter

- Considérer qu'un outil gratuit « sans inscription » ne pose pas de problème de confidentialité.
- Croire que remplacer les noms suffit à anonymiser.
- Recueillir un consentement de façade dans une relation de dépendance.
- Déduire des données sensibles (santé, orientation, origine) à partir d'autres données.
- Laisser la supervision humaine devenir une formalité.
- Publier des images générées sans le signaler.
- Ignorer les exigences de protection des données des bailleurs.

## 8.11 Exercice pratique

**Consigne (2 heures).** (1) Listez dix types de documents ou de données de votre organisation et attribuez à chacun une couleur du feu tricolore. (2) Choisissez un cas d'usage envisagé et appliquez les neuf étapes de l'examen éthique simplifié. (3) Rédigez la liste des décisions réservées à l'humain pour ce cas. (4) Appliquez la fiche P8.2 à une annonce ou une affiche de votre organisation.

**Éléments de correction.** Les données nominatives de bénéficiaires, de santé, d'enfants, les salaires et les signalements sont en rouge ; les budgets internes et les PV en orange ; les publications en vert. L'examen éthique identifie au moins un risque pour des personnes et une mesure concrète. Les décisions réservées couvrent toute décision affectant une personne.

## 8.12 Synthèse

- Les cadres internationaux (UNESCO, OCDE, NIST, ISO/IEC 42001, Conseil de l'Europe, AI Act) convergent : contrôle proportionné au risque pour les personnes.
- Les biais naissent des données, des critères et des usages ; on les teste et on implique les personnes concernées.
- La protection des données repose sur la finalité, la minimisation, la base légale, la sécurité et la responsabilité ; le feu tricolore la traduit au quotidien.
- La supervision humaine doit être réelle ; certaines décisions ne se délèguent jamais.
- Cybersécurité, droit d'auteur, environnement et protection des personnes vulnérables complètent l'analyse.
- Les obligations juridiques dépendent des pays : identifiez-les et faites-vous conseiller.

## 8.13 QCM — Module 8

**Q1.** (une seule réponse) La Recommandation de l'UNESCO sur l'éthique de l'IA (2021) est :

a) une loi directement applicable aux ASBL dans tous les pays.
b) une norme certifiable.
c) un contrat type.
d) une recommandation adoptée par les États membres, non contraignante pour les organisations.

**Q2.** (une seule réponse) ISO/IEC 42001:2023 est :

a) une loi européenne.
b) une recommandation de l'OCDE.
c) une norme volontaire de système de management de l'IA, certifiable.
d) un logiciel.

**Q3.** (une ou plusieurs réponses) Lesquelles de ces données sont classées « rouge » ?

a) La liste nominative des enfants inscrits.
b) Le rapport annuel publié.
c) Les salaires du personnel.
d) Un signalement d'abus.

**Q4.** (une seule réponse) Le principe de minimisation signifie :

a) ne traiter que les données strictement nécessaires à la finalité.
b) réduire la taille des fichiers.
c) minimiser le nombre d'outils.
d) supprimer toutes les données chaque année.

**Q5.** (une ou plusieurs réponses) Un consentement valable doit être :

a) libre.
b) spécifique.
c) éclairé.
d) irrévocable.

**Q6.** (une seule réponse) Le « biais d'automatisation » désigne :

a) une erreur de programmation.
b) un biais dans les données d'entraînement.
c) la tendance des humains à faire excessivement confiance aux résultats d'une machine.
d) la lenteur des automatisations.

**Q7.** (mise en situation — une seule réponse) Un message vocal imitant la voix du directeur demande au comptable un virement urgent. Que faire ?

a) Exécuter, la voix est reconnaissable.
b) Vérifier par un second canal convenu avant tout paiement inhabituel.
c) Demander à un assistant d'IA si la voix est authentique.
d) Exécuter puis prévenir le directeur.

**Q8.** (mise en situation — une seule réponse) Un partenaire propose un outil qui attribue un « score de vulnérabilité » à chaque ménage pour décider automatiquement de l'attribution de l'aide. Votre position ?

a) Refuser toute décision automatique ; l'outil peut au mieux éclairer une décision humaine motivée, après examen des biais, de la base légale et avec un recours.
b) Accepter, c'est plus objectif.
c) Accepter si le score est expliqué en anglais.
d) Accepter pour les ménages qui ne protestent pas.

**Q9.** (une seule réponse) Une image générée par IA montrant des enfants souffrants pour une campagne de dons :

a) est acceptable si elle est réaliste.
b) est acceptable si l'outil est payant.
c) est obligatoire pour protéger les vrais enfants.
d) pose des problèmes de dignité et de tromperie et est à proscrire.

**Q10.** (une ou plusieurs réponses) Avant d'utiliser un outil en ligne avec des données internes, il faut vérifier :

a) si les données saisies servent à entraîner les modèles.
b) la localisation des traitements.
c) la durée de conservation des conversations.
d) le nombre d'abonnés de l'outil sur les réseaux sociaux.

## 8.14 Corrigé détaillé — Module 8

**Q1 : d.** C'est un instrument normatif adopté par les États, qui n'impose pas directement d'obligations juridiques aux organisations.

**Q2 : c.** Norme volontaire et certifiable de système de management.

**Q3 : a, c, d.** Le rapport annuel publié est vert.

**Q4 : a.** Ne traiter que ce qui est nécessaire.

**Q5 : a, b, c.** Le consentement doit au contraire pouvoir être retiré (d).

**Q6 : c.** Il rend la supervision humaine illusoire si elle n'est pas organisée.

**Q7 : b.** Les imitations de voix sont devenues accessibles ; seule une procédure de vérification indépendante protège. Un outil d'IA (c) n'offre pas de garantie fiable.

**Q8 : a.** L'attribution d'une aide est une décision sur des personnes vulnérables : elle reste humaine, motivée et contestable.

**Q9 : d.** Elle porte atteinte à la dignité et trompe les donateurs.

**Q10 : a, b, c.** La popularité (d) n'est pas un critère de sécurité.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Agence internationale de l'énergie (AIE/IEA). (2025). *Energy and AI*.
- Conseil de l'Europe. (2018). *Protocole d'amendement à la Convention 108* (STCE n° 223).
- Conseil de l'Europe. (2024). *Convention-cadre sur l'intelligence artificielle et les droits de l'homme, la démocratie et l'État de droit* (STCE n° 225).
- ISO/IEC. (2023). *ISO/IEC 42001:2023 — Artificial intelligence — Management system*.
- Marelli, M. (dir.). (2024). *Handbook on Data Protection in Humanitarian Action* (3e éd.). Cambridge University Press / CICR. https://doi.org/10.1017/9781009414630
- NIST. (2023). *AI Risk Management Framework 1.0* (NIST AI 100-1). https://doi.org/10.6028/NIST.AI.100-1
- NIST. (2024). *Generative AI Profile* (NIST AI 600-1). https://doi.org/10.6028/NIST.AI.600-1
- OCDE. (2019, révisée en 2024). *Recommandation du Conseil sur l'intelligence artificielle*.
- OWASP Foundation. (2024). *OWASP Top 10 for LLM Applications* (version 2025).
- Règlement (UE) 2016/679 (RGPD).
- Règlement (UE) 2024/1689 (AI Act), modifié par le règlement (UE) 2026/1744 (référence à confirmer sur EUR-Lex).
- UNESCO. (2021). *Recommandation sur l'éthique de l'intelligence artificielle*.
