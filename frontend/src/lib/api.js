import axios from "axios";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
export const API = `${BACKEND_URL}/api`;

export const api = axios.create({ baseURL: API });

export const fetchProducts = (params = {}) =>
  api.get("/products", { params }).then((r) => r.data);
export const fetchProduct = (slug) =>
  api.get(`/products/${slug}`).then((r) => r.data);
export const fetchRelated = (slug) =>
  api.get(`/products/${slug}/related`).then((r) => r.data);
export const fetchCategories = () =>
  api.get("/categories").then((r) => r.data);
export const suggestProducts = (q) =>
  api.get("/products/suggest", { params: { q } }).then((r) => r.data);
export const createOrder = (payload) =>
  api.post("/orders", payload).then((r) => r.data);

export const formatPrice = (v, lang = "fr") =>
  new Intl.NumberFormat(lang === "fr" ? "fr-FR" : "en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 0,
  }).format(v);
