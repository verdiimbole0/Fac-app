import { useCallback, useState } from "react";
import { View, Text, TextInput, Button, ScrollView, StyleSheet } from "react-native";
import { useFocusEffect } from "@react-navigation/native";
import { api, clearAuth } from "../api";

export default function ProfileScreen({ navigation }) {
  const [me, setMe] = useState(null);
  const [bio, setBio] = useState("");
  const [specialites, setSpecialites] = useState("");
  const [tarif, setTarif] = useState("");
  const [error, setError] = useState(null);
  const [message, setMessage] = useState(null);

  const refresh = useCallback(() => {
    api("/api/auth/me")
      .then((data) => {
        setMe(data);
        if (data.tutorProfile) {
          setBio(data.tutorProfile.bio || "");
          setSpecialites((data.tutorProfile.specialites || []).join(", "));
          setTarif(data.tutorProfile.tarifSession != null ? String(data.tutorProfile.tarifSession) : "");
        }
      })
      .catch((err) => setError(err.message));
  }, []);

  useFocusEffect(refresh);

  async function handleSave() {
    setError(null);
    setMessage(null);
    try {
      await api("/api/tutors/me", {
        method: "PUT",
        body: JSON.stringify({
          bio,
          specialites: specialites
            .split(",")
            .map((s) => s.trim())
            .filter(Boolean),
          tarifSession: tarif === "" ? null : Number(tarif),
        }),
      });
      setMessage("Profil mis à jour !");
    } catch (err) {
      setError(err.message);
    }
  }

  async function handleLogout() {
    await clearAuth();
    navigation.reset({ index: 0, routes: [{ name: "Login" }] });
  }

  if (!me) {
    return (
      <View style={styles.container}>
        {error ? <Text style={styles.error}>{error}</Text> : <Text>Chargement...</Text>}
      </View>
    );
  }

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.name}>{me.fullName}</Text>
      <Text style={styles.meta}>{me.email}</Text>
      <Text style={styles.meta}>
        Rôle : {me.role === "TUTOR" ? "Tuteur·rice" : me.role === "STUDENT" ? "Étudiant·e" : me.role}
        {me.filiere ? ` · Filière : ${me.filiere}` : ""}
      </Text>
      {me.subscription && (
        <Text style={styles.meta}>
          Abonnement {me.subscription.plan} actif jusqu'au{" "}
          {new Date(me.subscription.expiresAt).toLocaleDateString()}
        </Text>
      )}

      {me.role === "TUTOR" && (
        <View style={styles.form}>
          <Text style={styles.sectionTitle}>Profil tuteur (visible par les étudiants)</Text>
          <TextInput
            style={[styles.input, styles.multiline]}
            placeholder="Bio : présente ton parcours et ta façon d'accompagner"
            value={bio}
            onChangeText={setBio}
            multiline
          />
          <TextInput
            style={styles.input}
            placeholder="Spécialités, séparées par des virgules"
            value={specialites}
            onChangeText={setSpecialites}
          />
          <TextInput
            style={styles.input}
            placeholder="Tarif indicatif par session en $ (3-200)"
            keyboardType="numeric"
            value={tarif}
            onChangeText={setTarif}
          />
          <Button title="Enregistrer" onPress={handleSave} />
        </View>
      )}

      {error && <Text style={styles.error}>{error}</Text>}
      {message && <Text style={styles.success}>{message}</Text>}

      <View style={{ marginTop: 24 }}>
        <Button title="Se déconnecter" color="#b91c1c" onPress={handleLogout} />
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { padding: 24 },
  name: { fontSize: 20, fontWeight: "bold" },
  meta: { color: "#555", marginTop: 4 },
  form: { marginTop: 20 },
  sectionTitle: { fontWeight: "bold", marginBottom: 8 },
  input: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 12,
    marginBottom: 12,
  },
  multiline: { minHeight: 80, textAlignVertical: "top" },
  error: { color: "red", marginTop: 8 },
  success: { color: "green", marginTop: 8 },
});
