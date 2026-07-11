import { requete, type Utilisateur } from "@/lib/db";
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

function identifiant(brut: string): number | null {
  const n = Number(brut);
  return Number.isInteger(n) && n > 0 ? n : null;
}

// Suspendre / réactiver / changer le rôle d'un compte.
export async function PATCH(req: Request, { params }: Params) {
  const garde = await verifierAdmin();
  if (!garde.ok) return garde.reponse;
  const cibleId = identifiant((await params).id);
  if (!cibleId) {
    return Response.json({ erreur: "Compte introuvable." }, { status: 404 });
  }

  let corps: { statut?: string; role?: string };
  try {
    corps = await req.json();
  } catch {
    return Response.json({ erreur: "Requête invalide." }, { status: 400 });
  }

  const [cible] = await requete<Utilisateur>(
    "SELECT * FROM utilisateurs WHERE id = $1",
    [cibleId],
  );
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
    await requete("UPDATE utilisateurs SET statut = $1 WHERE id = $2", [
      corps.statut,
      cibleId,
    ]);
    if (corps.statut === "suspendu") {
      await requete("DELETE FROM sessions WHERE utilisateur_id = $1", [cibleId]);
    }
  }
  if (corps.role === "admin" || corps.role === "membre") {
    await requete("UPDATE utilisateurs SET role = $1 WHERE id = $2", [
      corps.role,
      cibleId,
    ]);
  }
  return Response.json({ ok: true });
}

// Suppression d'un compte et de toutes ses données (rapports, sessions).
export async function DELETE(_req: Request, { params }: Params) {
  const garde = await verifierAdmin();
  if (!garde.ok) return garde.reponse;
  const cibleId = identifiant((await params).id);
  if (!cibleId) {
    return Response.json({ erreur: "Compte introuvable." }, { status: 404 });
  }
  if (cibleId === garde.admin.id) {
    return Response.json(
      { erreur: "Tu ne peux pas supprimer ton propre compte ici." },
      { status: 400 },
    );
  }
  const supprimes = await requete(
    "DELETE FROM utilisateurs WHERE id = $1 RETURNING id",
    [cibleId],
  );
  if (supprimes.length === 0) {
    return Response.json({ erreur: "Compte introuvable." }, { status: 404 });
  }
  return Response.json({ ok: true });
}
