import { useEffect, useState } from "react";
import { View, Text, FlatList, TouchableOpacity, StyleSheet } from "react-native";
import { api } from "../api";

export default function TutorsScreen({ navigation }) {
  const [tutors, setTutors] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    api("/api/tutors")
      .then(setTutors)
      .catch((err) => setError(err.message));
  }, []);

  return (
    <View style={styles.container}>
      {error && <Text style={styles.error}>{error}</Text>}
      {!error && tutors.length === 0 && <Text>Aucun tuteur disponible pour le moment.</Text>}
      <FlatList
        data={tutors}
        keyExtractor={(t) => t.id}
        renderItem={({ item }) => (
          <TouchableOpacity
            style={styles.card}
            onPress={() => navigation.navigate("BookSession", { tutor: item })}
          >
            <Text style={styles.name}>{item.fullName}</Text>
            {item.specialites?.length > 0 && (
              <Text style={styles.meta}>{item.specialites.join(", ")}</Text>
            )}
            {item.tarifSession != null && (
              <Text style={styles.meta}>Tarif indicatif : {item.tarifSession} $</Text>
            )}
            {item.bio && <Text style={styles.meta}>{item.bio}</Text>}
          </TouchableOpacity>
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
  name: { fontSize: 16, fontWeight: "bold" },
  meta: { color: "#555", marginTop: 2 },
  error: { color: "red", marginBottom: 12 },
});
