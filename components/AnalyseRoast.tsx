"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import Link from "next/link";
import RapportRoast from "@/components/RapportRoast";
import { roastVersMarkdown, type RapportRoastData } from "@/lib/roast";
import { analyserConversation } from "@/lib/whatsapp";
import { telechargerRapportPdf } from "@/lib/pdf";

type Etat = "saisie" | "analyse" | "fini";

const PHRASES_ATTENTE = [
  "Brandon lit tout. Même ce que vous regrettez. 👀",
  "Il compte les « mdr » un par un…",
  "Il croise les horaires d'envoi avec les temps de réponse…",
  "Il classe les pièces à conviction…",
  "Il cherche la métaphore parfaite. Il l'a trouvée. Elle est cruelle.",
];

export default function AnalyseRoast() {
  const [etat, setEtat] = useState<Etat>("saisie");
  const [conversation, setConversation] = useState("");
  const [rapport, setRapport] = useState<RapportRoastData | null>(null);
  const [erreur, setErreur] = useState<string | null>(null);
  const [nomFichier, setNomFichier] = useState<string | null>(null);
  const [phrase, setPhrase] = useState(0);
  const [copie, setCopie] = useState(false);
  const [donneesSupprimees, setDonneesSupprimees] = useState(false);
  const fichierRef = useRef<HTMLInputElement>(null);

  const stats = useMemo(
    () => (conversation.trim() ? analyserConversation(conversation) : null),
    [conversation],
  );

  useEffect(() => {
    if (etat !== "analyse") return;
    const t = setInterval(
      () => setPhrase((p) => (p + 1) % PHRASES_ATTENTE.length),
      2600,
    );
    return () => clearInterval(t);
  }, [etat]);

  async function chargerFichier(f: File) {
    if (f.size > 5 * 1024 * 1024) {
      setErreur("Fichier trop volumineux (5 Mo maximum).");
      return;
    }
    setErreur(null);
    setNomFichier(f.name);
    setConversation(await f.text());
  }

  async function analyser() {
    setErreur(null);
    setEtat("analyse");
    try {
      const reponse = await fetch("/api/roast", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ conversation }),
      });
      const corps = await reponse.json().catch(() => null);
      if (!reponse.ok) {
        throw new Error(corps?.erreur ?? `Erreur serveur (${reponse.status}).`);
      }
      setRapport(corps.rapport as RapportRoastData);
      setEtat("fini");
    } catch (e) {
      setErreur(e instanceof Error ? e.message : "Erreur inattendue.");
      setEtat("saisie");
    }
  }

  async function copier() {
    if (!rapport) return;
    await navigator.clipboard.writeText(roastVersMarkdown(rapport));
    setCopie(true);
    setTimeout(() => setCopie(false), 2000);
  }

  async function supprimerMesDonnees() {
    if (
      !window.confirm(
        "Supprimer tes données ? Tous les rapports enregistrés dans ton compte seront effacés définitivement.",
      )
    )
      return;
    const reponse = await fetch("/api/rapports", { method: "DELETE" });
    if (reponse.ok) setDonneesSupprimees(true);
  }

  const deuxPersonnes = stats && stats.participants.length === 2;
  const pret =
    conversation.trim().length >= 200 && !!stats && stats.nbMessages >= 10;

  return (
    <div className="mx-auto max-w-3xl px-5 py-10">
      {etat === "saisie" && (
        <>
          <p className="inline-block rounded-full bg-stone-800 px-3.5 py-1.5 text-xs font-bold uppercase tracking-wider text-white">
            🔥 Mode duo — le rapport de Brandon
          </p>
          <h1 className="mt-4 font-serif text-3xl font-bold text-stone-900">
            Deux personnes. Un dossier. Zéro filtre.
          </h1>
          <p className="mt-3 max-w-prose text-stone-600">
            Exporte une discussion WhatsApp <strong>à deux</strong> (pas un
            groupe) : Brandon instruit le dossier de chacun, pièces à
            conviction verbatim à l&apos;appui. C&apos;est satirique,
            c&apos;est chirurgical, et c&apos;est appuyé sur vos vrais
            messages.
          </p>

          <div className="mt-8">
            <input
              ref={fichierRef}
              type="file"
              accept=".txt,text/plain"
              className="hidden"
              onChange={(e) => {
                const f = e.target.files?.[0];
                if (f) void chargerFichier(f);
              }}
            />
            <button
              type="button"
              onClick={() => fichierRef.current?.click()}
              className="w-full rounded-2xl border-2 border-dashed border-stone-300 bg-white p-7 text-center transition hover:border-stone-500"
            >
              <p className="text-2xl">🗂️</p>
              <p className="mt-2 font-bold text-stone-900">
                {nomFichier ?? "Dépose l'export .txt du tête-à-tête"}
              </p>
              <p className="mt-1 text-xs text-stone-500">
                Clique ou glisse-dépose — 5 Mo max
              </p>
            </button>
            <p className="my-4 text-center text-xs uppercase tracking-widest text-stone-400">
              — ou —
            </p>
            <textarea
              value={conversation}
              onChange={(e) => {
                setConversation(e.target.value);
                setNomFichier(null);
              }}
              rows={8}
              placeholder={
                "12/03/2024, 21:47 - Léa: on peut parler ?\n12/03/2024, 23:58 - Hugo: mdr de quoi\n…"
              }
              className="w-full rounded-2xl border border-stone-300 bg-white p-4 font-mono text-[13px] text-stone-800 placeholder:text-stone-400 focus:border-stone-800 focus:outline-none"
            />
          </div>

          {stats && stats.nbMessages > 0 && (
            <div
              className={`mt-4 rounded-2xl border p-4 text-sm ${
                deuxPersonnes
                  ? "border-stone-300 bg-white text-stone-700"
                  : "border-amber-400 bg-amber-50 text-amber-800"
              }`}
            >
              {deuxPersonnes ? (
                <>
                  🗂️ Dossier recevable :{" "}
                  <strong>
                    {stats.participants[0].nom} (
                    {stats.participants[0].nbMessages} messages)
                  </strong>{" "}
                  contre{" "}
                  <strong>
                    {stats.participants[1].nom} (
                    {stats.participants[1].nbMessages} messages)
                  </strong>
                  {stats.premiereDate && stats.derniereDate
                    ? `, du ${stats.premiereDate} au ${stats.derniereDate}`
                    : ""}
                  .
                </>
              ) : (
                <>
                  ⚠️ {stats.participants.length} personne
                  {stats.participants.length > 1 ? "s" : ""} détectée
                  {stats.participants.length > 1 ? "s" : ""} — le mode duo
                  exige une discussion à <strong>deux</strong>. Pour les
                  groupes, c&apos;est{" "}
                  <Link href="/rapport" className="underline">
                    le rapport de Steve
                  </Link>
                  .
                </>
              )}
            </div>
          )}

          {erreur && (
            <p className="mt-4 rounded-2xl border border-red-300 bg-red-50 p-4 text-sm text-red-700">
              {erreur}
            </p>
          )}

          <button
            type="button"
            onClick={() => void analyser()}
            disabled={!pret || !deuxPersonnes}
            className="mt-8 w-full rounded-full bg-stone-900 px-6 py-4 text-lg font-bold text-white shadow-lg transition hover:bg-stone-700 disabled:cursor-not-allowed disabled:opacity-40"
          >
            {pret && deuxPersonnes
              ? "Ouvrir le dossier →"
              : "Colle une discussion à deux (quelques dizaines de messages)"}
          </button>
          <p className="mt-4 text-center text-xs text-stone-500">
            🔒 Ta conversation sert uniquement à instruire ce dossier — jamais
            stockée, jamais utilisée pour entraîner des modèles.
          </p>
        </>
      )}

      {etat === "analyse" && (
        <div className="py-24 text-center">
          <p className="text-4xl">🗂️</p>
          <h1 className="mt-4 font-serif text-2xl font-bold text-stone-900">
            Brandon instruit le dossier…
          </h1>
          <p className="mt-3 animate-pulse text-stone-500">
            {PHRASES_ATTENTE[phrase]}
          </p>
        </div>
      )}

      {etat === "fini" && rapport && (
        <>
          <div className="mb-6 flex flex-wrap items-center justify-between gap-3">
            <p className="text-xs font-bold uppercase tracking-widest text-stone-400">
              Dossier clos — enregistré dans{" "}
              <Link href="/mes-rapports" className="underline">
                ton espace
              </Link>
            </p>
            <div className="flex flex-wrap gap-2">
              <button
                type="button"
                className="rounded-full bg-stone-900 px-4 py-2 text-sm font-bold text-white hover:bg-stone-700"
                onClick={() =>
                  telechargerRapportPdf(
                    roastVersMarkdown(rapport),
                    rapport.titre,
                    "Le rapport de Brandon",
                    "rapport-brandon",
                  )
                }
              >
                ⬇️ Télécharger en PDF
              </button>
              <button
                type="button"
                className="rounded-full border border-stone-300 bg-white px-4 py-2 text-sm font-semibold text-stone-700 hover:border-stone-500"
                onClick={() => void copier()}
              >
                {copie ? "Copié ✓" : "Copier"}
              </button>
              <button
                type="button"
                className="rounded-full border border-stone-300 bg-white px-4 py-2 text-sm font-semibold text-stone-700 hover:border-stone-500"
                onClick={() => {
                  setEtat("saisie");
                  setRapport(null);
                  setConversation("");
                  setNomFichier(null);
                  setDonneesSupprimees(false);
                }}
              >
                Nouveau dossier
              </button>
              <button
                type="button"
                className="rounded-full border border-red-200 bg-red-50 px-4 py-2 text-sm font-semibold text-red-600 hover:border-red-400"
                onClick={() => void supprimerMesDonnees()}
              >
                🗑️ Supprimer mes données
              </button>
            </div>
          </div>
          {donneesSupprimees && (
            <p className="mb-4 rounded-2xl border border-stone-300 bg-white p-4 text-sm text-stone-700">
              ✅ Tous tes rapports sont effacés de nos serveurs. Il ne reste
              que ce que tu vois à l&apos;écran.
            </p>
          )}
          <RapportRoast rapport={rapport} />
        </>
      )}
    </div>
  );
}
