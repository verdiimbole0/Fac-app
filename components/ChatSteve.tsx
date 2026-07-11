"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import Link from "next/link";
import ReactMarkdown from "react-markdown";
import { analyserConversation } from "@/lib/whatsapp";
import { telechargerRapportPdf } from "@/lib/pdf";

const TYPES = [
  { id: "groupe d'amis", label: "👯 Groupe de potes" },
  { id: "couple", label: "❤️ Couple" },
  { id: "famille", label: "👨‍👩‍👧 Famille" },
  { id: "boulot", label: "💼 Boulot" },
  { id: "situationship", label: "🫠 Situationship" },
  { id: "autre", label: "🎲 Autre" },
];

type Etape = "type" | "conversation" | "generation" | "fini";

function BulleSteve({
  children,
  heure,
}: {
  children: React.ReactNode;
  heure?: string;
}) {
  return (
    <div className="bulle-recue apparait">
      {children}
      {heure && <span className="heure-bulle">{heure}</span>}
    </div>
  );
}

function heureActuelle(): string {
  return new Date().toLocaleTimeString("fr-FR", {
    hour: "2-digit",
    minute: "2-digit",
  });
}

export default function ChatSteve({ prenomCompte }: { prenomCompte: string }) {
  const [etape, setEtape] = useState<Etape>("type");
  const [type, setType] = useState<string | null>(null);
  const [conversation, setConversation] = useState("");
  const [prenom, setPrenom] = useState("");
  const [rapport, setRapport] = useState("");
  const [erreur, setErreur] = useState<string | null>(null);
  const [nomFichier, setNomFichier] = useState<string | null>(null);
  const [copie, setCopie] = useState(false);
  const [donneesSupprimees, setDonneesSupprimees] = useState(false);
  const fichierRef = useRef<HTMLInputElement>(null);
  const finRef = useRef<HTMLDivElement>(null);

  const stats = useMemo(
    () => (conversation.trim() ? analyserConversation(conversation) : null),
    [conversation],
  );

  useEffect(() => {
    finRef.current?.scrollIntoView({ behavior: "smooth", block: "end" });
  }, [etape, rapport, erreur, donneesSupprimees]);

  async function chargerFichier(f: File) {
    if (f.size > 5 * 1024 * 1024) {
      setErreur("Fichier trop volumineux (5 Mo maximum).");
      return;
    }
    setErreur(null);
    setNomFichier(f.name);
    setConversation(await f.text());
  }

  async function envoyer() {
    setErreur(null);
    setRapport("");
    setEtape("generation");
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
      setEtape("fini");
    } catch (e) {
      setErreur(e instanceof Error ? e.message : "Erreur inattendue.");
      setEtape("conversation");
    }
  }

  function titreRapport(): string {
    const m = rapport.match(/^#\s+(.+)$/m);
    return (m ? m[1] : "Conversation").replace(/^Le rapport de Steve — /, "").replace(/[«»]/g, "").trim();
  }

  async function copierRapport() {
    await navigator.clipboard.writeText(rapport);
    setCopie(true);
    setTimeout(() => setCopie(false), 2000);
  }

  async function supprimerMesDonnees() {
    const ok = window.confirm(
      "Supprimer tes données ? Tous les rapports enregistrés dans ton compte seront effacés définitivement. (Rappel : tes conversations, elles, ne sont jamais stockées.)",
    );
    if (!ok) return;
    const reponse = await fetch("/api/rapports", { method: "DELETE" });
    if (reponse.ok) setDonneesSupprimees(true);
  }

  function recommencer() {
    setEtape("type");
    setType(null);
    setConversation("");
    setPrenom("");
    setRapport("");
    setNomFichier(null);
    setErreur(null);
    setDonneesSupprimees(false);
  }

  const pret = conversation.trim().length >= 200;
  const statut =
    etape === "generation"
      ? rapport
        ? "écrit…"
        : "analyse ta conversation…"
      : "en ligne";

  return (
    <div className="mx-auto flex w-full max-w-3xl flex-1 flex-col px-0 sm:px-5 sm:py-6">
      <div className="carte flex flex-1 flex-col overflow-hidden !rounded-none sm:!rounded-2xl">
        {/* En-tête du chat */}
        <div className="flex items-center gap-3 bg-teal px-4 py-3 text-white">
          <Link href="/" aria-label="Retour à l'accueil" className="text-white/80 hover:text-white">
            ←
          </Link>
          <div className="flex h-10 w-10 items-center justify-center rounded-full bg-vert text-base font-bold text-teal">
            S
          </div>
          <div className="flex-1">
            <p className="font-bold leading-tight">Steve</p>
            <p className="text-xs text-white/75">{statut}</p>
          </div>
          <Link
            href="/mes-rapports"
            className="rounded-full bg-white/10 px-3 py-1.5 text-xs font-semibold hover:bg-white/20"
          >
            📁 Mes rapports
          </Link>
        </div>

        {/* Fil de discussion */}
        <div className="papier-peint flex flex-1 flex-col gap-3 overflow-y-auto px-4 py-5 sm:px-6">
          <BulleSteve heure={heureActuelle()}>
            Salut {prenomCompte} ! 👋 Envoie-moi une conversation, je la lis
            en entier, j&apos;analyse tout — et je te dis franchement ce que
            j&apos;en pense. Promis : jamais stockée, juste lue.
          </BulleSteve>
          <BulleSteve>D&apos;abord : c&apos;est quoi comme conversation ?</BulleSteve>

          {etape === "type" && (
            <div className="apparait mt-1 flex flex-wrap gap-2">
              {TYPES.map((t) => (
                <button
                  key={t.id}
                  type="button"
                  className="puce-type"
                  onClick={() => {
                    setType(t.id);
                    setEtape("conversation");
                  }}
                >
                  {t.label}
                </button>
              ))}
            </div>
          )}

          {type && (
            <div className="bulle-envoyee apparait">
              {TYPES.find((t) => t.id === type)?.label}
              <span className="heure-bulle">
                {heureActuelle()} <span className="coches">✓</span>
              </span>
            </div>
          )}

          {etape !== "type" && (
            <BulleSteve>
              Parfait. Envoie-moi l&apos;export WhatsApp avec le trombone 📎
              (Paramètres du chat → Exporter la discussion →{" "}
              <em>Sans les médias</em>), ou colle directement le texte
              ci-dessous. Ajoute ton prénom si tu veux que je sache qui tu es
              dans l&apos;histoire. 😉
            </BulleSteve>
          )}

          {(etape === "conversation" || etape === "generation" || etape === "fini") &&
            stats &&
            stats.nbMessages > 0 && (
              <BulleSteve>
                🔎 Je vois déjà :{" "}
                <strong>
                  {stats.nbMessages.toLocaleString("fr-FR")} messages
                </strong>
                , {stats.participants.length} participant
                {stats.participants.length > 1 ? "s" : ""}
                {stats.premiereDate && stats.derniereDate
                  ? `, du ${stats.premiereDate} au ${stats.derniereDate}`
                  : ""}
                .{" "}
                {stats.participants[0]
                  ? `Le plus bavard : ${stats.participants[0].nom}. `
                  : ""}
                Ça promet.
              </BulleSteve>
            )}

          {erreur && (
            <div className="bulle-recue apparait !border !border-danger/30">
              <span className="text-danger">⚠️ {erreur}</span>
            </div>
          )}

          {(etape === "generation" || etape === "fini") && (
            <div className="bulle-envoyee apparait">
              📄 Conversation envoyée
              {nomFichier ? ` (${nomFichier})` : ""} —{" "}
              {conversation.length.toLocaleString("fr-FR")} caractères
              <span className="heure-bulle">
                {heureActuelle()} <span className="coches">✓</span>
              </span>
            </div>
          )}

          {etape === "generation" && !rapport && (
            <BulleSteve>
              <span className="flex items-center gap-2">
                <span className="points-frappe">
                  <span />
                  <span />
                  <span />
                </span>
                <span className="text-gris">
                  Je lis tout, j&apos;analyse en profondeur. Vraiment tout. 👀
                </span>
              </span>
            </BulleSteve>
          )}

          {rapport && (
            <div className="bulle-recue apparait !max-w-full sm:!max-w-[95%]">
              <div className={`rapport ${etape === "generation" ? "curseur" : ""}`}>
                <ReactMarkdown>{rapport}</ReactMarkdown>
              </div>
            </div>
          )}

          {etape === "fini" && (
            <>
              <BulleSteve heure={heureActuelle()}>
                Voilà. 💚 Ton rapport est enregistré dans{" "}
                <Link href="/mes-rapports" className="font-semibold text-teal-2 underline">
                  ton espace
                </Link>
                . Tu peux le télécharger en PDF, ou tout effacer si tu
                préfères — c&apos;est toi qui décides.
              </BulleSteve>
              <div className="apparait mt-1 flex flex-wrap gap-2">
                <button
                  type="button"
                  className="btn-vert px-4 py-2 text-sm"
                  onClick={() => telechargerRapportPdf(rapport, titreRapport())}
                >
                  ⬇️ Télécharger en PDF
                </button>
                <button
                  type="button"
                  className="btn-blanc px-4 py-2 text-sm"
                  onClick={() => void copierRapport()}
                >
                  {copie ? "Copié ✓" : "Copier"}
                </button>
                <button
                  type="button"
                  className="btn-blanc px-4 py-2 text-sm"
                  onClick={recommencer}
                >
                  Nouveau rapport
                </button>
                <button
                  type="button"
                  className="btn-danger px-4 py-2 text-sm"
                  onClick={() => void supprimerMesDonnees()}
                >
                  🗑️ Supprimer mes données
                </button>
              </div>
              {donneesSupprimees && (
                <BulleSteve>
                  C&apos;est fait ✅ Tous tes rapports sont effacés de nos
                  serveurs. Il ne reste que ce que tu vois à l&apos;écran — et
                  ça disparaîtra en quittant la page.
                </BulleSteve>
              )}
            </>
          )}

          <div ref={finRef} />
        </div>

        {/* Barre de composition */}
        {etape === "conversation" && (
          <div className="border-t border-ligne bg-blanc p-3">
            <div className="flex flex-col gap-2">
              <div className="flex items-end gap-2">
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
                  aria-label="Joindre l'export .txt"
                  title="Joindre l'export .txt"
                  className="flex h-11 w-11 shrink-0 items-center justify-center rounded-full text-xl text-gris transition hover:bg-fond"
                >
                  📎
                </button>
                <textarea
                  value={conversation}
                  onChange={(e) => {
                    setConversation(e.target.value);
                    setNomFichier(null);
                  }}
                  rows={3}
                  placeholder="Colle ta conversation ici…"
                  className="champ !rounded-2xl text-sm"
                />
                <button
                  type="button"
                  onClick={() => void envoyer()}
                  disabled={!pret}
                  aria-label="Envoyer à Steve"
                  title={pret ? "Envoyer à Steve" : "Colle au moins quelques dizaines de messages"}
                  className="btn-vert flex h-11 w-11 shrink-0 items-center justify-center !rounded-full text-lg"
                >
                  ➤
                </button>
              </div>
              <input
                type="text"
                value={prenom}
                onChange={(e) => setPrenom(e.target.value)}
                maxLength={40}
                placeholder="Ton prénom dans la conversation (optionnel)"
                className="champ !w-auto !rounded-full !py-2 text-xs sm:ml-13"
              />
            </div>
          </div>
        )}
      </div>
      <p className="px-5 py-3 text-center text-xs text-gris">
        🔒 Ta conversation sert uniquement à écrire ce rapport — jamais
        stockée, jamais utilisée pour entraîner des modèles.
      </p>
    </div>
  );
}
