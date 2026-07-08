import { db, type Utilisateur } from "@/lib/db";
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

  const base = db();
  const existe = base
    .prepare("SELECT id FROM utilisateurs WHERE email = ?")
    .get(email);
  if (existe) {
    return Response.json(
      { erreur: "Un compte existe déjà avec cette adresse." },
      { status: 409 },
    );
  }

  // Le premier compte créé — ou l'adresse ADMIN_EMAIL — devient propriétaire.
  const nbComptes = (
    base.prepare("SELECT COUNT(*) AS n FROM utilisateurs").get() as { n: number }
  ).n;
  const role =
    nbComptes === 0 ||
    email === (process.env.ADMIN_EMAIL ?? "").trim().toLowerCase()
      ? "admin"
      : "membre";

  const { hash, sel } = hacherMdp(mdp);
  const resultat = base
    .prepare(
      "INSERT INTO utilisateurs (email, nom, mdp_hash, sel, role) VALUES (?, ?, ?, ?, ?)",
    )
    .run(email, nom, hash, sel, role);

  const jeton = creerSession(Number(resultat.lastInsertRowid));
  await poserCookieSession(jeton);

  const u = base
    .prepare("SELECT * FROM utilisateurs WHERE id = ?")
    .get(Number(resultat.lastInsertRowid)) as Utilisateur;
  return Response.json({ nom: u.nom, role: u.role });
}
