#!/usr/bin/env python3
"""Génère les 22 annexes opérationnelles (Markdown, DOCX via pandoc, XLSX) et ANNEXES.zip.

Usage : python3 annexes.py  (depuis la racine ASBL_AUGMENTEE)
"""
import os, re, glob, subprocess, zipfile, unicodedata
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "04_ANNEXES")
NAVY, GOLD, LIGHT = "102849", "C7A34F", "EAF0F5"

A = []  # chaque annexe : dict(num, titre, objectif, consignes, sections=[(titre, contenu)], tables=[(nom, entetes, lignes_exemple, nb_vides)])


def annexe(num, titre, objectif, consignes, sections=(), tables=()):
    A.append(dict(num=num, titre=titre, objectif=objectif, consignes=consignes, sections=list(sections), tables=list(tables)))


# ------------------------------------------------------------------ 1
annexe(1, "Questionnaire de diagnostic de maturité numérique",
       "Situer l'organisation sur six dimensions afin de choisir un niveau d'implémentation réaliste (débutant, intermédiaire, avancé).",
       ["Répondez en équipe (direction, finances, programmes, administration), en 45 minutes.",
        "Pour chaque affirmation, notez de 0 (pas du tout) à 5 (entièrement), en vous appuyant sur des faits.",
        "Calculez la moyenne par dimension (formule dans le tableur), puis la moyenne générale.",
        "Lecture : 0–1,9 = niveau Débutant à consolider ; 2–3,4 = Débutant/Intermédiaire ; 3,5–5 = Intermédiaire/Avancé.",
        "Conservez le résultat comme valeur de départ ; refaites le questionnaire tous les 12 mois."],
       tables=[("Questionnaire", ["Dimension", "N°", "Affirmation", "Note (0-5)", "Preuve / commentaire"], [
           ["Gouvernance du numérique", "1.1", "Une personne est responsable du numérique et de l'IA.", "", ""],
           ["Gouvernance du numérique", "1.2", "Le conseil a adopté des règles sur l'usage du numérique et de l'IA.", "", ""],
           ["Gouvernance du numérique", "1.3", "Les projets numériques sont décidés à partir de problèmes identifiés.", "", ""],
           ["Données et documents", "2.1", "Un plan de classement partagé existe et est appliqué.", "", ""],
           ["Données et documents", "2.2", "Les fichiers de référence (bénéficiaires, fournisseurs, projets) sont uniques et à jour.", "", ""],
           ["Données et documents", "2.3", "Les sauvegardes suivent la règle 3-2-1 et la restauration a été testée.", "", ""],
           ["Outils", "3.1", "Les outils de base (messagerie, stockage partagé, tableur) sont communs à tous.", "", ""],
           ["Outils", "3.2", "La comptabilité est tenue sur un logiciel adapté.", "", ""],
           ["Outils", "3.3", "Les données circulent entre outils sans ressaisie importante.", "", ""],
           ["Compétences", "4.1", "Le personnel est formé aux usages de base du numérique.", "", ""],
           ["Compétences", "4.2", "Au moins une personne sait paramétrer des formulaires et des automatisations simples.", "", ""],
           ["Compétences", "4.3", "Le personnel sait vérifier une réponse produite par une IA.", "", ""],
           ["Sécurité et protection des données", "5.1", "Les données sont classées selon leur sensibilité.", "", ""],
           ["Sécurité et protection des données", "5.2", "La double authentification est activée sur les comptes principaux.", "", ""],
           ["Sécurité et protection des données", "5.3", "Les accès sont retirés le jour du départ d'une personne.", "", ""],
           ["Usages de l'IA", "6.1", "Les usages actuels de l'IA sont recensés.", "", ""],
           ["Usages de l'IA", "6.2", "Des outils d'IA validés sont mis à disposition.", "", ""],
           ["Usages de l'IA", "6.3", "Les décisions réservées à l'humain sont définies.", "", ""]], 0)])

