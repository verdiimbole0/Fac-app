export interface StatsConversation {
  nbMessages: number;
  participants: { nom: string; nbMessages: number }[];
  premiereDate: string | null;
  derniereDate: string | null;
}

// Formats d'export WhatsApp rencontrés selon la plateforme / la langue :
//   "12/03/2024, 21:47 - Karim: message"        (Android)
//   "[12/03/2024 21:47:03] Karim: message"      (iOS)
//   "12/03/2024 à 21:47 - Karim : message"      (variante FR)
const LIGNE_MESSAGE =
  /^\[?(\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4})[,à\s]+\d{1,2}[:h]\d{2}(?::\d{2})?\]?\s*[-–]?\s*([^:]{1,40})\s?:\s(.*)$/;

const MESSAGES_SYSTEME = [
  "Les messages et les appels sont chiffrés",
  "a créé le groupe",
  "a ajouté",
  "a quitté",
  "a changé",
  "Vous avez rejoint",
  "<Médias omis>",
  "image absente",
];

export function analyserConversation(texte: string): StatsConversation {
  const compteurs = new Map<string, number>();
  let nbMessages = 0;
  let premiereDate: string | null = null;
  let derniereDate: string | null = null;

  for (const ligne of texte.split("\n")) {
    const m = ligne.match(LIGNE_MESSAGE);
    if (!m) continue;
    const [, date, auteurBrut, contenu] = m;
    const auteur = auteurBrut.trim();
    if (MESSAGES_SYSTEME.some((s) => contenu.includes(s) || auteur.includes(s)))
      continue;
    nbMessages += 1;
    compteurs.set(auteur, (compteurs.get(auteur) ?? 0) + 1);
    if (!premiereDate) premiereDate = date;
    derniereDate = date;
  }

  const participants = [...compteurs.entries()]
    .map(([nom, n]) => ({ nom, nbMessages: n }))
    .sort((a, b) => b.nbMessages - a.nbMessages);

  return { nbMessages, participants, premiereDate, derniereDate };
}
