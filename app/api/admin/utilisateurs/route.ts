import { db } from "@/lib/db";
import { utilisateurCourant } from "@/lib/auth";

export async function GET() {
  const u = await utilisateurCourant();
  if (!u || u.role !== "admin") {
    return Response.json({ erreur: "Accès réservé au propriétaire." }, { status: 403 });
  }
  const utilisateurs = db()
    .prepare(
      `SELECT u.id, u.email, u.nom, u.role, u.statut, u.cree_le,
              COUNT(r.id) AS nb_rapports
       FROM utilisateurs u
       LEFT JOIN rapports r ON r.utilisateur_id = u.id
       GROUP BY u.id ORDER BY u.id ASC`,
    )
    .all();
  return Response.json({ utilisateurs });
}
