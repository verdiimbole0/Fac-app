import { useState } from "react";
import { View, Text, TextInput, Button, TouchableOpacity, StyleSheet } from "react-native";
import { api } from "../api";

const TYPES = [
  { value: "TP", label: "TP" },
  { value: "PREPARATION_EXAM", label: "Préparation examen" },
  { value: "MEMOIRE_PFE", label: "Mémoire / PFE" },
];

export default function BookSessionScreen({ route, navigation }) {
  const { tutor } = route.params;
  const [type, setType] = useState("TP");
  const [date, setDate] = useState(""); // format attendu : AAAA-MM-JJ
  const [time, setTime] = useState(""); // format attendu : HH:MM
  const [price, setPrice] = useState("");
  const [error, setError] = useState(null);

  async function handleBook() {
    setError(null);
    const scheduledAt = new Date(`${date}T${time}:00`);
    if (isNaN(scheduledAt.getTime())) {
      setError("Date ou heure invalide (formats attendus : AAAA-MM-JJ et HH:MM)");
      return;
    }
    try {
      await api("/api/sessions", {
        method: "POST",
        body: JSON.stringify({
          tutorId: tutor.id,
          type,
          scheduledAt: scheduledAt.toISOString(),
          priceUsd: Number(price),
        }),
      });
      navigation.replace("Sessions");
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Créneau avec {tutor.fullName}</Text>

      <Text style={styles.label}>Type de session</Text>
      <View style={styles.typeRow}>
        {TYPES.map((t) => (
          <TouchableOpacity
            key={t.value}
            style={[styles.typeButton, type === t.value && styles.typeButtonActive]}
            onPress={() => setType(t.value)}
          >
            <Text style={type === t.value ? styles.typeTextActive : undefined}>{t.label}</Text>
          </TouchableOpacity>
        ))}
      </View>

      <Text style={styles.label}>Date (AAAA-MM-JJ)</Text>
      <TextInput style={styles.input} placeholder="2026-07-15" value={date} onChangeText={setDate} />

      <Text style={styles.label}>Heure (HH:MM)</Text>
      <TextInput style={styles.input} placeholder="14:00" value={time} onChangeText={setTime} />

      <Text style={styles.label}>Tarif en $ (3-30 $ session, 50-200 $ mémoire/PFE)</Text>
      <TextInput
        style={styles.input}
        placeholder="10"
        keyboardType="numeric"
        value={price}
        onChangeText={setPrice}
      />

      {error && <Text style={styles.error}>{error}</Text>}
      <Button title="Demander ce créneau" onPress={handleBook} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 24 },
  title: { fontSize: 18, fontWeight: "bold", marginBottom: 16 },
  label: { marginBottom: 4, color: "#555" },
  typeRow: { flexDirection: "row", gap: 8, marginBottom: 12, flexWrap: "wrap" },
  typeButton: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    paddingVertical: 6,
    paddingHorizontal: 10,
  },
  typeButtonActive: { backgroundColor: "#1e3a8a", borderColor: "#1e3a8a" },
  typeTextActive: { color: "#fff" },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 12,
    marginBottom: 12,
  },
  error: { color: "red", marginBottom: 12 },
});
