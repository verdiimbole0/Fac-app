# Partie VI — Laboratoire pratique et transformation durable {.partie}

*Place à l'entraînement. Le module 21 propose dix études de cas complètes, chacune reliant un problème réel à une méthode, à une solution adaptée aux moyens de l'organisation, et aux contrôles nécessaires. Le module 22 vous accompagne dans la construction de votre propre plan de transformation.*

# Module 21 — Études de cas et résolution de problèmes concrets

## 21.1 Mise en situation

Vous avez parcouru vingt modules. Il est temps de vérifier que vous savez mobiliser ces connaissances face à des situations complètes, où les problèmes s'entremêlent : un retard de reporting cache un problème de classement, qui cache un problème de gouvernance ; une idée d'IA séduisante cache un risque pour les personnes.

## 21.2 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. analyser une situation complexe en distinguant symptômes, causes et priorités ;
2. choisir entre solution organisationnelle, automatisation classique et IA ;
3. proposer une solution adaptée au niveau de maturité et aux moyens ;
4. définir les contrôles humains, les risques et les indicateurs ;
5. argumenter vos choix.

## 21.3 Mode d'emploi

![Figure 21.1 — Les dix études de cas et leurs modules de référence](03_ILLUSTRATIONS/figures/fig_21_1.svg)

Pour chaque cas : lisez la situation ; répondez aux questions **avant** de lire l'analyse proposée ; comparez. Les analyses ne sont pas les seules réponses possibles : ce qui compte est la qualité du raisonnement. Les organisations et données sont fictives.

## Cas 1 — Comptabilité désorganisée

**Situation.** Une association culturelle (8 salariés, budget 400 000 UM) n'a pas clôturé ses comptes depuis 14 mois. Les pièces sont dans des boîtes, des courriels et des téléphones. La comptable bénévole est partie. Le trésorier veut « un logiciel avec de l'IA qui remettra tout en ordre ».

**Questions.** (1) Quelle est la première priorité ? (2) L'IA peut-elle « remettre tout en ordre » ? (3) Quelle séquence proposez-vous ?

**Analyse proposée.**

- *Symptômes* : comptes non clôturés, pièces dispersées. *Causes profondes* : absence de procédure, dépendance à une bénévole, aucun classement.
- *Priorité* : reconstituer et sécuriser l'information (pièces, relevés bancaires), puis rattraper la comptabilité, avant toute automatisation.
- *Rôle de l'IA* : utile pour **accélérer** l'extraction des données de centaines de pièces numérisées et proposer des imputations — à condition qu'une personne compétente vérifie. Elle ne peut pas reconstituer des pièces manquantes ni décider des régularisations.
- *Séquence* : (1) rassembler toutes les pièces, les numériser et les classer par mois (règle de nommage, module 7) ; (2) récupérer tous les relevés bancaires ; (3) engager un professionnel pour le rattrapage (expert-comptable ou comptable expérimenté, selon les exigences locales) ; (4) utiliser l'extraction assistée (fiche P12.1) pour accélérer la saisie, avec vérification de 100 % des montants ; (5) rapprochements bancaires mensuels sur toute la période ; (6) liste des pièces manquantes et demandes de duplicatas ; (7) procédure de traitement des pièces pour l'avenir ; (8) choix d'un logiciel adapté (niveau Débutant ou Intermédiaire).
- *Contrôles humains* : validation des écritures, des régularisations et des comptes par une personne compétente ; arrêté des comptes par l'organe compétent.
- *Indicateurs* : mois rapprochés ; pièces manquantes ; date de clôture.

## Cas 2 — Retards de reporting financier

**Situation.** Une ONG de 40 salariés envoie systématiquement ses rapports financiers trimestriels avec 20 à 30 jours de retard à ses quatre bailleurs, qui exigent chacun un format différent. Les rapports sont construits par ressaisie dans des tableurs.

