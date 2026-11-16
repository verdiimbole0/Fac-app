# -*- coding: utf-8 -*-
"""Assemble le manuscrit : registre des sources -> bibliographie/webographie,
concaténation des chapitres, DOCX (pandoc) puis PDF (LibreOffice).
Usage : python3 08_OUTILS/construire_livre.py [--sans-pdf] [--partie PARTIE_I]"""
import csv, glob, os, re, subprocess, sys, zipfile, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "06_PRODUCTION_FINALE"
TMP = ROOT / "06_PRODUCTION_FINALE" / "_build"
sys.path.insert(0, str(ROOT / "08_OUTILS"))
from sources import SOURCES, CONSULTE  # noqa: E402

TITRE = "CLAUDE_ET_IA_INDUSTRIE_MINIERE"

def sort_key(s):
    """Tri APA : auteur puis année puis titre (sans mise en forme)."""
    return re.sub(r"[*_]", "", s["apa"]).lower()

def apa_complete(s):
    ref = s["apa"]
    if s.get("doi"):
        ref += f" https://doi.org/{s['doi']}"
    else:
        ref += f" {s['url']}"
    if s["cat"] == "W" or not s.get("doi"):
        ref += f" (consulté le {CONSULTE})"
    return ref

def generer_sources():
    d = ROOT / "05_BIBLIOGRAPHIE_WEBOGRAPHIE"; d.mkdir(exist_ok=True)
    biblio = sorted([s for s in SOURCES if s["cat"] == "B"], key=sort_key)
    web = sorted([s for s in SOURCES if s["cat"] == "W"], key=sort_key)
    with open(d / "BIBLIOGRAPHIE_WEBOGRAPHIE.md", "w", encoding="utf-8") as f:
        f.write("# Annexe I — Bibliographie et webographie vérifiées {#annexe-i}\n\n")
        f.write("Les références ci-dessous ont toutes été identifiées et contrôlées pendant la production de l'ouvrage "
                f"(consultations du {CONSULTE}). Elles sont présentées selon les normes APA (7e édition), adaptées au français. "
                "Le symbole ◆ signale une consultation directe du document ou de la page ; le symbole ◇ une référence dont "
                "l'existence, le titre, l'éditeur et l'adresse ont été confirmés par recherche documentaire, l'accès direct "
                "ayant été impossible depuis l'environnement de production (pare-feu, document payant ou norme commerciale). "
                "Le registre complet, avec la méthode de vérification et l'usage de chaque source, figure dans le fichier "
                "`REGISTRE_SOURCES.csv` livré avec le manuscrit.\n\n")
        f.write("## Bibliographie\n\n*Ouvrages, rapports institutionnels, normes, textes légaux et articles scientifiques.*\n\n")
        for s in biblio:
            f.write(f"- {'◆' if s['verif']=='D' else '◇'} {apa_complete(s)}\n")
        f.write("\n## Webographie\n\n*Documentations en ligne, centres d'aide, pages institutionnelles et annonces officielles.*\n\n")
        for s in web:
            f.write(f"- {'◆' if s['verif']=='D' else '◇'} {apa_complete(s)}\n")
    with open(d / "REGISTRE_SOURCES.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["id", "categorie", "type", "reference_APA", "url", "doi", "date_consultation", "verification", "usage"])
        for s in SOURCES:
            w.writerow([s["id"], "Bibliographie" if s["cat"] == "B" else "Webographie", s["type"], re.sub(r"[*]", "", s["apa"]),
                        s["url"], s.get("doi", ""), CONSULTE,
                        "Consultation directe" if s["verif"] == "D" else "Recherche documentaire (accès direct indisponible)",
                        s.get("note", "")])
    with open(ROOT / "00_GESTION_PROJET" / "REGISTRE_SOURCES.md", "w", encoding="utf-8") as f:
        f.write("# Registre des sources vérifiées\n\n> Fichier généré automatiquement depuis `08_OUTILS/sources.py` — ne pas éditer à la main.\n\n")
        f.write(f"Date de consultation : {CONSULTE}. D = consultation directe ; R = recherche documentaire.\n\n")
        f.write("| ID | Cat. | Vérif. | Référence | URL | Usage |\n|---|---|---|---|---|---|\n")
        for s in SOURCES:
            f.write(f"| {s['id']} | {s['cat']} | {s['verif']} | {s['apa']} | {s['url']} | {s.get('note','')} |\n")
    print(f"Sources : {len(biblio)} bibliographie, {len(web)} webographie")

def fichiers(partie=None):
    m = ROOT / "01_MANUSCRIT"
    ordre = ["PARTIE_0_LIMINAIRES", "PARTIE_I", "PARTIE_II", "PARTIE_III", "PARTIE_IV", "PARTIE_V", "PARTIE_VI"]
    files = []
    for p in ordre:
        if partie and p != partie and p != "PARTIE_0_LIMINAIRES": continue
        files += sorted(glob.glob(str(m / p / "*.md")))
    if not partie:
        files += sorted(glob.glob(str(ROOT / "04_ANNEXES" / "*.md")))
        files.append(str(ROOT / "05_BIBLIOGRAPHIE_WEBOGRAPHIE" / "BIBLIOGRAPHIE_WEBOGRAPHIE.md"))
    return files

def assembler(files):
    TMP.mkdir(parents=True, exist_ok=True)
    parts = []
    for fp in files:
        txt = Path(fp).read_text(encoding="utf-8")
        # chemins d'images relatifs à la racine du projet
        parts.append(txt.strip() + "\n\n")
    combined = TMP / "manuscrit_complet.md"
    combined.write_text("".join(parts), encoding="utf-8")
    return combined

def pandoc_docx(md, docx):
    ref = TMP / "reference.docx"
    subprocess.run([sys.executable, str(ROOT / "08_OUTILS" / "creer_reference_docx.py"), str(ref)], check=True)
    cmd = ["pandoc", str(md), "-f", "markdown+fenced_divs+pipe_tables+grid_tables+implicit_figures+raw_attribute",
           "-o", str(docx), "--reference-doc", str(ref), "--lua-filter", str(ROOT / "08_OUTILS" / "filtre_manuel.lua"),
           "--toc", "--toc-depth=2", "--resource-path", str(ROOT), "-M", "toc-title=Sommaire",
           "-M", "lang=fr-FR", "-M", "title=Claude et l'intelligence artificielle au service de l'industrie minière"]
    subprocess.run(cmd, check=True, cwd=str(ROOT))

def post_traitement(docx):
    from docx import Document
    from docx.shared import Pt, RGBColor
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    doc = Document(str(docx))
    # le titre pandoc (méta) est inutile : la page de titre est dans les liminaires
    body = doc.element.body
    for p in list(doc.paragraphs[:3]):
        if p.style.name in ("Title",):
            body.remove(p._p)
    for t in doc.tables:
        tbl = t._tbl
        tblPr = tbl.tblPr
        borders = OxmlElement("w:tblBorders")
        for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
            e = OxmlElement(f"w:{side}"); e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "4"); e.set(qn("w:color"), "B8C2CC")
            borders.append(e)
        old = tblPr.find(qn("w:tblBorders"))
        if old is not None: tblPr.remove(old)
        tblPr.append(borders)
        for ri, row in enumerate(t.rows):
            if ri == 0:
                trPr = row._tr.get_or_add_trPr(); h = OxmlElement("w:tblHeader"); h.set(qn("w:val"), "true"); trPr.append(h)
            for cell in row.cells:
                tcPr = cell._tc.get_or_add_tcPr()
                shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto")
                shd.set(qn("w:fill"), "0B2545" if ri == 0 else ("F4F6F9" if ri % 2 == 0 else "FFFFFF"))
                tcPr.append(shd)
                for p in cell.paragraphs:
                    p.paragraph_format.space_after = Pt(1); p.paragraph_format.alignment = None
                    for r in p.runs:
                        r.font.size = Pt(8.5)
                        if ri == 0:
                            r.font.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    # demande à Word de mettre à jour le sommaire à l'ouverture
    settings = doc.settings.element
    uf = OxmlElement("w:updateFields"); uf.set(qn("w:val"), "true"); settings.append(uf)
    doc.save(str(docx))

def main():
    sans_pdf = "--sans-pdf" in sys.argv
    partie = None
    if "--partie" in sys.argv: partie = sys.argv[sys.argv.index("--partie") + 1]
    generer_sources()
    files = fichiers(partie)
    md = assembler(files)
    OUT.mkdir(exist_ok=True)
    nom = TITRE if not partie else f"{TITRE}_{partie}"
    docx = OUT / f"{nom}.docx"
    pandoc_docx(md, docx)
    post_traitement(docx)
    print("DOCX :", docx)
    mots = len(re.findall(r"\w+", md.read_text(encoding="utf-8")))
    print(f"Fichiers : {len(files)} — environ {mots:,} mots".replace(",", " "))
    if not sans_pdf:
        pdf = OUT / f"{nom}.pdf"
        subprocess.run(["/usr/bin/python3", str(ROOT / "08_OUTILS" / "maj_toc_pdf.py"), str(docx), str(pdf)], check=True)

if __name__ == "__main__":
    main()
