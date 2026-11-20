# Module 20 — Gérer le changement et assurer la pérennité des solutions

## 20.1 Mise en situation

Six mois après le déploiement de l'assistant de procédures, Horizons Partagés fait le point. Au siège, l'outil est utilisé quotidiennement. Dans deux bureaux de terrain, presque personne ne l'utilise : « on n'a pas eu le temps », « je préfère appeler Ibrahim », « une fois il s'est trompé ». Le référent numérique qui avait paramétré l'outil a quitté l'organisation ; personne n'a mis à jour la base depuis la révision de la politique de voyage ; l'abonnement a augmenté. La solution est en train de mourir doucement — un scénario fréquent.

## 20.2 Problématique

Une solution d'IA n'est pas un achat ponctuel : c'est un **changement de pratiques** qu'il faut accompagner, et un **dispositif vivant** qu'il faut gouverner, maintenir, évaluer et faire évoluer. Les causes d'échec sont rarement techniques : elles tiennent à l'adoption, à la gouvernance et aux ressources.

## 20.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. comprendre les ressorts de la résistance et de l'adoption ;
2. concevoir un plan de formation et d'accompagnement ;
3. mettre en place une gouvernance de l'IA proportionnée ;
4. organiser la maintenance, l'évaluation et l'audit des systèmes ;
5. suivre les coûts récurrents ;
6. piloter l'amélioration continue.

## 20.4 Notions et définitions

- **Conduite du changement** : ensemble des actions qui aident les personnes à passer d'une pratique à une autre.
- **Adoption** : usage effectif, régulier et approprié d'un outil par les personnes visées.
- **Gouvernance de l'IA** : rôles, règles et processus par lesquels l'organisation décide, encadre, surveille et évalue ses usages de l'IA.
- **Dérive** : dégradation progressive des performances d'un système (documents obsolètes, changements des données, nouvelles versions de modèles).
- **Audit d'un système d'IA** : examen indépendant de la conformité, de l'efficacité et des risques d'un système.

## 20.5 Explications détaillées

### Comprendre la résistance

La résistance au changement a souvent des causes légitimes : peur de perdre son emploi ou sa compétence, crainte d'être surveillé, mauvaise expérience avec l'outil, surcharge de travail, absence de sens. La traiter suppose d'écouter, d'expliquer, d'associer — et parfois d'adapter le projet.

![Figure 20.2 — Facteurs d'adoption d'un nouvel outil](03_ILLUSTRATIONS/figures/fig_20_2.svg)

Les modèles d'acceptation de la technologie, largement étudiés en sciences de gestion, mettent en avant quelques déterminants : l'**utilité perçue** et la **facilité d'utilisation perçue** (Davis, 1989), auxquelles le modèle UTAUT ajoute l'**influence sociale** et les **conditions facilitantes** (Venkatesh et al., 2003). Traduction pratique :

| Déterminant | Question que se pose la personne | Actions |
|---|---|---|
| Utilité perçue | « Est-ce que cela m'aide vraiment ? » | Démontrer sur ses propres tâches ; partager des exemples concrets de collègues |
| Facilité perçue | « Est-ce simple pour moi ? » | Modèles prêts à l'emploi ; formation courte et pratique ; aide disponible |
| Influence sociale | « Les autres l'utilisent-ils ? » | Ambassadeurs dans chaque équipe ; exemple de la direction |
| Conditions facilitantes | « Ai-je le matériel, le temps, le droit ? » | Équipement ; temps dédié ; règles claires sur ce qui est permis |

### Gestion des équipes

