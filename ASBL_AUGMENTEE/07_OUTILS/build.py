#!/usr/bin/env python3
"""Compile le manuscrit : MANUSCRIT_SOURCE.md, MANUSCRIT_FINAL.docx, MANUSCRIT_FINAL.pdf (via paged.js + Chromium).

Usage : python3 07_OUTILS/build.py   (depuis ASBL_AUGMENTEE)
"""
import os, re, glob, subprocess, zipfile, shutil, unicodedata, json
from collections import defaultdict, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MS = os.path.join(ROOT, "02_MANUSCRIT")
TOOLS = os.path.join(ROOT, "07_OUTILS")
BUILD = os.path.join(TOOLS, "build")
LIV = os.path.join(ROOT, "06_LIVRABLES")

ORDER = (["pages_liminaires.md"]
         + [os.path.relpath(p, MS) for p in sorted(glob.glob(os.path.join(MS, "partie_*", "module_*.md")),
                                               key=lambda p: int(re.search(r"module_(\d+)", p).group(1)))]
         + ["conclusion.md", "pages_finales.md"])

INDEX_TERMS = ["agent IA", "AI Act", "anonymisation", "API", "apprentissage automatique", "apprentissage profond",
               "arbre à problèmes", "assistant conversationnel", "audit interne", "bailleur", "base de connaissances",
               "bénévole", "biais", "budget", "cadre logique", "cahier des charges", "chaîne de résultats", "cloud",
               "consentement", "contrôle interne", "COSO", "cybersécurité", "donnée personnelle", "droit d'auteur",
               "éligibilité", "extraction", "faible connectivité", "faux positif", "feu tricolore", "fonds affectés",
               "fractionnement", "gouvernance", "hallucination", "immobilisation", "imputation", "indicateur",
               "injection de prompt", "inventaire", "ISO/IEC 42001", "jeu de tests", "matrice de sélection", "CADRE",
               "minimisation", "NIST", "no-code", "OCR", "OCDE", "pilote", "piste d'audit", "plainte",
               "plan de classement", "procès-verbal", "prompt", "pseudonymisation", "RACI", "RAG",
               "rapprochement bancaire", "rapprochement à trois voies", "recrutement", "registre des décisions",
               "réversibilité", "RGPD", "RPA", "sauvegarde", "séparation des tâches", "supervision humaine",
               "tableau de bord", "traduction", "transparence", "trésorerie", "UNESCO", "WCAG"]


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def clean_title(t):
    t = re.sub(r"\{[^}]*\}", "", t).strip()
    return re.sub(r"^\d+(\.\d+)*\s+", "", t)


def preprocess():
    figs, tables, toc, index_text = [], [], [], defaultdict(str)
    out_parts = []
    h1n = 0
    for rel in ORDER:
        txt = open(os.path.join(MS, rel), encoding="utf-8").read()
        mod = None
        m = re.search(r"^# Module (\d+)", txt, re.M)
        if m:
            mod = int(m.group(1))
        key = f"M{mod}" if mod else ("Glossaire" if "liminaires" in rel else None)
        if key:
            index_text[key] += "\n" + txt
        lines = txt.split("\n")
        res, section, tcount, i = [], "", 0, 0
        while i < len(lines):
            ln = lines[i]
            # Titres de niveau 1 : identifiants et table des matières
            if ln.startswith("# "):
                h1n += 1
                hid = f"h{h1n}"
                title = clean_title(ln[2:])
                attrs = re.search(r"\{([^}]*)\}\s*$", ln)
                if attrs:
                    ln = ln[:attrs.start()] + "{#" + hid + " " + attrs.group(1) + "}"
                else:
                    ln = ln + " {#" + hid + "}"
                unlisted = attrs and "unlisted" in attrs.group(1)
                if not unlisted:
                    toc.append((hid, title, bool(attrs and "partie" in attrs.group(1))))
            if ln.startswith("## "):
                section = clean_title(ln[3:])
            # Figures
            fm = re.match(r"^!\[(Figure ([\d.]+)[^\]]*)\]\(([^)]+)\)\s*$", ln)
            if fm:
                cap, num, path = fm.group(1), fm.group(2), fm.group(3)
                fid = "fig-" + num.replace(".", "-")
                figs.append((num, cap, fid, mod))
                ln = f"![{cap}]({path}){{#{fid}}}"
            # Tableaux : légende automatique
            if ln.startswith("|") and (i == 0 or lines[i - 1].strip() == "") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|\s*$", lines[i + 1]):
                j = i
                while j < len(lines) and lines[j].startswith("|"):
                    res.append(lines[j]); j += 1
                tcount += 1
                num = f"{mod if mod is not None else 0}.{tcount}"
                cap = f"Tableau {num} : {section or 'Pages liminaires'}"
                tables.append((num, cap, mod))
                res.append(""); res.append(f"Table: {cap}")
                i = j
                continue
            res.append(ln)
            i += 1
        out_parts.append((rel, "\n".join(res)))
    return out_parts, figs, tables, toc, index_text


