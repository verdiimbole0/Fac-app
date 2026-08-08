import React from "react";
import { useNavigate, useParams } from "react-router-dom";
import { ArrowLeft, Save, X } from "lucide-react";
import { useAuth } from "@/context/AuthContext";
import { useStore } from "@/context/StoreContext";
import { fetchProduct } from "@/lib/api";
import { toast } from "sonner";

const emptyForm = {
  slug: "",
  name_fr: "",
  name_en: "",
  category: "women",
  subcategory: "",
  price: 100,
  compare_at: null,
  currency: "USD",
  images: [""],
  description_fr: "",
  description_en: "",
  composition_fr: "",
  composition_en: "",
  variants: { sizes: [], colors: [], materials: [] },
  rating: 4.7,
  reviews_count: 0,
  reviews: [],
  stock: 20,
  badges: [],
};

function Field({ label, ...props }) {
  return (
    <label className="block">
      <div className="label-caps text-[#737373] mb-2 text-xs">{label}</div>
      <input
        {...props}
        className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none"
      />
    </label>
  );
}
function TA({ label, ...props }) {
  return (
    <label className="block">
      <div className="label-caps text-[#737373] mb-2 text-xs">{label}</div>
      <textarea
        {...props}
        rows={3}
        className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none resize-y"
      />
    </label>
  );
}

