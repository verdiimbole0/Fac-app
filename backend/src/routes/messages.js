const express = require("express");
const path = require("path");
const crypto = require("crypto");
const multer = require("multer");
const { z } = require("zod");
const { PrismaClient } = require("@prisma/client");
const { requireAuth } = require("../middleware/auth");
const { UPLOADS_DIR, saveFile, sendFile } = require("../storage");

const router = express.Router();
const prisma = new PrismaClient();

const upload = multer({
  storage: multer.diskStorage({
    destination: UPLOADS_DIR,
    filename: (_req, file, cb) => {
      cb(null, `${crypto.randomUUID()}${path.extname(file.originalname)}`);
    },
  }),
  limits: { fileSize: 20 * 1024 * 1024 }, // 20 Mo max par document
});

// Vérifie que l'utilisateur connecté participe à la session (étudiant, tuteur ou admin).
async function loadSessionForUser(req, res) {
  const session = await prisma.session.findUnique({
    where: { id: req.params.id },
    include: { tutor: true },
  });
  if (!session) {
    res.status(404).json({ error: "Session introuvable" });
    return null;
  }
  const isParticipant =
    session.studentId === req.user.userId ||
    session.tutor.userId === req.user.userId ||
    req.user.role === "ADMIN";
  if (!isParticipant) {
    res.status(403).json({ error: "Accès refusé" });
    return null;
  }
  return session;
}

// Fil de discussion d'une session, du plus ancien au plus récent.
router.get("/:id/messages", requireAuth, async (req, res) => {
  const session = await loadSessionForUser(req, res);
  if (!session) return;

  const messages = await prisma.message.findMany({
    where: { sessionId: session.id },
    orderBy: { createdAt: "asc" },
    include: { sender: { select: { id: true, fullName: true, role: true } } },
  });

  res.json(
    messages.map((m) => ({
      id: m.id,
      content: m.content,
      createdAt: m.createdAt,
      sender: m.sender,
      attachment: m.fileName
        ? { fileName: m.fileName, mimeType: m.mimeType, sizeBytes: m.sizeBytes }
        : null,
    }))
  );
});

const sendSchema = z.object({
  content: z.string().min(1).max(5000).optional(),
});

// Envoi d'un message : texte, document joint (champ multipart "file"), ou les deux.
router.post("/:id/messages", requireAuth, upload.single("file"), async (req, res) => {
  const session = await loadSessionForUser(req, res);
  if (!session) return;

  const parsed = sendSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.flatten() });
  }
  const { content } = parsed.data;

  if (!content && !req.file) {
    return res.status(400).json({ error: "Message vide : texte ou document requis" });
  }

  if (req.file) {
    await saveFile(req.file.filename, req.file.mimetype);
  }

  const message = await prisma.message.create({
    data: {
      sessionId: session.id,
      senderId: req.user.userId,
      content: content || null,
      fileName: req.file ? req.file.originalname : null,
      storedName: req.file ? req.file.filename : null,
      mimeType: req.file ? req.file.mimetype : null,
      sizeBytes: req.file ? req.file.size : null,
    },
    include: { sender: { select: { id: true, fullName: true, role: true } } },
  });

  res.status(201).json({
    id: message.id,
    content: message.content,
    createdAt: message.createdAt,
    sender: message.sender,
    attachment: message.fileName
      ? { fileName: message.fileName, mimeType: message.mimeType, sizeBytes: message.sizeBytes }
      : null,
  });
});

// Téléchargement du document joint à un message.
router.get("/:id/messages/:messageId/file", requireAuth, async (req, res) => {
  const session = await loadSessionForUser(req, res);
  if (!session) return;

  const message = await prisma.message.findUnique({ where: { id: req.params.messageId } });
  if (!message || message.sessionId !== session.id || !message.storedName) {
    return res.status(404).json({ error: "Document introuvable" });
  }

  await sendFile(res, message.storedName, message.fileName);
});

module.exports = router;