- **Expliquer le pourquoi** : quel problème, quel bénéfice pour les équipes et pour la mission, et ce que l'organisation fera du temps gagné.
- **Rassurer sur l'emploi et la surveillance** : dire clairement si l'outil sera utilisé pour évaluer les personnes (il ne devrait pas l'être sans cadre explicite).
- **Associer** : utilisateurs testeurs, ambassadeurs, retours réguliers.
- **Reconnaître** les efforts et les réussites.
- **Accepter** les ajustements, y compris l'abandon d'un outil qui ne sert pas.

### Formation

Une formation efficace est **courte, pratique, liée aux tâches réelles, progressive et répétée**. Un plan de formation (annexe 16, fiche P20.1) comprend :

1. **un socle commun** pour tous (2 à 3 heures) : ce qu'est l'IA, ses limites, la politique de l'organisation, le feu tricolore, la vérification ;
2. **des modules métier** (1 à 2 heures) : les fiches prompts et solutions du métier ;
3. **une formation spécifique** pour chaque outil déployé ;
4. **une formation des référents** (plus approfondie) ;
5. **des rappels** : astuces mensuelles, partage de cas, mise à jour lors des changements.

Les petites habitudes répétées comptent davantage que les grandes formations ponctuelles : une « minute IA » en réunion d'équipe, une bibliothèque de prompts enrichie chaque mois, un canal d'entraide.

### Gouvernance de l'IA

![Figure 20.1 — Gouvernance de l'IA dans l'ASBL](03_ILLUSTRATIONS/figures/fig_20_1.svg)

Une gouvernance proportionnée à la taille de l'organisation comprend :

- **une politique d'utilisation de l'IA** adoptée par le conseil (annexe 10) ;
- **une personne référente** (ou un comité dans les grandes organisations) chargée du registre des outils, de la validation des nouveaux usages, des incidents et de la formation ;
- **des registres** : outils (annexe 9), risques (annexe 8), incidents ;
- **un circuit de validation** des nouveaux cas d'usage (examen éthique du module 8) ;
- **un bilan annuel** au conseil.

Les cadres de référence offrent des repères pour structurer cette gouvernance : la fonction « Gouverner » du NIST AI RMF, ou les exigences de système de management d'ISO/IEC 42001:2023 pour les organisations qui souhaitent aller plus loin, voire viser une certification.

### Maintenance

Chaque solution a un **responsable désigné** et un **suppléant**, et une **fiche de maintenance** : mises à jour de la base documentaire ; relance du jeu de tests après chaque mise à jour (de la base, des consignes ou du modèle utilisé par le fournisseur) ; revue des droits d'accès ; vérification des automatisations ; suivi des changements de conditions du fournisseur.

### Évaluation et performance

Les indicateurs définis dans le cahier des charges sont suivis dans le temps. On évalue aussi :

- **l'adoption** : nombre d'utilisateurs actifs, fréquence, par équipe ;
- **la qualité** : échantillons vérifiés, incidents, signalements ;
- **les effets** : temps, délais, erreurs, satisfaction ;
- **les effets non prévus** : nouvelles erreurs, perte de compétences, charge de vérification.

### Audit des systèmes

Une fois par an (ou à chaque changement important), un audit — interne ou externe — examine : conformité à la politique et aux lois ; exactitude des registres ; efficacité des contrôles humains (sont-ils réellement exercés ?) ; résultats des tests ; sécurité et droits d'accès ; gestion des incidents ; coûts et bénéfices.

### Coûts récurrents

Les coûts d'une solution évoluent : nombre d'utilisateurs, volumes, hausses tarifaires, nouvelles fonctions payantes, temps de maintenance. Un suivi trimestriel compare les coûts réels au budget et à la valeur produite ; il éclaire les décisions de renouvellement, d'extension ou d'arrêt.

### Amélioration continue

Le cycle **planifier — faire — vérifier — agir** s'applique : analyser les incidents et les signalements ; exploiter les questions sans réponse ; mettre à jour la base et les consignes ; enrichir les jeux de tests ; partager les bonnes pratiques ; décider chaque année de poursuivre, d'étendre, de modifier ou d'arrêter.

## 20.6 Application : relancer l'assistant de procédures

| Problème constaté | Cause | Action | Responsable | Échéance |
|---|---|---|---|---|
| Faible usage dans deux bureaux | Pas de formation sur place ; pas d'ambassadeur | Session pratique de 1 h 30 par bureau ; désignation d'un ambassadeur | Référente IA | 6 semaines |
| Méfiance après une erreur | Erreur non expliquée | Communication sur l'erreur, sa cause et la correction ; rappel de la vérification | Responsable financier | 2 semaines |
| Base non mise à jour | Départ du référent ; pas de suppléant | Désignation d'une référente et d'un suppléant ; procédure de mise à jour liée au circuit de validation des procédures | Direction | Immédiat |
| Coût en hausse | Licences inutilisées | Revue des licences ; suppression des comptes inactifs | Référente IA + finances | 1 mois |
| Pas d'évaluation | Indicateurs non suivis | Tableau de bord trimestriel ; bilan au comité de direction | Référente IA | Trimestriel |

### Solutions selon le niveau

| Niveau | Gouvernance | Formation | Maintenance et évaluation |
|---|---|---|---|
| Débutant | Politique d'une page, référent à temps partiel, liste des outils autorisés | Socle de 2 h, astuces mensuelles | Revue semestrielle des usages et des outils |
| Intermédiaire | Référent désigné, registres, circuit de validation, bilan annuel au CA | Socle + modules métier + ambassadeurs | Tableau de bord trimestriel, jeux de tests |
| Avancé | Comité IA, système de management inspiré d'ISO/IEC 42001, audits réguliers | Parcours par rôle, certification interne | Surveillance continue, journalisation, audit annuel |

## 20.7 Prompt prêt à l'emploi

### Fiche P20.1 — Construire un plan de formation

**A. Titre.** Plan de formation à l'usage responsable de l'IA.

**B. Objectif.** Obtenir un plan de formation par rôle, progressif et réaliste.

**C. Contexte d'utilisation.** Avant un déploiement ; lors de l'adoption d'une politique d'IA.

**D. Données nécessaires.** Rôles et effectifs ; niveau de départ (questionnaire) ; outils autorisés ; politique d'IA ; contraintes (temps, connectivité, langues).

**E. Prompt complet.**

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

**F. Instructions d'utilisation.** Ajustez selon les disponibilités ; validez avec la RH et la direction.

**G. Résultat attendu.** Un plan par rôle, un calendrier, un dispositif de soutien, des indicateurs.

**H. Exemple d'application (illustratif).** Pour Lumière des Collines (6 salariés, 30 bénévoles, connexion intermittente), le plan propose un socle de 2 heures en présentiel avec supports imprimés, des fiches prompts plastifiées près de l'ordinateur partagé, et une séance mensuelle de 30 minutes lors de la réunion des bénévoles.

**I. Méthode de vérification.** Cohérence avec la politique et les outils ; réalisme du temps demandé ; présence d'exercices réels.

**J. Précautions.** Données agrégées uniquement.

**K. Amélioration.** « Ajoute un module spécifique pour les administrateurs (1 h) centré sur la gouvernance et les risques. »

## 20.8 Résultats attendus

Des équipes formées et outillées ; une adoption mesurée et soutenue ; une gouvernance active ; des solutions maintenues, évaluées et auditées ; des coûts maîtrisés.

## 20.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** — Le conseil adopte la politique et reçoit le bilan annuel ; la direction décide de poursuivre, d'étendre ou d'arrêter chaque solution ; le référent IA valide les nouveaux usages ; l'audit est réalisé par une personne indépendante de la gestion de la solution.

## 20.10 Risques et erreurs à éviter

- Considérer le déploiement comme la fin du projet.
- Former une seule fois.
- Laisser une solution sans responsable ni suppléant.
- Ignorer les signaux faibles (non-usage, contournements).
- Utiliser l'outil pour surveiller les personnes sans cadre explicite.
- Ne pas suivre les coûts récurrents.

## 20.11 Exercice pratique

**Consigne (2 heures).** (1) Identifiez trois sources possibles de résistance dans votre organisation et une action pour chacune. (2) Appliquez P20.1. (3) Rédigez la fiche de maintenance d'une solution (responsable, suppléant, tâches, fréquence, indicateurs). (4) Proposez cinq indicateurs pour le bilan annuel au conseil.

**Éléments de correction.** Les résistances sont traitées comme légitimes ; le plan comprend des exercices réels ; la fiche de maintenance désigne un suppléant et prévoit la relance des tests ; les indicateurs couvrent adoption, qualité, effets et coûts.

## 20.12 Synthèse

- L'adoption dépend de l'utilité perçue, de la facilité, de l'influence sociale et des conditions facilitantes.
- La formation est courte, pratique, répétée.
- La gouvernance de l'IA est proportionnée : politique, référent, registres, bilan.
- Maintenance, évaluation, audit et suivi des coûts font vivre la solution.
- L'amélioration continue inclut la possibilité d'arrêter.

## 20.13 QCM — Module 20

**Q1.** (une seule réponse) Selon le modèle de Davis (1989), deux déterminants majeurs de l'acceptation d'une technologie sont :

a) le prix et la marque.
b) l'utilité perçue et la facilité d'utilisation perçue.
c) la couleur et la vitesse.
d) l'âge et le sexe.

