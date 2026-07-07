import { useCallback, useState } from "react";
import { View, Text, TouchableOpacity, ScrollView, StyleSheet } from "react-native";
import { useFocusEffect } from "@react-navigation/native";
import { api } from "../api";

const PLAN_DESCRIPTIONS = {
  DECOUVERTE: "Pour essayer : un suivi léger chaque mois.",
  STANDARD: "Le rythme régulier recommandé pendant le semestre.",
  INTENSIF: "Accompagnement rapproché : examens, mémoire, rattrapage.",
};

const PROVIDERS = [
  { value: "ORANGE_MONEY", label: "Orange Money" },
  { value: "AIRTEL_MONEY", label: "Airtel Money" },
  { value: "MPESA", label: "M-Pesa" },
  { value: "FONDEKA", label: "FONDEKA" },
];

export default function SubscriptionScreen() {
  const [plans, setPlans] = useState({});
  const [current, setCurrent] = useState(null);
  const [provider, setProvider] = useState("ORANGE_MONEY");
  const [error, setError] = useState(null);
  const [message, setMessage] = useState(null);

  const refresh = useCallback(() => {
    Promise.all([api("/api/subscriptions/plans"), api("/api/subscriptions/me")])
      .then(([p, c]) => {
        setPlans(p);
        setCurrent(c);
      })
      .catch((err) => setError(err.message));
  }, []);

  useFocusEffect(refresh);

  async function subscribe(plan) {
    setError(null);
    setMessage(null);
    try {
      const payment = await api("/api/payments/initiate", {
        method: "POST",
        body: JSON.stringify({ provider, purpose: "SUBSCRIPTION", plan }),
      });
      setMessage(
        `Paiement de ${payment.amountUsd} $ initié (réf. ${payment.reference}). ` +
          "L'abonnement sera activé dès la confirmation du paiement."
      );
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <ScrollView contentContainerStyle={styles.container}>
      {current ? (
        <View style={styles.activeBox}>
          <Text style={styles.activeText}>
            Abonnement {current.plan} actif jusqu'au{" "}
            {new Date(current.expiresAt).toLocaleDateString()}. Souscrire à nouveau prolonge de 30
            jours.
          </Text>
        </View>
      ) : (
        <Text style={styles.intro}>
          Aucun abonnement actif. Choisis un plan pour un accompagnement au mois.
        </Text>
      )}

      <Text style={styles.label}>Moyen de paiement</Text>
      <View style={styles.providerRow}>
        {PROVIDERS.map((p) => (
          <TouchableOpacity
            key={p.value}
            style={[styles.providerButton, provider === p.value && styles.providerButtonActive]}
            onPress={() => setProvider(p.value)}
          >
            <Text style={provider === p.value ? styles.providerTextActive : undefined}>
              {p.label}
            </Text>
          </TouchableOpacity>
        ))}
      </View>

      {Object.entries(plans).map(([plan, price]) => (
        <View key={plan} style={styles.planCard}>
          <Text style={styles.planName}>
            {plan.charAt(0) + plan.slice(1).toLowerCase()} — {price} $/mois
          </Text>
          <Text style={styles.planDescription}>{PLAN_DESCRIPTIONS[plan]}</Text>
          <TouchableOpacity style={styles.subscribeButton} onPress={() => subscribe(plan)}>
            <Text style={styles.subscribeText}>Souscrire</Text>
          </TouchableOpacity>
        </View>
      ))}

      {error && <Text style={styles.error}>{error}</Text>}
      {message && <Text style={styles.success}>{message}</Text>}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { padding: 16 },
  intro: { marginBottom: 16 },
  activeBox: {
    backgroundColor: "#ecfdf5",
    borderWidth: 1,
    borderColor: "#10b981",
    borderRadius: 8,
    padding: 12,
    marginBottom: 16,
  },
  activeText: { color: "#065f46" },
  label: { marginBottom: 6, color: "#555" },
  providerRow: { flexDirection: "row", flexWrap: "wrap", gap: 8, marginBottom: 16 },
  providerButton: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    paddingVertical: 6,
    paddingHorizontal: 10,
  },
  providerButtonActive: { backgroundColor: "#1e3a8a", borderColor: "#1e3a8a" },
  providerTextActive: { color: "#fff" },
  planCard: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 14,
    marginBottom: 12,
  },
  planName: { fontSize: 16, fontWeight: "bold" },
  planDescription: { color: "#555", marginVertical: 6 },
  subscribeButton: {
    backgroundColor: "#1e3a8a",
    borderRadius: 8,
    padding: 10,
  },
  subscribeText: { color: "#fff", textAlign: "center", fontWeight: "600" },
  error: { color: "red", marginTop: 8 },
  success: { color: "green", marginTop: 8 },
});
