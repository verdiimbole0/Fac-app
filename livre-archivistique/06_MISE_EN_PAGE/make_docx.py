#!/usr/bin/env python3
"""Produit le DOCX modifiable à partir du même manuscrit Markdown que le PDF."""
import re, subprocess, pathlib, copy
from docx import Document
from docx.shared import Pt, RGBColor, Mm, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import build

ROOT = build.ROOT
MS, OUTD = build.MS, ROOT / "06_MISE_EN_PAGE" / "build"
NAVY, GOLD, GRAY = "33373D", "2D5A3B", "F2F3F4"
LABELS = {"situation": ("SITUATION", "F2F3F4", "2D5A3B"), "objectifs": ("OBJECTIFS PÉDAGOGIQUES", "FFFFFF", "33373D"),
          "definition": ("DÉFINITIONS", "FFFFFF", "2D5A3B"), "exemple": ("EXEMPLE PROFESSIONNEL", "F2F3F4", "4A4F57"),
          "horizon": ("FIL ROUGE · ORGANISATION HORIZON (cas fictif)", "E6EFE8", "2D5A3B"), "attention": ("ATTENTION", "FFFFFF", "7B1E30"),
          "retenir": ("À RETENIR", "33373D", "2D5A3B"), "cas": ("CAS PRATIQUE", "FFFFFF", "33373D"), "corrige": ("CORRIGÉ", "F2F3F4", "4A4F57"),
          "qcm": ("QUESTIONNAIRE À CHOIX MULTIPLES", "FFFFFF", "33373D"), "prompt": ("PROMPT PRÊT À L'EMPLOI", "F7F7F8", "4A4F57"),
          "modele": ("MODÈLE RÉUTILISABLE", "FFFFFF", "2D5A3B"), "note": ("NOTE", "F2F3F4", "5E6166"), "glosscols": None}

LUA = r'''
local labels = {situation=1,objectifs=1,definition=1,exemple=1,horizon=1,attention=1,retenir=1,cas=1,corrige=1,qcm=1,prompt=1,modele=1,note=1}
function Div(el)
  local c = el.classes[1]
  if c == "glosscols" then return el.content end
  if c and labels[c] then
    local marker = pandoc.Para({pandoc.Str("@@BOX:" .. c .. "@@")})
    local blocks = {marker}
    for _, b in ipairs(el.content) do table.insert(blocks, b) end
    local cell = pandoc.Cell(blocks)
    local row = pandoc.Row({cell})
    local tbl = pandoc.Table({long = {}, short = {}}, {{pandoc.AlignDefault, 1.0}}, pandoc.TableHead({}), {{attr = {}, body = {row}, head = {}, row_head_columns = 0}}, pandoc.TableFoot({}))
    return tbl
  end
end
'''

def assemble_md():
    parts = []
    tp = ("::: {custom-style=\"Kicker\"}\nMANUEL PROFESSIONNEL\n:::\n\n# L'archivistique {.unnumbered .unlisted .titlepage}\n\n"
          "::: {custom-style=\"Subtitle\"}\nPrincipes et pratiques du métier d'archiviste\n:::\n\n"
          "*De la gestion des documents à la maîtrise des archives : les méthodes professionnelles pour organiser, protéger, retrouver et valoriser l'information de toute organisation.*\n\n"
          "**VERDI IMBOLE**\\\nAuteur indépendant · Auditeur financier · Freelance\n\nPublication indépendante · 2026\n")
    parts.append(tp)
    for f in build.PRELIM:
        fm, body = build.split_front((MS / f).read_text())
        parts.append(body)
    parts.append("# Sommaire {.unnumbered}\n\n@@TOC@@\n")
    for n, f in enumerate(build.CHAPS, 1):
        fm, body = build.split_front((MS / f).read_text())
        k = [0]
        def num(m):
            k[0] += 1
            return f"## {n}.{k[0]} {m.group(1)}"
        body = re.sub(r"^## (.+)$", num, body, flags=re.M)
        pts = "\n".join(f"{i}. {p}" for i, p in enumerate(fm["points"], 1))
        parts.append(f"# Chapitre {n} · {fm['titre']}\n\n::: {{custom-style=\"Accroche\"}}\n{fm['accroche']}\n:::\n\n**Dans ce chapitre**\n\n{pts}\n\n{body}")
    for f in build.BACK:
        fm, body = build.split_front((MS / f).read_text())
        parts.append(f"# {fm['titre']}\n\n{body}")
    md = "\n\n".join(parts)
    md = re.sub(r"\]\(\.\./03_ILLUSTRATIONS/schemas/(fig\w+)\.svg\)\{width=\d+%\}", r"](" + str(ROOT / "03_ILLUSTRATIONS/schemas") + r"/\1.png){width=16cm}", md)
    return md

