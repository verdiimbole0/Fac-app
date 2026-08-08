import React from "react";
import { Plus, Trash2, Tag } from "lucide-react";
import { useAuth } from "@/context/AuthContext";
import { useStore } from "@/context/StoreContext";
import { toast } from "sonner";

const emptyPromo = {
  code: "",
  kind: "percent",
  value: 10,
  min_subtotal: 0,
  category: "",
  expires_at: "",
  max_uses: "",
  active: true,
};

export default function AdminPromos() {
  const { authAxios } = useAuth();
  const { lang } = useStore();
  const [promos, setPromos] = React.useState([]);
  const [loading, setLoading] = React.useState(true);
  const [form, setForm] = React.useState(emptyPromo);
  const [creating, setCreating] = React.useState(false);

  const load = async () => {
    setLoading(true);
    const r = await authAxios.get("/admin/promos");
    setPromos(r.data);
    setLoading(false);
  };

  React.useEffect(() => {
    load();
  }, []);

  const create = async (e) => {
    e.preventDefault();
    setCreating(true);
    try {
      const payload = {
        ...form,
        code: form.code.toUpperCase(),
        value: Number(form.value),
        min_subtotal: Number(form.min_subtotal) || 0,
        max_uses: form.max_uses ? Number(form.max_uses) : null,
        expires_at: form.expires_at ? new Date(form.expires_at).toISOString() : null,
        category: form.category || null,
      };
      await authAxios.post("/admin/promos", payload);
      toast.success(lang === "en" ? "Created" : "Créé");
      setForm(emptyPromo);
      load();
    } catch (e) {
      toast.error(e?.response?.data?.detail || "Error");
    } finally {
      setCreating(false);
    }
  };

  const del = async (code) => {
    if (!window.confirm(lang === "en" ? "Delete this code?" : "Supprimer ce code ?")) return;
    await authAxios.delete(`/admin/promos/${code}`);
    toast.success(lang === "en" ? "Deleted" : "Supprimé");
    load();
  };

  return (
    <div data-testid="admin-promos-page" className="space-y-10">
      <h1 className="font-serif text-4xl tracking-tight">
        {lang === "en" ? "Promo codes" : "Codes promo"}
      </h1>

      {/* Create form */}
      <form
        onSubmit={create}
        data-testid="promo-create-form"
        className="border border-[#e5e2dc] bg-white p-6 md:p-8 space-y-4"
      >
        <div className="font-serif text-2xl mb-4">
          {lang === "en" ? "Create a code" : "Créer un code"}
        </div>
        <div className="grid md:grid-cols-3 gap-4">
          <label className="block">
            <div className="label-caps text-[#737373] mb-2 text-xs">Code</div>
            <input
              data-testid="promo-code-input"
              value={form.code}
              onChange={(e) => setForm({ ...form, code: e.target.value.toUpperCase() })}
              placeholder="BILLY20"
              required
              className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none uppercase"
            />
          </label>
          <label className="block">
            <div className="label-caps text-[#737373] mb-2 text-xs">Type</div>
            <select
              value={form.kind}
              onChange={(e) => setForm({ ...form, kind: e.target.value })}
              className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none"
            >
              <option value="percent">%</option>
              <option value="fixed">$ {lang === "en" ? "Fixed amount" : "Montant fixe"}</option>
            </select>
          </label>
          <label className="block">
            <div className="label-caps text-[#737373] mb-2 text-xs">
              {form.kind === "percent" ? "%" : "$"} {lang === "en" ? "Value" : "Valeur"}
            </div>
            <input
              type="number"
              step="0.01"
              value={form.value}
              onChange={(e) => setForm({ ...form, value: e.target.value })}
              required
              className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none"
            />
          </label>
          <label className="block">
            <div className="label-caps text-[#737373] mb-2 text-xs">
              {lang === "en" ? "Min subtotal ($)" : "Sous-total min ($)"}
            </div>
            <input
              type="number"
              step="0.01"
              value={form.min_subtotal}
              onChange={(e) => setForm({ ...form, min_subtotal: e.target.value })}
              className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none"
            />
          </label>
          <label className="block">
            <div className="label-caps text-[#737373] mb-2 text-xs">
              {lang === "en" ? "Category (optional)" : "Catégorie (facultatif)"}
            </div>
            <select
              value={form.category}
              onChange={(e) => setForm({ ...form, category: e.target.value })}
              className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none"
            >
              <option value="">{lang === "en" ? "All categories" : "Toutes"}</option>
              <option value="women">Femme / Women</option>
              <option value="men">Homme / Men</option>
              <option value="jewelry">Bijoux / Jewelry</option>
              <option value="kids">Enfant / Kids</option>
            </select>
          </label>
          <label className="block">
            <div className="label-caps text-[#737373] mb-2 text-xs">
              {lang === "en" ? "Max uses (optional)" : "Utilisations max"}
            </div>
            <input
              type="number"
              value={form.max_uses}
              onChange={(e) => setForm({ ...form, max_uses: e.target.value })}
              className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none"
            />
          </label>
          <label className="block">
            <div className="label-caps text-[#737373] mb-2 text-xs">
              {lang === "en" ? "Expires on (optional)" : "Expire le"}
            </div>
            <input
              type="date"
              value={form.expires_at}
              onChange={(e) => setForm({ ...form, expires_at: e.target.value })}
              className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none"
            />
          </label>
        </div>
        <div className="flex justify-end">
          <button
            data-testid="promo-create-btn"
            disabled={creating}
            className="bg-[#1a1a1a] text-[#fafaf7] px-8 py-3 label-caps flex items-center gap-2 disabled:bg-[#e5e2dc] bs-btn"
          >
            <Plus size={14} strokeWidth={1.5} />
            {lang === "en" ? "Create" : "Créer"}
          </button>
        </div>
      </form>

      {/* List */}
      {loading ? (
        <div className="text-[#737373]">…</div>
      ) : promos.length === 0 ? (
        <div className="border border-[#e5e2dc] p-12 text-center text-[#737373] flex flex-col items-center gap-4">
          <Tag size={32} strokeWidth={1} />
          {lang === "en" ? "No promo codes yet" : "Aucun code promo pour l'instant"}
        </div>
      ) : (
        <div className="border border-[#e5e2dc] bg-white overflow-x-auto">
          <table className="w-full text-sm">
            <thead className="border-b border-[#e5e2dc]">
              <tr className="text-left">
                {["Code", "Value", "Min", "Category", "Uses", "Expires", ""].map((h) => (
                  <th key={h} className="p-4 label-caps text-xs text-[#737373]">
                    {h}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {promos.map((p) => (
                <tr key={p.id} className="border-b border-[#e5e2dc]/60">
                  <td className="p-4 font-serif">{p.code}</td>
                  <td className="p-4">
                    {p.kind === "percent" ? `${p.value}%` : `$${p.value}`}
                  </td>
                  <td className="p-4">${p.min_subtotal || 0}</td>
                  <td className="p-4 label-caps text-xs">{p.category || "all"}</td>
                  <td className="p-4">
                    {p.uses || 0}
                    {p.max_uses ? ` / ${p.max_uses}` : ""}
                  </td>
                  <td className="p-4 text-xs">
                    {p.expires_at ? new Date(p.expires_at).toLocaleDateString() : "—"}
                  </td>
                  <td className="p-4">
                    <button
                      data-testid={`promo-delete-${p.code}`}
                      onClick={() => del(p.code)}
                      className="w-8 h-8 border border-[#e5e2dc] text-[#8c3a3a] flex items-center justify-center hover:border-[#8c3a3a]"
                    >
                      <Trash2 size={13} strokeWidth={1.5} />
                    </button>
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
