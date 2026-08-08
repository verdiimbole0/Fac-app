import React from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "@/context/AuthContext";
import { useStore } from "@/context/StoreContext";
import { toast } from "sonner";

// REMINDER: DO NOT HARDCODE THE URL, OR ADD ANY FALLBACKS OR REDIRECT URLS, THIS BREAKS THE AUTH
export default function AdminLogin() {
  const { loginJwt, admin } = useAuth();
  const { t, lang, setLang } = useStore();
  const navigate = useNavigate();
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [loading, setLoading] = React.useState(false);

  React.useEffect(() => {
    if (admin) navigate("/admin", { replace: true });
  }, [admin, navigate]);

  const submit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await loginJwt(email, password);
      toast.success(lang === "en" ? "Welcome" : "Bienvenue");
      navigate("/admin", { replace: true });
    } catch (err) {
      toast.error(
        err?.response?.data?.detail ||
          (lang === "en" ? "Invalid credentials" : "Identifiants invalides")
      );
    } finally {
      setLoading(false);
    }
  };

  const googleLogin = () => {
    // REMINDER: DO NOT HARDCODE THE URL, OR ADD ANY FALLBACKS OR REDIRECT URLS, THIS BREAKS THE AUTH
    const redirectUrl = window.location.origin + "/admin/auth-callback";
    window.location.href = `https://auth.emergentagent.com/?redirect=${encodeURIComponent(redirectUrl)}`;
  };

  return (
    <main
      data-testid="admin-login-page"
      className="min-h-[calc(100vh-80px)] grid grid-cols-1 lg:grid-cols-2"
    >
      {/* Left visual */}
      <aside className="hidden lg:block relative bg-[#1a1a1a] overflow-hidden">
        <img
          src="https://images.unsplash.com/photo-1759852694046-e571667a680d?crop=entropy&cs=srgb&fm=jpg&q=85&w=1200"
          alt=""
          className="absolute inset-0 w-full h-full object-cover opacity-70"
        />
        <div className="absolute inset-0 bg-gradient-to-tr from-[#1a1a1a]/70 to-transparent" />
        <div className="relative z-10 p-14 h-full flex flex-col justify-between text-[#fafaf7]">
          <div className="font-serif text-3xl">
            Billy's<span className="text-[#c5a880]">.</span>
          </div>
          <div>
            <div className="label-caps text-[#c5a880] mb-4">Back-office</div>
            <h1 className="font-serif text-5xl leading-tight">
              {lang === "en"
                ? "Manage your store\nwith elegance."
                : "Gérez votre boutique\navec élégance."}
            </h1>
          </div>
        </div>
      </aside>

      {/* Form */}
      <div className="flex items-center justify-center px-6 py-16 bg-[#fafaf7]">
        <div className="w-full max-w-md">
          <div className="flex justify-end mb-8 gap-2">
            <button
              data-testid="admin-lang-fr"
              onClick={() => setLang("fr")}
              className={`label-caps px-3 py-1.5 border ${lang === "fr" ? "bg-[#1a1a1a] text-[#fafaf7] border-[#1a1a1a]" : "border-[#e5e2dc]"}`}
            >
              FR
            </button>
            <button
              data-testid="admin-lang-en"
              onClick={() => setLang("en")}
              className={`label-caps px-3 py-1.5 border ${lang === "en" ? "bg-[#1a1a1a] text-[#fafaf7] border-[#1a1a1a]" : "border-[#e5e2dc]"}`}
            >
              EN
            </button>
          </div>

          <div className="label-caps text-[#a88b5f] mb-3">
            {lang === "en" ? "Admin access" : "Espace admin"}
          </div>
          <h2 className="font-serif text-4xl md:text-5xl leading-tight tracking-tight mb-3">
            {lang === "en" ? "Sign in" : "Connexion"}
          </h2>
          <p className="text-[#737373] text-sm mb-10">
            {lang === "en"
              ? "Access your Billy's Store back-office."
              : "Accédez au back-office de Billy's Store."}
          </p>

          <button
            data-testid="google-login-btn"
            onClick={googleLogin}
            className="w-full border border-[#1a1a1a] py-3.5 flex items-center justify-center gap-3 hover:bg-[#1a1a1a] hover:text-[#fafaf7] bs-btn mb-6"
          >
            <svg width="18" height="18" viewBox="0 0 48 48">
              <path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.2 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/>
              <path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/>
              <path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/>
              <path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/>
            </svg>
            <span className="label-caps">
              {lang === "en" ? "Continue with Google" : "Continuer avec Google"}
            </span>
          </button>

          <div className="flex items-center gap-4 my-6 text-[#737373]">
            <div className="flex-1 h-px bg-[#e5e2dc]" />
            <span className="label-caps text-xs">
              {lang === "en" ? "Or with email" : "Ou par email"}
            </span>
            <div className="flex-1 h-px bg-[#e5e2dc]" />
          </div>

          <form onSubmit={submit} className="space-y-4">
            <label className="block">
              <div className="label-caps text-[#737373] mb-2 text-xs">
                {t("email")}
              </div>
              <input
                data-testid="admin-email-input"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-3 text-sm outline-none transition-colors"
                placeholder="admin@billystore.com"
              />
            </label>
            <label className="block">
              <div className="label-caps text-[#737373] mb-2 text-xs">
                {lang === "en" ? "Password" : "Mot de passe"}
              </div>
              <input
                data-testid="admin-password-input"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                className="w-full border border-[#e5e2dc] focus:border-[#1a1a1a] bg-white px-4 py-3 text-sm outline-none transition-colors"
              />
            </label>
            <button
              data-testid="admin-login-submit"
              disabled={loading}
              className="w-full bg-[#1a1a1a] text-[#fafaf7] py-4 label-caps hover:bg-[#333] disabled:bg-[#e5e2dc] disabled:text-[#737373] bs-btn"
            >
              {loading ? "…" : lang === "en" ? "Sign in" : "Se connecter"}
            </button>
          </form>

          <p className="text-xs text-[#737373] mt-6">
            {lang === "en" ? "Default admin: " : "Admin par défaut : "}
            <code className="bg-[#f0ece3] px-1.5 py-0.5">admin@billystore.com</code>
          </p>
        </div>
      </div>
    </main>
  );
}
