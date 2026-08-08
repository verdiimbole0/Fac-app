import React from "react";
import { Link } from "react-router-dom";
import { Instagram, Twitter, Facebook } from "lucide-react";
import { useStore } from "@/context/StoreContext";

export default function Footer() {
  const { t } = useStore();
  return (
    <footer className="mt-32 bg-[#1a1a1a] text-[#fafaf7]">
      <div className="max-w-[1400px] mx-auto px-6 md:px-12 py-20 grid grid-cols-1 md:grid-cols-12 gap-12">
        <div className="md:col-span-5">
          <h3 className="font-serif text-3xl md:text-4xl leading-tight mb-4">
            {t("footer_newsletter_title")}
          </h3>
          <p className="text-[#fafaf7]/70 max-w-md mb-6 text-sm leading-relaxed">
            {t("footer_newsletter_body")}
          </p>
          <form
            data-testid="newsletter-form"
            onSubmit={(e) => e.preventDefault()}
            className="flex border-b border-[#fafaf7]/40 pb-2 max-w-md"
          >
            <input
              data-testid="newsletter-input"
              type="email"
              placeholder="email@example.com"
              className="bg-transparent flex-1 outline-none text-sm placeholder:text-[#fafaf7]/40 py-2"
            />
            <button
              data-testid="newsletter-submit"
              className="label-caps text-[#c5a880] hover:text-[#fafaf7] bs-btn"
            >
              {t("footer_subscribe")} →
            </button>
          </form>
        </div>
        <div className="md:col-span-2">
          <div className="label-caps mb-4 text-[#fafaf7]/50">{t("footer_shop")}</div>
          <ul className="space-y-2 text-sm">
            <li><Link to="/c/women" className="hover:text-[#c5a880]">Women</Link></li>
            <li><Link to="/c/men" className="hover:text-[#c5a880]">Men</Link></li>
            <li><Link to="/c/jewelry" className="hover:text-[#c5a880]">Jewelry</Link></li>
            <li><Link to="/c/kids" className="hover:text-[#c5a880]">Kids</Link></li>
          </ul>
        </div>
        <div className="md:col-span-2">
          <div className="label-caps mb-4 text-[#fafaf7]/50">{t("footer_help")}</div>
          <ul className="space-y-2 text-sm">
            <li><a href="#" className="hover:text-[#c5a880]">Shipping</a></li>
            <li><a href="#" className="hover:text-[#c5a880]">Returns</a></li>
            <li><a href="#" className="hover:text-[#c5a880]">Size guide</a></li>
            <li><a href="#" className="hover:text-[#c5a880]">Contact</a></li>
          </ul>
        </div>
        <div className="md:col-span-3">
          <div className="label-caps mb-4 text-[#fafaf7]/50">{t("footer_about")}</div>
          <ul className="space-y-2 text-sm">
            <li><a href="#" className="hover:text-[#c5a880]">Our story</a></li>
            <li><a href="#" className="hover:text-[#c5a880]">Sustainability</a></li>
            <li><a href="#" className="hover:text-[#c5a880]">Ateliers</a></li>
          </ul>
          <div className="flex gap-4 mt-6">
            <a href="#" className="hover:text-[#c5a880]"><Instagram size={18} strokeWidth={1.4} /></a>
            <a href="#" className="hover:text-[#c5a880]"><Twitter size={18} strokeWidth={1.4} /></a>
            <a href="#" className="hover:text-[#c5a880]"><Facebook size={18} strokeWidth={1.4} /></a>
          </div>
        </div>
      </div>
      <div className="border-t border-[#fafaf7]/10">
        <div className="max-w-[1400px] mx-auto px-6 md:px-12 py-6 flex flex-col md:flex-row justify-between items-center text-xs text-[#fafaf7]/50 gap-3">
          <div>© 2026 Billy's Store — {t("all_rights")}</div>
          <div className="font-serif italic">Crafted with care.</div>
        </div>
      </div>
    </footer>
  );
}
