import { requete } from "@/lib/db";
import { utilisateurCourant } from "@/lib/auth";

export async function GET() {
  const u = await utilisateurCourant();
  if (!u || u.role !== "admin") {
    return Response.json({ erreur: "Accès réservé au propriétaire." }, { status: 403 });
  }
  const utilisateurs = await requete(
    `SELECT u.id, u.email, u.nom, u.role, u.statut,
            to_char(u.cree_le AT TIME ZONE 'UTC', 'YYYY-MM-DD"T"HH24:MI:SS') AS cree_le,
            COUNT(r.id)::int AS nb_rapports
     FROM utilisateurs u
     LEFT JOIN rapports r ON r.utilisateur_id = u.id
     GROUP BY u.id ORDER BY u.id ASC`,
  );
  return Response.json({ utilisateurs });
}
