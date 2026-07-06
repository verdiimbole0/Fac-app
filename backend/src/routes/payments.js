const express = require("express");
const { z } = require("zod");
const { PrismaClient } = require("@prisma/client");
const { requireAuth } = require("../middleware/auth");
const { PRICING } = require("../pricing");

const router = express.Router();
const prisma = new PrismaClient();

const initiateSchema = z
  .object({
    provider: z.enum(["ORANGE_MONEY", "AIRTEL_MONEY", "MPESA", "FONDEKA"]),
    purpose: z.enum(["SESSION", "SUBSCRIPTION"]),
    // Pour une SESSION : sessionId obligatoire, le montant est celui du créneau.
    // Pour un SUBSCRIPTION : amountUsd obligatoire.
    sessionId: z.string().uuid().optional(),
    amountUsd: z.number().positive().optional(),
  })
  .refine((d) => d.purpose !== "SESSION" || d.sessionId, {
    message: "sessionId est requis pour payer une session",
  })
  .refine((d) => d.purpose !== "SUBSCRIPTION" || d.amountUsd, {
    message: "amountUsd est requis pour un abonnement",
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
  const { provider, purpose, sessionId } = parsed.data;
  let { amountUsd } = parsed.data;

  if (purpose === "SESSION") {
    const session = await prisma.session.findUnique({
      where: { id: sessionId },
      include: { payments: true },
    });
    if (!session) {
      return res.status(404).json({ error: "Session introuvable" });
    }
    if (session.studentId !== req.user.userId) {
      return res.status(403).json({ error: "Seul l'étudiant concerné peut payer cette session" });
    }
    if (session.status !== "CONFIRMED") {
      return res.status(409).json({ error: "Seule une session confirmée peut être payée" });
    }
    const alreadyPaid = session.payments.some((p) => p.status === "SUCCESS");
    const pending = session.payments.some((p) => p.status === "PENDING");
    if (alreadyPaid) {
      return res.status(409).json({ error: "Cette session est déjà payée" });
    }
    if (pending) {
      return res.status(409).json({ error: "Un paiement est déjà en cours pour cette session" });
    }
    amountUsd = session.priceUsd;
  }

  const reference = `FACAPP-${Date.now()}-${Math.floor(Math.random() * 10000)}`;

  const payment = await prisma.payment.create({
    data: {
      userId: req.user.userId,
      provider,
      amountUsd,
      reference,
      status: "PENDING",
      sessionId: purpose === "SESSION" ? sessionId : null,
    },
  });

  // TODO: appeler ici l'API du provider (Orange Money / Airtel Money / M-Pesa / FONDEKA)
  // pour déclencher le paiement côté opérateur, en utilisant `reference` comme identifiant
  // de corrélation avec le webhook de confirmation ci-dessous.

  res.status(201).json({
    paymentId: payment.id,
    reference,
    status: payment.status,
    amountUsd: payment.amountUsd,
  });
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
