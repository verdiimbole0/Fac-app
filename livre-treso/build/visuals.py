"""Visuels originaux (bandeaux de chapitres, pages de parties, couvertures). Aucune image externe."""
import os, sys, math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(ROOT, "data"))
import fil_rouge as F
OUT = os.path.join(ROOT, "illustrations", "design"); os.makedirs(OUT, exist_ok=True)
FD = os.path.expanduser("~/.fonts/")
def font(name, px): return ImageFont.truetype(FD + name, int(px))
DPI = 300; MM = DPI / 25.4
NAVY = (10, 30, 63); NAVY2 = (22, 56, 107); DEEP = (5, 16, 36); TEAL = (27, 158, 143); TEAL_L = (90, 214, 196); WHITE = (255, 255, 255)
GOLD = (214, 178, 94)

def gradient(w, h, c0=NAVY2, c1=DEEP, cx=0.35, cy=0.3):
    y, x = np.mgrid[0:h, 0:w]
    d = np.sqrt(((x / w - cx) * 1.2) ** 2 + ((y / h - cy)) ** 2); d = np.clip(d / 1.05, 0, 1)
    img = np.zeros((h, w, 3))
    for i in range(3): img[..., i] = c0[i] * (1 - d) + c1[i] * d
    return Image.fromarray(img.astype("uint8"), "RGB")

def grid(img, step, alpha=22, color=(120, 160, 210)):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    w, h = img.size
    for x in range(0, w, step): d.line([(x, 0), (x, h)], fill=color + (alpha,), width=1)
    for y in range(0, h, step): d.line([(0, y), (w, y)], fill=color + (alpha,), width=1)
    return Image.alpha_composite(img.convert("RGBA"), lay)

def glow(img, draw_fn, radius=18, strength=2):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); draw_fn(ImageDraw.Draw(lay))
    blur = lay.filter(ImageFilter.GaussianBlur(radius))
    out = img.convert("RGBA")
    for _ in range(strength): out = Image.alpha_composite(out, blur)
    return Image.alpha_composite(out, lay)

def skyline(img, base_y, height, values, x0, x1, seed=1, alpha=235, top_line=True):
    rnd = random.Random(seed); lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    n = len(values); vmax = max(values); bw = (x1 - x0) / n
    for i, v in enumerate(values):
        hh = height * (0.18 + 0.82 * v / vmax); gap = bw * rnd.uniform(0.12, 0.3)
        xa = x0 + i * bw + gap / 2; xb = x0 + (i + 1) * bw - gap / 2
        shade = rnd.uniform(0.0, 1.0); col = tuple(int(NAVY[k] * (1 - shade) + NAVY2[k] * shade) for k in range(3))
        d.rectangle([xa, base_y - hh, xb, base_y], fill=col + (alpha,))
        # « fenêtres » : petites lignes de données
        for yy in np.arange(base_y - hh + 10, base_y - 6, max(10, (xb - xa) / 3)):
            if rnd.random() < 0.55: d.line([(xa + 5, yy), (xb - 5, yy)], fill=(120, 170, 220, rnd.randint(25, 70)), width=2)
        if top_line: d.line([(xa, base_y - hh), (xb, base_y - hh)], fill=TEAL + (255,), width=4)
    return Image.alpha_composite(img.convert("RGBA"), lay)

