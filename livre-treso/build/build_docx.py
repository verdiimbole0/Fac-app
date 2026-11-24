"""Construit LA TRÉSO SOUS CONTRÔLE (DOCX A5) à partir de content/*.md et data/fil_rouge.py."""
import re, sys, os, json, glob
from docx import Document
from docx.shared import Pt, Mm, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "data"))
from style import *
import tables as T

TEXT_W_MM = 148 - 16 - 12
PAGEMAP = json.load(open(os.path.join(ROOT, "build", "pagemap.json"))) if os.path.exists(os.path.join(ROOT, "build", "pagemap.json")) else {}

def rgb(h): return RGBColor.from_string(h)
def set_cell_bg(cell, color):
    tcPr = cell._tc.get_or_add_tcPr(); shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), color); tcPr.append(shd)
def set_cell_borders(cell, **kw):
    tcPr = cell._tc.get_or_add_tcPr(); b = OxmlElement('w:tcBorders')
    for edge in ('top', 'left', 'bottom', 'right'):
        v = kw.get(edge)
        el = OxmlElement(f'w:{edge}')
        if v: el.set(qn('w:val'), v[0]); el.set(qn('w:sz'), str(v[1])); el.set(qn('w:color'), v[2]); el.set(qn('w:space'), '0')
        else: el.set(qn('w:val'), 'nil')
        b.append(el)
    tcPr.append(b)
def set_cell_margins(cell, top=60, bottom=60, left=110, right=110):
    tcPr = cell._tc.get_or_add_tcPr(); m = OxmlElement('w:tcMar')
    for k, v in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        e = OxmlElement(f'w:{k}'); e.set(qn('w:w'), str(v)); e.set(qn('w:type'), 'dxa'); m.append(e)
    tcPr.append(m)
def table_width(table, widths_mm):
    tbl = table._tbl; tblPr = tbl.tblPr
    w = OxmlElement('w:tblW'); w.set(qn('w:w'), str(int(sum(widths_mm) * 56.7))); w.set(qn('w:type'), 'dxa')
    for e in tblPr.findall(qn('w:tblW')): tblPr.remove(e)
    tblPr.append(w)
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
    grid = tbl.tblGrid
    for i, gc in enumerate(grid.findall(qn('w:gridCol'))):
        gc.set(qn('w:w'), str(int(widths_mm[i] * 56.7)))
    for row in table.rows:
        for i, c in enumerate(row.cells):
            c.width = Mm(widths_mm[i])
def no_split(row):
    trPr = row._tr.get_or_add_trPr(); e = OxmlElement('w:cantSplit'); trPr.append(e)
def repeat_header(row):
    trPr = row._tr.get_or_add_trPr(); e = OxmlElement('w:tblHeader'); trPr.append(e)
def keep_next(p, v=True): p.paragraph_format.keep_with_next = v

def nohyph(p):
    pPr = p._p.get_or_add_pPr(); e = OxmlElement('w:suppressAutoHyphens'); pPr.append(e); return p

_ANCHOR_ID = [5000]
def anchor_picture(paragraph, path, w_mm, h_mm, x_mm=0, y_mm=0):
    run = paragraph.add_run(); run.add_picture(path, width=Mm(w_mm), height=Mm(h_mm))
    inline = run._r.xpath('.//wp:inline')[0]
    E = lambda mm: int(mm * 36000)
    _ANCHOR_ID[0] += 1
    anchor = parse_xml(
        f'<wp:anchor {nsdecls("wp", "a", "pic", "r")} distT="0" distB="0" distL="0" distR="0" simplePos="0" relativeHeight="{_ANCHOR_ID[0]}" '
        f'behindDoc="1" locked="1" layoutInCell="1" allowOverlap="1"><wp:simplePos x="0" y="0"/>'
        f'<wp:positionH relativeFrom="page"><wp:posOffset>{E(x_mm)}</wp:posOffset></wp:positionH>'
        f'<wp:positionV relativeFrom="page"><wp:posOffset>{E(y_mm)}</wp:posOffset></wp:positionV>'
        f'<wp:extent cx="{E(w_mm)}" cy="{E(h_mm)}"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:wrapNone/></wp:anchor>')
    for tag in ('wp:docPr', 'wp:cNvGraphicFramePr', 'a:graphic'):
        el = inline.xpath(tag)[0]; anchor.append(el)
    inline.getparent().replace(inline, anchor)
    return run

NBSP = "\u00a0"
def typo(s):
    s = re.sub(r'(\d) (\d{3})(?!\d)', lambda m: m.group(1) + NBSP + m.group(2), s)
    s = re.sub(r'(\d) (\d{3})(?!\d)', lambda m: m.group(1) + NBSP + m.group(2), s)
    s = re.sub(r'(\d) (USD|CDF|%|j\b|jours|mois|semaines|h\b)', lambda m: m.group(1) + NBSP + m.group(2), s)
    s = re.sub(r' ([:;?!»])', NBSP + r'\1', s); s = s.replace('« ', '«' + NBSP)
    s = s.replace("'", "’")
    return s

INLINE = re.compile(r'(\*\*.+?\*\*|\*[^*\s][^*]*?\*|`[^`]+`)')
def add_runs(p, text, size=None, color=None, bold=None, font=None, italic=None):
    for part in INLINE.split(typo(text)):
        if not part: continue
        b = it = mono = False
        if part.startswith('**') and part.endswith('**'): part = part[2:-2]; b = True
        elif part.startswith('`') and part.endswith('`'): part = part[1:-1]; mono = True
        elif part.startswith('*') and part.endswith('*') and len(part) > 2: part = part[1:-1]; it = True
        r = p.add_run(part.replace('’', "’"))
        r.bold = True if (b or bold) else None
        r.italic = True if (it or italic) else None
        if mono: r.font.name = MONO_FONT; r.font.size = Pt(max(8.0, (size or BODY_PT) - 1.5))
        elif font: r.font.name = font
        if size and not mono: r.font.size = Pt(size)
        if color: r.font.color.rgb = rgb(color)
    return p

