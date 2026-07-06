export const API_URL = "http://localhost:4000"; // à remplacer par l'URL de votre backend déployé

// TODO: stocker le token de façon sécurisée (expo-secure-store) — cf. README, étape dédiée.
let auth = { token: null, user: null };

export function setAuth(token, user) {
  auth = { token, user };
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
