import React from "react";
import { useParams, useSearchParams } from "react-router-dom";
import { SlidersHorizontal, X } from "lucide-react";
import { useStore } from "@/context/StoreContext";
import { fetchProducts } from "@/lib/api";
import { localizedCategory } from "@/lib/i18n";
import ProductCard from "@/components/product/ProductCard";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Slider } from "@/components/ui/slider";
import { Checkbox } from "@/components/ui/checkbox";

const SIZES = ["XS", "S", "M", "L", "XL"];
const COLORS = [
  { name: "Noir", hex: "#111111" },
  { name: "Blanc cassé", hex: "#F5F1EA" },
  { name: "Beige", hex: "#D9C7A7" },
  { name: "Camel", hex: "#A87B4B" },
  { name: "Doré", hex: "#C5A880" },
  { name: "Bleu nuit", hex: "#1F2A44" },
  { name: "Olive", hex: "#6B6F3E" },
  { name: "Anthracite", hex: "#2D2D2F" },
];

function FiltersPanel({ filters, setFilters, clear }) {
  const { t } = useStore();
  return (
    <div className="space-y-8" data-testid="filters-panel">
      <div>
        <div className="flex justify-between items-center mb-4">
          <div className="label-caps">{t("price")}</div>
          <div className="text-xs text-[#737373]">
            ${filters.priceRange[0]} — ${filters.priceRange[1]}
          </div>
        </div>
        <Slider
          data-testid="filter-price-slider"
          value={filters.priceRange}
          min={0}
          max={600}
          step={10}
          onValueChange={(v) => setFilters({ ...filters, priceRange: v })}
        />
      </div>

      <div>
        <div className="label-caps mb-4">{t("size")}</div>
        <div className="flex flex-wrap gap-2">
          {SIZES.map((s) => (
            <button
              key={s}
              data-testid={`filter-size-${s}`}
              onClick={() =>
                setFilters({ ...filters, size: filters.size === s ? null : s })
              }
              className={`px-3 py-1.5 text-xs border bs-btn ${filters.size === s ? "border-[#1a1a1a] bg-[#1a1a1a] text-[#fafaf7]" : "border-[#e5e2dc] hover:border-[#1a1a1a]"}`}
            >
              {s}
            </button>
          ))}
        </div>
      </div>

      <div>
        <div className="label-caps mb-4">{t("color")}</div>
        <div className="flex flex-wrap gap-2">
          {COLORS.map((c) => (
            <button
              key={c.name}
              data-testid={`filter-color-${c.name}`}
              onClick={() =>
                setFilters({
                  ...filters,
                  color: filters.color === c.name ? null : c.name,
                })
              }
              title={c.name}
              className={`w-8 h-8 rounded-full border-2 bs-btn ${filters.color === c.name ? "border-[#1a1a1a]" : "border-[#e5e2dc]"}`}
              style={{ backgroundColor: c.hex }}
            />
          ))}
        </div>
      </div>

      <div>
        <div className="label-caps mb-4">{t("availability")}</div>
        <label className="flex items-center gap-3 cursor-pointer">
          <Checkbox
            data-testid="filter-in-stock"
            checked={filters.availability === "in_stock"}
            onCheckedChange={(v) =>
              setFilters({
                ...filters,
                availability: v ? "in_stock" : null,
              })
            }
          />
          <span className="text-sm">{t("in_stock")}</span>
        </label>
      </div>

      <button
        data-testid="clear-filters"
        onClick={clear}
        className="label-caps underline text-[#737373] hover:text-[#1a1a1a]"
      >
        {t("clear_filters")}
      </button>
    </div>
  );
}