def trend(img, pts, width=7, color=TEAL_L, dots=True):
    def fn(d):
        d.line(pts, fill=color + (255,), width=width, joint="curve")
        if dots:
            for p in pts[::max(1, len(pts) // 7)]: d.ellipse([p[0] - width * 1.4, p[1] - width * 1.4, p[0] + width * 1.4, p[1] + width * 1.4], fill=WHITE + (255,))
        p = pts[-1]; r = width * 2.6; d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=color + (255,))
    return glow(img, fn, radius=width * 3, strength=2)

def series_points(vals, x0, x1, ytop, ybot):
    v = np.array(vals, float); lo, hi = v.min(), v.max(); xs = np.linspace(x0, x1, len(v))
    ys = ybot - (v - lo) / (hi - lo + 1e-9) * (ybot - ytop)
    # lissage par interpolation
    xi = np.linspace(x0, x1, len(v) * 12); yi = np.interp(xi, xs, ys)
    k = 9; yi = np.convolve(np.pad(yi, k, mode="edge"), np.ones(2 * k + 1) / (2 * k + 1), mode="same")[k:-k]
    return list(zip(xi, yi))

def dial(img, c, r, alpha=90, ticks=72, needle_deg=None):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); cx, cy = c
    for rr, wd in ((r, 5), (r * 0.82, 3), (r * 0.62, 2)):
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=TEAL + (alpha,), width=wd)
    for t in range(ticks):
        a = 2 * math.pi * t / ticks; l = 0.1 if t % 6 == 0 else 0.05
        d.line([(cx + r * math.cos(a), cy + r * math.sin(a)), (cx + r * (1 - l) * math.cos(a), cy + r * (1 - l) * math.sin(a))], fill=TEAL + (alpha,), width=4 if t % 6 == 0 else 2)
    if needle_deg is not None:
        a = math.radians(needle_deg)
        d.line([(cx, cy), (cx + r * 0.75 * math.cos(a), cy + r * 0.75 * math.sin(a))], fill=TEAL_L + (min(255, alpha * 2),), width=8)
        d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=TEAL_L + (min(255, alpha * 2),))
    return Image.alpha_composite(img.convert("RGBA"), lay)

