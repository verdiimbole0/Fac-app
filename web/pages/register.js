import { useState } from "react";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:4000";

export default function Register() {
  const [form, setForm] = useState({
    fullName: "",
    email: "",
    password: "",
    role: "STUDENT",
    filiere: "",
    acceptedIntegrityCharter: false,
  });
  const [error, setError] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    setError(null);
    try {
      const res = await fetch(`${API_URL}/api/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          fullName: form.fullName,
          email: form.email,
          password: form.password,
          role: form.role,
          filiere: form.filiere || undefined,
          acceptedIntegrityCharter: form.acceptedIntegrityCharter,
        }),
      });
      const data = await res.json();
      if (!res.ok) {
        const err = data.error;
        throw new Error(typeof err === "string" ? err : "Inscription invalide, vérifiez les champs");
      }
      localStorage.setItem("facapp_token", data.token);
      localStorage.setItem("facapp_user", JSON.stringify(data.user));
      window.location.href = "/sessions";
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <main style={{ fontFamily: "sans-serif", padding: "3rem", maxWidth: 480, margin: "0 auto" }}>
      <h1>Inscription — Fac'App</h1>
      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
        <input
          type="text"
          placeholder="Nom complet"
          value={form.fullName}
          onChange={(e) => setForm({ ...form, fullName: e.target.value })}
          required
        />
        <input
          type="email"
          placeholder="Email"
          value={form.email}
          onChange={(e) => setForm({ ...form, email: e.target.value })}
          required
        />
        <input
          type="password"
          placeholder="Mot de passe (8 caractères minimum)"
          minLength={8}
          value={form.password}
          onChange={(e) => setForm({ ...form, password: e.target.value })}
          required
        />
        <select value={form.role} onChange={(e) => setForm({ ...form, role: e.target.value })}>
          <option value="STUDENT">Étudiant·e</option>
          <option value="TUTOR">Tuteur·rice</option>
        </select>
        <input
          type="text"
          placeholder="Filière / spécialité (optionnel)"
          value={form.filiere}
          onChange={(e) => setForm({ ...form, filiere: e.target.value })}
        />

        <fieldset style={{ border: "1px solid #ccc", borderRadius: 8, padding: "0.75rem" }}>
          <legend>Charte d'intégrité académique</legend>
          <p style={{ fontSize: "0.85rem", color: "#555" }}>
            Fac'App est un service d'accompagnement pédagogique : les tuteurs expliquent,
            corrigent et guident, mais ne réalisent pas le travail à la place de l'étudiant.
            Je m'engage à utiliser la plateforme dans le respect des règles de mon
            établissement et à ne pas présenter le travail d'un tuteur comme le mien.
          </p>
          <label style={{ fontSize: "0.9rem" }}>
            <input
              type="checkbox"
              checked={form.acceptedIntegrityCharter}
              onChange={(e) => setForm({ ...form, acceptedIntegrityCharter: e.target.checked })}
              required
            />{" "}
            J'accepte la charte d'intégrité académique
          </label>
        </fieldset>

        {error && <p style={{ color: "red" }}>{error}</p>}
        <button type="submit">Créer mon compte</button>
      </form>
      <p>
        Déjà un compte ? <a href="/login">Se connecter</a>
      </p>
    </main>
  );
}
