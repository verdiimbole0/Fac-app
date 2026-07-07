"use client";

import { useMemo, useRef, useState } from "react";
import Link from "next/link";
import ReactMarkdown from "react-markdown";
import { analyserConversation } from "@/lib/whatsapp";

const TYPES = [
  { id: "groupe d'amis", label: "👯 Groupe de potes" },
  { id: "couple", label: "❤️ Couple" },
  { id: "famille", label: "👨‍👩‍👧 Famille" },
  { id: "boulot", label: "💼 Boulot" },
  { id: "situationship", label: "🫠 Situationship" },
  { id: "autre", label: "🎲 Autre" },
];

type Etat = "saisie" | "generation" | "fini";

export default function PageRapport() {
  const [conversation, setConversation] = useState("");
  const [type, setType] = useState("groupe d'amis");
  const [prenom, setPrenom] = useState("");
  const [etat, setEtat] = useState<Etat>("saisie");
  const [rapport, setRapport] = useState("");
  const [erreur, setErreur] = useState<string | null>(null);
  const [nomFichier, setNomFichier] = useState<string | null>(null);
  const fichierRef = useRef<HTMLInputElement>(null);

  const stats = useMemo(
    () => (conversation.trim() ? analyserConversation(conversation) : null),
    [conversation],
  );

  async function chargerFichier(f: File) {
    if (f.size > 5 * 1024 * 1024) {
      setErreur("Fichier trop volumineux (5 Mo maximum).");
      return;
    }
    setErreur(null);
    setNomFichier(f.name);
    setConversation(await f.text());
  }

  async function genererRapport() {
    setErreur(null);
    setRapport("");
    setEtat("generation");
    try {
      const reponse = await fetch("/api/rapport", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ conversation, type, prenom }),
      });
      if (!reponse.ok) {
        const corps = await reponse.json().catch(() => null);
        throw new Error(corps?.erreur ?? `Erreur serveur (${reponse.status}).`);
      }
      if (!reponse.body) throw new Error("Réponse vide du serveur.");
      const lecteur = reponse.body.getReader();
      const decodeur = new TextDecoder();
      let texte = "";
      for (;;) {
        const { done, value } = await lecteur.read();
        if (done) break;
        texte += decodeur.decode(value, { stream: true });
        setRapport(texte);
      }
      setEtat("fini");
    } catch (e) {
      setErreur(e instanceof Error ? e.message : "Erreur inattendue.");
      setEtat("saisie");
    }
  }

  function recommencer() {
    setEtat("saisie");
    setRapport("");
    setErreur(null);
  }

  const pret = conversation.trim().length >= 200;

  return (
    <main className="flex-1">
      <header className="sticky top-0 z-20 border-b border-white/5 bg-ink/90 backdrop-blur">
        <div className="mx-auto flex max-w-3xl items-center justify-between px-5 py-4">
          <Link href="/" className="font-display text-lg font-bold text-accent">
            Que pense Bertrand
          </Link>
          <Link href="/" className="text-sm text-paper-dim hover:text-paper">
            ← Retour
          </Link>
        </div>
      </header>

      <div className="mx-auto max-w-3xl px-5 py-12">
        {etat === "saisie" && (
          <>
            <h1 className="font-display text-3xl font-bold">
              Donne ta conversation à Bertrand
            </h1>
            <p className="mt-3 text-paper-dim">
              Exporte ta discussion WhatsApp (Paramètres du chat → Exporter la
              discussion → <em>Sans les médias</em>), puis dépose le fichier
              .txt ici — ou colle directement le texte.
            </p>

            {/* Type de conversation */}
            <p className="mt-8 text-sm font-bold uppercase tracking-widest text-paper-dim">
              C&apos;est quoi comme conversation ?
            </p>
            <div className="mt-3 flex flex-wrap gap-2">
              {TYPES.map((t) => (
                <button
                  key={t.id}
                  type="button"
                  onClick={() => setType(t.id)}
                  className={`rounded-full border px-4 py-2 text-sm font-semibold transition ${
                    type === t.id
                      ? "border-accent bg-accent text-ink"
                      : "border-white/10 bg-ink-card text-paper-dim hover:border-accent/50"
                  }`}
                >
                  {t.label}
                </button>
              ))}
            </div>

            {/* Fichier ou texte */}
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
                className="w-full rounded-2xl border-2 border-dashed border-white/15 bg-ink-soft p-6 text-center transition hover:border-accent/60"
              >
                <p className="text-2xl">📄</p>
                <p className="mt-2 font-semibold">
                  {nomFichier ?? "Déposer l'export .txt"}
                </p>
                <p className="mt-1 text-xs text-paper-dim">
                  WhatsApp, iMessage ou n&apos;importe quel texte — 5 Mo max
                </p>
              </button>
              <p className="my-4 text-center text-xs uppercase tracking-widest text-paper-dim">
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
                  "12/03/2024, 21:47 - Karim: bon on les fait ces vacances ou pas\n12/03/2024, 21:52 - Julie: je regarde et je te dis\n…"
                }
                className="w-full rounded-2xl border border-white/10 bg-ink-soft p-4 text-sm text-paper placeholder:text-paper-dim/50 focus:border-accent focus:outline-none"
              />
            </div>

            {/* Aperçu des stats */}
            {stats && stats.nbMessages > 0 && (
              <div className="mt-4 rounded-2xl border border-accent/30 bg-accent/5 p-4 text-sm">
                <p className="font-bold text-accent">
                  🔎 Ce que Bertrand voit déjà :
                </p>
                <p className="mt-1 text-paper-dim">
                  {stats.nbMessages.toLocaleString("fr-FR")} messages,{" "}
                  {stats.participants.length} participant
                  {stats.participants.length > 1 ? "s" : ""}
                  {stats.premiereDate && stats.derniereDate
                    ? ` — du ${stats.premiereDate} au ${stats.derniereDate}`
                    : ""}
                  .{" "}
                  {stats.participants[0]
                    ? `Le plus bavard : ${stats.participants[0].nom} (${stats.participants[0].nbMessages} messages).`
                    : ""}
                </p>
              </div>
            )}

            {/* Prénom */}
            <div className="mt-6">
              <label
                htmlFor="prenom"
                className="text-sm font-bold uppercase tracking-widest text-paper-dim"
              >
                Ton prénom dans la conversation{" "}
                <span className="font-normal normal-case">(optionnel)</span>
              </label>
              <input
                id="prenom"
                type="text"
                value={prenom}
                onChange={(e) => setPrenom(e.target.value)}
                placeholder="ex. Karim"
                maxLength={40}
                className="mt-2 w-full rounded-2xl border border-white/10 bg-ink-soft p-4 text-sm focus:border-accent focus:outline-none sm:w-72"
              />
            </div>

            {erreur && (
              <p className="mt-6 rounded-2xl border border-red-500/40 bg-red-500/10 p-4 text-sm text-red-300">
                {erreur}
              </p>
            )}

            <button
              type="button"
              onClick={() => void genererRapport()}
              disabled={!pret}
              className="mt-8 w-full rounded-full bg-accent px-6 py-4 text-lg font-bold text-ink transition hover:bg-accent-strong disabled:cursor-not-allowed disabled:opacity-40"
            >
              {pret
                ? "Envoyer à Bertrand →"
                : "Colle au moins quelques dizaines de messages"}
            </button>
            <p className="mt-4 text-center text-xs text-paper-dim">
              🔒 Ta conversation sert uniquement à écrire ce rapport. Elle
              n&apos;est ni stockée, ni utilisée pour entraîner des modèles.
            </p>
          </>
        )}

        {(etat === "generation" || etat === "fini") && (
          <>
            <div className="flex items-center justify-between">
              <h1 className="font-display text-2xl font-bold">
                {etat === "generation"
                  ? "Bertrand écrit…"
                  : "Le rapport de Bertrand"}
              </h1>
              {etat === "fini" && (
                <div className="flex gap-2">
                  <button
                    type="button"
                    onClick={() => void navigator.clipboard.writeText(rapport)}
                    className="rounded-full border border-white/10 px-4 py-2 text-sm font-semibold text-paper-dim transition hover:border-accent hover:text-paper"
                  >
                    Copier
                  </button>
                  <button
                    type="button"
                    onClick={recommencer}
                    className="rounded-full bg-accent px-4 py-2 text-sm font-bold text-ink transition hover:bg-accent-strong"
                  >
                    Nouveau rapport
                  </button>
                </div>
              )}
            </div>
            {etat === "generation" && !rapport && (
              <p className="mt-4 animate-pulse text-paper-dim">
                Il lit tout. Vraiment tout. 👀
              </p>
            )}
            <div
              className={`rapport mt-6 rounded-3xl border border-white/10 bg-ink-soft p-6 sm:p-8 ${
                etat === "generation" && rapport ? "cursor-blink" : ""
              }`}
            >
              <ReactMarkdown>{rapport}</ReactMarkdown>
            </div>
          </>
        )}
      </div>
    </main>
  );
}
