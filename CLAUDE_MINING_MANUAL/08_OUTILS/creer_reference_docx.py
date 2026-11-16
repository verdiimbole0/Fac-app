# -*- coding: utf-8 -*-
"""Gabarit Word (reference.docx) — mise en page « livre » : format 15,5 × 23,5 cm,
marges en miroir, Garamond, titres courants alternés, encadrés sobres à filets.
Usage : python3 creer_reference_docx.py SORTIE.docx"""
import subprocess, sys
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

TITRE_LIVRE = "La Mine augmentée"
INK, SOFT, ACCENT, RULE, TINT = "1A1A1A", "555555", "8A5A2B", "8A5A2B", "F4F1EC"
SERIF, MONO = "Garamond", "Consolas"

def rgb(h): return RGBColor.from_string(h)

def find(doc, name):
    for s in doc.styles:
        if s.name == name or s.name.lower() == name.lower():
            return s
    raise KeyError(name)

def get(doc, name, base="Normal", kind=WD_STYLE_TYPE.PARAGRAPH):
    try:
        return find(doc, name)
    except KeyError:
        s = doc.styles.add_style(name, kind)
        if kind == WD_STYLE_TYPE.PARAGRAPH: s.base_style = find(doc, base)
        s.quick_style = True
        return s

def rpr_set(style, font=SERIF, size=None, bold=None, italic=None, color=None, caps=None, spacing=None):
    f = style.font; f.name = font
    rpr = style.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None: rf = OxmlElement("w:rFonts"); rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"): rf.set(qn(a), font)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
    if size: f.size = Pt(size)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    if color: f.color.rgb = rgb(color)
    if caps is not None: f.small_caps = caps
    if spacing is not None:
        sp = rpr.find(qn("w:spacing"))
        if sp is None: sp = OxmlElement("w:spacing"); rpr.append(sp)
        sp.set(qn("w:val"), str(int(spacing * 20)))

def para(style, before=0, after=0, line=None, align=None, indent_first=None, left=None, right=None,
         keep=None, page_break=None, widow=True):
    pf = style.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    if line: pf.line_spacing = Pt(line)
    if align is not None: pf.alignment = align
    if indent_first is not None: pf.first_line_indent = Cm(indent_first)
    if left is not None: pf.left_indent = Cm(left)
    if right is not None: pf.right_indent = Cm(right)
    if keep is not None: pf.keep_with_next = keep
    if page_break is not None: pf.page_break_before = page_break
    pf.widow_control = widow

def clear_borders(style):
    p = style.element.get_or_add_pPr()
    for t in ("w:pBdr", "w:shd"):
        e = p.find(qn(t))
        if e is not None: p.remove(e)

def borders(style, sides, color=RULE, sz=6, space=4):
    p = style.element.get_or_add_pPr(); clear_borders(style)
    b = OxmlElement("w:pBdr")
    for s in sides:
        e = OxmlElement(f"w:{s}"); e.set(qn("w:val"), "single"); e.set(qn("w:sz"), str(sz)); e.set(qn("w:space"), str(space)); e.set(qn("w:color"), color)
        b.append(e)
    p.insert(0, b)

def shade(style, fill):
    p = style.element.get_or_add_pPr()
    s = OxmlElement("w:shd"); s.set(qn("w:val"), "clear"); s.set(qn("w:color"), "auto"); s.set(qn("w:fill"), fill)
    b = p.find(qn("w:pBdr"))
    (b.addnext(s) if b is not None else p.insert(0, s))

def field(p, instr, size=9, caps=False, color=SOFT):
    def run(): r = p.add_run(); r.font.size = Pt(size); r.font.name = SERIF; r.font.small_caps = caps; r.font.color.rgb = rgb(color); return r
    r = run(); e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "begin"); r._r.append(e)
    r = run(); it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = instr; r._r.append(it)
    r = run(); e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "separate"); r._r.append(e)
    run().text = " "
    r = run(); e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end"); r._r.append(e)

def entete(paragraph, text=None, instr=None, align=WD_ALIGN_PARAGRAPH.CENTER):
    paragraph.text = ""; paragraph.alignment = align
    if text:
        r = paragraph.add_run(text); r.font.size = Pt(8.5); r.font.small_caps = True; r.font.name = SERIF; r.font.color.rgb = rgb(SOFT)
        rpr = r._r.get_or_add_rPr(); sp = OxmlElement("w:spacing"); sp.set(qn("w:val"), "30"); rpr.append(sp)
    if instr: field(paragraph, instr, size=8.5, caps=True)

