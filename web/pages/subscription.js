import { useEffect, useState } from "react";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:4000";

const PLAN_DESCRIPTIONS = {
  DECOUVERTE: "Pour essayer : un suivi léger chaque mois.",
  STANDARD: "Le rythme régulier recommandé pendant le semestre.",
  INTENSIF: "Accompagnement rapproché : examens, mémoire, rattrapage.",
};

const PROVIDER_LABELS = {
  ORANGE_MONEY: "Orange Money",
  AIRTEL_MONEY: "Airtel Money",
  MPESA: "M-Pesa",
  FONDEKA: "FONDEKA",
};

export default function Subscription() {
  const [user, setUser] = useState(null);
  const [plans, setPlans] = useState({});
  const [current, setCurrent] = useState(null);
  const [provider, setProvider] = useState("ORANGE_MONEY");
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
    const storedUser = localStorage.getItem("facapp_user");
    if (!localStorage.getItem("facapp_token") || !storedUser) {
      window.location.href = "/login";
      return;
    }
    setUser(JSON.parse(storedUser));
    (async () => {
      try {
        setPlans(await apiCall("/api/subscriptions/plans"));
        setCurrent(await apiCall("/api/subscriptions/me"));
      } catch (err) {
        setError(err.message);
      }
    })();
  }, []);

  async function subscribe(plan) {
    setError(null);
    setMessage(null);
    try {
      const payment = await apiCall("/api/payments/initiate", {
        method: "POST",
        body: JSON.stringify({ provider, purpose: "SUBSCRIPTION", plan }),
      });
      setMessage(
        `Paiement de ${payment.amountUsd} $ initié via ${PROVIDER_LABELS[provider]} (réf. ${payment.reference}). ` +
          "L'abonnement sera activé dès la confirmation du paiement."
      );
    } catch (err) {
      setError(err.message);
    }
  }

  if (!user) return null;

  return (
    <main style={{ fontFamily: "sans-serif", padding: "3rem", maxWidth: 700, margin: "0 auto" }}>
      <p>
        <a href="/sessions">← Mes sessions</a>
      </p>
      <h1>Abonnement — Fac'App</h1>

      {current ? (
        <p style={{ background: "#ecfdf5", border: "1px solid #10b981", borderRadius: 8, padding: "0.75rem" }}>
          Abonnement <strong>{current.plan}</strong> actif jusqu'au{" "}
          {new Date(current.expiresAt).toLocaleDateString()}. Souscrire à nouveau prolonge de 30 jours.
        </p>
      ) : (
        <p>Aucun abonnement actif. Choisissez un plan pour un accompagnement au mois.</p>
      )}

      {user.role !== "STUDENT" ? (
        <p>Les abonnements sont réservés aux étudiants.</p>
      ) : (
        <>
          <p>
            Moyen de paiement :{" "}
            <select value={provider} onChange={(e) => setProvider(e.target.value)}>
              {Object.entries(PROVIDER_LABELS).map(([value, label]) => (
                <option key={value} value={value}>{label}</option>
              ))}
            </select>
          </p>

          <div style={{ display: "flex", gap: "1rem", flexWrap: "wrap" }}>
            {Object.entries(plans).map(([plan, price]) => (
              <div
                key={plan}
                style={{ border: "1px solid #ccc", borderRadius: 8, padding: "1rem", flex: "1 1 180px" }}
              >
                <h2 style={{ marginTop: 0 }}>{plan.charAt(0) + plan.slice(1).toLowerCase()}</h2>
                <p style={{ fontSize: "1.5rem", margin: "0.5rem 0" }}>
                  {price} $<span style={{ fontSize: "0.9rem", color: "#555" }}>/mois</span>
                </p>
                <p style={{ color: "#555", fontSize: "0.9rem" }}>{PLAN_DESCRIPTIONS[plan]}</p>
                <button onClick={() => subscribe(plan)}>Souscrire</button>
              </div>
            ))}
          </div>
        </>
      )}

      {error && <p style={{ color: "red" }}>{error}</p>}
      {message && <p style={{ color: "green" }}>{message}</p>}
    </main>
  );
}
