# -*- coding: utf-8 -*-
"""Moteur PDF : HTML/CSS -> PDF via Chromium (Playwright), avec sommaire paginé en deux passes."""
import os, re, json, subprocess, html as H
from pypdf import PdfReader, PdfWriter
from content import NAVY, GOLD, TEAL, LIGHT, INK, MUTED, RED, ORANGE, NAVY2

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build"); os.makedirs(BUILD, exist_ok=True)
FONTS = os.path.join(HERE, "assets", "fonts")
ICONS = os.path.join(HERE, "assets", "icons")

def esc(t): return H.escape(t, quote=False)

def icon(name, color=TEAL, size=18, stroke=2):
    svg = open(os.path.join(ICONS, name + ".svg"), encoding="utf-8").read()
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    svg = svg.replace('stroke="currentColor"', f'stroke="#{color}"').replace('stroke-width="2"', f'stroke-width="{stroke}"')
    svg = re.sub(r'width="24"\s+height="24"', f'width="{size}" height="{size}"', svg)
    return f'<span class="ic">{svg}</span>'

def badge(name, bg=TEAL, color="FFFFFF", d=34, isz=None):
    isz = isz or int(d * 0.55)
    return f'<span class="badge" style="width:{d}px;height:{d}px;background:#{bg}">{icon(name, color, isz)}</span>'

def ff(name, file, weight, style="normal"):
    return f"@font-face{{font-family:'{name}';src:url('file://{FONTS}/{file}');font-weight:{weight};font-style:{style};}}"

