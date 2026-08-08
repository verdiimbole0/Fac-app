import React from "react";
import { Link, useSearchParams } from "react-router-dom";
import { Check, X, Loader } from "lucide-react";
import axios from "axios";
import { API } from "@/lib/api";
import { useStore } from "@/context/StoreContext";

export default function PaymentResult() {
  const [params] = useSearchParams();
  const { t, lang } = useStore();
  const [status, setStatus] = React.useState("loading");
  const [order, setOrder] = React.useState(null);

  React.useEffect(() => {
    const tx_ref = params.get("tx_ref");
    const transaction_id = params.get("transaction_id");
    const flw_status = params.get("status");
    if (!tx_ref || !transaction_id || flw_status === "cancelled") {
      setStatus("failed");
      return;
    }
    (async () => {
      try {
        const r = await axios.get(
          `${API}/payments/verify/${tx_ref}?transaction_id=${transaction_id}`
        );
        setStatus(r.data.status);
        setOrder(r.data.order);
      } catch {
        setStatus("failed");
      }
    })();
  }, [params]);

  if (status === "loading") {
    return (
      <main className="min-h-[60vh] flex flex-col items-center justify-center text-center px-6">
        <Loader size={40} strokeWidth={1} className="animate-spin text-[#a88b5f] mb-6" />
        <p className="font-serif text-2xl">
          {lang === "en" ? "Verifying payment…" : "Vérification du paiement…"}
        </p>
      </main>
    );
  }

  const paid = status === "paid";

  return (
    <main data-testid="payment-result" className="max-w-2xl mx-auto px-6 py-24 text-center">
      <div
        className={`w-16 h-16 mx-auto rounded-full border flex items-center justify-center mb-8 ${paid ? "border-[#2E4D43] text-[#2E4D43]" : "border-[#8c3a3a] text-[#8c3a3a]"}`}
      >
        {paid ? <Check size={28} strokeWidth={1.4} /> : <X size={28} strokeWidth={1.4} />}
      </div>
      <h1 className="font-serif text-4xl md:text-5xl tracking-tight mb-4">
        {paid ? t("order_confirmed") : (lang === "en" ? "Payment failed" : "Paiement échoué")}
      </h1>
      <p className="text-[#737373] mb-8">
        {paid
          ? t("order_confirmed_body")
          : lang === "en"
            ? "The payment could not be completed. No amount was charged."
            : "Le paiement n'a pas pu être finalisé. Aucun montant n'a été prélevé."}
      </p>
      {order && (
        <div className="inline-block border border-[#e5e2dc] px-6 py-4 mb-10">
          <div className="label-caps text-[#737373] text-xs">{t("order_number")}</div>
          <div className="font-serif text-xl mt-1">{order.order_number}</div>
        </div>
      )}
      <div>
        <Link
          to={paid ? "/" : "/checkout"}
          className="bg-[#1a1a1a] text-[#fafaf7] px-10 py-4 label-caps hover:bg-[#333] bs-btn inline-block"
        >
          {paid ? t("continue_shopping") : (lang === "en" ? "Try again" : "Réessayer")}
        </Link>
      </div>
    </main>
  );
}