**Questions.** (1) Quelles causes rechercher ? (2) Quelle solution structurelle ? (3) Où l'IA intervient-elle ?

**Analyse proposée.**

- *Causes à rechercher* (module 5) : clôture mensuelle tardive ; codes analytiques incomplets ; absence de table de correspondance entre lignes des bailleurs et comptes ; ressaisie ; validation tardive.
- *Solution structurelle* : calendrier de clôture (J+10) ; plan analytique complet (projet, bailleur, ligne) ; **tables de correspondance par bailleur** ; modèles de rapports alimentés par extraction de la comptabilité (tableau croisé ou fonction de reporting du logiciel).
- *IA* : rédaction de la note narrative d'analyse des écarts (fiche P12.3) à partir de chiffres validés ; vérification de cohérence entre rapport narratif et rapport financier. Pas de calcul par un modèle de langage.
- *Niveau* : Intermédiaire.
- *Contrôles* : revue du rapport par le responsable financier ; réconciliation rapport/comptabilité.
- *Indicateurs* : délai de remise ; nombre de corrections demandées par les bailleurs.

## Cas 3 — Risques de détournement

**Situation.** Dans une ONG, un bailleur signale que deux fournisseurs d'un bureau régional partagent la même adresse et le même numéro de téléphone. Le bureau régional effectue de nombreux achats juste sous le seuil de mise en concurrence.

**Questions.** (1) Quels tests analytiques ? (2) Comment conduire l'investigation ? (3) Quelles mesures préventives ?

**Analyse proposée.**

- *Tests* (module 13) : fournisseurs aux coordonnées communes (adresse, téléphone, compte bancaire) ; lien entre coordonnées fournisseurs et coordonnées du personnel ; fractionnement ; montants juste sous le seuil ; concentration des achats ; auto-approbation.
- *Investigation* : application de la politique de lutte contre la fraude ; information confidentielle de la direction et du président du comité d'audit ; préservation des preuves ; pas d'entretien prématuré avec les personnes concernées ; recours éventuel à un spécialiste ; respect du droit du travail et des droits des personnes.
- *Rôle de l'IA* : rapprochement de noms et d'adresses proches ; synthèse des résultats ; rédaction de la feuille de travail. Aucune conclusion automatique.
- *Prévention* : contrôle des données fournisseurs à la création et à la modification (second canal pour les RIB) ; alertes de fractionnement ; rotation et séparation des tâches ; canal de signalement confidentiel (dans l'étude ACFE 2024, le signalement était le premier mode de détection des fraudes internes de l'échantillon).
- *Indicateurs* : alertes traitées ; délais ; recommandations mises en œuvre.

## Cas 4 — Dépendance financière

**Situation.** Lumière des Collines dépend à 70 % d'un bailleur dont la convention expire dans 18 mois.

**Questions.** (1) Quelle stratégie ? (2) Quels usages de l'IA sont pertinents ? (3) Quels indicateurs ?

**Analyse proposée.**

- *Stratégie* (module 15) : objectif de diversification (par exemple : aucun bailleur au-delà de 50 % dans 3 ans ; 15 % de ressources non affectées) ; cartographie des sources ; dossier de matière première ; veille ; relation avec le bailleur actuel pour préparer le renouvellement.
- *IA (niveau Débutant)* : résumés d'appels et checklists d'éligibilité (P15.1) ; mise en forme des notes conceptuelles (P15.2) ; déclinaisons de communication pour une campagne de dons (module 17).
- *Points de vigilance* : ne pas multiplier les dossiers génériques ; go/no-go systématique ; respect des règles des bailleurs sur l'IA.
- *Indicateurs* : part du premier bailleur ; nombre de sources ; taux de succès ; ressources non affectées.

## Cas 5 — Perte de documents

**Situation.** Lors d'un audit, une fondation ne retrouve pas 15 % des pièces sélectionnées. Les documents sont répartis entre ordinateurs personnels, messageries et classeurs.

