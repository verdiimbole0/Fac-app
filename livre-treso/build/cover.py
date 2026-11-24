"""Couvertures : 1re de couverture, 4e de couverture, dos, et maquette d'impression complète."""
import os, sys, math, subprocess
from PIL import Image, ImageDraw, ImageFilter, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from visuals import *
LIV = os.path.join(ROOT, "livrables", "couverture"); os.makedirs(LIV, exist_ok=True)
BLEED = 3; W_MM, H_MM = 148 + 2 * BLEED, 210 + 2 * BLEED
W, H = int(W_MM * MM), int(H_MM * MM)
def px(mm): return int(mm * MM)

def wrap(d, text, f, maxw):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for word in para.split(" "):
            t = (cur + " " + word).strip()
            if d.textlength(t, font=f) <= maxw: cur = t
            else: lines.append(cur); cur = word
        lines.append(cur)
    return lines
def text_block(d, xy, text, f, fill, maxw, lh=1.28):
    x, y = xy
    for l in wrap(d, text, f, maxw): d.text((x, y), l, font=f, fill=fill); y += f.size * lh
    return y
def spaced(d, xy, text, f, fill, sp):
    x, y = xy
    for ch in text: d.text((x, y), ch, font=f, fill=fill); x += d.textlength(ch, font=f) + sp
    return x
def fit_font(d, name, text, maxw, start):
    s = start
    while d.textlength(text, font=font(name, s)) > maxw: s -= 2
    return font(name, s)
def shade(img, box, top_alpha=200, bottom_alpha=0):
    x0, y0, x1, y1 = box; lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for y in range(y0, y1):
        a = int(top_alpha + (bottom_alpha - top_alpha) * (y - y0) / max(1, y1 - y0)); d.line([(x0, y), (x1, y)], fill=DEEP + (a,))
    return Image.alpha_composite(img.convert("RGBA"), lay)

def background(seed, dial_c, dial_r, sky_h=0.36):
    rnd = random.Random(seed)
    img = gradient(W, H, cx=0.32, cy=0.22)
    img = grid(img, px(10), alpha=15)
    img = digits(img, (0, H * 0.42, W, H * 0.9), seed=seed, alpha=20, size=30)
    img = dial(img, dial_c, dial_r, alpha=60)
    vals = [rnd.uniform(0.25, 1.0) * (0.7 + 0.6 * i / 26) for i in range(26)]
    img = skyline(img, H + 2, H * sky_h, vals, -40, W + 40, seed=seed * 3, alpha=240)
    return img

def control_arc(img, c, r, a0, a1, width=26):
    def fn(d): d.arc([c[0] - r, c[1] - r, c[0] + r, c[1] + r], a0, a1, fill=TEAL_L + (255,), width=width)
    return glow(img, fn, radius=24, strength=2)

def front():
    dc = (W * 0.97, H * 0.52); dr = W * 0.40
    img = background(7, dc, dr)
    img = control_arc(img, dc, dr * 0.91, 150, 215, width=22)
    # aiguille vers la zone maîtrisée
    def needle(d):
        a = math.radians(185); d.line([dc, (dc[0] + dr * 0.86 * math.cos(a), dc[1] + dr * 0.86 * math.sin(a))], fill=WHITE + (235,), width=10)
        d.ellipse([dc[0] - 22, dc[1] - 22, dc[0] + 22, dc[1] + 22], fill=TEAL_L + (255,))
    img = glow(img, needle, radius=10, strength=1)
    vals = [15, 9, 4, 11, 19, 16, 27, 24, 33, 30, 41, 46, 52, 57]
    pts = series_points(vals, W * 0.40, W * 0.82, H * 0.63, H * 0.86)
    img = trend(img, pts, width=11)
    tip = pts[-1]
    def arrow(d):
        x, y = tip; s = 46; d.polygon([(x + s * 1.2, y - s * 1.1), (x - s * 0.1, y - s * 0.75), (x + s * 0.65, y + s * 0.25)], fill=TEAL_L + (255,))
    img = glow(img, arrow, radius=14, strength=1)
    img = shade(img, (0, 0, W, int(H * 0.56)), 175, 0)
    d = ImageDraw.Draw(img); M = px(BLEED + 13); maxw = W - 2 * M
    spaced(d, (M, px(BLEED + 16)), "MANUEL PRATIQUE  ·  ENTREPRISES & ASBL", font("Montserrat-SemiBold.ttf", 34), TEAL_L + (255,), 5)
    f1 = fit_font(d, "Montserrat-ExtraBold.ttf", "SOUS CONTRÔLE", maxw, 260)
    f0 = font("Montserrat-ExtraBold.ttf", int(f1.size * 1.28))
    y = px(BLEED + 30)
    d.text((M - 6, y), "LA TRÉSO", font=f0, fill=WHITE + (255,)); y += f0.size * 1.02
    img = glow(img, lambda dd: dd.text((M - 4, y), "SOUS CONTRÔLE", font=f1, fill=TEAL + (255,)), radius=16, strength=1)
    d = ImageDraw.Draw(img); y += f1.size * 1.32
    d.rectangle([M, y, M + px(26), y + 9], fill=TEAL_L + (255,)); y += px(6)
    y = text_block(d, (M, y), "Prenez les bonnes décisions financières, sans être expert-comptable.", font("SourceSerif4-RegularItalic.ttf", 62), (235, 242, 250, 255), maxw * 0.86, 1.22)
    y += px(5)
    spaced(d, (M, y), "PRÉVOIR  ·  ENCAISSER  ·  SÉCURISER  ·  PILOTER", font("Montserrat-SemiBold.ttf", 30), (170, 200, 230, 255), 4)
    # pastille
    bc = (W * 0.22, H * 0.70); br = px(18)
    def badge(dd): dd.ellipse([bc[0] - br, bc[1] - br, bc[0] + br, bc[1] + br], fill=TEAL + (250,))
    img = glow(img, badge, radius=20, strength=1); d = ImageDraw.Draw(img)
    d.ellipse([bc[0] - br + 14, bc[1] - br + 14, bc[0] + br - 14, bc[1] + br - 14], outline=WHITE + (160,), width=3)
    for i, (t, fn_, sz) in enumerate([("10", "Montserrat-ExtraBold.ttf", 96), ("OUTILS EXCEL", "Montserrat-Bold.ttf", 25), ("+ 60 QCM", "Montserrat-Bold.ttf", 25), ("CORRIGÉS", "Montserrat-Bold.ttf", 25)]):
        f = font(fn_, sz); tw = d.textlength(t, font=f); yy = bc[1] - br * 0.62 + [0, 112, 146, 178][i]
        d.text((bc[0] - tw / 2, yy), t, font=f, fill=WHITE + (255,))
    # auteur
    img = shade(img, (0, int(H * 0.86), W, H), 0, 230); d = ImageDraw.Draw(img)
    spaced(d, (M, H - px(BLEED + 22)), "VERDI IMBOLE", font("Montserrat-Bold.ttf", 52), WHITE + (255,), 9)
    d.text((M, H - px(BLEED + 12)), "Auteur indépendant  ·  Auditeur financier", font=font("SourceSans3-Regular.ttf", 34), fill=(190, 210, 230, 255))
    return img.convert("RGB")

