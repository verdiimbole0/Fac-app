"use client";

import { useRouter } from "next/navigation";

export function BoutonSupprimerRapport({ id }: { id: number }) {
  const router = useRouter();
  return (
    <button
      type="button"
      className="btn-danger px-3 py-1.5 text-xs"
      onClick={async () => {
        if (!window.confirm("Supprimer définitivement ce rapport ?")) return;
        await fetch(`/api/rapports/${id}`, { method: "DELETE" });
        router.refresh();
      }}
    >
      Supprimer
    </button>
  );
}

export function BoutonSupprimerMesDonnees() {
  const router = useRouter();
  return (
    <button
      type="button"
      className="btn-danger px-4 py-2 text-sm"
      onClick={async () => {
        if (
          !window.confirm(
            "Supprimer tes données ? Tous tes rapports seront effacés définitivement. (Tes conversations, elles, ne sont jamais stockées.)",
          )
        )
          return;
        await fetch("/api/rapports", { method: "DELETE" });
        router.refresh();
      }}
    >
      🗑️ Supprimer mes données
    </button>
  );
}

export function BoutonSupprimerCompte() {
  const router = useRouter();
  return (
    <button
      type="button"
      className="text-xs text-gris underline hover:text-danger"
      onClick={async () => {
        if (
          !window.confirm(
            "Supprimer ton compte ET toutes tes données ? Cette action est irréversible.",
          )
        )
          return;
        const reponse = await fetch("/api/auth/compte", { method: "DELETE" });
        if (!reponse.ok) {
          const corps = await reponse.json().catch(() => null);
          window.alert(corps?.erreur ?? "Suppression impossible.");
          return;
        }
        router.push("/");
        router.refresh();
      }}
    >
      Supprimer mon compte et toutes mes données
    </button>
  );
}
