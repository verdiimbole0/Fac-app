import { db, type Rapport } from "@/lib/db";
import { origineValide, utilisateurCourant } from "@/lib/auth";

type Params = { params: Promise<{ id: string }> };

export async function GET(_req: Request, { params }: Params) {
  const u = await utilisateurCourant();
  if (!u) return Response.json({ erreur: "Non connecté." }, { status: 401 });
  const { id } = await params;
  const rapport = db()
    .prepare("SELECT * FROM rapports WHERE id = ? AND utilisateur_id = ?")
    .get(Number(id), u.id) as Rapport | undefined;
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
  const { id } = await params;
  const resultat = db()
    .prepare("DELETE FROM rapports WHERE id = ? AND utilisateur_id = ?")
    .run(Number(id), u.id);
  if (resultat.changes === 0) {
    return Response.json({ erreur: "Rapport introuvable." }, { status: 404 });
  }
  return Response.json({ ok: true });
}