def back():
    dc = (W * 0.08, H * 0.80); img = background(11, dc, W * 0.42, sky_h=0.22)
    img = shade(img, (0, 0, W, int(H * 0.82)), 210, 120)
    d = ImageDraw.Draw(img); M = px(BLEED + 13); maxw = W - 2 * M; y = px(BLEED + 16)
    y = text_block(d, (M, y), "Vous vendez. Vous êtes rentable.\nAlors pourquoi l’argent\u00a0manque-t-il toujours\u00a0?", font("SourceSerif4-SemiBold.ttf", 66), WHITE + (255,), maxw, 1.18)
    d.rectangle([M, y + 18, M + px(22), y + 26], fill=TEAL_L + (255,)); y += px(9)
    body = ("MAKAO Distribution affiche 28 000 USD de bénéfice sur un trimestre… et ne peut plus payer ses fournisseurs. "
            "En suivant cette PME fictive de Kinshasa, de sa première alerte jusqu’à un dispositif complet, vous apprenez à reprendre "
            "le contrôle de votre trésorerie, pas à pas, avec des chiffres vérifiables et des outils prêts à l’emploi.")
    y = text_block(d, (M, y), body, font("SourceSans3-Regular.ttf", 38), (225, 233, 244, 255), maxw, 1.32) + px(4)
    d.text((M, y), "DANS CE LIVRE, VOUS APPRENDREZ À", font=font("Montserrat-Bold.ttf", 30), fill=TEAL_L + (255,)); y += px(6)
    items = ["construire un prévisionnel glissant sur 13 semaines et repérer le point bas ;",
             "faire rentrer l’argent plus vite et organiser vos paiements selon des priorités ;",
             "choisir le bon financement en calculant son coût réel ;",
             "sécuriser caisse, banque et paiements contre erreurs et fraudes ;",
             "piloter avec un tableau de bord d’une page et préparer un plan de crise ;",
             "gérer les fonds affectés d’une ASBL et utiliser l’IA sans perdre le contrôle."]
    fb = font("SourceSans3-Regular.ttf", 35)
    for it in items:
        d.ellipse([M, y + 12, M + 20, y + 32], fill=TEAL + (255,)); d.line([(M + 5, y + 22), (M + 9, y + 27), (M + 16, y + 16)], fill=WHITE + (255,), width=3)
        y = text_block(d, (M + 34, y), it, fb, WHITE + (255,), maxw - 34, 1.25) + 6
    y += px(4)
    # chiffres clés
    cw = (maxw - 3 * px(3)) / 4
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for i in range(4):
        x = M + i * (cw + px(3)); dl.rounded_rectangle([x, y, x + cw, y + px(19)], radius=18, fill=(255, 255, 255, 18), outline=TEAL + (190,), width=3)
    img = Image.alpha_composite(img, lay); d = ImageDraw.Draw(img)
    for i, (n, l) in enumerate([("12", "chapitres"), ("60", "QCM corrigés"), ("10", "outils Excel"), ("10", "prompts IA")]):
        x = M + i * (cw + px(3))
        f = font("Montserrat-ExtraBold.ttf", 84); tw = d.textlength(n, font=f); d.text((x + (cw - tw) / 2, y + 14), n, font=f, fill=TEAL_L + (255,))
        f2 = font("SourceSans3-SemiBold.ttf", 29); tw = d.textlength(l, font=f2); d.text((x + (cw - tw) / 2, y + px(13)), l, font=f2, fill=WHITE + (255,))
    y += px(25)
    d.text((M, y), "INCLUS", font=font("Montserrat-Bold.ttf", 30), fill=TEAL_L + (255,)); y += px(6)
    y = text_block(d, (M, y), "Un cas pratique fil rouge du diagnostic à la mission complète · 10 modèles Excel à formules · un plan d’action sur 90 jours · glossaire et index.",
                   font("SourceSans3-Regular.ttf", 35), WHITE + (255,), maxw, 1.3) + px(5)
    y = text_block(d, (M, y), "Pour les dirigeants de PME, responsables administratifs et financiers, comptables, trésoriers et responsables d’ASBL, gestionnaires de projets et étudiants.",
                   font("SourceSans3-Italic.ttf", 33) if os.path.exists(FD + "SourceSans3-Italic.ttf") else font("SourceSans3-RegularItalic.ttf", 33), (200, 215, 232, 255), maxw, 1.3)
    # auteur
    yb = H - px(BLEED + 34)
    d.line([(M, yb - px(3)), (W - M, yb - px(3))], fill=(255, 255, 255, 60), width=2)
    d.text((M, yb), "L’AUTEUR", font=font("Montserrat-Bold.ttf", 28), fill=TEAL_L + (255,))
    text_block(d, (M, yb + px(5)), "Verdi Imbole est auteur indépendant, auditeur financier et freelance. Il accompagne les entreprises et les ASBL "
               "dans leur gouvernance, leur comptabilité, leur contrôle interne et l’intégration de l’intelligence artificielle. Contact : verdiimbole0@gmail.com",
               font("SourceSans3-Regular.ttf", 31), (215, 226, 240, 255), maxw, 1.3)
    return img.convert("RGB")

