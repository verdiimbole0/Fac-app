import Link from "next/link";
import { redirect } from "next/navigation";
import EnTete from "@/components/EnTete";
import {
  BoutonSupprimerCompte,
  BoutonSupprimerMesDonnees,
  BoutonSupprimerRapport,
} from "@/components/ActionsRapports";
import { utilisateurCourant } from "@/lib/auth";
import { db, type Rapport } from "@/lib/db";

const EMOJIS: Record<string, string> = {
  "groupe d'amis": "👯",
  couple: "❤️",
  famille: "👨‍👩‍👧",
  boulot: "💼",
  situationship: "🫠",
  autre: "🎲",
};

export const dynamic = "force-dynamic";

export default async function PageMesRapports() {
  const u = await utilisateurCourant();
  if (!u) redirect("/connexion");

  const rapports = db()
    .prepare(
      "SELECT id, titre, type, cree_le FROM rapports WHERE utilisateur_id = ? ORDER BY id DESC",
    )
    .all(u.id) as Pick<Rapport, "id" | "titre" | "type" | "cree_le">[];

  return (
    <main className="flex flex-1 flex-col">
      <EnTete />
      <div className="papier-peint flex-1 py-10">
        <div className="mx-auto max-w-3xl px-5">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <div>
              <h1 className="text-2xl font-extrabold text-teal">
                Mes rapports
              </h1>
              <p className="mt-1 text-sm text-gris">
                {rapports.length === 0
                  ? "Aucun rapport pour l'instant."
                  : `${rapports.length} rapport${rapports.length > 1 ? "s" : ""} enregistré${rapports.length > 1 ? "s" : ""} dans ton espace.`}
              </p>
            </div>
            <div className="flex gap-2">
              <Link href="/rapport" className="btn-vert px-4 py-2 text-sm">
                + Nouveau rapport
              </Link>
              {rapports.length > 0 && <BoutonSupprimerMesDonnees />}
            </div>
          </div>

          <div className="mt-8 flex flex-col gap-3">
            {rapports.length === 0 && (
              <div className="carte p-8 text-center">
                <p className="text-3xl">📭</p>
                <p className="mt-3 font-bold text-teal">
                  Steve attend ta première conversation
                </p>
                <p className="mt-1 text-sm text-gris">
                  Envoie-lui un export WhatsApp, il te dira ce qu&apos;il en
                  pense — avec analyses et conseils.
                </p>
                <Link
                  href="/rapport"
                  className="btn-vert mt-5 inline-block px-6 py-2.5 text-sm"
                >
                  Parler à Steve →
                </Link>
              </div>
            )}
            {rapports.map((r) => (
              <div key={r.id} className="carte flex items-center gap-4 p-4">
                <span className="text-2xl">{EMOJIS[r.type] ?? "🎲"}</span>
                <div className="min-w-0 flex-1">
                  <Link
                    href={`/mes-rapports/${r.id}`}
                    className="block truncate font-bold text-teal hover:underline"
                  >
                    {r.titre}
                  </Link>
                  <p className="text-xs text-gris">
                    {new Date(r.cree_le + "Z").toLocaleDateString("fr-FR", {
                      day: "numeric",
                      month: "long",
                      year: "numeric",
                    })}{" "}
                    · {r.type}
                  </p>
                </div>
                <Link
                  href={`/mes-rapports/${r.id}`}
                  className="btn-blanc px-3 py-1.5 text-xs"
                >
                  Lire
                </Link>
                <BoutonSupprimerRapport id={r.id} />
              </div>
            ))}
          </div>

          <div className="mt-10 text-center">
            <BoutonSupprimerCompte />
          </div>
        </div>
      </div>
    </main>
  );
}
