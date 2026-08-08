import React from "react";
import { Plus, Trash2, Users as UsersIcon, Shield } from "lucide-react";
import { useAuth } from "@/context/AuthContext";
import { useStore } from "@/context/StoreContext";
import { toast } from "sonner";

const ROLES = [
  { value: "super_admin", label_fr: "Super Admin", label_en: "Super Admin", desc_fr: "Accès total (produits, commandes, promos, équipe)", desc_en: "Full access" },
  { value: "products_editor", label_fr: "Éditeur Produits", label_en: "Products Editor", desc_fr: "Peut gérer uniquement le catalogue", desc_en: "Can manage catalog only" },
  { value: "orders_manager", label_fr: "Gestionnaire Commandes", label_en: "Orders Manager", desc_fr: "Peut gérer uniquement les commandes", desc_en: "Can manage orders only" },
];

const emptyUser = { email: "", password: "", name: "", role: "products_editor" };

export default function AdminUsers() {
  const { admin, authAxios } = useAuth();
  const { lang } = useStore();
  const [users, setUsers] = React.useState([]);
  const [loading, setLoading] = React.useState(true);
  const [form, setForm] = React.useState(emptyUser);
  const [creating, setCreating] = React.useState(false);

  const load = async () => {
    setLoading(true);
    const r = await authAxios.get("/admin/users");
    setUsers(r.data);
    setLoading(false);
  };

  React.useEffect(() => {
    load();
  }, []);

  const create = async (e) => {
    e.preventDefault();
    setCreating(true);
    try {
      await authAxios.post("/admin/users", form);
      toast.success(lang === "en" ? "Team member added" : "Membre ajouté");
      setForm(emptyUser);
      load();
    } catch (e) {
      toast.error(e?.response?.data?.detail || "Error");
    } finally {
      setCreating(false);
    }
  };

  const updateRole = async (user_id, role) => {
    try {
      await authAxios.patch(`/admin/users/${user_id}/role`, { role });
      toast.success(lang === "en" ? "Role updated" : "Rôle mis à jour");
      load();
    } catch (e) {
      toast.error(e?.response?.data?.detail || "Error");
    }
  };

  const del = async (user_id, email) => {
    if (!window.confirm(`${lang === "en" ? "Remove" : "Retirer"} ${email} ?`)) return;
    try {
      await authAxios.delete(`/admin/users/${user_id}`);
      toast.success(lang === "en" ? "Removed" : "Retiré");
      load();
    } catch (e) {
      toast.error(e?.response?.data?.detail || "Error");
    }
  };

  const roleLabel = (r) => {
    const found = ROLES.find((x) => x.value === r);
    return found ? (lang === "en" ? found.label_en : found.label_fr) : r;
  };

  return (
    <div data-testid="admin-users-page" className="space-y-10">
      <div>
        <h1 className="font-serif text-4xl tracking-tight">
          {lang === "en" ? "Team" : "Équipe"}
        </h1>
        <p className="text-[#737373] text-sm mt-2 max-w-xl">
          {lang === "en"
            ? "Invite collaborators and control what they can access. Only super admins see this page."
            : "Invitez vos collaborateurs et contrôlez leur accès. Seuls les super admins voient cette page."}
        </p>
      </div>

      {/* Create form */}
      <form
        onSubmit={create}
        data-testid="user-create-form"
        className="border border-[#e5e2dc] bg-white p-6 md:p-8 space-y-4"
      >
        <div className="font-serif text-2xl mb-4 flex items-center gap-3">
          <Plus size={20} strokeWidth={1.4} className="text-[#a88b5f]" />
          {lang === "en" ? "Add a team member" : "Ajouter un membre"}
        </div>
        <div className="grid md:grid-cols-2 gap-4">
          <label className="block">
            <div className="label-caps text-[#737373] mb-2 text-xs">
              {lang === "en" ? "Full name" : "Nom complet"}
            </div>
            <input
              data-testid="user-name-input"
              value={form.name}
              onChange={(e) => setForm({ ...form, name: e.target.value })}
              required
              className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none"
            />
          </label>
          <label className="block">
            <div className="label-caps text-[#737373] mb-2 text-xs">Email</div>
            <input
              data-testid="user-email-input"
              type="email"
              value={form.email}
              onChange={(e) => setForm({ ...form, email: e.target.value })}
              required
              className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none"
            />
          </label>
          <label className="block">
            <div className="label-caps text-[#737373] mb-2 text-xs">
              {lang === "en" ? "Temporary password" : "Mot de passe temporaire"}
            </div>
            <input
              data-testid="user-password-input"
              type="text"
              value={form.password}
              onChange={(e) => setForm({ ...form, password: e.target.value })}
              required
              minLength={8}
              placeholder={lang === "en" ? "At least 8 chars" : "8 caractères minimum"}
              className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none"
            />
          </label>
          <label className="block">
            <div className="label-caps text-[#737373] mb-2 text-xs">
              {lang === "en" ? "Role" : "Rôle"}
            </div>
            <select
              data-testid="user-role-select"
              value={form.role}
              onChange={(e) => setForm({ ...form, role: e.target.value })}
              className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-2.5 text-sm outline-none"
            >
              {ROLES.map((r) => (
                <option key={r.value} value={r.value}>
                  {lang === "en" ? r.label_en : r.label_fr}
                </option>
              ))}
            </select>
          </label>
        </div>
        <div className="text-xs text-[#737373]">
          {ROLES.find((r) => r.value === form.role)?.[lang === "en" ? "desc_en" : "desc_fr"]}
        </div>
        <div className="flex justify-end">
          <button
            data-testid="user-create-btn"
            disabled={creating}
            className="bg-[#1a1a1a] text-[#fafaf7] px-8 py-3 label-caps flex items-center gap-2 disabled:bg-[#e5e2dc] bs-btn"
          >
            <Plus size={14} strokeWidth={1.5} />
            {lang === "en" ? "Invite" : "Inviter"}
          </button>
        </div>
      </form>

      {/* List */}
      {loading ? (
        <div className="text-[#737373]">…</div>
      ) : (
        <div className="border border-[#e5e2dc] bg-white overflow-x-auto">
          <table className="w-full text-sm">
            <thead className="border-b border-[#e5e2dc]">
              <tr className="text-left">
                {["", "Name", "Email", "Role", ""].map((h, i) => (
                  <th key={i} className="p-4 label-caps text-xs text-[#737373]">
                    {h}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {users.map((u) => (
                <tr key={u.user_id} className="border-b border-[#e5e2dc]/60">
                  <td className="p-4">
                    <div className="w-10 h-10 bg-[#f0ece3] rounded-full flex items-center justify-center font-serif">
                      {(u.name || u.email)[0].toUpperCase()}
                    </div>
                  </td>
                  <td className="p-4 font-serif">
                    {u.name}
                    {u.user_id === admin.user_id && (
                      <span className="label-caps text-[9px] text-[#a88b5f] ml-2">
                        {lang === "en" ? "You" : "Vous"}
                      </span>
                    )}
                  </td>
                  <td className="p-4">{u.email}</td>
                  <td className="p-4">
                    {u.user_id === admin.user_id ? (
                      <span className="label-caps text-xs bg-[#f0ece3] px-3 py-1.5 inline-flex items-center gap-1.5">
                        <Shield size={11} strokeWidth={1.5} />
                        {roleLabel(u.role)}
                      </span>
                    ) : (
                      <select
                        data-testid={`user-role-${u.user_id}`}
                        value={u.role}
                        onChange={(e) => updateRole(u.user_id, e.target.value)}
                        className="label-caps text-xs bg-[#f0ece3] px-3 py-1.5 border-0 outline-none"
                      >
                        {ROLES.map((r) => (
                          <option key={r.value} value={r.value}>
                            {lang === "en" ? r.label_en : r.label_fr}
                          </option>
                        ))}
                      </select>
                    )}
                  </td>
                  <td className="p-4 text-right">
                    {u.user_id !== admin.user_id && (
                      <button
                        data-testid={`user-delete-${u.user_id}`}
                        onClick={() => del(u.user_id, u.email)}
                        className="w-8 h-8 border border-[#e5e2dc] text-[#8c3a3a] flex items-center justify-center hover:border-[#8c3a3a] ml-auto"
                      >
                        <Trash2 size={13} strokeWidth={1.5} />
                      </button>
                    )}
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
