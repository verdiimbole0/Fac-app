import Anthropic from "@anthropic-ai/sdk";
import {
  PROMPT_BRANDON,
  RAPPORT_ROAST_DEMO,
  SCHEMA_RAPPORT_ROAST,
  type RapportRoastData,
} from "@/lib/roast";
import { analyserConversation } from "@/lib/whatsapp";
import { requete } from "@/lib/db";
import {
  ipClient,
  limiteDebit,
  origineValide,
  utilisateurCourant,
} from "@/lib/auth";

export const maxDuration = 300;

const MAX_CARACTERES = 400_000;
const MIN_CARACTERES = 200;

async function sauvegarder(utilisateurId: number, rapport: RapportRoastData) {
  await requete(
    "INSERT INTO rapports (utilisateur_id, titre, type, contenu) VALUES ($1, $2, $3, $4)",
    [utilisateurId, rapport.titre.slice(0, 120), "roast", JSON.stringify(rapport)],
  );
}

export async function POST(req: Request) {
  if (!(await origineValide())) {
    return Response.json({ erreur: "Origine non autorisée." }, { status: 403 });
  }
  const utilisateur = await utilisateurCourant();
  if (!utilisateur) {
    return Response.json(
      { erreur: "Connecte-toi pour envoyer une conversation à Brandon." },
      { status: 401 },
    );
  }
  if (!limiteDebit(`roast:${utilisateur.id}:${await ipClient()}`, 6, 3600_000)) {
    return Response.json(
      { erreur: "Brandon fume une cigarette : 6 rapports max par heure." },
      { status: 429 },
    );
  }

  let corps: { conversation?: string };
  try {
    corps = await req.json();
  } catch {
    return Response.json({ erreur: "Corps de requête invalide." }, { status: 400 });
  }

  const conversation = (corps.conversation ?? "").trim();
  if (conversation.length < MIN_CARACTERES) {
    return Response.json(
      {
        erreur:
          "Conversation trop courte : Brandon a besoin de matière pour instruire le dossier.",
      },
      { status: 400 },
    );
  }
  if (conversation.length > MAX_CARACTERES) {
    return Response.json(
      {
        erreur: `Conversation trop longue (maximum ${MAX_CARACTERES.toLocaleString("fr-FR")} caractères). Exporte une période plus courte.`,
      },
      { status: 413 },
    );
  }

  // Le mode duo exige une discussion à deux : on vérifie avant de payer un appel.
  const stats = analyserConversation(conversation);
  if (stats.nbMessages < 10 || stats.participants.length < 2) {
    return Response.json(
      {
        erreur:
          "Brandon n'a pas reconnu une discussion à deux personnes. Exporte une conversation privée WhatsApp (pas un groupe) au format .txt.",
      },
      { status: 400 },
    );
  }
  if (stats.participants.length > 2) {
    return Response.json(
      {
        erreur: `Brandon instruit des dossiers en tête-à-tête, et il a détecté ${stats.participants.length} personnes. Exporte une discussion à deux, pas un groupe.`,
      },
      { status: 400 },
    );
  }

  if (!process.env.ANTHROPIC_API_KEY) {
    await new Promise((r) => setTimeout(r, 1200));
    await sauvegarder(utilisateur.id, RAPPORT_ROAST_DEMO);
    return Response.json({ rapport: RAPPORT_ROAST_DEMO, demo: true });
  }

  const client = new Anthropic();
  const contexte = [
    `Les deux protagonistes détectés : ${stats.participants
      .map((p) => `${p.nom} (${p.nbMessages} messages)`)
      .join(" et ")}. Période : ${stats.premiereDate ?? "?"} → ${stats.derniereDate ?? "?"}.`,
    "Voici la conversation exportée, telle quelle :",
    "<conversation>",
    conversation,
    "</conversation>",
    "Mène ta méthode d'analyse, puis produis le rapport JSON de Brandon.",
  ].join("\n\n");

  const flux = client.messages.stream({
    model: "claude-opus-4-8",
    max_tokens: 8000,
    thinking: { type: "adaptive" },
    output_config: { effort: "high", format: SCHEMA_RAPPORT_ROAST },
    system: PROMPT_BRANDON,
    messages: [{ role: "user", content: contexte }],
  });

  try {
    const final = await flux.finalMessage();
    if (final.stop_reason === "refusal") {
      return Response.json(
        { erreur: "Brandon préfère ne pas commenter cette conversation." },
        { status: 422 },
      );
    }
    const texte = final.content.find((b) => b.type === "text");
    if (!texte || texte.type !== "text") {
      throw new Error("Réponse sans contenu textuel.");
    }
    const rapport = JSON.parse(texte.text) as RapportRoastData;
    await sauvegarder(utilisateur.id, rapport);
    return Response.json({ rapport });
  } catch (e) {
    console.error("roast:", e);
    return Response.json(
      { erreur: "Brandon a renversé son café. Réessaie dans un instant." },
      { status: 502 },
    );
  }
}