export default function AdminProductEdit() {
  const { slug } = useParams();
  const isNew = !slug;
  const { authAxios } = useAuth();
  const { lang } = useStore();
  const navigate = useNavigate();
  const [form, setForm] = React.useState(emptyForm);
  const [loading, setLoading] = React.useState(!isNew);
  const [saving, setSaving] = React.useState(false);

  React.useEffect(() => {
    if (isNew) return;
    (async () => {
      const p = await fetchProduct(slug);
      setForm({ ...emptyForm, ...p });
      setLoading(false);
    })();
  }, [slug, isNew]);

  const save = async () => {
    setSaving(true);
    try {
      const payload = {
        ...form,
        price: Number(form.price),
        compare_at: form.compare_at ? Number(form.compare_at) : null,
        stock: Number(form.stock),
        reviews_count: Number(form.reviews_count),
        rating: Number(form.rating),
        images: form.images.filter((i) => i && i.trim()),
      };
      if (isNew) {
        await authAxios.post("/admin/products", payload);
      } else {
        await authAxios.put(`/admin/products/${slug}`, payload);
      }
      toast.success(lang === "en" ? "Saved" : "Enregistré");
      navigate("/admin/products");
    } catch (e) {
      toast.error(e?.response?.data?.detail || "Error");
    } finally {
      setSaving(false);
    }
  };

  const toggleBadge = (b) => {
    setForm((f) => ({
      ...f,
      badges: f.badges.includes(b) ? f.badges.filter((x) => x !== b) : [...f.badges, b],
    }));
  };

  const updateImage = (i, v) => {
    setForm((f) => ({ ...f, images: f.images.map((x, k) => (k === i ? v : x)) }));
  };
  const addImage = () => setForm((f) => ({ ...f, images: [...f.images, ""] }));
  const removeImage = (i) =>
    setForm((f) => ({ ...f, images: f.images.filter((_, k) => k !== i) }));

  if (loading) return <div className="text-[#737373]">…</div>;

  return (
    <div data-testid="admin-product-edit" className="max-w-4xl space-y-6">
      <button
        onClick={() => navigate("/admin/products")}
        className="label-caps text-[#737373] flex items-center gap-2 hover:text-[#1a1a1a]"
      >
        <ArrowLeft size={14} strokeWidth={1.5} /> {lang === "en" ? "Back" : "Retour"}
      </button>
      <h1 className="font-serif text-4xl tracking-tight">
        {isNew ? (lang === "en" ? "New product" : "Nouveau produit") : form.name_fr}
      </h1>

      <div className="grid md:grid-cols-2 gap-4">
        <Field
          data-testid="edit-slug"
          label="Slug (URL)"
          value={form.slug}
          onChange={(e) => setForm({ ...form, slug: e.target.value })}
          disabled={!isNew}
        />
        <label className="block">
          <div className="label-caps text-[#737373] mb-2 text-xs">Category</div>
          <select
            value={form.category}
            onChange={(e) => setForm({ ...form, category: e.target.value })}
            className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none"
          >
            <option value="women">Femme / Women</option>
            <option value="men">Homme / Men</option>
            <option value="jewelry">Bijoux / Jewelry</option>
            <option value="kids">Enfant / Kids</option>
          </select>
        </label>
        <Field label="Nom (FR)" value={form.name_fr} onChange={(e) => setForm({ ...form, name_fr: e.target.value })} />
        <Field label="Name (EN)" value={form.name_en} onChange={(e) => setForm({ ...form, name_en: e.target.value })} />
        <Field label="Sous-catégorie" value={form.subcategory} onChange={(e) => setForm({ ...form, subcategory: e.target.value })} />
        <Field label="Prix (USD)" type="number" step="0.01" value={form.price} onChange={(e) => setForm({ ...form, price: e.target.value })} />
        <Field label="Prix barré" type="number" step="0.01" value={form.compare_at || ""} onChange={(e) => setForm({ ...form, compare_at: e.target.value })} />
        <Field label="Stock" type="number" value={form.stock} onChange={(e) => setForm({ ...form, stock: e.target.value })} />
      </div>

      <TA label="Description (FR)" value={form.description_fr} onChange={(e) => setForm({ ...form, description_fr: e.target.value })} />
      <TA label="Description (EN)" value={form.description_en} onChange={(e) => setForm({ ...form, description_en: e.target.value })} />
      <div className="grid md:grid-cols-2 gap-4">
        <Field label="Composition (FR)" value={form.composition_fr} onChange={(e) => setForm({ ...form, composition_fr: e.target.value })} />
        <Field label="Composition (EN)" value={form.composition_en} onChange={(e) => setForm({ ...form, composition_en: e.target.value })} />
      </div>

      <div>
        <div className="label-caps text-[#737373] mb-2 text-xs">Images (URL)</div>
        <div className="space-y-2">
          {form.images.map((img, i) => (
            <div key={i} className="flex gap-2 items-center">
              {img && <img src={img} alt="" className="w-12 h-14 object-cover bg-[#f0ece3]" />}
              <input
                value={img}
                onChange={(e) => updateImage(i, e.target.value)}
                placeholder="https://…"
                className="flex-1 border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none"
              />
              {form.images.length > 1 && (
                <button onClick={() => removeImage(i)} className="p-2 text-[#8c3a3a]">
                  <X size={14} strokeWidth={1.5} />
                </button>
              )}
            </div>
          ))}
          <button onClick={addImage} className="label-caps text-[#a88b5f] mt-2">
            + Ajouter une image
          </button>
        </div>
      </div>

      <div>
        <div className="label-caps text-[#737373] mb-2 text-xs">Badges</div>
        <div className="flex gap-2">
          {["new", "bestseller"].map((b) => (
            <button
              key={b}
              type="button"
              onClick={() => toggleBadge(b)}
              className={`px-4 py-2 label-caps text-xs border ${form.badges.includes(b) ? "border-[#1a1a1a] bg-[#1a1a1a] text-[#fafaf7]" : "border-[#e5e2dc]"}`}
            >
              {b}
            </button>
          ))}
        </div>
      </div>

      <div className="pt-6 border-t border-[#e5e2dc] flex justify-end gap-3">
        <button
          onClick={() => navigate("/admin/products")}
          className="border border-[#1a1a1a] px-6 py-3 label-caps"
        >
          {lang === "en" ? "Cancel" : "Annuler"}
        </button>
        <button
          data-testid="admin-save-product"
          onClick={save}
          disabled={saving}
          className="bg-[#1a1a1a] text-[#fafaf7] px-8 py-3 label-caps flex items-center gap-2 disabled:bg-[#e5e2dc] bs-btn"
        >
          <Save size={14} strokeWidth={1.5} />
          {saving ? "…" : (lang === "en" ? "Save" : "Enregistrer")}
        </button>
      </div>
    </div>
  );
}
