# Fac'App — "Ta réussite sur mesure."

Plateforme de tutorat universitaire (TP, préparation aux examens, accompagnement mémoires/PFE) — mobile + web, marché prioritaire RDC.

## Structure du projet

```
facapp/
├── backend/    → API Node.js/Express + Prisma (PostgreSQL)
├── web/        → Site web Next.js (étudiants + tuteurs)
└── mobile/     → App mobile Expo/React Native
```

## Ce qui est déjà en place

- **Backend** : inscription/connexion (JWT), schéma de base de données complet (étudiants, tuteurs, sessions, abonnements, paiements, messages), route d'initiation de paiement + webhook générique pour Orange Money / Airtel Money / M-Pesa / FONDEKA (stub à brancher sur les vraies API).
- **Réservation de créneaux** : liste des tuteurs (`GET /api/tutors`), demande de créneau par un étudiant (`POST /api/sessions`, avec contrôle des tarifs et des conflits d'horaires), liste des sessions de l'utilisateur connecté (`GET /api/sessions`), confirmation/clôture par le tuteur et annulation par les deux parties (`PATCH /api/sessions/:id/confirm|complete|cancel`).
- **Liaison session ↔ paiement** : `POST /api/payments/initiate` avec `purpose: "SESSION"` + `sessionId` — le montant est celui du créneau, réservé à l'étudiant concerné, session confirmée uniquement, pas de double paiement (une nouvelle tentative reste possible après un échec). Le statut de paiement est visible dans `GET /api/sessions`.
- **Messagerie asynchrone** : fil de discussion par session (`GET|POST /api/sessions/:id/messages`), dépôt de documents en multipart (20 Mo max) et téléchargement (`GET /api/sessions/:id/messages/:messageId/file`), accessible uniquement aux participants. Stockage sur disque local (`backend/uploads/`) pour l'instant.
- **Charte d'intégrité académique** : acceptation obligatoire à l'inscription (`acceptedIntegrityCharter`), affichée sur les formulaires web et mobile.
- **Web** : page d'accueil, inscription (avec charte), connexion, page `/sessions` (réservation, confirmation/annulation/clôture, paiement d'une session confirmée) et fil de discussion `/sessions/[id]` avec dépôt et téléchargement de documents.
- **Mobile** : inscription (avec charte) et connexion (token stocké via `expo-secure-store`, reconnexion automatique), écrans « Choisir un tuteur », « Réserver un créneau », « Mes sessions », paiement d'une session confirmée et messagerie par session (texte ; dépôt de documents via le site web pour l'instant).

## Démarrage rapide

### 1. Backend
```bash
cd backend
cp .env.example .env   # renseigner DATABASE_URL et JWT_SECRET
npm install
npm run prisma:migrate  # crée les tables en base
npm run dev              # démarre l'API sur http://localhost:4000
```

### 2. Web
```bash
cd web
npm install
npm run dev   # démarre sur http://localhost:3000
```

### 3. Mobile
```bash
cd mobile
npm install
npm start   # ouvre Expo, scanner le QR code avec l'app Expo Go
```

## Prochaines étapes de développement (dans l'ordre)

1. **Paiement réel** : intégrer les API/SDK d'Orange Money, Airtel Money, M-Pesa et FONDEKA dans `backend/src/routes/payments.js` (remplacer les TODO) — en attente des accès API des opérateurs. Chaque provider aura sa propre documentation d'intégration et son format de webhook.
2. **Stockage des documents dans le cloud** : remplacer le disque local (`backend/uploads/`) par S3/Supabase Storage dans `backend/src/routes/messages.js` avant le déploiement.
3. **Dépôt de documents depuis le mobile** : ajouter `expo-document-picker` à l'écran Messages (aujourd'hui l'upload se fait depuis le site web).
4. **Déploiement** : backend (Render/Railway/Fly.io), web (Vercel), mobile (EAS Build pour les stores).

## Notes importantes

- Les tarifs sont encodés dans `backend/src/pricing.js` (`PRICING`) selon la grille validée : 3-30 $/session à l'acte, 30-50 $/mois abonnement, 50-200 $ accompagnement mémoires/PFE. La réservation de créneaux valide le prix demandé contre ces bornes.
- Les créneaux durent 1 h : deux sessions d'un même tuteur ne peuvent pas démarrer à moins d'une heure d'écart (contrôle de conflit dans `backend/src/routes/sessions.js`).
- Le webhook de paiement est générique — il faudra un handler dédié par provider une fois leurs accès API obtenus (clés dans `.env`).
