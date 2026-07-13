import { redirect } from "next/navigation";
import ChatSteve from "@/components/ChatSteve";
import { utilisateurCourant } from "@/lib/auth";

export default async function PageRapport() {
  const u = await utilisateurCourant();
  if (!u) redirect("/connexion");
  return (
    <main className="flex min-h-screen flex-1 flex-col bg-fond">
      <ChatSteve prenomCompte={u.nom} />
    </main>
  );
}