# ------------------------------------------------------------------ 2
annexe(2, "Matrice d'identification des problèmes",
       "Recenser les problèmes, distinguer symptômes et causes profondes, et estimer leur impact.",
       ["Une ligne par problème. Remplissez les causes avec la méthode des « 5 pourquoi » (module 5).",
        "Impact et fréquence : de 1 (faible) à 5 (fort). Priorité = impact × fréquence (formule).",
        "Indiquez la nature de la solution pressentie : organisationnelle, outil simple, IA envisageable."],
       tables=[("Problèmes", ["N°", "Processus", "Symptôme observé (fait mesuré)", "Cause profonde", "Source de preuve", "Impact (1-5)", "Fréquence (1-5)", "Priorité", "Nature de la solution pressentie", "Responsable"], [
           ["P1", "Reporting financier", "Rapports remis avec 20 jours de retard (4 trimestres)", "Pas de table de correspondance bailleurs/comptes", "Courriers des bailleurs", 4, 4, "=F2*G2", "Outil simple + organisation", "Responsable financier"]], 12)])

# ------------------------------------------------------------------ 3
annexe(3, "Matrice de sélection des cas d'usage IA",
       "Prioriser les cas d'usage selon des critères pondérés, de façon transparente et calculée.",
       ["Faites valider les poids avant de noter (total = 100 %).",
        "Notez de 1 à 5 en groupe (3 à 5 personnes de fonctions différentes). Pour le coût et le risque, 5 = coût faible / risque faible.",
        "Le score est calculé automatiquement (SOMMEPROD). Consignez toute décision qui s'écarte du classement."],
       tables=[("Matrice", ["Cas d'usage", "Mission (25 %)", "Gain (20 %)", "Données (15 %)", "Faisabilité (15 %)", "Coût inversé (10 %)", "Risque inversé (15 %)", "Score /5", "Décision et motif"], [
           ["Projet de PV et suivi des décisions", 3, 4, 5, 5, 5, 4, "=ROUND(B2*0.25+C2*0.2+D2*0.15+E2*0.15+F2*0.1+G2*0.15,2)", "Pilote (gain rapide)"],
           ["Synthèse des rapports de terrain", 4, 4, 4, 4, 5, 4, "=ROUND(B3*0.25+C3*0.2+D3*0.15+E3*0.15+F3*0.1+G3*0.15,2)", "Pilote"],
           ["Tri automatique des candidatures", 2, 3, 3, 3, 3, 1, "=ROUND(B4*0.25+C4*0.2+D4*0.15+E4*0.15+F4*0.1+G4*0.15,2)", "Écarté : décisions sur des personnes"]], 10)])

# ------------------------------------------------------------------ 4
annexe(4, "Fiche de cadrage d'un projet IA",
       "Décrire un cas d'usage de façon homogène avant décision (porte 1).",
       ["Une fiche par cas d'usage ; deux pages maximum.", "Utilisez la fiche prompt P6.1 pour un premier jet, puis complétez avec des faits."],
       sections=[("Champs de la fiche", """| Rubrique | Contenu |
|---|---|
| Intitulé du cas d'usage | |
| Porteur (fonction) | |
| Problème (gabarit : pour [acteur], dans [processus], le problème est…, ce qui entraîne…) | |
| Valeur de départ mesurée | |
| Résultat attendu et indicateurs (cible, échéance) | |
| Solution sans IA envisagée | |
| Solution avec IA : niveau, rôle de l'IA / du logiciel / de l'humain | |
| Données nécessaires et classification (vert / orange / rouge) | |
| Personnes affectées et impact d'une erreur | |
| Contrôles humains indispensables | |
| Risques principaux et mesures | |
| Coûts sur 3 ans (postes) | |
| Questions à trancher | |
| Décision (go / no-go), date, décideur | |"""),
                 ("Exemple (extrait)", "Problème : pour la secrétaire bénévole du CA, dans le processus de suivi des réunions, les PV sont diffusés en moyenne 30 jours après la réunion et 5 décisions sur 12 n'ont pas de responsable, ce qui entraîne des décisions non exécutées. Résultat attendu : projet de PV diffusé en 7 jours ; 100 % des décisions avec responsable et échéance.")])

# ------------------------------------------------------------------ 5
annexe(5, "Cahier des charges fonctionnel simplifié",
       "Spécifier le besoin, les exigences et les critères d'acceptation, sans imposer de solution technique.",
       ["Rédigez avec les futurs utilisateurs.", "Les critères d'acceptation sont mesurables et fixés avant les tests.", "Fiche prompt associée : P19.1."],
       sections=[("Plan type", """1. Contexte et problème (avec mesures de départ)
2. Objectifs et indicateurs
3. Utilisateurs (rôles, nombre, lieux, connectivité)
4. Périmètre : inclus / exclu
5. Fonctions attendues : indispensables / souhaitables
6. Données et documents concernés ; classification
7. Exigences de sécurité et de confidentialité (comptes nominatifs, droits, localisation, non-utilisation des données pour l'entraînement, journalisation)
8. Exigences d'accessibilité, de langue et de fonctionnement en faible débit
9. Contrôles humains prévus
10. Critères d'acceptation (ex. : ≥ 90 % de réponses correctes et sourcées sur le jeu de tests ; 0 invention ; 100 % de refus corrects hors périmètre)
11. Contraintes : budget, calendrier, compétences
12. Maintenance, responsable, suppléant, réversibilité (export des données)
13. Validation : date, signataires""")])

