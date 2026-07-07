const express = require("express");
const { z } = require("zod");
const { PrismaClient } = require("@prisma/client");
const { requireAuth, requireRole } = require("../middleware/auth");

const router = express.Router();
const prisma = new PrismaClient();

// Liste des tuteurs disponibles, pour choisir avec qui réserver un créneau.
router.get("/", requireAuth, async (_req, res) => {
  const tutors = await prisma.tutorProfile.findMany({
    include: { user: { select: { fullName: true, filiere: true } } },
    orderBy: { user: { fullName: "asc" } },
  });

  res.json(
    tutors.map((t) => ({
      id: t.id,
      fullName: t.user.fullName,
      filiere: t.user.filiere,
      bio: t.bio,
      specialites: t.specialites,
      tarifSession: t.tarifSession,
    }))
  );
});

const updateProfileSchema = z.object({
  bio: z.string().max(2000).optional(),
  specialites: z.array(z.string().min(1).max(100)).max(20).optional(),
  // Tarif indicatif à l'acte : de 3 $ (TP) à 200 $ (accompagnement mémoire/PFE)
  tarifSession: z.number().min(3).max(200).nullable().optional(),
});

// Le tuteur connecté met à jour son profil public.
router.put("/me", requireAuth, requireRole("TUTOR"), async (req, res) => {
  const parsed = updateProfileSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.flatten() });
  }

  const profile = await prisma.tutorProfile.findUnique({
    where: { userId: req.user.userId },
  });
  if (!profile) {
    return res.status(404).json({ error: "Profil tuteur introuvable" });
  }

  const updated = await prisma.tutorProfile.update({
    where: { id: profile.id },
    data: parsed.data,
  });
  res.json(updated);
});

module.exports = router;
