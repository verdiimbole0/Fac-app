import React from "react";
import { Link } from "react-router-dom";
import { Heart, Star } from "lucide-react";
import { useStore } from "@/context/StoreContext";
import { localizedName } from "@/lib/i18n";
import { formatPrice } from "@/lib/api";

export default function ProductCard({ product, index = 0 }) {
  const { lang, t, toggleWishlist, inWishlist, addToCart } = useStore();
  const [img1, img2] = product.images;
  const soldOut = product.stock === 0;
  const hasNew = product.badges?.includes("new");
  const hasBest = product.badges?.includes("bestseller");
  const discount = product.compare_at && product.compare_at > product.price;
  const wished = inWishlist(product.id);

  return (
    <article
      data-testid={`product-card-${product.slug}`}
      className="bs-card group relative bs-fade-up"
      style={{ animationDelay: `${Math.min(index * 60, 400)}ms` }}
    >
      <Link to={`/product/${product.slug}`} className="block">
        <div className="relative aspect-[3/4] bg-[#f0ece3] overflow-hidden">
          <img
            src={img1}
            alt={localizedName(product, lang)}
            loading="lazy"
            className="bs-img-primary absolute inset-0 w-full h-full object-cover"
          />
          {img2 && (
            <img
              src={img2}
              alt=""
              loading="lazy"
              className="bs-img-secondary absolute inset-0 w-full h-full object-cover"
            />
          )}

          {/* Badges */}
          <div className="absolute top-3 left-3 flex flex-col gap-1.5">
            {hasNew && !soldOut && (
              <span className="label-caps bg-[#fafaf7] text-[#1a1a1a] px-2 py-1">
                {t("new")}
              </span>
            )}
            {hasBest && !soldOut && (
              <span className="label-caps bg-[#c5a880] text-[#1a1a1a] px-2 py-1">
                {t("bestseller")}
              </span>
            )}
            {soldOut && (
              <span className="label-caps bg-[#1a1a1a] text-[#fafaf7] px-2 py-1">
                {t("sold_out")}
              </span>
            )}
            {discount && !soldOut && (
              <span className="label-caps bg-[#8c3a3a] text-[#fafaf7] px-2 py-1">
                -{Math.round(((product.compare_at - product.price) / product.compare_at) * 100)}%
              </span>
            )}
          </div>

          {/* Wishlist */}
          <button
            data-testid={`wishlist-btn-${product.slug}`}
            aria-label="Wishlist"
            onClick={(e) => {
              e.preventDefault();
              toggleWishlist(product.id);
            }}
            className="absolute top-3 right-3 w-9 h-9 bg-[#fafaf7]/90 hover:bg-[#fafaf7] flex items-center justify-center bs-btn"
          >
            <Heart
              size={16}
              strokeWidth={1.4}
              className={wished ? "fill-[#8c3a3a] stroke-[#8c3a3a]" : ""}
            />
          </button>

          {/* Quick add - hidden on mobile */}
          {!soldOut && (
            <div className="bs-quick absolute bottom-0 left-0 right-0 p-3 hidden md:block">
              <button
                data-testid={`quick-add-${product.slug}`}
                onClick={(e) => {
                  e.preventDefault();
                  addToCart({
                    product_id: product.id,
                    name: localizedName(product, lang),
                    price: product.price,
                    image: product.images[0],
                    quantity: 1,
                    slug: product.slug,
                    size: product.variants?.sizes?.[0] || null,
                    color: product.variants?.colors?.[0]?.name || null,
                  });
                }}
                className="w-full bg-[#1a1a1a] text-[#fafaf7] py-3 label-caps hover:bg-[#333] bs-btn"
              >
                {t("add_to_cart")}
              </button>
            </div>
          )}
        </div>

        {/* Info */}
        <div className="pt-4 flex justify-between items-start gap-4">
          <div className="min-w-0">
            <div className="label-caps text-[#737373] mb-1 truncate">
              {product.subcategory}
            </div>
            <h3 className="font-serif text-lg md:text-xl leading-tight truncate">
              {localizedName(product, lang)}
            </h3>
            <div className="flex items-center gap-1 mt-1.5 text-xs text-[#737373]">
              <Star size={12} strokeWidth={1.5} className="fill-[#c5a880] stroke-[#c5a880]" />
              <span>{product.rating.toFixed(1)}</span>
              <span className="opacity-60">({product.reviews_count})</span>
            </div>
          </div>
          <div className="text-right whitespace-nowrap">
            <div className="text-base md:text-lg">
              {formatPrice(product.price, lang)}
            </div>
            {discount && (
              <div className="text-xs text-[#737373] line-through">
                {formatPrice(product.compare_at, lang)}
              </div>
            )}
          </div>
        </div>
      </Link>
    </article>
  );
}