class Builder:
    def __init__(self):
        self.doc = Document(); self.setup(); self.first = True
        self.fig_n = {}; self.tab_n = {}; self.chap = 0; self.running = ""; self.small = None; self.heads = []
    def setup(self):
        d = self.doc; s = d.sections[0]
        s.page_width = Mm(148); s.page_height = Mm(210)
        s.top_margin = Mm(15); s.bottom_margin = Mm(14); s.left_margin = Mm(16); s.right_margin = Mm(12)
        s.header_distance = Mm(8); s.footer_distance = Mm(8)
        settings = d.settings.element
        mm = OxmlElement('w:mirrorMargins'); settings.append(mm)
        eo = OxmlElement('w:evenAndOddHeaders'); settings.append(eo)
        lang = OxmlElement('w:themeFontLang'); lang.set(qn('w:val'), 'fr-FR'); settings.append(lang)
        ah = OxmlElement('w:autoHyphenation'); settings.append(ah)
        ch = OxmlElement('w:consecutiveHyphenLimit'); ch.set(qn('w:val'), '2'); settings.append(ch)
        hz = OxmlElement('w:hyphenationZone'); hz.set(qn('w:val'), '284'); settings.append(hz)
        dc = OxmlElement('w:doNotHyphenateCaps'); settings.append(dc)
        st = d.styles
        n = st['Normal']; n.font.name = BODY_FONT; n.font.size = Pt(BODY_PT); n.font.color.rgb = rgb("1E2633")
        rpr = n.element.get_or_add_rPr(); rf = rpr.find(qn('w:rFonts'))
        for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'): rf.set(qn(a), BODY_FONT)
        l = OxmlElement('w:lang'); l.set(qn('w:val'), 'fr-FR'); rpr.append(l)
        pf = n.paragraph_format; pf.space_after = Pt(3); pf.space_before = Pt(0); pf.line_spacing = 1.1
        pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        pf.widow_control = True
        for name, size, color, before, after, font in [("Heading 1", 22, NAVY, 0, 8, DISPLAY_FONT), ("Heading 2", 13, NAVY, 10, 3, DISPLAY_FONT),
                                                         ("Heading 3", 9.6, TEAL, 8, 2, TITLE_FONT)]:
            h = st[name]; h.font.name = font; h.font.size = Pt(size); h.font.bold = True; h.font.color.rgb = rgb(color); h.font.italic = False
            r = h.element.get_or_add_rPr(); rf = r.find(qn('w:rFonts'))
            if rf is None: rf = OxmlElement('w:rFonts'); r.append(rf)
            for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'): rf.set(qn(a), font)
            for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:cstheme', 'w:eastAsiaTheme'):
                if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
            h.paragraph_format.space_before = Pt(before); h.paragraph_format.space_after = Pt(after)
            h.paragraph_format.keep_with_next = True; h.paragraph_format.line_spacing = 1.05
            h.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            h.element.get_or_add_pPr().append(OxmlElement('w:suppressAutoHyphens'))
            h.font.bold = (name != 'Heading 1')
        # styles de légende / tableau
        from docx.enum.style import WD_STYLE_TYPE
        cap = st.add_style('Legende', WD_STYLE_TYPE.PARAGRAPH); cap.base_style = n; cap.font.size = Pt(8.5)
        cap.font.italic = True; cap.font.color.rgb = rgb(MID); cap.paragraph_format.space_after = Pt(8)
        cap.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap.element.get_or_add_pPr().append(OxmlElement('w:suppressAutoHyphens'))
        tt = st.add_style('TabTexte', WD_STYLE_TYPE.PARAGRAPH); tt.base_style = n; tt.font.size = Pt(8.3)
        tt.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        tt.element.get_or_add_pPr().append(OxmlElement('w:suppressAutoHyphens'))
        tt.paragraph_format.space_after = Pt(0); tt.paragraph_format.line_spacing = 1.0
        for lvl in ('List Bullet', 'List Number'):
            ls = st[lvl]; ls.font.name = BODY_FONT; ls.paragraph_format.space_after = Pt(2.5); ls.paragraph_format.line_spacing = 1.12
    # ---------- sections, en-têtes, pieds -----------------------------------
    def _field(self, p, instr):
        r = p.add_run(); f1 = OxmlElement('w:fldChar'); f1.set(qn('w:fldCharType'), 'begin'); r._r.append(f1)
        r2 = p.add_run(); it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = instr; r2._r.append(it)
        r3 = p.add_run(); f2 = OxmlElement('w:fldChar'); f2.set(qn('w:fldCharType'), 'separate'); r3._r.append(f2)
        r4 = p.add_run("1")
        r5 = p.add_run(); f3 = OxmlElement('w:fldChar'); f3.set(qn('w:fldCharType'), 'end'); r5._r.append(f3)
        for r in (r, r2, r3, r4, r5): r.font.size = Pt(8); r.font.name = TITLE_FONT; r.font.color.rgb = rgb(NAVY)
    def new_section(self, running, blank_header=False, numbered=True, first_number=True):
        if self.first:
            sec = self.doc.sections[0]; self.first = False
        else:
            body = self.doc.element.body
            last = body[-2] if len(body) > 1 else None   # body[-1] = sectPr
            if last is not None and last.tag == qn('w:p') and not ''.join(last.itertext()).strip() and last.find('.//' + qn('w:drawing')) is None \
               and last.getprevious() is not None and last.getprevious().tag == qn('w:tbl'):
                pPr = last.find(qn('w:pPr'))
                if pPr is None or pPr.find(qn('w:sectPr')) is None:
                    p = [x for x in self.doc.paragraphs if x._p is last][0]
                    pf = p.paragraph_format; pf.space_after = Pt(0); pf.space_before = Pt(0)
                    pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(1)
            sec = self.doc.add_section(WD_SECTION.NEW_PAGE)
            # le paragraphe porteur du saut de section ne doit pas créer de page vide
            for p in reversed(self.doc.paragraphs):
                if p._p.pPr is not None and p._p.pPr.find(qn('w:sectPr')) is not None:
                    pf = p.paragraph_format; pf.space_after = Pt(0); pf.space_before = Pt(0)
                    pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(1); break
            prev = self.doc.paragraphs[-2] if len(self.doc.paragraphs) > 1 else None
        sec.different_first_page_header_footer = True
        for hdr, align, text in ((sec.header, WD_ALIGN_PARAGRAPH.RIGHT, running), (sec.even_page_header, WD_ALIGN_PARAGRAPH.LEFT, "LA TRÉSO SOUS CONTRÔLE")):
            hdr.is_linked_to_previous = False
            p = hdr.paragraphs[0]; p.text = ""; p.alignment = align
            if not blank_header:
                r = p.add_run(text.upper() if text else ""); r.font.size = Pt(7); r.font.name = TITLE_FONT; r.font.color.rgb = rgb(MID)
                r.font.bold = True
                pPr = p._p.get_or_add_pPr(); bd = OxmlElement('w:pBdr'); bt = OxmlElement('w:bottom')
                bt.set(qn('w:val'), 'single'); bt.set(qn('w:sz'), '4'); bt.set(qn('w:color'), 'C9D1DC'); bt.set(qn('w:space'), '3'); bd.append(bt); pPr.append(bd)
        for fi, (ftr, align) in enumerate(((sec.footer, WD_ALIGN_PARAGRAPH.RIGHT), (sec.even_page_footer, WD_ALIGN_PARAGRAPH.LEFT), (sec.first_page_footer, WD_ALIGN_PARAGRAPH.CENTER))):
            ftr.is_linked_to_previous = False
            p = ftr.paragraphs[0]; p.text = ""; p.alignment = align
            if numbered and (first_number or fi != 2): self._field(p, "PAGE")
        sec.first_page_header.is_linked_to_previous = False
        sec.first_page_header.paragraphs[0].text = ""
        return sec
    # ---------- blocs ----------------------------------------------------------
    def para(self, text, style=None, align=None, size=None, color=None, bold=None, after=None, before=None, italic=None, font=None, keep=False, container=None):
        cont = container or self.doc
        p = cont.add_paragraph(style=style) if style else cont.add_paragraph()
        add_runs(p, text, size=size, color=color, bold=bold, italic=italic, font=font)
        if align is not None:
            p.alignment = align; nohyph(p)
        if after is not None: p.paragraph_format.space_after = Pt(after)
        if before is not None: p.paragraph_format.space_before = Pt(before)
        if keep: keep_next(p)
        return p
    def bullet(self, text, numbered=False, container=None, color=None, level=0):
        cont = container or self.doc
        p = cont.add_paragraph()
        pf = p.paragraph_format; pf.left_indent = Mm(4.5 + 4*level); pf.first_line_indent = Mm(-3.5); pf.space_after = Pt(2.2)
        pf.line_spacing = 1.12
        if numbered:
            m = re.match(r'(\d+)\.\s+(.*)', text); num, text = m.group(1), m.group(2)
            r = p.add_run(num + ".\t"); r.bold = True; r.font.color.rgb = rgb(color or TEAL)
            pf.left_indent = Mm(5.5 + 4*level); pf.first_line_indent = Mm(-4.5)
            pf.tab_stops.add_tab_stop(Mm(5.5 + 4*level))
        else:
            r = p.add_run("•\t"); r.font.color.rgb = rgb(color or TEAL); r.bold = True
            pf.tab_stops.add_tab_stop(Mm(4.5 + 4*level))
        add_runs(p, text, color=None if color is None or color in (TEAL,) else color)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        return p
    def heading(self, text, level):
        p = self.doc.add_heading(level=level); add_runs(p, text)
        return p
    def chapter_opener(self, num, title, running):
        self.chap = num; self.running = running; self.heads.append(('chap', f'CHAPITRE {num}', f'{num}. {title}'))
        self.new_section(f"Chapitre {num} · {running}", first_number=False)
        p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        anchor_picture(p, os.path.join(ROOT, "illustrations", "design", f"bandeau_ch{num:02d}.jpg"), 148, 64, 0, 0)
        add_runs(p, f"CHAPITRE {num}", size=8.5, color=TEAL, bold=True, font=TITLE_FONT)
        p.paragraph_format.space_before = Pt(144); p.paragraph_format.space_after = Pt(3); keep_next(p)
        p2 = self.doc.add_heading(level=1); add_runs(p2, title)
        self._rule(TEAL, 18, 22, after=10)
    def _rule(self, color, sz, width_pct=100, after=8):
        p = self.doc.add_paragraph(); pPr = p._p.get_or_add_pPr(); bd = OxmlElement('w:pBdr'); bt = OxmlElement('w:bottom')
        bt.set(qn('w:val'), 'single'); bt.set(qn('w:sz'), str(sz)); bt.set(qn('w:color'), color); bt.set(qn('w:space'), '1'); bd.append(bt); pPr.append(bd)
        p.paragraph_format.space_after = Pt(after); p.paragraph_format.right_indent = Mm(TEXT_W_MM*(1-width_pct/100))
        r = p.add_run(""); r.font.size = Pt(2)
    def part_page(self, num, title, sub):
        self.heads.append(('part', f'PARTIE {num}', f'Partie {num} · {title}'))
        self.new_section("", blank_header=True, first_number=False)
        idx = {"I": 1, "II": 2, "III": 3, "IV": 4}[num]
        p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        anchor_picture(p, os.path.join(ROOT, "illustrations", "design", f"partie_{idx}.jpg"), 148, 210, 0, 0)
        add_runs(p, f"PARTIE {num}", size=11, color="5AD6C4", bold=True, font=TITLE_FONT); p.paragraph_format.space_before = Pt(40)
        p.paragraph_format.space_after = Pt(8)
        p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT; nohyph(p); add_runs(p, title, size=25, color=WHITE, font=DISPLAY_FONT)
        p.paragraph_format.line_spacing = 1.05; p.paragraph_format.space_after = Pt(12)
        self._rule("5AD6C4", 18, 22, after=12)
        for line in sub:
            p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT; nohyph(p)
            m = re.match(r'Chapitre (\d+)\. (.*)', line)
            if m:
                r = p.add_run(f"{int(m.group(1)):02d}  "); r.font.name = TITLE_FONT; r.font.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = rgb("5AD6C4")
                add_runs(p, m.group(2), size=10, color="D7E3F2")
            else: add_runs(p, line, size=10, color="D7E3F2")
            p.paragraph_format.space_after = Pt(5); p.paragraph_format.left_indent = Mm(8); p.paragraph_format.first_line_indent = Mm(-8)
    def box(self, kind, title, lines, keep=False):
        if kind == 'citation':
            p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.left_indent = Mm(10); p.paragraph_format.first_line_indent = Mm(-10)
            p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(10); p.paragraph_format.line_spacing = 1.12
            r = p.add_run("\u201c\t"); r.font.name = DISPLAY_FONT; r.font.size = Pt(34); r.font.color.rgb = rgb(TEAL); r.font.bold = True
            p.paragraph_format.tab_stops.add_tab_stop(Mm(10))
            add_runs(p, " ".join(l.strip() for l in lines if l.strip()), size=12.5, color=NAVY, italic=True, font=DISPLAY_FONT)
            for rr in p.runs[1:]: rr.font.size = Pt(12.5)
            if title:
                q = self.doc.add_paragraph(); q.alignment = WD_ALIGN_PARAGRAPH.LEFT; q.paragraph_format.left_indent = Mm(10)
                add_runs(q, title, size=8.5, color=TEAL, bold=True, font=TITLE_FONT); q.paragraph_format.space_after = Pt(10)
            return
        label, bg, bcol, bstyle, bsz, lcol = BOXES[kind]
        t = self.doc.add_table(rows=1, cols=1); c = t.rows[0].cells[0]; table_width(t, [TEXT_W_MM])
        set_cell_bg(c, bg); set_cell_margins(c, 90, 90, 150, 130)
        if bstyle == "left": set_cell_borders(c, left=('single', bsz, bcol))
        elif bstyle == "leftdash": set_cell_borders(c, left=('dashed', bsz, bcol), top=('dotted', 4, bcol), bottom=('dotted', 4, bcol), right=('dotted', 4, bcol))
        elif bstyle == "top": set_cell_borders(c, top=('single', bsz, bcol))
        elif bstyle == "all": set_cell_borders(c, top=('single', bsz, bcol), left=('single', bsz, bcol), bottom=('single', bsz, bcol), right=('single', bsz, bcol))
        else: set_cell_borders(c)
        p = c.paragraphs[0]
        txtcol = WHITE if kind == "action" else None
        if label:
            add_runs(p, label + (" · " + title if title else ""), size=7.8, color=lcol if kind != "action" else TEAL, bold=True, font=TITLE_FONT)
            p.paragraph_format.space_after = Pt(3)
            first = False
        else:
            first = True
        self._render_lines(lines, container=c, first_para=p if first else None, box=kind, txtcol=txtcol)
        if keep: no_split(t.rows[0])
        if kind != 'action':
            sp = self.doc.add_paragraph(); sp.paragraph_format.space_after = Pt(3); sp.paragraph_format.line_spacing = 0.6
    # ---------- tableaux --------------------------------------------------------
    def table(self, header, rows, widths=None, caption=None, align=None, bold_rows=(), total_rows=(), font_size=8.3, header_font=7.8, note=None):
        ncol = len(header)
        if widths is None:
            first = min(46, TEXT_W_MM * 0.42) if ncol > 2 else TEXT_W_MM*0.6
            rest = (TEXT_W_MM - first) / (ncol - 1); widths = [first] + [rest]*(ncol-1)
        else:
            s = sum(widths); widths = [w * TEXT_W_MM / s for w in widths]
        if caption:
            self.tab_n[self.chap] = self.tab_n.get(self.chap, 0) + 1
            cp = self.para(f"Tableau {self.chap}.{self.tab_n[self.chap]}. {caption}" if self.chap else f"Tableau. {caption}", size=8.3, color=NAVY, bold=True, after=2, keep=True)
        t = self.doc.add_table(rows=1+len(rows), cols=ncol); t.alignment = WD_TABLE_ALIGNMENT.CENTER
        table_width(t, widths)
        if align is None:
            align = ['l'] + ['r'] * (ncol-1)
        for i, h in enumerate(header):
            c = t.rows[0].cells[i]; set_cell_bg(c, NAVY); set_cell_margins(c, 40, 40, 60, 60); set_cell_borders(c)
            p = c.paragraphs[0]; p.style = self.doc.styles['TabTexte']; add_runs(p, h, size=header_font, color=WHITE, bold=True, font=TITLE_FONT)
            p.alignment = {'l': WD_ALIGN_PARAGRAPH.LEFT, 'r': WD_ALIGN_PARAGRAPH.RIGHT, 'c': WD_ALIGN_PARAGRAPH.CENTER}[align[i]]
            c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        repeat_header(t.rows[0]); no_split(t.rows[0])
        for ri, row in enumerate(rows):
            tr = t.rows[ri+1]; no_split(tr)
            is_total = ri in total_rows or (isinstance(row[0], str) and row[0].startswith(("Total", "TOTAL", "Solde", "Trésorerie nette")))
            for i in range(ncol):
                c = tr.cells[i]; set_cell_margins(c, 28, 28, 60, 60)
                v = row[i] if i < len(row) else ""
                bg = "E9EEF5" if is_total else (GREY if ri % 2 else WHITE)
                set_cell_bg(c, bg)
                set_cell_borders(c, bottom=('single', 2, "D5DCE6"), top=('single', 8, NAVY) if is_total else None)
                p = c.paragraphs[0]; p.style = self.doc.styles['TabTexte']
                add_runs(p, str(v), size=font_size, bold=True if (is_total or ri in bold_rows) else None)
                p.alignment = {'l': WD_ALIGN_PARAGRAPH.LEFT, 'r': WD_ALIGN_PARAGRAPH.RIGHT, 'c': WD_ALIGN_PARAGRAPH.CENTER}[align[i]]
                c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        # garder le tableau groupé si court
        if len(rows) <= 9:
            for row in t.rows[:-1]:
                for c in row.cells:
                    for p in c.paragraphs: keep_next(p)
        sp = self.para(note, size=7.8, color=MID, italic=True, after=6) if note else self.doc.add_paragraph()
        if not note: sp.paragraph_format.space_after = Pt(4); sp.paragraph_format.line_spacing = 0.7
    def figure(self, path, caption, width_mm=None):
        self.fig_n[self.chap] = self.fig_n.get(self.chap, 0) + 1
        p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; keep_next(p)
        p.paragraph_format.space_after = Pt(2); p.paragraph_format.space_before = Pt(4)
        p.add_run().add_picture(os.path.join(ROOT, path), width=Mm(width_mm or TEXT_W_MM))
        label = f"Figure {self.chap}.{self.fig_n[self.chap]}. " if self.chap else "Figure. "
        self.para(label + caption, style='Legende')
    # ---------- markup -------------------------------------------------------------
    def _render_lines(self, lines, container=None, first_para=None, box=None, txtcol=None):
        i = 0; cont = container or self.doc
        def P(text, **kw):
            nonlocal first_para
            if first_para is not None:
                p = first_para; first_para = None; add_runs(p, text, color=txtcol, **kw); return p
            p = cont.add_paragraph(); add_runs(p, text, color=txtcol, **kw); return p
        while i < len(lines):
            ln = lines[i].rstrip('\n')
            if not ln.strip(): i += 1; continue
            if ln.startswith('|'):
                tl = []
                while i < len(lines) and lines[i].startswith('|'): tl.append(lines[i].strip()); i += 1
                rows = [[c.strip() for c in r.strip('|').split('|')] for r in tl if not re.match(r'^\|[\s:\-|]+\|$', r)]
                if container is None:
                    widths = None; m = re.match(r'^\{w:([\d,\s.]+)\}(.*)', rows[0][0])
                    if m: widths = [float(x) for x in m.group(1).split(',')]; rows[0][0] = m.group(2)
                    align = ['l'] + ['r' if re.match(r'^[-\d\s.,%()+]+$', rows[1][k] if len(rows) > 1 and k < len(rows[1]) else '') else 'l' for k in range(1, len(rows[0]))]
                    self.table(rows[0], rows[1:], widths=widths, caption=self._pending_caption, align=align); self._pending_caption = None
                else:
                    self._mini_table(cont, rows)
                continue
            if ln.startswith('Table: '): self._pending_caption = ln[7:].strip(); i += 1; continue
            m = re.match(r'^(\s*)- (.*)', ln)
            if m:
                self._list_item(cont, m.group(2), False, txtcol, level=len(m.group(1))//2, first_para=first_para); first_para = None; i += 1; continue
            m = re.match(r'^(\s*)(\d+\.\s+.*)', ln)
            if m:
                self._list_item(cont, m.group(2), True, txtcol, level=len(m.group(1))//2, first_para=first_para); first_para = None; i += 1; continue
            m = re.match(r'^([a-d])\)\s+(.*)', ln)
            if m:
                opts = []
                while i < len(lines) and re.match(r'^([a-d])\)\s+(.*)', lines[i]):
                    mm = re.match(r'^([a-d])\)\s+(.*)', lines[i]); opts.append((mm.group(1), mm.group(2))); i += 1
                half = TEXT_W_MM/2
                pairs = [opts[k:k+2] for k in range(0, len(opts), 2)] if max(len(o[1]) for o in opts) <= 40 else [[o] for o in opts]
                for pi, pr in enumerate(pairs):
                    p = cont.add_paragraph(); pf = p.paragraph_format; pf.left_indent = Mm(5); pf.first_line_indent = Mm(-4)
                    pf.space_after = Pt(1); pf.tab_stops.add_tab_stop(Mm(5)); pf.tab_stops.add_tab_stop(Mm(half)); pf.tab_stops.add_tab_stop(Mm(half+5))
                    for k, (L, txt) in enumerate(pr):
                        if k: p.add_run("\t")
                        r = p.add_run(L + ")\t"); r.bold = True; r.font.color.rgb = rgb(TEAL)
                        add_runs(p, txt, size=9.8)
                    if pi < len(pairs)-1: keep_next(p)
                    else: pf.space_after = Pt(5)
                continue
            if ln.startswith('Q') and re.match(r'^Q\d+\.', ln):
                m = re.match(r'^(Q\d+)\.\s*(.*)', ln)
                p = cont.add_paragraph(); p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(2); keep_next(p)
                r = p.add_run(m.group(1).replace('Q', 'Question ') + ". "); r.bold = True; r.font.color.rgb = rgb(NAVY); r.font.name = TITLE_FONT; r.font.size = Pt(8.8)
                add_runs(p, m.group(2)); i += 1; continue
            if ln.startswith('>>'):
                p = P(ln[2:].strip(), bold=True); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in p.runs: r.font.color.rgb = rgb(NAVY); r.font.size = Pt(11)
                i += 1; continue
            if box == 'prompt':
                p = P(ln, size=8.6); i += 1
                p.paragraph_format.space_after = Pt(2.5); p.paragraph_format.line_spacing = 1.08
                continue
            p = P(ln, size=self.small) if not box else P(ln, size=10 if box == 'action' else None); i += 1
            if box: p.paragraph_format.space_after = Pt(3)
            elif self.small: p.paragraph_format.space_after = Pt(3); p.paragraph_format.line_spacing = 1.1
        return first_para
    def _list_item(self, cont, text, numbered, txtcol, level=0, first_para=None):
        if first_para is not None and False: pass
        p = self.bullet(text, numbered=numbered, container=cont, color=TEAL if not txtcol else TEAL, level=level)
        if txtcol:
            for r in p.runs[1:]: r.font.color.rgb = rgb(txtcol)
    def _mini_table(self, cont, rows):
        ncol = len(rows[0]); t = cont.add_table(rows=len(rows), cols=ncol)
        w = (TEXT_W_MM - 12); widths = [w*0.5] + [w*0.5/(ncol-1)]*(ncol-1) if ncol > 1 else [w]
        table_width(t, widths)
        for ri, row in enumerate(rows):
            for ci in range(ncol):
                c = t.rows[ri].cells[ci]; set_cell_margins(c, 20, 20, 50, 50)
                set_cell_borders(c, bottom=('single', 2, "C9D1DC")); set_cell_bg(c, "E2E8F0" if ri == 0 else WHITE)
                p = c.paragraphs[0]; p.style = self.doc.styles['TabTexte']
                add_runs(p, row[ci] if ci < len(row) else "", size=8, bold=True if ri == 0 or row[0].startswith(('Total', 'Solde')) else None)
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT if ci == 0 or not re.match(r'^[-\d\s.,%()+]+$', row[ci] if ci < len(row) else '') else WD_ALIGN_PARAGRAPH.RIGHT
        cont.add_paragraph().paragraph_format.space_after = Pt(1)
    def render_file(self, path):
        lines = open(path, encoding='utf-8').read().split('\n')
        self._pending_caption = None
        i = 0; buf = []
        def flush():
            nonlocal buf
            if buf: self._render_lines(buf); buf = []
        while i < len(lines):
            ln = lines[i]
            if ln.startswith('%%'): i += 1; continue
            if ln.startswith(':::'):
                flush(); m = re.match(r':::(\w+)(!?)\s*(.*)', ln); kind, keep, title = m.group(1), m.group(2), m.group(3).strip()
                inner = []; i += 1
                while not lines[i].startswith(':::'): inner.append(lines[i]); i += 1
                i += 1; self.box(kind, title, inner, keep=bool(keep)); continue
            if ln.startswith('@'):
                flush(); self.directive(ln[1:].strip()); i += 1; continue
            if ln.startswith('### '): flush(); self.heading(ln[4:], 3); i += 1; continue
            if ln.startswith('## '): flush(); self.heading(ln[3:], 2); i += 1; continue
            buf.append(ln); i += 1
        flush()
    def directive(self, d):
        cmd, _, arg = d.partition(' '); args = [a.strip() for a in arg.split('|')] if arg else []
        if cmd == 'part': self.part_page(args[0], args[1], args[2:])
        elif cmd == 'chapter': self.chapter_opener(int(args[0]), args[1], args[2] if len(args) > 2 else args[1])
        elif cmd == 'section':
            self.chap = 0; self.running = args[0]; self.new_section(args[1] if len(args) > 1 else args[0], blank_header=False)
            if args[0] != 'Sommaire': self.heads.append(('sec', args[0], args[0]))
            p2 = self.doc.add_heading(level=1); add_runs(p2, args[0]); self._rule(TEAL, 18, 22, after=10)
        elif cmd == 'rawsection': self.chap = 0; self.new_section(args[0] if args else "", blank_header=not args, numbered=True)
        elif cmd == 'pagebreak': self.doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        elif cmd == 'figure': self.figure(args[0], args[1], float(args[2]) if len(args) > 2 else None)
        elif cmd == 'table':
            fn = getattr(T, args[0]); spec = fn()
            self.table(spec['header'], spec['rows'], widths=spec.get('widths'), caption=args[1] if len(args) > 1 else spec.get('caption'),
                       align=spec.get('align'), font_size=spec.get('size', 8.3), note=spec.get('note'), bold_rows=spec.get('bold', ()),
                       total_rows=spec.get('totals', ()))
        elif cmd == 'space': p = self.doc.add_paragraph(); p.paragraph_format.space_after = Pt(float(args[0]) if args else 12)
        elif cmd == 'fontsize': self.small = float(args[0]) if args and args[0] != 'reset' else None
        elif cmd == 'keyfigures': self.keyfigures(args)
        elif cmd == 'toc': self.toc()
        elif cmd == 'index': self.index()
        elif cmd == 'titlepage': self.titlepage()
        elif cmd == 'center':
            self.para(args[0], align=WD_ALIGN_PARAGRAPH.CENTER, size=float(args[1]) if len(args) > 1 else None,
                      color=NAVY, bold=len(args) > 2 and args[2] == 'b', font=TITLE_FONT if len(args) > 2 and args[2] == 'b' else None)
        else: raise ValueError(d)
    def keyfigures(self, args):
        pairs = list(zip(args[0::2], args[1::2])); n = len(pairs)
        t = self.doc.add_table(rows=1, cols=2*n-1); gap = 3; cw = (TEXT_W_MM - gap*(n-1)) / n
        table_width(t, [cw if i % 2 == 0 else gap for i in range(2*n-1)])
        for i, (num, lab) in enumerate(pairs):
            c = t.rows[0].cells[2*i]; set_cell_bg(c, GREY); set_cell_borders(c, top=('single', 18, TEAL)); set_cell_margins(c, 90, 90, 80, 80)
            p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.LEFT; add_runs(p, num, size=22, color=TEAL, bold=True, font=TITLE_FONT)
            p.paragraph_format.space_after = Pt(0); p.paragraph_format.line_spacing = 1.0
            q = c.add_paragraph(); q.alignment = WD_ALIGN_PARAGRAPH.LEFT; add_runs(q, lab, size=8.3, color=NAVY); q.paragraph_format.line_spacing = 1.0
            if i < n-1:
                g = t.rows[0].cells[2*i+1]; set_cell_borders(g)
        sp = self.doc.add_paragraph(); sp.paragraph_format.space_after = Pt(4)
    def titlepage(self):
        self.new_section("", blank_header=True, numbered=False)
        p = self.doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        anchor_picture(p, os.path.join(ROOT, "illustrations", "design", "bandeau_titre.jpg"), 148, 92, 0, 0)
        add_runs(p, "MANUEL PRATIQUE · ENTREPRISES & ASBL", size=8, color=TEAL, bold=True, font=TITLE_FONT)
        p.paragraph_format.space_before = Pt(226); p.paragraph_format.space_after = Pt(8)
        self.para("LA TRÉSO", size=32, color=NAVY, bold=True, font=TITLE_FONT, after=0, align=WD_ALIGN_PARAGRAPH.LEFT)
        self.para("SOUS CONTRÔLE", size=32, color=TEAL, bold=True, font=TITLE_FONT, after=8, align=WD_ALIGN_PARAGRAPH.LEFT)
        self._rule(TEAL, 18, 22, 12)
        self.para("Prenez les bonnes décisions financières, sans être expert-comptable.", size=14, color=NAVY, italic=True, font=DISPLAY_FONT, after=40, align=WD_ALIGN_PARAGRAPH.LEFT)
        self.para("Verdi Imbole", size=13, color=NAVY, bold=True, font=TITLE_FONT, after=2, align=WD_ALIGN_PARAGRAPH.LEFT)
        self.para("Auteur indépendant, auditeur financier et freelance", size=9.5, color=MID, after=0, align=WD_ALIGN_PARAGRAPH.LEFT)
    def toc(self):
        entries = PAGEMAP.get('toc', [])
        for kind, text, page in entries:
            p = self.doc.add_paragraph(); pf = p.paragraph_format; p.alignment = WD_ALIGN_PARAGRAPH.LEFT; nohyph(p)
            pf.tab_stops.add_tab_stop(Mm(10)); pf.tab_stops.add_tab_stop(Mm(TEXT_W_MM), alignment=2, leader=0)
            if kind == 'part':
                pf.space_before = Pt(5); pf.space_after = Pt(1.5)
                add_runs(p, text.upper().replace("·", " ·"), size=7.4, color=MID, bold=True, font=TITLE_FONT)
            elif kind == 'chap':
                m = re.match(r'(\d+)\. (.*)', text)
                pf.space_after = Pt(1.8); pf.left_indent = Mm(10); pf.first_line_indent = Mm(-10); pf.line_spacing = 1.0; pf.right_indent = Mm(0)
                r = p.add_run(f"{int(m.group(1)):02d}\t"); r.font.name = TITLE_FONT; r.font.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = rgb(TEAL)
                add_runs(p, m.group(2), size=9, color=NAVY)
                r = p.add_run("\t" + str(page)); r.font.size = Pt(9); r.font.color.rgb = rgb(MID); r.font.name = TITLE_FONT
            else:
                pf.space_after = Pt(1); pf.space_before = Pt(1); pf.left_indent = Mm(10); pf.line_spacing = 1.0
                add_runs(p, text, size=9, color=NAVY, font=DISPLAY_FONT)
                r = p.add_run("\t" + str(page)); r.font.size = Pt(9); r.font.color.rgb = rgb(MID); r.font.name = TITLE_FONT
        if not entries: self.para("[table des matières générée au second passage]")
    def index(self):
        entries = PAGEMAP.get('index', [])
        t = self.doc.add_table(rows=1, cols=2); table_width(t, [TEXT_W_MM/2, TEXT_W_MM/2])
        half = (len(entries)+1)//2
        for col, chunk in enumerate((entries[:half], entries[half:])):
            c = t.rows[0].cells[col]; set_cell_borders(c); set_cell_margins(c, 0, 0, 0, 90)
            first = True; letter = None
            for term, pages in chunk:
                L = term[0].upper().replace('É', 'E')
                if L != letter:
                    letter = L
                    p = c.paragraphs[0] if first else c.add_paragraph(); first = False
                    add_runs(p, L, size=9, color=TEAL, bold=True, font=TITLE_FONT); p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(1)
                p = c.add_paragraph(); p.paragraph_format.space_after = Pt(0.5); p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.left_indent = Mm(3); p.paragraph_format.first_line_indent = Mm(-3)
                add_runs(p, f"{term}, {', '.join(str(x) for x in pages)}", size=7.9)

ORDERS = {
 'pPr': "pStyle keepNext keepLines pageBreakBefore framePr widowControl numPr suppressLineNumbers pBdr shd tabs suppressAutoHyphens kinsoku wordWrap overflowPunct topLinePunct autoSpaceDE autoSpaceDN bidi adjustRightInd snapToGrid spacing ind contextualSpacing mirrorIndents suppressOverlap jc textDirection textAlignment textboxTightWrap outlineLvl divId cnfStyle rPr sectPr pPrChange",
 'tcPr': "cnfStyle tcW gridSpan hMerge vMerge tcBorders shd noWrap tcMar textDirection tcFitText vAlign hideMark",
 'tblPr': "tblStyle tblpPr tblOverlap bidiVisual tblStyleRowBandSize tblStyleColBandSize tblW jc tblCellSpacing tblInd tblBorders shd tblLayout tblCellMar tblLook",
 'settings': "writeProtection view zoom removePersonalInformation removeDateAndTime doNotDisplayPageBoundaries displayBackgroundShape printPostScriptOverText printFractionalCharacterWidth printFormsData embedTrueTypeFonts embedSystemFonts saveSubsetFonts saveFormsData mirrorMargins alignBordersAndEdges bordersDoNotSurroundHeader bordersDoNotSurroundFooter gutterAtTop hideSpellingErrors hideGrammaticalErrors activeWritingStyle proofState formsDesign attachedTemplate linkStyles stylePaneFormatFilter stylePaneSortMethod documentType mailMerge revisionView trackRevisions doNotTrackMoves doNotTrackFormatting documentProtection autoFormatOverride styleLockTheme styleLockQFSet defaultTabStop autoHyphenation consecutiveHyphenLimit hyphenationZone doNotHyphenateCaps showEnvelope summaryLength clickAndTypeStyle defaultTableStyle evenAndOddHeaders bookFoldRevPrinting bookFoldPrinting bookFoldPrintingSheets drawingGridHorizontalSpacing drawingGridVerticalSpacing displayHorizontalDrawingGridEvery displayVerticalDrawingGridEvery doNotUseMarginsForDrawingGridOrigin drawingGridHorizontalOrigin drawingGridVerticalOrigin doNotShadeFormData noPunctuationKerning characterSpacingControl printTwoOnOne strictFirstAndLastChars noLineBreaksAfter noLineBreaksBefore savePreviewPicture doNotValidateAgainstSchema saveInvalidXml ignoreMixedContent alwaysShowPlaceholderText doNotDemarcateInvalidXml saveXmlDataOnly useXSLTWhenSaving saveThroughXslt showXMLTags alwaysMergeEmptyNamespace updateFields hdrShapeDefaults footnotePr endnotePr compat docVars rsids mathPr attachedSchema themeFontLang clrSchemeMapping doNotIncludeSubdocsInStats doNotAutoCompressPictures forceUpgrade captions readModeInkLockDown smartTagType schemaLibrary shapeDefaults doNotEmbedSmartTags decimalSymbol listSeparator"}
ORDERS = {k: {n: i for i, n in enumerate(v.split())} for k, v in ORDERS.items()}
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
def reorder(root):
    for el in root.iter():
        tag = el.tag.replace(W, '') if isinstance(el.tag, str) else ''
        if tag in ORDERS:
            o = ORDERS[tag]; kids = list(el)
            # supprimer les doublons d'un même élément (on garde le dernier)
            seen = {}
            for k in kids: seen[k.tag] = k
            ln = lambda k: k.tag.split('}')[-1] if isinstance(k.tag, str) else ''
            keep = [k for k in kids if seen.get(k.tag) is k or ln(k) not in o]
            for k in kids: el.remove(k)
            for k in sorted(keep, key=lambda k: o.get(ln(k), 999)): el.append(k)
        if tag == 'zoom' and el.get(W + 'percent') is None: el.set(W + 'percent', '100')

if __name__ == "__main__":
    b = Builder()
    files = sorted(glob.glob(os.path.join(ROOT, "content", "*.md")))
    for f in files: b.render_file(f)
    out = os.path.join(ROOT, "livrables", "LA_TRESO_SOUS_CONTROLE.docx")
    b.doc.core_properties.author = "Verdi Imbole"; b.doc.core_properties.title = "La tréso sous contrôle"
    b.doc.core_properties.language = "fr-FR"
    reorder(b.doc.element); reorder(b.doc.settings.element); reorder(b.doc.styles.element)
    for sec in b.doc.sections:
        for hf in (sec.header, sec.even_page_header, sec.first_page_header, sec.footer, sec.even_page_footer, sec.first_page_footer):
            reorder(hf._element)
    b.doc.save(out); print(out)
    json.dump(b.heads, open(os.path.join(ROOT, 'build', 'headings.json'), 'w'), ensure_ascii=False)
