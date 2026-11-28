# -*- coding: utf-8 -*-
"""Supprime les tirets cadratins (—) du texte en respectant le sens :
- « Chapitre 3 — Titre », « Figure 3.1 — Légende » ... -> « Chapitre 3. Titre »
- « **Libellé** — explication » -> « **Libellé** : explication »
- incise « a — b — c » -> « a, b, c »
- tiret isolé « a — b » -> « a : b » (ou « a, b » si la phrase contient déjà deux-points)
- cellule de tableau vide « | — | » -> « |  | »
Usage : python3 supprimer_tirets.py fichier.md [...]"""
import re, sys

LIB = r"(?:Chapitre|Figure|Tableau|Partie|PARTIE|Annexe|ANNEXE|Cas d'usage|Prompt|Exercice|Atelier|Étape|Étude de cas|Check-list)"

CONJ = r"(?:et|mais|ou|donc|car|puis|sinon|voire|y compris|surtout|notamment|sauf|même|si|ni|pas|sans|avant|après|parce|lorsque|quand|tant|à condition|avec|pour|en|dont|qui|que|afin|selon|plutôt|surtout)\b"

def ligne(l):
    if "—" not in l: return l
    l = re.sub(r"\|\s*—\s*(?=\|)", "|  ", l)                                        # cellule vide
    l = re.sub(rf"(\b{LIB}\s+[0-9IVXA-M][0-9.]*[A-Za-z]?)\s+—\s+(?=[A-ZÀ-Ý«\[*(])", r"\1. ", l)  # libellé numéroté
    l = re.sub(rf"^(#+\s+[^—\n]*?)\s+—\s+(?!{CONJ})", r"\1 : ", l)                              # titre de section
    l = re.sub(r"^(\s*)—\s+", r"\1", l)                                              # tiret en début de ligne
    # incises appariées dans une même proposition : virgules, ou parenthèses si l'incise est une énumération
    def paire(m):
        x = m.group(1).strip()
        return f" ({x})" if ("," in x and "(" not in x) else f", {x},"
    l = re.sub(r"\s+—\s*([^—.!?;:\n]{1,320}?)\s*—,?", paire, l)
    l = re.sub(r"(\*\*|\*)\s+—\s+", r"\1 : ", l)                                      # **Libellé** — texte
    # tiret isolé : virgule devant une conjonction, deux-points sinon
    l = re.sub(rf"\s+—\s+(?={CONJ})", ", ", l)
    l = re.sub(r"\s+—\s+", " : ", l)
    l = re.sub(r"\s*—\s*", " ", l)                                                   # cas résiduels
    l = re.sub(r",\s*,", ",", l); l = re.sub(r",\s*([.;:)»])", r"\1", l); l = re.sub(r" ,", ",", l)
    l = re.sub(r"\) ,", "),", l)
    return l

def traiter(texte):
    return "\n".join(ligne(l) for l in texte.split("\n"))

if __name__ == "__main__":
    for f in sys.argv[1:]:
        t = open(f, encoding="utf-8").read()
        n = traiter(t)
        if n != t: open(f, "w", encoding="utf-8").write(n)
