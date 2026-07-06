import { useCallback, useState } from "react";
import { View, Text, TextInput, Button, FlatList, StyleSheet } from "react-native";
import { useFocusEffect } from "@react-navigation/native";
import { api, getUser } from "../api";

export default function MessagesScreen({ route }) {
  const { session } = route.params;
  const [messages, setMessages] = useState([]);
  const [content, setContent] = useState("");
  const [error, setError] = useState(null);
  const user = getUser();

  const refresh = useCallback(() => {
    api(`/api/sessions/${session.id}/messages`)
      .then(setMessages)
      .catch((err) => setError(err.message));
  }, [session.id]);

  useFocusEffect(refresh);

  async function handleSend() {
    if (!content.trim()) return;
    setError(null);
    try {
      await api(`/api/sessions/${session.id}/messages`, {
        method: "POST",
        body: JSON.stringify({ content: content.trim() }),
      });
      setContent("");
      refresh();
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <View style={styles.container}>
      {error && <Text style={styles.error}>{error}</Text>}
      <FlatList
        data={messages}
        keyExtractor={(m) => m.id}
        ListEmptyComponent={<Text>Aucun message pour le moment.</Text>}
        renderItem={({ item }) => {
          const mine = item.sender?.id === user?.id;
          return (
            <View style={[styles.bubble, mine ? styles.mine : styles.theirs]}>
              <Text style={styles.sender}>
                {mine ? "Moi" : item.sender?.fullName} ·{" "}
                {new Date(item.createdAt).toLocaleString()}
              </Text>
              {item.content && <Text>{item.content}</Text>}
              {item.attachment && (
                <Text style={styles.attachment}>
                  📎 {item.attachment.fileName} (à télécharger depuis le site web pour l'instant)
                </Text>
              )}
            </View>
          );
        }}
      />
      {/* TODO: dépôt de documents depuis le mobile (expo-document-picker) — déjà possible via le site web */}
      <View style={styles.composer}>
        <TextInput
          style={styles.input}
          placeholder="Ton message..."
          value={content}
          onChangeText={setContent}
          multiline
        />
        <Button title="Envoyer" onPress={handleSend} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16 },
  bubble: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 10,
    marginBottom: 8,
    maxWidth: "85%",
  },
  mine: { alignSelf: "flex-end", backgroundColor: "#e0e7ff" },
  theirs: { alignSelf: "flex-start", backgroundColor: "#fff" },
  sender: { fontSize: 11, color: "#666", marginBottom: 2 },
  attachment: { color: "#1d4ed8", marginTop: 4 },
  composer: { flexDirection: "row", alignItems: "flex-end", gap: 8, marginTop: 8 },
  input: {
    flex: 1,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 10,
    maxHeight: 100,
  },
  error: { color: "red", marginBottom: 8 },
});
