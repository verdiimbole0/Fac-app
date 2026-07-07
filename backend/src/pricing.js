// Grille tarifaire de référence (en $) — à ajuster si besoin
const PRICING = {
  SESSION_TP: { min: 3, max: 30 },
  SESSION_EXAM_PREP: { min: 3, max: 30 },
  SUBSCRIPTION_MONTHLY: { min: 30, max: 50 },
  MEMOIRE_PFE: { min: 50, max: 200 },
};

// Bornes de prix applicables selon le type de session réservé
const SESSION_TYPE_PRICING = {
  TP: PRICING.SESSION_TP,
  PREPARATION_EXAM: PRICING.SESSION_EXAM_PREP,
  MEMOIRE_PFE: PRICING.MEMOIRE_PFE,
};

// Tarif mensuel de chaque plan d'abonnement (dans la fourchette 30-50 $)
const PLAN_PRICING = {
  DECOUVERTE: 30,
  STANDARD: 40,
  INTENSIF: 50,
};

module.exports = { PRICING, SESSION_TYPE_PRICING, PLAN_PRICING };
