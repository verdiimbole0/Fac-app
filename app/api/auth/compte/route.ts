import { requete } from "@/lib/db";
import {
  detruireSession,
  origineValide,
  utilisateurCourant,
} from "@/lib/auth";

// Suppression totale du compte : rapports, sessions et profil (RGPD).
export async function DELETE() {
  if (!(await origineValide())) {
    return Response.json({ erreur: "Origine non autorisée." }, { status: 403 });
  }
  const u = await utilisateurCourant();
  if (!u) {
    return Response.json({ erreur: "Non connecté." }, { status: 401 });
  }
  const [{ n: admins }] = await requete<{ n: number }>(
    "SELECT COUNT(*)::int AS n FROM utilisateurs WHERE role = 'admin' AND id != $1",
    [u.id],
  );
  if (u.role === "admin" && admins === 0) {
    return Response.json(
      {
        erreur:
          "Tu es le seul compte propriétaire : nomme un autre propriétaire avant de supprimer ce compte.",
      },
      { status: 400 },
    );
  }
  await detruireSession();
  await requete("DELETE FROM utilisateurs WHERE id = $1", [u.id]);
  return Response.json({ ok: true });
}
