#!/usr/bin/env python3
"""Tests analytiques sur le fichier fictif de dépenses du RCE (module 13).

Usage : python3 tests_audit.py depenses.csv fournisseurs.csv [sortie.csv]
Seuil d'autorisation / de bon de commande : 1 000 UM (hypothèse du cas).
"""
import csv, sys, datetime
from collections import defaultdict

SEUIL = 1000.0
VAGUES = ("divers", "diverses", "prestation de services")


def load(p):
    with open(p, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=";"))


def main(dep_path, four_path, out=None):
    dep = load(dep_path)
    four = {r["code_fournisseur"] for r in load(four_path)}
    for r in dep:
        r["montant"] = float(r["montant"])
        r["d"] = datetime.date.fromisoformat(r["date"])
    flags = defaultdict(list)
    # T1 doublons : même fournisseur, même montant, même libellé
    seen = defaultdict(list)
    for r in dep:
        seen[(r["code_fournisseur"], r["montant"], r["libelle"].lower())].append(r["id"])
    for k, ids in seen.items():
        if len(ids) > 1:
            for i in ids:
                flags[i].append(f"T1 doublon potentiel ({'/'.join(ids)})")
    # T2 fournisseur hors base
    for r in dep:
        if r["code_fournisseur"] not in four:
            flags[r["id"]].append("T2 fournisseur absent du fichier fournisseurs")
    # T3 pièce manquante
    for r in dep:
        if r["piece_jointe"].strip().lower() != "oui":
            flags[r["id"]].append("T3 pièce justificative manquante")
    # T4 demandeur = approbateur
    for r in dep:
        if r["demandeur"] == r["approbateur"]:
            flags[r["id"]].append("T4 auto-approbation (demandeur = approbateur)")
    # T5 fractionnement : >=2 dépenses < seuil, même fournisseur, fenêtre 7 jours, cumul > seuil
    byf = defaultdict(list)
    for r in dep:
        if r["montant"] < SEUIL:
            byf[r["code_fournisseur"]].append(r)
    for f, rs in byf.items():
        rs.sort(key=lambda r: r["d"])
        for i, a in enumerate(rs):
            grp = [b for b in rs[i:] if (b["d"] - a["d"]).days <= 7]
            if len(grp) >= 2 and sum(b["montant"] for b in grp) > SEUIL:
                for b in grp:
                    m = f"T5 fractionnement possible ({'/'.join(x['id'] for x in grp)}, cumul {sum(x['montant'] for x in grp):.2f})"
                    if not any(x.startswith("T5") for x in flags[b["id"]]):
                        flags[b["id"]].append(m)
    # T6 montants ronds >= seuil (multiples de 500)
    for r in dep:
        if r["montant"] >= SEUIL and r["montant"] % 500 == 0:
            flags[r["id"]].append("T6 montant rond élevé")
    # T7 week-end
    for r in dep:
        if r["d"].weekday() >= 5:
            flags[r["id"]].append("T7 date de week-end")
    # T8 > seuil sans bon de commande
    for r in dep:
        if r["montant"] >= SEUIL and not r["bon_commande"].strip():
            flags[r["id"]].append("T8 montant ≥ seuil sans bon de commande")
    # T9 libellé vague
    for r in dep:
        if any(v in r["libelle"].lower() for v in VAGUES):
            flags[r["id"]].append("T9 libellé imprécis")
    total = sum(r["montant"] for r in dep)
    print(f"Population : {len(dep)} dépenses, total {total:.2f} UM")
    for t in ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9"]:
        ids = sorted({i for i, fl in flags.items() if any(x.startswith(t) for x in fl)})
        print(f"{t} : {len(ids)} -> {', '.join(ids)}")
    print(f"Opérations signalées (au moins un test) : {len(flags)}")
    rows = []
    for r in dep:
        if r["id"] in flags:
            rows.append([r["id"], r["date"], r["fournisseur"], f"{r['montant']:.2f}", r["approbateur"], " | ".join(flags[r["id"]])])
            print(" ", rows[-1])
    if out:
        with open(out, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["id", "date", "fournisseur", "montant", "approbateur", "alertes"])
            w.writerows(rows)


if __name__ == "__main__":
    main(*sys.argv[1:])
