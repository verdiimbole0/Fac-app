const express = require("express");
const { z } = require("zod");
const { PrismaClient } = require("@prisma/client");
const { requireAuth } = require("../middleware/auth");

const router = express.Router();
const prisma = new PrismaClient();

// Grille tarifaire de référence (en $) — à ajuster si besoin
const PRICING = {
  SESSION_TP: { min: 3, max: 30 },
  SESSION_EXAM_PREP: { min: 3, max: 30 },
  SUBSCRIPTION_MONTHLY: { min: 30, max: 50 },
  MEMOIRE_PFE: { min: 50, max: 200 },
};

const initiateSchema = z.object({
  provider: z.enum(["ORANGE_MONEY", "AIRTEL_MONEY", "MPESA", "FONDEKA"]),
  amountUsd: z.number().positive(),
  purpose: z.enum(["SESSION", "SUBSCRIPTION"]),
});

// Initie un paiement : crée un enregistrement PENDING puis retourne une référence
// à utiliser pour rediriger l'utilisateur vers le flux de paiement du provider choisi.
// NOTE: l'intégration réelle avec chaque opérateur/FONDEKA (redirection, SDK, ou
// requête USSD push) doit être branchée ici selon leur documentation respective.
router.post("/initiate", requireAuth, async (req, res) => {
  const parsed = initiateSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: parsed.error.flatten() });
  }
  const { provider, amountUsd, purpose } = parsed.data;

  const reference = `FACAPP-${Date.now()}-${Math.floor(Math.random() * 10000)}`;

  const payment = await prisma.payment.create({
    data: {
      userId: req.user.userId,
      provider,
      amountUsd,
      reference,
      status: "PENDING",
    },
  });

  // TODO: appeler ici l'API du provider (Orange Money / Airtel Money / M-Pesa / FONDEKA)
  // pour déclencher le paiement côté opérateur, en utilisant `reference` comme identifiant
  // de corrélation avec le webhook de confirmation ci-dessous.

  res.status(201).json({ paymentId: payment.id, reference, status: payment.status });
});

// Webhook générique de confirmation — chaque provider aura un format de payload différent,
// à adapter une fois leur documentation d'intégration obtenue.
router.post("/webhook/:provider", async (req, res) => {
  const { provider } = req.params;
  const { reference, status } = req.body; // format à adapter selon le provider réel

  const payment = await prisma.payment.findUnique({ where: { reference } });
  if (!payment) {
    return res.status(404).json({ error: "Paiement introuvable pour cette référence" });
  }

  const newStatus = status === "SUCCESS" ? "SUCCESS" : "FAILED";
  await prisma.payment.update({
    where: { reference },
    data: { status: newStatus },
  });

  console.log(`[webhook:${provider}] Paiement ${reference} → ${newStatus}`);
  res.json({ received: true });
});

router.get("/pricing", (_req, res) => res.json(PRICING));

module.exports = router;
