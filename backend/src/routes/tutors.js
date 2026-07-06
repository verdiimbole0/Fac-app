const express = require("express");
const { PrismaClient } = require("@prisma/client");
const { requireAuth } = require("../middleware/auth");

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

module.exports = router;
