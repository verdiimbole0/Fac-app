import "server-only";
import crypto from "node:crypto";
import { cookies, headers } from "next/headers";
import { requete, type Utilisateur } from "./db";

const COOKIE = "steve_session";
const DUREE_SESSION_JOURS = 30;

/* ————— Mots de passe : scrypt (natif Node), sel unique par compte ————— */

const SCRYPT_OPTS = { N: 16384, r: 8, p: 1 };

export function hacherMdp(mdp: string): { hash: string; sel: string } {
  const sel = crypto.randomBytes(16).toString("hex");
  const hash = crypto.scryptSync(mdp, sel, 32, SCRYPT_OPTS).toString("hex");
  return { hash, sel };
}

export function verifierMdp(mdp: string, hash: string, sel: string): boolean {
  const candidat = crypto.scryptSync(mdp, sel, 32, SCRYPT_OPTS);
  const attendu = Buffer.from(hash, "hex");
  return (
    candidat.length === attendu.length &&
    crypto.timingSafeEqual(candidat, attendu)
  );
}

export function validerInscription(
  email: string,
  nom: string,
  mdp: string,
): string | null {
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email) || email.length > 254)
    return "Adresse e-mail invalide.";
  if (nom.length < 2 || nom.length > 60)
    return "Le nom doit faire entre 2 et 60 caractères.";
  if (mdp.length < 10)
    return "Le mot de passe doit faire au moins 10 caractères.";
  if (mdp.length > 200) return "Mot de passe trop long.";
  return null;
}

/* ————— Sessions : jeton opaque aléatoire, stocké haché (révocable) ————— */

function hacherJeton(jeton: string): string {
  return crypto.createHash("sha256").update(jeton).digest("hex");
}

export async function creerSession(utilisateurId: number): Promise<string> {
  const jeton = crypto.randomBytes(32).toString("base64url");
  const expire = new Date(
    Date.now() + DUREE_SESSION_JOURS * 24 * 3600 * 1000,
  ).toISOString();
  await requete(
    "INSERT INTO sessions (utilisateur_id, jeton_hash, expire_le) VALUES ($1, $2, $3)",
    [utilisateurId, hacherJeton(jeton), expire],
  );
  return jeton;
}

export async function poserCookieSession(jeton: string) {
  (await cookies()).set(COOKIE, jeton, {
    httpOnly: true,
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
    path: "/",
    maxAge: DUREE_SESSION_JOURS * 24 * 3600,
  });
}

export async function detruireSession() {
  const magasin = await cookies();
  const jeton = magasin.get(COOKIE)?.value;
  if (jeton) {
    await requete("DELETE FROM sessions WHERE jeton_hash = $1", [
      hacherJeton(jeton),
    ]);
  }
  magasin.delete(COOKIE);
}

export async function utilisateurCourant(): Promise<Utilisateur | null> {
  const jeton = (await cookies()).get(COOKIE)?.value;
  if (!jeton) return null;
  const lignes = await requete<Utilisateur>(
    `SELECT u.* FROM sessions s
     JOIN utilisateurs u ON u.id = s.utilisateur_id
     WHERE s.jeton_hash = $1 AND s.expire_le > now()
       AND u.statut = 'actif'`,
    [hacherJeton(jeton)],
  );
  return lignes[0] ?? null;
}

/* ————— Garde anti-CSRF : les mutations doivent venir du même site ————— */

export async function origineValide(): Promise<boolean> {
  const h = await headers();
  const origine = h.get("origin");
  if (!origine) return true; // requêtes same-origin sans en-tête (rare)
  const hote = h.get("host");
  try {
    return new URL(origine).host === hote;
  } catch {
    return false;
  }
}

/* ————— Limitation de débit en mémoire (par clé) —————
   Sur serverless, chaque instance a son propre compteur : protection
   « meilleur effort », suffisante pour un petit site. ————— */

const compteurs = new Map<string, { n: number; jusqua: number }>();

export function limiteDebit(
  cle: string,
  max: number,
  fenetreMs: number,
): boolean {
  const present = Date.now();
  const entree = compteurs.get(cle);
  if (!entree || entree.jusqua < present) {
    compteurs.set(cle, { n: 1, jusqua: present + fenetreMs });
    return true;
  }
  entree.n += 1;
  return entree.n <= max;
}

export async function ipClient(): Promise<string> {
  const h = await headers();
  return (
    h.get("x-forwarded-for")?.split(",")[0]?.trim() ??
    h.get("x-real-ip") ??
    "inconnue"
  );
}
