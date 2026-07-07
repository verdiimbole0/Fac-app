# Que pense Bertrand — Des rapports IA sur tes conversations

Clone fonctionnel du modèle de [whatbrandonthinks.com](https://www.whatbrandonthinks.com/fr) (« Que pense Brandon »), **sans aucune logique de paiement**.

## Analyse du modèle original

**Concept.** Un personnage IA (« Brandon ») lit une conversation exportée (WhatsApp / iMessage) et rédige un rapport humoristique et sans filtre : dynamiques du groupe, rôles de chacun, private jokes, superlatifs, verdict. Produit viral pensé pour le partage (TikTok / Instagram).

**Parcours utilisateur.**
1. L'utilisateur exporte sa conversation (~2 min de son côté) ;
2. il l'envoie au service ;
3. l'IA lit tous les messages et rédige le rapport en quelques minutes ;
4. le rapport lui est livré (sur le site original : par WhatsApp ou e-mail, après paiement à l'unité).

**Promesses clés reprises ici.** Tout type de conversation (potes, couple, famille, boulot, situationship — « plus c'est le bazar, mieux c'est »), confidentialité (conversation jamais stockée, jamais utilisée pour l'entraînement), rapport rédigé par Claude (Anthropic).

**Écarts volontaires.** Pas de paiement (demandé), pas de livraison WhatsApp/e-mail (le rapport s'affiche en streaming dans le navigateur), personnage renommé « Bertrand » et design original.

## Architecture

- **Next.js 16 (App Router) + TypeScript + Tailwind v4**
- `app/page.tsx` — landing page (hero, types de conversations, comment ça marche, contenu du rapport, confidentialité, FAQ)
- `app/rapport/page.tsx` — flux de génération : dépôt d'un export `.txt` ou collage du texte, choix du type de conversation, aperçu de statistiques (parseur d'export WhatsApp), affichage du rapport en streaming (markdown)
- `app/api/rapport/route.ts` — appelle l'API Claude (`claude-opus-4-8`, thinking adaptatif, streaming) avec le persona Bertrand et renvoie le texte en flux ; garde-fous sur la taille (refus explicite au-delà de 400 000 caractères, jamais de troncature silencieuse)
- `lib/whatsapp.ts` — parseur des formats d'export WhatsApp (Android / iOS / FR)
- `lib/demo.ts` — rapport de démonstration servi quand aucune clé API n'est configurée

**Confidentialité par construction :** la conversation transite uniquement en mémoire (requête → API Claude → flux de réponse). Aucune base de données, aucun stockage.

## Lancer le projet

```bash
npm install
export ANTHROPIC_API_KEY=sk-ant-...   # facultatif : sans clé, l'app sert un rapport de démo
npm run dev
```

Puis ouvrir <http://localhost:3000>.

## Mode démo

Sans `ANTHROPIC_API_KEY`, l'API renvoie un rapport d'exemple (streamé) précédé d'un bandeau « Mode démo », ce qui permet de tester tout le parcours sans clé.
