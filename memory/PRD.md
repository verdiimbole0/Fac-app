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

## Iteration 2 (2026-02-08) — Back-office + Paiement + Promos
- [x] **Back-office `/admin` bilingue** : login page premium (Google Auth Emergent + JWT email/password), dashboard stats, sidebar navigation
- [x] **Admin Products CRUD** : liste, création, édition (nom FR/EN, description, images multiples, badges NEW/BESTSELLER, stock, catégorie), suppression avec confirmation
- [x] **Admin Orders** : table avec status dropdown (pending/paid/shipped/delivered/cancelled/failed), modal détail complet, bouton "Copier l'email de confirmation" pour envoi manuel (template FR/EN dans le presse-papier)
- [x] **Admin Promo codes** : création (code, %/fixe, min sous-total, catégorie ciblée, max_uses, date d'expiration), liste avec compteur d'usages, suppression
- [x] **Promo sur checkout** : input dans le récapitulatif, validation live (endpoint `/api/promos/apply`), affichage réduction, X pour retirer. Compteur `uses` s'incrémente à la commande.
- [x] **Flutterwave Standard v3** : 5ème méthode de paiement dans le checkout, initialisation hosted checkout, webhook signature verification, redirect `/payment/result` avec verify server-side. **Clés API vides pour l'instant** — l'endpoint retourne 503 tant que `FLW_SECRET_KEY` n'est pas dans `.env`.
- [x] Auth playbook `/app/auth_testing.md` + credentials `/app/memory/test_credentials.md`
- [x] Testing agent iteration 2 : 25/25 backend pass, tous les flows admin/promo vérifiés

## Iteration 3 (2026-02-08) — Stock + Rôles + Emails auto
- [x] **Décrément stock atomique** : à la création de commande, chaque item décrémente le stock avec `$inc:{stock:-qty}` conditionné à `stock >= qty`. Si un item échoue, rollback des items précédents. Retourne **409 "Insufficient stock for X"**. Testé : commande 999 unités sur produit avec 6 en stock → refusé, stock intact.
- [x] **Restauration stock** : si le paiement Flutterwave échoue, le stock est restauré via `restore_stock()` dans `finalize_flw_payment()`.
- [x] **Rôles admin (RBAC serveur)** : 3 rôles (`super_admin`, `products_editor`, `orders_manager`) avec matrice `PERMS`. Dépendance `require_perm(perm)` protège chaque route admin. Testé : editor peut CRUD produits, refusé 403 sur orders/promos/users.
- [x] **Page `/admin/users` (super_admin only)** : formulaire d'invitation (nom, email, password, rôle avec description contextuelle), liste avec swap de rôle inline + suppression. Impossible de se supprimer soi-même.
- [x] **Filtrage nav sidebar** par permission via `hasPerm()` — chaque rôle ne voit que ses items.
- [x] **Emails auto Resend** : `send_order_confirmation_email()` avec HTML premium (Playfair Display + palette site) envoie la confirmation aux clients. Silent skip si `RESEND_API_KEY` vide. **Warn log** si Resend API retourne une erreur.
- [x] Testing agent iteration 3 : 40/40 backend pytest passing, /admin/users flow validé end-to-end. RBAC corrigé sur POST /admin/products.

## Backlog / Prioritized Next Steps
### P0 (bloquants pour production)
- Coller les vraies clés dans `/app/backend/.env` :
  - `FLW_SECRET_KEY`, `FLW_PUBLIC_KEY`, `FLW_SECRET_HASH` (Flutterwave)
  - `RESEND_API_KEY`, `RESEND_FROM_EMAIL` (Resend) — le domaine doit être vérifié dans Resend
- Persistance panier/wishlist côté serveur (session ou compte client)

### P1 (haute valeur)
- Programme de fidélité (points par commande, palier de réduction automatique)
- Système d'avis clients authentifiés avec upload photos réel
- MongoDB transactions pour rendre le decrement_stock atomique multi-items
- Emails de suivi (expédition, livraison) en plus de la confirmation
- Password reset flow pour comptes admin invités

### P2 (améliorations)
- SEO avancé (SSR/meta OG dynamiques par produit)
- Wishlist partageable (URL publique)
- Recommandations personnalisées basées sur historique
- Multi-devise (EUR/XOF/USD)
- Blog éditorial ("Journal") pour SEO
- Audit log des actions admin
