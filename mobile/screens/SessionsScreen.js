import { useCallback, useState } from "react";
import { View, Text, FlatList, Button, StyleSheet } from "react-native";
import { useFocusEffect } from "@react-navigation/native";
import { api, getUser } from "../api";

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

export default function SessionsScreen() {
  const [sessions, setSessions] = useState([]);
  const [error, setError] = useState(null);
  const user = getUser();
  const isTutor = user?.role === "TUTOR";

  const refresh = useCallback(() => {
    api("/api/sessions")
      .then(setSessions)
      .catch((err) => setError(err.message));
  }, []);

  useFocusEffect(refresh);

  async function updateStatus(id, action) {
    setError(null);
    try {
      await api(`/api/sessions/${id}/${action}`, { method: "PATCH" });
      refresh();
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <View style={styles.container}>
      {error && <Text style={styles.error}>{error}</Text>}
      {!error && sessions.length === 0 && <Text>Aucune session pour le moment.</Text>}
      <FlatList
        data={sessions}
        keyExtractor={(s) => s.id}
        renderItem={({ item }) => (
          <View style={styles.card}>
            <Text style={styles.name}>
              {TYPE_LABELS[item.type]} —{" "}
              {item.scheduledAt ? new Date(item.scheduledAt).toLocaleString() : "date à définir"}
            </Text>
            <Text style={styles.meta}>
              {isTutor
                ? `Étudiant : ${item.student?.fullName}`
                : `Tuteur : ${item.tutor?.user?.fullName}`}{" "}
              — {item.priceUsd} $
            </Text>
            <Text style={styles.meta}>Statut : {STATUS_LABELS[item.status]}</Text>
            <View style={styles.actions}>
              {isTutor && item.status === "REQUESTED" && (
                <Button title="Confirmer" onPress={() => updateStatus(item.id, "confirm")} />
              )}
              {isTutor && item.status === "CONFIRMED" && (
                <Button title="Marquer effectuée" onPress={() => updateStatus(item.id, "complete")} />
              )}
              {(item.status === "REQUESTED" || item.status === "CONFIRMED") && (
                <Button title="Annuler" color="#b91c1c" onPress={() => updateStatus(item.id, "cancel")} />
              )}
            </View>
          </View>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16 },
  card: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 12,
    marginBottom: 12,
  },
  name: { fontSize: 15, fontWeight: "bold" },
  meta: { color: "#555", marginTop: 2 },
  actions: { flexDirection: "row", gap: 8, marginTop: 8, flexWrap: "wrap" },
  error: { color: "red", marginBottom: 12 },
});
