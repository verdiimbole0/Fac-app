import { useEffect, useState } from "react";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:4000";

export default function Profile() {
  const [me, setMe] = useState(null);
  const [form, setForm] = useState({ bio: "", specialites: "", tarifSession: "" });
  const [error, setError] = useState(null);
  const [message, setMessage] = useState(null);

  async function apiCall(path, options = {}) {
    const res = await fetch(`${API_URL}${path}`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("facapp_token")}`,
      },
      ...options,
    });
    const data = await res.json();
    if (!res.ok) {
      throw new Error(typeof data.error === "string" ? data.error : "Requête invalide");
    }
    return data;
  }

  useEffect(() => {
    if (!localStorage.getItem("facapp_token")) {
      window.location.href = "/login";
      return;
    }
    (async () => {
      try {
        const data = await apiCall("/api/auth/me");
        setMe(data);
        if (data.tutorProfile) {
          setForm({
            bio: data.tutorProfile.bio || "",
            specialites: (data.tutorProfile.specialites || []).join(", "),
            tarifSession: data.tutorProfile.tarifSession ?? "",
          });
        }
      } catch (err) {
        setError(err.message);
      }
    })();
  }, []);

  async function handleSave(e) {
    e.preventDefault();
    setError(null);
    setMessage(null);
    try {
      await apiCall("/api/tutors/me", {
        method: "PUT",
        body: JSON.stringify({
          bio: form.bio,
          specialites: form.specialites
            .split(",")
            .map((s) => s.trim())
            .filter(Boolean),
          tarifSession: form.tarifSession === "" ? null : Number(form.tarifSession),
        }),
      });
      setMessage("Profil mis à jour !");
    } catch (err) {
      setError(err.message);
    }
  }

  function logout() {
    localStorage.removeItem("facapp_token");
    localStorage.removeItem("facapp_user");
    window.location.href = "/";
  }

  if (!me) return null;

  return (
    <main style={{ fontFamily: "sans-serif", padding: "3rem", maxWidth: 600, margin: "0 auto" }}>
      <p>
        <a href="/sessions">← Mes sessions</a>
      </p>
      <h1>Mon profil</h1>
      <p>
        <strong>{me.fullName}</strong> — {me.email}
        <br />
        Rôle : {me.role === "TUTOR" ? "Tuteur·rice" : me.role === "STUDENT" ? "Étudiant·e" : me.role}
        {me.filiere && <> · Filière : {me.filiere}</>}
      </p>
      {me.subscription && (
        <p>
          Abonnement <strong>{me.subscription.plan}</strong> actif jusqu'au{" "}
          {new Date(me.subscription.expiresAt).toLocaleDateString()}
        </p>
      )}

      {me.role === "TUTOR" && (
        <form onSubmit={handleSave} style={{ display: "flex", flexDirection: "column", gap: "0.75rem", marginTop: "1rem" }}>
          <h2>Profil tuteur (visible par les étudiants)</h2>
          <textarea
            rows={4}
            placeholder="Bio : présente ton parcours et ta façon d'accompagner"
            value={form.bio}
            onChange={(e) => setForm({ ...form, bio: e.target.value })}
          />
          <input
            type="text"
            placeholder="Spécialités, séparées par des virgules (ex: Analyse, Algorithmique)"
            value={form.specialites}
            onChange={(e) => setForm({ ...form, specialites: e.target.value })}
          />
          <input
            type="number"
            min="3"
            max="200"
            step="0.5"
            placeholder="Tarif indicatif par session en $ (3-200)"
            value={form.tarifSession}
            onChange={(e) => setForm({ ...form, tarifSession: e.target.value })}
          />
          <button type="submit">Enregistrer</button>
        </form>
      )}

      {error && <p style={{ color: "red" }}>{error}</p>}
      {message && <p style={{ color: "green" }}>{message}</p>}

      <p style={{ marginTop: "2rem" }}>
        <button onClick={logout}>Se déconnecter</button>
      </p>
    </main>
  );
}