**Questions.** (1) Mesures immédiates ? (2) Organisation durable ? (3) Place de l'IA ?

**Analyse proposée.**

- *Immédiat* : recherche ciblée (messageries, ordinateurs), demande de duplicatas aux fournisseurs, note explicative à l'auditeur.
- *Durable* (module 7) : plan de classement par fonction ; règle de nommage ; canal unique de réception des factures ; lien pièce-écriture dans le logiciel ; sauvegarde 3-2-1 ; interdiction des dossiers personnels pour les documents de l'organisation.
- *IA* : indexation et classification automatique des documents numérisés (types, dates, montants) avec vérification ; à terme, recherche par le sens (assistant documentaire). L'IA ne retrouve que ce qui a été conservé.
- *Indicateurs* : taux de pièces retrouvées en moins de cinq minutes ; pièces non liées aux écritures.

## Cas 6 — Mauvais suivi de projets

**Situation.** Un réseau associatif gère 12 projets ; aucun tableau de bord commun ; les indicateurs sont définis différemment d'un projet à l'autre ; les rapports arrivent en retard et se contredisent.

**Questions.** (1) Quelles fondations ? (2) Quelle solution par niveau ? (3) Quels contrôles ?

**Analyse proposée.**

- *Fondations* (module 11) : référentiel commun d'indicateurs (définitions, méthodes de calcul, désagrégations) ; plan de S&E par projet ; calendrier de collecte.
- *Solutions* : Débutant — tableur commun avec onglets par projet et tableau de synthèse ; Intermédiaire — formulaires mobiles hors ligne reliés à une base et tableau de bord ; Avancé — système d'information de S&E intégré, rapports générés à partir des données.
- *IA* : contrôles de cohérence, synthèse des données qualitatives, rédaction des rapports d'avancement (P11.3) avec traçabilité des chiffres.
- *Contrôles* : validation mensuelle des données par les chargés de S&E ; pointage des chiffres des rapports.
- *Indicateurs* : complétude des données ; ponctualité des rapports ; nombre de contradictions détectées.

## Cas 7 — Gestion insuffisante des bénévoles

**Situation.** La Maison des Aînés Solidaires compte 80 bénévoles ; un tiers part chaque année ; les plannings sont faits à la main ; certains bénévoles se sentent peu reconnus ; des visites sont oubliées.

**Questions.** (1) Quelles causes ? (2) Quelles solutions ? (3) Quelles données protéger ?

**Analyse proposée.**

- *Causes* : accueil et formation insuffisants ; planification manuelle ; manque de reconnaissance ; absence de suivi des visites.
- *Solutions* (module 14) : parcours d'accueil (guide, binôme) ; outil de planification avec application mobile (niveau Intermédiaire) ou tableur partagé (niveau Débutant) ; proposition de planning assistée sur données pseudonymisées (P14.3) ; confirmations automatiques ; messages de reconnaissance ; entretien de départ.
- *Données à protéger* : informations sur la santé et la dépendance des personnes âgées (rouge) ; adresses ; coordonnées des bénévoles.
- *Contrôles* : validation humaine du planning ; suivi des visites non réalisées.
- *Indicateurs* : taux de visites réalisées ; taux de rétention des bénévoles ; satisfaction.

## Cas 8 — Absence de suivi des bénéficiaires

**Situation.** Une ONG de soutien scolaire ne sait pas combien d'enfants elle a réellement accompagnés l'an dernier, ni combien ont progressé. Les listes sont tenues sur papier par chaque animateur.

**Questions.** (1) Quelles données minimales collecter ? (2) Comment protéger les enfants ? (3) L'IA prédictive du décrochage est-elle une bonne idée ?

**Analyse proposée.**

