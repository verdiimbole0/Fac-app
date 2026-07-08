import Link from "next/link";
import { notFound, redirect } from "next/navigation";
import ReactMarkdown from "react-markdown";
import EnTete from "@/components/EnTete";
import BarreRapport from "@/components/BarreRapport";
import { utilisateurCourant } from "@/lib/auth";
import { db, type Rapport } from "@/lib/db";

export const dynamic = "force-dynamic";

export default async function PageLectureRapport({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const u = await utilisateurCourant();
  if (!u) redirect("/connexion");

  const { id } = await params;
  const rapport = db()
    .prepare("SELECT * FROM rapports WHERE id = ? AND utilisateur_id = ?")
    .get(Number(id), u.id) as Rapport | undefined;
  if (!rapport) notFound();

  return (
    <main className="flex flex-1 flex-col">
      <EnTete />
      <div className="papier-peint flex-1 py-10">
        <div className="mx-auto max-w-3xl px-5">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <Link
              href="/mes-rapports"
              className="text-sm font-semibold text-teal-2 hover:underline"
            >
              ← Mes rapports
            </Link>
            <BarreRapport
              id={rapport.id}
              titre={rapport.titre}
              contenu={rapport.contenu}
            />
          </div>
          <article className="rapport carte mt-6 p-6 sm:p-9">
            <ReactMarkdown>{rapport.contenu}</ReactMarkdown>
          </article>
        </div>
      </div>
    </main>
  );
}