def set_cell_shading(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), color)
    tcPr.append(sh)

def set_cell_borders(cell, color, left=None, sz=6):
    tcPr = cell._tc.get_or_add_tcPr()
    b = OxmlElement("w:tcBorders")
    for side in ("top", "left", "bottom", "right"):
        e = OxmlElement(f"w:{side}")
        e.set(qn("w:val"), "single"); e.set(qn("w:color"), color)
        e.set(qn("w:sz"), str(left if (side == "left" and left) else sz))
        b.append(e)
    tcPr.append(b)

def para_shading(p, color):
    pPr = p._p.get_or_add_pPr()
    sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), color)
    pPr.append(sh)

def para_left_border(p, color, sz=24):
    pPr = p._p.get_or_add_pPr()
    bd = OxmlElement("w:pBdr"); l = OxmlElement("w:left")
    l.set(qn("w:val"), "single"); l.set(qn("w:sz"), str(sz)); l.set(qn("w:space"), "6"); l.set(qn("w:color"), color)
    bd.append(l); pPr.append(bd)

class SD:
    def __init__(self, d): self.d = d; self.m = {s.name: s for s in d.styles}
    def __getitem__(self, k): return self.m[k]
    def __iter__(self): return iter(self.m.values())
    def add_style(self, n, t):
        s = self.d.styles.add_style(n, t); self.m[n] = s; return s

def make_reference():
    ref = OUTD / "reference.docx"
    with open(ref, "wb") as fh:
        subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"], stdout=fh, check=True)
    d = Document(ref)
    st = SD(d)
    def font(s, name, size, bold=None, color=None, italic=None):
        s.font.name = name; s.font.size = Pt(size)
        rpr = s.element.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
        if rf is None:
            rf = OxmlElement("w:rFonts"); rpr.append(rf)
        for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            rf.set(qn(a), name)
        if bold is not None: s.font.bold = bold
        if italic is not None: s.font.italic = italic
        if color: s.font.color.rgb = RGBColor.from_string(color)
    for nm in ("Normal", "Body Text", "First Paragraph", "Compact"):
        if nm in [s.name for s in st]:
            s = st[nm]; font(s, "Source Sans 3", 10.5, color="222428")
            s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            s.paragraph_format.line_spacing = 1.2
            s.paragraph_format.space_after = Pt(5)
    font(st["Heading 1"], "Montserrat Light", 22, False, NAVY); st["Heading 1"].paragraph_format.page_break_before = True
    st["Heading 1"].paragraph_format.space_after = Pt(14)
    font(st["Heading 2"], "Montserrat", 12.5, True, NAVY); st["Heading 2"].paragraph_format.space_before = Pt(14)
    font(st["Heading 3"], "Montserrat", 11, True, NAVY)
    for h in ("Heading 1", "Heading 2", "Heading 3"):
        st[h].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        st[h].paragraph_format.keep_with_next = True
    if "Title" in [s.name for s in st]:
        font(st["Title"], "Montserrat Light", 30, False, NAVY)
    for nm, sz, col, it in (("Subtitle", 15, GOLD, False), ("Accroche", 12.5, "4A4F57", True), ("Kicker", 8.5, GOLD, False)):
        s = st[nm] if nm in [x.name for x in st] else st.add_style(nm, 1)
        s.base_style = st["Normal"]; font(s, "Montserrat" if nm != "Accroche" else "Source Sans 3", sz, nm != "Accroche", col, it)
        s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    font(st["Caption"] if "Caption" in [s.name for s in st] else st.add_style("Caption", 1), "Montserrat", 8.5, False, "5E6166")
    for nm in ("Table Caption", "Image Caption"):
        if nm in [s.name for s in st]:
            font(st[nm], "Montserrat", 8.5, True, NAVY); st[nm].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    sec = d.sections[0]
    sec.page_width, sec.page_height = Mm(210), Mm(297)
    sec.left_margin = sec.right_margin = Mm(20); sec.top_margin = Mm(22); sec.bottom_margin = Mm(20)
    d.save(ref)
    return ref

def add_field(par, instr):
    r = par.add_run(); f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin"); r._r.append(f1)
    r2 = par.add_run(); it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = instr; r2._r.append(it)
    r3 = par.add_run(); f2 = OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"), "separate"); r3._r.append(f2)
    r4 = par.add_run("1")
    r5 = par.add_run(); f3 = OxmlElement("w:fldChar"); f3.set(qn("w:fldCharType"), "end"); r5._r.append(f3)

