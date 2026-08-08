import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { X, Minus, Plus, ShoppingBag } from "lucide-react";
import { Sheet, SheetContent } from "@/components/ui/sheet";
import { useStore } from "@/context/StoreContext";
import { formatPrice } from "@/lib/api";

export default function CartDrawer() {
  const {
    cart,
    cartOpen,
    setCartOpen,
    updateQty,
    removeFromCart,
    totals,
    t,
    lang,
  } = useStore();
  const navigate = useNavigate();

  const handleCheckout = () => {
    setCartOpen(false);
    navigate("/checkout");
  };

  return (
    <Sheet open={cartOpen} onOpenChange={setCartOpen}>
      <SheetContent
        side="right"
        className="w-full sm:max-w-[480px] p-0 bg-[#fafaf7] border-l border-[#e5e2dc] flex flex-col"
        data-testid="cart-drawer"
      >
        <div className="flex items-center justify-between px-6 py-5 border-b border-[#e5e2dc]">
          <h2 className="font-serif text-2xl">
            {t("cart")}{" "}
            <span className="text-[#737373] text-base">({totals.count})</span>
          </h2>
          <button
            data-testid="close-cart"
            onClick={() => setCartOpen(false)}
            className="p-1"
          >
            <X strokeWidth={1.4} size={22} />
          </button>
        </div>

        {/* Free shipping progress */}
        {cart.length > 0 && (
          <div className="px-6 pt-5 pb-4 border-b border-[#e5e2dc]">
            <div className="text-xs text-[#1a1a1a] mb-2">
              {totals.amountToFree === 0
                ? t("free_shipping_reached")
                : t("free_shipping_progress").replace(
                    "%AMOUNT%",
                    formatPrice(totals.amountToFree, lang)
                  )}
            </div>
            <div className="h-[2px] bg-[#e5e2dc] w-full overflow-hidden">
              <div
                data-testid="free-shipping-bar"
                className="h-full bg-[#c5a880] transition-all duration-500"
                style={{ width: `${totals.progressToFree}%` }}
              />
            </div>
          </div>
        )}

        {/* Items */}
        <div className="flex-1 overflow-y-auto">
          {cart.length === 0 ? (
            <div
              data-testid="cart-empty"
              className="h-full flex flex-col items-center justify-center px-6 py-16 text-center"
            >
              <ShoppingBag
                size={40}
                strokeWidth={1}
                className="text-[#737373] mb-6"
              />
              <h3 className="font-serif text-2xl mb-2">
                {t("cart_empty_title")}
              </h3>
              <p className="text-[#737373] text-sm mb-6 max-w-xs">
                {t("cart_empty_body")}
              </p>
              <button
                onClick={() => setCartOpen(false)}
                className="label-caps border border-[#1a1a1a] text-[#1a1a1a] px-6 py-3 hover:bg-[#1a1a1a] hover:text-[#fafaf7] bs-btn"
              >
                {t("cart_empty_cta")}
              </button>
            </div>
          ) : (
            <ul className="divide-y divide-[#e5e2dc]">
              {cart.map((item) => (
                <li
                  key={item.line_id}
                  data-testid={`cart-item-${item.product_id}`}
                  className="p-6 flex gap-4"
                >
                  <Link
                    to={`/product/${item.slug}`}
                    onClick={() => setCartOpen(false)}
                    className="w-20 h-24 bg-[#f0ece3] flex-shrink-0 overflow-hidden"
                  >
                    <img
                      src={item.image}
                      alt={item.name}
                      className="w-full h-full object-cover"
                    />
                  </Link>
                  <div className="flex-1 min-w-0">
                    <div className="flex justify-between gap-2">
                      <Link
                        to={`/product/${item.slug}`}
                        onClick={() => setCartOpen(false)}
                        className="font-serif text-base truncate hover:text-[#a88b5f]"
                      >
                        {item.name}
                      </Link>
                      <div className="text-sm">
                        {formatPrice(item.price * item.quantity, lang)}
                      </div>
                    </div>
                    <div className="text-xs text-[#737373] mt-1">
                      {[item.size, item.color].filter(Boolean).join(" · ")}
                    </div>
                    <div className="flex justify-between items-center mt-3">
                      <div className="flex items-center border border-[#e5e2dc]">
                        <button
                          data-testid={`cart-decrease-${item.product_id}`}
                          onClick={() =>
                            updateQty(item.line_id, item.quantity - 1)
                          }
                          className="w-8 h-8 flex items-center justify-center hover:bg-[#f0ece3] bs-btn"
                          aria-label="Decrease quantity"
                        >
                          <Minus size={12} strokeWidth={1.5} />
                        </button>
                        <span className="w-8 text-center text-sm">
                          {item.quantity}
                        </span>
                        <button
                          data-testid={`cart-increase-${item.product_id}`}
                          onClick={() =>
                            updateQty(item.line_id, item.quantity + 1)
                          }
                          className="w-8 h-8 flex items-center justify-center hover:bg-[#f0ece3] bs-btn"
                          aria-label="Increase quantity"
                        >
                          <Plus size={12} strokeWidth={1.5} />
                        </button>
                      </div>
                      <button
                        data-testid={`cart-remove-${item.product_id}`}
                        onClick={() => removeFromCart(item.line_id)}
                        className="text-xs underline text-[#737373] hover:text-[#8c3a3a]"
                      >
                        {t("remove")}
                      </button>
                    </div>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>

        {cart.length > 0 && (
          <div className="border-t border-[#e5e2dc] p-6 space-y-4">
            <div className="flex justify-between text-sm">
              <span className="text-[#737373]">{t("subtotal")}</span>
              <span>{formatPrice(totals.subtotal, lang)}</span>
            </div>
            <div className="flex justify-between text-sm">
              <span className="text-[#737373]">{t("shipping")}</span>
              <span>
                {totals.shipping === 0 ? t("free") : formatPrice(totals.shipping, lang)}
              </span>
            </div>
            <button
              data-testid="checkout-btn"
              onClick={handleCheckout}
              className="w-full bg-[#1a1a1a] text-[#fafaf7] py-4 label-caps hover:bg-[#333] bs-btn"
            >
              {t("checkout")} — {formatPrice(totals.total, lang)}
            </button>
          </div>
        )}
      </SheetContent>
    </Sheet>
  );
}
