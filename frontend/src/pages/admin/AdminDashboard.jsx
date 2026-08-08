import React from "react";
import { useAuth } from "@/context/AuthContext";
import { useStore } from "@/context/StoreContext";
import { fetchProducts } from "@/lib/api";
import { formatPrice } from "@/lib/api";
import { Link } from "react-router-dom";

export default function AdminDashboard() {
  const { authAxios } = useAuth();
  const { lang } = useStore();
  const [stats, setStats] = React.useState({ orders: 0, revenue: 0, pending: 0, products: 0 });
  const [recent, setRecent] = React.useState([]);

  React.useEffect(() => {
    (async () => {
      try {
        const productsP = fetchProducts({ limit: 200 });
        // Orders fetch may 403 for products_editor — swallow silently
        const ordersP = authAxios
          .get("/admin/orders")
          .then((r) => r.data)
          .catch(() => []);
        const [orders, products] = await Promise.all([ordersP, productsP]);
        const revenue = orders
          .filter((o) => ["paid", "shipped", "delivered"].includes(o.status))
          .reduce((s, o) => s + (o.total || 0), 0);
        setStats({
          orders: orders.length,
          revenue,
          pending: orders.filter((o) => o.status === "pending").length,
          products: products.length,
        });
        setRecent(orders.slice(0, 5));
      } catch (e) {
        console.error(e);
      }
    })();
  }, [authAxios]);

  const cards = [
    {
      label: lang === "en" ? "Total orders" : "Commandes totales",
      value: stats.orders,
    },
    {
      label: lang === "en" ? "Revenue" : "Chiffre d'affaires",
      value: formatPrice(stats.revenue, lang),
    },
    {
      label: lang === "en" ? "Pending" : "En attente",
      value: stats.pending,
    },
    {
      label: lang === "en" ? "Products" : "Produits",
      value: stats.products,
    },
  ];

  return (
    <div data-testid="admin-dashboard" className="space-y-10">
      <h1 className="font-serif text-4xl tracking-tight">
        {lang === "en" ? "Overview" : "Vue d'ensemble"}
      </h1>
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {cards.map((c) => (
          <div
            key={c.label}
            className="border border-[#e5e2dc] bg-white p-6"
          >
            <div className="label-caps text-[#737373] text-xs mb-3">{c.label}</div>
            <div className="font-serif text-3xl">{c.value}</div>
          </div>
        ))}
      </div>

      <div>
        <div className="flex justify-between items-end mb-4">
          <h2 className="font-serif text-2xl">
            {lang === "en" ? "Recent orders" : "Dernières commandes"}
          </h2>
          <Link to="/admin/orders" className="label-caps text-[#a88b5f]">
            {lang === "en" ? "See all →" : "Tout voir →"}
          </Link>
        </div>
        {recent.length === 0 ? (
          <div className="border border-[#e5e2dc] p-8 text-center text-[#737373]">
            {lang === "en" ? "No orders yet" : "Aucune commande pour l'instant"}
          </div>
        ) : (
          <div className="border border-[#e5e2dc] bg-white overflow-x-auto">
            <table className="w-full text-sm">
              <thead className="border-b border-[#e5e2dc]">
                <tr className="text-left">
                  {[
                    lang === "en" ? "Order" : "Commande",
                    lang === "en" ? "Customer" : "Client",
                    "Total",
                    "Status",
                  ].map((h) => (
                    <th key={h} className="p-4 label-caps text-xs text-[#737373]">
                      {h}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {recent.map((o) => (
                  <tr key={o.id} className="border-b border-[#e5e2dc]/60">
                    <td className="p-4 font-serif">{o.order_number}</td>
                    <td className="p-4">{o.contact?.email}</td>
                    <td className="p-4">{formatPrice(o.total, lang)}</td>
                    <td className="p-4">
                      <span className="label-caps text-[10px] bg-[#f0ece3] px-2 py-1">
                        {o.status}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
