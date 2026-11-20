#!/usr/bin/env python3
"""Crée le modèle de styles Word (reference.docx) de l'ouvrage : 17 × 24 cm, Source Serif 4 / Source Sans 3."""
import os, subprocess
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "reference.docx")
NAVY, TEAL, GOLD, GREY = RGBColor(0x10, 0x28, 0x49), RGBColor(0x16, 0x7D, 0x73), RGBColor(0xC7, 0xA3, 0x4F), RGBColor(0x4A, 0x5A, 0x70)

subprocess.run(["pandoc", "-o", OUT, "--print-default-data-file", "reference.docx"], check=True)

d = Document(OUT)
for s in d.sections:
    s.page_width, s.page_height = Cm(17), Cm(24)
    s.top_margin, s.bottom_margin = Cm(2.2), Cm(2.2)
    s.left_margin, s.right_margin = Cm(2.0), Cm(1.8)
    s.header_distance = s.footer_distance = Cm(1.0)


def font(style, name, size=None, color=None, bold=None, italic=None):
    st = next((x for x in d.styles if x.name == style), None)
    if st is None:
        raise KeyError(style)
    st.font.name = name
    rpr = st.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts"); rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), name)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        if rf.get(qn(a)) is not None:
            del rf.attrib[qn(a)]
    if size: st.font.size = Pt(size)
    if color is not None: st.font.color.rgb = color
    if bold is not None: st.font.bold = bold
    if italic is not None: st.font.italic = italic
    return st


for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
    try:
        st = font(name, "Source Serif 4", 11.5, RGBColor(0x1F, 0x1F, 0x1F))
        pf = st.paragraph_format
        pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE; pf.line_spacing = 1.4
        if name != "Compact":
            pf.space_after = Pt(6)
    except KeyError:
        pass

sizes = {1: 22, 2: 15, 3: 12.5, 4: 11.5, 5: 11, 6: 11}
for lvl, sz in sizes.items():
    st = font(f"Heading {lvl}", "Source Sans 3", sz, NAVY if lvl != 3 else TEAL, True, False)
    st.paragraph_format.space_before = Pt(18 if lvl <= 2 else 10)
    st.paragraph_format.space_after = Pt(8 if lvl <= 2 else 4)
    st.paragraph_format.keep_with_next = True
    if lvl == 1:
        st.paragraph_format.page_break_before = True
for name in ("Title", "Subtitle", "Author", "Date"):
    try: font(name, "Source Sans 3", None, NAVY)
    except KeyError: pass
for name in ("Caption", "Image Caption", "Table Caption"):
    try: font(name, "Source Sans 3", 9.5, GREY, False, True)
    except KeyError: pass
for name in ("Source Code", "Verbatim Char"):
    try: font(name, "JetBrains Mono", 8.5, NAVY)
    except KeyError: pass
try:
    st = font("Block Text", "Source Sans 3", 10.5, NAVY)
except KeyError:
    pass
for name in ("Hyperlink",):
    try: font(name, "Source Serif 4", None, TEAL)
    except KeyError: pass
try:
    font("TOC Heading", "Source Sans 3", 18, NAVY, True)
except KeyError:
    pass


# Styles personnalisés des pages liminaires
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
def pstyle(name, size, bold, before=0, after=6):
    st = next((x for x in d.styles if x.name == name), None) or d.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    st.base_style = next(x for x in d.styles if x.name == "Normal")
    font(name, "Source Sans 3", size, NAVY, bold, False)
    st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    st.paragraph_format.space_before = Pt(before); st.paragraph_format.space_after = Pt(after)
pstyle("Faux titre", 24, True, 180, 0)
pstyle("Page de titre", 13, False, 6, 8)
cs = next((x for x in d.styles if x.name == "Titre du livre"), None) or d.styles.add_style("Titre du livre", WD_STYLE_TYPE.CHARACTER)
font("Titre du livre", "Source Sans 3", 30, NAVY, True, False)

# Style de tableau : bordures fines et ligne d'en-tête
tst = next(x for x in d.styles if x.name == "Table")
tblPr = tst.element.find(qn("w:tblPr"))
if tblPr is None:
    tblPr = OxmlElement("w:tblPr"); tst.element.append(tblPr)
b = OxmlElement("w:tblBorders")
for edge in ("top", "bottom", "insideH"):
    e = OxmlElement(f"w:{edge}"); e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "4"); e.set(qn("w:color"), "B8C4D2"); b.append(e)
tblPr.append(b)
font("Table", "Source Sans 3", 9, RGBColor(0x1F, 0x1F, 0x1F))

# En-tête / pied de page discrets
sec = d.sections[0]
p = sec.footer.paragraphs[0] if sec.footer.paragraphs else sec.footer.add_paragraph()
p.text = ""
run = p.add_run("ASBL augmentée — Verdi Imbole    ")
run.font.size = Pt(8); run.font.color.rgb = GREY; run.font.name = "Source Sans 3"
fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), "PAGE")
r = OxmlElement("w:r"); t = OxmlElement("w:t"); t.text = "1"; r.append(t); fld.append(r); p._p.append(fld)
d.save(OUT)
print("reference.docx prêt")
