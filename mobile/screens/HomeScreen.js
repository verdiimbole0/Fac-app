import { View, Text, Button, StyleSheet } from "react-native";
import { getUser } from "../api";

export default function HomeScreen({ navigation }) {
  const user = getUser();
  const isStudent = user?.role !== "TUTOR";

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Bienvenue sur Fac'App</Text>
      <Text style={styles.text}>
        Réserve une session avec un tuteur, dépose tes documents, ou consulte ton abonnement.
      </Text>
      <View style={styles.actions}>
        {isStudent && (
          <Button title="Réserver un créneau" onPress={() => navigation.navigate("Tutors")} />
        )}
        <Button title="Mes sessions" onPress={() => navigation.navigate("Sessions")} />
        {isStudent && (
          <Button title="Mon abonnement" onPress={() => navigation.navigate("Subscription")} />
        )}
        <Button title="Mon profil" onPress={() => navigation.navigate("Profile")} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 24 },
  title: { fontSize: 22, fontWeight: "bold", marginBottom: 12 },
  text: { marginBottom: 24 },
  actions: { gap: 12 },
});
