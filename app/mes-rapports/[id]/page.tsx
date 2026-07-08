import Link from "next/link";
import { notFound, redirect } from "next/navigation";
import ReactMarkdown from "react-markdown";
import EnTete from "@/components/EnTete";
import BarreRapport from "@/components/BarreRapport";
import RapportRoast from "@/components/RapportRoast";
import { roastVersMarkdown, type RapportRoastData } from "@/lib/roast";
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

  // Les rapports « roast » (mode duo) sont stockés en JSON structuré ;
  // ceux de Steve en markdown.
  let roast: RapportRoastData | null = null;
  if (rapport.type === "roast") {
    try {
      roast = JSON.parse(rapport.contenu) as RapportRoastData;
    } catch {
      roast = null;
    }
  }
  const markdown = roast ? roastVersMarkdown(roast) : rapport.contenu;

  return (
    <main className="flex flex-1 flex-col">
      <EnTete />
      <div className={`flex-1 py-10 ${roast ? "bg-stone-100" : "papier-peint"}`}>
        <div className="mx-auto max-w-3xl px-5">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <Link
              href="/mes-rapports"
              className={`text-sm font-semibold hover:underline ${
                roast ? "text-stone-600" : "text-teal-2"
              }`}
            >
              ← Mes rapports
            </Link>
            <BarreRapport
              id={rapport.id}
              titre={rapport.titre}
              contenu={markdown}
              marque={roast ? "Le rapport de Brandon" : undefined}
              prefixeFichier={roast ? "rapport-brandon" : undefined}
            />
          </div>
          {roast ? (
            <div className="mt-6">
              <RapportRoast rapport={roast} />
            </div>
          ) : (
            <article className="rapport carte mt-6 p-6 sm:p-9">
              <ReactMarkdown>{rapport.contenu}</ReactMarkdown>
            </article>
          )}
        </div>
      </div>
    </main>
  );
}
