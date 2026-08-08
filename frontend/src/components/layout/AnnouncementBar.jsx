import React from "react";
import { useStore } from "@/context/StoreContext";

export default function AnnouncementBar() {
  const { t } = useStore();
  const items = [t("ann1"), t("ann2"), t("ann3")];
  const repeated = [...items, ...items, ...items, ...items];
  return (
    <div
      data-testid="announcement-bar"
      className="w-full bg-[#1a1a1a] text-[#fafaf7] overflow-hidden border-b border-black/20"
    >
      <div className="flex whitespace-nowrap bs-marquee py-2">
        {repeated.map((txt, i) => (
          <span
            key={i}
            className="label-caps px-8 opacity-90"
            style={{ letterSpacing: "0.28em" }}
          >
            {txt}
            <span className="mx-6 opacity-40">·</span>
          </span>
        ))}
      </div>
    </div>
  );
}
