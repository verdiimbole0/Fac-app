# Module 16 — Achats, approvisionnements, logistique et patrimoine

## 16.1 Mise en situation

Le RCE doit acheter douze pompes manuelles pour un programme d'accès à l'eau. Le technicien rédige une demande sur un bout de papier ; trois fournisseurs envoient leurs offres sous des formes très différentes (un PDF de six pages, une photo de devis manuscrit, un courriel) ; le comité d'achat compare « à l'œil » ; à la livraison, une pompe est endommagée mais la facture est payée en totalité ; six mois plus tard, l'inventaire ne retrouve que dix pompes dans le registre.

Chacune de ces étapes peut être améliorée — certaines avec l'IA, la plupart avec des procédures et des outils simples.

## 16.2 Problématique

Les achats représentent souvent la plus grande part des dépenses d'une ASBL et concentrent des risques importants : surcoûts, favoritisme, fractionnement, fraude, ruptures de stock, perte d'actifs. Les bailleurs imposent des règles de mise en concurrence et de traçabilité. La fonction achats-logistique manipule par ailleurs beaucoup de documents hétérogènes (devis, bons de commande, bons de livraison, factures, fiches d'inventaire) : un terrain favorable à l'extraction et au rapprochement assistés.

## 16.3 Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :

1. structurer le circuit achats de la demande au paiement, avec séparation des tâches ;
2. organiser la consultation et extraire les offres dans un tableau comparatif normalisé ;
3. appliquer une grille d'évaluation pondérée transparente ;
4. contrôler la réception par rapprochement à trois voies ;
5. tenir stocks, inventaires et registre des immobilisations ;
6. planifier maintenance et réapprovisionnements.

## 16.4 Notions et définitions

- **Demande d'achat** : expression formelle d'un besoin (quoi, combien, quand, pour quel projet, quel budget).
- **Seuils de procédure** : montants qui déterminent la procédure (achat direct, consultation de trois fournisseurs, appel d'offres).
- **Tableau comparatif** : document qui présente les offres de façon homogène et les évalue selon des critères définis à l'avance.
- **Bon de commande** : engagement formel envers le fournisseur.
- **Rapprochement à trois voies** : comparaison commande / bon de livraison / facture avant paiement.
- **Immobilisation** : bien durable dont la valeur dépasse un seuil fixé par la politique comptable, inscrit à l'actif et suivi dans un registre.
- **Inventaire** : comptage physique des stocks et des biens, comparé aux registres.

> **⚖️ Adaptation réglementaire** — Les seuils de procédure, les règles d'origine des biens, les obligations de publicité et les règles de propriété des biens financés dépendent des bailleurs et, pour certaines organisations, du droit des marchés publics ou du droit fiscal local. Les règles du bailleur s'appliquent aux achats qu'il finance.

## 16.5 Explications détaillées

![Figure 16.1 — Circuit achats et logistique](03_ILLUSTRATIONS/figures/fig_16_1.svg)

### Demande d'achat et contrôle budgétaire

Un formulaire numérique de demande d'achat (champs obligatoires : description, spécifications, quantité, date souhaitée, projet, ligne budgétaire, estimation) réduit les allers-retours. L'IA peut aider le demandeur à **préciser les spécifications techniques** (fiche P16.1, partie 1) — à condition qu'un technicien les valide et qu'elles ne soient pas rédigées de façon à favoriser un fournisseur. Le contrôle budgétaire vérifie le disponible sur la ligne (module 12).

### Fournisseurs

Le fichier fournisseurs est un référentiel critique : identité, coordonnées, documents légaux, coordonnées bancaires (dont toute modification est vérifiée par un second canal), historique de performance. Les doublons et les fournisseurs inactifs doivent être nettoyés (module 7). L'IA peut repérer des fournisseurs aux noms ou coordonnées proches (possible doublon ou fournisseur lié).

### Consultation et comparaison des offres

L'IA est particulièrement utile pour **normaliser des offres hétérogènes** : extraire, de chaque devis, le prix unitaire, les quantités, les frais annexes (transport, installation), le délai, la garantie, la validité de l'offre, les conditions de paiement et la conformité aux spécifications. Elle produit un tableau homogène que le comité examine. **L'évaluation** elle-même suit une grille définie avant l'ouverture des offres, et **la décision** appartient au comité.

*Exemple (fictif) — 12 pompes manuelles :*

| | Offre A | Offre B | Offre C |
|---|---|---|---|
| Prix unitaire | 2 050 | 1 890 | 1 980 |
| Transport | inclus | 900 | inclus |
| **Prix total rendu site** | **24 600** | **23 580** | **23 760** |
| Délai de livraison | 6 semaines | 10 semaines | 4 semaines |
| Garantie | 12 mois | 24 mois | 12 mois |
| Certificat de conformité aux spécifications | fourni | fourni | **manquant** |

Critère éliminatoire : conformité technique attestée. Le règlement de consultation de l'organisation autorise la régularisation d'un **document administratif manquant** dans un délai de 48 heures, sans modification de l'offre. Le fournisseur C transmet le certificat dans le délai.

Grille de notation (définie avant l'ouverture) : prix 60 %, délai 25 %, garantie 15 %. Note prix = (prix le plus bas / prix de l'offre) × 100 ; note délai = (délai le plus court / délai de l'offre) × 100 ; note garantie = (garantie de l'offre / garantie la plus longue) × 100.

| | Prix (60 %) | Délai (25 %) | Garantie (15 %) | **Total** |
|---|---|---|---|---|
| A | 95,85 | 66,67 | 50,00 | **81,68** |
| B | 100,00 | 40,00 | 100,00 | **85,00** |
| C | 99,24 | 100,00 | 50,00 | **92,05** |

*Calcul pour C :* 99,24 × 0,60 + 100 × 0,25 + 50 × 0,15 = 59,54 + 25,00 + 7,50 = 92,05 (calculé au tableur). Le comité retient l'offre C et consigne sa décision et ses motifs dans un procès-verbal de sélection.

### Commandes et livraisons

Le bon de commande reprend exactement l'offre retenue. À la livraison, le réceptionnaire — **qui n'est ni le demandeur ni l'acheteur** — compte, contrôle l'état, signe le bon de livraison et note les réserves. Dans l'exemple : 12 pompes livrées, dont une au corps fissuré ; réserve inscrite sur le bon de livraison avec photo.

Le **rapprochement à trois voies** (commande : 12 ; livraison : 12 dont 1 avec réserve ; facture : 12 × 1 980 = 23 760) conduit à **bloquer le paiement d'une pompe** (1 980 UM) jusqu'au remplacement. L'IA peut extraire les quantités des trois documents et signaler l'écart ; le logiciel bloque ; le logisticien et le comptable traitent.

### Stocks et inventaires

Les stocks (kits, médicaments, matériaux) se suivent par fiche de stock (entrées, sorties, solde) ou dans un outil de gestion des stocks. Inventaire physique au moins annuel, souvent trimestriel pour les stocks sensibles, par une équipe qui ne tient pas le stock, avec rapprochement et analyse des écarts. L'IA aide à : extraire les données des bons de sortie manuscrits photographiés ; proposer des **seuils de réapprovisionnement** à partir de l'historique de consommation (à valider) ; rédiger le rapport d'inventaire.

### Immobilisations

Chaque bien au-dessus du seuil reçoit une étiquette (numéro unique, éventuellement code QR), est inscrit au registre (description, numéro de série, date, valeur, projet et bailleur, localisation, responsable, état) et suit son cycle : affectation, transfert, maintenance, cession, mise au rebut, avec autorisation. Les biens installés dans les communautés (pompes) font l'objet d'un **procès-verbal de remise** au comité de gestion, selon les règles du bailleur sur la propriété des biens.

### Maintenance et approvisionnements

Un calendrier de maintenance préventive (véhicules, générateurs, pompes) réduit les pannes coûteuses. Les rappels sont des automatisations simples. L'IA peut aider à rédiger des fiches de maintenance à partir des manuels des fabricants et à analyser les historiques de pannes.

## 16.6 Application métier : de la demande d'achat à l'inventaire au RCE

**A. Contexte.** Grande ONG, ERP, achats importants, bureaux de terrain.
**B. Problème.** Offres hétérogènes, comparaisons subjectives, réceptions non contrôlées, actifs non suivis.
**C. Symptômes.** Paiement d'une pompe endommagée ; écart d'inventaire de deux pompes ; remarques d'audit sur la documentation des sélections.
**D. Causes profondes.** Pas de formulaire de demande ; pas de grille définie à l'avance ; réceptionnaire = demandeur ; registre des immobilisations non à jour.
**E. Processus actuel.** Demande papier → consultation informelle → choix → livraison → paiement.
**F. Faiblesses.** Séparation des tâches ; traçabilité des choix ; rapprochement.
**G. Résultat recherché.** 100 % des achats au-dessus du seuil avec tableau comparatif et PV ; rapprochement à trois voies systématique ; écart d'inventaire nul ou expliqué.
**H. Pertinence de l'IA.** Forte pour l'extraction et la normalisation des offres et des documents de réception ; faible pour l'évaluation et la décision.
**I. Alternatives sans IA.** Modèle de tableau comparatif ; saisie manuelle des offres.
**J. Solution.** Formulaire de demande ; extraction assistée des offres ; grille pondérée au tableur ; PV de sélection ; rapprochement assisté ; registre des immobilisations avec étiquetage.
**K. Niveau.** Intermédiaire (Débutant possible pour les petites structures).
**L. Outils.** Formulaire numérique ; assistant validé ; tableur ou module achats de l'ERP ; étiquettes ; application de scan pour l'inventaire.
**M. Étapes détaillées.**

1. Demande d'achat via formulaire ; contrôle budgétaire.
2. Spécifications validées par le technicien (aide de l'IA possible).
3. Grille d'évaluation définie et validée **avant** la consultation.
4. Consultation selon le seuil ; réception des offres dans une boîte dédiée, ouverture en comité à date fixe.
5. Extraction et normalisation des offres (fiche P16.1).
6. Vérification par l'acheteur de chaque valeur extraite par rapport aux offres originales.
7. Notation au tableur ; délibération ; PV de sélection signé.
8. Bon de commande.
9. Réception par une personne indépendante ; bon de livraison avec réserves et photos.
10. Rapprochement à trois voies (fiche P16.2) ; blocage des écarts.
11. Entrée en stock ou inscription au registre des immobilisations ; étiquetage.
12. Paiement selon la procédure (module 12).
13. Inventaire périodique et maintenance.

**N. Prompts.** P16.1, P16.2.
**O. Exemple de résultat.** Tableaux ci-dessus.
**P. Vérification.** Contrôle de chaque valeur extraite ; recalcul de la grille ; vérification du PV.
**Q. Contrôles humains.** Spécifications, grille, évaluation, décision, réception physique, traitement des écarts, approbation du paiement, inventaire.
**R. Risques.** Erreur d'extraction (prix, unité, frais de transport oubliés) ; spécifications orientées ; conflit d'intérêts ; confidentialité des offres.
**S. Coûts et maintenance.** Outils existants pour le niveau Débutant ; module achats de l'ERP et application d'inventaire pour les niveaux supérieurs.
**T. Indicateurs.** Délai demande–commande ; part des achats conformes à la procédure ; nombre d'écarts de rapprochement ; écarts d'inventaire ; taux de disponibilité des équipements.
**U. Amélioration continue.** Évaluation annuelle des fournisseurs ; ajustement des seuils de réapprovisionnement.

### Solutions selon le niveau

| Niveau | Mise en œuvre | Outils | Coûts | Limites |
|---|---|---|---|---|
| Débutant | Formulaire de demande, tableau comparatif au tableur, extraction assistée des offres, registre des immobilisations en tableur, fiches de stock | Formulaire, tableur, assistant | Faibles | Saisie manuelle ; discipline |
| Intermédiaire | Logiciel achats/stock avec workflow ; extraction de documents ; étiquettes à code QR et application d'inventaire mobile | Logiciel de gestion, application mobile | Abonnements | Paramétrage |
| Avancé | Module achats de l'ERP intégré à la comptabilité (engagements, rapprochement automatique, blocages), portail fournisseurs, prévisions de consommation | ERP, portail | Élevés | Complexité ; adoption par les fournisseurs |

## 16.7 Prompts prêts à l'emploi

### Fiche P16.1 — Normaliser des offres hétérogènes dans un tableau comparatif

**A. Titre.** Tableau comparatif normalisé des offres.

**B. Objectif.** Extraire et présenter les offres de façon homogène, avec les écarts par rapport aux spécifications.

**C. Contexte d'utilisation.** Consultation de fournisseurs, après ouverture des offres.

**D. Données nécessaires.** Spécifications techniques ; offres (PDF, photos, courriels) ; règles de consultation (outil autorisé pour données orange : les offres sont confidentielles).

**E. Prompt complet.**

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

**F. Instructions d'utilisation.** Vérifiez chaque valeur sur l'offre originale ; reportez les valeurs vérifiées dans le tableur de notation ; la notation se fait selon la grille prédéfinie.

**G. Résultat attendu.** Un tableau homogène et sourcé, sans classement, avec une liste de clarifications.

**H. Exemple d'application (illustratif).** Le tableau signale pour l'offre B : « Transport : 900 UM (devis, ligne 14, mention manuscrite en bas de page) » — un montant que la lecture rapide du comité avait manqué, et qui change le classement par le prix.

**I. Méthode de vérification.** Pointage de chaque cellule ; recalcul des totaux au tableur ; contrôle des unités (prix par pièce ou par lot ?).

**J. Précautions.** Les offres sont confidentielles ; outil validé exclusivement. Aucune transmission d'une offre à un autre fournisseur.

**K. Amélioration.** « Ajoute une ligne "risques" (fournisseur nouveau, délai long, absence de service après-vente local) en citant les éléments des offres. »

### Fiche P16.2 — Rapprochement commande / livraison / facture

**A. Titre.** Rapprochement à trois voies assisté.

**B. Objectif.** Repérer les écarts de quantités, de prix et de références avant paiement.

**C. Contexte d'utilisation.** Réception, avant transmission de la facture au paiement.

**D. Données nécessaires.** Bon de commande, bon de livraison signé (avec réserves), facture.

**E. Prompt complet.**

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

**F. Instructions d'utilisation.** Le comptable applique les montants au tableur ; le logisticien gère les réserves avec le fournisseur.

**G. Résultat attendu.** Un tableau d'écarts et d'actions.

**H. Exemple d'application (illustratif).** « Pompe manuelle : commandée 12, livrée 12 (1 avec réserve : corps fissuré), facturée 12, prix 1 980 = 1 980 → bloquer partiellement : montant à bloquer = 1 × prix unitaire ». La comptable bloque 1 980 UM.

**I. Méthode de vérification.** Contrôle sur les documents originaux ; vérification des signatures et de l'indépendance du réceptionnaire.

**J. Précautions.** Données orange ; coordonnées bancaires non recopiées.

**K. Amélioration.** « Rédige le courriel au fournisseur demandant le remplacement de l'article sous réserve, avec les références des documents. »

## 16.8 Résultats attendus

Achats conformes et documentés ; comparaisons transparentes ; aucun paiement sans rapprochement ; stocks et actifs suivis ; maintenance planifiée.

## 16.9 Contrôles humains

> **🛑 Contrôle humain obligatoire** — Validation des spécifications, définition de la grille, évaluation et choix du fournisseur, réception physique, traitement des écarts, approbation des paiements, autorisation des cessions et mises au rebut. Séparation des tâches entre demandeur, acheteur, réceptionnaire et payeur.

## 16.10 Risques et erreurs à éviter

- Laisser l'IA classer les offres ou choisir le fournisseur.
- Définir la grille après avoir vu les offres.
- Oublier les frais annexes dans la comparaison.
- Payer sans rapprochement à trois voies.
- Confier la réception au demandeur.
- Ne pas étiqueter les immobilisations.

## 16.11 Exercice pratique

**Consigne (2 heures).** (1) Avec trois devis réels ou fictifs, appliquez P16.1. (2) Construisez la grille au tableur (poids définis avant) et recalculez l'exemple des pompes pour vérifier les totaux 81,68 / 85,00 / 92,05. (3) Rédigez la procédure de réception en cinq étapes, en précisant qui fait quoi.

**Éléments de correction.** (1) Le tableau ne classe pas les offres et cite les sources. (2) Les totaux sont retrouvés au centième près ; si vous obtenez des valeurs légèrement différentes, vérifiez l'arrondi des notes intermédiaires. (3) La procédure prévoit l'indépendance du réceptionnaire, le comptage, le contrôle de l'état, les réserves écrites et la transmission au comptable.

## 16.12 Synthèse

- Le circuit achats repose sur la séparation des tâches et des règles connues à l'avance.
- L'IA normalise les offres et rapproche les documents ; le comité évalue et décide.
- Le rapprochement à trois voies protège contre les paiements indus.
- Stocks, immobilisations et maintenance se suivent avec des registres à jour et des inventaires indépendants.

## 16.13 QCM — Module 16

**Q1.** (une seule réponse) Le rapprochement à trois voies compare :

a) trois devis.
b) budget, engagement et paiement.
c) stock, inventaire et immobilisations.
d) commande, bon de livraison et facture.

