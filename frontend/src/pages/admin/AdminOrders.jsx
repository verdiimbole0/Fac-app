import React from "react";
import { useAuth } from "@/context/AuthContext";
import { useStore } from "@/context/StoreContext";
import { formatPrice } from "@/lib/api";
import { toast } from "sonner";
import { Copy, Mail } from "lucide-react";

const STATUS_LABELS = {
  fr: {
    pending: "En attente",
    paid: "Payée",
    shipped: "Expédiée",
    delivered: "Livrée",
    cancelled: "Annulée",
    failed: "Échouée",
  },
  en: {
    pending: "Pending",
    paid: "Paid",
    shipped: "Shipped",
    delivered: "Delivered",
    cancelled: "Cancelled",
    failed: "Failed",
  },
};

const STATUS_COLORS = {
  pending: "bg-[#f0ece3] text-[#a88b5f]",
  paid: "bg-[#2E4D43] text-[#fafaf7]",
  shipped: "bg-[#1F2A44] text-[#fafaf7]",
  delivered: "bg-[#1a1a1a] text-[#fafaf7]",
  cancelled: "bg-[#e5e2dc] text-[#737373]",
  failed: "bg-[#8c3a3a] text-[#fafaf7]",
};

export default function AdminOrders() {
  const { authAxios } = useAuth();
  const { lang } = useStore();
  const [orders, setOrders] = React.useState([]);
  const [loading, setLoading] = React.useState(true);
  const [selected, setSelected] = React.useState(null);

  const load = async () => {
    setLoading(true);
    const r = await authAxios.get("/admin/orders");
    setOrders(r.data);
    setLoading(false);
  };

  React.useEffect(() => {
    load();
  }, []);

  const updateStatus = async (id, status) => {
    try {
      await authAxios.patch(`/admin/orders/${id}/status`, { status });
      toast.success(lang === "en" ? "Updated" : "Mis à jour");
      load();
      if (selected?.id === id) setSelected((s) => ({ ...s, status }));
    } catch (e) {
      toast.error(e?.response?.data?.detail || "Error");
    }
  };

  const copyEmailTemplate = (o) => {
    const text = `${lang === "en" ? "Hello" : "Bonjour"} ${o.contact.first_name},

${lang === "en" ? "Thank you for your order at Billy's Store." : "Merci pour votre commande chez Billy's Store."}

${lang === "en" ? "Order" : "Commande"}: ${o.order_number}
Total: ${formatPrice(o.total, lang)}

${lang === "en" ? "Items" : "Articles"}:
${o.items.map((i) => `- ${i.name} × ${i.quantity} — ${formatPrice(i.price * i.quantity, lang)}`).join("\n")}

${lang === "en" ? "Shipping to" : "Livraison à"}: ${o.shipping.address}, ${o.shipping.city} ${o.shipping.postal_code} ${o.shipping.country}

${lang === "en" ? "We'll notify you when it ships." : "Nous vous préviendrons dès l'expédition."}

Billy's Store`;
    navigator.clipboard.writeText(text);
    toast.success(lang === "en" ? "Email copied" : "Email copié");
  };

  return (
    <div data-testid="admin-orders-page" className="space-y-8">
      <h1 className="font-serif text-4xl tracking-tight">
        {lang === "en" ? "Orders" : "Commandes"}
      </h1>

      {loading ? (
        <div className="text-[#737373]">…</div>
      ) : orders.length === 0 ? (
        <div className="border border-[#e5e2dc] p-12 text-center text-[#737373]">
          {lang === "en" ? "No orders yet" : "Aucune commande"}
        </div>
      ) : (
        <div className="border border-[#e5e2dc] bg-white overflow-x-auto">
          <table className="w-full text-sm">
            <thead className="border-b border-[#e5e2dc]">
              <tr className="text-left">
                {["Order", "Date", "Customer", "Total", "Payment", "Status", ""].map((h) => (
                  <th key={h} className="p-4 label-caps text-xs text-[#737373]">
                    {h}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {orders.map((o) => (
                <tr key={o.id} className="border-b border-[#e5e2dc]/60 hover:bg-[#f0ece3]/40">
                  <td className="p-4 font-serif">{o.order_number}</td>
                  <td className="p-4 text-[#737373] text-xs">
                    {new Date(o.created_at).toLocaleDateString(lang === "en" ? "en-US" : "fr-FR")}
                  </td>
                  <td className="p-4">
                    <div>{o.contact?.first_name} {o.contact?.last_name}</div>
                    <div className="text-xs text-[#737373]">{o.contact?.email}</div>
                  </td>
                  <td className="p-4">{formatPrice(o.total, lang)}</td>
                  <td className="p-4 label-caps text-xs">{o.payment_method}</td>
                  <td className="p-4">
                    <select
                      value={o.status}
                      onChange={(e) => updateStatus(o.id, e.target.value)}
                      className={`label-caps text-[10px] px-3 py-1.5 ${STATUS_COLORS[o.status] || "bg-[#f0ece3]"}`}
                    >
                      {Object.keys(STATUS_LABELS[lang]).map((s) => (
                        <option key={s} value={s}>
                          {STATUS_LABELS[lang][s]}
                        </option>
                      ))}
                    </select>
                  </td>
                  <td className="p-4">
                    <div className="flex gap-1 justify-end">
                      <button
                        onClick={() => setSelected(o)}
                        className="label-caps text-xs underline text-[#a88b5f]"
                      >
                        {lang === "en" ? "View" : "Voir"}
                      </button>
                      <button
                        onClick={() => copyEmailTemplate(o)}
                        title={lang === "en" ? "Copy email template" : "Copier le template email"}
                        className="w-8 h-8 border border-[#e5e2dc] flex items-center justify-center hover:border-[#1a1a1a] ml-2"
                      >
                        <Mail size={13} strokeWidth={1.5} />
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {selected && (
        <div
          className="fixed inset-0 bg-[#1a1a1a]/60 z-50 flex items-center justify-center p-4"
          onClick={() => setSelected(null)}
        >
          <div
            className="bg-[#fafaf7] max-w-2xl w-full max-h-[90vh] overflow-y-auto p-8"
            onClick={(e) => e.stopPropagation()}
            data-testid="order-detail-modal"
          >
            <div className="flex justify-between items-start mb-6">
              <div>
                <div className="label-caps text-[#a88b5f] text-xs mb-1">
                  {STATUS_LABELS[lang][selected.status] || selected.status}
                </div>
                <div className="font-serif text-3xl">{selected.order_number}</div>
              </div>
              <button onClick={() => setSelected(null)} className="text-[#737373]">
                ✕
              </button>
            </div>

            <div className="grid md:grid-cols-2 gap-6 mb-6 text-sm">
              <div>
                <div className="label-caps text-xs mb-2">{lang === "en" ? "Contact" : "Contact"}</div>
                <div>{selected.contact.first_name} {selected.contact.last_name}</div>
                <div className="text-[#737373]">{selected.contact.email}</div>
                <div className="text-[#737373]">{selected.contact.phone}</div>
              </div>
              <div>
                <div className="label-caps text-xs mb-2">{lang === "en" ? "Shipping" : "Livraison"}</div>
                <div>{selected.shipping.address}</div>
                <div>{selected.shipping.city}, {selected.shipping.postal_code}</div>
                <div>{selected.shipping.country}</div>
              </div>
              <div>
                <div className="label-caps text-xs mb-2">{lang === "en" ? "Payment" : "Paiement"}</div>
                <div>{selected.payment_method}</div>
                <div className="text-[#737373]">{selected.payment_phone}</div>
              </div>
              {selected.promo_code && (
                <div>
                  <div className="label-caps text-xs mb-2">{lang === "en" ? "Promo" : "Code promo"}</div>
                  <div>{selected.promo_code} (-{formatPrice(selected.discount, lang)})</div>
                </div>
              )}
            </div>

            <div className="border-t border-[#e5e2dc] pt-4">
              <div className="label-caps text-xs mb-3">{lang === "en" ? "Items" : "Articles"}</div>
              <ul className="divide-y divide-[#e5e2dc]">
                {selected.items.map((i, idx) => (
                  <li key={idx} className="py-3 flex justify-between text-sm">
                    <span>
                      {i.name} × {i.quantity}
                      <span className="text-[#737373] text-xs ml-2">
                        {[i.size, i.color].filter(Boolean).join(" · ")}
                      </span>
                    </span>
                    <span>{formatPrice(i.price * i.quantity, lang)}</span>
                  </li>
                ))}
              </ul>
              <div className="flex justify-between pt-4 font-serif text-lg">
                <span>Total</span>
                <span>{formatPrice(selected.total, lang)}</span>
              </div>
            </div>

            <button
              onClick={() => copyEmailTemplate(selected)}
              className="mt-6 w-full bg-[#1a1a1a] text-[#fafaf7] py-3 label-caps flex items-center justify-center gap-2 hover:bg-[#333]"
            >
              <Copy size={14} strokeWidth={1.5} />
              {lang === "en" ? "Copy email template" : "Copier l'email de confirmation"}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
