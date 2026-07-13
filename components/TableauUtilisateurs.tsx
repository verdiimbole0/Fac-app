"use client";

import { useRouter } from "next/navigation";

export interface LigneUtilisateur {
  id: number;
  email: string;
  nom: string;
  role: "admin" | "membre";
  statut: "actif" | "suspendu";
  cree_le: string;
  nb_rapports: number;
}

export default function TableauUtilisateurs({
  utilisateurs,
  monId,
}: {
  utilisateurs: LigneUtilisateur[];
  monId: number;
}) {
  const router = useRouter();

  async function patcher(id: number, corps: object) {
    const reponse = await fetch(`/api/admin/utilisateurs/${id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(corps),
    });
    if (!reponse.ok) {
      const c = await reponse.json().catch(() => null);
      window.alert(c?.erreur ?? "Action impossible.");
    }
    router.refresh();
  }

  async function supprimer(id: number, email: string) {
    if (
      !window.confirm(
        `Supprimer le compte ${email} et toutes ses données (rapports, sessions) ? Action irréversible.`,
      )
    )
      return;
    const reponse = await fetch(`/api/admin/utilisateurs/${id}`, {
      method: "DELETE",
    });
    if (!reponse.ok) {
      const c = await reponse.json().catch(() => null);
      window.alert(c?.erreur ?? "Suppression impossible.");
    }
    router.refresh();
  }

  return (
    <div className="carte overflow-x-auto">
      <table className="w-full min-w-[640px] text-sm">
        <thead>
          <tr className="border-b border-ligne text-left text-xs uppercase tracking-wide text-gris">
            <th className="px-4 py-3">Membre</th>
            <th className="px-4 py-3">Rôle</th>
            <th className="px-4 py-3">Statut</th>
            <th className="px-4 py-3">Rapports</th>
            <th className="px-4 py-3">Inscrit le</th>
            <th className="px-4 py-3 text-right">Actions</th>
          </tr>
        </thead>
        <tbody>
          {utilisateurs.map((u) => (
            <tr key={u.id} className="border-b border-ligne last:border-0">
              <td className="px-4 py-3">
                <p className="font-bold text-encre">
                  {u.nom}
                  {u.id === monId && (
                    <span className="ml-2 text-xs font-normal text-gris">
                      (toi)
                    </span>
                  )}
                </p>
                <p className="text-xs text-gris">{u.email}</p>
              </td>
              <td className="px-4 py-3">
                <span
                  className={`rounded-full px-2.5 py-1 text-xs font-bold ${
                    u.role === "admin"
                      ? "bg-teal text-white"
                      : "bg-fond text-gris"
                  }`}
                >
                  {u.role === "admin" ? "Propriétaire" : "Membre"}
                </span>
              </td>
              <td className="px-4 py-3">
                <span
                  className={`rounded-full px-2.5 py-1 text-xs font-bold ${
                    u.statut === "actif"
                      ? "bg-bulle-sortie text-teal"
                      : "bg-danger/10 text-danger"
                  }`}
                >
                  {u.statut === "actif" ? "● Actif" : "⏸ Suspendu"}
                </span>
              </td>
              <td className="px-4 py-3 text-gris">{u.nb_rapports}</td>
              <td className="px-4 py-3 text-xs text-gris">
                {new Date(u.cree_le + "Z").toLocaleDateString("fr-FR")}
              </td>
              <td className="px-4 py-3">
                {u.id !== monId && (
                  <div className="flex justify-end gap-2">
                    {u.statut === "actif" ? (
                      <button
                        type="button"
                        className="btn-blanc px-3 py-1.5 text-xs"
                        onClick={() => void patcher(u.id, { statut: "suspendu" })}
                      >
                        Suspendre
                      </button>
                    ) : (
                      <button
                        type="button"
                        className="btn-vert px-3 py-1.5 text-xs"
                        onClick={() => void patcher(u.id, { statut: "actif" })}
                      >
                        Réactiver
                      </button>
                    )}
                    <button
                      type="button"
                      className="btn-danger px-3 py-1.5 text-xs"
                      onClick={() => void supprimer(u.id, u.email)}
                    >
                      Supprimer
                    </button>
                  </div>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
