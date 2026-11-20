#!/usr/bin/env python3
"""Couvertures (1re et 4e) et illustration des pages de partie. Création originale.

Usage : python3 07_OUTILS/couverture.py   (depuis ASBL_AUGMENTEE)
Produit 06_LIVRABLES/COUVERTURE/ (PDF format livre, PDF impression avec fond perdu 3 mm, PNG)
et 07_OUTILS/art/partie_art.svg.
"""
import os, math, random, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "07_OUTILS")
OUT = os.path.join(ROOT, "06_LIVRABLES", "COUVERTURE")
ART = os.path.join(TOOLS, "art")
FONTS = os.path.join(TOOLS, "fonts")


def heart(cx, cy, s, n=16):
    pts = []
    for k in range(n):
        t = 2 * math.pi * k / n
        x = 16 * math.sin(t) ** 3
        y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
        pts.append((cx + x * s, cy + y * s))
    return pts


def person(x, y, r, fill, op=1.0):
    return (f'<g opacity="{op}"><circle cx="{x:.1f}" cy="{y - r * 1.05:.1f}" r="{r * 0.62:.1f}" fill="{fill}"/>'
            f'<path d="M{x - r:.1f},{y + r * 1.05:.1f} Q{x - r:.1f},{y - r * 0.1:.1f} {x:.1f},{y - r * 0.1:.1f} '
            f'Q{x + r:.1f},{y - r * 0.1:.1f} {x + r:.1f},{y + r * 1.05:.1f} Z" fill="{fill}"/></g>')


def doc_icon(x, y, w, col, op):
    h = w * 1.3
    s = f'<g opacity="{op}"><rect x="{x - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{w * 0.12:.1f}" fill="none" stroke="{col}" stroke-width="2"/>'
    for i in range(3):
        yy = y - h / 2 + h * (0.3 + 0.2 * i)
        s += f'<line x1="{x - w * 0.3:.1f}" y1="{yy:.1f}" x2="{x + w * (0.3 if i < 2 else 0.05):.1f}" y2="{yy:.1f}" stroke="{col}" stroke-width="2" stroke-linecap="round"/>'
    return s + "</g>"


def chart_icon(x, y, w, col, op):
    s = f'<g opacity="{op}">'
    for i, hh in enumerate((0.35, 0.6, 0.9)):
        s += f'<rect x="{x - w / 2 + i * w * 0.36:.1f}" y="{y + w / 2 - w * hh:.1f}" width="{w * 0.24:.1f}" height="{w * hh:.1f}" rx="2" fill="{col}"/>'
    return s + "</g>"