CSS = "".join([ff("Montserrat", "Montserrat-Regular.ttf", 400), ff("Montserrat", "Montserrat-Medium.ttf", 500),
               ff("Montserrat", "Montserrat-SemiBold.ttf", 600), ff("Montserrat", "Montserrat-Bold.ttf", 700),
               ff("Montserrat", "Montserrat-ExtraBold.ttf", 800), ff("Inter", "Inter-Regular.otf", 400),
               ff("Inter", "Inter-Medium.otf", 500), ff("Inter", "Inter-SemiBold.otf", 600), ff("Inter", "Inter-Bold.otf", 700),
               ff("Inter", "Inter-Italic.otf", 400, "italic")]) + f"""
:root{{--navy:#{NAVY};--navy2:#{NAVY2};--gold:#{GOLD};--teal:#{TEAL};--light:#{LIGHT};--ink:#{INK};--muted:#{MUTED};--red:#{RED};--orange:#{ORANGE};}}
@page{{size:A4;margin:18mm 17mm 19mm 17mm;}}
@page full{{margin:0;}}
*{{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
html,body{{margin:0;padding:0;background:#fff;}}
body{{font-family:Inter,sans-serif;font-size:9.6pt;line-height:1.55;color:var(--ink);}}
p{{margin:0 0 7pt 0;}}
h1,h2,h3,h4{{font-family:Montserrat,sans-serif;color:var(--navy);margin:0;line-height:1.2;}}
h2{{font-size:16.5pt;font-weight:700;margin:16pt 0 9pt 0;padding-left:11pt;border-left:4pt solid var(--gold);break-after:avoid;}}
h2.first{{margin-top:0;}}
h3{{font-size:12pt;font-weight:700;margin:13pt 0 6pt 0;color:var(--navy);break-after:avoid;}}
h3 .num{{color:var(--teal);margin-right:5pt;}}
h4{{font-size:10pt;font-weight:700;margin:9pt 0 4pt 0;break-after:avoid;}}
.kicker{{font-family:Montserrat;font-weight:700;font-size:8pt;letter-spacing:1.2pt;text-transform:uppercase;color:var(--gold);}}
ul,ol{{margin:3pt 0 8pt 0;padding-left:15pt;}} li{{margin:2pt 0;}}
strong{{color:var(--navy);font-weight:600;}}
.page-break{{break-before:page;}}
.avoid{{break-inside:avoid;}}
.ic{{display:inline-flex;vertical-align:middle;}} .ic svg{{display:block;}}
.badge{{display:inline-flex;align-items:center;justify-content:center;border-radius:50%;flex:none;}}
.full{{page:full;width:210mm;height:296.6mm;position:relative;overflow:hidden;break-after:page;}}
.navy{{background:var(--navy);color:#fff;}}
.lead{{font-size:11pt;color:var(--muted);line-height:1.6;}}
/* encadrés */
.box{{border-radius:6pt;padding:9pt 12pt 8pt 12pt;margin:9pt 0;break-inside:avoid;position:relative;}}
.box .bt{{font-family:Montserrat;font-weight:700;font-size:8.2pt;letter-spacing:.8pt;text-transform:uppercase;margin-bottom:4pt;display:flex;align-items:center;gap:6pt;}}
.box p:last-child,.box ul:last-child{{margin-bottom:0;}}
.key{{background:#E6F4F2;border-left:4pt solid var(--teal);}} .key .bt{{color:var(--teal);}}
.warn{{background:#FBEDEB;border-left:4pt solid var(--red);}} .warn .bt{{color:var(--red);}}
.tip{{background:#FBF5E6;border-left:4pt solid var(--gold);}} .tip .bt{{color:#9C7C2C;}}
.ex{{background:var(--light);border-left:4pt solid var(--navy);}} .ex .bt{{color:var(--navy);}}
.ask{{background:#fff;border:1.2pt dashed var(--teal);}} .ask .bt{{color:var(--teal);}}
.prompt{{background:#0E2449;color:#fff;border-radius:6pt;padding:9pt 12pt;margin:7pt 0 9pt 0;font-size:8.9pt;line-height:1.5;white-space:pre-wrap;break-inside:avoid;font-family:Inter;}}
.prompt .pl{{display:block;font-family:Montserrat;font-weight:700;font-size:7.5pt;letter-spacing:1pt;color:var(--gold);margin-bottom:4pt;text-transform:uppercase;}}
.answer{{background:var(--light);border-radius:6pt;padding:9pt 12pt;margin:6pt 0 9pt 0;font-size:8.9pt;white-space:pre-wrap;break-inside:avoid;border:1pt solid #DDE3EC;}}
.answer .pl{{display:block;font-family:Montserrat;font-weight:700;font-size:7.5pt;letter-spacing:1pt;color:var(--teal);margin-bottom:4pt;text-transform:uppercase;}}
/* tables */
table.tbl{{width:100%;border-collapse:collapse;margin:7pt 0 10pt 0;font-size:8.8pt;break-inside:auto;}}
table.tbl th{{background:var(--navy);color:#fff;font-family:Montserrat;font-weight:700;font-size:8pt;text-align:left;padding:6pt 7pt;}}
table.tbl td{{padding:5.5pt 7pt;border-bottom:1pt solid #E3E7EE;vertical-align:top;}}
table.tbl tr:nth-child(even) td{{background:#F7F9FB;}}
table.tbl tr{{break-inside:avoid;}}
/* cartes */
.grid{{display:grid;gap:8pt;margin:8pt 0 10pt 0;}} .g2{{grid-template-columns:1fr 1fr;}} .g3{{grid-template-columns:1fr 1fr 1fr;}} .g4{{grid-template-columns:repeat(4,1fr);}}
.card{{background:var(--light);border-radius:7pt;padding:10pt 11pt;break-inside:avoid;}}
.card h4{{margin-top:5pt;}}
.card p{{font-size:8.8pt;margin:0;}}
.chip{{display:inline-block;font-family:Montserrat;font-weight:700;font-size:7pt;letter-spacing:.6pt;padding:2.5pt 7pt;border-radius:10pt;text-transform:uppercase;}}
/* quiz */
.quiz-q{{background:#fff;border:1pt solid #DCE2EB;border-radius:7pt;padding:10pt 12pt;margin:8pt 0;break-inside:avoid;}}
.quiz-q .qt{{font-family:Montserrat;font-weight:700;color:var(--navy);font-size:10.5pt;margin-bottom:6pt;display:flex;gap:8pt;align-items:flex-start;}}
.qn{{background:var(--navy);color:#fff;border-radius:50%;width:22pt;height:22pt;flex:none;display:inline-flex;align-items:center;justify-content:center;font-size:8.5pt;}}
.opt{{display:flex;gap:8pt;align-items:center;margin:4pt 0 4pt 30pt;}}
.ol{{width:16pt;height:16pt;border-radius:50%;border:1.2pt solid var(--navy);display:inline-flex;align-items:center;justify-content:center;font-family:Montserrat;font-weight:700;font-size:7.5pt;color:var(--navy);flex:none;}}
.corr{{border-left:4pt solid var(--teal);background:#F3FAF9;border-radius:6pt;padding:9pt 12pt;margin:8pt 0;break-inside:avoid;}}
.corr .good{{font-family:Montserrat;font-weight:700;color:var(--teal);font-size:10pt;margin-bottom:3pt;}}
/* sommaire */
.toc a{{color:inherit;text-decoration:none;}}
.toc .l1{{display:flex;align-items:baseline;font-family:Montserrat;font-weight:700;color:var(--navy);font-size:10.5pt;margin:9pt 0 2pt 0;}}
.toc .l2{{display:flex;align-items:baseline;font-size:9.3pt;margin:2.5pt 0 2.5pt 14pt;color:var(--ink);}}
.toc .dots{{flex:1;border-bottom:1pt dotted #B9C2D0;margin:0 6pt;transform:translateY(-3pt);}}
.toc .pg{{font-family:Montserrat;font-weight:700;color:var(--teal);min-width:16pt;text-align:right;}}
.mk{{display:inline-block;width:0;font-size:2px;line-height:0;color:rgba(255,255,255,0.01);white-space:nowrap;vertical-align:top;}}
.write{{border-bottom:1pt solid #C9D1DE;height:20pt;}}
.small{{font-size:8.2pt;color:var(--muted);}}
"""

