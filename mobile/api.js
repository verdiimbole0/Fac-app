import * as SecureStore from "expo-secure-store";

// URL du backend : définir EXPO_PUBLIC_API_URL (fichier .env ou variable EAS)
// avec l'URL du backend déployé ; localhost par défaut en développement.
export const API_URL = process.env.EXPO_PUBLIC_API_URL || "http://localhost:4000";

const AUTH_KEY = "facapp_auth";

let auth = { token: null, user: null };

export async function setAuth(token, user) {
  auth = { token, user };
  await SecureStore.setItemAsync(AUTH_KEY, JSON.stringify(auth));
}

// Recharge la session stockée au lancement de l'app ; retourne l'utilisateur ou null.
export async function loadAuth() {
  const raw = await SecureStore.getItemAsync(AUTH_KEY);
  if (raw) {
    auth = JSON.parse(raw);
  }
  return auth.user;
}

export async function clearAuth() {
  auth = { token: null, user: null };
  await SecureStore.deleteItemAsync(AUTH_KEY);
}

export function getUser() {
  return auth.user;
}

export async function api(path, options = {}) {
  const res = await fetch(`${API_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(auth.token ? { Authorization: `Bearer ${auth.token}` } : {}),
      ...options.headers,
    },
  });
  const data = await res.json();
  if (!res.ok) {
    const err = data.error;
    throw new Error(typeof err === "string" ? err : "Requête invalide");
  }
  return data;
}

// Envoi multipart (documents) — le Content-Type est posé par fetch avec la boundary.
export async function apiUpload(path, formData) {
  const res = await fetch(`${API_URL}${path}`, {
    method: "POST",
    headers: auth.token ? { Authorization: `Bearer ${auth.token}` } : {},
    body: formData,
  });
  const data = await res.json();
  if (!res.ok) {
    const err = data.error;
    throw new Error(typeof err === "string" ? err : "Envoi impossible");
  }
  return data;
}
