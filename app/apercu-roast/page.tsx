import RapportRoast from "@/components/RapportRoast";
import { RAPPORT_ROAST_DEMO } from "@/lib/roast";

// Aperçu du composant RapportRoast avec les données d'exemple —
// le format exact que le persona « Brandon » renvoie en JSON.

export const metadata = {
  title: "Aperçu — Rapport de Brandon",
};

export default function PageApercuRoast() {
  return (
    <main className="min-h-screen bg-stone-100 px-4 py-12">
      <RapportRoast rapport={RAPPORT_ROAST_DEMO} />
      <p className="mx-auto mt-6 max-w-2xl text-center text-xs text-stone-400">
        Aperçu du composant <code>RapportRoast</code> avec des données
        d&apos;exemple — le JSON exact que renvoie le persona « Brandon »
        (voir <code>lib/roast.ts</code>).
      </p>
    </main>
  );
}
