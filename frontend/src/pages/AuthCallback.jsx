import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useAuth } from "@/context/AuthContext";

export default function AuthCallback() {
  const location = useLocation();
  const navigate = useNavigate();
  const { finishGoogleLogin } = useAuth();
  const processedRef = React.useRef(false);
  const [error, setError] = React.useState(null);

  React.useEffect(() => {
    if (processedRef.current) return;
    processedRef.current = true;

    const hash = location.hash || window.location.hash;
    const match = hash.match(/session_id=([^&]+)/);
    if (!match) {
      navigate("/admin/login");
      return;
    }
    (async () => {
      try {
        await finishGoogleLogin(match[1]);
        // Clean the fragment
        window.history.replaceState(null, "", "/admin");
        navigate("/admin", { replace: true });
      } catch (e) {
        setError(
          e?.response?.data?.detail ||
            "Erreur de connexion Google — accès restreint à l'administrateur."
        );
      }
    })();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <main className="min-h-[70vh] flex items-center justify-center px-6">
      <div className="text-center max-w-md">
        <div className="font-serif text-2xl mb-3">
          {error ? "Accès refusé" : "Connexion en cours…"}
        </div>
        {error && (
          <>
            <p className="text-[#737373] text-sm mb-6">{error}</p>
            <button
              onClick={() => navigate("/admin/login")}
              className="label-caps border border-[#1a1a1a] px-6 py-3 hover:bg-[#1a1a1a] hover:text-[#fafaf7] bs-btn"
            >
              Retour au login
            </button>
          </>
        )}
      </div>
    </main>
  );
}
