"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";

export default function FormulaireAuth({
  mode,
}: {
  mode: "inscription" | "connexion";
}) {
  const [email, setEmail] = useState("");
  const [nom, setNom] = useState("");
  const [mdp, setMdp] = useState("");
  const [erreur, setErreur] = useState<string | null>(null);
  const [envoi, setEnvoi] = useState(false);
  const router = useRouter();

  async function soumettre(e: React.FormEvent) {
    e.preventDefault();
    setErreur(null);
    setEnvoi(true);
    try {
      const reponse = await fetch(`/api/auth/${mode}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(
          mode === "inscription" ? { email, nom, mdp } : { email, mdp },
        ),
      });
      const corps = await reponse.json().catch(() => null);
      if (!reponse.ok) {
        throw new Error(corps?.erreur ?? `Erreur (${reponse.status}).`);
      }
      router.push("/rapport");
      router.refresh();
    } catch (err) {
      setErreur(err instanceof Error ? err.message : "Erreur inattendue.");
      setEnvoi(false);
    }
  }

  return (
    <form onSubmit={soumettre} className="carte w-full max-w-md p-7">
      <div className="flex items-center gap-3">
        <span className="flex h-11 w-11 items-center justify-center rounded-full bg-vert text-lg font-bold text-teal">
          S
        </span>
        <div>
          <h1 className="text-xl font-extrabold text-teal">
            {mode === "inscription" ? "Créer ton compte" : "Bon retour !"}
          </h1>
          <p className="text-xs text-gris">
            {mode === "inscription"
              ? "Steve t'attend. Ça prend 30 secondes."
              : "Steve a gardé ta place au chaud."}
          </p>
        </div>
      </div>

      <div className="mt-6 flex flex-col gap-4">
        {mode === "inscription" && (
          <div>
            <label htmlFor="nom" className="text-sm font-semibold text-encre">
              Ton prénom (ou pseudo)
            </label>
            <input
              id="nom"
              type="text"
              required
              minLength={2}
              maxLength={60}
              value={nom}
              onChange={(e) => setNom(e.target.value)}
              className="champ mt-1.5"
              placeholder="ex. Karim"
              autoComplete="name"
            />
          </div>
        )}
        <div>
          <label htmlFor="email" className="text-sm font-semibold text-encre">
            Adresse e-mail
          </label>
          <input
            id="email"
            type="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="champ mt-1.5"
            placeholder="toi@exemple.fr"
            autoComplete="email"
          />
        </div>
        <div>
          <label htmlFor="mdp" className="text-sm font-semibold text-encre">
            Mot de passe
          </label>
          <input
            id="mdp"
            type="password"
            required
            minLength={mode === "inscription" ? 10 : 1}
            value={mdp}
            onChange={(e) => setMdp(e.target.value)}
            className="champ mt-1.5"
            placeholder={
              mode === "inscription" ? "10 caractères minimum" : "••••••••••"
            }
            autoComplete={
              mode === "inscription" ? "new-password" : "current-password"
            }
          />
        </div>
      </div>

      {erreur && (
        <p className="mt-4 rounded-xl border border-danger/30 bg-danger/5 p-3 text-sm text-danger">
          {erreur}
        </p>
      )}

      <button
        type="submit"
        disabled={envoi}
        className="btn-vert mt-6 w-full px-6 py-3.5 text-base"
      >
        {envoi
          ? "Un instant…"
          : mode === "inscription"
            ? "Créer mon compte →"
            : "Me connecter →"}
      </button>

      <p className="mt-5 text-center text-sm text-gris">
        {mode === "inscription" ? (
          <>
            Déjà un compte ?{" "}
            <Link href="/connexion" className="font-semibold text-teal-2 hover:underline">
              Connexion
            </Link>
          </>
        ) : (
          <>
            Pas encore de compte ?{" "}
            <Link href="/inscription" className="font-semibold text-teal-2 hover:underline">
              Inscription
            </Link>
          </>
        )}
      </p>
    </form>
  );
}
