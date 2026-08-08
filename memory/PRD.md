# Billy's Store — Product Requirements Document

## Original Problem Statement
Application web e-commerce de niveau professionnel "Billy's Store" — fluide, moderne, rapide, visuellement attrayante. Catégories : Bijoux & Accessoires, Mode Homme, Mode Femme, Mode Enfant. Look luxe/minimaliste/chic, jamais générique. Bilingue FR/EN. Paiement via mobile money.

## User Choices (2026-02-08)
- MVP: catalogue + fiche produit + panier + wishlist + checkout mobile money simulé
- Pas d'authentification (achat invité uniquement)
- Données démo pré-remplies (25 produits, images Unsplash)
- Interface bilingue FR/EN avec toggle
- Style: choix du design agent → **Luxury Minimalist** (Playfair Display + Manrope, off-white/noir/or)

## User Personas
- **Visiteur premium** : recherche pièces raffinées, veut naviguer sans friction, apprécie l'esthétique éditoriale.
- **Acheteur mobile** : parcourt et checkout depuis smartphone, doit pouvoir tout faire au pouce.

## Architecture (Iteration 1 — 2026-02-08)
### Backend (FastAPI + MongoDB)
- `GET /api/categories` — 4 catégories avec heros
- `GET /api/products` — filtres category/search/min_price/max_price/size/color/availability, tri newest/price_asc/price_desc/bestseller
- `GET /api/products/suggest?q=` — autocomplétion (max 6)
- `GET /api/products/{slug}` — fiche produit
- `GET /api/products/{slug}/related` — cross-sell
- `POST /api/orders` + `GET /api/orders/{id}` — commande stockée (order_number BS-XXXXXXXX)
- Seed automatique de 25 produits au startup (`seed_data.py`)

### Frontend (React + Tailwind + shadcn)
- Providers : `StoreProvider` (cart/wishlist/lang/drawer state) + `BrowserRouter` + `Toaster`
- Routes : `/`, `/c/:slug`, `/product/:slug`, `/wishlist`, `/checkout`
- Persistance localStorage : cart, wishlist, langue
- Design system : `index.css` (Playfair Display + Manrope, palette #fafaf7/#1a1a1a/#c5a880), animations `bs-fade-up`/`bs-marquee`/hover swap image

## What's Been Implemented (2026-02-08)
- [x] Homepage éditoriale : marquee announcement bar, hero asymétrique, 4 category cards, featured, editorial dark, new arrivals
- [x] Category listing page avec sidebar filtres (prix slider, tailles, couleurs, dispo) + sort + mobile filter sheet
- [x] Product detail page : galerie thumbs + zoom, sélecteurs variantes (couleur/taille), guide des tailles dialog, accordions (Détails/Composition/Retours), avis, "Vous aimerez aussi"
- [x] Recherche overlay avec autocomplétion et empty state
- [x] Cart drawer latéral droit avec barre progress livraison offerte (seuil 150$), qty controls, remove
- [x] Wishlist icône cœur + page dédiée + empty state
- [x] Checkout 3 étapes (Coordonnées → Livraison → Paiement mobile money) avec 4 providers UI (Orange Money, MTN MoMo, Wave, Moov) + écran confirmation
- [x] Toggle FR/EN header + mobile menu hamburger + design mobile-first
- [x] 25 produits seed avec vraies images Unsplash, badges NEW/BESTSELLER/SOLD OUT/discount
- [x] Footer avec newsletter, colonnes de liens, socials
- [x] Backend testé 100% pass ; PDP direct-URL vérifié via screenshot

## Backlog / Prioritized Next Steps
### P0 (bloquants pour production)
- Intégration paiement mobile money réelle (Orange, Wave API) — actuellement UI mock
- Persistance panier/wishlist côté serveur (session ou compte)

### P1 (haute valeur)
- Back-office admin `/admin` (CRUD produits + stock + commandes)
- Emails transactionnels (confirmation commande, tracking)
- Programme fidélité / codes promo
- Système d'avis clients authentifiés avec upload photos réel
- Auth optionnelle (JWT ou Google) pour retrouver commandes

### P2 (améliorations)
- SEO avancé (SSR/meta OG dynamiques par produit)
- Wishlist partageable (URL publique)
- Recommandations personnalisées basées sur historique
- Multi-devise (EUR/XOF/USD)
- Blog éditorial ("Journal") pour SEO
