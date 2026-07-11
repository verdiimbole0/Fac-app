import { requete, type Rapport } from "@/lib/db";
import { origineValide, utilisateurCourant } from "@/lib/auth";

type Params = { params: Promise<{ id: string }> };

function identifiant(brut: string): number | null {
  const n = Number(brut);
  return Number.isInteger(n) && n > 0 ? n : null;
}

export async function GET(_req: Request, { params }: Params) {
  const u = await utilisateurCourant();
  if (!u) return Response.json({ erreur: "Non connecté." }, { status: 401 });
  const id = identifiant((await params).id);
  if (!id) {
    return Response.json({ erreur: "Rapport introuvable." }, { status: 404 });
  }
  const [rapport] = await requete<Rapport>(
    "SELECT * FROM rapports WHERE id = $1 AND utilisateur_id = $2",
    [id, u.id],
  );
  if (!rapport) {
    return Response.json({ erreur: "Rapport introuvable." }, { status: 404 });
  }
  return Response.json({ rapport });
}

export async function DELETE(_req: Request, { params }: Params) {
  if (!(await origineValide())) {
    return Response.json({ erreur: "Origine non autorisée." }, { status: 403 });
  }
  const u = await utilisateurCourant();
  if (!u) return Response.json({ erreur: "Non connecté." }, { status: 401 });
  const id = identifiant((await params).id);
  if (!id) {
    return Response.json({ erreur: "Rapport introuvable." }, { status: 404 });
  }
  const supprimes = await requete(
    "DELETE FROM rapports WHERE id = $1 AND utilisateur_id = $2 RETURNING id",
    [id, u.id],
  );
  if (supprimes.length === 0) {
    return Response.json({ erreur: "Rapport introuvable." }, { status: 404 });
  }
  return Response.json({ ok: true });
}
