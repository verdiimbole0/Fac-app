#!/usr/bin/env python3
"""Assemble le manuscrit (Markdown) en HTML puis en PDF (WeasyPrint).
Usage : python3 build.py            -> 06_MISE_EN_PAGE/build/livre.html + livre_interieur.pdf
"""
import re, subprocess, html, pathlib, yaml, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MS = ROOT / "02_MANUSCRIT"
OUT = ROOT / "06_MISE_EN_PAGE" / "build"
OUT.mkdir(exist_ok=True)

PRELIM = ["00_mentions.md", "00_auteur.md", "00_preface.md", "00_avant_propos.md", "00_utiliser.md", "00_parcours.md"]
CHAPS = [f"ch{n:02d}.md" for n in range(1, 11)]
BACK = ["conclusion.md", "annexes.md", "glossaire.md", "bibliographie.md"]

ICONS = {  # pictogrammes au trait (or) pour les ouvertures de chapitre
 1: '<rect x="20" y="60" width="160" height="110" rx="4"/><path d="M20 90h160M70 60v-25h60v25M85 120h30"/><rect x="80" y="110" width="40" height="22" rx="3"/>',
 2: '<circle cx="100" cy="100" r="70"/><path d="M100 30l14 -12M100 30l14 12M170 100l12 14M170 100l-12 14M100 170l-14 12M100 170l-14 -12M30 100l-12 -14M30 100l12 -14"/><circle cx="100" cy="100" r="22"/>',
 3: '<path d="M25 55h55l12 14h85v100H25z"/><path d="M25 85h152M45 110h60M45 130h90M45 150h40"/>',
 4: '<circle cx="85" cy="85" r="52"/><path d="M123 123l52 52"/><path d="M60 75h50M60 95h35"/>',
 5: '<path d="M100 20l70 28v50c0 45-30 72-70 85-40-13-70-40-70-85V48z"/><path d="M100 70c-14 20-22 32-22 44a22 22 0 0044 0c0-12-8-24-22-44z"/>',
 6: '<path d="M55 25h90M55 175h90M65 25c0 45 70 50 70 75s-70 30-70 75M135 25c0 45-70 50-70 75s70 30 70 75"/><path d="M85 160h30"/>',
 7: '<path d="M55 140a35 35 0 010-70 50 50 0 0195-10 32 32 0 015 80z"/><path d="M100 95v60M80 135l20 20 20-20"/>',
 8: '<rect x="45" y="90" width="110" height="85" rx="6"/><path d="M70 90V65a30 30 0 0160 0v25"/><circle cx="100" cy="125" r="10"/><path d="M100 135v20"/>',
 9: '<rect x="55" y="55" width="90" height="90" rx="8"/><rect x="80" y="80" width="40" height="40"/><path d="M75 55V30M100 55V30M125 55V30M75 170v-25M100 170v-25M125 170v-25M55 75H30M55 100H30M55 125H30M170 75h-25M170 100h-25M170 125h-25"/>',
 10: '<path d="M30 175V80l70-45 70 45v95z"/><path d="M60 175v-55h30v55M115 105h30v25h-30zM30 175h140"/>',
}

def opener_bg(n):
    """Fond graphique de l'ouverture : rayonnages stylisés + pictogramme."""
    shelves = []
    for i in range(7):
        y = 40 + i * 38
        shelves.append(f'<line x1="140" y1="{y}" x2="210" y2="{y}" stroke="#1B3A6B" stroke-width="0.6"/>')
        x = 142
        k = 0
        while x < 208:
            w = 5 + ((i * 7 + k * 3) % 5)
            h = 18 + ((i * 5 + k * 11) % 14)
            col = "#C7A34F" if (i + k) % 9 == 0 else "#173563"
            shelves.append(f'<rect x="{x}" y="{y-h}" width="{w}" height="{h}" fill="{col}" opacity="{0.9 if col=="#C7A34F" else 0.85}"/>')
            x += w + 1.2
            k += 1
    icon = ICONS[n]
    return f'''<svg class="op-bg" viewBox="0 0 210 297" xmlns="http://www.w3.org/2000/svg">
<rect width="210" height="297" fill="#0A1E3F"/>
<rect x="0" y="0" width="6" height="297" fill="#C7A34F"/>
{''.join(shelves)}
<rect x="130" y="0" width="80" height="297" fill="url(#fade)"/>
<defs><linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="#0A1E3F" stop-opacity="1"/><stop offset="0.6" stop-color="#0A1E3F" stop-opacity="0.15"/><stop offset="1" stop-color="#0A1E3F" stop-opacity="0"/></linearGradient></defs>
<path d="M0 206 L210 190 L210 297 L0 297 Z" fill="#102A52"/><path d="M0 206 L210 190" stroke="#C7A34F" stroke-width="0.8"/>
<g transform="translate(152 222) scale(0.25)" fill="none" stroke="#C7A34F" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
</svg>'''

import json as _json
STAT_ICONS = _json.load(open(pathlib.Path(__file__).resolve().parent / "stat_icons.json"))

def stats_html(body):
    """Rangée de chiffres clés du chapitre (calculés sur le manuscrit)."""
    nsec = len(re.findall(r"^## ", body, flags=re.M))
    nfig = len(re.findall(r"^!\[", body, flags=re.M))
    ntab = len(re.findall(r"^\|[-|: ]+\|\s*$", body, flags=re.M))
    nq = len(re.findall(r"^\*\*\d+\.\*\* ", body, flags=re.M))
    items = [("sec", nsec, "sections"), ("fig", nfig, "schémas"), ("tab", ntab, "tableaux"), ("qcm", nq, "questions QCM")]
    cells = "".join(f'<div class="st"><img src="{STAT_ICONS[k]}"><div class="n">{n}</div><div class="l">{l}</div></div>' for k, n, l in items)
    return f'<div class="op-stats">{cells}</div>'