def spine(pages):
    sw_mm = round(pages * 0.05 + 0.5, 1); sw = int(sw_mm * MM)
    img = Image.new("RGB", (sw, H), NAVY); d = ImageDraw.Draw(img)
    lay = Image.new("RGBA", (H, sw), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    f = font("Montserrat-ExtraBold.ttf", int(sw * 0.42)); fa = font("Montserrat-SemiBold.ttf", int(sw * 0.32))
    t1, t2 = "LA TRÉSO ", "SOUS CONTRÔLE"; x = px(BLEED + 18); yy = (sw - f.size) / 2 - sw * 0.05
    dl.text((x, yy), t1, font=f, fill=WHITE + (255,)); x += dl.textlength(t1, font=f); dl.text((x, yy), t2, font=f, fill=TEAL_L + (255,))
    ta = "VERDI IMBOLE"; dl.text((H - px(BLEED + 18) - dl.textlength(ta, font=fa), (sw - fa.size) / 2 - sw * 0.04), ta, font=fa, fill=(200, 215, 232, 255))
    img.paste(lay.rotate(-90, expand=True), (0, 0), lay.rotate(-90, expand=True))
    return img, sw_mm

def save_pdf(img, path):
    img.save(path, "PDF", resolution=DPI)

if __name__ == "__main__":
    pages = int(sys.argv[1]) if len(sys.argv) > 1 else 126
    fr, bk = front(), back(); sp, sw_mm = spine(pages)
    fr.save(os.path.join(LIV, "couverture_1_avant.jpg"), quality=95, dpi=(DPI, DPI)); save_pdf(fr, os.path.join(LIV, "couverture_1_avant.pdf"))
    bk.save(os.path.join(LIV, "couverture_4_arriere.jpg"), quality=95, dpi=(DPI, DPI)); save_pdf(bk, os.path.join(LIV, "couverture_4_arriere.pdf"))
    full = Image.new("RGB", (bk.width + sp.width + fr.width - 2 * px(BLEED), H), NAVY)
    full.paste(bk.crop((0, 0, bk.width - px(BLEED), H)), (0, 0)); full.paste(sp, (bk.width - px(BLEED), 0))
    full.paste(fr.crop((px(BLEED), 0, fr.width, H)), (bk.width - px(BLEED) + sp.width, 0))
    full.save(os.path.join(LIV, "couverture_complete_impression.jpg"), quality=95, dpi=(DPI, DPI)); save_pdf(full, os.path.join(LIV, "couverture_complete_impression.pdf"))
    # versions sans fond perdu pour la lecture numérique
    for im, n in ((fr, "avant"), (bk, "arriere")):
        im.crop((px(BLEED), px(BLEED), im.width - px(BLEED), im.height - px(BLEED))).save(os.path.join(OUT, f"cover_{n}_rogne.jpg"), quality=95, dpi=(DPI, DPI))
    print("dos (mm):", sw_mm, "largeur totale (mm):", round(full.width / MM, 1))
