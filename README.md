# Que pense Steve — Des rapports humains sur tes conversations

Application inspirée du modèle de [whatbrandonthinks.com](https://www.whatbrandonthinks.com/fr), **sans logique de paiement**, avec comptes utilisateurs, design façon WhatsApp et un analyste nommé Steve.

## Le concept

Steve lit une conversation exportée (WhatsApp `.txt` ou copier-coller), **mène une analyse approfondie** (chronologie, volumes par personne, temps de réponse, dynamiques, moments-clés) puis rédige un rapport **humain** : drôle, émotif, encourageant quand il le faut — et objectif dans son verdict. Chaque rapport se termine par **les conseils de Steve** : des pistes concrètes pour améliorer la situation analysée.

## Fonctionnalités

- **Comptes utilisateurs** : inscription/connexion ; le premier compte créé (ou l'adresse `ADMIN_EMAIL`) devient propriétaire.
- **Console de gestion** (`/admin`) réservée au propriétaire : liste des comptes, suspension/réactivation (révoque les sessions), suppression d'un compte et de ses données, statistiques.
- **Interface de chat façon WhatsApp** (`/rapport`) : on parle à Steve comme dans une discussion — trombone pour joindre l'export, bulles, indicateur de frappe, rapport rédigé en direct.
- **Espace personnel** (`/mes-rapports`) : relecture des rapports, **téléchargement en PDF** (généré côté client, le rapport ne repart pas vers le serveur), suppression individuelle.
- **« Supprimer mes données »** : efface tous les rapports stockés en un clic (disponible après chaque rapport et dans l'espace personnel). Suppression de compte possible également.
- **Mode duo « Brandon »** (`/roast`) : pour les discussions à **deux** personnes. Le persona « Brandon » (`lib/roast.ts`) mène l'analyse puis renvoie un rapport satirique **JSON structuré** (sortie garantie conforme via `output_config.format`) : titre-métaphore, dossiers de chacun avec pièces à conviction verbatim, teasing. Rendu par le composant `RapportRoast` (aperçu sur `/apercu-roast`), refus explicite des conversations de groupe, sauvegarde, relecture et PDF comme les rapports de Steve.
- **Mode démo** : sans `ANTHROPIC_API_KEY`, un rapport d'exemple est servi pour tester tout le parcours.

## Sécurité

- Mots de passe hachés avec **scrypt** + sel unique par compte (jamais stockés en clair), comparaison en temps constant.
- Sessions à **jeton opaque aléatoire** (32 octets), stocké **haché** en base → révocables, illisibles même en cas de fuite de la base.
- Cookies `HttpOnly`, `SameSite=Lax`, `Secure` en production.
- **Anti-CSRF** : vérification de l'origine sur toutes les mutations.
- **Limitation de débit** : connexion (5/15 min), inscription (5/h), génération (6/h).
- Messages d'erreur de connexion génériques (pas d'énumération de comptes).
- **En-têtes de sécurité** stricts (CSP, X-Frame-Options DENY, nosniff, HSTS, Referrer-Policy, Permissions-Policy).
- Requêtes SQL exclusivement préparées (pas d'injection), validation des entrées côté serveur.
- **Les conversations ne sont jamais stockées** : elles transitent en mémoire le temps de la génération. Seuls les rapports sont conservés, dans l'espace de l'utilisateur, effaçables à tout moment.

## Architecture

- **Next.js 16 (App Router) + TypeScript + Tailwind v4**
- `lib/db.ts` — SQLite (better-sqlite3) : utilisateurs, sessions, rapports
- `lib/auth.ts` — hachage scrypt, sessions, garde CSRF, limitation de débit
- `lib/pdf.ts` — export PDF côté client (jsPDF)
- `lib/whatsapp.ts` — parseur d'exports WhatsApp (Android/iOS/FR)
- `app/api/…` — auth, génération (Claude `claude-opus-4-8`, streaming, effort élevé), rapports, admin
- `components/ChatSteve.tsx` — l'interface de conversation avec Steve

## Lancer le projet

```bash
npm install
export ANTHROPIC_API_KEY=sk-ant-...   # facultatif : sans clé, mode démo
export ADMIN_EMAIL=toi@exemple.fr     # facultatif : cette adresse devient propriétaire
npm run dev
```

Puis ouvrir <http://localhost:3000>. **Le premier compte inscrit devient propriétaire du site.**

## Déploiement

La base SQLite vit dans `donnees/steve.db` : il faut un hébergeur à disque persistant (VPS, Railway, Fly.io…). Sur une plateforme serverless (Vercel), remplacer `lib/db.ts` par un Postgres managé — le reste du code ne change pas. Servir impérativement en HTTPS (les cookies `Secure` l'exigent en production).
