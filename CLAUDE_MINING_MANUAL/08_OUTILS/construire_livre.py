# -*- coding: utf-8 -*-
"""Assemble le manuscrit : registre des sources -> bibliographie/webographie,
concaténation des chapitres, DOCX (pandoc) puis PDF (LibreOffice).
Usage : python3 08_OUTILS/construire_livre.py [--sans-pdf] [--tome 1|2|3]"""
import csv, glob, os, re, subprocess, sys, zipfile, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "06_PRODUCTION_FINALE"
TMP = ROOT / "06_PRODUCTION_FINALE" / "_build"
sys.path.insert(0, str(ROOT / "08_OUTILS"))
from sources import SOURCES, CONSULTE  # noqa: E402

TITRE = "LA_MINE_AUGMENTEE"
AUTEUR = "Verdi Imbole"

# Découpage en trois tomes : numérotation continue des parties et des chapitres ;
# le glossaire (A) et la bibliographie (I) figurent dans chaque tome.
TOMES = {
    1: dict(romain="I", titre="Comprendre et maîtriser Claude", parties=["PARTIE_I", "PARTIE_II"],
            annexes="ACEHI", chapitres=range(1, 17)),
    2: dict(romain="II", titre="Claude dans les métiers et les processus miniers", parties=["PARTIE_III"],
            annexes="ABDI", chapitres=range(17, 33)),
    3: dict(romain="III", titre="Méthodes, gouvernance et mise en pratique", parties=["PARTIE_IV", "PARTIE_V", "PARTIE_VI"],
            annexes="AFGIJKLM", chapitres=range(33, 44)),
}
TOME_DES_ANNEXES = {l: [t for t, c in TOMES.items() if l in c["annexes"]] for l in "ABCDEFGHIJKLM"}
TOME_DU_CHAPITRE = {n: t for t, c in TOMES.items() for n in c["chapitres"]}

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

def ecrire_bibliographie(chemin, utilisees=None):
    """Annexe I : références classées APA, sans note liminaire. `utilisees` restreint aux sources citées dans le tome."""
    garder = lambda s_: utilisees is None or s_["id"] in utilisees
    biblio = sorted([s for s in SOURCES if s["cat"] == "B" and garder(s)], key=sort_key)
    web = sorted([s for s in SOURCES if s["cat"] == "W" and garder(s)], key=sort_key)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("## Annexe I. Bibliographie et webographie\n\n")
        for titre, lst in (("Bibliographie", biblio), ("Webographie", web)):
            if not lst: continue
            f.write(f"### {titre}\n\n")
            for s_ in lst:
                f.write(f"::: {{custom-style=\"Reference\"}}\n{apa_complete(s_)}\n:::\n\n")
    return len(biblio), len(web)

