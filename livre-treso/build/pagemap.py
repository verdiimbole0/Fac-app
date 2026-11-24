import json, os, re, subprocess, unicodedata
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "livrables", "LA_TRESO_SOUS_CONTROLE.pdf")
def norm(s):
    s = s.replace("’", " ").replace("'", " ")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()
n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout).group(1))
pages = [norm(subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), PDF, "-"], capture_output=True, text=True).stdout) for i in range(1, n+1)]
heads = json.load(open(os.path.join(ROOT, "build", "headings.json")))
toc = []; cur = 2
for kind, key, label in heads:
    k = norm(key)
    for p in range(cur, n+1):
        txt = pages[p-1]
        if (txt + " ").startswith(k + " "):
            toc.append((kind, label, p)); cur = p; break
    else:
        toc.append((kind, label, 0))
# index
TERMS = ["Affacturage", "Amortissement", "Avance opérationnelle", "Balance âgée", "Billetage", "Budget de trésorerie", "Caisse",
 "Chiffre d'affaires", "Compte courant d'associé", "Contrôle interne", "COSO", "Couverture", "Créance douteuse", "Crédit de trésorerie",
 "Découvert", "Double paiement", "DPO", "DSO", "Écart", "Escompte", "Excédent", "Facilité de caisse", "Flux de financement",
 "Flux d'exploitation", "Flux d'investissement", "Fonds affectés", "Fraude", "Hallucination", "IAS 7", "ISO 31000", "Monnaie électronique",
 "NIST", "Plan d'urgence", "Point bas", "Prévisionnel glissant", "Profil d'encaissement", "Prompt", "Rapprochement bancaire", "Relance",
 "Réserve de sécurité", "Risque de change", "Scénario", "Séparation des fonctions", "SYCEBNL", "SYSCOHADA", "Tableau de bord",
 "Taux de change", "Trésorerie nette", "Acompte", "ASBL", "Bailleur", "Budget", "Calendrier des paiements", "Charges fixes",
 "Créance client", "Décaissement", "Dette fournisseur", "Encaissement", "Excel", "Google Sheets", "Investissement", "Litige", "Matrice des risques",
 "OHADA", "Plafond", "Préfinancement", "Rapport de trésorerie", "Résultat", "Stock", "Subvention", "Tranche", "Validation", "Intelligence artificielle", "Anonymiser"]
first_body = next((p for k, l, p in toc if k == 'part'), 9); last_body = next((p for k, l, p in toc if l.startswith('Glossaire')), n)
index = []
for t in sorted(TERMS, key=lambda x: norm(x)):
    k = norm(t); found = []
    variants = [k, k + "s"] if not k.endswith("s") else [k]
    for p in range(first_body, last_body):
        if any(re.search(r"\b" + re.escape(v) + r"\b", pages[p-1]) for v in variants): found.append(p)
    if found:
        # compresser : garder au plus 7 pages
        index.append((t, found[:7]))
json.dump({"toc": toc, "index": index}, open(os.path.join(ROOT, "build", "pagemap.json"), "w"), ensure_ascii=False, indent=1)
print(n, "pages;", sum(1 for t in toc if t[2] == 0), "titres introuvables;", len(index), "entrées d'index")
for t in toc: print(t)
