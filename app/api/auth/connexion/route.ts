import { db, type Utilisateur } from "@/lib/db";
import {
  creerSession,
  ipClient,
  limiteDebit,
  origineValide,
  poserCookieSession,
  verifierMdp,
} from "@/lib/auth";

const ERREUR_GENERIQUE = "E-mail ou mot de passe incorrect.";

export async function POST(req: Request) {
  if (!(await origineValide())) {
    return Response.json({ erreur: "Origine non autorisée." }, { status: 403 });
  }

  let corps: { email?: string; mdp?: string };
  try {
    corps = await req.json();
  } catch {
    return Response.json({ erreur: "Requête invalide." }, { status: 400 });
  }

  const email = (corps.email ?? "").trim().toLowerCase();
  const mdp = corps.mdp ?? "";
  if (!email || !mdp) {
    return Response.json({ erreur: ERREUR_GENERIQUE }, { status: 400 });
  }

  if (!limiteDebit(`connexion:${await ipClient()}:${email}`, 5, 900_000)) {
    return Response.json(
      { erreur: "Trop de tentatives. Réessaie dans 15 minutes." },
      { status: 429 },
    );
  }

  const u = db()
    .prepare("SELECT * FROM utilisateurs WHERE email = ?")
    .get(email) as Utilisateur | undefined;

  // Message identique que le compte existe ou non : pas d'énumération.
  if (!u || !verifierMdp(mdp, u.mdp_hash, u.sel)) {
    return Response.json({ erreur: ERREUR_GENERIQUE }, { status: 401 });
  }
  if (u.statut === "suspendu") {
    return Response.json(
      { erreur: "Ce compte est suspendu. Contacte le propriétaire du site." },
      { status: 403 },
    );
  }

  const jeton = creerSession(u.id);
  await poserCookieSession(jeton);
  return Response.json({ nom: u.nom, role: u.role });
}
