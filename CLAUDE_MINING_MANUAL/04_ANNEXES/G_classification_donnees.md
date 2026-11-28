## Annexe G. Modèle de classification et de protection des données

*Modèle fictif (MCC), à adapter à la politique de sécurité de l'information de votre entreprise et au droit applicable.*

### G.1. Les quatre niveaux

| Niveau | Définition | Exemples (secteur minier) | Usage de Claude | Mesures |
|---|---|---|---|---|
| **1 : Public** | Information publiée ou destinée à l'être | Rapports publiés, textes officiels, communiqués, rapports ITIE publiés | Libre | Vérifier que l'information est réellement publique |
| **2 : Usage interne** | Diffusion interne ; dommage limité en cas de fuite | Procédures, rapports internes non sensibles, données de production agrégées, supports de formation | Espace d'entreprise uniquement | Pas de compte personnel |
| **3 : Confidentiel** | Dommage significatif en cas de fuite | Contrats et prix, données RH, incidents nominatifs, plaintes, données financières non publiées, résultats techniques non publiés non privilégiés | Espace d'entreprise, accord du propriétaire de la donnée, minimisation et pseudonymisation | Projets à accès restreint ; mémoire et connecteurs vérifiés |
| **4 : Restreint** | Dommage grave ; diffusion nominative | Informations privilégiées (résultats d'exploration, réserves avant publication), stratégie, fusions-acquisitions, contentieux, données de santé, plans de sûreté | **Interdit** | Outils dédiés, accès nominatif |

### G.2. Arbre de décision

1. L'information est-elle publique ? → Niveau 1.
2. Une fuite causerait-elle un dommage grave (marchés, sécurité, santé, contentieux, stratégie) ? → Niveau 4.
3. Contient-elle des données personnelles, contractuelles, financières ou techniques non publiées ? → Niveau 3.
4. Sinon → Niveau 2.

En cas de doute, retenir le niveau le plus élevé et demander au propriétaire de la donnée.

### G.3. Techniques de protection

| Technique | Quand | Exemple |
|---|---|---|
| Minimisation | Toujours | Ne transmettre que les colonnes utiles |
| Pseudonymisation | Données personnelles nécessaires à l'analyse | Matricules au lieu des noms |
| Agrégation | Statistiques suffisantes | Nombre de plaintes par village et par mois |
| Anonymisation | Diffusion large | Rapport d'incident pour une causerie |
| Extrait ciblé | Documents longs | Articles pertinents d'un contrat |

### G.4. Responsabilités

| Rôle | Responsabilités |
|---|---|
| Propriétaire de la donnée | Classe, autorise l'usage, révise |
| Utilisateur | Applique la classification, minimise, signale les incidents |
| Référent IA | Conseille, forme, tient le registre des cas d'usage |
| Informatique et sécurité | Configure les outils, contrôle les accès, journalise |
| Juridique | Vérifie les obligations (contrats, données personnelles, marchés) |

### G.5. Marquage

Indiquer le niveau en en-tête ou pied de page des documents (« MCC, Confidentiel, Niveau 3 »), dans le nom des projets Claude (« [N3] Achats : Contrats ») et dans le registre des cas d'usage.
