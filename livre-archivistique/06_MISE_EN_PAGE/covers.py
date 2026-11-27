#!/usr/bin/env python3
"""Couvertures avant et arrière (A4) : illustration vectorielle originale
d'un couloir de magasin d'archives en perspective. Sortie PDF + PNG."""
import pathlib, random, subprocess
from weasyprint import HTML

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "03_ILLUSTRATIONS" / "couverture"
OUT.mkdir(parents=True, exist_ok=True)
NAVY, GOLD = "#0A1E3F", "#2D5A3B"
BORD, BORDV, BORDC, VC = "#7B1E30", "#A3364A", "#D98A98", "#8DBB9A"
random.seed(7)

def corridor(cx=105, cy=112, f=70, zmax=16, tint=1.0):
    """Couloir d'archives : deux murs de rayonnages (x = ±1), boîtes en façade."""
    P = lambda x, y, z: (cx + f * x / z, cy - f * y / z)
    def quad(pts, fill, op=1, stroke=None):
        d = "M" + " L".join(f"{a:.2f} {b:.2f}" for a, b in pts) + "Z"
        s = f' stroke="{stroke}" stroke-width="0.12"' if stroke else ""
        return f'<path d="{d}" fill="{fill}" opacity="{op:.2f}"{s}/>'
    out = []
    # sol et plafond
    out.append(quad([P(-1, -1, 1), P(1, -1, 1), P(1, -1, zmax), P(-1, -1, zmax)], "#1D2433"))
    out.append(quad([P(-1, 1.7, 1), P(1, 1.7, 1), P(1, 1.7, zmax), P(-1, 1.7, zmax)], "#06122A"))
    for k in range(1, 9):  # lignes de sol
        z = 1 + k * 1.6
        out.append(f'<line x1="{P(-1,-1,z)[0]:.2f}" y1="{P(-1,-1,z)[1]:.2f}" x2="{P(1,-1,z)[0]:.2f}" y2="{P(1,-1,z)[1]:.2f}" stroke="#1A3361" stroke-width="0.25" opacity="0.6"/>')
    out.append(f'<line x1="{P(0,-1,1)[0]}" y1="{P(0,-1,1)[1]}" x2="{P(0,-1,zmax)[0]}" y2="{P(0,-1,zmax)[1]}" stroke="{BORDC}" stroke-width="0.35" opacity="0.35"/>')
    levels = [-0.95, -0.42, 0.11, 0.64, 1.17]
    lvl_h = 0.47
    kraft = ["#C9D3E3", "#B9C3D6", "#DCE3EF", "#A9B6CC"]
    navy_box = ["#7B1E30", "#2D5A3B", "#14305C"]
    for side in (-1, 1):
        # montants et tablettes, du fond vers l'avant
        z = zmax
        bays = []
        while z > 1.05:
            z0 = max(1.05, z - 1.1)
            bays.append((z0, z))
            z = z0
        for z0, z1 in bays:
            depth_op = max(0.25, min(1, 3.2 / z1)) * tint
            for y in levels:
                # boîtes sur la tablette
                zz = z0 + 0.03
                while zz < z1 - 0.06:
                    w = random.uniform(0.16, 0.26)
                    hh = random.uniform(0.30, 0.42)
                    if zz + w > z1 - 0.03:
                        break
                    col = random.choice(kraft if random.random() < 0.55 else navy_box)
                    x = side * 0.995
                    out.append(quad([P(x, y, zz), P(x, y + hh, zz), P(x, y + hh, zz + w), P(x, y, zz + w)], col, depth_op))
                    if random.random() < 0.8:  # étiquette dorée
                        ly = y + hh * 0.55
                        out.append(quad([P(x, ly, zz + w * .22), P(x, ly + hh * .16, zz + w * .22), P(x, ly + hh * .16, zz + w * .78), P(x, ly, zz + w * .78)], "#D98A98" if col in kraft else GOLD, depth_op))
                    zz += w + random.uniform(0.01, 0.05)
                # tablette
                out.append(quad([P(side, y, z0), P(side * 0.9, y, z0), P(side * 0.9, y, z1), P(side, y, z1)], "#3A4E73", depth_op))
                out.append(quad([P(side * 0.9, y - 0.03, z0), P(side * 0.9, y, z0), P(side * 0.9, y, z1), P(side * 0.9, y - 0.03, z1)], "#9AA6BC", depth_op * 0.9))
            # montant vertical
            out.append(quad([P(side * 0.9, -1, z0), P(side * 0.9, 1.68, z0), P(side * 0.86, 1.68, z0), P(side * 0.86, -1, z0)], "#22457F", depth_op))
        # bandeau lumineux au plafond
    for k in range(5, 15, 2):
        a, b = P(-0.12, 1.69, k), P(0.12, 1.69, k + 0.9)
        out.append(f'<rect x="{a[0]:.2f}" y="{a[1]:.2f}" width="{b[0]-a[0]:.2f}" height="{max(0.3,b[1]-a[1]):.2f}" fill="#F2F4F7" opacity="{0.9*2/k:.2f}"/>')
    return "\n".join(out)

