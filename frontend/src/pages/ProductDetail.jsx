import React from "react";
import { Link, useParams } from "react-router-dom";
import { Heart, Star, Truck, RotateCcw, Shield, ChevronRight, Ruler } from "lucide-react";
import { useStore } from "@/context/StoreContext";
import { fetchProduct, fetchRelated, formatPrice } from "@/lib/api";
import { localizedName, localizedDesc, localizedComp } from "@/lib/i18n";
import ProductCard from "@/components/product/ProductCard";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Dialog, DialogContent, DialogTrigger } from "@/components/ui/dialog";
import { toast } from "sonner";

export default function ProductDetail() {
  const { slug } = useParams();
  const { t, lang, addToCart, toggleWishlist, inWishlist } = useStore();
  const [product, setProduct] = React.useState(null);
  const [related, setRelated] = React.useState([]);
  const [size, setSize] = React.useState(null);
  const [color, setColor] = React.useState(null);
  const [activeImg, setActiveImg] = React.useState(0);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    let cancelled = false;
    setLoading(true);
    (async () => {
      try {
        const p = await fetchProduct(slug);
        if (cancelled) return;
        setProduct(p);
        setSize(p.variants?.sizes?.[0] || null);
        setColor(p.variants?.colors?.[0]?.name || null);
        setActiveImg(0);
        const r = await fetchRelated(slug);
        if (!cancelled) setRelated(r);
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [slug]);

  if (loading || !product) {
    return (
      <main className="max-w-[1400px] mx-auto px-5 md:px-10 py-16 grid grid-cols-12 gap-8">
        <div className="col-span-12 lg:col-span-7 aspect-[4/5] bg-[#f0ece3] animate-pulse" />
        <div className="col-span-12 lg:col-span-5 space-y-4">
          <div className="h-6 w-24 bg-[#f0ece3] animate-pulse" />
          <div className="h-12 w-3/4 bg-[#f0ece3] animate-pulse" />
          <div className="h-6 w-1/3 bg-[#f0ece3] animate-pulse" />
        </div>
      </main>
    );
  }

  const soldOut = product.stock === 0;
  const wished = inWishlist(product.id);

  const handleAdd = () => {
    addToCart({
      product_id: product.id,
      name: localizedName(product, lang),
      price: product.price,
      image: product.images[0],
      quantity: 1,
      slug: product.slug,
      category: product.category,
      size,
      color,
    });
    toast.success(lang === "en" ? "Added to bag" : "Ajouté au panier");
  };

  return (
    <main data-testid="product-detail-page" className="max-w-[1400px] mx-auto px-5 md:px-10 py-8 md:py-12">
      {/* Breadcrumb */}
      <nav className="text-xs text-[#737373] mb-8 flex items-center gap-2">
        <Link to="/" className="hover:text-[#1a1a1a]">Billy's</Link>
        <ChevronRight size={12} strokeWidth={1.5} />
        <Link to={`/c/${product.category}`} className="hover:text-[#1a1a1a] capitalize">
          {product.category}
        </Link>
        <ChevronRight size={12} strokeWidth={1.5} />
        <span className="text-[#1a1a1a]">{localizedName(product, lang)}</span>
      </nav>

      <div className="grid grid-cols-12 gap-6 lg:gap-16">
        {/* Gallery */}
        <div className="col-span-12 lg:col-span-7">
          <div className="grid grid-cols-12 gap-3">
            <div className="hidden lg:flex col-span-2 flex-col gap-3">
              {product.images.map((img, i) => (
                <button
                  key={i}
                  data-testid={`gallery-thumb-${i}`}
                  onClick={() => setActiveImg(i)}
                  className={`aspect-square bg-[#f0ece3] overflow-hidden border-2 ${activeImg === i ? "border-[#1a1a1a]" : "border-transparent"}`}
                >
                  <img src={img} alt="" className="w-full h-full object-cover" />
                </button>
              ))}
            </div>
            <div className="col-span-12 lg:col-span-10">
              <div className="aspect-[4/5] bg-[#f0ece3] overflow-hidden">
                <img
                  src={product.images[activeImg]}
                  alt={localizedName(product, lang)}
                  className="w-full h-full object-cover bs-fade-up"
                  key={activeImg}
                />
              </div>
              <div className="flex gap-2 mt-3 lg:hidden">
                {product.images.map((img, i) => (
                  <button
                    key={i}
                    onClick={() => setActiveImg(i)}
                    className={`w-14 h-14 bg-[#f0ece3] overflow-hidden border-2 ${activeImg === i ? "border-[#1a1a1a]" : "border-transparent"}`}
                  >
                    <img src={img} alt="" className="w-full h-full object-cover" />
                  </button>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Info */}
        <div className="col-span-12 lg:col-span-5">
          <div className="lg:sticky lg:top-28">
            <div className="label-caps text-[#a88b5f] mb-3">{product.subcategory}</div>
            <h1 className="font-serif text-3xl md:text-4xl lg:text-5xl tracking-tight leading-tight">
              {localizedName(product, lang)}
            </h1>

            <div className="flex items-center gap-3 mt-4">
              <div className="flex items-center gap-1 text-sm">
                {Array.from({ length: 5 }).map((_, i) => (
                  <Star
                    key={i}
                    size={14}
                    strokeWidth={1.5}
                    className={i < Math.round(product.rating) ? "fill-[#c5a880] stroke-[#c5a880]" : "stroke-[#e5e2dc]"}
                  />
                ))}
                <span className="ml-2 text-[#737373]">
                  {product.rating.toFixed(1)} · {product.reviews_count} {t("reviews").toLowerCase()}
                </span>
              </div>
            </div>

            <div className="flex items-end gap-3 mt-6">
              <div className="font-serif text-3xl">{formatPrice(product.price, lang)}</div>
              {product.compare_at && (
                <div className="text-[#737373] line-through text-lg mb-1">
                  {formatPrice(product.compare_at, lang)}
                </div>
              )}
            </div>

            <p className="text-[#4a4a4a] text-sm leading-relaxed mt-6">
              {localizedDesc(product, lang)}
            </p>

            {/* Colors */}
            {product.variants?.colors?.length > 0 && (
              <div className="mt-8">
                <div className="flex justify-between mb-3">
                  <div className="label-caps">{t("color")}</div>
                  <div className="text-xs text-[#737373]">{color}</div>
                </div>
                <div className="flex gap-3 flex-wrap">
                  {product.variants.colors.map((c) => (
                    <button
                      key={c.name}
                      data-testid={`color-swatch-${c.name}`}
                      onClick={() => setColor(c.name)}
                      className={`w-9 h-9 rounded-full border-2 bs-btn ${color === c.name ? "border-[#1a1a1a]" : "border-[#e5e2dc]"}`}
                      style={{ backgroundColor: c.hex }}
                      title={c.name}
                    />
                  ))}
                </div>
              </div>
            )}

            {/* Sizes */}
            {product.variants?.sizes?.length > 0 && (
              <div className="mt-8">
                <div className="flex justify-between mb-3">
                  <div className="label-caps">{t("size")}</div>
                  <Dialog>
                    <DialogTrigger asChild>
                      <button
                        data-testid="size-guide-btn"
                        className="text-xs underline flex items-center gap-1.5 text-[#737373] hover:text-[#1a1a1a]"
                      >
                        <Ruler size={12} strokeWidth={1.5} /> {t("size_guide")}
                      </button>
                    </DialogTrigger>
                    <DialogContent className="bg-[#fafaf7] max-w-xl rounded-none">
                      <h3 className="font-serif text-2xl mb-4">{t("size_guide")}</h3>
                      <table className="w-full text-sm">
                        <thead>
                          <tr className="border-b border-[#e5e2dc]">
                            <th className="text-left py-3 label-caps">Taille</th>
                            <th className="text-left py-3 label-caps">Poitrine</th>
                            <th className="text-left py-3 label-caps">Taille</th>
                            <th className="text-left py-3 label-caps">Hanches</th>
                          </tr>
                        </thead>
                        <tbody>
                          {[
                            ["XS", "82-86", "62-66", "88-92"],
                            ["S", "86-90", "66-70", "92-96"],
                            ["M", "90-94", "70-74", "96-100"],
                            ["L", "94-100", "74-80", "100-106"],
                            ["XL", "100-106", "80-86", "106-112"],
                          ].map((r) => (
                            <tr key={r[0]} className="border-b border-[#e5e2dc]/60">
                              {r.map((c, i) => (
                                <td key={i} className="py-3">{c}</td>
                              ))}
                            </tr>
                          ))}
                        </tbody>
                      </table>
                      <p className="text-xs text-[#737373] mt-4">
                        Mesures en centimètres · Compass measurements in cm
                      </p>
                    </DialogContent>
                  </Dialog>
                </div>
                <div className="flex flex-wrap gap-2">
                  {product.variants.sizes.map((s) => (
                    <button
                      key={s}
                      data-testid={`size-option-${s}`}
                      onClick={() => setSize(s)}
                      className={`min-w-[52px] px-3 py-3 text-sm border bs-btn ${size === s ? "border-[#1a1a1a] bg-[#1a1a1a] text-[#fafaf7]" : "border-[#e5e2dc] hover:border-[#1a1a1a]"}`}
                    >
                      {s}
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* CTA */}
            <div className="mt-10 flex gap-3">
              <button
                data-testid="add-to-cart-btn"
                disabled={soldOut}
                onClick={handleAdd}
                className="flex-1 bg-[#1a1a1a] text-[#fafaf7] py-4 label-caps hover:bg-[#333] disabled:bg-[#e5e2dc] disabled:text-[#737373] bs-btn"
              >
                {soldOut ? t("sold_out") : t("add_to_cart")}
              </button>
              <button
                data-testid="wishlist-toggle"
                onClick={() => toggleWishlist(product.id)}
                aria-label="Wishlist"
                className="w-14 border border-[#1a1a1a] flex items-center justify-center hover:bg-[#1a1a1a] hover:text-[#fafaf7] bs-btn"
              >
                <Heart
                  size={18}
                  strokeWidth={1.4}
                  className={wished ? "fill-[#8c3a3a] stroke-[#8c3a3a]" : ""}
                />
              </button>
            </div>

            {/* Trust */}
            <div className="mt-8 pt-6 border-t border-[#e5e2dc] grid grid-cols-3 gap-3 text-xs text-[#4a4a4a]">
              <div className="flex flex-col items-start gap-1.5"><Truck size={16} strokeWidth={1.4} /> Livraison rapide</div>
              <div className="flex flex-col items-start gap-1.5"><RotateCcw size={16} strokeWidth={1.4} /> {t("return_policy")}</div>
              <div className="flex flex-col items-start gap-1.5"><Shield size={16} strokeWidth={1.4} /> {t("secure_payment")}</div>
            </div>

            {/* Accordion */}
            <Accordion type="single" collapsible className="mt-8">
              <AccordionItem value="details" className="border-[#e5e2dc]">
                <AccordionTrigger data-testid="acc-details" className="label-caps hover:no-underline">
                  {t("details")}
                </AccordionTrigger>
                <AccordionContent className="text-sm text-[#4a4a4a] leading-relaxed">
                  {localizedDesc(product, lang)}
                </AccordionContent>
              </AccordionItem>
              <AccordionItem value="composition" className="border-[#e5e2dc]">
                <AccordionTrigger data-testid="acc-composition" className="label-caps hover:no-underline">
                  {t("composition")}
                </AccordionTrigger>
                <AccordionContent className="text-sm text-[#4a4a4a] leading-relaxed">
                  {localizedComp(product, lang)}
                </AccordionContent>
              </AccordionItem>
              <AccordionItem value="returns" className="border-[#e5e2dc]">
                <AccordionTrigger data-testid="acc-returns" className="label-caps hover:no-underline">
                  {t("returns_shipping")}
                </AccordionTrigger>
                <AccordionContent className="text-sm text-[#4a4a4a] leading-relaxed">
                  Livraison offerte dès 150$. Retours gratuits sous 30 jours.
                  Expédition en 48h ouvrées. · Free shipping over $150. Free returns within 30 days.
                </AccordionContent>
              </AccordionItem>
            </Accordion>
          </div>
        </div>
      </div>

      {/* Reviews */}
      {product.reviews?.length > 0 && (
        <section className="mt-24 md:mt-32">
          <div className="flex justify-between items-end mb-10">
            <h2 className="font-serif text-3xl md:text-4xl tracking-tight">
              {t("reviews")}{" "}
              <span className="text-[#737373] text-base">({product.reviews_count})</span>
            </h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {product.reviews.map((r, i) => (
              <div key={i} data-testid={`review-${i}`} className="border border-[#e5e2dc] p-6">
                <div className="flex items-center gap-1 mb-3">
                  {Array.from({ length: 5 }).map((_, k) => (
                    <Star key={k} size={12} strokeWidth={1.5} className={k < r.rating ? "fill-[#c5a880] stroke-[#c5a880]" : "stroke-[#e5e2dc]"} />
                  ))}
                </div>
                <div className="font-serif text-lg mb-2">{r.title}</div>
                <p className="text-sm text-[#4a4a4a] leading-relaxed mb-4">{r.body}</p>
                <div className="text-xs text-[#737373]">
                  {r.author} · <span className="text-[#a88b5f]">{t("verified_purchase")}</span>
                </div>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Related */}
      {related.length > 0 && (
        <section className="mt-24 md:mt-32">
          <h2 className="font-serif text-3xl md:text-4xl tracking-tight mb-10">
            {t("you_may_also_like")}
          </h2>
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-x-4 gap-y-10 md:gap-x-6 md:gap-y-14">
            {related.map((p, i) => (
              <ProductCard key={p.id} product={p} index={i} />
            ))}
          </div>
        </section>
      )}
    </main>
  );
}
