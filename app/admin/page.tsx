import { redirect } from "next/navigation";
import EnTete from "@/components/EnTete";
import TableauUtilisateurs, {
  type LigneUtilisateur,
} from "@/components/TableauUtilisateurs";
import { utilisateurCourant } from "@/lib/auth";
import { requete } from "@/lib/db";

export const dynamic = "force-dynamic";

export default async function PageAdmin() {
  const u = await utilisateurCourant();
  if (!u) redirect("/connexion");
  if (u.role !== "admin") redirect("/rapport");

  const utilisateurs = await requete<LigneUtilisateur>(
    `SELECT u.id, u.email, u.nom, u.role, u.statut,
            to_char(u.cree_le AT TIME ZONE 'UTC', 'YYYY-MM-DD"T"HH24:MI:SS') AS cree_le,
            COUNT(r.id)::int AS nb_rapports
     FROM utilisateurs u
     LEFT JOIN rapports r ON r.utilisateur_id = u.id
     GROUP BY u.id ORDER BY u.id ASC`,
  );

  const actifs = utilisateurs.filter((x) => x.statut === "actif").length;
  const totalRapports = utilisateurs.reduce((s, x) => s + x.nb_rapports, 0);

  return (
    <main className="flex flex-1 flex-col">
      <EnTete />
      <div className="papier-peint flex-1 py-10">
        <div className="mx-auto max-w-4xl px-5">
          <h1 className="text-2xl font-extrabold text-teal">
            Gestion du site
          </h1>
          <p className="mt-1 text-sm text-gris">
            Espace réservé au propriétaire : comptes, statuts, suppressions.
          </p>

          <div className="mt-6 grid gap-4 sm:grid-cols-3">
            {[
              [String(utilisateurs.length), "comptes au total"],
              [String(actifs), "comptes actifs"],
              [String(totalRapports), "rapports générés"],
            ].map(([n, l]) => (
              <div key={l} className="carte p-5 text-center">
                <p className="text-3xl font-extrabold text-teal">{n}</p>
                <p className="mt-1 text-xs uppercase tracking-wide text-gris">
                  {l}
                </p>
              </div>
            ))}
          </div>

          <div className="mt-8">
            <TableauUtilisateurs utilisateurs={utilisateurs} monId={u.id} />
          </div>

          <p className="mt-6 text-xs text-gris">
            Suspendre un compte révoque immédiatement toutes ses sessions.
            Supprimer un compte efface aussi tous ses rapports. Les
            conversations, elles, ne sont jamais stockées.
          </p>
        </div>
      </div>
    </main>
  );
}
