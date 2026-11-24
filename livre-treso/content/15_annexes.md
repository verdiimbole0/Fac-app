@section Annexes pratiques : les dix modèles|Annexes pratiques
Les dix modèles ci-dessous sont fournis dans le classeur Excel « Outils_Treso_sous_controle.xlsx », avec les données d'exemple de MAKAO, et sous forme de dix fichiers séparés. Ils fonctionnent dans Excel (versions récentes) et dans Google Sheets. Les formules sont données ici avec les noms français des fonctions ; les références de colonnes correspondent aux fichiers. Règle commune : les cellules de saisie sont sur fond clair, les cellules calculées sont protégées.
## A1. Situation journalière de trésorerie
**Usage** : chaque matin, établir le disponible prouvé. **Colonnes** : A Compte ; B Devise ; C Solde en devise ; D Taux (CDF pour 1 USD, 1 pour l'USD) ; E Solde en USD ; F Preuve (relevé, billetage, capture). **Formules** : `E2 = C2/D2` ; total `E8 = SOMME(E2:E7)`. **Consigne** : saisir le taux du jour et sa source en cellule D10.
Table: Exemple A1, MAKAO au 31/12/2025
|{w:40,12,18,10,20}Compte|Devise|Solde devise|Taux|Solde USD
|Banque Alpha USD|USD|11 400|1|11 400
|Banque Alpha CDF|CDF|3 420 000|2 850|1 200
|Caisse USD|USD|600|1|600
|Caisse CDF|CDF|1 140 000|2 850|400
|Monnaie électronique|USD|1 400|1|1 400
|Total|||| 15 000
## A2. Budget mensuel de trésorerie
**Usage** : plan validé sur l'année, mois par mois. **Structure** : lignes d'encaissements et de décaissements par catégorie, une colonne par mois. **Formules** : total des encaissements `=SOMME(C5:C7)` ; solde final `=C3+C8-C18` ; solde initial du mois suivant `D3 = C19`. **Consigne** : ne jamais saisir un solde initial à la main après le premier mois.
## A3. Prévisionnel glissant sur 13 semaines
**Usage** : piloter les points bas. **Onglet Mouvements** : A Date ; B Sens (E ou D) ; C Catégorie ; D Libellé ; E Montant ; F Solde cumulé `F2 = F1+SI(B2="E";E2;-E2)` (lignes triées par date, sorties avant entrées). **Onglet Synthèse**, une ligne par semaine : début, fin ; entrées `=SOMME.SI.ENS(Mouvements!E:E;Mouvements!B:B;"E";Mouvements!A:A;">="&B5;Mouvements!A:A;"<="&C5)` ; sorties idem avec "D" ; clôture `=D5+E5-F5` ; point bas `=MIN(D5;MIN.SI.ENS(Mouvements!F:F;Mouvements!A:A;">="&B5;Mouvements!A:A;"<="&C5))`. **Consigne** : chaque lundi, remplacer les prévisions passées par le réalisé et ajouter une semaine.
Table: Exemple A3, les quatre premières semaines après les décisions du chapitre 5
|{w:10,20,16,14,14,14,12}Sem.|Période|Ouverture|Entrées|Sorties|Clôture|Point bas
|S1|05/01-11/01|15 000|26 500|31 500|10 000|5 000
|S2|12/01-18/01|10 000|26 500|2 100|34 400|10 000
|S3|19/01-25/01|34 400|26 500|51 150|9 750|9 750
|S4|26/01-01/02|9 750|26 500|9 000|27 250|9 750
## A4. Suivi des créances clients
**Colonnes** : A Client ; B N° facture ; C Date ; D Montant ; E Échéance ; F Payé ; G Reste `=D2-F2` ; H Jours de retard `=SI(G2>0;MAX(0;$K$1-E2);0)` (K1 = date d'analyse) ; I Tranche `=SI(G2=0;"Soldée";SI(H2=0;"Non échu";SI(H2<=30;"1-30 j";SI(H2<=60;"31-60 j";SI(H2<=90;"61-90 j";"+90 j")))))` ; J Dernière action ; K Date promise ; L Statut. **Balance âgée** : `=SOMME.SI.ENS(G:G;A:A;$A20;I:I;B$19)`. **Consigne** : une ligne par facture ; mise à jour à chaque paiement et à chaque relance.
Table: Exemple A4, quatre factures au 31/12/2025 (date d'analyse K1 = 31/12/2025)
|{w:19,18,16,10,8,13,16}Client|Facture|Échéance|Reste|Jours|Tranche|Action
|Les Palmiers|FA-2025-1187|28/12/2025|9 000|3|1-30 j|Relance J+3
|Clinique Lumière|FA-2025-1290|20/01/2026|14 000|0|Non échu|Rappel J-5
|Espoir Rural|FA-2025-0890|15/10/2025|2 000|77|61-90 j|Renvoi facture
|Bâtir Kongo|FA-2025-0951|15/09/2025|4 000|107|+90 j|Litige
## A5. Suivi des dettes fournisseurs
**Colonnes** : A Fournisseur ; B N° facture ; C Date ; D Montant ; E Échéance ; F Payé ; G Reste `=D2-F2` ; H Jours avant échéance `=E2-$K$1` ; I Priorité (liste : Obligatoire, Critique, Négociable, Différable) ; J Contrôle doublon `=SI(NB.SI.ENS(A:A;A2;B:B;B2)>1;"DOUBLON";"")`. **Consigne** : aucun paiement tant que la colonne J affiche « DOUBLON ».
Table: Exemple A5, le double paiement du chapitre 7
|{w:24,18,14,14,30}Fournisseur|Facture|Montant|Payé le|Contrôle doublon
|Mobilier Express|MX-1187|4 800|12/01/2026|DOUBLON
|Mobilier Express|MX-1187|4 800|25/01/2026|DOUBLON
## A6. Calendrier des paiements
**Colonnes** : A Date prévue ; B Bénéficiaire ; C Montant ; D Catégorie ; E Validé par ; F Statut ; G Disponible restant `G2 = $H$1-SOMME($C$2:C2)` (H1 = trésorerie disponible pour la semaine) ; H Alerte `=SI(G2<0;"INSUFFISANT";"")`. **Consigne** : trier par priorité puis par date ; aucune ligne « INSUFFISANT » ne part en paiement sans arbitrage écrit.
Table: Exemple A6, semaine du 5 janvier (disponible H1 = 41 500 USD)
|{w:13,37,14,18,18}Date|Bénéficiaire|Montant|Catégorie|Disponible restant
|05/01|Loyer|4 000|Obligatoire|37 500
|05/01|Papeteries Unies (1re part)|6 000|Négociable|31 500
|10/01|Charges externes|1 500|Obligatoire|30 000
|10/01|InfoPlus (1re part)|20 000|Critique|10 000
## A7. Rapprochement bancaire
**Bloc comptabilité** : solde comptable, plus ou moins les opérations de la banque non comptabilisées (frais, virements reçus). **Bloc banque** : solde du relevé, moins les chèques émis non présentés, plus les remises non créditées. **Contrôle** : `=SI(ABS(B10-E10)<0,01;"RAPPROCHÉ";"ÉCART À EXPLIQUER")`. **Consigne** : signature du préparateur et du réviseur ; suivi des éléments de plus de 30 jours.
## A8. Checklist de contrôle interne
**Colonnes** : Domaine (caisse, banque, paiements, achats, créances, monnaie électronique, IA et données) ; Contrôle ; Fréquence ; Responsable ; Fait (Oui/Non) ; Date ; Commentaire. **Indicateur** : taux de conformité `=NB.SI(E:E;"Oui")/NB.SI.ENS(E:E;"<>";E:E;"<>Fait")`. Le fichier contient 24 contrôles issus des chapitres 7, 10 et 11.
## A9. Tableau de bord de trésorerie
**Onglet Saisie** : trésorerie, charges fixes, encaissements prévus et réels, décaissements prévus et réels, créances par tranche, dettes, achats et ventes des trois derniers mois, point bas prévu. **Onglet Indicateurs** : couverture `=Tresorerie/ChargesFixes` ; réalisation `=EncReel/EncPrevu` ; DSO `=Creances/Ventes3M*92` ; DPO `=Dettes/Achats3M*92` ; état `=SI(valeur<seuil;"ALERTE";"OK")` (sens adapté à chaque indicateur). **Graphiques** : soldes hebdomadaires, prévu et réalisé, ancienneté des créances.
## A10. Analyse des écarts
**Colonnes** : A Catégorie ; B Prévu ; C Réalisé ; D Écart `=C2-B2` ; E Écart % `=SI(B2=0;"";D2/B2)` ; F Nature (liste : Décalage, Volume, Anomalie, Imprévu) ; G Explication ; H Action et responsable. **Consigne** : expliquer tout écart supérieur à 2 % ou à 1 000 USD ; reporter les décalages dans la prévision suivante.

Table: Exemple A10, deux lignes de janvier 2026
|{w:24,12,12,12,12,14,14}Catégorie|Prévu|Réalisé|Écart|Écart %|Nature|Action
|Créances au 31/12|87 000|83 000|-4 000|-4,6 %|Décalage|Palmiers relancé
|Fournisseurs|72 000|76 800|+4 800|+6,7 %|Anomalie|Avoir obtenu
:::conseil
Avant d'utiliser un modèle, faites-le tourner avec les données de MAKAO et retrouvez les chiffres du livre : c'est la meilleure façon de vérifier que vous l'avez compris.
:::
