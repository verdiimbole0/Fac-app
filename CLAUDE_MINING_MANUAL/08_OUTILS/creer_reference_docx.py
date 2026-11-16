# -*- coding: utf-8 -*-
"""Crée le gabarit Word (reference.docx) utilisé par pandoc : styles, encadrés,
en-têtes et pieds de page. Usage : python3 creer_reference_docx.py SORTIE.docx"""
import subprocess, sys, copy
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY, GOLD, GREY, TURQ, RED, INK = "0B2545", "C9A227", "EEF1F5", "13A89E", "B23A48", "222831"
BODY, HEAD, MONO = "Cambria", "Calibri", "Consolas"

# type d'encadré -> (couleur de bordure, couleur de fond)
ENCADRES = {
    "Retenir":     (NAVY, "E6ECF4"),
    "Terrain":     (TURQ, "E3F4F2"),
    "Attention":   (RED,  "F8E6E9"),
    "Erreur":      ("D9822B", "FBEEDF"),
    "Application": (GOLD, "FAF4DF"),
    "Defi":        ("6A4C93", "EFE9F6"),
    "Setrompe":    ("8C2F39", "F4E4E6"),
    "Controle":    ("2D6A4F", "E4F1EA"),
    "Carnet":      (GOLD, "FFFFFF"),
}

def rgb(h): return RGBColor.from_string(h)

def set_font(style, name, size=None, bold=None, color=None, italic=None):
    f = style.font
    f.name = name
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts"); rpr.append(rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(a), name)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        if rfonts.get(qn(a)) is not None: del rfonts.attrib[qn(a)]
    if size: f.size = Pt(size)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    if color: f.color.rgb = rgb(color)

def ppr(style):
    return style.element.get_or_add_pPr()

def add_border(style, color, sides=("top", "left", "bottom", "right"), sz=8, space=6, val="single"):
    p = ppr(style)
    old = p.find(qn("w:pBdr"))
    if old is not None: p.remove(old)
    bdr = OxmlElement("w:pBdr")
    for s in sides:
        e = OxmlElement(f"w:{s}")
        e.set(qn("w:val"), val); e.set(qn("w:sz"), str(sz)); e.set(qn("w:space"), str(space)); e.set(qn("w:color"), color)
        bdr.append(e)
    # pBdr doit précéder shd/spacing/ind dans le schéma : on l'insère en tête
    p.insert(0, bdr)

def add_shading(style, fill):
    p = ppr(style)
    old = p.find(qn("w:shd"))
    if old is not None: p.remove(old)
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    bdr = p.find(qn("w:pBdr"))
    if bdr is not None: bdr.addnext(shd)
    else: p.insert(0, shd)

def get_or_add(doc, name, base="Normal", kind=WD_STYLE_TYPE.PARAGRAPH):
    try:
        return doc.styles[name]
    except KeyError:
        s = doc.styles.add_style(name, kind)
        if kind == WD_STYLE_TYPE.PARAGRAPH: s.base_style = doc.styles[base]
        s.quick_style = True
        return s

def page_break_before(style, on=True):
    style.paragraph_format.page_break_before = on

def field_run(paragraph, instr):
    r = paragraph.add_run()
    b = OxmlElement("w:fldChar"); b.set(qn("w:fldCharType"), "begin"); r._r.append(b)
    r2 = paragraph.add_run(); it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = instr; r2._r.append(it)
    r3 = paragraph.add_run(); s = OxmlElement("w:fldChar"); s.set(qn("w:fldCharType"), "separate"); r3._r.append(s)
    r4 = paragraph.add_run("1")
    r5 = paragraph.add_run(); e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end"); r5._r.append(e)
    return [r, r2, r3, r4, r5]