GRAD = f'''<defs>
<radialGradient id="glow" cx="105" cy="112" r="70" gradientUnits="userSpaceOnUse">
 <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.9"/><stop offset="0.18" stop-color="#B9C9BE" stop-opacity="0.45"/>
 <stop offset="0.55" stop-color="{NAVY}" stop-opacity="0"/></radialGradient>
<linearGradient id="shade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="{NAVY}" stop-opacity="0.55"/><stop offset="0.22" stop-color="{NAVY}" stop-opacity="0"/>
 <stop offset="0.5" stop-color="{NAVY}" stop-opacity="0.05"/><stop offset="0.64" stop-color="{NAVY}" stop-opacity="0.88"/><stop offset="1" stop-color="{NAVY}" stop-opacity="1"/></linearGradient>
<linearGradient id="side" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="{NAVY}" stop-opacity="0.65"/><stop offset="0.3" stop-color="{NAVY}" stop-opacity="0"/>
 <stop offset="0.7" stop-color="{NAVY}" stop-opacity="0"/><stop offset="1" stop-color="{NAVY}" stop-opacity="0.65"/></linearGradient>
</defs>'''

FONTS = (ROOT / "06_MISE_EN_PAGE" / "livre.css").read_text().split(":root")[0]

def page(svg_body, overlay_html):
    return f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>{FONTS}
@page {{ size: 210mm 297mm; margin: 0; }} body {{ margin:0; }}
.pg {{ position: relative; width: 210mm; height: 297mm; overflow: hidden; background: {NAVY}; color: white; }}
.pg svg.bg {{ position:absolute; left:0; top:0; width:210mm; height:297mm; }}
.abs {{ position:absolute; }}
</style></head><body><div class="pg">
<svg class="bg" viewBox="0 0 210 297" xmlns="http://www.w3.org/2000/svg">{GRAD}<rect width="210" height="297" fill="{NAVY}"/>{svg_body}</svg>
{overlay_html}</div></body></html>'''

def front():
    body = corridor() + '<rect width="210" height="297" fill="url(#glow)"/><rect width="210" height="297" fill="url(#side)"/><rect width="210" height="297" fill="url(#shade)"/>'
    body += f'<path d="M0 172 L210 150 L210 297 L0 297 Z" fill="{NAVY}" opacity="0.93"/><path d="M0 172 L210 150" stroke="{BORDV}" stroke-width="1.1"/>'
    body += f'<rect x="0" y="0" width="210" height="3" fill="{BORD}"/><rect x="18" y="182" width="1.2" height="88" rx="0.6" fill="{BORDV}"/>'
    html = f'''
<div class="abs" style="left:18mm;top:14mm;font:700 7.5pt Montserrat;letter-spacing:.42em;color:{BORDC}">MANUEL PROFESSIONNEL</div>
<div class="abs" style="right:18mm;top:14mm;font:600 7.5pt Montserrat;letter-spacing:.3em;color:#C9D3E3">MÉTHODES · OUTILS · CAS PRATIQUES</div>
<div class="abs" style="left:25mm;top:184mm;width:170mm">
 <div style="font:200 41pt/1 Montserrat;letter-spacing:.02em;color:white">L'ARCHIVISTIQUE</div>
 <div style="font:600 14.5pt/1.3 Montserrat;letter-spacing:.06em;color:{VC};margin-top:5mm;text-transform:uppercase">Principes et pratiques<br>du métier d'archiviste</div>
 <div style="font:italic 400 11.5pt/1.45 'Source Sans 3';color:#E3E8EF;margin-top:6mm;width:150mm">De la gestion des documents à la maîtrise des archives : les méthodes professionnelles pour organiser, protéger, retrouver et valoriser l'information de toute organisation.</div>
</div>

