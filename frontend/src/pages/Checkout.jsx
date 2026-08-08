import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { Check, Shield, RotateCcw, Lock, ArrowLeft } from "lucide-react";
import { useStore } from "@/context/StoreContext";
import { createOrder, formatPrice } from "@/lib/api";

const PAY_METHODS = [
  { id: "orange_money", label: "Orange Money", accent: "#FF7900" },
  { id: "mtn_momo", label: "MTN MoMo", accent: "#FFCB05" },
  { id: "wave", label: "Wave", accent: "#1DC2FF" },
  { id: "moov", label: "Moov Money", accent: "#005EB8" },
];

const STEPS = ["step_contact", "step_shipping", "step_payment"];

export default function Checkout() {
  const { cart, totals, t, lang, clearCart } = useStore();
  const navigate = useNavigate();
  const [step, setStep] = React.useState(0);
  const [confirmed, setConfirmed] = React.useState(null);
  const [submitting, setSubmitting] = React.useState(false);

  const [contact, setContact] = React.useState({
    email: "",
    phone: "",
    first_name: "",
    last_name: "",
  });
  const [shipping, setShipping] = React.useState({
    address: "",
    city: "",
    postal_code: "",
    country: lang === "en" ? "Senegal" : "Sénégal",
  });
  const [payment, setPayment] = React.useState({
    method: "orange_money",
    phone: "",
  });

  React.useEffect(() => {
    if (cart.length === 0 && !confirmed) navigate("/");
  }, [cart, confirmed, navigate]);

  const validateStep = () => {
    if (step === 0) {
      return contact.email && contact.phone && contact.first_name && contact.last_name;
    }
    if (step === 1) {
      return shipping.address && shipping.city && shipping.postal_code && shipping.country;
    }
    return payment.method && payment.phone.length >= 8;
  };

  const submit = async () => {
    setSubmitting(true);
    try {
      const order = await createOrder({
        contact,
        shipping,
        payment_method: payment.method,
        payment_phone: payment.phone,
        items: cart.map((i) => ({
          product_id: i.product_id,
          name: i.name,
          price: i.price,
          quantity: i.quantity,
          size: i.size,
          color: i.color,
          image: i.image,
        })),
        subtotal: totals.subtotal,
        shipping_cost: totals.shipping,
        total: totals.total,
      });
      setConfirmed(order);
      clearCart();
    } finally {
      setSubmitting(false);
    }
  };

  if (confirmed) {
    return (
      <main data-testid="order-confirmed" className="max-w-3xl mx-auto px-5 md:px-10 py-24 text-center">
        <div className="w-16 h-16 mx-auto rounded-full border border-[#1a1a1a] flex items-center justify-center mb-8">
          <Check size={28} strokeWidth={1.4} />
        </div>
        <h1 className="font-serif text-4xl md:text-5xl tracking-tight mb-4">
          {t("order_confirmed")}
        </h1>
        <p className="text-[#737373] max-w-md mx-auto mb-6">{t("order_confirmed_body")}</p>
        <div className="inline-block border border-[#e5e2dc] px-6 py-4 mb-10">
          <div className="label-caps text-[#737373] text-xs">{t("order_number")}</div>
          <div className="font-serif text-xl mt-1">{confirmed.order_number}</div>
        </div>
        <div>
          <Link
            to="/"
            data-testid="continue-shopping"
            className="bg-[#1a1a1a] text-[#fafaf7] px-10 py-4 label-caps hover:bg-[#333] bs-btn inline-block"
          >
            {t("continue_shopping")}
          </Link>
        </div>
      </main>
    );
  }

  const StepInputs = () => {
    if (step === 0)
      return (
        <div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <Field label={t("first_name")} value={contact.first_name} onChange={(v) => setContact({ ...contact, first_name: v })} testid="input-first-name" />
            <Field label={t("last_name")} value={contact.last_name} onChange={(v) => setContact({ ...contact, last_name: v })} testid="input-last-name" />
          </div>
          <Field label={t("email")} type="email" value={contact.email} onChange={(v) => setContact({ ...contact, email: v })} testid="input-email" />
          <Field label={t("phone")} value={contact.phone} onChange={(v) => setContact({ ...contact, phone: v })} testid="input-phone" />
        </div>
      );
    if (step === 1)
      return (
        <div className="space-y-4">
          <Field label={t("address")} value={shipping.address} onChange={(v) => setShipping({ ...shipping, address: v })} testid="input-address" />
          <div className="grid grid-cols-2 gap-4">
            <Field label={t("city")} value={shipping.city} onChange={(v) => setShipping({ ...shipping, city: v })} testid="input-city" />
            <Field label={t("postal_code")} value={shipping.postal_code} onChange={(v) => setShipping({ ...shipping, postal_code: v })} testid="input-postal" />
          </div>
          <Field label={t("country")} value={shipping.country} onChange={(v) => setShipping({ ...shipping, country: v })} testid="input-country" />
        </div>
      );
    return (
      <div className="space-y-6">
        <div>
          <div className="label-caps mb-4">{t("payment_method")} — {t("payment_mobile_money")}</div>
          <div className="grid grid-cols-2 gap-3">
            {PAY_METHODS.map((m) => (
              <button
                key={m.id}
                data-testid={`pay-${m.id}`}
                onClick={() => setPayment({ ...payment, method: m.id })}
                className={`p-4 border text-left bs-btn ${payment.method === m.id ? "border-[#1a1a1a] bg-[#1a1a1a] text-[#fafaf7]" : "border-[#e5e2dc] hover:border-[#1a1a1a]"}`}
              >
                <div
                  className="w-3 h-3 rounded-full mb-3"
                  style={{ backgroundColor: m.accent }}
                />
                <div className="font-serif text-lg">{m.label}</div>
              </button>
            ))}
          </div>
        </div>
        <Field label={t("payment_phone")} value={payment.phone} onChange={(v) => setPayment({ ...payment, phone: v })} testid="input-payment-phone" />
        <div className="p-4 border border-[#e5e2dc] bg-[#f0ece3]/40 text-xs text-[#4a4a4a] flex gap-3 items-start">
          <Lock size={14} strokeWidth={1.5} className="mt-0.5 flex-shrink-0" />
          <span>
            {lang === "en"
              ? "You will receive a confirmation prompt on your Mobile Money account to validate the payment."
              : "Vous recevrez une demande de validation sur votre compte Mobile Money pour finaliser le paiement."}
          </span>
        </div>
      </div>
    );
  };

  return (
    <main data-testid="checkout-page" className="max-w-[1400px] mx-auto px-5 md:px-10 py-10 md:py-16 grid grid-cols-12 gap-8 lg:gap-16">
      {/* Left */}
      <div className="col-span-12 lg:col-span-7">
        <button
          onClick={() => (step === 0 ? navigate(-1) : setStep(step - 1))}
          className="label-caps text-[#737373] flex items-center gap-2 mb-8 hover:text-[#1a1a1a]"
        >
          <ArrowLeft size={14} strokeWidth={1.5} /> {t("back")}
        </button>

        {/* Steps */}
        <div className="flex items-center gap-6 mb-10">
          {STEPS.map((s, i) => (
            <div
              key={s}
              className={`flex items-center gap-3 ${i === step ? "text-[#1a1a1a]" : "text-[#737373]"}`}
            >
              <div className={`w-7 h-7 rounded-full border flex items-center justify-center text-xs ${i <= step ? "border-[#1a1a1a] bg-[#1a1a1a] text-[#fafaf7]" : "border-[#e5e2dc]"}`}>
                {i < step ? <Check size={12} strokeWidth={2} /> : i + 1}
              </div>
              <span className="label-caps hidden md:inline">{t(s)}</span>
            </div>
          ))}
        </div>

        <h1 className="font-serif text-3xl md:text-4xl tracking-tight mb-8">
          {t(STEPS[step])}
        </h1>

        <StepInputs />

        <div className="mt-10 flex justify-between items-center">
          <div className="flex items-center gap-6 text-xs text-[#737373]">
            <div className="flex items-center gap-1.5"><Shield size={14} strokeWidth={1.4} /> {t("secure_payment")}</div>
            <div className="flex items-center gap-1.5"><RotateCcw size={14} strokeWidth={1.4} /> {t("return_policy")}</div>
          </div>
          <button
            data-testid={step < 2 ? "continue-btn" : "place-order-btn"}
            disabled={!validateStep() || submitting}
            onClick={() => (step < 2 ? setStep(step + 1) : submit())}
            className="bg-[#1a1a1a] text-[#fafaf7] px-10 py-4 label-caps hover:bg-[#333] disabled:bg-[#e5e2dc] disabled:text-[#737373] bs-btn"
          >
            {submitting ? "…" : step < 2 ? t("continue") : t("place_order")}
          </button>
        </div>
      </div>

      {/* Summary */}
      <aside className="col-span-12 lg:col-span-5">
        <div className="lg:sticky lg:top-28 border border-[#e5e2dc] p-6 md:p-8 bg-[#fafaf7]">
          <div className="font-serif text-2xl mb-6">
            {lang === "en" ? "Order summary" : "Récapitulatif"}
          </div>
          <ul className="divide-y divide-[#e5e2dc] max-h-[320px] overflow-y-auto -mx-2 px-2">
            {cart.map((item) => (
              <li key={item.line_id} className="py-4 flex gap-4">
                <div className="w-16 h-20 bg-[#f0ece3] flex-shrink-0 overflow-hidden relative">
                  <img src={item.image} alt="" className="w-full h-full object-cover" />
                  <span className="absolute -top-2 -right-2 w-5 h-5 bg-[#1a1a1a] text-[#fafaf7] text-[10px] rounded-full flex items-center justify-center">
                    {item.quantity}
                  </span>
                </div>
                <div className="flex-1 min-w-0">
                  <div className="font-serif text-sm truncate">{item.name}</div>
                  <div className="text-xs text-[#737373] mt-1">
                    {[item.size, item.color].filter(Boolean).join(" · ")}
                  </div>
                </div>
                <div className="text-sm">{formatPrice(item.price * item.quantity, lang)}</div>
              </li>
            ))}
          </ul>
          <div className="border-t border-[#e5e2dc] mt-4 pt-4 space-y-2 text-sm">
            <div className="flex justify-between">
              <span className="text-[#737373]">{t("subtotal")}</span>
              <span>{formatPrice(totals.subtotal, lang)}</span>
            </div>
            <div className="flex justify-between">
              <span className="text-[#737373]">{t("shipping")}</span>
              <span>{totals.shipping === 0 ? t("free") : formatPrice(totals.shipping, lang)}</span>
            </div>
            <div className="flex justify-between font-serif text-lg pt-3 border-t border-[#e5e2dc]">
              <span>Total</span>
              <span>{formatPrice(totals.total, lang)}</span>
            </div>
          </div>
        </div>
      </aside>
    </main>
  );
}

function Field({ label, value, onChange, type = "text", testid }) {
  return (
    <label className="block">
      <div className="label-caps text-[#737373] mb-2 text-xs">{label}</div>
      <input
        data-testid={testid}
        type={type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-3 text-sm outline-none transition-colors"
      />
    </label>
  );
}
