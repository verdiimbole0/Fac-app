import Database from "better-sqlite3";
import fs from "node:fs";
import path from "node:path";

// Base locale : les conversations ne sont JAMAIS stockées ici.
// On ne conserve que les comptes, les sessions et les rapports générés
// (pour relecture / PDF), que l'utilisateur peut effacer à tout moment.

const DOSSIER = path.join(process.cwd(), "donnees");
const FICHIER = path.join(DOSSIER, "steve.db");

declare global {
  var __steveDb: Database.Database | undefined;
}

function ouvrir(): Database.Database {
  fs.mkdirSync(DOSSIER, { recursive: true });
  const db = new Database(FICHIER);
  db.pragma("journal_mode = WAL");
  db.pragma("foreign_keys = ON");
  db.exec(`
    CREATE TABLE IF NOT EXISTS utilisateurs (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      email TEXT NOT NULL UNIQUE,
      nom TEXT NOT NULL,
      mdp_hash TEXT NOT NULL,
      sel TEXT NOT NULL,
      role TEXT NOT NULL DEFAULT 'membre' CHECK (role IN ('admin','membre')),
      statut TEXT NOT NULL DEFAULT 'actif' CHECK (statut IN ('actif','suspendu')),
      cree_le TEXT NOT NULL DEFAULT (datetime('now'))
    );
    CREATE TABLE IF NOT EXISTS sessions (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      utilisateur_id INTEGER NOT NULL REFERENCES utilisateurs(id) ON DELETE CASCADE,
      jeton_hash TEXT NOT NULL UNIQUE,
      expire_le TEXT NOT NULL,
      cree_le TEXT NOT NULL DEFAULT (datetime('now'))
    );
    CREATE INDEX IF NOT EXISTS idx_sessions_jeton ON sessions(jeton_hash);
    CREATE TABLE IF NOT EXISTS rapports (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      utilisateur_id INTEGER NOT NULL REFERENCES utilisateurs(id) ON DELETE CASCADE,
      titre TEXT NOT NULL,
      type TEXT NOT NULL,
      contenu TEXT NOT NULL,
      cree_le TEXT NOT NULL DEFAULT (datetime('now'))
    );
    CREATE INDEX IF NOT EXISTS idx_rapports_utilisateur ON rapports(utilisateur_id);
  `);
  return db;
}

// Réutilise la connexion entre rechargements (dev) et entre requêtes.
export function db(): Database.Database {
  if (!globalThis.__steveDb) globalThis.__steveDb = ouvrir();
  return globalThis.__steveDb;
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
