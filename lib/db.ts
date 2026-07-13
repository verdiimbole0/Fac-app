// Couche base de données : Postgres partout.
// - En production : Neon (gratuit) via DATABASE_URL — compatible serverless (Vercel).
// - En local : PGlite (Postgres embarqué), persisté dans donnees/pg, zéro configuration.
// Les conversations ne sont JAMAIS stockées ici : uniquement les comptes,
// les sessions et les rapports générés, effaçables par l'utilisateur.

type Ligne = Record<string, unknown>;
type Executeur = (texte: string, params?: unknown[]) => Promise<Ligne[]>;

const SCHEMA = `
CREATE TABLE IF NOT EXISTS utilisateurs (
  id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  nom TEXT NOT NULL,
  mdp_hash TEXT NOT NULL,
  sel TEXT NOT NULL,
  role TEXT NOT NULL DEFAULT 'membre' CHECK (role IN ('admin','membre')),
  statut TEXT NOT NULL DEFAULT 'actif' CHECK (statut IN ('actif','suspendu')),
  cree_le TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS sessions (
  id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  utilisateur_id INTEGER NOT NULL REFERENCES utilisateurs(id) ON DELETE CASCADE,
  jeton_hash TEXT NOT NULL UNIQUE,
  expire_le TIMESTAMPTZ NOT NULL,
  cree_le TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_sessions_jeton ON sessions(jeton_hash);
CREATE TABLE IF NOT EXISTS rapports (
  id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  utilisateur_id INTEGER NOT NULL REFERENCES utilisateurs(id) ON DELETE CASCADE,
  titre TEXT NOT NULL,
  type TEXT NOT NULL,
  contenu TEXT NOT NULL,
  cree_le TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_rapports_utilisateur ON rapports(utilisateur_id);
`;

async function initialiser(): Promise<Executeur> {
  if (process.env.DATABASE_URL) {
    const { neon } = await import("@neondatabase/serverless");
    const sql = neon(process.env.DATABASE_URL);
    for (const instruction of SCHEMA.split(";").map((s) => s.trim()).filter(Boolean)) {
      await sql.query(instruction);
    }
    return async (texte, params) => {
      // Selon la version du pilote, query() renvoie les lignes directement
      // ou un objet { rows } complet.
      const resultat = (await sql.query(texte, params as unknown[])) as unknown;
      if (Array.isArray(resultat)) return resultat as Ligne[];
      return (resultat as { rows: Ligne[] }).rows;
    };
  }

  if (process.env.VERCEL) {
    throw new Error(
      "DATABASE_URL manquante : sur Vercel, crée une base Neon (gratuite) et renseigne DATABASE_URL dans les variables d'environnement du projet.",
    );
  }

  // Local : Postgres embarqué, persisté sur disque, aucune configuration.
  const { mkdirSync } = await import("node:fs");
  mkdirSync("donnees/pg", { recursive: true });
  const { PGlite } = await import("@electric-sql/pglite");
  const pg = new PGlite("donnees/pg");
  await pg.exec(SCHEMA);
  return async (texte, params) => {
    const resultat = await pg.query(texte, params as unknown[]);
    return resultat.rows as Ligne[];
  };
}

declare global {
  var __steveExecuteur: Promise<Executeur> | undefined;
}

/** Exécute une requête SQL paramétrée ($1, $2…) et renvoie les lignes. */
export function requete<T = Ligne>(
  texte: string,
  params?: unknown[],
): Promise<T[]> {
  globalThis.__steveExecuteur ??= initialiser();
  return globalThis.__steveExecuteur.then((exec) => exec(texte, params)) as Promise<T[]>;
}

export interface Utilisateur {
  id: number;
  email: string;
  nom: string;
  mdp_hash: string;
  sel: string;
  role: "admin" | "membre";
  statut: "actif" | "suspendu";
  cree_le: string;
}

export interface Rapport {
  id: number;
  utilisateur_id: number;
  titre: string;
  type: string;
  contenu: string;
  cree_le: string;
}

/** Rend un horodatage lisible côté SQL, stable quel que soit le pilote. */
export const COL_CREE_LE = `to_char(cree_le AT TIME ZONE 'UTC', 'YYYY-MM-DD"T"HH24:MI:SS') AS cree_le`;