# ------------------------------------------------------------------ 6
annexe(6, "Modèle de cartographie de processus",
       "Décrire un processus « tel quel » puis « cible », étape par étape, avec les rôles et les contrôles.",
       ["Délimitez le déclencheur et le résultat final.", "Une ligne par étape ; suivez au moins une transaction réelle pour valider.", "Dessinez ensuite les couloirs (un par acteur)."],
       tables=[("Processus", ["N°", "Étape", "Acteur (fonction)", "Outil / document", "Durée ou délai", "Contrôle existant", "Point de blocage", "Rôle IA (cible)", "Rôle logiciel (cible)", "Rôle humain (cible)"], [
           ["1", "Remplir la demande de dépense", "Demandeur", "Fiche papier", "1 jour", "Aucun", "Fiche incomplète", "Néant", "Formulaire avec champs obligatoires", "Saisit et signe"],
           ["2", "Vérifier le budget", "Coordination", "Tableur personnel", "2 jours", "Partiel", "Fichier non partagé", "Néant", "Calcul du disponible", "Examine les dépassements"]], 15)])

# ------------------------------------------------------------------ 7
annexe(7, "Matrice des responsabilités (RACI)",
       "Préciser, pour chaque activité, qui réalise, qui décide, qui est consulté et qui est informé.",
       ["Une seule personne « A » par activité.", "Au moins un « R » par activité.", "Évitez les colonnes surchargées de « R » : signe de surcharge."],
       tables=[("RACI", ["Activité", "Direction", "Référent IA", "Responsable financier", "Chef de projet", "Utilisateurs", "Conseil d'administration"], [
           ["Adoption de la politique d'IA", "R", "C", "C", "I", "C", "A"],
           ["Validation d'un nouvel outil", "A", "R", "C", "C", "I", "I"],
           ["Pilote : assistant de procédures", "A", "R", "C", "R", "C", "I"]], 12)])

# ------------------------------------------------------------------ 8
annexe(8, "Registre des risques IA",
       "Identifier, évaluer et suivre les risques liés aux usages de l'IA.",
       ["Probabilité et impact de 1 à 5 ; score = P × I (formule).", "Réévaluez après mesures (risque résiduel).", "Revue trimestrielle par le référent IA ; synthèse annuelle au conseil."],
       tables=[("Risques", ["N°", "Usage / outil", "Description du risque", "Personnes ou actifs affectés", "Probabilité (1-5)", "Impact (1-5)", "Score", "Mesures", "Responsable", "Probabilité résiduelle", "Impact résiduel", "Score résiduel", "Date de revue"], [
           ["R1", "Assistants grand public", "Saisie de données de bénéficiaires dans un outil non validé", "Bénéficiaires, ASBL", 3, 5, "=E2*F2", "Feu tricolore, formation, outil validé", "Référent IA", 2, 5, "=J2*K2", ""],
           ["R2", "Projet de PV assisté", "Décision mal retranscrite", "Gouvernance", 2, 4, "=E3*F3", "Texte des décisions repris des notes ; relecture", "Secrétaire", 1, 4, "=J3*K3", ""]], 12)])

# ------------------------------------------------------------------ 9
annexe(9, "Registre des outils IA utilisés",
       "Tenir l'inventaire des outils et automatisations, de leurs conditions et des données autorisées.",
       ["Tout nouvel outil est inscrit avant usage, après validation.", "Revue au moins annuelle des conditions d'utilisation."],
       tables=[("Outils", ["Outil (catégorie)", "Usage autorisé", "Données autorisées (vert/orange/rouge)", "Offre (gratuite/pro)", "Données utilisées pour l'entraînement ? (contrat)", "Localisation des traitements", "Responsable", "Utilisateurs", "Date de validation", "Prochaine revue", "Observations"], [
           ["Assistant conversationnel grand public", "Rédaction sur contenus publics", "Vert", "Gratuite", "Possible selon conditions", "Non garantie", "Référent IA", "Tous", "", "", "Aucune donnée interne"],
           ["Suite bureautique pro avec assistant", "Rédaction, synthèse, PV", "Vert, orange", "Pro", "Non (clause contractuelle à vérifier)", "À préciser", "Référent IA", "Personnel", "", "", ""]], 12)])