def generated_lists(figs, tables, index_text):
    md = "# Index alphabétique {#index-alpha .unnumbered}\n\n*Les renvois indiquent les modules (M) où la notion est principalement traitée ; « Glossaire » renvoie aux pages liminaires.*\n\n::: index\n"
    keys = list(index_text.keys())
    for term in sorted(INDEX_TERMS, key=lambda t: unicodedata.normalize("NFKD", t.lower()).encode("ascii", "ignore")):
        pat = re.compile(r"(?<![\w-])" + re.escape(term) + r"s?(?![\w-])", re.I if term.lower() == term else 0)
        counts = {k: len(pat.findall(index_text[k])) for k in keys}
        total = sum(counts.values())
        refs = [k for k in keys if counts[k] >= (1 if total < 6 else 2)]
        if refs:
            md += f"**{term}** : {', '.join(refs)}\n\n"
    md += ":::\n\n# Liste des illustrations {#liste-illustrations .unnumbered}\n\n::: listeillus\n"
    for num, cap, fid, mod in figs:
        md += f"- [{cap}](#{fid})\n"
    md += ":::\n\n# Liste des tableaux {#liste-tableaux .unnumbered}\n\n*Les tableaux sont numérotés par module ; le numéro 0 désigne les pages liminaires.*\n\n"
    for num, cap, mod in tables:
        md += f"- {cap}\n"
    return md + "\n"


def assemble(parts, lists, target):
    out = []
    for rel, txt in parts:
        if rel == "pages_finales.md":
            k = txt.index("# Annexes et modèles téléchargeables")
            txt = txt[:k] + lists + txt[k:]
        if target == "docx":
            txt = re.sub(r"03_ILLUSTRATIONS/figures/(fig_[\d_]+)\.svg", r"03_ILLUSTRATIONS/png/\1.png", txt)
        elif target == "html":
            txt = txt.replace("03_ILLUSTRATIONS/figures/", "../../03_ILLUSTRATIONS/figures/")
            txt = re.sub(r"^# ((?:Module \d+)|(?:Partie [IVX]+)) : (.*?)( \{[^}]*\})$", r"# [\1]{.pill} \2\3", txt, flags=re.M)
        out.append(txt)
    if target == "docx":
        cov = "06_LIVRABLES/COUVERTURE/"
        out.insert(0, f"![]({cov}couverture_avant.png){{width=100%}}\n\n::: saut\n:::\n")
        out.append(f"\n::: saut\n:::\n\n![]({cov}couverture_arriere.png){{width=100%}}\n")
    return "\n\n".join(out)


def toc_html(toc):
    h = '<nav class="tdm"><h1 id="tdm-titre" class="unnumbered">Table des matières</h1><ol>'
    for hid, title, partie in toc:
        cls = ' class="partie"' if partie else ""
        h += f'<li{cls}><a href="#{hid}">{title}</a></li>'
    return h + "</ol></nav>"


def build_docx(md):
    src = os.path.join(BUILD, "livre_docx.md")
    open(src, "w", encoding="utf-8").write(md)
    out = os.path.join(LIV, "MANUSCRIT_FINAL.docx")
    subprocess.run(["pandoc", src, "-f", "markdown+pipe_tables+fenced_divs+bracketed_spans", "-o", out,
                    "--reference-doc", os.path.join(TOOLS, "reference.docx"), "--lua-filter", os.path.join(TOOLS, "livre.lua"),
                    "--resource-path", ROOT, "--metadata", "lang=fr-FR", "--metadata", "title=ASBL augmentée"], check=True, cwd=ROOT)
    # Demander à Word de mettre à jour la table des matières à l'ouverture
    tmp = out + ".tmp"
    with zipfile.ZipFile(out) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/settings.xml":
                s = data.decode("utf-8")
                if "updateFields" not in s:
                    s = s.replace("</w:settings>", '<w:updateFields w:val="true"/></w:settings>')
                data = s.encode("utf-8")
            if item.filename == "word/document.xml":
                # Supprime le bloc de titre généré par pandoc (le titre figure déjà dans les pages liminaires)
                s = data.decode("utf-8")
                s = re.sub(r'<w:p><w:pPr><w:pStyle w:val="Title" /></w:pPr>.*?</w:p>', "", s, count=1, flags=re.S)
                data = s.encode("utf-8")
            zout.writestr(item, data)
    os.replace(tmp, out)
    return out