def generer_sources():
    etiquettes()
    d = ROOT / "05_BIBLIOGRAPHIE_WEBOGRAPHIE"; d.mkdir(exist_ok=True)
    nb, nw = ecrire_bibliographie(d / "BIBLIOGRAPHIE_WEBOGRAPHIE.md")
    with open(d / "REGISTRE_SOURCES.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["id", "categorie", "type", "citation_dans_le_texte", "reference_APA", "url", "doi", "date_consultation", "verification", "usage"])
        for s in SOURCES:
            w.writerow([s["id"], "Bibliographie" if s["cat"] == "B" else "Webographie", s["type"], "(" + s["_cite"] + ")", re.sub(r"[*]", "", s["_apa"]),
                        s["url"], s.get("doi", ""), CONSULTE,
                        "Consultation directe" if s["verif"] == "D" else "Recherche documentaire (accès direct indisponible)",
                        s.get("note", "")])
    with open(ROOT / "00_GESTION_PROJET" / "REGISTRE_SOURCES.md", "w", encoding="utf-8") as f:
        f.write("# Registre des sources vérifiées\n\n> Fichier généré automatiquement depuis `08_OUTILS/sources.py` : ne pas éditer à la main.\n\n")
        f.write(f"Date de consultation : {CONSULTE}. D = consultation directe ; R = recherche documentaire.\n\n")
        f.write("| ID | Cat. | Vérif. | Citation | Référence | URL | Usage |\n|---|---|---|---|---|---|---|\n")
        for s in SOURCES:
            f.write(f"| {s['id']} | {s['cat']} | {s['verif']} | ({s['_cite']}) | {s['_apa']} | {s['url']} | {s.get('note','')} |\n")
    print(f"Sources : {nb} bibliographie, {nw} webographie")

def fichiers_tome(t):
    """Liste ordonnée des fichiers d'un tome (« @BIBLIO » marque l'emplacement de l'Annexe I)."""
    m, cfg = ROOT / "01_MANUSCRIT", TOMES[t]
    files = sorted(glob.glob(str(m / "PARTIE_0_LIMINAIRES" / "*.md")))
    for p in cfg["parties"]:
        files += sorted(glob.glob(str(m / p / "*.md")))
    files.append(str(ROOT / "04_ANNEXES" / "00_ouverture_annexes.md"))
    for l in cfg["annexes"]:
        if l == "I": files.append("@BIBLIO")
        else: files += glob.glob(str(ROOT / "04_ANNEXES" / f"{l}_*.md"))
    return files

def renvois(txt, t):
    """Signale le tome des annexes et chapitres situés dans un autre tome."""
    def ann(m):
        l = m.group(2); ts = TOME_DES_ANNEXES[l]
        if t in ts: return m.group(0)
        suite = m.group(3)
        if suite.startswith(" ("): return f"{m.group(1)} {l} (tome {ts[0]}, "
        if suite.startswith(")"): return f"{m.group(1)} {l}, tome {ts[0]})"
        return f"{m.group(1)} {l} (tome {ts[0]}){suite}"
    txt = re.sub(r"\b([Aa]nnexe) ([A-M])\b( \(|\)|)", ann, txt)
    def chap(m):
        n = int(m.group(1)); tt = TOME_DU_CHAPITRE.get(n)
        if tt is None or tt == t: return m.group(0)
        if m.group(2) == ")": return f"chapitre {n}, tome {tt})"
        if m.group(2) == " (": return f"chapitre {n} (tome {tt}, "
        return f"chapitre {n} (tome {tt})"
    return re.sub(r"\bchapitre (\d+)\b(\)| \(|)", chap, txt)

def ouverture_annexes(txt, t):
    lignes = [l for l in txt.split("\n") if not re.match(r"^- Annexe ([A-M])\.", l)
              or re.match(r"^- Annexe ([A-M])\.", l).group(1) in TOMES[t]["annexes"]]
    return "\n".join(lignes)

def assembler_tome(t):
    TMP.mkdir(parents=True, exist_ok=True)
    index = {s["id"]: s for s in SOURCES}
    for s_ in SOURCES: s_.pop("_utilisee", None)
    cfg = TOMES[t]; parts = []; pos_biblio = None
    for fp in fichiers_tome(t):
        if fp == "@BIBLIO":
            pos_biblio = len(parts); parts.append(""); continue
        txt = Path(fp).read_text(encoding="utf-8")
        txt = txt.replace("{{TOME_ROMAIN}}", cfg["romain"]).replace("{{TITRE_TOME}}", cfg["titre"])
        if Path(fp).name == "00_ouverture_annexes.md": txt = ouverture_annexes(txt, t)
        txt = renvois(txt, t)
        txt = citer(txt, index, fp)
        parts.append(txt.strip() + "\n\n")
    utilisees = {s_["id"] for s_ in SOURCES if s_.get("_utilisee")}
    bib = TMP / f"bibliographie_tome{t}.md"
    nb, nw = ecrire_bibliographie(bib, utilisees)
    parts[pos_biblio] = bib.read_text(encoding="utf-8") + "\n\n"
    print(f"Tome {t} : {nb} références bibliographiques, {nw} ressources en ligne")
    combined = TMP / f"tome{t}.md"
    combined.write_text("".join(parts), encoding="utf-8")
    return combined

def pandoc_docx(md, docx):
    ref = TMP / "reference.docx"
    subprocess.run([sys.executable, str(ROOT / "08_OUTILS" / "creer_reference_docx.py"), str(ref)], check=True)
    cmd = ["pandoc", str(md), "-f", "markdown+fenced_divs+pipe_tables+grid_tables+implicit_figures+raw_attribute",
           "-o", str(docx), "--reference-doc", str(ref), "--lua-filter", str(ROOT / "08_OUTILS" / "filtre_manuel.lua"),
           "--resource-path", str(ROOT), "-M", "toc-title=Sommaire",
           "-M", "lang=fr-FR"]
    subprocess.run(cmd, check=True, cwd=str(ROOT))

def couverture_xml(doc, chemin, nom, idx):
    """Image pleine page ancrée au coin de la page, devant le texte (masque en-tête et folio)."""
    from docx.shared import Cm
    from docx.oxml import parse_xml
    rid, _ = doc.part.get_or_add_image(str(chemin))
    cx, cy = int(Cm(15.5)), int(Cm(23.5))
    return parse_xml(f'''<w:r xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
 xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
 xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
 xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:drawing>
<wp:anchor distT="0" distB="0" distL="0" distR="0" simplePos="0" relativeHeight="{251660000+idx}" behindDoc="0" locked="1" layoutInCell="1" allowOverlap="1">
<wp:simplePos x="0" y="0"/><wp:positionH relativeFrom="page"><wp:posOffset>0</wp:posOffset></wp:positionH>
<wp:positionV relativeFrom="page"><wp:posOffset>0</wp:posOffset></wp:positionV>
<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:wrapNone/>
<wp:docPr id="{90000+idx}" name="{nom}"/><wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>
<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic>
<pic:nvPicPr><pic:cNvPr id="{90000+idx}" name="{nom}"/><pic:cNvPicPr/></pic:nvPicPr>
<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>
<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>
</pic:pic></a:graphicData></a:graphic></wp:anchor></w:drawing></w:r>''')

def couvertures(doc, t):
    """1re de couverture en tête du livre, 4e de couverture en dernière page (sur page paire)."""
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    d = ROOT / "02_ILLUSTRATIONS" / "COUVERTURES"
    body = doc.element.body
    def para(*runs):
        p = OxmlElement("w:p")
        for r in runs: p.append(r)
        return p
    def saut():
        r = OxmlElement("w:r"); br = OxmlElement("w:br"); br.set(qn("w:type"), "page"); r.append(br); return r
    # avant : couverture puis page blanche (verso) avant la page de titre
    body.insert(0, para(saut()))
    body.insert(0, para(couverture_xml(doc, d / f"tome{t}_couverture_avant.png", "Couverture", 1), saut()))
    # arrière : dernière page
    sect = body.find(qn("w:sectPr"))
    sect.addprevious(para(saut()))
    sect.addprevious(para(couverture_xml(doc, d / f"tome{t}_couverture_arriere.png", "Quatrieme de couverture", 2)))

def liminaires_sans_entete(doc):
    """Section distincte pour les pages liminaires (couverture, titre, mentions, sommaire) : ni titre courant ni folio."""
    import copy
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    body = doc.element.body
    cible = None
    for p in body.iter(qn("w:p")):
        st = p.find(qn("w:pPr") + "/" + qn("w:pStyle"))
        if st is not None and st.get(qn("w:val")) == "Heading2" and "Avant-propos" in "".join(t.text or "" for t in p.iter(qn("w:t"))):
            cible = p; break
    if cible is None: return
    ancre = cible
    while ancre.getprevious() is not None and ancre.getprevious().tag == qn("w:bookmarkStart"):
        ancre = ancre.getprevious()
    prev = OxmlElement("w:p"); ancre.addprevious(prev)   # paragraphe porteur du saut de section, après le sommaire
    def poser_type(sect, val):
        for e in sect.findall(qn("w:type")): sect.remove(e)
        t = OxmlElement("w:type"); t.set(qn("w:val"), val)
        sect.find(qn("w:pgSz")).addprevious(t)
    corps = body.find(qn("w:sectPr"))
    sect = copy.deepcopy(corps)
    for tag in ("w:headerReference", "w:footerReference", "w:titlePg"):
        for e in sect.findall(qn(tag)): sect.remove(e)
    poser_type(sect, "nextPage")
    pPr = prev.find(qn("w:pPr"))
    if pPr is None:
        pPr = OxmlElement("w:pPr"); prev.insert(0, pPr)
    pPr.append(sect)
    s0 = doc.sections[0]
    assert s0._sectPr is sect
    for hf in (s0.header, s0.even_page_header, s0.footer, s0.even_page_footer):
        hf.is_linked_to_previous = False
        for p in hf.paragraphs: p.text = ""
    poser_type(corps, "oddPage")   # le corps démarre sur une belle page

def post_traitement(docx, tome):
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
    INK, RULE = "1A1A1A", "8A5A2B"
    def bord(parent, tag, sides):
        old = parent.find(qn(tag))
        if old is not None: parent.remove(old)
        el = OxmlElement(tag)
        for side, (val, sz, col) in sides.items():
            e = OxmlElement(f"w:{side}"); e.set(qn("w:val"), val); e.set(qn("w:sz"), str(sz)); e.set(qn("w:space"), "0"); e.set(qn("w:color"), col)
            el.append(e)
        parent.append(el)
    nil = ("nil", 0, "auto")
    for t in doc.tables:
        tblPr = t._tbl.tblPr
        # filets « booktabs » : filet épais en haut et en bas, filet fin sous l'en-tête, aucune trame
        bord(tblPr, "w:tblBorders", {"top": ("single", 10, INK), "left": nil, "bottom": ("single", 10, INK),
                                      "right": nil, "insideH": ("single", 2, "D9D4CC"), "insideV": nil})
        for ri, row in enumerate(t.rows):
            if ri == 0:
                trPr = row._tr.get_or_add_trPr(); h = OxmlElement("w:tblHeader"); h.set(qn("w:val"), "true"); trPr.append(h)
            for cell in row.cells:
                tcPr = cell._tc.get_or_add_tcPr()
                for old in tcPr.findall(qn("w:shd")): tcPr.remove(old)
                if ri == 0:
                    bord(tcPr, "w:tcBorders", {"bottom": ("single", 6, RULE)})
                for p in cell.paragraphs:
                    pf = p.paragraph_format
                    pf.space_before = Pt(1.5); pf.space_after = Pt(1.5); pf.first_line_indent = Pt(0); pf.alignment = None
                    for r in p.runs:
                        r.font.size = Pt(8.5)
                        if ri == 0:
                            r.font.bold = False; r.font.small_caps = True; r.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
    liminaires_sans_entete(doc)
    couvertures(doc, tome)
    cp = doc.core_properties
    cp.title = f"La Mine augmentée. Tome {TOMES[tome]['romain']} : {TOMES[tome]['titre']}"
    cp.author = AUTEUR; cp.last_modified_by = AUTEUR; cp.language = "fr-FR"
    # demande à Word de mettre à jour le sommaire à l'ouverture
    settings = doc.settings.element
    uf = OxmlElement("w:updateFields"); uf.set(qn("w:val"), "true"); settings.append(uf)
    doc.save(str(docx))

def construire(t, sans_pdf=False):
    md = assembler_tome(t)
    OUT.mkdir(exist_ok=True)
    nom = f"{TITRE}_TOME_{t}"
    docx = OUT / f"{nom}.docx"
    pandoc_docx(md, docx)
    post_traitement(docx, t)
    mots = len(re.findall(r"\w+", md.read_text(encoding="utf-8")))
    print(f"DOCX : {docx} (environ {mots:,} mots)".replace(",", " "))
    if sans_pdf: return
    pdf = OUT / f"{nom}.pdf"
    exporter = lambda: subprocess.run(["/usr/bin/python3", str(ROOT / "08_OUTILS" / "maj_toc_pdf.py"), str(docx), str(pdf)], check=True)
    exporter()
    pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout).group(1))
    if pages % 2:
        # la 4e de couverture doit tomber sur une page paire (verso) : on ajoute une page blanche
        from docx import Document
        from docx.oxml import OxmlElement
        from docx.oxml.ns import qn
        d = Document(str(docx)); body = d.element.body
        dernier = body.find(qn("w:sectPr")).getprevious()
        p = OxmlElement("w:p"); r = OxmlElement("w:r"); br = OxmlElement("w:br"); br.set(qn("w:type"), "page")
        r.append(br); p.append(r); dernier.addprevious(p)
        d.save(str(docx)); exporter()

def main():
    sans_pdf = "--sans-pdf" in sys.argv
    tomes = [int(sys.argv[sys.argv.index("--tome") + 1])] if "--tome" in sys.argv else [1, 2, 3]
    generer_sources()
    for t in tomes:
        construire(t, sans_pdf)

if __name__ == "__main__":
    main()