# ------------------------------------------------------------------ 10
annexe(10, "Politique interne d'utilisation de l'IA",
       "Modèle de politique à adapter et à faire adopter par l'organe compétent.",
       ["Adaptez les passages entre crochets.", "Faites relire par un conseil juridique pour les aspects liés à la loi applicable.", "Version courte : une page (sections 1 à 6) ; version complète : toutes les sections."],
       sections=[("Modèle de politique", """**Politique d'utilisation de l'intelligence artificielle de [NOM DE L'ASBL]**
Adoptée par [ORGANE] le [DATE]. Révision annuelle.

**1. Objet et champ.** La présente politique encadre l'usage des outils d'intelligence artificielle par le personnel, les bénévoles, les administrateurs et les prestataires agissant pour [NOM DE L'ASBL].

**2. Principes.** L'IA est utilisée au service de la mission, dans le respect des droits et de la dignité des personnes, de la confidentialité, de l'équité et de la transparence. L'organisation reste responsable de toute production et de toute décision.

**3. Classification des données.** Avant tout usage, l'utilisateur détermine la couleur des données (vert : public ; orange : interne ; rouge : personnel, sensible ou confidentiel). Les données rouges ne sont jamais saisies dans un outil non validé spécifiquement à cet effet.

**4. Outils autorisés.** Seuls les outils inscrits au registre des outils sont autorisés, pour les usages et les données indiqués. L'usage de comptes professionnels est obligatoire lorsqu'il existe.

**5. Vérification.** Toute production destinée à l'extérieur ou servant de base à une décision est vérifiée et validée par une personne habilitée. Les calculs financiers sont réalisés dans les outils de calcul prévus.

**6. Décisions réservées à l'humain.** Aucune décision relative à l'accès d'une personne à un service, au recrutement, à l'évaluation, à la rémunération, à la sanction, à l'approbation de paiements ou à la protection des personnes n'est prise par un système automatisé.

**7. Transparence.** Les personnes sont informées lorsqu'elles interagissent avec un système automatisé et peuvent joindre un humain. Les contenus générés susceptibles d'être pris pour réels sont signalés. Les exigences des bailleurs relatives à l'IA sont respectées.

**8. Propriété intellectuelle.** Les utilisateurs ne soumettent pas de contenus sur lesquels l'organisation n'a pas de droits et vérifient les conditions d'utilisation des contenus générés.

**9. Sécurité.** Comptes nominatifs, double authentification, moindre privilège, validation humaine des actions irréversibles des agents, vérification par un second canal des demandes inhabituelles de paiement.

**10. Incidents.** Toute erreur significative, fuite ou usage non conforme est signalé sans délai au référent IA, qui tient le registre des incidents.

**11. Rôles.** Le conseil adopte la politique et reçoit un bilan annuel ; la direction arbitre ; le référent IA tient les registres, valide les nouveaux usages, organise la formation ; chaque utilisateur applique la politique.

**12. Formation.** Toute personne utilisant l'IA suit la formation socle.

**13. Non-respect.** Le non-respect de la politique peut entraîner des mesures proportionnées, conformément au règlement intérieur et au droit applicable.

**14. Révision.** La politique est révisée chaque année et à chaque évolution réglementaire importante.""")])

# ------------------------------------------------------------------ 11
annexe(11, "Fiche de classification des données",
       "Classer les données et documents selon le feu tricolore et associer les règles d'usage.",
       ["Listez les types de données et documents de chaque service.", "En cas de doute, choisissez la couleur la plus protectrice."],
       tables=[("Classification", ["Type de donnée / document", "Service", "Contient des données personnelles ?", "Données sensibles ? (santé, enfants, etc.)", "Couleur (vert/orange/rouge)", "Outils autorisés", "Qui y a accès", "Durée de conservation", "Observations"], [
           ["Rapport annuel publié", "Communication", "Non", "Non", "Vert", "Tous outils autorisés", "Public", "Permanente", ""],
           ["Budget interne", "Finances", "Non", "Non", "Orange", "Outils professionnels validés", "Direction, finances", "Selon la loi", ""],
           ["Liste nominative des élèves", "Programmes", "Oui", "Oui (enfants)", "Rouge", "Base interne uniquement", "Coordinatrice", "Fin de l'accompagnement + délai légal", "Pseudonymiser pour toute analyse"]], 15)])