def digits(img, region, seed=3, alpha=28, size=26):
    rnd = random.Random(seed); lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    f = font("SourceSans3-Regular.ttf", size); x0, y0, x1, y1 = region
    for _ in range(int((x1 - x0) * (y1 - y0) / 9000)):
        s = rnd.choice(["+", "-", ""]) + f"{rnd.randint(1, 99)} {rnd.randint(0, 999):03d}"
        d.text((rnd.uniform(x0, x1), rnd.uniform(y0, y1)), s, font=f, fill=(150, 190, 230, rnd.randint(alpha // 3, alpha)))
    return Image.alpha_composite(img.convert("RGBA"), lay)

# -------- séries « réelles » du livre utilisées comme motifs --------------------
SERIES = {
    1: [70, 62, 48, 35, 22, 15, 30, 44], 2: F.CREANCES_BUCKETS + [30_000, 52_000, 41_000],
    3: [r['cloture'] + 30000 for r in F.W_BASE], 4: [26500, 26500, 26500, 26500, 25688, 25688, 29250, 29250, 30000],
    5: [F.M_PLAN[m]['cloture'] + 10000 for m in range(1, 7)], 6: [r['cloture'] + 25000 for r in F.W_REPREV],
    7: [13000, 12890, 14390, 12890, 16340, 16450, 15000, 18000], 8: [F.TRESO_31JAN, 22000, 18550, 40900, 51300, 54550],
    9: [F.SCEN_PES_MES['m'][m]['cloture'] + 10000 for m in (4, 5, 6)] + [40000, 47000, 52000],
    10: [r['cloture'] + 12000 for r in F.ASBL_REEL], 11: [3, 5, 4, 7, 6, 9, 8, 11, 10, 13], 12: [r['cloture'] for r in F.C12_W_MES]}

def chapter_band(num, w_mm=148, h_mm=64):
    w, h = int(w_mm * MM), int(h_mm * MM); rnd = random.Random(num)
    img = gradient(w, h, cx=0.25 + 0.05 * (num % 3), cy=0.2)
    img = grid(img, int(9 * MM), alpha=16)
    img = digits(img, (0, 0, w * 0.6, h * 0.75), seed=num, alpha=34)
    img = dial(img, (w * 0.83, h * 0.42), h * 0.62, alpha=50)
    vals = SERIES[num]; ext = [abs(v) for v in vals] * 2
    img = skyline(img, h + 2, h * 0.52, [max(1, e * rnd.uniform(0.6, 1.2)) for e in ext][:16], -20, w * 0.72, seed=num * 7, alpha=230)
    pts = series_points(vals, w * 0.03, w * 0.64, h * 0.30, h * 0.70)
    img = trend(img, pts, width=7)
    d = ImageDraw.Draw(img)
    f = font("Montserrat-ExtraBold.ttf", h * 0.62); s = f"{num:02d}"
    tb = d.textbbox((0, 0), s, font=f); tw = tb[2] - tb[0]; x = w - tw - w * 0.05; y = h * 0.08 - tb[1]
    img = glow(img, lambda dd: dd.text((x, y), s, font=f, fill=TEAL + (255,)), radius=22, strength=1)
    d = ImageDraw.Draw(img)
    d.text((x + 6, y + h * 0.66), "CHAPITRE", font=font("Montserrat-SemiBold.ttf", h * 0.07), fill=(200, 230, 225, 255))
    img.convert("RGB").save(os.path.join(OUT, f"bandeau_ch{num:02d}.jpg"), quality=92, dpi=(DPI, DPI))

def part_page(roman, idx, w_mm=148, h_mm=210):
    w, h = int(w_mm * MM), int(h_mm * MM); rnd = random.Random(100 + idx)
    img = gradient(w, h, cx=0.3, cy=0.25)
    img = grid(img, int(10 * MM), alpha=14)
    img = digits(img, (0, h * 0.45, w, h), seed=idx, alpha=26)
    img = dial(img, (w * 0.95, h * 0.52), w * 0.42, alpha=42)
    vals = [rnd.uniform(0.2, 1) for _ in range(22)]
    img = skyline(img, h + 2, h * 0.36, vals, -30, w + 30, seed=idx * 13, alpha=235)
    pts = series_points([v + i * 0.06 for i, v in enumerate([rnd.uniform(0, 1) for _ in range(12)])], w * 0.05, w * 0.92, h * 0.60, h * 0.80)
    img = trend(img, pts, width=8)
    d = ImageDraw.Draw(img); f = font("Montserrat-ExtraBold.ttf", h * 0.30)
    tb = d.textbbox((0, 0), roman, font=f)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).text((w - (tb[2] - tb[0]) - w * 0.06, h * 0.36 - tb[1]), roman, font=f, fill=TEAL + (60,))
    img = Image.alpha_composite(img, lay)
    img.convert("RGB").save(os.path.join(OUT, f"partie_{idx}.jpg"), quality=92, dpi=(DPI, DPI))

def title_band(w_mm=148, h_mm=92):
    w, h = int(w_mm * MM), int(h_mm * MM)
    img = gradient(w, h, cx=0.3, cy=0.3); img = grid(img, int(9 * MM), alpha=16)
    img = digits(img, (0, 0, w, h * 0.7), seed=42, alpha=26)
    img = dial(img, (w * 0.86, h * 0.40), h * 0.48, alpha=55, needle_deg=330)
    img = skyline(img, h + 2, h * 0.45, [0.3 + 0.7 * ((i * 37) % 11) / 11 * (0.6 + i / 30) for i in range(20)], -20, w + 20, seed=5, alpha=235)
    img = trend(img, series_points([15, 9, 4, 11, 19, 16, 27, 24, 33, 30, 41, 46, 52, 57], w * 0.05, w * 0.70, h * 0.35, h * 0.78), width=8)
    img.convert("RGB").save(os.path.join(OUT, "bandeau_titre.jpg"), quality=92, dpi=(DPI, DPI))

if __name__ == "__main__":
    title_band()
    for n in range(1, 13): chapter_band(n)
    for i, r in enumerate(["I", "II", "III", "IV"], 1): part_page(r, i)
    print(sorted(os.listdir(OUT)))
