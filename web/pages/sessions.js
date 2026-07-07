import { useEffect, useState } from "react";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:4000";

const TYPE_LABELS = {
  TP: "TP",
  PREPARATION_EXAM: "Préparation examen",
  MEMOIRE_PFE: "Mémoire / PFE",
};

const STATUS_LABELS = {
  REQUESTED: "En attente de confirmation",
  CONFIRMED: "Confirmée",
  COMPLETED: "Effectuée",
  CANCELLED: "Annulée",
};

const PROVIDER_LABELS = {
  ORANGE_MONEY: "Orange Money",
  AIRTEL_MONEY: "Airtel Money",
  MPESA: "M-Pesa",
  FONDEKA: "FONDEKA",
};

function paymentInfo(session) {
  const payments = session.payments || [];
  const success = payments.find((p) => p.status === "SUCCESS");
  if (success) return { paid: true, label: `Payée via ${PROVIDER_LABELS[success.provider]}` };
  const pending = payments.find((p) => p.status === "PENDING");
  if (pending)
    return { paid: false, pending: true, label: `Paiement en cours (réf. ${pending.reference})` };
  return { paid: false, pending: false, label: null };
}

function PayControls({ onPay }) {
  const [provider, setProvider] = useState("ORANGE_MONEY");
  return (
    <span style={{ display: "inline-flex", gap: "0.25rem" }}>
      <select value={provider} onChange={(e) => setProvider(e.target.value)}>
        {Object.entries(PROVIDER_LABELS).map(([value, label]) => (
          <option key={value} value={value}>{label}</option>
        ))}
      </select>
      <button onClick={() => onPay(provider)}>Payer</button>
    </span>
  );
}