# ------------------------------------------------------------------ 12
annexe(12, "Checklist de protection des données",
       "Vérifier les points essentiels avant tout traitement de données personnelles, notamment avec un outil d'IA.",
       ["Cochez chaque point ; tout « non » doit être traité avant de commencer.", "Pour les traitements à risque élevé, consultez un conseil juridique."],
       sections=[("Checklist", """| N° | Question | Oui / Non | Action si non |
|---|---|---|---|
| 1 | La finalité du traitement est-elle définie et légitime ? | | |
| 2 | Une base légale est-elle identifiée selon la loi applicable ? | | |
| 3 | Seules les données nécessaires sont-elles utilisées (minimisation) ? | | |
| 4 | Les personnes sont-elles informées dans une langue qu'elles comprennent ? | | |
| 5 | Si le consentement est la base, est-il libre, spécifique, éclairé et révocable ? | | |
| 6 | Les données peuvent-elles être anonymisées ou pseudonymisées pour cet usage ? | | |
| 7 | L'outil est-il inscrit au registre et autorisé pour cette couleur de données ? | | |
| 8 | Le contrat exclut-il l'utilisation des données pour l'entraînement ? | | |
| 9 | La localisation des traitements et les transferts sont-ils connus et conformes ? | | |
| 10 | Les accès sont-ils limités aux personnes nécessaires ? | | |
| 11 | La durée de conservation est-elle fixée ? | | |
| 12 | Une décision automatisée affectant des personnes est-elle exclue ? | | |
| 13 | Les personnes vulnérables bénéficient-elles de protections renforcées ? | | |
| 14 | Une procédure d'incident (fuite, perte) existe-t-elle ? | | |
| 15 | Le traitement est-il inscrit au registre des risques ? | | |""")])

# ------------------------------------------------------------------ 13
annexe(13, "Modèle de validation humaine",
       "Tracer qui a vérifié et validé une production ou une proposition issue de l'IA.",
       ["À utiliser pour les productions externes et les propositions servant de base à une décision.", "Conservez la fiche avec le document validé."],
       tables=[("Validations", ["Date", "Document / opération", "Outil utilisé", "Classification des données", "Éléments vérifiés", "Sources de vérification", "Corrections apportées", "Validé par (fonction)", "Décision (validé / rejeté / à revoir)"], [
           ["2026-03-14", "Projet de PV du CA du 18/03", "Suite pro avec assistant", "Orange", "Texte des décisions, votes, quorum", "Notes de séance", "Vote corrigé (7 pour, 1 abst.)", "Secrétaire", "Validé"]], 15)])

# ------------------------------------------------------------------ 14
annexe(14, "Fiche de contrôle des productions IA",
       "Vérifier une sortie d'IA avant usage (boucle « 6 V », module 3).",
       ["Remplissez une fiche pour chaque production importante.", "Le niveau de contrôle est proportionné à l'enjeu."],
       sections=[("Grille de contrôle", """| Point de contrôle | Conforme | Commentaire |
|---|---|---|
| La consigne respectait la méthode CADRE | | |
| Les données fournies étaient autorisées (couleur) | | |
| La réponse a été lue en entier | | |
| Chaque chiffre a été vérifié sur la source | | |
| Chaque nom, date, référence a été vérifié | | |
| Les citations existent mot pour mot dans la source | | |
| Aucune affirmation non fondée (impact, statistique) | | |
| Absence de biais ou de formulation dévalorisante | | |
| Ton et format adaptés au public | | |
| Accessibilité (texte alternatif, langage clair) si diffusion | | |
| Validation par la personne habilitée | | |""")])

