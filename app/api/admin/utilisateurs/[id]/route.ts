import { db, type Utilisateur } from "@/lib/db";
import { origineValide, utilisateurCourant } from "@/lib/auth";

type Params = { params: Promise<{ id: string }> };

async function verifierAdmin(): Promise<
  { ok: true; admin: Utilisateur } | { ok: false; reponse: Response }
> {
  if (!(await origineValide())) {
    return {
      ok: false,
      reponse: Response.json({ erreur: "Origine non autorisée." }, { status: 403 }),
    };
  }
  const u = await utilisateurCourant();
  if (!u || u.role !== "admin") {
    return {
      ok: false,
      reponse: Response.json(
        { erreur: "Accès réservé au propriétaire." },
        { status: 403 },
      ),
    };
  }
  return { ok: true, admin: u };
}

// Suspendre / réactiver / changer le rôle d'un compte.
export async function PATCH(req: Request, { params }: Params) {
  const garde = await verifierAdmin();
  if (!garde.ok) return garde.reponse;
  const { id } = await params;
  const cibleId = Number(id);

  let corps: { statut?: string; role?: string };
  try {
    corps = await req.json();
  } catch {
    return Response.json({ erreur: "Requête invalide." }, { status: 400 });
  }

  const base = db();
  const cible = base
    .prepare("SELECT * FROM utilisateurs WHERE id = ?")
    .get(cibleId) as Utilisateur | undefined;
  if (!cible) {
    return Response.json({ erreur: "Compte introuvable." }, { status: 404 });
  }
  if (cible.id === garde.admin.id) {
    return Response.json(
      { erreur: "Tu ne peux pas modifier ton propre compte ici." },
      { status: 400 },
    );
  }

  if (corps.statut === "actif" || corps.statut === "suspendu") {
    base
      .prepare("UPDATE utilisateurs SET statut = ? WHERE id = ?")
      .run(corps.statut, cibleId);
    if (corps.statut === "suspendu") {
      base.prepare("DELETE FROM sessions WHERE utilisateur_id = ?").run(cibleId);
    }
  }
  if (corps.role === "admin" || corps.role === "membre") {
    base
      .prepare("UPDATE utilisateurs SET role = ? WHERE id = ?")
      .run(corps.role, cibleId);
  }
  return Response.json({ ok: true });
}

// Suppression d'un compte et de toutes ses données (rapports, sessions).
export async function DELETE(_req: Request, { params }: Params) {
  const garde = await verifierAdmin();
  if (!garde.ok) return garde.reponse;
  const { id } = await params;
  const cibleId = Number(id);
  if (cibleId === garde.admin.id) {
    return Response.json(
      { erreur: "Tu ne peux pas supprimer ton propre compte ici." },
      { status: 400 },
    );
  }
  const resultat = db()
    .prepare("DELETE FROM utilisateurs WHERE id = ?")
    .run(cibleId);
  if (resultat.changes === 0) {
    return Response.json({ erreur: "Compte introuvable." }, { status: 404 });
  }
  return Response.json({ ok: true });
}
