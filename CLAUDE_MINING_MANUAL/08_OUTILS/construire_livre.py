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

COURT = {  # auteur abrégé pour les citations dans le texte
    "Anthropic": "Anthropic", "Model Context Protocol": "Model Context Protocol",
    "National Institute of Standards and Technology": "NIST",
    "Organisation internationale de normalisation & Commission électrotechnique internationale": "ISO/IEC",
    "Parlement européen & Conseil de l'Union européenne": "Règlement (UE) 2024/1689",
    "UNESCO": "UNESCO", "OWASP Foundation": "OWASP",
    "International Council on Mining and Metals": "ICMM", "Global Tailings Review": "Global Tailings Review",
    "Programme des Nations Unies pour l'environnement": "PNUE",
    "Initiative pour la transparence dans les industries extractives": "ITIE",
    "Extractive Industries Transparency Initiative": "ITIE", "OCDE": "OCDE",
    "Organisation internationale du Travail": "OIT", "Société financière internationale": "SFI",
    "Banque mondiale": "Banque mondiale", "U.S. Geological Survey": "USGS",
    "Agence internationale de l'énergie": "AIE", "Joint Ore Reserves Committee": "JORC",
    "Committee for Mineral Reserves International Reporting Standards": "CRIRSCO",
    "Global Reporting Initiative": "GRI", "République démocratique du Congo": "RDC",
    "Intergovernmental Forum on Mining, Minerals, Metals and Sustainable Development": "IGF",
    "Organisation pour l'harmonisation en Afrique du droit des affaires": "OHADA",
}

def _parse(s):
    """Retourne (auteur_long, annee, date_complement, titre) depuis la chaîne APA."""
    apa = re.sub(r"\(s\.d\.-[a-z]+\)", "(s.d.)", s["apa"])
    m = re.match(r"^(.*?)\s\((s\.d\.|\d{4})(,[^)]*)?\)\.\s*(.*)$", apa)
    auteur, annee, cpl, reste = m.group(1), m.group(2), m.group(3) or "", m.group(4)
    return auteur.rstrip("."), annee, cpl, reste, apa

def _court(auteur):
    if auteur in COURT: return COURT[auteur]
    noms = re.findall(r"([A-ZÀ-Ý][\w'’\-]+), [A-Z]", auteur)
    if len(noms) >= 3 or "…" in auteur: return f"{noms[0]} et al."
    if len(noms) == 2: return f"{noms[0]} et {noms[1]}"
    return noms[0] if noms else auteur

def etiquettes():
    """Calcule pour chaque source l'étiquette de citation APA, avec suffixes a, b, c."""
    groupes = {}
    for s in SOURCES:
        auteur, annee, cpl, reste, apa = _parse(s)
        groupes.setdefault((auteur, annee), []).append((re.sub(r"[*_]", "", reste).lower(), s))
    lab = {}
    for (auteur, annee), lst in groupes.items():
        lst.sort()
        for i, (_, s) in enumerate(lst):
            lettres = "abcdefghijklmnopqrstuvwxyz"
            code = (lettres[i // 26 - 1] if i >= 26 else "") + lettres[i % 26]
            suf = "" if len(lst) == 1 else ("-" if annee == "s.d." else "") + code
            _, _, cpl, reste, apa = _parse(s)
            s["_annee"] = annee + suf
            s["_cite"] = f"{_court(auteur)}, {annee}{suf}"
            s["_apa"] = f"{auteur}. ({annee}{suf}{cpl}). {reste}" if not auteur.endswith(".") else f"{auteur} ({annee}{suf}{cpl}). {reste}"
            s["_apa"] = s["_apa"].replace("..", ".")
    return {s["id"]: s for s in SOURCES}

def citer(texte, index, fichier=""):
    """Remplace [@ID] / [@ID, p. 3] / [@ID1; @ID2] par (Auteur, année). Signale les clés inconnues."""
    def rep(m):
        parts = []
        for c in m.group(1).split(";"):
            c = c.strip().lstrip("@")
            cle, _, loc = c.partition(",")
            cle = cle.strip()
            if cle not in index:
                raise SystemExit(f"Citation inconnue [{cle}] dans {fichier}")
            index[cle]["_utilisee"] = True
            parts.append(index[cle]["_cite"] + (f",{loc}" if loc else ""))
        return "(" + " ; ".join(parts) + ")"
    return re.sub(r"\[(@[A-Za-z0-9\-]+(?:,[^\]@;]*)?(?:;\s*@[A-Za-z0-9\-]+(?:,[^\]@;]*)?)*)\]", rep, texte)

def sort_key(s):
    """Tri APA : auteur puis année puis titre (sans mise en forme)."""
    return re.sub(r"[*_]", "", s.get("_apa", s["apa"])).lower()

def apa_complete(s):
    ref = s.get("_apa", s["apa"])
    if s.get("doi"):
        ref += f" https://doi.org/{s['doi']}"
    else:
        ref += f" {s['url']}"
    if s["cat"] == "W" or not s.get("doi"):
        ref += f" (consulté le {CONSULTE})"
    return ref

def generer_sources():
    etiquettes()
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
        w.writerow(["id", "categorie", "type", "citation_dans_le_texte", "reference_APA", "url", "doi", "date_consultation", "verification", "usage"])
        for s in SOURCES:
            w.writerow([s["id"], "Bibliographie" if s["cat"] == "B" else "Webographie", s["type"], "(" + s["_cite"] + ")", re.sub(r"[*]", "", s["_apa"]),
                        s["url"], s.get("doi", ""), CONSULTE,
                        "Consultation directe" if s["verif"] == "D" else "Recherche documentaire (accès direct indisponible)",
                        s.get("note", "")])
    with open(ROOT / "00_GESTION_PROJET" / "REGISTRE_SOURCES.md", "w", encoding="utf-8") as f:
        f.write("# Registre des sources vérifiées\n\n> Fichier généré automatiquement depuis `08_OUTILS/sources.py` — ne pas éditer à la main.\n\n")
        f.write(f"Date de consultation : {CONSULTE}. D = consultation directe ; R = recherche documentaire.\n\n")
        f.write("| ID | Cat. | Vérif. | Citation | Référence | URL | Usage |\n|---|---|---|---|---|---|---|\n")
        for s in SOURCES:
            f.write(f"| {s['id']} | {s['cat']} | {s['verif']} | ({s['_cite']}) | {s['_apa']} | {s['url']} | {s.get('note','')} |\n")
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
    index = {s["id"]: s for s in SOURCES}
    parts = []
    for fp in files:
        txt = Path(fp).read_text(encoding="utf-8")
        txt = citer(txt, index, fp)
        parts.append(txt.strip() + "\n\n")
    non = [s["id"] for s in SOURCES if not s.get("_utilisee")]
    if non: print("Sources du registre non citées dans le texte :", ", ".join(non))
    combined = TMP / "manuscrit_complet.md"
    combined.write_text("".join(parts), encoding="utf-8")
    return combined

def pandoc_docx(md, docx):
    ref = TMP / "reference.docx"
    subprocess.run([sys.executable, str(ROOT / "08_OUTILS" / "creer_reference_docx.py"), str(ref)], check=True)
    cmd = ["pandoc", str(md), "-f", "markdown+fenced_divs+pipe_tables+grid_tables+implicit_figures+raw_attribute",
           "-o", str(docx), "--reference-doc", str(ref), "--lua-filter", str(ROOT / "08_OUTILS" / "filtre_manuel.lua"),
           "--resource-path", str(ROOT), "-M", "toc-title=Sommaire",
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
