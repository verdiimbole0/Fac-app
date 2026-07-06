import { useCallback, useState } from "react";
import { View, Text, TextInput, Button, FlatList, StyleSheet, TouchableOpacity } from "react-native";
import { useFocusEffect } from "@react-navigation/native";
import * as DocumentPicker from "expo-document-picker";
import { api, apiUpload, getUser } from "../api";

export default function MessagesScreen({ route }) {
  const { session } = route.params;
  const [messages, setMessages] = useState([]);
  const [content, setContent] = useState("");
  const [attachment, setAttachment] = useState(null);
  const [sending, setSending] = useState(false);
  const [error, setError] = useState(null);
  const user = getUser();

  const refresh = useCallback(() => {
    api(`/api/sessions/${session.id}/messages`)
      .then(setMessages)
      .catch((err) => setError(err.message));
  }, [session.id]);

  useFocusEffect(refresh);

  async function pickDocument() {
    const result = await DocumentPicker.getDocumentAsync({ copyToCacheDirectory: true });
    if (!result.canceled && result.assets?.length) {
      setAttachment(result.assets[0]);
    }
  }

  async function handleSend() {
    if (!content.trim() && !attachment) return;
    setError(null);
    setSending(true);
    try {
      if (attachment) {
        const form = new FormData();
        if (content.trim()) form.append("content", content.trim());
        form.append("file", {
          uri: attachment.uri,
          name: attachment.name,
          type: attachment.mimeType || "application/octet-stream",
        });
        await apiUpload(`/api/sessions/${session.id}/messages`, form);
      } else {
        await api(`/api/sessions/${session.id}/messages`, {
          method: "POST",
          body: JSON.stringify({ content: content.trim() }),
        });
      }
      setContent("");
      setAttachment(null);
      refresh();
    } catch (err) {
      setError(err.message);
    } finally {
      setSending(false);
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
                  📎 {item.attachment.fileName} (téléchargeable depuis le site web)
                </Text>
              )}
            </View>
          );
        }}
      />
      {attachment && (
        <View style={styles.attachmentRow}>
          <Text style={styles.attachment} numberOfLines={1}>
            📎 {attachment.name}
          </Text>
          <TouchableOpacity onPress={() => setAttachment(null)}>
            <Text style={styles.removeAttachment}>✕</Text>
          </TouchableOpacity>
        </View>
      )}
      <View style={styles.composer}>
        <TouchableOpacity style={styles.attachButton} onPress={pickDocument}>
          <Text style={styles.attachButtonText}>📎</Text>
        </TouchableOpacity>
        <TextInput
          style={styles.input}
          placeholder="Ton message..."
          value={content}
          onChangeText={setContent}
          multiline
        />
        <Button title={sending ? "Envoi..." : "Envoyer"} onPress={handleSend} disabled={sending} />
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
  attachmentRow: { flexDirection: "row", alignItems: "center", gap: 8, marginTop: 8 },
  removeAttachment: { color: "#b91c1c", fontSize: 16, paddingHorizontal: 6 },
  attachButton: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 10,
  },
  attachButtonText: { fontSize: 16 },
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
