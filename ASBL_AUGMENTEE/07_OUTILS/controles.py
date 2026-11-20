#!/usr/bin/env python3
"""Contrôles automatisés du manuscrit (structure, QCM, fiches prompts, figures, références, placeholders)."""
import os, re, glob, csv, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MS = os.path.join(ROOT, "02_MANUSCRIT")
files = sorted(glob.glob(os.path.join(MS, "partie_*", "module_*.md")), key=lambda p: int(re.search(r"module_(\d+)", p).group(1)))
rep = {"modules": [], "alertes": []}

for f in files:
    t = open(f, encoding="utf-8").read()
    n = int(re.search(r"module_(\d+)", f).group(1))
    q = re.findall(r"^\*\*Q(\d+)\.\*\*", t, re.M)
    corr = re.findall(r"^\*\*Q(\d+) : ([a-d](?:, [a-d])*)\.\*\*", t, re.M)
    fiches = re.findall(r"^### Fiche (P[\d.]+)", t, re.M)
    fiche_ok = []
    for m in re.finditer(r"### Fiche (P[\d.]+).*?(?=\n### Fiche |\n## \d)", t, re.S):
        body = m.group(0)
        missing = [L for L in "ABCDEFGHIJK" if f"**{L}." not in body]
        fiche_ok.append((m.group(1), missing))
    opts_ok = True
    for m in re.finditer(r"^\*\*Q(\d+)\.\*\*.*?(?=^\*\*Q\d+\.\*\*|^## )", t, re.S | re.M):
        if len(re.findall(r"^[a-d]\) ", m.group(0), re.M)) != 4:
            opts_ok = False; rep["alertes"].append(f"M{n} Q{m.group(1)} : nombre d'options ≠ 4")
    rub = {
        "mise en situation": bool(re.search(r"Mise en situation", t)),
        "objectifs": "Objectifs d'apprentissage" in t,
        "notions": bool(re.search(r"Notions et définitions|Mode d'emploi", t)),
        "illustration": "![Figure" in t,
        "niveaux": bool(re.search(r"Solutions selon le niveau|Solutions par niveau|Niveau 1|niveau Débutant", t)),
        "prompts": bool(fiches) or n == 21,
        "contrôles humains": "Contrôle humain obligatoire" in t or n == 21,
        "risques": bool(re.search(r"Risques et erreurs", t)) or n == 21,
        "exercice": "Exercice" in t,
        "synthèse": "Synthèse" in t,
        "QCM": len(q) >= 10,
        "corrigé": len(corr) == len(q) and len(q) >= 10,
    }
    for k, v in rub.items():
        if not v:
            rep["alertes"].append(f"M{n} : rubrique manquante ou non détectée — {k}")
    for code, miss in fiche_ok:
        if miss:
            rep["alertes"].append(f"M{n} fiche {code} : rubriques manquantes {miss}")
    rep["modules"].append({"module": n, "mots": len(re.findall(r"\w+", t)), "questions": len(q), "corrigés": len(corr),
                           "fiches": fiches, "figures": len(re.findall(r"!\[Figure", t)), "options_ok": opts_ok})

# Figures référencées existantes
alltxt = "\n".join(open(p, encoding="utf-8").read() for p in glob.glob(os.path.join(MS, "**", "*.md"), recursive=True))
for p in re.findall(r"\]\((03_ILLUSTRATIONS/[^)]+)\)", alltxt):
    if not os.path.exists(os.path.join(ROOT, p)):
        rep["alertes"].append(f"Figure introuvable : {p}")
figs_used = set(re.findall(r"fig_[\d_]+\.svg", alltxt))
figs_all = {os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "03_ILLUSTRATIONS", "figures", "*.svg"))}
for x in sorted(figs_all - figs_used):
    rep["alertes"].append(f"Figure produite mais non utilisée : {x}")
# Placeholders résiduels hors prompts
noncode = re.sub(r"```.*?```", "", alltxt, flags=re.S)
for pat in ["TODO", "XXX", "Lorem", "[À COMPLÉTER PAR L'AUTEUR]", "TBD"]:
    if pat in noncode:
        rep["alertes"].append(f"Placeholder détecté : {pat}")
# Références citées en texte vs registre
reg = open(os.path.join(ROOT, "01_RECHERCHE_DOCUMENTAIRE", "sources_verifiees.csv"), encoding="utf-8").read()
for auteur in ["Vaswani", "Lewis", "Ji", "Bender", "Dell'Acqua", "Brynjolfsson", "Davis", "Venkatesh", "Sweller", "Marelli", "COSO", "NIST", "UNESCO", "OCDE", "ACFE", "WCAG", "OWASP", "INPAS", "CHS"]:
    if auteur in alltxt and auteur not in reg and auteur not in ("OCDE",):
        rep["alertes"].append(f"Référence citée absente du registre : {auteur}")
rep["total_mots_modules"] = sum(m["mots"] for m in rep["modules"])
rep["total_questions"] = sum(m["questions"] for m in rep["modules"])
rep["total_fiches"] = sum(len(m["fiches"]) for m in rep["modules"])
json.dump(rep, open(os.path.join(ROOT, "05_CONTROLE_QUALITE", "controles_automatiques.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in rep.items() if k != "modules"}, ensure_ascii=False, indent=1))
for m in rep["modules"]:
    print(m["module"], m["mots"], m["questions"], m["corrigés"], len(m["fiches"]), m["figures"], m["options_ok"])