def main(out):
    subprocess.run(["pandoc", "-o", out, "--print-default-data-file", "reference.docx"], check=True)
    doc = Document(out)
    doc.settings.odd_and_even_pages_header_footer = True
    st = doc.settings.element
    mm = OxmlElement("w:mirrorMargins"); st.append(mm)
    hy = OxmlElement("w:autoHyphenation"); hy.set(qn("w:val"), "true"); st.append(hy)
    for sec in doc.sections:
        sec.page_width, sec.page_height = Cm(15.5), Cm(23.5)
        sec.top_margin, sec.bottom_margin = Cm(2.0), Cm(2.1)
        sec.left_margin, sec.right_margin = Cm(2.1), Cm(1.6)   # intérieur / extérieur (miroir)
        sec.header_distance, sec.footer_distance = Cm(1.0), Cm(1.0)
        # Titres courants : verso = titre du livre ; recto = titre du chapitre en cours
        entete(sec.even_page_header.paragraphs[0], text=TITRE_LIVRE)
        entete(sec.header.paragraphs[0], instr=' STYLEREF "Heading 2" ')
        for f in (sec.footer, sec.even_page_footer):
            fp = f.paragraphs[0]; fp.text = ""; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            field(fp, " PAGE ", size=9.5, color=INK)

    # Corps du texte
    n = find(doc, "Normal"); rpr_set(n, size=11, color=INK); para(n, line=14.5)
    lang = n.element.get_or_add_rPr(); l = OxmlElement("w:lang"); l.set(qn("w:val"), "fr-FR"); lang.append(l)
    for name in ("Body Text", "First Paragraph"):
        s = get(doc, name); rpr_set(s, size=11, color=INK)
        para(s, after=0, line=14.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, indent_first=0 if name == "First Paragraph" else 0.6)
    c = get(doc, "Compact"); rpr_set(c, size=11, color=INK); para(c, after=1, line=14.5, align=WD_ALIGN_PARAGRAPH.LEFT)

    # Titres
    h1 = find(doc, "Heading 1")   # Parties
    rpr_set(h1, size=24, bold=False, italic=False, color=INK, caps=True, spacing=2); clear_borders(h1)
    para(h1, before=150, after=30, line=32, align=WD_ALIGN_PARAGRAPH.CENTER, keep=True, page_break=True)
    h2 = find(doc, "Heading 2")   # Chapitres
    rpr_set(h2, size=21, bold=False, italic=False, color=INK, caps=False); clear_borders(h2)
    para(h2, before=70, after=28, line=25, align=WD_ALIGN_PARAGRAPH.LEFT, keep=True, page_break=True)
    borders(h2, ["bottom"], color=RULE, sz=4, space=10)
    h3 = find(doc, "Heading 3")   # Sections A–L
    rpr_set(h3, size=11.5, bold=True, italic=False, color=INK, caps=True, spacing=0.6); clear_borders(h3)
    para(h3, before=20, after=6, keep=True, align=WD_ALIGN_PARAGRAPH.LEFT)
    h4 = find(doc, "Heading 4")
    rpr_set(h4, size=11.5, bold=False, italic=True, color=INK); clear_borders(h4)
    para(h4, before=12, after=3, keep=True, align=WD_ALIGN_PARAGRAPH.LEFT)
    for k in ("Heading 5", "Heading 6"):
        s = find(doc, k); rpr_set(s, size=11, bold=False, italic=True, color=INK); clear_borders(s)
    for k in ("Title", "Subtitle"):
        s = find(doc, k); rpr_set(s, size=24, color=INK); clear_borders(s)

    # Code et prompts : bloc teinté, sans filet coloré
    sc = get(doc, "Source Code"); rpr_set(sc, font=MONO, size=8, color="2B2B2B")
    para(sc, before=0, after=0, line=10.5, left=0.3, right=0.1, align=WD_ALIGN_PARAGRAPH.LEFT)
    clear_borders(sc); borders(sc, ["top", "bottom", "left", "right"], color=TINT, sz=4, space=4); shade(sc, TINT)
    vc = get(doc, "Verbatim Char", kind=WD_STYLE_TYPE.CHARACTER); rpr_set(vc, font=MONO, size=8.5, color="2B2B2B")

    # Légendes et figures
    for name in ("Image Caption", "Table Caption", "Caption"):
        s = get(doc, name); rpr_set(s, size=8.5, italic=True, color=SOFT)
        para(s, before=3, after=12, line=11, align=WD_ALIGN_PARAGRAPH.LEFT)
    for name in ("Captioned Figure", "Figure"):
        s = get(doc, name); para(s, before=10, after=2, align=WD_ALIGN_PARAGRAPH.CENTER, keep=True)
        s.paragraph_format.line_spacing = 1.0   # interligne simple : une image ne doit pas être rognée par un interligne exact

    bq = get(doc, "Block Text"); rpr_set(bq, size=11, italic=True, color=INK); clear_borders(bq)
    para(bq, before=8, after=8, line=14.5, left=1.0, right=1.0, align=WD_ALIGN_PARAGRAPH.JUSTIFY)

    # Encadrés : filets haut/bas couleur cuivre, fond très léger, titre en petites capitales
    for key in ("Retenir", "Terrain", "Attention", "Erreur", "Application", "Defi", "Setrompe", "Controle"):
        body = get(doc, f"Encadre {key}"); rpr_set(body, size=10, color=INK)
        para(body, before=0, after=2, line=13, left=0.25, right=0.25, align=WD_ALIGN_PARAGRAPH.LEFT)
        borders(body, ["top", "bottom", "left", "right"], color=TINT, sz=4, space=6); shade(body, TINT)
        bb = body.element.get_or_add_pPr().find(qn("w:pBdr")).find(qn("w:bottom")); bb.set(qn("w:color"), RULE); bb.set(qn("w:sz"), "8")
        t = get(doc, f"Encadre {key} Titre", base=f"Encadre {key}")
        rpr_set(t, size=8.5, bold=True, color=ACCENT, caps=True, spacing=1.2)
        para(t, before=12, after=0, line=13, left=0.25, right=0.25, keep=True)
        borders(t, ["top", "left", "right"], color=TINT, sz=4, space=6)
        p = t.element.get_or_add_pPr(); b = p.find(qn("w:pBdr")); top = b.find(qn("w:top"))
        top.set(qn("w:color"), RULE); top.set(qn("w:sz"), "8")
        shade(t, TINT)

    # Carnet de réflexion
    cl = get(doc, "Carnet Ligne"); rpr_set(cl, size=11, color="FFFFFF"); para(cl, line=22)
    borders(cl, ["bottom"], color="BDB7AE", sz=2, space=1)
    p = cl.element.get_or_add_pPr(); p.find(qn("w:pBdr")).find(qn("w:bottom")).set(qn("w:val"), "dotted")
    cr = get(doc, "Carnet Rubrique"); rpr_set(cr, size=10, italic=True, color=INK); para(cr, before=9, after=0, keep=True)
    ct = get(doc, "Carnet Titre"); rpr_set(ct, size=14, color=INK, caps=True, spacing=1.5)
    para(ct, before=24, after=4, align=WD_ALIGN_PARAGRAPH.CENTER, page_break=True); clear_borders(ct)
    cc = get(doc, "Carnet Cadre"); rpr_set(cc, size=11, color="FFFFFF"); para(cc, line=16)
    borders(cc, ["top", "bottom", "left", "right"], color="BDB7AE", sz=2, space=4)

    # Ouvertures de parties
    pi = get(doc, "Partie Intro"); rpr_set(pi, size=11.5, italic=True, color=INK)
    para(pi, before=0, after=8, line=15, left=0.8, right=0.8, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    pc = get(doc, "Partie Chapitres"); rpr_set(pc, size=10, color=SOFT); para(pc, after=1, left=0.8, align=WD_ALIGN_PARAGRAPH.LEFT)

    # Page de titre
    for name, size, it, caps, before, after in [("Titre Livre", 30, False, True, 140, 14), ("Sous-titre Livre", 13.5, True, False, 0, 40),
                                               ("Mention Livre", 10, False, True, 0, 4)]:
        s = get(doc, name); rpr_set(s, size=size, italic=it, caps=caps, color=INK, spacing=2 if name == "Titre Livre" else None)
        para(s, before=before, after=after, line={"Titre Livre": 40, "Sous-titre Livre": 18}.get(name, 13), align=WD_ALIGN_PARAGRAPH.CENTER)

    # Bibliographie : retrait suspendu
    ref = get(doc, "Reference"); rpr_set(ref, size=10, color=INK)
    para(ref, after=5, line=13, left=0.8, indent_first=-0.8, align=WD_ALIGN_PARAGRAPH.LEFT)

    # Sommaire
    th = get(doc, "TOC Heading"); rpr_set(th, size=20, color=INK, caps=True, spacing=2); para(th, before=40, after=24, align=WD_ALIGN_PARAGRAPH.CENTER)
    for i in (1, 2, 3):
        s = get(doc, f"TOC {i}")
        rpr_set(s, size=10.5 if i == 1 else 10, bold=False, color=INK, caps=(i == 1), spacing=0.8 if i == 1 else None)
        para(s, before=10 if i == 1 else 1, after=1, left=0 if i == 1 else 0.5)
    doc.save(out)
    print("reference.docx créé :", out)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "reference.docx")
