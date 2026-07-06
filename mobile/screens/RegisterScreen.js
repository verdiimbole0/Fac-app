import { useState } from "react";
import { View, Text, TextInput, Button, Switch, StyleSheet, ScrollView, TouchableOpacity } from "react-native";
import { API_URL, setAuth } from "../api";

export default function RegisterScreen({ navigation }) {
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("STUDENT");
  const [filiere, setFiliere] = useState("");
  const [charterAccepted, setCharterAccepted] = useState(false);
  const [error, setError] = useState(null);

  async function handleRegister() {
    setError(null);
    try {
      const res = await fetch(`${API_URL}/api/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          fullName,
          email,
          password,
          role,
          filiere: filiere || undefined,
          acceptedIntegrityCharter: charterAccepted,
        }),
      });
      const data = await res.json();
      if (!res.ok) {
        throw new Error(
          typeof data.error === "string" ? data.error : "Inscription invalide, vérifiez les champs"
        );
      }
      await setAuth(data.token, data.user);
      navigation.replace("Home");
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Créer un compte</Text>

      <TextInput style={styles.input} placeholder="Nom complet" value={fullName} onChangeText={setFullName} />
      <TextInput
        style={styles.input}
        placeholder="Email"
        autoCapitalize="none"
        keyboardType="email-address"
        value={email}
        onChangeText={setEmail}
      />
      <TextInput
        style={styles.input}
        placeholder="Mot de passe (8 caractères minimum)"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />

      <View style={styles.roleRow}>
        {[
          { value: "STUDENT", label: "Étudiant·e" },
          { value: "TUTOR", label: "Tuteur·rice" },
        ].map((r) => (
          <TouchableOpacity
            key={r.value}
            style={[styles.roleButton, role === r.value && styles.roleButtonActive]}
            onPress={() => setRole(r.value)}
          >
            <Text style={role === r.value ? styles.roleTextActive : undefined}>{r.label}</Text>
          </TouchableOpacity>
        ))}
      </View>

      <TextInput
        style={styles.input}
        placeholder="Filière / spécialité (optionnel)"
        value={filiere}
        onChangeText={setFiliere}
      />

      <View style={styles.charterBox}>
        <Text style={styles.charterTitle}>Charte d'intégrité académique</Text>
        <Text style={styles.charterText}>
          Fac'App est un service d'accompagnement pédagogique : les tuteurs expliquent, corrigent
          et guident, mais ne réalisent pas le travail à la place de l'étudiant. Je m'engage à
          utiliser la plateforme dans le respect des règles de mon établissement et à ne pas
          présenter le travail d'un tuteur comme le mien.
        </Text>
        <View style={styles.charterRow}>
          <Switch value={charterAccepted} onValueChange={setCharterAccepted} />
          <Text style={styles.charterAccept}>J'accepte la charte</Text>
        </View>
      </View>

      {error && <Text style={styles.error}>{error}</Text>}
      <Button title="Créer mon compte" onPress={handleRegister} />
      <View style={{ marginTop: 12 }}>
        <Button title="J'ai déjà un compte" onPress={() => navigation.goBack()} />
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { padding: 24 },
  title: { fontSize: 22, fontWeight: "bold", marginBottom: 16, textAlign: "center" },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 12,
    marginBottom: 12,
  },
  roleRow: { flexDirection: "row", gap: 8, marginBottom: 12 },
  roleButton: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    paddingVertical: 8,
    paddingHorizontal: 12,
  },
  roleButtonActive: { backgroundColor: "#1e3a8a", borderColor: "#1e3a8a" },
  roleTextActive: { color: "#fff" },
  charterBox: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 12,
    marginBottom: 12,
  },
  charterTitle: { fontWeight: "bold", marginBottom: 6 },
  charterText: { color: "#555", fontSize: 13, marginBottom: 8 },
  charterRow: { flexDirection: "row", alignItems: "center", gap: 8 },
  charterAccept: { fontWeight: "500" },
  error: { color: "red", marginBottom: 12, textAlign: "center" },
});
