import { redirect } from "next/navigation";
import EnTete from "@/components/EnTete";
import AnalyseRoast from "@/components/AnalyseRoast";
import { utilisateurCourant } from "@/lib/auth";

export const metadata = {
  title: "Mode duo — le rapport de Brandon",
};

export default async function PageRoast() {
  const u = await utilisateurCourant();
  if (!u) redirect("/connexion");
  return (
    <main className="flex min-h-screen flex-1 flex-col bg-stone-100">
      <EnTete />
      <AnalyseRoast />
    </main>
  );
}
