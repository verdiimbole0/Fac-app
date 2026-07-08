import { db, type Rapport } from "@/lib/db";
import { origineValide, utilisateurCourant } from "@/lib/auth";

export async function GET() {
  const u = await utilisateurCourant();
  if (!u) return Response.json({ erreur: "Non connecté." }, { status: 401 });
  const rapports = db()
    .prepare(
      "SELECT id, titre, type, cree_le FROM rapports WHERE utilisateur_id = ? ORDER BY id DESC",
    )
    .all(u.id) as Pick<Rapport, "id" | "titre" | "type" | "cree_le">[];
  return Response.json({ rapports });
}

// « Supprimer mes données » : efface tous les rapports stockés de l'utilisateur.
export async function DELETE() {
  if (!(await origineValide())) {
    return Response.json({ erreur: "Origine non autorisée." }, { status: 403 });
  }
  const u = await utilisateurCourant();
  if (!u) return Response.json({ erreur: "Non connecté." }, { status: 401 });
  const resultat = db()
    .prepare("DELETE FROM rapports WHERE utilisateur_id = ?")
    .run(u.id);
  return Response.json({ supprimes: resultat.changes });
}