def split_front(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if m:
        return yaml.safe_load(m.group(1)), m.group(2)
    return {}, text

def md2html(md, numprefix=None):
    """Convertit en HTML ; numérote les titres de niveau 2 (1.1, 1.2...)."""
    if numprefix is not None:
        k = [0]
        def num(m):
            k[0] += 1
            return f"## [{numprefix}.{k[0]}]{{.secnum}} {m.group(1)}"
        md = re.sub(r"^## (.+)$", num, md, flags=re.M)
    md = md.replace("../03_ILLUSTRATIONS/", str(ROOT / "03_ILLUSTRATIONS") + "/")
    r = subprocess.run(["pandoc", "-f", "markdown+fenced_divs+pipe_tables+table_captions+implicit_figures+bracketed_spans",
                        "-t", "html5", "--wrap=none"], input=md, capture_output=True, text=True, check=True)
    h = r.stdout
    # encadrés placés juste après un titre de même nature : on supprime l'étiquette redondante
    h = re.sub(r'(</h2>\s*<div class=")(retenir|attention|qcm)(")', r'\1\2 nolabel\3', h)
    h = re.sub(r'<colgroup>.*?</colgroup>', '', h, flags=re.S)
    return h

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def build():
    parts, toc = [], []
    # ---------- page de titre ----------
    parts.append((ROOT / "06_MISE_EN_PAGE" / "titlepage.html").read_text())
    # ---------- préliminaires ----------
    for f in PRELIM:
        fm, body = split_front((MS / f).read_text())
        parts.append(f'<section class="prelim" id="{f[:-3]}">{md2html(body)}</section>')
    parts.append('<section class="prelim" id="sommaire"><h1>Sommaire</h1><div class="toc">@@TOC@@</div></section>')
    # ---------- chapitres ----------
    for n, f in enumerate(CHAPS, 1):
        fm, body = split_front((MS / f).read_text())
        title = fm["titre"]
        short = fm.get("court", title)
        pts = "".join(f'<div class="pt"><span class="sq">{i}</span>{html.escape(p)}</div>' for i, p in enumerate(fm["points"], 1))
        cid = f"ch{n}"
        parts.append(f'''<section class="opener" id="{cid}">{opener_bg(n)}
<div class="op-label">CHAPITRE</div><div class="op-num">{n:02d}</div>
<h1 data-short="Chapitre {n} · {html.escape(short)}">{html.escape(title)}</h1><div class="op-rule"></div>
<div class="op-vline"></div><p class="op-accroche">{html.escape(fm["accroche"])}</p>
{stats_html(body)}
<div class="op-points"><div class="t">DANS CE CHAPITRE</div>{pts}</div>
<div class="op-foot">L'ARCHIVISTIQUE · PRINCIPES ET PRATIQUES DU MÉTIER D'ARCHIVISTE</div></section>''')
        h = md2html(body, numprefix=n)
        secs = []
        def addid(m):
            i = f"{cid}-s{len(secs)+1}"
            txt = re.sub(r"<[^>]+>", "", m.group(2))
            secs.append((i, txt))
            return f'<h2 id="{i}"{m.group(1)}>{m.group(2)}</h2>'
        h = re.sub(r'<h2(?: id="[^"]*")?([^>]*)>(.*?)</h2>', addid, h)
        parts.append(f'<section class="chapter-body">{h}</section>')
        sub = "".join(f'<div class="s"><a href="#{i}">{html.escape(t)}</a></div>' for i, t in secs
                      if not re.search(r"QCM|retenir|Erreurs fréquentes", t))
        toc.append(f'<div class="tc"><div class="c"><a href="#{cid}">{n}. {html.escape(title)}</a></div>{sub}</div>')
    # ---------- fin d'ouvrage ----------
    for f in BACK:
        fm, body = split_front((MS / f).read_text())
        cls = fm.get("classe", "")
        bid = f[:-3]
        h = md2html(body)
        parts.append(f'<section class="backmatter {cls}" id="{bid}"><h1>{html.escape(fm["titre"])}</h1>{h}</section>')
        sub = ""
        if bid == "annexes":
            ids = re.findall(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', h)
            sub = "".join(f'<div class="s"><a href="#{i}">{re.sub("<[^>]+>","",t)}</a></div>' for i, t in ids)
        toc.append(f'<div class="tc"><div class="c"><a href="#{bid}">{html.escape(fm["titre"])}</a></div>{sub}</div>')
    doc = "\n".join(parts).replace("@@TOC@@", "\n".join(toc))
    page = f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>L'archivistique : principes et pratiques du métier d'archiviste</title>
<meta name="author" content="Verdi Imbole"><link rel="stylesheet" href="livre.css"></head>
<body>{doc}</body></html>'''
    (ROOT / "06_MISE_EN_PAGE" / "livre.html").write_text(page)
    return page

if __name__ == "__main__":
    build()
    from weasyprint import HTML
    d = HTML(filename=str(ROOT / "06_MISE_EN_PAGE" / "livre.html")).render()
    print("pages:", len(d.pages))
    d.write_pdf(str(OUT / "livre_interieur.pdf"))
