"use client";

import { useRouter } from "next/navigation";

export default function BoutonDeconnexion() {
  const router = useRouter();
  return (
    <button
      type="button"
      onClick={async () => {
        await fetch("/api/auth/deconnexion", { method: "POST" });
        router.push("/");
        router.refresh();
      }}
      className="text-sm text-white/80 hover:text-white"
    >
      Déconnexion
    </button>
  );
}
