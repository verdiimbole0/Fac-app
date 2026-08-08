import React from "react";
import { Link } from "react-router-dom";
import { Heart } from "lucide-react";
import { useStore } from "@/context/StoreContext";
import { fetchProducts } from "@/lib/api";
import ProductCard from "@/components/product/ProductCard";

export default function Wishlist() {
  const { wishlist, t } = useStore();
  const [products, setProducts] = React.useState([]);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    (async () => {
      setLoading(true);
      const all = await fetchProducts({ limit: 200 });
      setProducts(all.filter((p) => wishlist.includes(p.id)));
      setLoading(false);
    })();
  }, [wishlist]);

  return (
    <main data-testid="wishlist-page" className="max-w-[1400px] mx-auto px-5 md:px-10 py-12 md:py-20 min-h-[60vh]">
      <div className="mb-10 md:mb-14">
        <div className="label-caps text-[#a88b5f] mb-3">{t("wishlist")}</div>
        <h1 className="font-serif text-4xl md:text-5xl lg:text-6xl tracking-tight">
          {t("wishlist")}
        </h1>
      </div>

      {loading ? (
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-x-4 gap-y-10 md:gap-x-6 md:gap-y-14">
          {Array.from({ length: 4 }).map((_, i) => (
            <div key={i} className="animate-pulse">
              <div className="aspect-[3/4] bg-[#f0ece3]" />
            </div>
          ))}
        </div>
      ) : products.length === 0 ? (
        <div
          data-testid="wishlist-empty"
          className="py-24 border border-[#e5e2dc] flex flex-col items-center text-center"
        >
          <Heart size={44} strokeWidth={1} className="text-[#737373] mb-6" />
          <h3 className="font-serif text-3xl mb-2">{t("wishlist_empty_title")}</h3>
          <p className="text-[#737373] max-w-sm mb-8">{t("wishlist_empty_body")}</p>
          <Link
            to="/c/all"
            className="bg-[#1a1a1a] text-[#fafaf7] px-8 py-3.5 label-caps hover:bg-[#333] bs-btn"
          >
            {t("cart_empty_cta")}
          </Link>
        </div>
      ) : (
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-x-4 gap-y-10 md:gap-x-6 md:gap-y-14">
          {products.map((p, i) => (
            <ProductCard key={p.id} product={p} index={i} />
          ))}
        </div>
      )}
    </main>
  );
}
