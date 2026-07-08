"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { telechargerRapportPdf } from "@/lib/pdf";

export default function BarreRapport({
  id,
  titre,
  contenu,
  marque = "Que pense Steve",
  prefixeFichier = "rapport-steve",
}: {
  id: number;
  titre: string;
  contenu: string;
  marque?: string;
  prefixeFichier?: string;
}) {
  const [copie, setCopie] = useState(false);
  const router = useRouter();

  return (
    <div className="flex flex-wrap gap-2">
      <button
        type="button"
        className="btn-vert px-4 py-2 text-sm"
        onClick={() => telechargerRapportPdf(contenu, titre, marque, prefixeFichier)}
      >
        ⬇️ Télécharger en PDF
      </button>
      <button
        type="button"
        className="btn-blanc px-4 py-2 text-sm"
        onClick={async () => {
          await navigator.clipboard.writeText(contenu);
          setCopie(true);
          setTimeout(() => setCopie(false), 2000);
        }}
      >
        {copie ? "Copié ✓" : "Copier"}
      </button>
      <button
        type="button"
        className="btn-danger px-4 py-2 text-sm"
        onClick={async () => {
          if (!window.confirm("Supprimer définitivement ce rapport ?")) return;
          await fetch(`/api/rapports/${id}`, { method: "DELETE" });
          router.push("/mes-rapports");
          router.refresh();
        }}
      >
        🗑️ Supprimer
      </button>
    </div>
  );
}