**Q2.** (une ou plusieurs réponses) Le modèle UTAUT ajoute notamment :

a) l'influence sociale.
b) les conditions facilitantes.
c) le cours de l'action du fournisseur.
d) la taille de l'écran.

**Q3.** (une seule réponse) Une formation efficace à l'IA est :

a) longue et théorique, une seule fois.
b) courte, pratique, liée aux tâches réelles et répétée.
c) réservée à la direction.
d) remplacée par la documentation du fournisseur.

**Q4.** (une ou plusieurs réponses) Une gouvernance proportionnée de l'IA comprend :

a) une politique adoptée par le conseil.
b) une personne référente.
c) des registres des outils et des risques.
d) l'interdiction de tout nouvel usage.

**Q5.** (une seule réponse) La « dérive » d'un système désigne :

a) une panne de serveur.
b) une dégradation progressive des performances (documents obsolètes, nouvelles versions de modèles…).
c) une hausse de prix.
d) un changement d'interface.

**Q6.** (une seule réponse) Après une mise à jour du modèle par le fournisseur, il faut :

a) ne rien faire.
b) relancer le jeu de tests.
c) changer de fournisseur.
d) supprimer la base documentaire.

**Q7.** (mise en situation — une seule réponse) Le référent qui a paramétré l'outil quitte l'organisation sans suppléant. Le risque principal est :

