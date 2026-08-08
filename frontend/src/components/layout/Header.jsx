import React from "react";
import { Link, NavLink, useNavigate } from "react-router-dom";
import { Search, Heart, ShoppingBag, Menu, X } from "lucide-react";
import { useStore } from "@/context/StoreContext";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";

export default function Header() {
  const { t, lang, setLang, wishlist, totals, setCartOpen, setSearchOpen } = useStore();
  const navigate = useNavigate();
  const [mobileOpen, setMobileOpen] = React.useState(false);

  const nav = [
    { to: "/c/women", label: t("nav_women") },
    { to: "/c/men", label: t("nav_men") },
    { to: "/c/jewelry", label: t("nav_jewelry") },
    { to: "/c/kids", label: t("nav_kids") },
    { to: "/c/all", label: t("nav_all") },
  ];

  return (
    <header
      data-testid="site-header"
      className="sticky top-0 z-40 bg-[#fafaf7]/95 backdrop-blur-md border-b border-[#e5e2dc]"
    >
      <div className="max-w-[1400px] mx-auto px-5 md:px-10 h-16 md:h-20 flex items-center justify-between gap-6">
        {/* Mobile menu */}
        <div className="lg:hidden">
          <Sheet open={mobileOpen} onOpenChange={setMobileOpen}>
            <SheetTrigger asChild>
              <button
                data-testid="mobile-menu-btn"
                aria-label="Open menu"
                className="p-2 -ml-2"
              >
                <Menu strokeWidth={1.4} size={22} />
              </button>
            </SheetTrigger>
            <SheetContent side="left" className="w-[85%] max-w-[360px] bg-[#fafaf7] border-r border-[#e5e2dc] p-0">
              <div className="p-6 border-b border-[#e5e2dc] flex items-center justify-between">
                <span className="font-serif text-2xl">Billy's</span>
                <button onClick={() => setMobileOpen(false)} aria-label="Close">
                  <X strokeWidth={1.4} size={20} />
                </button>
              </div>
              <nav className="p-6 flex flex-col gap-5">
                {nav.map((n) => (
                  <NavLink
                    key={n.to}
                    to={n.to}
                    onClick={() => setMobileOpen(false)}
                    data-testid={`mobile-nav-${n.to.split("/").pop()}`}
                    className="font-serif text-2xl tracking-tight"
                  >
                    {n.label}
                  </NavLink>
                ))}
                <div className="mt-6 pt-6 border-t border-[#e5e2dc] flex gap-3">
                  <button
                    onClick={() => setLang("fr")}
                    data-testid="mobile-lang-fr"
                    className={`label-caps px-3 py-1.5 border ${lang === "fr" ? "border-[#1a1a1a] bg-[#1a1a1a] text-[#fafaf7]" : "border-[#e5e2dc]"}`}
                  >
                    FR
                  </button>
                  <button
                    onClick={() => setLang("en")}
                    data-testid="mobile-lang-en"
                    className={`label-caps px-3 py-1.5 border ${lang === "en" ? "border-[#1a1a1a] bg-[#1a1a1a] text-[#fafaf7]" : "border-[#e5e2dc]"}`}
                  >
                    EN
                  </button>
                </div>
              </nav>
            </SheetContent>
          </Sheet>
        </div>

        {/* Logo */}
        <Link
          to="/"
          data-testid="logo-link"
          className="font-serif text-2xl md:text-3xl tracking-tight leading-none"
        >
          Billy's<span className="text-[#a88b5f]">.</span>
        </Link>

        {/* Nav */}
        <nav className="hidden lg:flex items-center gap-9">
          {nav.map((n) => (
            <NavLink
              key={n.to}
              to={n.to}
              data-testid={`nav-${n.to.split("/").pop()}`}
              className={({ isActive }) =>
                `bs-underline label-caps text-[#1a1a1a]/90 hover:text-[#1a1a1a]`
              }
            >
              {n.label}
            </NavLink>
          ))}
        </nav>

        {/* Actions */}
        <div className="flex items-center gap-1 md:gap-3">
          <div className="hidden md:flex items-center border border-[#e5e2dc] mr-1">
            <button
              onClick={() => setLang("fr")}
              data-testid="lang-fr"
              className={`label-caps px-2.5 py-1.5 bs-btn ${lang === "fr" ? "bg-[#1a1a1a] text-[#fafaf7]" : "text-[#1a1a1a]"}`}
            >
              FR
            </button>
            <button
              onClick={() => setLang("en")}
              data-testid="lang-en"
              className={`label-caps px-2.5 py-1.5 bs-btn ${lang === "en" ? "bg-[#1a1a1a] text-[#fafaf7]" : "text-[#1a1a1a]"}`}
            >
              EN
            </button>
          </div>

          <button
            aria-label="Search"
            data-testid="open-search"
            onClick={() => setSearchOpen(true)}
            className="p-2 hover:text-[#a88b5f] bs-btn"
          >
            <Search strokeWidth={1.4} size={20} />
          </button>
          <button
            aria-label="Wishlist"
            data-testid="open-wishlist"
            onClick={() => navigate("/wishlist")}
            className="p-2 relative hover:text-[#a88b5f] bs-btn"
          >
            <Heart strokeWidth={1.4} size={20} />
            {wishlist.length > 0 && (
              <span
                data-testid="wishlist-count"
                className="absolute -top-0.5 -right-0.5 bg-[#c5a880] text-[#1a1a1a] text-[10px] w-4 h-4 flex items-center justify-center rounded-full font-medium"
              >
                {wishlist.length}
              </span>
            )}
          </button>
          <button
            aria-label="Cart"
            data-testid="open-cart"
            onClick={() => setCartOpen(true)}
            className="p-2 relative hover:text-[#a88b5f] bs-btn"
          >
            <ShoppingBag strokeWidth={1.4} size={20} />
            {totals.count > 0 && (
              <span
                data-testid="cart-count"
                className="absolute -top-0.5 -right-0.5 bg-[#1a1a1a] text-[#fafaf7] text-[10px] w-4 h-4 flex items-center justify-center rounded-full font-medium"
              >
                {totals.count}
              </span>
            )}
          </button>
        </div>
      </div>
    </header>
  );
}
