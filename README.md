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
- **Messagerie asynchrone** : fil de discussion par session (`GET|POST /api/sessions/:id/messages`), dépôt de documents en multipart (20 Mo max) et téléchargement (`GET /api/sessions/:id/messages/:messageId/file`), accessible uniquement aux participants. Stockage configurable (`backend/src/storage.js`) : disque local par défaut, ou tout service compatible S3 (AWS S3, Supabase Storage, Cloudflare R2...) via `STORAGE_DRIVER=s3` + variables `S3_*`.
- **Charte d'intégrité académique** : acceptation obligatoire à l'inscription (`acceptedIntegrityCharter`), affichée sur les formulaires web et mobile.
- **Web** : page d'accueil, inscription (avec charte), connexion, page `/sessions` (réservation, confirmation/annulation/clôture, paiement d'une session confirmée) et fil de discussion `/sessions/[id]` avec dépôt et téléchargement de documents.
- **Mobile** : inscription (avec charte) et connexion (token stocké via `expo-secure-store`, reconnexion automatique), écrans « Choisir un tuteur », « Réserver un créneau », « Mes sessions », paiement d'une session confirmée et messagerie par session (texte + dépôt de documents via `expo-document-picker`).
- **Prêt pour le déploiement** : migrations Prisma versionnées (`backend/prisma/migrations/`), `Dockerfile` backend, blueprint Render (`render.yaml`), CORS configurable (`CORS_ORIGIN`), config Expo/EAS (`mobile/app.json`, `mobile/eas.json`), URL de l'API configurable partout (`NEXT_PUBLIC_API_URL` web, `EXPO_PUBLIC_API_URL` mobile).

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

## Déploiement

### Backend + base de données (Render)
Le blueprint `render.yaml` crée l'API et la base PostgreSQL en un clic : sur
[Render](https://render.com), « New → Blueprint » en pointant ce dépôt. Ensuite :
- renseigner `CORS_ORIGIN` avec l'URL du site (ex. `https://facapp.vercel.app`) ;
- pour un stockage de documents persistant, passer `STORAGE_DRIVER=s3` et renseigner
  les variables `S3_*` (bucket S3, Supabase Storage ou Cloudflare R2) — le disque
  local de Render est éphémère ;
- un `Dockerfile` est aussi fourni dans `backend/` pour Railway, Fly.io ou tout hébergeur Docker.

### Web (Vercel)
Importer le dépôt sur [Vercel](https://vercel.com) avec `web/` comme *Root Directory*,
et définir la variable `NEXT_PUBLIC_API_URL` avec l'URL de l'API déployée.

### Mobile (EAS Build)
```bash
cd mobile
npx eas login
npx eas build --profile preview --platform android   # APK de test
npx eas build --profile production                    # builds pour les stores
```
L'URL de l'API se règle dans `eas.json` (variable `EXPO_PUBLIC_API_URL` de chaque profil).

## Prochaines étapes de développement

1. **Paiement réel** : intégrer les API/SDK d'Orange Money, Airtel Money, M-Pesa et FONDEKA dans `backend/src/routes/payments.js` (remplacer les TODO) — en attente des accès API des opérateurs. Chaque provider aura sa propre documentation d'intégration et son format de webhook.
2. **Mise en production** : créer les comptes Render/Vercel/Expo et dérouler la section « Déploiement » ci-dessus (tout est prêt côté code).
3. **Téléchargement des documents depuis le mobile** : ouvrir/télécharger les pièces jointes dans l'app (`expo-file-system` + `expo-sharing`) — l'envoi mobile fonctionne déjà, la lecture se fait sur le web.

## Notes importantes

- Les tarifs sont encodés dans `backend/src/pricing.js` (`PRICING`) selon la grille validée : 3-30 $/session à l'acte, 30-50 $/mois abonnement, 50-200 $ accompagnement mémoires/PFE. La réservation de créneaux valide le prix demandé contre ces bornes.
- Les créneaux durent 1 h : deux sessions d'un même tuteur ne peuvent pas démarrer à moins d'une heure d'écart (contrôle de conflit dans `backend/src/routes/sessions.js`).
- Le webhook de paiement est générique — il faudra un handler dédié par provider une fois leurs accès API obtenus (clés dans `.env`).
