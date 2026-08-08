import React from "react";
import { NavLink, Outlet, useNavigate } from "react-router-dom";
import { LayoutDashboard, Package, ShoppingBag, Tag, LogOut, Store } from "lucide-react";
import { useAuth } from "@/context/AuthContext";
import { useStore } from "@/context/StoreContext";

export default function AdminLayout() {
  const { admin, loading, logout } = useAuth();
  const { lang, setLang } = useStore();
  const navigate = useNavigate();

  React.useEffect(() => {
    if (!loading && !admin) navigate("/admin/login", { replace: true });
  }, [admin, loading, navigate]);

  if (loading || !admin) {
    return (
      <div className="min-h-[60vh] flex items-center justify-center text-[#737373]">
        …
      </div>
    );
  }

  const items = [
    { to: "/admin", end: true, icon: LayoutDashboard, key: "dashboard", label_fr: "Tableau de bord", label_en: "Dashboard" },
    { to: "/admin/products", icon: Package, key: "products", label_fr: "Produits", label_en: "Products" },
    { to: "/admin/orders", icon: ShoppingBag, key: "orders", label_fr: "Commandes", label_en: "Orders" },
    { to: "/admin/promos", icon: Tag, key: "promos", label_fr: "Codes promo", label_en: "Promo codes" },
  ];

  return (
    <div className="min-h-screen grid grid-cols-1 lg:grid-cols-[260px_1fr] bg-[#fafaf7]">
      <aside className="border-r border-[#e5e2dc] bg-white lg:min-h-screen" data-testid="admin-sidebar">
        <div className="p-6 border-b border-[#e5e2dc]">
          <div className="font-serif text-2xl">
            Billy's<span className="text-[#c5a880]">.</span>
          </div>
          <div className="label-caps text-[10px] text-[#a88b5f] mt-1">
            Back-office
          </div>
        </div>
        <nav className="p-3 space-y-1">
          {items.map((it) => (
            <NavLink
              key={it.to}
              to={it.to}
              end={it.end}
              data-testid={`admin-nav-${it.key}`}
              className={({ isActive }) =>
                `flex items-center gap-3 px-3 py-2.5 label-caps ${isActive ? "bg-[#1a1a1a] text-[#fafaf7]" : "text-[#1a1a1a] hover:bg-[#f0ece3]"}`
              }
            >
              <it.icon size={16} strokeWidth={1.5} />
              {lang === "en" ? it.label_en : it.label_fr}
            </NavLink>
          ))}
        </nav>
        <div className="p-3 border-t border-[#e5e2dc] mt-auto">
          <NavLink
            to="/"
            className="flex items-center gap-3 px-3 py-2.5 label-caps text-[#737373] hover:text-[#1a1a1a]"
          >
            <Store size={16} strokeWidth={1.5} />
            {lang === "en" ? "View store" : "Voir la boutique"}
          </NavLink>
          <button
            data-testid="admin-logout"
            onClick={async () => {
              await logout();
              navigate("/admin/login");
            }}
            className="w-full flex items-center gap-3 px-3 py-2.5 label-caps text-[#8c3a3a] hover:bg-[#f0ece3]"
          >
            <LogOut size={16} strokeWidth={1.5} />
            {lang === "en" ? "Sign out" : "Déconnexion"}
          </button>
        </div>
      </aside>

      <main className="p-6 md:p-10 lg:p-12 overflow-x-hidden">
        <div className="flex items-center justify-between mb-8">
          <div>
            <div className="label-caps text-[#a88b5f] text-xs">
              {lang === "en" ? "Signed in as" : "Connecté en tant que"}
            </div>
            <div className="font-serif text-lg">{admin.email}</div>
          </div>
          <div className="flex items-center gap-2 border border-[#e5e2dc]">
            <button
              onClick={() => setLang("fr")}
              className={`label-caps px-2.5 py-1.5 ${lang === "fr" ? "bg-[#1a1a1a] text-[#fafaf7]" : ""}`}
            >
              FR
            </button>
            <button
              onClick={() => setLang("en")}
              className={`label-caps px-2.5 py-1.5 ${lang === "en" ? "bg-[#1a1a1a] text-[#fafaf7]" : ""}`}
            >
              EN
            </button>
          </div>
        </div>
        <Outlet />
      </main>
    </div>
  );
}