**Q2.** (une ou plusieurs réponses) Qui ne devrait pas réceptionner la marchandise ?

a) Le demandeur.
b) L'acheteur.
c) Une personne indépendante désignée.
d) Le payeur.

**Q3.** (une seule réponse) La grille d'évaluation des offres doit être définie :

a) après l'ouverture des offres.
b) avant l'ouverture des offres.
c) par le fournisseur.
d) par l'IA après lecture des offres.

**Q4.** (une seule réponse) Dans l'exemple, le prix total rendu site de l'offre B est :

a) 23 580
b) 22 680
c) 23 760
d) 24 600

**Q5.** (une seule réponse) La note totale de l'offre C est :

a) 81,68
b) 85,00
c) 99,24
d) 92,05

**Q6.** (une ou plusieurs réponses) Dans l'extraction des offres, l'IA doit :

a) citer la source de chaque valeur.
b) signaler les informations non précisées.
c) classer les offres.
d) ne pas convertir les devises sans instruction.

**Q7.** (mise en situation — une seule réponse) Une pompe livrée est endommagée ; la facture porte sur 12 pompes. Que faites-vous ?

a) Payer la totalité et demander un avoir plus tard.
b) Bloquer le paiement de l'article sous réserve jusqu'au remplacement, selon la procédure.
c) Refuser toute la livraison.
d) Ne rien signaler.