# ------------------------------------------------------------------ 15
annexe(15, "Modèle de tableau de bord",
       "Suivre les indicateurs des projets IA et de la transformation (adoption, qualité, effets, risques, coûts).",
       ["Une ligne par indicateur ; mise à jour mensuelle ou trimestrielle.", "L'écart à la cible est calculé automatiquement."],
       tables=[("Tableau de bord", ["Famille", "Indicateur", "Définition", "Valeur de départ", "Cible", "Valeur actuelle", "Écart à la cible", "Tendance", "Source", "Responsable", "Commentaire"], [
           ["Adoption", "Utilisateurs actifs", "Personnes ayant utilisé l'outil dans le mois", 0, 20, 14, "=F2-E2", "↑", "Statistiques de l'outil", "Référent IA", ""],
           ["Qualité", "Réponses correctes et sourcées", "Échantillon hebdomadaire de 20 réponses", 0.0, 0.9, 0.93, "=F3-E3", "→", "Revue du service financier", "Responsable financier", ""],
           ["Effets", "Temps hebdomadaire consacré aux questions", "Heures par semaine", 6, 3, 3.5, "=F4-E4", "↓", "Journal des tâches", "Responsable financier", ""]], 12)])

# ------------------------------------------------------------------ 16
annexe(16, "Plan de formation",
       "Organiser la formation par rôle, de façon progressive et répétée (module 20).",
       ["Sessions de 2 heures maximum, avec exercice sur une tâche réelle.", "Prévoir un format hors ligne si la connexion est faible."],
       tables=[("Plan", ["Module", "Public", "Objectifs", "Durée", "Format", "Exercice pratique", "Évaluation", "Mois", "Formateur", "Participants prévus", "Participants formés"], [
           ["Socle commun", "Tous", "Comprendre l'IA, ses limites, la politique, le feu tricolore, la vérification", "2 h", "Présentiel", "Test P2.1 sur un document public", "QCM modules 1 et 8", "M1", "Référent IA", 16, ""],
           ["Comptabilité assistée", "Finances", "Fiches P12.1 à P12.3, contrôles", "2 h", "Présentiel", "Extraction de 3 factures", "Taux d'exactitude mesuré", "M2", "Responsable financier", 3, ""]], 10)])

# ------------------------------------------------------------------ 17
annexe(17, "Feuille de route sur 90 jours",
       "Planifier 13 semaines : fondations, pilotes, évaluation, décision (module 22).",
       ["Pas plus de deux pilotes.", "Politique d'IA adoptée avant les pilotes sur données internes.", "Marquez d'un « X » les semaines d'exécution."],
       tables=[("Plan 90 jours", ["Action", "Livrable", "Responsable", "Jalon"] + [f"S{i}" for i in range(1, 14)], [
           ["Diagnostic et inventaire", "Diagnostic synthétique", "Coordinatrice", "S3 validé", "X", "X", "X"] + [""] * 10,
           ["Politique IA et feu tricolore", "Politique adoptée", "Coordinatrice", "S5 CA", "", "X", "X", "X", "X"] + [""] * 8,
           ["Évaluation des pilotes", "Note d'évaluation", "Coordinatrice", "S11", ""] + [""] * 8 + ["X", "X", "", ""],
           ["Décision et feuille de route 12 mois", "Décision du CA", "Président", "S13", ""] + [""] * 10 + ["X", "X"]], 8)])

# ------------------------------------------------------------------ 19
annexe(19, "Modèle de suivi des anomalies",
       "Enregistrer et traiter les alertes (doublons, écarts, pièces manquantes, etc.) jusqu'à leur clôture.",
       ["Chaque alerte est instruite et documentée, même si elle se révèle être un faux positif.", "Les indices de fraude suivent la politique dédiée, de façon confidentielle."],
       tables=[("Anomalies", ["N°", "Date de détection", "Source (test, contrôle, signalement)", "Opération(s)", "Description", "Montant", "Priorité", "Vérifications réalisées", "Conclusion (faux positif / anomalie / indice à investiguer)", "Action", "Responsable", "Date de clôture"], [
           ["A01", "2026-04-08", "Test T1 doublons", "D01 / D13", "Même fournisseur, montant, libellé et bon de commande", 1240, "Élevée", "Bons de commande et de livraison", "Anomalie : paiement en double", "Demande de remboursement", "Responsable financier", ""],
           ["A02", "2026-04-08", "Test T1 doublons", "D03 / D39", "Hôtel, même montant", 270, "Faible", "Ordres de mission", "Faux positif : deux missions distinctes", "Aucune", "Contrôleuse interne", "2026-04-09"]], 15)])

