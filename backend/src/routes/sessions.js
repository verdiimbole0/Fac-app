const express = require("express");
const { z } = require("zod");
const { PrismaClient } = require("@prisma/client");
const { requireAuth, requireRole } = require("../middleware/auth");
const { SESSION_TYPE_PRICING } = require("../pricing");

const router = express.Router();
const prisma = new PrismaClient();

// Durée d'un créneau : deux sessions d'un même tuteur ne peuvent pas
// démarrer à moins d'une heure d'écart.
const SLOT_DURATION_MS = 60 * 60 * 1000;

const createSchema = z.object({
  tutorId: z.string().uuid(),
  type: z.enum(["TP", "PREPARATION_EXAM", "MEMOIRE_PFE"]),
  scheduledAt: z.string().datetime({ offset: true }),
  priceUsd: z.number().positive(),
});

// Un étudiant demande un créneau auprès d'un tuteur → session REQUESTED,
// à confirmer ensuite par le tuteur.
router.post("/", requireAuth, requireRole("STUDENT"), async (req, res) => {
  const parsed = createSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.flatten() });
  }
  const { tutorId, type, scheduledAt, priceUsd } = parsed.data;

  const start = new Date(scheduledAt);
  if (start.getTime() <= Date.now()) {
    return res.status(400).json({ error: "Le créneau doit être dans le futur" });
  }

  const bounds = SESSION_TYPE_PRICING[type];
  if (priceUsd < bounds.min || priceUsd > bounds.max) {
    return res.status(400).json({
      error: `Le tarif pour ce type de session doit être entre ${bounds.min} $ et ${bounds.max} $`,
    });
  }

  const tutor = await prisma.tutorProfile.findUnique({ where: { id: tutorId } });
  if (!tutor) {
    return res.status(404).json({ error: "Tuteur introuvable" });
  }
  if (tutor.userId === req.user.userId) {
    return res.status(400).json({ error: "Impossible de réserver un créneau avec soi-même" });
  }

  const conflict = await prisma.session.findFirst({
    where: {
      tutorId,
      status: { in: ["REQUESTED", "CONFIRMED"] },
      scheduledAt: {
        gt: new Date(start.getTime() - SLOT_DURATION_MS),
        lt: new Date(start.getTime() + SLOT_DURATION_MS),
      },
    },
  });
  if (conflict) {
    return res.status(409).json({ error: "Ce créneau n'est plus disponible pour ce tuteur" });
  }

  const session = await prisma.session.create({
    data: {
      studentId: req.user.userId,
      tutorId,
      type,
      scheduledAt: start,
      priceUsd,
      status: "REQUESTED",
    },
    include: {
      tutor: { include: { user: { select: { fullName: true } } } },
    },
  });

  res.status(201).json(session);
});

// Liste les sessions de l'utilisateur connecté (étudiant ou tuteur).
router.get("/", requireAuth, async (req, res) => {
  let where;
  if (req.user.role === "TUTOR") {
    const tutorProfile = await prisma.tutorProfile.findUnique({
      where: { userId: req.user.userId },
    });
    if (!tutorProfile) {
      return res.status(404).json({ error: "Profil tuteur introuvable" });
    }
    where = { tutorId: tutorProfile.id };
  } else if (req.user.role === "ADMIN") {
    where = {};
  } else {
    where = { studentId: req.user.userId };
  }

  const sessions = await prisma.session.findMany({
    where,
    orderBy: { scheduledAt: "asc" },
    include: {
      student: { select: { id: true, fullName: true, filiere: true } },
      tutor: { include: { user: { select: { id: true, fullName: true } } } },
    },
  });

  res.json(sessions);
});

// Charge une session et vérifie que l'utilisateur connecté y participe.
async function loadSessionForUser(req, res) {
  const session = await prisma.session.findUnique({
    where: { id: req.params.id },
    include: { tutor: true },
  });
  if (!session) {
    res.status(404).json({ error: "Session introuvable" });
    return null;
  }
  const isStudent = session.studentId === req.user.userId;
  const isTutor = session.tutor.userId === req.user.userId;
  if (!isStudent && !isTutor && req.user.role !== "ADMIN") {
    res.status(403).json({ error: "Accès refusé" });
    return null;
  }
  return { session, isStudent, isTutor };
}

// Le tuteur confirme une demande de créneau.
router.patch("/:id/confirm", requireAuth, requireRole("TUTOR", "ADMIN"), async (req, res) => {
  const loaded = await loadSessionForUser(req, res);
  if (!loaded) return;
  const { session, isTutor } = loaded;

  if (!isTutor && req.user.role !== "ADMIN") {
    return res.status(403).json({ error: "Seul le tuteur concerné peut confirmer" });
  }
  if (session.status !== "REQUESTED") {
    return res.status(409).json({ error: `Session déjà ${session.status.toLowerCase()}` });
  }

  const updated = await prisma.session.update({
    where: { id: session.id },
    data: { status: "CONFIRMED" },
  });
  res.json(updated);
});

// L'étudiant ou le tuteur annule une session non terminée.
router.patch("/:id/cancel", requireAuth, async (req, res) => {
  const loaded = await loadSessionForUser(req, res);
  if (!loaded) return;
  const { session } = loaded;

  if (session.status === "COMPLETED" || session.status === "CANCELLED") {
    return res.status(409).json({ error: `Session déjà ${session.status.toLowerCase()}` });
  }

  const updated = await prisma.session.update({
    where: { id: session.id },
    data: { status: "CANCELLED" },
  });
  res.json(updated);
});

// Le tuteur marque une session confirmée comme effectuée.
router.patch("/:id/complete", requireAuth, requireRole("TUTOR", "ADMIN"), async (req, res) => {
  const loaded = await loadSessionForUser(req, res);
  if (!loaded) return;
  const { session, isTutor } = loaded;

  if (!isTutor && req.user.role !== "ADMIN") {
    return res.status(403).json({ error: "Seul le tuteur concerné peut clôturer" });
  }
  if (session.status !== "CONFIRMED") {
    return res.status(409).json({ error: "Seule une session confirmée peut être clôturée" });
  }

  const updated = await prisma.session.update({
    where: { id: session.id },
    data: { status: "COMPLETED" },
  });
  res.json(updated);
});

module.exports = router;