def build_html(md, toc):
    md = md.replace("::: tdm\n:::", "```{=html}\n" + toc_html(toc) + "\n```")
    src = os.path.join(BUILD, "livre_html.md")
    open(src, "w", encoding="utf-8").write(md)
    head = os.path.join(BUILD, "head.html")
    open(head, "w", encoding="utf-8").write(
        '<script>window.PagedConfig={auto:true,after:function(){window.__paged_done=true;}};</script>\n'
        '<script src="../vendor/paged.polyfill.min.js"></script>\n')
    out = os.path.join(BUILD, "livre.html")
    subprocess.run(["pandoc", src, "-f", "markdown+pipe_tables+fenced_divs+bracketed_spans", "-t", "html5", "-s", "-o", out,
                    "--css", "../livre.css", "--include-in-header", head, "--lua-filter", os.path.join(TOOLS, "livre.lua"),
                    "--metadata", "pagetitle=ASBL augmentée", "--metadata", "lang=fr-FR"], check=True, cwd=BUILD)
    return out


def build_pdf(html):
    js = os.path.join(BUILD, "print.js")
    pdf = os.path.join(LIV, "MANUSCRIT_FINAL.pdf")
    open(js, "w").write(f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch({{args:['--allow-file-access-from-files']}});
  const p = await b.newPage();
  p.setDefaultTimeout(600000);
  await p.goto('file://{html}', {{waitUntil: 'load'}});
  await p.waitForFunction(() => window.__paged_done === true, null, {{timeout: 600000, polling: 1000}});
  const n = await p.evaluate(() => document.querySelectorAll('.pagedjs_page').length);
  console.log('pages', n);
  await p.pdf({{path: '{pdf}', preferCSSPageSize: true, printBackground: true}});
  await b.close();
}})();
""")
    env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
    r = subprocess.run(["node", js], env=env, capture_output=True, text=True)
    print(r.stdout, r.stderr[-2000:])
    return pdf


def main():
    os.makedirs(BUILD, exist_ok=True); os.makedirs(LIV, exist_ok=True)
    parts, figs, tables, toc, index_text = preprocess()
    lists = generated_lists(figs, tables, index_text)
    src_md = assemble(parts, lists, "source")
    open(os.path.join(LIV, "MANUSCRIT_SOURCE.md"), "w", encoding="utf-8").write(
        "<!-- Manuscrit assemblé automatiquement par 07_OUTILS/build.py. Chemins d'images relatifs au dossier ASBL_AUGMENTEE. -->\n\n" + src_md)
    json.dump({"figures": len(figs), "tableaux": len(tables), "titres_niveau_1": len(toc),
               "mots": len(re.findall(r"\w+", src_md))}, open(os.path.join(BUILD, "stats.json"), "w"), indent=1)
    print(f"{len(figs)} figures, {len(tables)} tableaux, {len(toc)} titres de niveau 1")
    build_docx(assemble(parts, lists, "docx"))
    html = build_html(assemble(parts, lists, "html"), toc)
    if os.environ.get("NO_PDF") != "1":
        build_pdf(html)
        ajouter_couvertures()


def ajouter_couvertures():
    from pypdf import PdfReader, PdfWriter
    pdf = os.path.join(LIV, "MANUSCRIT_FINAL.pdf")
    cov = os.path.join(LIV, "COUVERTURE")
    w = PdfWriter()
    for f in (os.path.join(cov, "couverture_avant.pdf"), pdf, os.path.join(cov, "couverture_arriere.pdf")):
        for pg in PdfReader(f).pages:
            w.add_page(pg)
    tmp = pdf + ".tmp"
    with open(tmp, "wb") as fh:
        w.write(fh)
    os.replace(tmp, pdf)


if __name__ == "__main__":
    main()
