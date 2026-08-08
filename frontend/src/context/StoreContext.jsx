import React, { createContext, useContext, useEffect, useMemo, useReducer, useState } from "react";
import { translations } from "@/lib/i18n";

const StoreContext = createContext(null);

const CART_KEY = "billystore_cart_v1";
const WISH_KEY = "billystore_wish_v1";
const LANG_KEY = "billystore_lang_v1";

const initialCart = () => {
  try {
    return JSON.parse(localStorage.getItem(CART_KEY) || "[]");
  } catch {
    return [];
  }
};
const initialWish = () => {
  try {
    return JSON.parse(localStorage.getItem(WISH_KEY) || "[]");
  } catch {
    return [];
  }
};

function cartReducer(state, action) {
  switch (action.type) {
    case "ADD": {
      const item = action.payload;
      const key = `${item.product_id}-${item.size || ""}-${item.color || ""}`;
      const existing = state.find(
        (i) => `${i.product_id}-${i.size || ""}-${i.color || ""}` === key
      );
      if (existing) {
        return state.map((i) =>
          i === existing ? { ...i, quantity: i.quantity + (item.quantity || 1) } : i
        );
      }
      return [...state, { ...item, quantity: item.quantity || 1 }];
    }
    case "UPDATE_QTY":
      return state.map((i) =>
        i.line_id === action.payload.line_id
          ? { ...i, quantity: Math.max(1, action.payload.quantity) }
          : i
      );
    case "REMOVE":
      return state.filter((i) => i.line_id !== action.payload);
    case "CLEAR":
      return [];
    default:
      return state;
  }
}

export function StoreProvider({ children }) {
  const [cart, dispatchCart] = useReducer(
    cartReducer,
    null,
    () => initialCart()
  );
  const [wishlist, setWishlist] = useState(initialWish);
  const [lang, setLang] = useState(
    () => localStorage.getItem(LANG_KEY) || "fr"
  );
  const [cartOpen, setCartOpen] = useState(false);
  const [searchOpen, setSearchOpen] = useState(false);

  useEffect(() => {
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
  }, [cart]);
  useEffect(() => {
    localStorage.setItem(WISH_KEY, JSON.stringify(wishlist));
  }, [wishlist]);
  useEffect(() => {
    localStorage.setItem(LANG_KEY, lang);
    document.documentElement.lang = lang;
  }, [lang]);

  const addToCart = (item) => {
    const line_id =
      item.line_id ||
      `${item.product_id}-${item.size || ""}-${item.color || ""}-${Date.now()}`;
    dispatchCart({ type: "ADD", payload: { ...item, line_id } });
    setCartOpen(true);
  };
  const updateQty = (line_id, quantity) =>
    dispatchCart({ type: "UPDATE_QTY", payload: { line_id, quantity } });
  const removeFromCart = (line_id) =>
    dispatchCart({ type: "REMOVE", payload: line_id });
  const clearCart = () => dispatchCart({ type: "CLEAR" });

  const toggleWishlist = (productId) => {
    setWishlist((prev) =>
      prev.includes(productId)
        ? prev.filter((id) => id !== productId)
        : [...prev, productId]
    );
  };
  const inWishlist = (productId) => wishlist.includes(productId);

  const t = useMemo(() => (key) => translations[lang]?.[key] || key, [lang]);

  const totals = useMemo(() => {
    const subtotal = cart.reduce((s, i) => s + i.price * i.quantity, 0);
    const freeThreshold = 150;
    const shipping = subtotal >= freeThreshold || subtotal === 0 ? 0 : 12;
    const total = subtotal + shipping;
    const count = cart.reduce((s, i) => s + i.quantity, 0);
    const progressToFree = Math.min(100, (subtotal / freeThreshold) * 100);
    const amountToFree = Math.max(0, freeThreshold - subtotal);
    return { subtotal, shipping, total, count, progressToFree, amountToFree, freeThreshold };
  }, [cart]);

  const value = {
    cart,
    wishlist,
    lang,
    setLang,
    t,
    cartOpen,
    setCartOpen,
    searchOpen,
    setSearchOpen,
    addToCart,
    updateQty,
    removeFromCart,
    clearCart,
    toggleWishlist,
    inWishlist,
    totals,
  };

  return <StoreContext.Provider value={value}>{children}</StoreContext.Provider>;
}

export const useStore = () => {
  const ctx = useContext(StoreContext);
  if (!ctx) throw new Error("useStore must be used within StoreProvider");
  return ctx;
};
