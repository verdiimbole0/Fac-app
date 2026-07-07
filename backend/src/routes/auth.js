const express = require("express");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const { z } = require("zod");
const { PrismaClient } = require("@prisma/client");
const { requireAuth } = require("../middleware/auth");

const router = express.Router();
const prisma = new PrismaClient();

// Profil complet de l'utilisateur connecté (avec profil tuteur et abonnement actif).
router.get("/me", requireAuth, async (req, res) => {
  const user = await prisma.user.findUnique({
    where: { id: req.user.userId },
    select: {
      id: true,
      email: true,
      fullName: true,
      role: true,
      filiere: true,
      createdAt: true,
      tutorProfile: true,
    },
  });
  if (!user) {
    return res.status(404).json({ error: "Utilisateur introuvable" });
  }

  const subscription = await prisma.subscription.findFirst({
    where: { userId: user.id, active: true, expiresAt: { gt: new Date() } },
    orderBy: { expiresAt: "desc" },
  });

  res.json({ ...user, subscription });
});

const registerSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
  fullName: z.string().min(2),
  role: z.enum(["STUDENT", "TUTOR"]).default("STUDENT"),
  filiere: z.string().optional(),
  acceptedIntegrityCharter: z
    .boolean()
    .refine((v) => v === true, {
      message: "La charte d'intégrité académique doit être acceptée pour s'inscrire",
    }),
});

router.post("/register", async (req, res) => {
  const parsed = registerSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.flatten() });
  }
  const { email, password, fullName, role, filiere, acceptedIntegrityCharter } = parsed.data;

  const existing = await prisma.user.findUnique({ where: { email } });
  if (existing) {
    return res.status(409).json({ error: "Un compte existe déjà avec cet email" });
  }

  const passwordHash = await bcrypt.hash(password, 10);
  const user = await prisma.user.create({
    data: { email, passwordHash, fullName, role, filiere, acceptedIntegrityCharter },
  });

  if (role === "TUTOR") {
    await prisma.tutorProfile.create({ data: { userId: user.id } });
  }

  const token = jwt.sign({ userId: user.id, role: user.role }, process.env.JWT_SECRET, {
    expiresIn: "7d",
  });

  res.status(201).json({ token, user: { id: user.id, email: user.email, role: user.role } });
});

const loginSchema = z.object({
  email: z.string().email(),
  password: z.string(),
});

router.post("/login", async (req, res) => {
  const parsed = loginSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.flatten() });
  }
  const { email, password } = parsed.data;

  const user = await prisma.user.findUnique({ where: { email } });
  if (!user) {
    return res.status(401).json({ error: "Identifiants invalides" });
  }

  const valid = await bcrypt.compare(password, user.passwordHash);
  if (!valid) {
    return res.status(401).json({ error: "Identifiants invalides" });
  }

  const token = jwt.sign({ userId: user.id, role: user.role }, process.env.JWT_SECRET, {
    expiresIn: "7d",
  });

  res.json({ token, user: { id: user.id, email: user.email, role: user.role } });
});

module.exports = router;
