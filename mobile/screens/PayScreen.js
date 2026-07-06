import { useState } from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";
import { api } from "../api";

const PROVIDERS = [
  { value: "ORANGE_MONEY", label: "Orange Money" },
  { value: "AIRTEL_MONEY", label: "Airtel Money" },
  { value: "MPESA", label: "M-Pesa" },
  { value: "FONDEKA", label: "FONDEKA" },
];

export default function PayScreen({ route, navigation }) {
  const { session } = route.params;
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  async function handlePay(provider) {
    setError(null);
    try {
      const payment = await api("/api/payments/initiate", {
        method: "POST",
        body: JSON.stringify({ provider, purpose: "SESSION", sessionId: session.id }),
      });
      setResult(payment);
    } catch (err) {
      setError(err.message);
    }
  }

  if (result) {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>Paiement initié ✓</Text>
        <Text style={styles.text}>Montant : {result.amountUsd} $</Text>
        <Text style={styles.text}>Référence : {result.reference}</Text>
        <Text style={styles.note}>
          Vous recevrez la demande de confirmation sur votre téléphone une fois les opérateurs
          raccordés à la plateforme.
        </Text>
        <TouchableOpacity style={styles.provider} onPress={() => navigation.navigate("Sessions")}>
          <Text style={styles.providerText}>Retour à mes sessions</Text>
        </TouchableOpacity>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Payer la session — {session.priceUsd} $</Text>
      <Text style={styles.text}>Choisissez votre moyen de paiement :</Text>
      {PROVIDERS.map((p) => (
        <TouchableOpacity key={p.value} style={styles.provider} onPress={() => handlePay(p.value)}>
          <Text style={styles.providerText}>{p.label}</Text>
        </TouchableOpacity>
      ))}
      {error && <Text style={styles.error}>{error}</Text>}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 24 },
  title: { fontSize: 18, fontWeight: "bold", marginBottom: 12 },
  text: { marginBottom: 12 },
  note: { color: "#555", marginBottom: 16 },
  provider: {
    backgroundColor: "#1e3a8a",
    borderRadius: 8,
    padding: 14,
    marginBottom: 10,
  },
  providerText: { color: "#fff", textAlign: "center", fontWeight: "600" },
  error: { color: "red", marginTop: 8 },
});
