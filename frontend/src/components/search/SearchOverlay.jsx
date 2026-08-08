import React from "react";
import { useNavigate } from "react-router-dom";
import { Search, X } from "lucide-react";
import { Dialog, DialogContent } from "@/components/ui/dialog";
import { useStore } from "@/context/StoreContext";
import { suggestProducts, formatPrice } from "@/lib/api";
import { localizedName } from "@/lib/i18n";

export default function SearchOverlay() {
  const { searchOpen, setSearchOpen, t, lang } = useStore();
  const [q, setQ] = React.useState("");
  const [results, setResults] = React.useState([]);
  const [loading, setLoading] = React.useState(false);
  const navigate = useNavigate();

  React.useEffect(() => {
    if (!searchOpen) {
      setQ("");
      setResults([]);
    }
  }, [searchOpen]);

  React.useEffect(() => {
    if (!q || q.length < 1) {
      setResults([]);
      return;
    }
    let cancelled = false;
    setLoading(true);
    const t = setTimeout(async () => {
      try {
        const data = await suggestProducts(q);
        if (!cancelled) setResults(data);
      } finally {
        if (!cancelled) setLoading(false);
      }
    }, 200);
    return () => {
      cancelled = true;
      clearTimeout(t);
    };
  }, [q]);

  const go = (slug) => {
    setSearchOpen(false);
    navigate(`/product/${slug}`);
  };
  const viewAll = () => {
    setSearchOpen(false);
    navigate(`/c/all?search=${encodeURIComponent(q)}`);
  };

  return (
    <Dialog open={searchOpen} onOpenChange={setSearchOpen}>
      <DialogContent
        data-testid="search-overlay"
        className="max-w-3xl bg-[#fafaf7] border-[#e5e2dc] rounded-none p-0 top-[10%] translate-y-0"
      >
        <div className="p-6 border-b border-[#e5e2dc] flex items-center gap-4">
          <Search size={20} strokeWidth={1.4} className="text-[#737373]" />
          <input
            autoFocus
            data-testid="search-input"
            value={q}
            onChange={(e) => setQ(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && q) viewAll();
            }}
            placeholder={t("search_placeholder")}
            className="flex-1 bg-transparent outline-none font-serif text-2xl placeholder:text-[#737373]/60"
          />
          <button onClick={() => setSearchOpen(false)} aria-label="Close">
            <X size={20} strokeWidth={1.4} />
          </button>
        </div>
        <div className="max-h-[60vh] overflow-y-auto">
          {q && results.length === 0 && !loading && (
            <div
              data-testid="search-no-results"
              className="p-12 text-center text-[#737373]"
            >
              <p className="font-serif text-xl mb-2">
                {t("search_no_results")} "{q}"
              </p>
            </div>
          )}
          {results.length > 0 && (
            <ul>
              {results.map((r) => (
                <li key={r.id}>
                  <button
                    data-testid={`search-result-${r.slug}`}
                    onClick={() => go(r.slug)}
                    className="w-full flex items-center gap-4 p-4 hover:bg-[#f0ece3] text-left bs-btn"
                  >
                    <img
                      src={r.images[0]}
                      alt=""
                      className="w-14 h-16 object-cover bg-[#f0ece3]"
                    />
                    <div className="flex-1 min-w-0">
                      <div className="label-caps text-[#737373] text-[10px]">
                        {r.category}
                      </div>
                      <div className="font-serif text-base truncate">
                        {lang === "en" ? r.name_en : r.name_fr}
                      </div>
                    </div>
                    <div className="text-sm">{formatPrice(r.price, lang)}</div>
                  </button>
                </li>
              ))}
              <li className="border-t border-[#e5e2dc]">
                <button
                  data-testid="search-view-all"
                  onClick={viewAll}
                  className="w-full label-caps p-4 hover:bg-[#f0ece3] bs-btn"
                >
                  {t("search_view_all")} →
                </button>
              </li>
            </ul>
          )}
        </div>
      </DialogContent>
    </Dialog>
  );
}