a) une hausse de l'adoption.
b) l'abandon progressif de la maintenance et la dégradation de la solution.
c) une baisse des coûts.
d) aucun.

**Q8.** (mise en situation — une seule réponse) Des agents disent préférer appeler le responsable financier « car l'outil s'est trompé une fois ». Que faites-vous ?

a) Rendre l'outil obligatoire.
b) Expliquer l'erreur et sa correction, rappeler la vérification, montrer des exemples réussis.
c) Interdire les appels.
d) Supprimer l'outil.

**Q9.** (une seule réponse) L'audit d'un système d'IA doit être réalisé par :

a) la personne qui gère la solution.
b) une personne indépendante de la gestion de la solution.
c) le fournisseur.
d) l'outil lui-même.

**Q10.** (une ou plusieurs réponses) Indicateurs pertinents pour le bilan annuel :

a) utilisateurs actifs par équipe.
b) incidents et signalements.
c) coûts réels comparés au budget et à la valeur.
d) nombre de messages promotionnels du fournisseur.

## 20.14 Corrigé détaillé — Module 20

**Q1 : b.** Ce sont les deux construits fondateurs du modèle d'acceptation de la technologie.

**Q2 : a, b.** Avec la performance attendue et l'effort attendu.

**Q3 : b.** La répétition et la pratique fondent les habitudes.

**Q4 : a, b, c.** L'interdiction générale (d) n'est pas une gouvernance.

**Q5 : b.** D'où la nécessité de tests réguliers.

**Q6 : b.** Une nouvelle version peut changer les comportements.

**Q7 : b.** Responsable et suppléant sont indispensables.

**Q8 : b.** La confiance se reconstruit par la transparence et la démonstration.

**Q9 : b.** L'indépendance garantit l'objectivité.

**Q10 : a, b, c.** Le critère d est sans rapport avec la valeur.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.

## Références du module

- Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly, 13*(3), 319–340. https://doi.org/10.2307/249008
- ISO/IEC. (2023). *ISO/IEC 42001:2023*.
- NIST. (2023). *AI Risk Management Framework 1.0*.
- Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. *MIS Quarterly, 27*(3), 425–478. https://doi.org/10.2307/30036540
