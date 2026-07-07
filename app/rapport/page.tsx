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
  const [survol, setSurvol] = useState(false);
  const [copie, setCopie] = useState(false);
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

  async function copierRapport() {
    await navigator.clipboard.writeText(rapport);
    setCopie(true);
    setTimeout(() => setCopie(false), 2000);
  }

  const pret = conversation.trim().length >= 200;

  return (
    <main className="flex-1">
      <header className="sticky top-0 z-20 border-b border-line bg-ink/85 backdrop-blur">
        <div className="mx-auto flex max-w-3xl items-center justify-between px-5 py-3.5">
          <Link href="/" className="flex items-center gap-2">
            <span className="flex h-8 w-8 items-center justify-center rounded-xl bg-gradient-to-br from-accent to-accent-2 text-base">
              🧠
            </span>
            <span className="voice text-lg font-bold">Que pense Bertrand</span>
          </Link>
          <Link href="/" className="text-sm text-dim hover:text-paper">
            ← Retour
          </Link>
        </div>
      </header>

      <div className="halo mx-auto max-w-3xl px-5 py-12">
        {etat === "saisie" && (
          <>
            <p className="etiquette text-accent">Nouveau dossier</p>
            <h1 className="mt-3 text-3xl font-extrabold tracking-tight md:text-4xl">
              Donne ta conversation à{" "}
              <span className="voice degrade-accent">Bertrand</span>
            </h1>
            <p className="mt-4 text-dim">
              Exporte ta discussion WhatsApp (Paramètres du chat → Exporter la
              discussion → <em>Sans les médias</em>), puis dépose le fichier
              .txt ici — ou colle directement le texte.
            </p>

            {/* Type de conversation */}
            <p className="etiquette mt-10 text-dim">
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
                      ? "border-accent bg-accent/15 text-accent"
                      : "border-line bg-ink-2 text-dim hover:border-accent/50 hover:text-paper"
                  }`}
                >
                  {t.label}
                </button>
              ))}
            </div>

            {/* Fichier ou texte */}
            <div className="mt-9">
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
                onDragOver={(e) => {
                  e.preventDefault();
                  setSurvol(true);
                }}
                onDragLeave={() => setSurvol(false)}
                onDrop={(e) => {
                  e.preventDefault();
                  setSurvol(false);
                  const f = e.dataTransfer.files?.[0];
                  if (f) void chargerFichier(f);
                }}
                className={`w-full rounded-2xl border-2 border-dashed p-7 text-center transition ${
                  survol
                    ? "border-accent bg-accent/10"
                    : "border-line bg-ink-2 hover:border-accent/60"
                }`}
              >
                <p className="text-2xl">📄</p>
                <p className="mt-2 font-bold">
                  {nomFichier ?? "Dépose l'export .txt ici"}
                </p>
                <p className="mt-1 text-xs text-dim">
                  Clique ou glisse-dépose — WhatsApp, iMessage ou
                  n&apos;importe quel texte, 5 Mo max
                </p>
              </button>
              <p className="etiquette my-4 text-center text-dim">— ou —</p>
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
                className="w-full rounded-2xl border border-line bg-ink-2 p-4 text-sm text-paper placeholder:text-dim/50 focus:border-accent focus:outline-none"
              />
            </div>

            {/* Aperçu des stats */}
            {stats && stats.nbMessages > 0 && (
              <div className="lever mt-4 rounded-2xl border border-accent/35 bg-accent/8 p-4 text-sm">
                <p className="etiquette text-accent">
                  🔎 Ce que Bertrand voit déjà
                </p>
                <p className="mt-2 text-dim">
                  <strong className="text-paper">
                    {stats.nbMessages.toLocaleString("fr-FR")} messages
                  </strong>
                  , {stats.participants.length} participant
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
            <div className="mt-8">
              <label htmlFor="prenom" className="etiquette text-dim">
                Ton prénom dans la conversation (optionnel)
              </label>
              <input
                id="prenom"
                type="text"
                value={prenom}
                onChange={(e) => setPrenom(e.target.value)}
                placeholder="ex. Karim"
                maxLength={40}
                className="mt-2 block w-full rounded-2xl border border-line bg-ink-2 p-4 text-sm focus:border-accent focus:outline-none sm:w-72"
              />
            </div>

            {erreur && (
              <p className="mt-6 rounded-2xl border border-red-400/40 bg-red-400/10 p-4 text-sm text-red-300">
                {erreur}
              </p>
            )}

            <button
              type="button"
              onClick={() => void genererRapport()}
              disabled={!pret}
              className="btn-accent mt-9 w-full rounded-full px-6 py-4 text-lg font-bold"
            >
              {pret
                ? "Envoyer à Bertrand →"
                : "Colle au moins quelques dizaines de messages"}
            </button>
            <p className="mt-4 text-center text-xs text-dim">
              🔒 Ta conversation sert uniquement à écrire ce rapport. Elle
              n&apos;est ni stockée, ni utilisée pour entraîner des modèles.
            </p>
          </>
        )}

        {(etat === "generation" || etat === "fini") && (
          <>
            <div className="flex flex-wrap items-center justify-between gap-3">
              <div>
                <p className="etiquette text-accent">
                  {etat === "generation" ? "Dossier en cours" : "Dossier clos"}
                </p>
                <h1 className="mt-1 text-2xl font-extrabold tracking-tight">
                  {etat === "generation" ? (
                    <span className="voice">Bertrand écrit…</span>
                  ) : (
                    <>
                      Le rapport de{" "}
                      <span className="voice degrade-accent">Bertrand</span>
                    </>
                  )}
                </h1>
              </div>
              {etat === "fini" && (
                <div className="flex gap-2">
                  <button
                    type="button"
                    onClick={() => void copierRapport()}
                    className="rounded-full border border-line px-4 py-2 text-sm font-semibold text-dim transition hover:border-accent hover:text-paper"
                  >
                    {copie ? "Copié ✓" : "Copier"}
                  </button>
                  <button
                    type="button"
                    onClick={recommencer}
                    className="btn-accent rounded-full px-4 py-2 text-sm font-bold"
                  >
                    Nouveau rapport
                  </button>
                </div>
              )}
            </div>
            {etat === "generation" && !rapport && (
              <p className="mt-5 flex items-center gap-3 text-dim">
                <span className="points-frappe">
                  <span />
                  <span />
                  <span />
                </span>
                Il lit tout. Vraiment tout. 👀
              </p>
            )}
            <div
              className={`rapport carte mt-6 rounded-3xl p-6 sm:p-9 ${
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