def style_data_table(t):
    if len(t.rows) < 1:
        return
    hdr = len(t.rows) > 1
    for i, row in enumerate(t.rows):
        for cell in row.cells:
            set_cell_borders(cell, "C2C4C7", sz=4)
            if i == 0 and hdr:
                set_cell_shading(cell, NAVY)
            for p in cell.paragraphs:
                p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in p.runs:
                    r.font.size = Pt(8.5 if i == 0 else 9)
                    if i == 0 and hdr:
                        r.font.color.rgb = RGBColor(255, 255, 255); r.bold = True; r.font.name = "Montserrat"

def postprocess(path, full=True):
    d = Document(path)
    # 1) encadrés
    for t in d.tables:
        cells = t._cells
        if len(cells) == 1 and cells[0].paragraphs and cells[0].paragraphs[0].text.startswith("@@BOX:"):
            c = cells[0]; p0 = c.paragraphs[0]
            kind = re.match(r"@@BOX:(\w+)@@", p0.text).group(1)
            label, fill, accent = LABELS[kind]
            for r in p0.runs: r.text = ""
            run = p0.add_run(label); run.bold = True; run.font.size = Pt(7.5); run.font.name = "Montserrat"
            run.font.color.rgb = RGBColor.from_string("8DBB9A" if kind == "retenir" else accent)
            p0.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            set_cell_shading(c, fill)
            set_cell_borders(c, accent if kind not in ("retenir",) else NAVY, left=36 if kind in ("situation", "definition", "cas", "prompt") else None, sz=6)
            if kind == "retenir":
                for p in c.paragraphs[1:]:
                    for r in p.runs:
                        r.font.color.rgb = RGBColor(255, 255, 255) if not r.bold else RGBColor.from_string("8DBB9A")
                for tb in c.tables:
                    pass
            for tb in c.tables:
                style_data_table(tb)
        else:
            style_data_table(t)
    # 2) titres de niveau 2 : bandeau marine
    for p in d.paragraphs:
        if p.style.name == "Heading 2":
            para_shading(p, NAVY)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.color.rgb = RGBColor(255, 255, 255); r.text = r.text.upper()
        elif p.style.name == "Heading 3":
            para_left_border(p, GOLD, 24)
    # 3) sommaire automatique
    for p in d.paragraphs:
        if p.text.strip() == "@@TOC@@":
            for r in p.runs: r.text = ""
            add_field(p, 'TOC \\o "1-2" \\h \\z \\u')
            note = p.insert_paragraph_before("Clic droit sur le sommaire puis « Mettre à jour les champs » pour actualiser les numéros de page.")
            note.runs[0].italic = True; note.runs[0].font.size = Pt(8)
    # 4) page de titre : pas de saut avant le premier titre
    first_h1 = next(p for p in d.paragraphs if p.style.name == "Heading 1")
    first_h1.paragraph_format.page_break_before = False
    if full:
        first_h1.style = SD(d)["Title"]
    # 5) en-têtes et pieds de page
    sec = d.sections[0]
    sec.different_first_page_header_footer = True
    hp = sec.header.paragraphs[0]; hp.text = ""
    r = hp.add_run("L'ARCHIVISTIQUE · PRINCIPES ET PRATIQUES DU MÉTIER D'ARCHIVISTE"); r.font.size = Pt(7.5); r.font.name = "Montserrat"; r.font.color.rgb = RGBColor.from_string(GOLD); r.bold = True
    fp = sec.footer.paragraphs[0]; fp.text = ""; fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = fp.add_run("Verdi Imbole  ·  page "); r.font.size = Pt(8); r.font.name = "Montserrat"; r.font.color.rgb = RGBColor.from_string("5E6166")
    add_field(fp, "PAGE")
    # demande la mise à jour des champs à l'ouverture
    settings = d.settings.element
    uf = OxmlElement("w:updateFields"); uf.set(qn("w:val"), "true"); settings.append(uf)
    comp = settings.find(qn("w:compat"))
    if comp is None:
        comp = OxmlElement("w:compat"); settings.append(comp)
    comp.insert(0, OxmlElement("w:doNotExpandShiftReturn"))
    d.core_properties.author = "Verdi Imbole"
    d.core_properties.title = "L'archivistique : principes et pratiques du métier d'archiviste"
    d.save(path)

def postprocess_light(path):
    postprocess(path, full=False)

def main():
    ref = make_reference()
    md = assemble_md()
    (OUTD / "livre_docx.md").write_text(md)
    (OUTD / "boxes.lua").write_text(LUA)
    out = OUTD / "livre.docx"
    subprocess.run(["pandoc", str(OUTD / "livre_docx.md"), "-f", "markdown+fenced_divs+pipe_tables+table_captions+implicit_figures",
                    "-t", "docx", "--reference-doc", str(ref), "--lua-filter", str(OUTD / "boxes.lua"), "-o", str(out)], check=True)
    postprocess(out)
    print("ok", out)

if __name__ == "__main__":
    main()
