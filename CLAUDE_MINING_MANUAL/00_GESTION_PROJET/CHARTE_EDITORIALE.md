# Charte éditoriale

## 1. Ton et style
- Français professionnel, naturel, accessible ; vouvoiement du lecteur.
- Le lecteur est accompagné par un formateur expérimenté : phrases courtes, exemples concrets, analogies minières.
- Chaque notion technique est définie à sa première apparition (gras + définition), puis reprise au glossaire (Annexe A).
- Paragraphes de 3 à 6 phrases maximum ; listes et tableaux dès que l'information est structurée.
- Pas de jargon gratuit, pas de superlatifs commerciaux sur Claude, pas de promesses de gains non démontrés.

## 2. Structure obligatoire d'un chapitre
| Bloc | Titre dans le manuscrit |
|---|---|
| A | Mise en situation professionnelle |
| B | Objectifs d'apprentissage (verbes observables : identifier, rédiger, vérifier, comparer, produire…) |
| C | Comprendre avant de pratiquer |
| D | Démonstration guidée |
| E | Prompts commentés |
| F | Exercices pratiques (au moins un guidé + un autonome) |
| G | Livrable professionnel |
| H | Vérification des résultats |
| I | Limites et précautions |
| J | Boîte à outils |
| K | Quiz (8 à 10 questions, corrigés en fin de partie) |
| L | Mon carnet d'application et de réflexion (généré par le gabarit commun) |

Les chapitres de la Partie III ajoutent, pour chaque cas d'usage important, la grille en 12 points : problème, méthode habituelle, contribution de Claude, données nécessaires, procédure, prompt, échanges successifs, exemple de résultat, contrôle qualité, erreurs possibles, limites, livrable final.

## 3. Encadrés (syntaxe Markdown → styles Word)
```
::: {.encadre .retenir}      À RETENIR
::: {.encadre .terrain}      CONSEIL DE TERRAIN
::: {.encadre .attention}    ATTENTION
::: {.encadre .erreur}       ERREUR FRÉQUENTE
::: {.encadre .application}  APPLICATION PROFESSIONNELLE
::: {.encadre .defi}         DÉFI PRATIQUE
::: {.encadre .setrompe}     QUAND CLAUDE SE TROMPE
::: {.encadre .controle}     CONTRÔLE QUALITÉ
::: {.prompt}                Prompt (police à chasse fixe, fond gris)
```

## 4. Conventions
- Nombres : espace insécable des milliers (2 350), virgule décimale (2,4 %).
- Unités : t, kt, Mt, Mt/an, g/t, %, USD, MUSD.
- Noms de produits : Claude, Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5, Claude Fable 5.2, Projects (Projets), Artifacts (artefacts), Research (recherche approfondie), Skills (compétences), Cowork, Claude Code, MCP. Le terme anglais de l'interface est donné entre parenthèses à la première occurrence.
- Les prompts sont rédigés en français, prêts à copier.
- Données fictives : toujours signalées par la mention « (fictif) » ou par le contexte MCC.
- Informations sur Claude : datées « état au 16 novembre 2026 » lorsqu'elles sont susceptibles d'évoluer (modèles, prix, plans, fonctionnalités).

## 5. Citations et sources
- Norme APA 7e édition, adaptée au français : (Auteur, année) dans le texte ; référence complète en bibliographie/webographie.
- Toute affirmation technique, juridique, réglementaire ou chiffrée externe est sourcée.
- Seules les références du `REGISTRE_SOURCES.md` peuvent être citées.
- Reformulation fidèle privilégiée ; citations directes courtes, entre guillemets, avec localisation.
- Distinction explicite : fait documenté / interprétation de l'auteur / exemple fictif.

## 6. Illustrations
- Numérotation par chapitre : Figure 3.2 = 2e figure du chapitre 3.
- Chaque figure : numéro, titre, légende explicative, source (« Illustration réalisée pour cet ouvrage » ou crédit complet de la licence).
- Interface de Claude : **aucune fausse capture d'écran**. Les vues d'interface sont des **illustrations schématiques** explicitement signalées comme telles.
- Photographies externes : uniquement sous licence libre (domaine public, CC BY, CC BY-SA) avec auteur, URL, licence et date de consultation.

## 7. Sécurité et responsabilité
- Claude est présenté comme un outil d'assistance ; la responsabilité reste humaine.
- Aucune délégation à Claude des décisions critiques : tirs et explosifs, stabilité des ouvrages (fosses, digues, galeries), interventions d'urgence, décisions de sécurité engageant la vie humaine. Ce principe est rappelé dans chaque chapitre concerné.

## 8. Palette graphique
| Usage | Couleur | Code |
|---|---|---|
| Titres, structure | Bleu marine profond | #0B2545 |
| Accents | Or discret | #C9A227 |
| Fonds | Gris clair | #EEF1F5 |
| Technologie / environnement | Turquoise | #13A89E |
| Alerte | Rouge brique | #B23A48 |
| Texte | Gris anthracite | #222831 |
