const express = require("express");
const { PrismaClient } = require("@prisma/client");
const { requireAuth } = require("../middleware/auth");
const { PLAN_PRICING } = require("../pricing");

const router = express.Router();
const prisma = new PrismaClient();

// Plans disponibles et leur tarif mensuel.
router.get("/plans", (_req, res) => res.json(PLAN_PRICING));

// Abonnement en cours de l'utilisateur connecté (null si aucun actif).
router.get("/me", requireAuth, async (req, res) => {
  const subscription = await prisma.subscription.findFirst({
    where: { userId: req.user.userId, active: true, expiresAt: { gt: new Date() } },
    orderBy: { expiresAt: "desc" },
  });
  res.json(subscription);
});

module.exports = router;
