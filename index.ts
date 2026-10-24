// Exemple Higgsfield : génération texte → vidéo avec Seedance 2.5.
// Lancer avec : npm run higgsfield:exemple
// Les identifiants sont lus côté serveur depuis .env.local (HF_CREDENTIALS=key-id:key-secret).
import { existsSync } from "node:fs";
import {
  APIError,
  AuthenticationError,
  BadInputError,
  CredentialsMissedError,
  NotEnoughCreditsError,
  TimeoutError,
  ValidationError,
  createHiggsfieldClient,
} from "@higgsfield/client/v2";

const MODELE = "bytedance/seedance-2.5/text-to-video";

if (existsSync(".env.local")) process.loadEnvFile(".env.local");

async function main(): Promise<number> {
  const credentials = process.env.HF_CREDENTIALS;
  if (!credentials) {
    console.error("HF_CREDENTIALS est absent : ajoutez-le dans .env.local (format key-id:key-secret).");
    return 1;
  }

  const client = createHiggsfieldClient({
    credentials,
    // La génération vidéo peut dépasser les 5 minutes d'attente par défaut du SDK.
    maxPollTime: 15 * 60 * 1000,
  });

  const reponse = await client.subscribe(MODELE, {
    input: {
      prompt: "A cinematic scene at sunset",
      duration: 5,
      resolution: "720p",
      aspect_ratio: "16:9",
    },
    withPolling: true,
  });

  // Le SDK type le statut sans « canceled », mais l'API peut le renvoyer.
  const statut: string = reponse.status;
  switch (statut) {
    case "completed": {
      const url = reponse.video?.url;
      if (!url) {
        console.error(`Requête ${reponse.request_id} terminée, mais aucune URL de vidéo n'a été renvoyée.`);
        return 1;
      }
      console.log(`Vidéo générée : ${url}`);
      return 0;
    }
    case "nsfw":
      console.error(`Requête ${reponse.request_id} refusée par la modération (crédits remboursés).`);
      return 1;
    case "failed":
      console.error(`Requête ${reponse.request_id} échouée (crédits remboursés).`);
      return 1;
    case "canceled":
      console.error(`Requête ${reponse.request_id} annulée.`);
      return 1;
    default:
      console.error(`Requête ${reponse.request_id} terminée avec un statut inattendu : ${statut}.`);
      return 1;
  }
}

main()
  .then((code) => {
    process.exitCode = code;
  })
  .catch((erreur: unknown) => {
    if (erreur instanceof CredentialsMissedError || erreur instanceof AuthenticationError) {
      console.error("Authentification refusée : vérifiez HF_CREDENTIALS dans .env.local.");
    } else if (erreur instanceof NotEnoughCreditsError) {
      // Le SDK convertit tout HTTP 403 en NotEnoughCreditsError, y compris un refus de proxy.
      console.error("Accès refusé (403) : crédits Higgsfield insuffisants, ou api.higgsfield.ai bloqué par le réseau.");
    } else if (erreur instanceof BadInputError || erreur instanceof ValidationError) {
      console.error(`Paramètres refusés : ${erreur.message}`);
    } else if (erreur instanceof TimeoutError) {
      // Le SDK n'arrête pas l'attente sur une annulation : elle finit en dépassement de délai.
      console.error(`Aucun résultat final dans le délai imparti (requête annulée ou trop longue) : ${erreur.message}`);
    } else if (erreur instanceof APIError) {
      console.error(`Erreur API Higgsfield (${erreur.statusCode}) : ${erreur.message}`);
    } else {
      console.error("Erreur inattendue :", erreur instanceof Error ? erreur.message : erreur);
    }
    process.exitCode = 1;
  });
