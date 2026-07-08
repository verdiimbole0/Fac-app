import { db } from "@/lib/db";
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
  const base = db();
  const admins = (
    base
      .prepare(
        "SELECT COUNT(*) AS n FROM utilisateurs WHERE role = 'admin' AND id != ?",
      )
      .get(u.id) as { n: number }
  ).n;
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
  base.prepare("DELETE FROM utilisateurs WHERE id = ?").run(u.id);
  return Response.json({ ok: true });
}
