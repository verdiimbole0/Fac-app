# -*- coding: utf-8 -*-
"""Petite bibliothèque de mise en page pour python-pptx (charte de la formation)."""
import os, re, hashlib
import cairosvg
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from content import *

HERE = os.path.dirname(os.path.abspath(__file__))
ICON_DIR = os.path.join(HERE, "assets", "icons")
CACHE = os.path.join(HERE, "build", "icons_png"); os.makedirs(CACHE, exist_ok=True)
TITLE_FONT = "Montserrat"; BODY_FONT = "Inter"

def rgb(h): return RGBColor.from_string(h)

def icon_png(name, color=NAVY, px=256, stroke=2):
    out = os.path.join(CACHE, f"{name}_{color}_{px}_{stroke}.png")
    if not os.path.exists(out):
        svg = open(os.path.join(ICON_DIR, name + ".svg"), encoding="utf-8").read()
        svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
        svg = svg.replace('stroke="currentColor"', f'stroke="#{color}"').replace('stroke-width="2"', f'stroke-width="{stroke}"')
        cairosvg.svg2png(bytestring=svg.encode(), write_to=out, output_width=px, output_height=px)
    return out

class Deck:
    def __init__(self):
        self.prs = Presentation()
        self.prs.slide_width = Inches(13.333); self.prs.slide_height = Inches(7.5)
        self.blank = self.prs.slide_layouts[6]
        self.notes = []
        self.count = 0

    # ------------------------------------------------------------ primitives
    def new(self, bg=WHITE):
        s = self.prs.slides.add_slide(self.blank)
        self.count += 1
        self.rect(s, 0, 0, 13.333, 7.5, fill=bg)
        return s

    def rect(self, s, x, y, w, h, fill=None, line=None, lw=1, shape=MSO_SHAPE.RECTANGLE, radius=None, shadow=False):
        sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
        if fill: sh.fill.solid(); sh.fill.fore_color.rgb = rgb(fill)
        else: sh.fill.background()
        if line: sh.line.color.rgb = rgb(line); sh.line.width = Pt(lw)
        else: sh.line.fill.background()
        if radius is not None and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
            sh.adjustments[0] = radius
        if not shadow:
            sp = sh._element.spPr
            ef = sp.makeelement(qn("a:effectLst"), {}); sp.append(ef)
        sh.text_frame.text = ""
        return sh

    def rrect(self, s, x, y, w, h, fill=WHITE, line=None, lw=1, radius=0.08):
        return self.rect(s, x, y, w, h, fill=fill, line=line, lw=lw, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=radius)

    def circle(self, s, x, y, d, fill=NAVY, line=None, text=None, color=WHITE, size=14, font=TITLE_FONT, bold=True):
        sh = self.rect(s, x, y, d, d, fill=fill, line=line, shape=MSO_SHAPE.OVAL)
        if text is not None:
            tf = sh.text_frame; tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
            r = p.add_run(); r.text = text; self._fmt(r, size, bold, color, font)
        return sh

    def _fmt(self, r, size, bold, color, font, italic=False):
        f = r.font; f.size = Pt(size); f.bold = bold; f.italic = italic; f.color.rgb = rgb(color); f.name = font
        rPr = r._r.get_or_add_rPr()
        for tag in ("a:latin", "a:ea", "a:cs"):
            el = rPr.find(qn(tag))
            if el is None: el = rPr.makeelement(qn(tag), {}); rPr.append(el)
            el.set("typeface", font)

    def text(self, s, x, y, w, h, content, size=16, color=INK, bold=False, font=BODY_FONT, align="l",
             anchor="t", spacing=1.1, italic=False, margin=0.02, bullets=False, para_space=4):
        """content: str (\n = paragraph) ou liste de paragraphes ; chaque paragraphe = str ou liste de runs
        (texte, dict(options)). Préfixe '•' pour puce."""
        tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        tf = tb.text_frame; tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(margin); tf.margin_top = tf.margin_bottom = Inches(0.01)
        tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}[anchor]
        bodyPr = tf._txBody.find(qn("a:bodyPr"))
        for c in list(bodyPr): bodyPr.remove(c)
        paras = content.split("\n") if isinstance(content, str) else content
        for i, para in enumerate(paras):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[align]
            p.line_spacing = spacing
            if i > 0: p.space_before = Pt(para_space)
            runs = para if isinstance(para, list) else [para]
            for run in runs:
                if isinstance(run, tuple): t, o = run
                else: t, o = run, {}
                r = p.add_run(); r.text = t
                self._fmt(r, o.get("size", size), o.get("bold", bold), o.get("color", color), o.get("font", font), o.get("italic", italic))
        return tb

    def icon(self, s, name, x, y, size, color=NAVY, stroke=2):
        return s.shapes.add_picture(icon_png(name, color, stroke=stroke), Inches(x), Inches(y), Inches(size), Inches(size))

    def icon_badge(self, s, name, x, y, d, bg=TEAL, color=WHITE, ratio=0.55):
        self.circle(s, x, y, d, fill=bg)
        isz = d * ratio
        self.icon(s, name, x + (d - isz) / 2, y + (d - isz) / 2, isz, color)

    def line(self, s, x1, y1, x2, y2, color=GOLD, w=1.5):
        c = s.shapes.add_connector(1, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
        c.line.color.rgb = rgb(color); c.line.width = Pt(w)
        return c

    def arrow(self, s, x, y, w, h, fill=GOLD):
        return self.rect(s, x, y, w, h, fill=fill, shape=MSO_SHAPE.RIGHT_ARROW)

    def set_notes(self, s, notes):
        s.notes_slide.notes_text_frame.text = notes

    # ------------------------------------------------------------ gabarits
    def header(self, s, kicker, title, chapter=None, dark=False):
        col = WHITE if dark else NAVY
        self.rect(s, 0.6, 0.55, 0.08, 0.95, fill=GOLD)
        self.text(s, 0.85, 0.5, 11.5, 0.35, kicker.upper(), size=11, color=GOLD if not dark else GOLD, bold=True, font=TITLE_FONT)
        self.text(s, 0.85, 0.8, 11.8, 0.8, title, size=27, color=col, bold=True, font=TITLE_FONT, spacing=1.0)

    def footer(self, s, dark=False):
        col = "8A96AB" if not dark else "9FB0CC"
        self.line(s, 0.6, 7.0, 12.73, 7.0, color="D9DEE7" if not dark else "2A4270", w=0.75)
        self.text(s, 0.6, 7.07, 8, 0.3, "IA & PROMPT ENGINEERING APPLIQUÉS AUX ENTREPRISES", size=8.5, color=col, bold=True, font=TITLE_FONT)
        self.text(s, 11.2, 7.07, 1.53, 0.3, str(self.count), size=9, color=col, bold=True, font=TITLE_FONT, align="r")

    def chat_window(self, s, x, y, w, h, title="Assistant IA"):
        self.rrect(s, x, y, w, h, fill=WHITE, line="D5DBE5", lw=1, radius=0.03)
        self.rect(s, x + 0.02, y + 0.02, w - 0.04, 0.42, fill=LIGHT)
        for i, c in enumerate(["E46A5E", "E9B949", "5BB974"]):
            self.circle(s, x + 0.2 + i * 0.22, y + 0.15, 0.13, fill=c)
        self.text(s, x + 0.9, y + 0.08, w - 1.2, 0.3, title, size=10, color=MUTED, bold=True, font=TITLE_FONT)

    def bubble_user(self, s, x, y, w, h, txt, size=11.5):
        self.rrect(s, x, y, w, h, fill=NAVY, radius=0.12)
        self.text(s, x + 0.18, y + 0.1, w - 0.36, h - 0.2, txt, size=size, color=WHITE, anchor="m")

    def bubble_ai(self, s, x, y, w, h, txt, size=11, mono=False):
        self.icon_badge(s, "sparkles", x, y, 0.38, bg=TEAL)
        self.rrect(s, x + 0.5, y, w - 0.5, h, fill=LIGHT, radius=0.06)
        self.text(s, x + 0.68, y + 0.1, w - 0.86, h - 0.2, txt, size=size, color=INK, anchor="t", spacing=1.05)
