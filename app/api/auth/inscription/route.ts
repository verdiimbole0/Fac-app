import { requete } from "@/lib/db";
import {
  creerSession,
  hacherMdp,
  ipClient,
  limiteDebit,
  origineValide,
  poserCookieSession,
  validerInscription,
} from "@/lib/auth";

export async function POST(req: Request) {
  if (!(await origineValide())) {
    return Response.json({ erreur: "Origine non autorisée." }, { status: 403 });
  }
  if (!limiteDebit(`inscription:${await ipClient()}`, 5, 3600_000)) {
    return Response.json(
      { erreur: "Trop de tentatives. Réessaie dans une heure." },
      { status: 429 },
    );
  }

  let corps: { email?: string; nom?: string; mdp?: string };
  try {
    corps = await req.json();
  } catch {
    return Response.json({ erreur: "Requête invalide." }, { status: 400 });
  }

  const email = (corps.email ?? "").trim().toLowerCase();
  const nom = (corps.nom ?? "").trim();
  const mdp = corps.mdp ?? "";

  const probleme = validerInscription(email, nom, mdp);
  if (probleme) return Response.json({ erreur: probleme }, { status: 400 });

  const existe = await requete("SELECT id FROM utilisateurs WHERE email = $1", [
    email,
  ]);
  if (existe.length > 0) {
    return Response.json(
      { erreur: "Un compte existe déjà avec cette adresse." },
      { status: 409 },
    );
  }

  // Le premier compte créé — ou l'adresse ADMIN_EMAIL — devient propriétaire.
  const [{ n: nbComptes }] = await requete<{ n: number }>(
    "SELECT COUNT(*)::int AS n FROM utilisateurs",
  );
  const role =
    nbComptes === 0 ||
    email === (process.env.ADMIN_EMAIL ?? "").trim().toLowerCase()
      ? "admin"
      : "membre";

  const { hash, sel } = hacherMdp(mdp);
  const [cree] = await requete<{ id: number; nom: string; role: string }>(
    `INSERT INTO utilisateurs (email, nom, mdp_hash, sel, role)
     VALUES ($1, $2, $3, $4, $5) RETURNING id, nom, role`,
    [email, nom, hash, sel, role],
  );

  const jeton = await creerSession(cree.id);
  await poserCookieSession(jeton);
  return Response.json({ nom: cree.nom, role: cree.role });
}