export default function Category() {
  const { slug } = useParams();
  const [searchParams] = useSearchParams();
  const initialSearch = searchParams.get("search") || "";
  const { t, lang } = useStore();

  const [products, setProducts] = React.useState([]);
  const [loading, setLoading] = React.useState(true);
  const [filters, setFilters] = React.useState({
    priceRange: [0, 600],
    size: null,
    color: null,
    availability: null,
  });
  const [sort, setSort] = React.useState("newest");
  const [mobileFilterOpen, setMobileFilterOpen] = React.useState(false);

  const category = slug === "all" ? "all" : slug;

  const clear = () =>
    setFilters({
      priceRange: [0, 600],
      size: null,
      color: null,
      availability: null,
    });

  React.useEffect(() => {
    let cancelled = false;
    setLoading(true);
    (async () => {
      const params = {
        category,
        sort,
        min_price: filters.priceRange[0],
        max_price: filters.priceRange[1],
      };
      if (filters.size) params.size = filters.size;
      if (filters.color) params.color = filters.color;
      if (filters.availability) params.availability = filters.availability;
      if (initialSearch) params.search = initialSearch;
      const data = await fetchProducts(params);
      if (!cancelled) {
        setProducts(data);
        setLoading(false);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [category, sort, filters, initialSearch]);

  const title =
    initialSearch
      ? `"${initialSearch}"`
      : slug === "all"
        ? t("nav_all")
        : localizedCategory(slug, lang);

  return (
    <main data-testid="category-page" className="max-w-[1400px] mx-auto px-5 md:px-10 py-10 md:py-16">
      {/* Header */}
      <div className="mb-10 md:mb-14 flex flex-col md:flex-row md:items-end md:justify-between gap-4">
        <div>
          <div className="label-caps text-[#a88b5f] mb-3">{t("nav_all")}</div>
          <h1 className="font-serif text-4xl md:text-5xl lg:text-6xl tracking-tight">
            {title}
          </h1>
          <div className="text-[#737373] text-sm mt-3">
            {products.length} {t("results")}
          </div>
        </div>
        <div className="flex items-center gap-3">
          <div className="lg:hidden">
            <Sheet open={mobileFilterOpen} onOpenChange={setMobileFilterOpen}>
              <SheetTrigger asChild>
                <button
                  data-testid="mobile-filter-btn"
                  className="border border-[#1a1a1a] px-4 py-2.5 label-caps flex items-center gap-2 bs-btn"
                >
                  <SlidersHorizontal size={14} strokeWidth={1.5} />
                  {t("filters")}
                </button>
              </SheetTrigger>
              <SheetContent side="left" className="bg-[#fafaf7] p-6 w-[85%] max-w-[380px] overflow-y-auto">
                <div className="flex justify-between items-center mb-8">
                  <div className="font-serif text-2xl">{t("filters")}</div>
                  <button onClick={() => setMobileFilterOpen(false)}>
                    <X size={20} strokeWidth={1.4} />
                  </button>
                </div>
                <FiltersPanel filters={filters} setFilters={setFilters} clear={clear} />
              </SheetContent>
            </Sheet>
          </div>
          <Select value={sort} onValueChange={setSort}>
            <SelectTrigger
              data-testid="sort-select"
              className="w-[200px] rounded-none border-[#1a1a1a] bg-[#fafaf7] label-caps"
            >
              <SelectValue placeholder={t("sort_by")} />
            </SelectTrigger>
            <SelectContent className="rounded-none bg-[#fafaf7]">
              <SelectItem value="newest">{t("sort_newest")}</SelectItem>
              <SelectItem value="bestseller">{t("sort_bestseller")}</SelectItem>
              <SelectItem value="price_asc">{t("sort_price_asc")}</SelectItem>
              <SelectItem value="price_desc">{t("sort_price_desc")}</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </div>

      <div className="grid grid-cols-12 gap-6 lg:gap-10">
        {/* Sidebar */}
        <aside className="hidden lg:block lg:col-span-3 pr-6 border-r border-[#e5e2dc]">
          <FiltersPanel filters={filters} setFilters={setFilters} clear={clear} />
        </aside>

        {/* Grid */}
        <div className="col-span-12 lg:col-span-9">
          {loading ? (
            <div className="grid grid-cols-2 lg:grid-cols-3 gap-x-4 gap-y-10 md:gap-x-6 md:gap-y-14">
              {Array.from({ length: 6 }).map((_, i) => (
                <div key={i} className="animate-pulse">
                  <div className="aspect-[3/4] bg-[#f0ece3]" />
                  <div className="h-4 bg-[#f0ece3] mt-4 w-2/3" />
                  <div className="h-4 bg-[#f0ece3] mt-2 w-1/3" />
                </div>
              ))}
            </div>
          ) : products.length === 0 ? (
            <div
              data-testid="empty-results"
              className="py-24 text-center border border-[#e5e2dc]"
            >
              <h3 className="font-serif text-3xl mb-3">
                {t("search_no_results")}
              </h3>
              <button
                onClick={clear}
                className="label-caps underline hover:text-[#a88b5f]"
              >
                {t("clear_filters")}
              </button>
            </div>
          ) : (
            <div className="grid grid-cols-2 lg:grid-cols-3 gap-x-4 gap-y-10 md:gap-x-6 md:gap-y-14">
              {products.map((p, i) => (
                <ProductCard key={p.id} product={p} index={i} />
              ))}
            </div>
          )}
        </div>
      </div>
    </main>
  );
}
