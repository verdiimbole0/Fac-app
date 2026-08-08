import React from "react";
import { Link } from "react-router-dom";
import { Plus, Edit3, Trash2 } from "lucide-react";
import { fetchProducts, formatPrice } from "@/lib/api";
import { useAuth } from "@/context/AuthContext";
import { useStore } from "@/context/StoreContext";
import { localizedName } from "@/lib/i18n";
import { toast } from "sonner";

export default function AdminProducts() {
  const { authAxios } = useAuth();
  const { lang } = useStore();
  const [products, setProducts] = React.useState([]);
  const [loading, setLoading] = React.useState(true);
  const [search, setSearch] = React.useState("");

  const load = async () => {
    setLoading(true);
    const data = await fetchProducts({ limit: 300 });
    setProducts(data);
    setLoading(false);
  };

  React.useEffect(() => {
    load();
  }, []);

  const del = async (slug) => {
    if (!window.confirm(lang === "en" ? "Delete this product?" : "Supprimer ce produit ?")) return;
    try {
      await authAxios.delete(`/admin/products/${slug}`);
      toast.success(lang === "en" ? "Deleted" : "Supprimé");
      load();
    } catch (e) {
      toast.error(e?.response?.data?.detail || "Error");
    }
  };

  const filtered = products.filter((p) =>
    !search
      ? true
      : (p.name_fr + p.name_en + p.slug).toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div data-testid="admin-products-page" className="space-y-8">
      <div className="flex justify-between items-center flex-wrap gap-4">
        <h1 className="font-serif text-4xl tracking-tight">
          {lang === "en" ? "Products" : "Produits"}
        </h1>
        <Link
          to="/admin/products/new"
          data-testid="admin-new-product"
          className="bg-[#1a1a1a] text-[#fafaf7] px-6 py-3 label-caps flex items-center gap-2 hover:bg-[#333] bs-btn"
        >
          <Plus size={14} strokeWidth={1.5} />
          {lang === "en" ? "New product" : "Nouveau produit"}
        </Link>
      </div>

      <input
        placeholder={lang === "en" ? "Search…" : "Rechercher…"}
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="w-full max-w-md border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-3 text-sm outline-none"
      />

      {loading ? (
        <div className="text-[#737373]">…</div>
      ) : (
        <div className="border border-[#e5e2dc] bg-white overflow-x-auto">
          <table className="w-full text-sm">
            <thead className="border-b border-[#e5e2dc]">
              <tr className="text-left">
                {["", "Product", "Category", "Price", "Stock", "Badges", ""].map((h, i) => (
                  <th key={i} className="p-4 label-caps text-xs text-[#737373]">
                    {h}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {filtered.map((p) => (
                <tr
                  key={p.id}
                  data-testid={`admin-product-row-${p.slug}`}
                  className="border-b border-[#e5e2dc]/60"
                >
                  <td className="p-4">
                    <img
                      src={p.images[0]}
                      alt=""
                      className="w-14 h-16 object-cover bg-[#f0ece3]"
                    />
                  </td>
                  <td className="p-4">
                    <div className="font-serif">{localizedName(p, lang)}</div>
                    <div className="text-xs text-[#737373]">/{p.slug}</div>
                  </td>
                  <td className="p-4 label-caps text-xs">{p.category}</td>
                  <td className="p-4">{formatPrice(p.price, lang)}</td>
                  <td className="p-4">
                    <span
                      className={
                        p.stock === 0 ? "text-[#8c3a3a]" : ""
                      }
                    >
                      {p.stock}
                    </span>
                  </td>
                  <td className="p-4">
                    <div className="flex gap-1">
                      {p.badges?.map((b) => (
                        <span
                          key={b}
                          className="label-caps text-[9px] bg-[#f0ece3] px-2 py-1"
                        >
                          {b}
                        </span>
                      ))}
                    </div>
                  </td>
                  <td className="p-4">
                    <div className="flex gap-2 justify-end">
                      <Link
                        to={`/admin/products/${p.slug}`}
                        data-testid={`admin-edit-${p.slug}`}
                        className="w-9 h-9 border border-[#e5e2dc] flex items-center justify-center hover:border-[#1a1a1a] bs-btn"
                      >
                        <Edit3 size={14} strokeWidth={1.5} />
                      </Link>
                      <button
                        data-testid={`admin-delete-${p.slug}`}
                        onClick={() => del(p.slug)}
                        className="w-9 h-9 border border-[#e5e2dc] text-[#8c3a3a] flex items-center justify-center hover:border-[#8c3a3a] bs-btn"
                      >
                        <Trash2 size={14} strokeWidth={1.5} />
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
