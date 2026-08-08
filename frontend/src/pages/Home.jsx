import React from "react";
import { Link } from "react-router-dom";
import { ArrowRight } from "lucide-react";
import { useStore } from "@/context/StoreContext";
import { fetchProducts, fetchCategories } from "@/lib/api";
import { localizedCategory } from "@/lib/i18n";
import ProductCard from "@/components/product/ProductCard";

export default function Home() {
  const { t, lang } = useStore();
  const [featured, setFeatured] = React.useState([]);
  const [newArrivals, setNewArrivals] = React.useState([]);
  const [categories, setCategories] = React.useState([]);

  React.useEffect(() => {
    (async () => {
      const [f, n, c] = await Promise.all([
        fetchProducts({ sort: "bestseller", limit: 8 }),
        fetchProducts({ sort: "newest", limit: 4 }),
        fetchCategories(),
      ]);
      setFeatured(f);
      setNewArrivals(n);
      setCategories(c);
    })();
  }, []);

  return (
    <main data-testid="home-page">
      {/* HERO */}
      <section className="relative overflow-hidden bs-grain bg-[#fafaf7]">
        <div className="max-w-[1400px] mx-auto px-5 md:px-10 py-16 md:py-24 lg:py-32 grid grid-cols-12 gap-6 lg:gap-10 items-center">
          <div className="col-span-12 lg:col-span-5 relative z-10 bs-fade-up">
            <div className="label-caps text-[#a88b5f] mb-6">
              {t("hero_kicker")}
            </div>
            <h1 className="font-serif text-5xl sm:text-6xl lg:text-7xl leading-[0.95] tracking-tight whitespace-pre-line">
              {t("hero_title")}
            </h1>
            <p className="text-[#737373] mt-6 max-w-md text-base leading-relaxed">
              {t("hero_sub")}
            </p>
            <div className="mt-10 flex flex-wrap gap-4">
              <Link
                to="/c/women"
                data-testid="hero-cta-primary"
                className="bg-[#1a1a1a] text-[#fafaf7] px-8 py-4 label-caps hover:bg-[#333] bs-btn inline-flex items-center gap-2"
              >
                {t("hero_cta")} <ArrowRight size={16} strokeWidth={1.4} />
              </Link>
              <Link
                to="/c/all?sort=newest"
                data-testid="hero-cta-secondary"
                className="border border-[#1a1a1a] px-8 py-4 label-caps hover:bg-[#1a1a1a] hover:text-[#fafaf7] bs-btn"
              >
                {t("hero_cta_secondary")}
              </Link>
            </div>
          </div>
          <div className="col-span-12 lg:col-span-7 relative bs-fade-up" style={{ animationDelay: "150ms" }}>
            <div className="relative aspect-[4/5] lg:aspect-[5/6] bg-[#f0ece3]">
              <img
                src="https://images.unsplash.com/photo-1759852694046-e571667a680d?crop=entropy&cs=srgb&fm=jpg&q=85&w=1600"
                alt="Editorial hero"
                className="absolute inset-0 w-full h-full object-cover"
              />
              <div className="hidden lg:block absolute -bottom-6 -left-6 bg-[#fafaf7] px-6 py-5 max-w-[260px]">
                <div className="label-caps text-[#a88b5f] mb-2">
                  Édition limitée
                </div>
                <div className="font-serif text-lg leading-tight">
                  Blazers structurés & cachemires nobles.
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CATEGORIES */}
      <section className="max-w-[1400px] mx-auto px-5 md:px-10 py-20 md:py-28">
        <div className="flex justify-between items-end mb-10 md:mb-14">
          <h2 className="font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight">
            {t("shop_by_category")}
          </h2>
        </div>
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6">
          {categories.map((c, i) => (
            <Link
              key={c.slug}
              to={`/c/${c.slug}`}
              data-testid={`category-card-${c.slug}`}
              className="group relative aspect-[3/4] overflow-hidden bg-[#f0ece3] bs-fade-up"
              style={{ animationDelay: `${i * 80}ms` }}
            >
              <img
                src={c.hero}
                alt={localizedCategory(c.slug, lang)}
                className="w-full h-full object-cover transition-transform duration-[900ms] group-hover:scale-[1.06]"
              />
              <div className="absolute inset-x-0 bottom-0 p-4 md:p-6 bg-gradient-to-t from-black/60 to-transparent">
                <div className="font-serif text-white text-xl md:text-2xl lg:text-3xl">
                  {localizedCategory(c.slug, lang)}
                </div>
                <div className="label-caps text-[#c5a880] mt-1 flex items-center gap-2">
                  Découvrir <ArrowRight size={14} strokeWidth={1.5} />
                </div>
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* FEATURED */}
      <section className="max-w-[1400px] mx-auto px-5 md:px-10 pb-20 md:pb-28">
        <div className="flex justify-between items-end mb-10 md:mb-14">
          <div>
            <div className="label-caps text-[#a88b5f] mb-3">Édition</div>
            <h2 className="font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight">
              {t("featured")}
            </h2>
          </div>
          <Link
            to="/c/all"
            className="hidden md:inline-flex items-center gap-2 label-caps hover:text-[#a88b5f]"
          >
            {t("nav_all")} <ArrowRight size={14} strokeWidth={1.5} />
          </Link>
        </div>
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-x-4 gap-y-10 md:gap-x-6 md:gap-y-14">
          {featured.map((p, i) => (
            <ProductCard key={p.id} product={p} index={i} />
          ))}
        </div>
      </section>

      {/* EDITORIAL */}
      <section className="bg-[#1a1a1a] text-[#fafaf7] relative overflow-hidden">
        <div className="max-w-[1400px] mx-auto px-5 md:px-10 py-24 md:py-32 grid grid-cols-12 gap-6 lg:gap-12 items-center">
          <div className="col-span-12 lg:col-span-6 order-2 lg:order-1">
            <div className="aspect-[4/5] bg-[#333]">
              <img
                src="https://images.unsplash.com/photo-1611095006346-d5e3313245e1?crop=entropy&cs=srgb&fm=jpg&q=85&w=1600"
                alt="Craft"
                className="w-full h-full object-cover"
              />
            </div>
          </div>
          <div className="col-span-12 lg:col-span-6 lg:pl-12 order-1 lg:order-2">
            <div className="label-caps text-[#c5a880] mb-6">
              {t("editorial_kicker")}
            </div>
            <h2 className="font-serif text-4xl md:text-5xl lg:text-6xl leading-[1.05]">
              {t("editorial_title")}
            </h2>
            <p className="text-[#fafaf7]/70 mt-6 leading-relaxed max-w-lg">
              {t("editorial_body")}
            </p>
            <a
              href="#"
              className="mt-10 inline-block label-caps border-b border-[#c5a880] pb-1 text-[#c5a880]"
            >
              {t("editorial_cta")} →
            </a>
          </div>
        </div>
      </section>

      {/* NEW ARRIVALS */}
      {newArrivals.length > 0 && (
        <section className="max-w-[1400px] mx-auto px-5 md:px-10 py-20 md:py-28">
          <div className="flex justify-between items-end mb-10">
            <h2 className="font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight">
              {t("hero_cta_secondary")}
            </h2>
          </div>
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-x-4 gap-y-10 md:gap-x-6 md:gap-y-14">
            {newArrivals.map((p, i) => (
              <ProductCard key={p.id} product={p} index={i} />
            ))}
          </div>
        </section>
      )}
    </main>
  );
}
