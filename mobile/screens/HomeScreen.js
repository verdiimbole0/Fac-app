import { View, Text, StyleSheet } from "react-native";

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Bienvenue sur Fac'App</Text>
      <Text>
        Réserve une session avec un tuteur, dépose tes documents, ou consulte ton abonnement.
      </Text>
      {/* TODO: liste des tuteurs disponibles, réservation de créneaux, accès à l'abonnement */}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 24 },
  title: { fontSize: 22, fontWeight: "bold", marginBottom: 12 },
});
