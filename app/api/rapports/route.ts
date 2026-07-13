import { COL_CREE_LE, requete, type Rapport } from "@/lib/db";
import { origineValide, utilisateurCourant } from "@/lib/auth";

export async function GET() {
  const u = await utilisateurCourant();
  if (!u) return Response.json({ erreur: "Non connecté." }, { status: 401 });
  const rapports = await requete<
    Pick<Rapport, "id" | "titre" | "type" | "cree_le">
  >(
    `SELECT id, titre, type, ${COL_CREE_LE}
     FROM rapports WHERE utilisateur_id = $1 ORDER BY id DESC`,
    [u.id],
  );
  return Response.json({ rapports });
}

// « Supprimer mes données » : efface tous les rapports stockés de l'utilisateur.
export async function DELETE() {
  if (!(await origineValide())) {
    return Response.json({ erreur: "Origine non autorisée." }, { status: 403 });
  }
  const u = await utilisateurCourant();
  if (!u) return Response.json({ erreur: "Non connecté." }, { status: 401 });
  const supprimes = await requete(
    "DELETE FROM rapports WHERE utilisateur_id = $1 RETURNING id",
    [u.id],
  );
  return Response.json({ supprimes: supprimes.length });
}