def network_svg(w, h, cx, cy, scale, dark=True, seed=7):
    rnd = random.Random(seed)
    if dark:
        line, node, ppl, core_in, ring = "#B9B0FF", "#FFFFFF", "#F1EEFF", "#2A1F86", "#9C90FF"
    else:
        line, node, ppl, core_in, ring = "#5B4BD5", "#FFFFFF", "#241A6B", "#FFFFFF", "#7B6CF0"
    g = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" preserveAspectRatio="xMidYMid slice">',
         '<defs><radialGradient id="core" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#FFFFFF" stop-opacity=".95"/>'
         '<stop offset="35%" stop-color="#B7AEFF" stop-opacity=".75"/><stop offset="100%" stop-color="#6C5CE7" stop-opacity="0"/></radialGradient>'
         '<radialGradient id="halo" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#9F8CFF" stop-opacity=".55"/><stop offset="100%" stop-color="#9F8CFF" stop-opacity="0"/></radialGradient>'
         '<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>']
    S = scale
    if not dark:
        g.append('<defs><linearGradient id="bgl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#D6E3FB"/><stop offset=".55" stop-color="#E4DEFC"/><stop offset="1" stop-color="#EFEBFD"/></linearGradient></defs>')
        g.append(f'<rect width="{w}" height="{h}" fill="url(#bgl)"/>')
    # anneaux d'orbite
    for r, dash, op in ((150, "2 7", .35), (250, "", .22), (350, "3 10", .25), (455, "", .12)):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        g.append(f'<circle cx="{cx}" cy="{cy}" r="{r * S}" fill="none" stroke="{ring}" stroke-width="1.4" opacity="{op}"{d}/>')
    # constellation extérieure
    pts = []
    for _ in range(95):
        a = rnd.uniform(0, 2 * math.pi); r = rnd.uniform(280, 640) * S
        x, y = cx + r * math.cos(a) * 1.25, cy + r * math.sin(a) * 0.9
        if -20 < x < w + 20 and -20 < y < h + 20:
            pts.append((x, y, rnd.uniform(1.5, 4.2)))
    for i, (x, y, _) in enumerate(pts):
        near = sorted(pts, key=lambda p: (p[0] - x) ** 2 + (p[1] - y) ** 2)[1:3]
        for (x2, y2, _) in near:
            g.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{line}" stroke-width="1" opacity=".28"/>')
    for (x, y, r) in pts:
        g.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{node}" opacity="{rnd.uniform(.35, .9):.2f}"/>')
    # personnes sur l'anneau 250 et liens vers le cœur
    n = 10; ppl_pts = []
    for k in range(n):
        a = -math.pi / 2 + 2 * math.pi * k / n + 0.12
        x, y = cx + 250 * S * math.cos(a), cy + 250 * S * math.sin(a)
        ppl_pts.append((x, y))
    for k, (x, y) in enumerate(ppl_pts):
        x2, y2 = ppl_pts[(k + 1) % n]
        g.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{line}" stroke-width="1.6" opacity=".55"/>')
        g.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{cx:.1f}" y2="{cy:.1f}" stroke="{line}" stroke-width="1.2" opacity=".35" stroke-dasharray="4 6"/>')
        # liens vers la constellation
        for (px, py, _) in sorted(pts, key=lambda p: (p[0] - x) ** 2 + (p[1] - y) ** 2)[:2]:
            g.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{px:.1f}" y2="{py:.1f}" stroke="{line}" stroke-width="1" opacity=".3"/>')
    # icônes de processus sur l'anneau 350
    for k in range(6):
        a = -math.pi / 2 + 2 * math.pi * k / 6 + math.pi / 6
        x, y = cx + 350 * S * math.cos(a) * 1.02, cy + 350 * S * math.sin(a)
        g.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{20 * S:.1f}" fill="{core_in}" stroke="{ring}" stroke-width="1.5" opacity=".9"/>')
        g.append(doc_icon(x, y, 16 * S, node if dark else "#5B4BD5", .95) if k % 2 == 0 else chart_icon(x, y, 20 * S, node if dark else "#5B4BD5", .95))
    # cœur central
    g.append(f'<circle cx="{cx}" cy="{cy}" r="{230 * S}" fill="url(#halo)"/>')
    g.append(f'<circle cx="{cx}" cy="{cy}" r="{120 * S}" fill="url(#core)"/>')
    g.append(f'<circle cx="{cx}" cy="{cy}" r="{86 * S}" fill="{core_in}" stroke="#D9D3FF" stroke-width="2.2"/>')
    hp = heart(cx, cy + 3 * S, 3.5 * S, 22)
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in heart(cx, cy + 3 * S, 3.5 * S, 90))
    g.append(f'<polygon points="{poly}" fill="{"#8F80FF" if dark else "#C9C1FF"}" opacity=".35"/>')
    inner = [(cx - 20 * S, cy - 4 * S), (cx + 20 * S, cy - 4 * S), (cx, cy + 16 * S)]
    allp = hp + inner
    hl = "#FFFFFF" if dark else "#241A6B"
    for i, (x, y) in enumerate(hp):
        x2, y2 = hp[(i + 1) % len(hp)]
        g.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{hl}" stroke-width="2.4" filter="url(#glow)"/>')
    for (x, y) in inner:
        for (x2, y2) in sorted(hp, key=lambda p: (p[0] - x) ** 2 + (p[1] - y) ** 2)[:2]:
            g.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{hl}" stroke-width="1.2" opacity=".7"/>')
    for i, (x, y) in enumerate(allp):
        g.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{(3.4 if i < len(hp) else 3.0) * S:.1f}" fill="{"#C9C1FF" if dark else "#7B6CF0"}" stroke="{hl}" stroke-width="1.2"/>')
    # personnes (au-dessus des liens)
    for (x, y) in ppl_pts:
        g.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{27 * S:.1f}" fill="{core_in}" stroke="{ring}" stroke-width="1.6" opacity=".95"/>')
        g.append(person(x, y + 3 * S, 12.5 * S, ppl))
    g.append("</svg>")
    return "".join(g)


def faces():
    css = ""
    for w in (400, 500, 600, 700):
        css += f"@font-face{{font-family:'Inter';src:url('file://{FONTS}/inter-latin-{w}-normal.woff2');font-weight:{w}}}"
    for w in (600, 700, 800, 900):
        css += f"@font-face{{font-family:'Outfit';src:url('file://{FONTS}/outfit-latin-{w}-normal.woff2');font-weight:{w}}}"
    return css


BG = ("background:radial-gradient(circle at 18% 12%, rgba(124,108,255,.45), transparent 42%),"
      "radial-gradient(circle at 92% 78%, rgba(63,91,216,.45), transparent 45%),"
      "radial-gradient(circle at 50% 40%, rgba(160,140,255,.18), transparent 60%),"
      "linear-gradient(165deg,#120C3A 0%,#1E1660 38%,#2A1F86 72%,#1A1458 100%);")


def page(body, bleed):
    W, H = 170 + 2 * bleed, 240 + 2 * bleed
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>{faces()}
@page{{size:{W}mm {H}mm;margin:0}}
*{{box-sizing:border-box}} html,body{{margin:0;padding:0}}
.c{{width:{W}mm;height:{H}mm;position:relative;overflow:hidden;{BG}color:#fff;font-family:'Inter',sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.in{{position:absolute;left:{bleed}mm;top:{bleed}mm;width:170mm;height:240mm}}
.pill{{display:inline-block;font:600 8.5pt 'Inter';letter-spacing:.18em;text-transform:uppercase;color:#E3DEFF;border:1.2px solid rgba(201,193,255,.75);border-radius:999px;padding:2.2mm 4.5mm;background:rgba(255,255,255,.06)}}
.grad{{background:linear-gradient(90deg,#E9E5FF 0%,#B7AEFF 45%,#8FA7FF 100%);-webkit-background-clip:text;background-clip:text;color:transparent}}
</style></head><body><div class="c"><div class="in">{body}</div></div></body></html>"""


def front(art):
    return f"""
<div style="position:absolute;left:0;top:14mm;width:170mm;height:132mm">{art}</div>
<div style="position:absolute;left:16mm;top:13mm"><span class="pill">Édition 2026</span></div>
<div style="position:absolute;left:16mm;right:14mm;top:150mm">
  <div style="font:900 62pt/0.9 'Outfit';letter-spacing:.01em">ASBL</div>
  <div class="grad" style="font:900 47pt/1.02 'Outfit';letter-spacing:.005em;margin-top:1.5mm">AUGMENTÉE</div>
  <div style="width:24mm;height:1.6mm;border-radius:1mm;background:linear-gradient(90deg,#9C8CFF,#6F8BFF);margin:6mm 0 5mm"></div>
  <div style="font:500 15pt/1.3 'Inter';color:#DCD7FF;max-width:125mm">Comment implémenter l'IA dans vos processus</div>
</div>
<div style="position:absolute;left:16mm;right:16mm;bottom:13mm;display:flex;justify-content:space-between;align-items:center">
  <div style="font:700 13pt 'Outfit';letter-spacing:.28em;text-transform:uppercase">Verdi Imbole</div>
  <div style="display:flex;gap:2mm">{''.join(f'<span style="width:2.2mm;height:2.2mm;border-radius:50%;background:{c};display:inline-block"></span>' for c in ('#E3DEFF','#B7AEFF','#8FA7FF'))}</div>
</div>"""


def back(art):
    stats = [("22", "modules progressifs"), ("40", "fiches prompts prêtes à l'emploi"), ("10", "études de cas complètes"), ("22", "annexes et modèles")]
    cards = "".join(f'<div style="flex:1;background:rgba(255,255,255,.07);border:1px solid rgba(201,193,255,.35);border-radius:4mm;padding:3.5mm 3mm;text-align:center">'
                    f'<div class="grad" style="font:900 24pt/1 \'Outfit\'">{n}</div><div style="font:500 7.6pt/1.3 \'Inter\';color:#DCD7FF;margin-top:1.5mm">{t}</div></div>' for n, t in stats)
    return f"""
<div style="position:absolute;right:-62mm;top:-40mm;width:150mm;height:120mm;opacity:.22">{art}</div>
<div style="position:absolute;left:16mm;right:16mm;top:16mm">
  <span class="pill">Édition 2026</span>
  <div style="font:900 15pt 'Outfit';letter-spacing:.04em;margin-top:7mm;color:#E3DEFF">ASBL AUGMENTÉE</div>
  <div style="font:500 9.5pt 'Inter';color:#B9B2EE;margin-top:1mm">Comment implémenter l'IA dans vos processus</div>
  <div style="font:800 21pt/1.15 'Outfit';margin-top:13mm;max-width:132mm">L'intelligence artificielle au service de votre mission.</div>
  <div style="font:400 9.6pt/1.6 'Inter';color:#E8E5FB;margin-top:6mm;max-width:138mm">
    <p style="margin:0 0 3mm">Associations, ONG, fondations : vos équipes portent des missions essentielles avec des moyens comptés. L'intelligence artificielle peut leur rendre du temps, fiabiliser les processus et éclairer les décisions, à condition d'être comprise, maîtrisée et encadrée.</p>
    <p style="margin:0 0 3mm">Ce manuel vous guide pas à pas : comprendre l'IA sans jargon, diagnostiquer votre organisation, protéger les données et les personnes, puis implémenter des solutions concrètes dans chaque métier (gouvernance, projets, comptabilité, audit, ressources humaines, financements, achats, communication, terrain), à la mesure de vos moyens.</p>
    <p style="margin:0">Chaque solution précise ce que fait l'IA, ce que fait le logiciel, ce que fait le professionnel, et ce qui doit être vérifié.</p>
  </div>
  <div style="display:flex;gap:3mm;margin-top:8mm">{cards}</div>
  <div style="font:400 8.6pt/1.5 'Inter';color:#C9C3F2;margin-top:6mm"><b style="color:#fff;font-weight:600">Pour qui ?</b> Dirigeants, administrateurs, comptables, auditeurs, chefs de projet, responsables RH et financements, logisticiens, communicants, agents de terrain, bénévoles et consultants.</div>
</div>
<div style="position:absolute;left:16mm;right:16mm;bottom:14mm;background:rgba(255,255,255,.08);border:1px solid rgba(201,193,255,.4);border-radius:4mm;padding:4.5mm 5mm;display:flex;gap:4.5mm;align-items:center">
  <div style="width:12mm;height:12mm;border-radius:50%;background:linear-gradient(135deg,#9C8CFF,#6F8BFF);flex:none;display:flex;align-items:center;justify-content:center;font:800 12pt 'Outfit'">VI</div>
  <div><div style="font:700 11.5pt 'Outfit';letter-spacing:.06em">Verdi Imbole</div>
  <div style="font:400 8.4pt/1.45 'Inter';color:#DCD7FF">Auteur indépendant, auditeur financier et consultant freelance en intelligence artificielle.</div>
  <div style="font:600 8.4pt 'Inter';color:#B7AEFF;margin-top:.8mm">verdiimbole0@gmail.com</div></div>
</div>"""


def render(html_path, pdf, png, w_mm, h_mm):
    js = os.path.join(OUT, "_r.js")
    open(js, "w").write(f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch({{args:['--allow-file-access-from-files']}});
const p=await b.newPage({{viewport:{{width:{round(w_mm * 3.7795)},height:{round(h_mm * 3.7795)}}},deviceScaleFactor:3}});
await p.goto('file://{html_path}');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.pdf({{path:'{pdf}',width:'{w_mm}mm',height:'{h_mm}mm',printBackground:true,preferCSSPageSize:true}});
{"await p.screenshot({path:'" + png + "'});" if png else ""}await b.close();}})();""")
    env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
    subprocess.run(["node", js], env=env, check=True)
    os.remove(js)


def main():
    os.makedirs(OUT, exist_ok=True); os.makedirs(ART, exist_ok=True)
    art_f = network_svg(1000, 780, 500, 395, 0.95, True, 7)
    art_b = network_svg(1000, 780, 500, 395, 0.95, True, 11)
    open(os.path.join(ART, "couverture_art.svg"), "w").write(art_f)
    open(os.path.join(ART, "partie_art.svg"), "w").write(network_svg(1700, 1150, 850, 590, 1.05, False, 3))
    for name, body in (("couverture_avant", front(art_f)), ("couverture_arriere", back(art_b))):
        for bleed, suffix in ((0, ""), (3, "_impression_fond_perdu_3mm")):
            hp = os.path.join(OUT, f"_{name}{suffix}.html")
            open(hp, "w", encoding="utf-8").write(page(body, bleed))
            render(hp, os.path.join(OUT, f"{name}{suffix}.pdf"), os.path.join(OUT, f"{name}.png") if bleed == 0 else None, 170 + 2 * bleed, 240 + 2 * bleed)
            os.remove(hp)
    print("couvertures produites dans", OUT)


if __name__ == "__main__":
    main()