- *Données minimales* (modules 7 et 18) : identifiant non signifiant, classe, groupe, présence, résultats d'évaluations définies, consentement des parents ; pas de données non nécessaires.
- *Protection* : accès restreint ; table de correspondance séparée ; consentement parental ; aucune donnée nominative dans des outils non validés ; conservation limitée.
- *IA prédictive* : à ce stade, **non**. Les données historiques n'existent pas ; les risques de stigmatisation des enfants sont réels ; une règle simple (« trois absences consécutives → appel aux parents ») répond au besoin. L'IA peut aider à construire le modèle de tableur et à analyser des données agrégées.
- *Indicateurs* : nombre d'enfants suivis ; assiduité ; progression selon les évaluations définies.

## Cas 9 — Administration manuelle

**Situation.** Dans une fondation de 25 salariés, les demandes de congé, les notes de frais, les réservations de salles et de véhicules se font par courriel et sur papier ; l'assistante administrative passe la moitié de son temps à relancer et à recopier.

**Questions.** (1) IA ou automatisation classique ? (2) Quel enchaînement ? (3) Quels risques ?

**Analyse proposée.**

- *Diagnostic* : processus à règles stables (circuits de validation connus) → **automatisation classique** d'abord (formulaires, workflows, calendriers partagés, rappels).
- *Enchaînement* (module 9) : formulaires numériques → workflow de validation → notifications → enregistrement dans un tableau ou un logiciel → archivage. L'IA intervient ponctuellement : extraction des justificatifs de notes de frais (P12.1), réponses aux questions sur les règles (assistant de procédures, module 19).
- *Risques* : automatisations non documentées ; dépendance à une personne ; données personnelles (congés maladie) à protéger ; double saisie si les outils ne sont pas reliés.
- *Indicateurs* : délai de traitement ; temps administratif libéré ; satisfaction des salariés.

## Cas 10 — Déployer une politique d'utilisation responsable de l'IA

**Situation.** Un sondage interne d'Horizons Partagés montre que 60 % du personnel utilise des assistants d'IA, souvent gratuits, sans règle ; certains y ont collé des listes de patients ou des budgets confidentiels. La direction veut agir sans freiner les usages utiles.

**Questions.** (1) Mesures d'urgence ? (2) Contenu de la politique ? (3) Comment la faire vivre ?

**Analyse proposée.**

- *Urgence* : message clair de la direction (interdiction immédiate de saisir des données rouges dans des outils non validés) ; recensement des usages ; évaluation des incidents passés (quelles données, quels outils) et, si nécessaire, conseil juridique sur les obligations éventuelles de notification selon la loi applicable.
- *Politique* (annexe 10) : objet et champ ; principes ; feu tricolore ; outils autorisés ; décisions réservées à l'humain ; transparence ; propriété intellectuelle ; signalement des incidents ; rôles (référent, direction, CA) ; formation ; sanctions proportionnées ; révision annuelle.
- *Faire vivre* (module 20) : adoption par le CA ; formation de 2 heures pour tous ; affichage du feu tricolore ; outil professionnel validé mis à disposition (pour offrir une alternative sûre) ; registre des outils et des risques ; bilan annuel.
- *Indicateurs* : personnel formé ; incidents signalés ; usages d'outils non validés (enquête anonyme) ; satisfaction.

## 21.4 Synthèse

- Les problèmes visibles cachent souvent des causes organisationnelles.
- L'automatisation classique suffit fréquemment ; l'IA intervient là où le langage, les documents et la variabilité dominent.
- Les données sensibles et les décisions sur les personnes imposent des limites fermes.
- Chaque solution s'accompagne de contrôles humains et d'indicateurs.

## 21.5 Exercice de synthèse

**Consigne (3 heures).** Choisissez le problème le plus pressant de votre organisation et rédigez une étude de cas complète selon le gabarit A→U (introduction de la partie IV), avec au moins une solution sans IA, une solution par niveau, la liste des décisions réservées à l'humain et cinq indicateurs.