# ------------------------------------------------------------------ 20
annexe(20, "Modèle de suivi des recommandations",
       "Suivre la mise en œuvre des recommandations (audit, contrôle interne) et des décisions.",
       ["Une ligne par recommandation, avec preuve de mise en œuvre.", "Présentez le tableau à chaque comité d'audit ou conseil."],
       tables=[("Recommandations", ["N°", "Source (audit, date)", "Constat", "Recommandation", "Priorité", "Responsable", "Échéance", "État (à faire / en cours / réalisée / reportée)", "Preuve de mise en œuvre", "Commentaire"], [
           ["R01", "Audit interne T1 2026", "Fractionnement des achats et auto-approbation (D16-D18)", "Interdire l'auto-approbation ; alerte mensuelle de cumul par fournisseur", "Élevée", "DAF", "2026-06-30", "En cours", "", ""]], 15)])

# ------------------------------------------------------------------ 21
annexe(21, "Modèle de mesure des performances",
       "Comparer la situation avant et après une solution, et documenter la valeur produite.",
       ["Mesurez la valeur de départ avant le déploiement (journal des tâches, extractions).", "Distinguez les gains mesurés des estimations.", "Précisez à quoi le temps gagné a été réaffecté."],
       tables=[("Mesure", ["Indicateur", "Unité", "Méthode de mesure", "Avant (date)", "Après (date)", "Variation", "Variation %", "Mesuré / estimé", "Commentaire (réaffectation du temps, effets non prévus)"], [
           ["Temps de traitement par facture", "minutes", "Chronométrage de 30 factures", 6, 2.5, "=E2-D2", "=IF(D2=0,\"\",(E2-D2)/D2)", "Mesuré", "Temps réaffecté à l'analyse budgétaire"]], 10)])

# ------------------------------------------------------------------ 22
annexe(22, "Checklist de mise en production d'une solution IA",
       "Décider du déploiement (porte 2) sur la base de critères vérifiés.",
       ["Tous les points « bloquants » doivent être conformes.", "Signature de la direction requise."],
       sections=[("Checklist", """| N° | Point | Bloquant | Conforme (oui/non) | Preuve |
|---|---|---|---|---|
| 1 | Cahier des charges validé, critères d'acceptation fixés avant tests | Oui | | |
| 2 | Jeu de tests exécuté ; critères d'acceptation atteints | Oui | | |
| 3 | Pilote mené ; indicateurs comparés aux valeurs de départ | Oui | | |
| 4 | Examen éthique et checklist de protection des données réalisés | Oui | | |
| 5 | Outil inscrit au registre ; contrat vérifié (confidentialité, entraînement, localisation, réversibilité) | Oui | | |
| 6 | Droits d'accès configurés (moindre privilège, comptes nominatifs, double authentification) | Oui | | |
| 7 | Contrôles humains définis et documentés | Oui | | |
| 8 | Risques inscrits au registre avec mesures | Oui | | |
| 9 | Utilisateurs formés ; supports disponibles | Non | | |
| 10 | Responsable et suppléant de maintenance désignés | Oui | | |
| 11 | Procédure de mise à jour et de relance des tests | Oui | | |
| 12 | Procédure d'incident et d'arrêt d'urgence | Oui | | |
| 13 | Budget récurrent validé | Non | | |
| 14 | Communication aux utilisateurs et, le cas échéant, aux personnes concernées | Non | | |

Décision : ☐ mise en production ☐ mise en production partielle ☐ report ☐ arrêt : Date : ______ : Signature de la direction : ______""")])


# ------------------------------------------------------------------ 18 : bibliothèque extraite du manuscrit
def bibliotheque():
    rows, md = [], []
    for f in sorted(glob.glob(os.path.join(ROOT, "02_MANUSCRIT", "partie_*", "module_*.md"))):
        txt = open(f, encoding="utf-8").read()
        mod = int(re.search(r"module_(\d+)", f).group(1))
        for m in re.finditer(r"### Fiche (P[\d.]+) : (.+?)\n(.*?)(?=\n### Fiche |\n## \d)", txt, re.S):
            code, titre, body = m.group(1), m.group(2).strip(), m.group(3)
            obj = re.search(r"\*\*B\. Objectif\.\*\* (.+)", body)
            ctx = re.search(r"\*\*C\. Contexte d'utilisation\.\*\* (.+)", body)
            prompt = re.search(r"```text\n(.*?)```", body, re.S)
            verif = re.search(r"\*\*I\. Méthode de vérification\.\*\* (.+)", body)
            prec = re.search(r"\*\*J\. Précautions\.\*\* (.+)", body)
            r = [code, mod, titre, obj.group(1) if obj else "", ctx.group(1) if ctx else "",
                 prompt.group(1).strip() if prompt else "", verif.group(1) if verif else "", prec.group(1) if prec else ""]
            rows.append(r)
            md.append(f"### {code} : {titre} (module {mod})\n\n**Objectif.** {r[3]}\n\n**Contexte.** {r[4]}\n\n```text\n{r[5]}\n```\n\n**Vérification.** {r[6]}\n\n**Précautions.** {r[7]}\n")
    return rows, md