**Q8.** (mise en situation — une seule réponse) Un technicien demande à l'IA de rédiger des spécifications « qui correspondent exactement au modèle du fournisseur X ». Votre réaction ?

a) C'est contraire à l'équité de la consultation ; les spécifications doivent décrire le besoin fonctionnel.
b) C'est efficace.
c) C'est acceptable sous le seuil.
d) Il faut demander au fournisseur X de les écrire.

**Q9.** (une seule réponse) Une immobilisation est :

a) tout achat de fournitures.
b) un stock de médicaments.
c) un bien loué.
d) un bien durable au-dessus d'un seuil, inscrit et suivi dans un registre.

**Q10.** (une ou plusieurs réponses) Indicateurs pertinents pour la fonction achats-logistique :

a) délai demande–commande.
b) écarts d'inventaire.
c) nombre d'écarts de rapprochement.
d) nombre de fournisseurs consultés par l'IA.

## 16.14 Corrigé détaillé — Module 16

**Q1 : d.** C'est le contrôle clé avant paiement.

**Q2 : a, b, d.** La réception est confiée à une personne indépendante (c).

**Q3 : b.** Sinon, la grille peut être ajustée pour favoriser une offre.

**Q4 : a.** 12 × 1 890 + 900 = 23 580.

**Q5 : d.** 59,54 + 25,00 + 7,50 = 92,05 (calcul au tableur).

**Q6 : a, b, d.** Le classement (c) relève du comité.

**Q7 : b.** Le blocage partiel protège l'organisation sans pénaliser les articles conformes.

**Q8 : a.** Des spécifications orientées faussent la concurrence et peuvent rendre la dépense inéligible.

**Q9 : d.** Le seuil est fixé par la politique comptable.

**Q10 : a, b, c.** Le critère d (outil) ne mesure pas la performance du processus.

**Barème.** 2 points par question (tout ou rien pour les réponses multiples). Total sur 20. **Niveau de maîtrise :** 0–9 à consolider · 10–13 en progression · 14–17 maîtrise opérationnelle · 18–20 maîtrise avancée.