export default function Sessions() {
  const [user, setUser] = useState(null);
  const [tutors, setTutors] = useState([]);
  const [sessions, setSessions] = useState([]);
  const [form, setForm] = useState({ tutorId: "", type: "TP", scheduledAt: "", priceUsd: "" });
  const [error, setError] = useState(null);
  const [message, setMessage] = useState(null);

  function authHeaders() {
    return {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("facapp_token")}`,
    };
  }

  async function apiCall(path, options = {}) {
    const res = await fetch(`${API_URL}${path}`, { headers: authHeaders(), ...options });
    const data = await res.json();
    if (!res.ok) {
      const err = data.error;
      throw new Error(typeof err === "string" ? err : "Requête invalide");
    }
    return data;
  }

  async function refreshSessions() {
    setSessions(await apiCall("/api/sessions"));
  }

  useEffect(() => {
    const token = localStorage.getItem("facapp_token");
    const storedUser = localStorage.getItem("facapp_user");
    if (!token || !storedUser) {
      window.location.href = "/login";
      return;
    }
    const parsedUser = JSON.parse(storedUser);
    setUser(parsedUser);
    (async () => {
      try {
        if (parsedUser.role === "STUDENT") {
          setTutors(await apiCall("/api/tutors"));
        }
        await refreshSessions();
      } catch (err) {
        setError(err.message);
      }
    })();
  }, []);

  async function handleBook(e) {
    e.preventDefault();
    setError(null);
    setMessage(null);
    try {
      await apiCall("/api/sessions", {
        method: "POST",
        body: JSON.stringify({
          tutorId: form.tutorId,
          type: form.type,
          scheduledAt: new Date(form.scheduledAt).toISOString(),
          priceUsd: Number(form.priceUsd),
        }),
      });
      setMessage("Créneau demandé ! Le tuteur doit maintenant le confirmer.");
      setForm({ ...form, scheduledAt: "", priceUsd: "" });
      await refreshSessions();
    } catch (err) {
      setError(err.message);
    }
  }

  async function updateStatus(id, action) {
    setError(null);
    setMessage(null);
    try {
      await apiCall(`/api/sessions/${id}/${action}`, { method: "PATCH" });
      await refreshSessions();
    } catch (err) {
      setError(err.message);
    }
  }

  async function pay(sessionId, provider) {
    setError(null);
    setMessage(null);
    try {
      const payment = await apiCall("/api/payments/initiate", {
        method: "POST",
        body: JSON.stringify({ provider, purpose: "SESSION", sessionId }),
      });
      setMessage(
        `Paiement de ${payment.amountUsd} $ initié via ${PROVIDER_LABELS[provider]} (réf. ${payment.reference}). ` +
          "Vous recevrez la demande de confirmation sur votre téléphone une fois les opérateurs raccordés."
      );
      await refreshSessions();
    } catch (err) {
      setError(err.message);
    }
  }

  if (!user) return null;
  const isStudent = user.role === "STUDENT";
  const isTutor = user.role === "TUTOR";

  return (
    <main style={{ fontFamily: "sans-serif", padding: "3rem", maxWidth: 700, margin: "0 auto" }}>
      <p>
        {isStudent && (
          <>
            <a href="/subscription">Abonnement</a>{" · "}
          </>
        )}
        <a href="/profile">Mon profil</a>
      </p>
      <h1>Mes sessions — Fac'App</h1>

      {isStudent && (
        <section style={{ marginBottom: "2rem" }}>
          <h2>Réserver un créneau</h2>
          <form onSubmit={handleBook} style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
            <select
              value={form.tutorId}
              onChange={(e) => setForm({ ...form, tutorId: e.target.value })}
              required
            >
              <option value="">— Choisir un tuteur —</option>
              {tutors.map((t) => (
                <option key={t.id} value={t.id}>
                  {t.fullName}
                  {t.specialites?.length ? ` (${t.specialites.join(", ")})` : ""}
                </option>
              ))}
            </select>
            <select value={form.type} onChange={(e) => setForm({ ...form, type: e.target.value })}>
              {Object.entries(TYPE_LABELS).map(([value, label]) => (
                <option key={value} value={value}>{label}</option>
              ))}
            </select>
            <input
              type="datetime-local"
              value={form.scheduledAt}
              onChange={(e) => setForm({ ...form, scheduledAt: e.target.value })}
              required
            />
            <input
              type="number"
              min="1"
              step="0.5"
              placeholder="Tarif en $ (3-30 $ session, 50-200 $ mémoire/PFE)"
              value={form.priceUsd}
              onChange={(e) => setForm({ ...form, priceUsd: e.target.value })}
              required
            />
            <button type="submit">Demander ce créneau</button>
          </form>
        </section>
      )}

      {error && <p style={{ color: "red" }}>{error}</p>}
      {message && <p style={{ color: "green" }}>{message}</p>}

      <section>
        <h2>{isTutor ? "Créneaux demandés par les étudiants" : "Mes créneaux"}</h2>
        {sessions.length === 0 && <p>Aucune session pour le moment.</p>}
        <ul style={{ listStyle: "none", padding: 0, display: "flex", flexDirection: "column", gap: "0.75rem" }}>
          {sessions.map((s) => {
            const pInfo = paymentInfo(s);
            return (
              <li key={s.id} style={{ border: "1px solid #ccc", borderRadius: 8, padding: "0.75rem" }}>
                <strong>{TYPE_LABELS[s.type]}</strong> — {s.scheduledAt ? new Date(s.scheduledAt).toLocaleString() : "date à définir"}
                <br />
                {isTutor ? `Étudiant : ${s.student?.fullName}` : `Tuteur : ${s.tutor?.user?.fullName}`} — {s.priceUsd} $
                <br />
                Statut : {STATUS_LABELS[s.status]}
                {pInfo.label && (
                  <>
                    <br />
                    Paiement : {pInfo.label} {pInfo.paid && "✓"}
                  </>
                )}
                <div style={{ marginTop: "0.5rem", display: "flex", gap: "0.5rem", flexWrap: "wrap", alignItems: "center" }}>
                  {isTutor && s.status === "REQUESTED" && (
                    <button onClick={() => updateStatus(s.id, "confirm")}>Confirmer</button>
                  )}
                  {isTutor && s.status === "CONFIRMED" && (
                    <button onClick={() => updateStatus(s.id, "complete")}>Marquer effectuée</button>
                  )}
                  {(s.status === "REQUESTED" || s.status === "CONFIRMED") && (
                    <button onClick={() => updateStatus(s.id, "cancel")}>Annuler</button>
                  )}
                  {isStudent && s.status === "CONFIRMED" && !pInfo.paid && !pInfo.pending && (
                    <PayControls onPay={(provider) => pay(s.id, provider)} />
                  )}
                  <a href={`/sessions/${s.id}`}>Messages &amp; documents</a>
                </div>
              </li>
            );
          })}
        </ul>
      </section>
    </main>
  );
}