**Éléments de correction.** L'étude est convaincante si les causes sont étayées par des faits, si la solution est proportionnée aux moyens, si les risques pour les personnes sont identifiés et si les indicateurs comportent une valeur de départ.

## 21.6 QCM — Module 21

**Q1.** (une seule réponse) Dans le cas 1, la première priorité est :

a) acheter un logiciel avec IA.
b) rassembler, numériser et classer les pièces et les relevés.
c) produire immédiatement les états financiers.
d) recruter un développeur.

**Q2.** (une seule réponse) Dans le cas 2, l'outil structurel clé pour produire les rapports de quatre bailleurs à partir d'une comptabilité est :

a) un assistant conversationnel.
b) la table de correspondance par bailleur.
c) un agent autonome.
d) la ressaisie.

**Q3.** (une ou plusieurs réponses) Dans le cas 3, quels tests sont pertinents ?

a) Fournisseurs aux coordonnées communes.
b) Coordonnées fournisseurs identiques à celles du personnel.
c) Fractionnement sous le seuil.
d) Nombre de pages des factures.

**Q4.** (une seule réponse) Dans le cas 3, face aux indices, l'organisation doit :

a) publier les noms des suspects.
b) appliquer sa politique de lutte contre la fraude, de façon confidentielle, en préservant les preuves.
c) laisser l'IA conclure.
d) ignorer l'alerte du bailleur.

**Q5.** (une seule réponse) Dans le cas 8, l'IA prédictive du décrochage est déconseillée principalement parce que :

a) elle est trop chère.
b) les données historiques manquent et les risques de stigmatisation sont réels, alors qu'une règle simple suffit.
c) elle est interdite partout.
d) les enfants n'utilisent pas d'ordinateur.

**Q6.** (une seule réponse) Dans le cas 9, la première réponse adaptée est :

a) un agent IA autonome.
b) l'automatisation classique (formulaires, workflows, rappels).
c) un modèle prédictif.
d) le statu quo.

**Q7.** (une ou plusieurs réponses) Dans le cas 10, les mesures d'urgence comprennent :

a) un message clair interdisant la saisie de données rouges dans des outils non validés.
b) le recensement des usages.
c) l'évaluation des incidents passés et, si nécessaire, un conseil juridique.
d) l'interdiction définitive de toute IA.

**Q8.** (une seule réponse) Dans le cas 7, quelles données sont classées rouges ?

a) Les horaires de permanence.
b) Les informations sur la santé et la dépendance des personnes âgées.
c) Le guide d'accueil des bénévoles.
d) Le calendrier des formations.

**Q9.** (une seule réponse) Dans le cas 5, l'IA :

a) peut retrouver des documents jamais conservés.
b) peut indexer et classer les documents conservés, sous vérification.
c) remplace le plan de classement.
d) dispense de sauvegarde.

**Q10.** (une ou plusieurs réponses) Points communs aux dix cas :

a) partir du problème et de ses causes.
b) proportionner la solution aux moyens.
c) prévoir des contrôles humains et des indicateurs.
d) commencer systématiquement par l'outil d'IA le plus avancé.

## 21.7 Corrigé détaillé — Module 21

**Q1 : b.** Sans pièces ni relevés, aucune comptabilité fiable n'est possible.

**Q2 : b.** Elle relie les lignes de chaque bailleur aux comptes et codes analytiques.

**Q3 : a, b, c.** Le nombre de pages (d) n'est pas un indicateur de risque.

**Q4 : b.** Confidentialité, préservation des preuves et respect des droits.

**Q5 : b.** Proportionnalité et protection des enfants.

**Q6 : b.** Les règles stables relèvent de l'automatisation classique.

**Q7 : a, b, c.** L'interdiction totale (d) pousserait les usages dans l'ombre.

**Q8 : b.** Données de santé et de dépendance : rouge.

**Q9 : b.** L'IA ne retrouve que ce qui existe.

**Q10 : a, b, c.** La démarche commence par le problème, pas par l'outil (d).

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.