def main(out):
    base = subprocess.run(["pandoc", "-o", out, "--print-default-data-file", "reference.docx"], check=True)
    doc = Document(out)
    st = doc.styles

    # --- Page : A4 (17 x 24 serait l'idéal éditeur ; A4 pour l'impression bureautique)
    for sec in doc.sections:
        sec.page_width, sec.page_height = Cm(21), Cm(29.7)
        sec.left_margin = sec.right_margin = Cm(2.2)
        sec.top_margin, sec.bottom_margin = Cm(2.3), Cm(2.2)
        sec.header_distance = sec.footer_distance = Cm(1.1)
        # en-tête
        h = sec.header; hp = h.paragraphs[0] if h.paragraphs else h.add_paragraph()
        hp.text = ""; r = hp.add_run("CLAUDE ET L'IA AU SERVICE DE L'INDUSTRIE MINIÈRE")
        r.font.size = Pt(8); r.font.color.rgb = rgb(NAVY); r.font.name = HEAD; r.font.bold = True
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        pb = OxmlElement("w:pBdr"); bt = OxmlElement("w:bottom")
        for k, v in (("w:val", "single"), ("w:sz", "6"), ("w:space", "4"), ("w:color", GOLD)): bt.set(qn(k), v)
        pb.append(bt); hp._p.get_or_add_pPr().append(pb)
        # pied de page : numéro
        f = sec.footer; fp = f.paragraphs[0] if f.paragraphs else f.add_paragraph()
        fp.text = ""; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for rr in field_run(fp, " PAGE "):
            rr.font.size = Pt(9); rr.font.color.rgb = rgb(NAVY); rr.font.name = HEAD

    # --- Styles de base
    normal = st["Normal"]; set_font(normal, BODY, 10.5, color=INK)
    normal.paragraph_format.space_after = Pt(5); normal.paragraph_format.line_spacing = 1.12
    for name in ("Body Text", "First Paragraph", "Compact"):
        s = get_or_add(doc, name); set_font(s, BODY, 10.5, color=INK)
        s.paragraph_format.space_after = Pt(5 if name != "Compact" else 2)
        s.paragraph_format.space_before = Pt(0)
        s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if name != "Compact" else None

    heads = {
        "Title": (HEAD, 28, True, NAVY), "Subtitle": (HEAD, 14, False, GOLD),
        "Heading 1": (HEAD, 26, True, NAVY), "Heading 2": (HEAD, 20, True, NAVY),
        "Heading 3": (HEAD, 14, True, NAVY), "Heading 4": (HEAD, 12, True, TURQ),
        "Heading 5": (HEAD, 11, True, INK), "Heading 6": (HEAD, 10.5, True, INK),
    }
    for name, (font, size, bold, color) in heads.items():
        s = st[name]; set_font(s, font, size, bold, color, italic=False)
        s.paragraph_format.keep_with_next = True
    st["Heading 1"].paragraph_format.space_before = Pt(160)
    st["Heading 1"].paragraph_format.space_after = Pt(24)
    page_break_before(st["Heading 1"])
    add_border(st["Heading 1"], GOLD, sides=("bottom",), sz=24, space=8)
    st["Heading 2"].paragraph_format.space_before = Pt(0)
    st["Heading 2"].paragraph_format.space_after = Pt(18)
    page_break_before(st["Heading 2"])
    add_border(st["Heading 2"], GOLD, sides=("bottom",), sz=12, space=6)
    st["Heading 3"].paragraph_format.space_before = Pt(16)
    st["Heading 3"].paragraph_format.space_after = Pt(6)
    add_border(st["Heading 3"], TURQ, sides=("left",), sz=24, space=6)
    st["Heading 4"].paragraph_format.space_before = Pt(10)
    st["Heading 4"].paragraph_format.space_after = Pt(4)

    # Code / prompts
    sc = get_or_add(doc, "Source Code"); set_font(sc, MONO, 8.5, color="1B263B")
    sc.paragraph_format.space_after = Pt(0); sc.paragraph_format.line_spacing = 1.0
    add_border(sc, "9AA5B1", sides=("left",), sz=18, space=6); add_shading(sc, "F2F4F7")
    vt = get_or_add(doc, "Verbatim Char", kind=WD_STYLE_TYPE.CHARACTER); set_font(vt, MONO, 9, color="1B263B")

    # Légendes et figures
    for name in ("Image Caption", "Table Caption", "Caption"):
        s = get_or_add(doc, name); set_font(s, HEAD, 8.5, False, "4A5568", italic=True)
        s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        s.paragraph_format.space_after = Pt(10)
    cf = get_or_add(doc, "Captioned Figure"); cf.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER; cf.paragraph_format.keep_with_next = True
    fg = get_or_add(doc, "Figure"); fg.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER; fg.paragraph_format.keep_with_next = True

    # Citations
    bq = get_or_add(doc, "Block Text"); set_font(bq, BODY, 10, italic=True, color="34495E")
    add_border(bq, GOLD, sides=("left",), sz=18, space=8); bq.paragraph_format.left_indent = Cm(0.6)

    # Encadrés : style corps + style titre par type
    for key, (bc, fill) in ENCADRES.items():
        body = get_or_add(doc, f"Encadre {key}"); set_font(body, BODY, 10, color=INK)
        body.paragraph_format.left_indent = Cm(0.3); body.paragraph_format.right_indent = Cm(0.3)
        body.paragraph_format.space_after = Pt(3); body.paragraph_format.space_before = Pt(0)
        add_border(body, bc, sz=8, space=5); add_shading(body, fill)
        title = get_or_add(doc, f"Encadre {key} Titre", base=f"Encadre {key}")
        set_font(title, HEAD, 10, True, bc)
        title.paragraph_format.keep_with_next = True; title.paragraph_format.space_before = Pt(8)

    # Carnet : lignes d'écriture
    ligne = get_or_add(doc, "Carnet Ligne"); set_font(ligne, BODY, 11, color="FFFFFF")
    ligne.paragraph_format.space_after = Pt(0); ligne.paragraph_format.line_spacing = Pt(22)
    add_border(ligne, "B8C2CC", sides=("bottom",), sz=4, space=1, val="dotted")
    cq = get_or_add(doc, "Carnet Rubrique"); set_font(cq, HEAD, 10, True, NAVY)
    cq.paragraph_format.space_before = Pt(8); cq.paragraph_format.keep_with_next = True
    ct = get_or_add(doc, "Carnet Titre"); set_font(ct, HEAD, 16, True, GOLD)
    ct.paragraph_format.page_break_before = True; ct.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ct.paragraph_format.space_after = Pt(4)
    add_border(ct, GOLD, sides=("bottom",), sz=8, space=4)
    cad = get_or_add(doc, "Carnet Cadre"); set_font(cad, BODY, 11, color="FFFFFF")
    add_border(cad, "B8C2CC", sz=6, space=4); cad.paragraph_format.space_after = Pt(0)

    # Ouverture de partie
    po = get_or_add(doc, "Partie Intro"); set_font(po, BODY, 12, italic=True, color=NAVY)
    po.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT; po.paragraph_format.space_after = Pt(8)
    pc = get_or_add(doc, "Partie Chapitres"); set_font(pc, HEAD, 11, False, INK)
    pc.paragraph_format.left_indent = Cm(0.6); pc.paragraph_format.space_after = Pt(2)

    # Page de titre
    for name, (font, size, bold, color, align) in {
        "Titre Livre": (HEAD, 30, True, NAVY, WD_ALIGN_PARAGRAPH.LEFT),
        "Sous-titre Livre": (HEAD, 15, False, GOLD, WD_ALIGN_PARAGRAPH.LEFT),
        "Mention Livre": (BODY, 10, False, "4A5568", WD_ALIGN_PARAGRAPH.LEFT),
    }.items():
        s = get_or_add(doc, name); set_font(s, font, size, bold, color); s.paragraph_format.alignment = align
        s.paragraph_format.space_after = Pt(10)
    get_or_add(doc, "Titre Livre").paragraph_format.space_before = Pt(180)

    # Sommaire
    for i in (1, 2, 3):
        try:
            s = st[f"TOC {i}"]
        except KeyError:
            s = get_or_add(doc, f"TOC {i}")
        set_font(s, HEAD, 11 if i == 1 else 10, i == 1, NAVY if i == 1 else INK)
        s.paragraph_format.space_before = Pt(6 if i == 1 else 0); s.paragraph_format.space_after = Pt(1)
    th = get_or_add(doc, "TOC Heading"); set_font(th, HEAD, 20, True, NAVY)

    # Listes à puces : légère réduction d'espacement
    doc.save(out)
    print("reference.docx créé :", out)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "reference.docx")
