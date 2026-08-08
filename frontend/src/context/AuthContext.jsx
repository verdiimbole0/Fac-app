import React, { createContext, useContext, useEffect, useState } from "react";
import axios from "axios";
import { API } from "@/lib/api";

const AuthContext = createContext(null);
const TOKEN_KEY = "billystore_admin_token";

export function AuthProvider({ children }) {
  const [admin, setAdmin] = useState(null);
  const [loading, setLoading] = useState(true);
  const [token, setTokenState] = useState(
    () => localStorage.getItem(TOKEN_KEY) || null
  );

  const setToken = (t) => {
    if (t) localStorage.setItem(TOKEN_KEY, t);
    else localStorage.removeItem(TOKEN_KEY);
    setTokenState(t);
  };

  const authAxios = axios.create({ baseURL: API, withCredentials: true });
  authAxios.interceptors.request.use((config) => {
    if (token) config.headers.Authorization = `Bearer ${token}`;
    return config;
  });

  const checkAuth = async () => {
    // If a session_id fragment is in URL, skip /me — AuthCallback will process it first
    if (window.location.hash?.includes("session_id=")) {
      setLoading(false);
      return;
    }
    try {
      const r = await authAxios.get("/auth/me");
      setAdmin(r.data);
    } catch {
      setAdmin(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    checkAuth();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const loginJwt = async (email, password) => {
    const r = await authAxios.post("/auth/login", { email, password });
    setToken(r.data.access_token);
    // Fetch fresh /auth/me to get role + permissions
    try {
      const me = await axios.get(`${API}/auth/me`, {
        headers: { Authorization: `Bearer ${r.data.access_token}` },
      });
      setAdmin(me.data);
    } catch {
      setAdmin({ ...r.data.user, auth_type: "jwt" });
    }
    return r.data.user;
  };

  const finishGoogleLogin = async (sessionId) => {
    await authAxios.post("/auth/google-session", { session_id: sessionId });
    // Fetch full /auth/me for role & permissions
    const me = await authAxios.get("/auth/me");
    setAdmin(me.data);
    return me.data;
  };

  const hasPerm = (perm) =>
    Array.isArray(admin?.permissions) && admin.permissions.includes(perm);

  const logout = async () => {
    try {
      await authAxios.post("/auth/logout");
    } catch {}
    setToken(null);
    setAdmin(null);
  };

  return (
    <AuthContext.Provider
      value={{ admin, loading, loginJwt, finishGoogleLogin, logout, authAxios, token, hasPerm }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be within AuthProvider");
  return ctx;
};