def write_xlsx(path, tables):
    wb = Workbook(); wb.remove(wb.active)
    thin = Side(style="thin", color="BBBBBB")
    for name, head, rows, empty in tables:
        ws = wb.create_sheet(name[:31])
        ws.append(head)
        for c in ws[1]:
            c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor=NAVY)
            c.alignment = Alignment(wrap_text=True, vertical="center")
        for r in rows:
            ws.append(r)
        for _ in range(empty):
            ws.append([""] * len(head))
        for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
            for c in row:
                c.border = Border(top=thin, bottom=thin, left=thin, right=thin)
                if c.row > 1:
                    c.alignment = Alignment(wrap_text=True, vertical="top")
        for i, h in enumerate(head, 1):
            ws.column_dimensions[get_column_letter(i)].width = max(10, min(45, len(str(h)) + 6))
        ws.freeze_panes = "A2"
    wb.save(path)


def table_md(head, rows):
    s = "| " + " | ".join(head) + " |\n|" + "---|" * len(head) + "\n"
    for r in rows:
        s += "| " + " | ".join("" if str(x).startswith("=") else str(x) for x in r) + " |\n"
    return s


def main():
    os.makedirs(OUT, exist_ok=True)
    rows18, md18 = bibliotheque()
    annexe(18, "Bibliothèque de prompts par métier",
           "Rassembler les fiches prompts de l'ouvrage pour une réutilisation immédiate, avec leur méthode de vérification.",
           ["Copiez le prompt, remplacez les éléments entre crochets, respectez les précautions.", "Ajoutez vos propres prompts testés dans le tableur (onglet « Bibliothèque »), avec leur méthode de vérification.", "Les fiches complètes (rubriques A à K) figurent dans les modules."],
           sections=[("Fiches", "\n".join(md18))],
           tables=[("Bibliothèque", ["Code", "Module", "Titre", "Objectif", "Contexte", "Prompt", "Vérification", "Précautions"], rows18, 10)])
    A.sort(key=lambda a: a["num"])
    files = []
    for a in A:
        base = f"Annexe_{a['num']:02d}_" + re.sub(r"[^A-Za-z0-9]+", "_", unicodedata.normalize("NFKD", a["titre"]).encode("ascii", "ignore").decode())[:50].strip("_")
        md = f"# Annexe {a['num']} : {a['titre']}\n\n*ASBL augmentée : © 2026 Verdi Imbole. Reproduction autorisée pour l'usage interne de l'organisation de l'acheteur.*\n\n## Objectif\n\n{a['objectif']}\n\n## Mode d'emploi\n\n" + "\n".join(f"{i}. {c}" for i, c in enumerate(a["consignes"], 1)) + "\n\n"
        for t, c in a["sections"]:
            md += f"## {t}\n\n{c}\n\n"
        for name, head, rows, empty in a["tables"]:
            if a["num"] == 18:
                continue
            md += f"## Modèle : {name}\n\n*Le fichier tableur joint contient ce modèle avec formules et lignes vides.*\n\n" + table_md(head, rows) + "\n"
        mdp = os.path.join(OUT, base + ".md")
        open(mdp, "w", encoding="utf-8").write(md)
        docx = os.path.join(OUT, base + ".docx")
        subprocess.run(["pandoc", mdp, "-o", docx, "--reference-doc", os.path.join(ROOT, "07_OUTILS", "reference.docx")], check=True)
        files += [mdp, docx]
        if a["tables"]:
            x = os.path.join(OUT, base + ".xlsx")
            write_xlsx(x, a["tables"]); files.append(x)
    for f in glob.glob(os.path.join(OUT, "donnees_exercices", "*")):
        files.append(f)
    z = os.path.join(ROOT, "06_LIVRABLES", "ANNEXES.zip")
    os.makedirs(os.path.dirname(z), exist_ok=True)
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, os.path.relpath(f, OUT))
    print(f"{len(A)} annexes ; {len(rows18)} prompts dans la bibliothèque ; {len(files)} fichiers ; {z}")


if __name__ == "__main__":
    main()
