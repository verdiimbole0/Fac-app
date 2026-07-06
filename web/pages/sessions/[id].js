import { useEffect, useRef, useState } from "react";
import { useRouter } from "next/router";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:4000";

function formatSize(bytes) {
  if (bytes == null) return "";
  if (bytes < 1024) return `${bytes} o`;
  if (bytes < 1024 * 1024) return `${Math.round(bytes / 1024)} Ko`;
  return `${(bytes / (1024 * 1024)).toFixed(1)} Mo`;
}

export default function SessionThread() {
  const router = useRouter();
  const { id } = router.query;
  const [user, setUser] = useState(null);
  const [messages, setMessages] = useState([]);
  const [content, setContent] = useState("");
  const [error, setError] = useState(null);
  const [sending, setSending] = useState(false);
  const fileRef = useRef(null);

  function token() {
    return localStorage.getItem("facapp_token");
  }

  async function refresh() {
    const res = await fetch(`${API_URL}/api/sessions/${id}/messages`, {
      headers: { Authorization: `Bearer ${token()}` },
    });
    const data = await res.json();
    if (!res.ok) {
      throw new Error(typeof data.error === "string" ? data.error : "Erreur de chargement");
    }
    setMessages(data);
  }

  useEffect(() => {
    if (!id) return;
    const storedUser = localStorage.getItem("facapp_user");
    if (!token() || !storedUser) {
      window.location.href = "/login";
      return;
    }
    setUser(JSON.parse(storedUser));
    refresh().catch((err) => setError(err.message));
  }, [id]);

  async function handleSend(e) {
    e.preventDefault();
    setError(null);
    const file = fileRef.current?.files?.[0];
    if (!content.trim() && !file) {
      setError("Écrivez un message ou joignez un document");
      return;
    }
    setSending(true);
    try {
      const body = new FormData();
      if (content.trim()) body.append("content", content.trim());
      if (file) body.append("file", file);
      const res = await fetch(`${API_URL}/api/sessions/${id}/messages`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token()}` },
        body,
      });
      const data = await res.json();
      if (!res.ok) {
        throw new Error(typeof data.error === "string" ? data.error : "Envoi impossible");
      }
      setContent("");
      if (fileRef.current) fileRef.current.value = "";
      await refresh();
    } catch (err) {
      setError(err.message);
    } finally {
      setSending(false);
    }
  }

  async function downloadAttachment(messageId, fileName) {
    setError(null);
    try {
      const res = await fetch(`${API_URL}/api/sessions/${id}/messages/${messageId}/file`, {
        headers: { Authorization: `Bearer ${token()}` },
      });
      if (!res.ok) throw new Error("Téléchargement impossible");
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = fileName;
      a.click();
      URL.revokeObjectURL(url);
    } catch (err) {
      setError(err.message);
    }
  }

  if (!user) return null;

  return (
    <main style={{ fontFamily: "sans-serif", padding: "3rem", maxWidth: 700, margin: "0 auto" }}>
      <p>
        <a href="/sessions">← Mes sessions</a>
      </p>
      <h1>Messages de la session</h1>
      <p style={{ color: "#555", fontSize: "0.9rem" }}>
        Dépose tes documents (TP, brouillons...) et échange avec {user.role === "TUTOR" ? "l'étudiant·e" : "ton tuteur·rice"}.
      </p>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <ul style={{ listStyle: "none", padding: 0, display: "flex", flexDirection: "column", gap: "0.75rem" }}>
        {messages.length === 0 && <li>Aucun message pour le moment.</li>}
        {messages.map((m) => {
          const mine = m.sender?.id === user.id;
          return (
            <li
              key={m.id}
              style={{
                border: "1px solid #ccc",
                borderRadius: 8,
                padding: "0.75rem",
                background: mine ? "#eef2ff" : "#fff",
                alignSelf: mine ? "flex-end" : "flex-start",
                maxWidth: "85%",
              }}
            >
              <strong>{mine ? "Moi" : m.sender?.fullName}</strong>{" "}
              <span style={{ color: "#888", fontSize: "0.8rem" }}>
                {new Date(m.createdAt).toLocaleString()}
              </span>
              {m.content && <p style={{ margin: "0.5rem 0 0" }}>{m.content}</p>}
              {m.attachment && (
                <p style={{ margin: "0.5rem 0 0" }}>
                  📎{" "}
                  <button
                    onClick={() => downloadAttachment(m.id, m.attachment.fileName)}
                    style={{ background: "none", border: "none", color: "#1d4ed8", cursor: "pointer", padding: 0, textDecoration: "underline" }}
                  >
                    {m.attachment.fileName}
                  </button>{" "}
                  <span style={{ color: "#888", fontSize: "0.8rem" }}>({formatSize(m.attachment.sizeBytes)})</span>
                </p>
              )}
            </li>
          );
        })}
      </ul>

      <form onSubmit={handleSend} style={{ display: "flex", flexDirection: "column", gap: "0.5rem", marginTop: "1rem" }}>
        <textarea
          rows={3}
          placeholder="Ton message..."
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <input type="file" ref={fileRef} />
        <button type="submit" disabled={sending}>
          {sending ? "Envoi..." : "Envoyer"}
        </button>
      </form>
    </main>
  );
}
