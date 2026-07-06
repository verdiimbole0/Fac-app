# Fac'App — "Ta réussite sur mesure."

Plateforme de tutorat universitaire (TP, préparation aux examens, accompagnement mémoires/PFE) — mobile + web, marché prioritaire RDC.

## Structure du projet

```
facapp/
├── backend/    → API Node.js/Express + Prisma (PostgreSQL)
├── web/        → Site web Next.js (étudiants + tuteurs)
└── mobile/     → App mobile Expo/React Native
```

## Ce qui est déjà en place (v0)

- **Backend** : inscription/connexion (JWT), schéma de base de données complet (étudiants, tuteurs, sessions, abonnements, paiements), route d'initiation de paiement + webhook générique pour Orange Money / Airtel Money / M-Pesa / FONDEKA (stub à brancher sur les vraies API).
- **Web** : page d'accueil + page de connexion connectée à l'API.
- **Mobile** : navigation Login → Home, écran de connexion connecté à l'API.

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

1. **Paiement réel** : intégrer les API/SDK d'Orange Money, Airtel Money, M-Pesa et FONDEKA dans `backend/src/routes/payments.js` (remplacer les TODO). Chaque provider aura sa propre documentation d'intégration et son format de webhook.
2. **Réservation de créneaux** : ajouter les routes backend pour créer/lister/confirmer des `Session`, + écrans mobile/web correspondants.
3. **Messagerie asynchrone** : dépôt de documents et retour écrit (upload de fichiers, stockage S3/Supabase Storage).
4. **Charte d'intégrité académique** : à faire accepter à l'inscription (champ `acceptedIntegrityCharter` à ajouter au modèle `User`).
5. **Sécurisation du token mobile** : remplacer le stockage simple par `expo-secure-store`.
6. **Déploiement** : backend (Render/Railway/Fly.io), web (Vercel), mobile (EAS Build pour les stores).

## Notes importantes

- Les tarifs sont déjà encodés dans `backend/src/routes/payments.js` (`PRICING`) selon la grille validée : 3-30 $/session à l'acte, 30-50 $/mois abonnement, 50-200 $ accompagnement mémoires/PFE.
- Le webhook de paiement est générique — il faudra un handler dédié par provider une fois leurs accès API obtenus (clés dans `.env`).