class Doc:
    """Collecte le HTML d'un document + les entrées du sommaire."""
    def __init__(self, label):
        self.label = label; self.parts = []; self.toc = []; self.n = 0
    def add(self, h): self.parts.append(h)
    def mark(self, title, level=1):
        self.n += 1; mid = f"zzmk{self.n:03d}zz"
        self.toc.append((mid, title, level))
        return f'<span class="mk">{mid}</span>'
    def toc_html(self, pages=None):
        out = ['<div class="toc">']
        for mid, t, lv in self.toc:
            p = pages.get(mid, "") if pages else "00"
            out.append(f'<div class="l{lv}"><span>{esc(t)}</span><span class="dots"></span><span class="pg">{p}</span></div>')
        out.append("</div>")
        return "".join(out)

def wrap(body):
    return f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'

RENDER_JS = os.path.join(BUILD, "render.js")
open(RENDER_JS, "w").write(r"""
const { chromium } = require('playwright');
(async () => {
  const [,, htmlPath, pdfPath, footer] = process.argv;
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + htmlPath, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const opts = { path: pdfPath, format: 'A4', printBackground: true, preferCSSPageSize: true };
  if (footer && footer !== '-') {
    opts.displayHeaderFooter = true;
    opts.headerTemplate = '<span></span>';
    opts.footerTemplate = `<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:7px;color:#8A96AB;padding:0 17mm;display:flex;justify-content:space-between;-webkit-print-color-adjust:exact;"><span style="letter-spacing:1px;font-weight:bold;">${footer}</span><span style="font-weight:bold;color:#0A1E3F;">— <span class="pageNumber"></span> —</span></div>`;
  }
  await p.pdf(opts); await b.close();
})();
""")

def render(html, pdf, footer="-"):
    hp = pdf.replace(".pdf", ".html")
    open(hp, "w", encoding="utf-8").write(html)
    subprocess.run(["node", RENDER_JS, hp, pdf, footer], check=True, cwd="/tmp")

def build(doc, cover_html, body_fn, out_pdf, footer):
    """body_fn(toc_html) -> html du corps. Deux passes pour paginer le sommaire."""
    base = os.path.join(BUILD, os.path.basename(out_pdf).replace(".pdf", ""))
    render(wrap(cover_html), base + "_cover.pdf")
    render(wrap(body_fn(doc.toc_html())), base + "_body.pdf", footer)
    pages = {}
    for i, pg in enumerate(PdfReader(base + "_body.pdf").pages):
        txt = pg.extract_text() or ""
        for mid, _, _ in doc.toc:
            if mid in txt and mid not in pages: pages[mid] = i + 1
    render(wrap(body_fn(doc.toc_html(pages))), base + "_body.pdf", footer)
    w = PdfWriter()
    for f in (base + "_cover.pdf", base + "_body.pdf"):
        for pg in PdfReader(f).pages: w.add_page(pg)
    w.add_metadata({"/Title": doc.label, "/Author": "Formation IA & Prompt Engineering"})
    with open(out_pdf, "wb") as fh: w.write(fh)
    missing = [t for mid, t, _ in doc.toc if mid not in pages]
    print(os.path.basename(out_pdf), "pages:", len(PdfReader(out_pdf).pages), "missing toc:", missing)
