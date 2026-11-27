#!/usr/bin/env python3
"""Couvertures avant et arrière (A4) : illustration vectorielle originale
d'un couloir de magasin d'archives en perspective, baigné d'une lumière chaude,
avec des feuillets qui s'envolent vers le lecteur. Sortie PDF + PNG.
Palette : marine, bleu pastel, moutarde, orange, bordeaux."""
import pathlib, random, subprocess, math
from weasyprint import HTML

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "03_ILLUSTRATIONS" / "couverture"
OUT.mkdir(parents=True, exist_ok=True)
NAVY, NAVYD, NAVY2 = "#0A1E3F", "#06132B", "#1F3A68"
PAST, PASTM, PASTL = "#BFD3EC", "#8FB4E0", "#DCE9F7"
MOUT, OCRE, ORANGE, BORD = "#D9A520", "#A8761A", "#E07B39", "#7B1E30"
CREAM = "#FFF4DC"
VP = (105, 92)  # point de fuite

def corridor(cx=VP[0], cy=VP[1], f=66, zmax=17, tint=1.0, seed=7):
    """Couloir d'archives : deux murs de rayonnages (x = ±1), boîtes colorées en façade."""
    rnd = random.Random(seed)
    P = lambda x, y, z: (cx + f * x / z, cy - f * y / z)
    def quad(pts, fill, op=1):
        d = "M" + " L".join(f"{a:.2f} {b:.2f}" for a, b in pts) + "Z"
        return f'<path d="{d}" fill="{fill}" opacity="{op:.2f}"/>'
    out = []
    out.append(quad([P(-1, -1, 1), P(1, -1, 1), P(1, -1, zmax), P(-1, -1, zmax)], "#0C1A36"))
    out.append(quad([P(-1, 1.7, 1), P(1, 1.7, 1), P(1, 1.7, zmax), P(-1, 1.7, zmax)], NAVYD))
    # reflet lumineux au sol
    out.append(quad([P(-0.35, -1, 1.2), P(0.35, -1, 1.2), P(0.05, -1, zmax), P(-0.05, -1, zmax)], "#F2C766", 0.22))
    for k in range(1, 10):
        z = 1 + k * 1.55
        a, b = P(-1, -1, z), P(1, -1, z)
        out.append(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{NAVY2}" stroke-width="0.25" opacity="0.7"/>')
    levels = [-0.95, -0.42, 0.11, 0.64, 1.17]
    warm = ["#E9D3A6", "#DDBF86", "#F1E0BC", "#CFAE72"]        # kraft
    cool = [PAST, PASTM, PASTL]                                  # bleu pastel
    accent = [MOUT, ORANGE, BORD, NAVY2]
    for side in (-1, 1):
        z = zmax; bays = []
        while z > 1.05:
            z0 = max(1.05, z - 1.1); bays.append((z0, z)); z = z0
        for z0, z1 in bays:
            depth_op = max(0.28, min(1, 3.4 / z1)) * tint
            for y in levels:
                zz = z0 + 0.03
                while zz < z1 - 0.06:
                    w = rnd.uniform(0.16, 0.26); hh = rnd.uniform(0.30, 0.42)
                    if zz + w > z1 - 0.03:
                        break
                    r = rnd.random()
                    col = rnd.choice(warm) if r < 0.45 else rnd.choice(cool) if r < 0.78 else rnd.choice(accent)
                    x = side * 0.995
                    out.append(quad([P(x, y, zz), P(x, y + hh, zz), P(x, y + hh, zz + w), P(x, y, zz + w)], col, depth_op))
                    if rnd.random() < 0.85:  # étiquette
                        ly = y + hh * 0.55
                        lab = "white" if col in accent else (BORD if col in warm else NAVY2)
                        out.append(quad([P(x, ly, zz + w * .22), P(x, ly + hh * .16, zz + w * .22), P(x, ly + hh * .16, zz + w * .78), P(x, ly, zz + w * .78)], lab, depth_op * 0.9))
                    zz += w + rnd.uniform(0.01, 0.05)
                out.append(quad([P(side, y, z0), P(side * 0.9, y, z0), P(side * 0.9, y, z1), P(side, y, z1)], "#2B4776", depth_op))
                out.append(quad([P(side * 0.9, y - 0.03, z0), P(side * 0.9, y, z0), P(side * 0.9, y, z1), P(side * 0.9, y - 0.03, z1)], "#E7C77A", depth_op * 0.55))
            out.append(quad([P(side * 0.9, -1, z0), P(side * 0.9, 1.68, z0), P(side * 0.86, 1.68, z0), P(side * 0.86, -1, z0)], "#2A4A80", depth_op))
    for k in range(5, 16, 2):  # plafonniers
        a, b = P(-0.12, 1.69, k), P(0.12, 1.69, k + 0.9)
        out.append(f'<rect x="{a[0]:.2f}" y="{a[1]:.2f}" width="{b[0]-a[0]:.2f}" height="{max(0.3,b[1]-a[1]):.2f}" rx="0.3" fill="{CREAM}" opacity="{min(0.95, 2.2/k):.2f}"/>')
    return "\n".join(out)

def mix(c1, c2, t):
    a = [int(c1[i:i+2], 16) for i in (1, 3, 5)]; b = [int(c2[i:i+2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02X}" for x, y in zip(a, b))

def glow(cx=VP[0], cy=VP[1], R=78, n=48):
    """Lumière chaude par cercles translucides empilés (rendu identique sur tout moteur)."""
    stops = [(0.0, "#FFF8E6"), (0.08, "#FFE2A0"), (0.22, MOUT), (0.45, ORANGE), (0.75, BORD), (1.0, NAVY)]
    def col(t):
        for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
            if t <= t1:
                return mix(c0, c1, (t - t0) / (t1 - t0))
        return NAVY
    out = []
    for i in range(n, 0, -1):
        t = i / n
        r = R * t
        op = 0.025 + 0.13 * (1 - t) ** 2.4
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.2f}" fill="{col(t)}" opacity="{op:.3f}"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="3.2" fill="#FFF8E6" opacity="0.9"/><circle cx="{cx}" cy="{cy}" r="6.5" fill="#FFE7AE" opacity="0.35"/>')
    return "".join(out)

def rays(cx=VP[0], cy=VP[1]):
    """Faisceaux de lumière qui rayonnent depuis le fond du couloir."""
    out = []
    for i, ang in enumerate(range(-80, 261, 17)):
        a1, a2 = math.radians(ang), math.radians(ang + 5)
        R = 220
        out.append(f'<path d="M{cx} {cy} L{cx+R*math.cos(a1):.1f} {cy+R*math.sin(a1):.1f} L{cx+R*math.cos(a2):.1f} {cy+R*math.sin(a2):.1f} Z" fill="#F2C766" opacity="{0.07 if i % 2 else 0.045}"/>')
    return "".join(out)

def flying_pages(seed=3):
    """Feuillets qui s'échappent de la lumière vers le lecteur : le mouvement de la couverture."""
    rnd = random.Random(seed)
    out = []
    specs = [(118, 70, 7, -14, 0.55), (90, 64, 6, 18, 0.5), (130, 52, 9, 22, 0.7), (74, 48, 9, -26, 0.68),
             (146, 30, 12, -10, 0.85), (58, 26, 13, 12, 0.85), (160, 102, 8, 30, 0.6), (44, 96, 10, -20, 0.7),
             (100, 40, 7, 8, 0.6), (176, 60, 15, 16, 0.95), (30, 58, 15, -18, 0.95)]
    for x, y, s, rot, op in specs:
        w, h = s, s * 1.32
        tab = rnd.choice([MOUT, ORANGE, BORD, PASTM, None, None])
        g = f'<g transform="translate({x} {y}) rotate({rot})" opacity="{op}">'
        g += f'<rect x="{-w/2+0.5:.2f}" y="{-h/2+0.6:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{s*0.08:.2f}" fill="#000" opacity="0.25"/>'
        g += f'<rect x="{-w/2:.2f}" y="{-h/2:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{s*0.08:.2f}" fill="{CREAM if rnd.random()<0.6 else "#FFFFFF"}"/>'
        for k in range(4):
            ly = -h / 2 + h * (0.28 + k * 0.15)
            g += f'<line x1="{-w*0.32:.2f}" y1="{ly:.2f}" x2="{w*(0.32 if k<3 else 0.05):.2f}" y2="{ly:.2f}" stroke="{PASTM}" stroke-width="{s*0.045:.2f}" stroke-linecap="round"/>'
        if tab:
            g += f'<rect x="{-w/2:.2f}" y="{-h/2:.2f}" width="{w*0.42:.2f}" height="{h*0.13:.2f}" rx="{s*0.05:.2f}" fill="{tab}"/>'
        out.append(g + "</g>")
    return "".join(out)

def stripe(y, h, x0=0, x1=210):
    """Filet segmenté aux cinq couleurs de la palette."""
    cols = [NAVY2, PASTM, MOUT, ORANGE, BORD]
    w = (x1 - x0) / len(cols)
    return "".join(f'<rect x="{x0+i*w:.2f}" y="{y}" width="{w+0.05:.2f}" height="{h}" fill="{c}"/>' for i, c in enumerate(cols))

DEFS = f'''<defs>
<linearGradient id="bgv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{NAVYD}"/><stop offset="1" stop-color="{NAVY}"/></linearGradient>
<radialGradient id="glow" cx="{VP[0]}" cy="{VP[1]}" r="92" gradientUnits="userSpaceOnUse">
 <stop offset="0" stop-color="#FFF8E6" stop-opacity="1"/><stop offset="0.07" stop-color="#FFE2A0" stop-opacity="0.95"/>
 <stop offset="0.2" stop-color="{MOUT}" stop-opacity="0.6"/><stop offset="0.42" stop-color="{ORANGE}" stop-opacity="0.22"/>
 <stop offset="0.75" stop-color="{BORD}" stop-opacity="0.08"/><stop offset="1" stop-color="{NAVY}" stop-opacity="0"/></radialGradient>
<radialGradient id="ray" cx="{VP[0]}" cy="{VP[1]}" r="150" gradientUnits="userSpaceOnUse">
 <stop offset="0" stop-color="#FFE7AE" stop-opacity="0.55"/><stop offset="0.5" stop-color="{MOUT}" stop-opacity="0.12"/><stop offset="1" stop-color="{MOUT}" stop-opacity="0"/></radialGradient>
<linearGradient id="floorglow" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="{MOUT}" stop-opacity="0.05"/><stop offset="1" stop-color="#FFE7AE" stop-opacity="0.55"/></linearGradient>
<linearGradient id="side" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="{NAVYD}" stop-opacity="0.7"/><stop offset="0.28" stop-color="{NAVYD}" stop-opacity="0"/>
 <stop offset="0.72" stop-color="{NAVYD}" stop-opacity="0"/><stop offset="1" stop-color="{NAVYD}" stop-opacity="0.7"/></linearGradient>
<linearGradient id="top" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{NAVYD}" stop-opacity="0.85"/><stop offset="0.16" stop-color="{NAVYD}" stop-opacity="0"/></linearGradient>
<linearGradient id="panel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVYD}"/></linearGradient>
</defs>'''

FONTS = (ROOT / "06_MISE_EN_PAGE" / "livre.css").read_text().split(":root")[0]

def page(svg_body, overlay_html):
    return f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>{FONTS}
@page {{ size: 210mm 297mm; margin: 0; }} body {{ margin:0; }}
.pg {{ position: relative; width: 210mm; height: 297mm; overflow: hidden; background: {NAVY}; color: white; }}
.pg svg.bg {{ position:absolute; left:0; top:0; width:210mm; height:297mm; }}
.abs {{ position:absolute; }}
</style></head><body><div class="pg">
<svg class="bg" viewBox="0 0 210 297" xmlns="http://www.w3.org/2000/svg">{DEFS}<rect width="210" height="297" fill="url(#bgv)"/>{svg_body}</svg>
{overlay_html}</div></body></html>'''

def front():
    b = rays() + corridor() + glow() + flying_pages()
    # assombrissement des bords (vignettage) par bandes translucides
    for k in range(12):
        w = 2.2 * (k + 1)
        b += f'<rect x="0" y="0" width="{w:.1f}" height="200" fill="{NAVYD}" opacity="0.06"/><rect x="{210-w:.1f}" y="0" width="{w:.1f}" height="200" fill="{NAVYD}" opacity="0.06"/>'
        b += f'<rect x="0" y="0" width="210" height="{1.6*(k+1):.1f}" fill="{NAVYD}" opacity="0.06"/>'
    # ruban en biais tricolore puis panneau du titre
    b += f'<path d="M0 182 L210 156 L210 297 L0 297 Z" fill="{NAVY}"/>'
    b += f'<path d="M0 178.4 L210 152.4 L210 155.4 L0 181.4 Z" fill="{MOUT}"/>'
    b += f'<path d="M0 181.4 L210 155.4 L210 157.2 L0 183.2 Z" fill="{ORANGE}"/>'
    b += f'<path d="M0 183.2 L210 157.2 L210 158.6 L0 184.6 Z" fill="{BORD}"/>'
    b += stripe(0, 2.6) + stripe(294.4, 2.6)
    b += f'<rect x="20" y="268.6" width="3.2" height="3.2" rx="0.6" fill="{MOUT}"/>'
    html = f'''
<div class="abs" style="left:20mm;top:12mm;font:700 7.6pt Montserrat;letter-spacing:.42em;color:{MOUT}">MANUEL PROFESSIONNEL</div>
<div class="abs" style="right:20mm;top:12mm;font:600 7.6pt Montserrat;letter-spacing:.28em;color:{PASTL}">MÉTHODES · OUTILS · CAS PRATIQUES</div>
<div class="abs" style="left:20mm;top:199mm;width:172mm">
 <div style="font:800 38pt/1 Montserrat;letter-spacing:.005em;color:white;white-space:nowrap"><span style="font-weight:300;color:{PAST}">L'</span>ARCHIVISTIQUE</div>
 <div style="width:34mm;height:1.6mm;border-radius:1mm;background:{MOUT};margin:4.5mm 0 4mm"></div>
 <div style="font:600 13.5pt/1.3 Montserrat;letter-spacing:.07em;color:{PAST};text-transform:uppercase">Principes et pratiques du métier d'archiviste</div>
 <div style="font:italic 400 11.3pt/1.45 'Source Sans 3';color:#EAF1FA;margin-top:4.5mm;width:160mm">De la gestion des documents à la maîtrise des archives : les méthodes professionnelles pour <span style="color:{MOUT};font-weight:700;font-style:italic">organiser, protéger, retrouver et valoriser</span> l'information de toute organisation.</div>
</div>
<div class="abs" style="left:26mm;top:268mm;font:800 13.5pt Montserrat;letter-spacing:.24em;color:white">VERDI IMBOLE</div>
<div class="abs" style="right:20mm;top:269.5mm;font:600 7.2pt Montserrat;letter-spacing:.25em;color:{PASTM}">ÉDITION 2026</div>
'''
    return page(b, html)

def back():
    b = stripe(0, 2.6) + stripe(294.4, 2.6)
    # lueur chaude discrète en haut à droite, en écho à la couverture avant
    b = b.replace("</defs>", "")
    b = f'<defs><radialGradient id="glowb" cx="200" cy="10" r="70" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{MOUT}" stop-opacity="0.35"/><stop offset="0.5" stop-color="{ORANGE}" stop-opacity="0.1"/><stop offset="1" stop-color="{NAVY}" stop-opacity="0"/></radialGradient></defs>' + b
    # frise de rayonnages aux couleurs de la palette
    for lvl, y in enumerate((234, 243)):
        x = 0; k = lvl * 3
        while x < 210:
            w = 3 + (k * 7) % 4; h = 6 + (k * 5) % 4
            m = k % 9
            col = {0: MOUT, 3: ORANGE, 5: PASTM, 7: BORD}.get(m, "#1A3563")
            b += f'<rect x="{x:.1f}" y="{y-h}" width="{w}" height="{h}" rx="0.5" fill="{col}"/>'
            x += w + 0.8; k += 1
        b += f'<line x1="0" y1="{y}" x2="210" y2="{y}" stroke="{NAVY2}" stroke-width="0.6"/>'
    items = ["Comprendre les principes et le cycle de vie des archives",
             "Construire un plan de classement, coter, indexer et retrouver",
             "Conserver le papier et sécuriser le numérique (PDF/A, GED, sauvegardes)",
             "Fixer les durées de conservation et éliminer en toute légalité",
             "Maîtriser les risques et renforcer le contrôle interne",
             "Utiliser l'intelligence artificielle avec méthode et prudence",
             "Diagnostiquer, rédiger une politique et piloter un service d'archives"]
    sq_cols = [(MOUT, NAVY), (ORANGE, "white"), (BORD, "white"), (PASTM, NAVY)]
    li = "".join(f'<div style="position:relative;padding-left:9mm;min-height:5.6mm;margin-bottom:2.2mm"><div style="position:absolute;left:0;top:-0.4mm;width:5.6mm;height:5.6mm;line-height:5.6mm;text-align:center;background:{sq_cols[(i-1)%4][0]};color:{sq_cols[(i-1)%4][1]};border-radius:1.4mm;font:800 7.8pt/5.6mm Montserrat">{i}</div><div style="font:500 9.5pt/1.3 Montserrat;color:white;padding-top:.3mm">{t}</div></div>' for i, t in enumerate(items, 1))
    stats = [("10", "chapitres progressifs", MOUT), ("10", "cas pratiques corrigés", ORANGE), ("60", "questions de QCM expliquées", "#E07A8E"), ("10", "modèles réutilisables", PASTM)]
    st = "".join(f'<div style="width:37mm;background:rgba(31,58,104,.55);border-radius:2.6mm;border-top:1.2mm solid {c};padding:3mm 3mm 3.2mm"><div style="font:800 22pt/1 Montserrat;color:{c}">{n}</div><div style="font:600 7pt/1.3 Montserrat;letter-spacing:.05em;color:{PASTL};text-transform:uppercase;margin-top:1.6mm">{t}</div></div>' for n, t, c in stats)
    aud = "".join(f'<span style="display:inline-block;border:.3mm solid {PASTM};border-radius:3mm;padding:.2mm 2.6mm;margin:0 1.6mm 1.6mm 0;white-space:nowrap">{a}</span>' for a in ["Étudiants", "Assistants administratifs", "Secrétaires", "Comptables", "Responsables administratifs et financiers", "Responsables RH", "Dirigeants", "Responsables d'ASBL", "Agents des administrations", "Archivistes débutants", "Consultants"])
    html = f'''
<div class="abs" style="left:22mm;top:18mm;width:166mm">
 <div style="display:flex"><div style="flex:none;width:1.4mm;border-radius:.7mm;background:{MOUT};margin-right:5mm"></div>
 <div style="font:300 20pt/1.2 Montserrat;color:white">Vos documents vous protègent-ils,<br>ou vous <b style="font-weight:800;color:{MOUT}">exposent</b>-ils ?</div></div>
 <div style="font:400 10.6pt/1.5 'Source Sans 3';color:#EAF1FA;margin-top:6mm;text-align:justify">Une pièce introuvable le jour d'un audit, un contrat original égaré, des dossiers du personnel incomplets, des fichiers éparpillés sur dix ordinateurs : derrière ces situations se cache presque toujours l'absence d'une méthode. <b style="color:white">Ce manuel vous la donne.</b> Pas à pas, il vous conduit des principes fondamentaux de l'archivistique à la mise en place d'un véritable service d'archives, dans une entreprise, une ASBL ou une administration.</div>
 <div style="font:700 7.6pt Montserrat;letter-spacing:.35em;color:{MOUT};margin:7.5mm 0 3.8mm">VOUS APPRENDREZ À</div>
 {li}
 <div style="display:flex;gap:4mm;margin-top:6.5mm">{st}</div>
 <div style="font:400 10pt/1.45 'Source Sans 3';color:#EAF1FA;margin-top:6.5mm;text-align:justify">Un fil rouge suit une association fictive, l'<b style="color:{MOUT}">Organisation Horizon</b>, du désordre initial à un système d'archivage fonctionnel. Tableaux, schémas, modèles de registres, bordereau, procès-verbal, politique d'archivage, checklist de contrôle interne et prompts d'IA prêts à l'emploi : <b style="color:white">tout est conçu pour être appliqué dès demain.</b></div>
</div>
<div class="abs" style="left:22mm;top:194mm;width:166mm">
 <div style="font:700 7.6pt Montserrat;letter-spacing:.35em;color:{MOUT};margin-bottom:2.6mm">POUR QUI ?</div>
 <div style="font:500 8.4pt/1.75 Montserrat;color:white">{aud}</div>
</div>
<div class="abs" style="left:22mm;top:248mm;width:156mm;background:{NAVY2};border-radius:3.2mm;border-left:1.6mm solid {MOUT};padding:4.4mm 5.5mm">
 <div style="font:800 10pt Montserrat;letter-spacing:.2em;color:white">VERDI IMBOLE</div>
 <div style="font:400 9pt/1.45 'Source Sans 3';color:#EAF1FA;margin-top:1.5mm;text-align:justify">Auteur indépendant, auditeur financier et consultant freelance, il accompagne des ASBL et des entreprises dans l'implémentation d'outils d'intelligence artificielle, l'amélioration de la gouvernance et de la comptabilité, et le renforcement du contrôle interne.</div>
 <div style="font:700 8pt Montserrat;color:{MOUT};margin-top:2mm;letter-spacing:.05em">verdiimbole0@gmail.com</div>
</div>
<div class="abs" style="left:22mm;top:286.5mm;font:600 6.8pt Montserrat;letter-spacing:.25em;color:{PASTM}">PUBLICATION INDÉPENDANTE · ÉDITION 2026</div>
'''
    return page(b, html)

if __name__ == "__main__":
    for name, fn in (("couverture_avant", front), ("couverture_arriere", back)):
        h = fn()
        (OUT / f"{name}.html").write_text(h)
        HTML(string=h, base_url=str(ROOT / "06_MISE_EN_PAGE")).write_pdf(OUT / f"{name}.pdf")
        subprocess.run(["pdftoppm", "-r", "200", "-png", "-singlefile", str(OUT / f"{name}.pdf"), str(OUT / name)], check=True)
        print("ok", name)
