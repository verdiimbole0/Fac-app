import { redirect } from "next/navigation";
import EnTete from "@/components/EnTete";
import FormulaireAuth from "@/components/FormulaireAuth";
import { utilisateurCourant } from "@/lib/auth";

export default async function PageConnexion() {
  if (await utilisateurCourant()) redirect("/rapport");
  return (
    <main className="flex flex-1 flex-col">
      <EnTete />
      <div className="papier-peint flex flex-1 items-center justify-center px-5 py-16">
        <FormulaireAuth mode="connexion" />
      </div>
    </main>
  );
}