<div class="abs" style="left:25mm;top:274mm;font:700 13pt Montserrat;letter-spacing:.22em;color:white">VERDI IMBOLE</div>
<div class="abs" style="right:18mm;top:276mm;font:500 7pt Montserrat;letter-spacing:.25em;color:#8A93A3">ÉDITION 2026</div>
'''
    return page(body, html)

def back():
    body = f'<rect x="0" y="294" width="210" height="3" fill="{BORD}"/><rect x="18" y="20" width="1.2" height="40" rx="0.6" fill="{BORDV}"/>'
    # frise de rayonnages stylisés (comme les ouvertures de chapitre)
    x = 0; k = 0
    for lvl, y in enumerate((222, 232)):
        x = 0; k = lvl * 3
        while x < 210:
            w = 3 + (k * 7) % 4; h = 6 + (k * 5) % 4
            col = (BORD if k % 2 else GOLD) if k % 11 == 0 else "#173563"
            body += f'<rect x="{x:.1f}" y="{y-h}" width="{w}" height="{h}" fill="{col}"/>'
            x += w + 0.8; k += 1
        body += f'<line x1="0" y1="{y}" x2="210" y2="{y}" stroke="#22457F" stroke-width="0.5"/>'
    items = ["Comprendre les principes et le cycle de vie des archives",
             "Construire un plan de classement, coter, indexer et retrouver",
             "Conserver le papier et sécuriser le numérique (PDF/A, GED, sauvegardes)",
             "Fixer les durées de conservation et éliminer en toute légalité",
             "Maîtriser les risques et renforcer le contrôle interne",
             "Utiliser l'intelligence artificielle avec méthode et prudence",
             "Diagnostiquer, rédiger une politique et piloter un service d'archives"]
    li = "".join(f'<div style="display:flex;align-items:flex-start;margin-bottom:2.3mm"><span style="flex:none;width:5.2mm;height:5.2mm;line-height:5.2mm;text-align:center;background:{BORD};color:white;border-radius:1.2mm;font:800 7.5pt Montserrat;margin-right:3mm">{i}</span><span style="font:500 9.4pt/1.35 Montserrat;color:white">{t}</span></div>' for i, t in enumerate(items, 1))
    stats = [("10", "chapitres progressifs"), ("10", "cas pratiques corrigés"), ("60", "questions de QCM expliquées"), ("10", "modèles réutilisables")]
    st = "".join(f'<div style="width:40mm"><div style="font:200 26pt/1 Montserrat;color:{VC}">{n}</div><div style="font:600 7.5pt/1.3 Montserrat;letter-spacing:.06em;color:#C9D3E3;text-transform:uppercase;margin-top:1.5mm">{t}</div></div>' for n, t in stats)
    html = f'''
<div class="abs" style="left:24mm;top:19mm;width:165mm">
 <div style="font:300 19pt/1.22 Montserrat;color:white">Vos documents vous protègent-ils,<br>ou vous exposent-ils ?</div>
 <div style="font:400 10.5pt/1.5 'Source Sans 3';color:#E3E8EF;margin-top:6mm;text-align:justify">Une pièce introuvable le jour d'un audit, un contrat original égaré, des dossiers du personnel incomplets, des fichiers éparpillés sur dix ordinateurs : derrière ces situations se cache presque toujours l'absence d'une méthode. Ce manuel vous la donne. Pas à pas, il vous conduit des principes fondamentaux de l'archivistique à la mise en place d'un véritable service d'archives, dans une entreprise, une ASBL ou une administration.</div>
 <div style="font:700 7.5pt Montserrat;letter-spacing:.35em;color:{BORDC};margin:8mm 0 4mm">VOUS APPRENDREZ À</div>
 {li}
 <div style="display:flex;gap:3mm;margin-top:7mm">{st}</div>
 <div style="font:400 10pt/1.45 'Source Sans 3';color:#E3E8EF;margin-top:7mm;text-align:justify">Un fil rouge suit une association fictive, l'<b style="color:white">Organisation Horizon</b>, du désordre initial à un système d'archivage fonctionnel. Tableaux, schémas, modèles de registres, bordereau, procès-verbal, politique d'archivage, checklist de contrôle interne et prompts d'IA prêts à l'emploi : tout est conçu pour être appliqué dès demain.</div>
</div>
<div class="abs" style="left:24mm;top:242mm;width:162mm;background:rgba(20,48,92,.95);border-top:.8mm solid {BORDV};border-radius:3mm;padding:4.5mm 5mm">
 <div style="font:700 10pt Montserrat;letter-spacing:.18em;color:white">VERDI IMBOLE</div>
 <div style="font:400 9pt/1.45 'Source Sans 3';color:#E3E8EF;margin-top:1.5mm;text-align:justify">Auteur indépendant, auditeur financier et consultant freelance, il accompagne des ASBL et des entreprises dans l'implémentation d'outils d'intelligence artificielle, l'amélioration de la gouvernance et de la comptabilité, et le renforcement du contrôle interne.</div>
 <div style="font:600 8pt Montserrat;color:{VC};margin-top:2mm;letter-spacing:.05em">verdiimbole0@gmail.com</div>
</div>
<div class="abs" style="left:24mm;top:283mm;font:500 6.8pt Montserrat;letter-spacing:.25em;color:#8A93A3">PUBLICATION INDÉPENDANTE · ÉDITION 2026</div>
'''
    return page(body, html)

if __name__ == "__main__":
    for name, fn in (("couverture_avant", front), ("couverture_arriere", back)):
        h = fn()
        src = OUT / f"{name}.html"
        src.write_text(h)
        HTML(string=h, base_url=str(ROOT / "06_MISE_EN_PAGE")).write_pdf(OUT / f"{name}.pdf")
        subprocess.run(["pdftoppm", "-r", "200", "-png", "-singlefile", str(OUT / f"{name}.pdf"), str(OUT / name)], check=True)
        print("ok", name)
