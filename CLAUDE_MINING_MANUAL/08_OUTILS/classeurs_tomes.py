# -*- coding: utf-8 -*-
"""Classeurs Excel de travail des trois tomes de « La Mine augmentée ».
Le contenu provient exclusivement du manuscrit (tableaux, check-lists, annexes) ;
les classeurs y ajoutent seulement des colonnes de suivi, des listes déroulantes et des calculs.
Sorties : 06_PRODUCTION_FINALE/LA_MINE_AUGMENTEE_TOME_{N}_Classeur_de_travail.xlsx"""
import glob, re
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.chart import RadarChart, Reference, BarChart

ROOT = Path(__file__).resolve().parents[1]
MAN, ANN, OUT = ROOT / "01_MANUSCRIT", ROOT / "04_ANNEXES", ROOT / "06_PRODUCTION_FINALE"
AUTEUR = "Verdi Imbole"
TOMES = {1: ("I", "Comprendre et maîtriser Claude", "B07A45", range(1, 17)),
         2: ("II", "Claude dans les métiers et les processus miniers", "5E8F78", range(17, 33)),
         3: ("III", "Méthodes, gouvernance et mise en pratique", "5B7BB0", range(33, 44))}
INK, CREME, BANDE, FILET, SAISIE = "1C1D1F", "EFE7D8", "F8F5EF", "D9D4CC", "FFF8E7"
TITRE_F, CORPS_F = "Garamond", "Calibri"

# ------------------------------------------------------------------ lecture du manuscrit
def nettoie(t):
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t); t = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"\1", t)
    t = t.replace("`", "").replace("\\", "")
    return re.sub(r"\[@[^\]]+\]", "", t).strip()

def tableaux(texte):
    """Renvoie la liste des tableaux Markdown : (titre de section le plus proche, en-tête, lignes)."""
    res, lignes, titre = [], texte.split("\n"), ""
    i = 0
    while i < len(lignes):
        l = lignes[i]
        if l.startswith("#"): titre = nettoie(l.lstrip("#").strip())
        if l.startswith("|") and i + 1 < len(lignes) and re.match(r"^\|[\s:|-]+\|$", lignes[i + 1]):
            tete = [nettoie(c) for c in l.strip().strip("|").split("|")]
            corps = []; i += 2
            while i < len(lignes) and lignes[i].startswith("|"):
                corps.append([nettoie(c) for c in lignes[i].strip().strip("|").split("|")]); i += 1
            res.append((titre, tete, corps)); continue
        i += 1
    return res

def lire(p): return Path(p).read_text(encoding="utf-8")

def chapitres():
    d = {}
    for f in glob.glob(str(MAN / "PARTIE_*" / "*_chapitre_*.md")):
        m = re.search(r"^## Chapitre (\d+)\. (.+)$", lire(f), re.M)
        if m: d[int(m.group(1))] = (m.group(2).strip(), f)
    return d

def metiers():
    """Intitulés courts des métiers, tels qu'ils figurent dans l'ouverture de la partie III."""
    t = lire(MAN / "PARTIE_III" / "00_ouverture_partie_III.md")
    return {int(n): x.strip() for n, x in re.findall(r"^- Chapitre (\d+)\. (.+)$", t, re.M)}

def nb_questions(f):
    t = lire(f); k = t.find("### K. Quiz")
    bloc = t[k:t.find("\n### ", k + 5)] if k >= 0 else ""
    return len(re.findall(r"^\d+\. ", bloc, re.M))

# ------------------------------------------------------------------ mise en forme
def filet(c=FILET): s = Side(style="thin", color=c); return Border(left=s, right=s, top=s, bottom=s)

class Feuille:
    def __init__(self, wb, nom, accent, titre, sous_titre, largeurs, premiere=False):
        self.ws = wb.active if premiere else wb.create_sheet(nom)
        self.ws.title = nom; self.accent = accent; self.n = len(largeurs)
        ws = self.ws
        ws.sheet_properties.tabColor = accent; ws.sheet_view.showGridLines = False
        for i, w in enumerate(largeurs, 1): ws.column_dimensions[get_column_letter(i)].width = w
        der = get_column_letter(self.n)
        for r in (1, 2):
            for c in range(1, self.n + 1): ws.cell(r, c).fill = PatternFill("solid", fgColor=INK)
        ws.merge_cells(f"A1:{der}1"); ws.merge_cells(f"A2:{der}2")
        ws["A1"] = titre; ws["A1"].font = Font(name=TITRE_F, size=20, color=CREME)
        ws["A1"].alignment = Alignment(vertical="center", indent=1)
        ws["A2"] = sous_titre; ws["A2"].font = Font(name=TITRE_F, size=11, italic=True, color=accent)
        ws["A2"].alignment = Alignment(vertical="top", indent=1)
        ws.row_dimensions[1].height = 38; ws.row_dimensions[2].height = 22
        for c in range(1, self.n + 1):
            ws.cell(3, c).border = Border(top=Side(style="medium", color=accent))
        ws.row_dimensions[3].height = 8
        self.r = 4
        ws.page_setup.orientation = "landscape"; ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        ws.print_options.horizontalCentered = True
        ws.oddFooter.left.text = f"La Mine augmentée · {AUTEUR}"; ws.oddFooter.right.text = "Page &P / &N"

    def section(self, texte):
        ws = self.ws; self.r += 1
        ws.cell(self.r, 1, texte).font = Font(name=TITRE_F, size=13, bold=True, color=INK)
        for c in range(1, self.n + 1):
            ws.cell(self.r, c).border = Border(bottom=Side(style="thin", color=self.accent))
        self.r += 1

    def note(self, texte, italique=True, couleur="555555", hauteur=None):
        ws = self.ws
        ws.merge_cells(start_row=self.r, start_column=1, end_row=self.r, end_column=self.n)
        c = ws.cell(self.r, 1, texte); c.font = Font(name=CORPS_F, size=9.5, italic=italique, color=couleur)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if hauteur: ws.row_dimensions[self.r].height = hauteur
        self.r += 1

    def entete(self, cols):
        ws = self.ws
        for i, t in enumerate(cols, 1):
            c = ws.cell(self.r, i, t)
            c.font = Font(name=CORPS_F, size=10, bold=True, color="FFFFFF")
            c.fill = PatternFill("solid", fgColor=self.accent)
            c.alignment = Alignment(wrap_text=True, vertical="center"); c.border = filet(self.accent)
        ws.row_dimensions[self.r].height = 30
        self.r += 1; return self.r - 1

    def ligne(self, vals, saisie=(), hauteur=None, gras0=False):
        ws = self.ws; bande = (self.r % 2 == 0)
        for i, v in enumerate(vals, 1):
            c = ws.cell(self.r, i, v)
            c.font = Font(name=CORPS_F, size=10, bold=(gras0 and i == 1), color="1F3A5F" if i in saisie else "1A1A1A")
            c.alignment = Alignment(wrap_text=True, vertical="top"); c.border = filet()
            if i in saisie: c.fill = PatternFill("solid", fgColor=SAISIE)
            elif bande: c.fill = PatternFill("solid", fgColor=BANDE)
        if hauteur: ws.row_dimensions[self.r].height = hauteur
        self.r += 1; return self.r - 1

    def liste(self, valeurs, plage, invite=""):
        dv = DataValidation(type="list", formula1='"' + ",".join(valeurs) + '"', allow_blank=True,
                            showErrorMessage=True, errorTitle="Valeur non prévue",
                            error="Choisissez une valeur dans la liste.", promptTitle="Choix", prompt=invite or "Choisissez dans la liste.")
        self.ws.add_data_validation(dv); dv.add(plage)

def hauteur(*textes, largeur=60):
    n = max(1, max(len(str(t)) // max(1, largeur) + 1 + str(t).count("\n") for t in textes))
    return min(15 * n, 300)

def accueil(wb, t, feuilles):
    rom, titre, acc, _ = TOMES[t]
    f = Feuille(wb, "Accueil", acc, "La Mine augmentée", f"Tome {rom} : {titre}  ·  Classeur de travail", [4, 34, 90], premiere=True)
    ws = f.ws
    f.r += 1
    f.note("Maîtriser Claude et l'intelligence artificielle générative dans les métiers et les processus miniers.", italique=True, couleur=INK)
    f.note(f"Auteur : {AUTEUR}, auteur indépendant, auditeur financier et freelance.", italique=False, couleur=INK)
    f.section("Contenu du classeur")
    f.entete(["", "Feuille", "Usage"])
    for nom, desc in feuilles:
        r = f.ligne(["", nom, desc], hauteur=hauteur(desc, largeur=95))
        ws.cell(r, 2).hyperlink = f"#'{nom}'!A1"; ws.cell(r, 2).font = Font(name=CORPS_F, size=10, color=acc, underline="single")
    f.section("Mode d'emploi")
    for l in ["Les cellules sur fond crème sont à compléter ; les autres sont issues du livre ou calculées.",
              "Les listes déroulantes proposent les valeurs prévues par la méthode du livre.",
              "Les exemples de Mbiyo Copper Cobalt SA (MCC) sont fictifs, comme dans le livre.",
              "Avant d'utiliser vos propres documents avec Claude, vérifiez leur classification (chapitre 37 et Annexe G)."]:
        f.note("•  " + l, italique=False, couleur="333333")
    f.section("Droits")
    f.note(f"© {AUTEUR}, 2026. Tous droits réservés. Ce classeur accompagne le livre « La Mine augmentée ». "
           "Il peut être utilisé et reproduit pour un usage professionnel personnel ou interne à une organisation ; "
           "sa diffusion publique ou sa vente requièrent l'autorisation écrite de l'auteur.", hauteur=45)
    ws.freeze_panes = "A4"

def suivi_quiz(wb, t):
    rom, titre, acc, chs = TOMES[t]; ch = chapitres()
    f = Feuille(wb, "Suivi des quiz", acc, "Suivi des quiz", f"Tome {rom} : chapitres {chs[0]} à {chs[-1]}", [11, 58, 12, 12, 12, 16, 30])
    f.note("Saisissez le nombre de bonnes réponses après correction (corrigés expliqués à la fin de chaque partie). "
           "Seuil de réussite retenu par la grille d'évaluation des compétences (Annexe K) : 80 %.")
    f.r += 1
    seuil = f.r; f.ws.cell(seuil, 2, "Seuil de réussite").font = Font(name=CORPS_F, bold=True)
    c = f.ws.cell(seuil, 3, 0.8); c.number_format = "0 %"; c.fill = PatternFill("solid", fgColor=SAISIE); c.border = filet()
    f.r += 2
    h = f.entete(["Chapitre", "Titre", "Questions", "Bonnes réponses", "Score", "Statut", "Points à revoir"])
    d = f.r
    for n in chs:
        tt, fp = ch[n]
        r = f.ligne([n, tt, nb_questions(fp), None, None, None, None], saisie=(4, 7), hauteur=hauteur(tt, largeur=58))
        f.ws.cell(r, 5, f'=IF(D{r}="","",D{r}/C{r})').number_format = "0 %"
        f.ws.cell(r, 6, f'=IF(D{r}="","",IF(D{r}/C{r}>=$C${seuil},"Acquis","À revoir"))')
    fin = f.r - 1
    r = f.ligne(["Total", "", f"=SUM(C{d}:C{fin})", f"=SUM(D{d}:D{fin})", None, None, None], gras0=True)
    f.ws.cell(r, 5, f'=IF(COUNT(D{d}:D{fin})=0,"",D{r}/SUMIF(D{d}:D{fin},"<>",C{d}:C{fin}))').number_format = "0 %"
    f.ws.cell(r, 6, f'=COUNTIF(F{d}:F{fin},"Acquis")&" / {len(chs)} acquis"')
    dv = DataValidation(type="whole", operator="between", formula1="0", formula2="20", allow_blank=True,
                        error="Nombre de bonnes réponses entre 0 et le nombre de questions.", showErrorMessage=True)
    f.ws.add_data_validation(dv); dv.add(f"D{d}:D{fin}")
    f.ws.conditional_formatting.add(f"F{d}:F{fin}", CellIsRule(operator="equal", formula=['"Acquis"'], fill=PatternFill("solid", fgColor="DDEBDD"), font=Font(color="2F5E3A", bold=True)))
    f.ws.conditional_formatting.add(f"F{d}:F{fin}", CellIsRule(operator="equal", formula=['"À revoir"'], fill=PatternFill("solid", fgColor="F6DED8"), font=Font(color="8A2E22", bold=True)))
    f.ws.freeze_panes = f.ws.cell(h + 1, 3)

# ------------------------------------------------------------------ TOME 1
def tome1(wb):
    acc = TOMES[1][2]
    accueil(wb, 1, [("Carte des opportunités", "Inventorier les tâches de votre service et qualifier l'apport de Claude (chapitre 1, tableau 1.2)."),
                    ("Constructeur CADRE", "Rédiger une instruction complète brique par brique et obtenir le texte assemblé (chapitre 10)."),
                    ("Check-lists", "Vérifier un résultat de Claude avec les check-lists de l'Annexe E et mesurer le taux de conformité."),
                    ("Capacités et limites", "Consulter le tableau récapitulatif des capacités et limites de Claude (Annexe H)."),
                    ("Suivi des quiz", "Enregistrer vos scores aux quiz des chapitres 1 à 16.")])
    # Carte des opportunités
    ch1 = lire(next(iter(glob.glob(str(MAN / "PARTIE_I" / "01_chapitre_01.md")))))
    _, tete, corps = next(x for x in tableaux(ch1) if x[1][0] == "Tâche" and "Décision" in x[1])
    f = Feuille(wb, "Carte des opportunités", acc, "Carte des opportunités IA", "Chapitre 1 · modèle du tableau 1.2", [34, 12, 40, 34, 12, 12, 24])
    f.note("Les cinq premières lignes reprennent l'exemple du livre (service HSE de MCC, fictif). Complétez les lignes suivantes pour votre service.")
    f.r += 1
    h = f.entete(tete); d = f.r
    for row in corps:
        v = row[:]; m = re.match(r"(\d+)", v[1]); v[1] = int(m.group(1)) if m else None
        r = f.ligne(v, hauteur=hauteur(*v, largeur=36)); f.ws.cell(r, 2).number_format = '0" h"'
    for _ in range(15):
        r = f.ligne([None] * 7, saisie=tuple(range(1, 8)), hauteur=30); f.ws.cell(r, 2).number_format = '0" h"'
    fin = f.r - 1
    f.ligne(["Temps total concerné", f"=SUM(B{d}:B{fin})", "", "", "", "", ""], gras0=True)
    f.ws.cell(f.r - 1, 2).number_format = '0" h/mois"'
    f.liste(["Fort", "Moyen", "Faible"], f"E{d}:E{fin}", "Intérêt de l'usage")
    f.liste(["Faible", "Moyen", "Élevé", "Critique"], f"F{d}:F{fin}", "Niveau de risque")
    for val, fond, enc in (("Critique", "F6DED8", "8A2E22"), ("Élevé", "FBE9D9", "8A4B12"), ("Faible", "DDEBDD", "2F5E3A")):
        f.ws.conditional_formatting.add(f"F{d}:F{fin}", CellIsRule(operator="equal", formula=[f'"{val}"'], fill=PatternFill("solid", fgColor=fond), font=Font(color=enc, bold=True)))
    f.ws.conditional_formatting.add(f"E{d}:E{fin}", CellIsRule(operator="equal", formula=['"Fort"'], font=Font(color="2F5E3A", bold=True)))
    f.ws.freeze_panes = f.ws.cell(h + 1, 2); f.ws.auto_filter.ref = f"A{h}:G{fin}"
    # Constructeur CADRE
    ch10 = lire(MAN / "PARTIE_II" / "10_chapitre_10.md")
    _, tete, corps = next(x for x in tableaux(ch10) if x[1][0] == "Brique")
    f = Feuille(wb, "Constructeur CADRE", acc, "Constructeur d'instruction CADRE", "Chapitre 10 · Contexte, Action, Données, Règles, Exigences de sortie", [18, 20, 40, 70])
    f.note("Rédigez chaque brique dans la colonne de droite. L'instruction assemblée se met à jour automatiquement : copiez-la dans Claude. "
           "La méthode CADRE est un cadre pédagogique propre au livre, et non une méthode officielle d'Anthropic.", hauteur=32)
    f.r += 1
    h = f.entete(tete + ["Votre texte"]); d = f.r
    for row in corps:
        f.ligne(row + [None], saisie=(4,), hauteur=75)
    etiq = ["[C : CONTEXTE]", "[A : ACTION]", "[D : DONNÉES]", "[R : RÈGLES]", "[E : EXIGENCES DE SORTIE]"]
    f.r += 1; f.section("Instruction assemblée")
    parts = "&CHAR(10)&CHAR(10)&".join(f'"{e} "&D{d + i}' for i, e in enumerate(etiq))
    f.ws.merge_cells(start_row=f.r, start_column=1, end_row=f.r, end_column=4)
    c = f.ws.cell(f.r, 1, "=" + parts); c.alignment = Alignment(wrap_text=True, vertical="top")
    c.font = Font(name="Consolas", size=10, color=INK); c.fill = PatternFill("solid", fgColor="F4F1EC"); c.border = filet(acc)
    f.ws.row_dimensions[f.r].height = 260
    f.r += 2
    _, t2, c2 = next(x for x in tableaux(ch10) if x[1][:2] == ["Erreur", "Exemple"]) if any(x[1][:2] == ["Erreur", "Exemple"] for x in tableaux(ch10)) else (None, None, None)
    if t2:
        f.section("Les erreurs de formulation les plus fréquentes (tableau du chapitre 10)")
        f.entete(t2[:4])
        for row in c2: f.ligne(row[:4], hauteur=hauteur(*row, largeur=30))
    # Check-lists
    E = lire(ANN / "E_checklists.md")
    f = Feuille(wb, "Check-lists", acc, "Check-lists de vérification", "Annexe E · à appliquer avant de valider un résultat de Claude", [30, 80, 14, 40])
    f.note("Pour chaque point : Oui (vérifié), Non (à corriger) ou Sans objet. Le taux de conformité exclut les points sans objet.")
    f.r += 1
    synth = f.r; f.r += 12  # place réservée à la synthèse
    h = f.entete(["Check-list", "Point de contrôle", "Statut", "Commentaire"]); d = f.r
    blocs = []
    for sec in re.split(r"^### ", E, flags=re.M)[1:]:
        nom = nettoie(sec.split("\n")[0]); items = re.findall(r"^- \[ \] (.+)$", sec, re.M)
        if not items: continue
        deb = f.r
        for it in items: f.ligne([nom, nettoie(it), None, None], saisie=(3, 4), hauteur=hauteur(it, largeur=80))
        blocs.append((nom, deb, f.r - 1))
    fin = f.r - 1
    f.liste(["Oui", "Non", "Sans objet"], f"C{d}:C{fin}", "Résultat du contrôle")
    f.ws.conditional_formatting.add(f"C{d}:C{fin}", CellIsRule(operator="equal", formula=['"Oui"'], fill=PatternFill("solid", fgColor="DDEBDD"), font=Font(color="2F5E3A", bold=True)))
    f.ws.conditional_formatting.add(f"C{d}:C{fin}", CellIsRule(operator="equal", formula=['"Non"'], fill=PatternFill("solid", fgColor="F6DED8"), font=Font(color="8A2E22", bold=True)))
    sv = f.r; f.r = synth
    f.section("Synthèse")
    f.entete(["Check-list", "Points", "Non conformes", "Conformité"])
    for nom, a, b in blocs:
        r = f.ligne([nom, b - a + 1, f'=COUNTIF(C{a}:C{b},"Non")', None])
        f.ws.cell(r, 4, f'=IF(COUNTIF(C{a}:C{b},"Oui")+COUNTIF(C{a}:C{b},"Non")=0,"",COUNTIF(C{a}:C{b},"Oui")/(COUNTIF(C{a}:C{b},"Oui")+COUNTIF(C{a}:C{b},"Non")))').number_format = "0 %"
    f.r = sv
    f.ws.freeze_panes = f.ws.cell(h + 1, 2) if False else None
    # Capacités et limites
    H = lire(ANN / "H_capacites_limites.md")
    f = Feuille(wb, "Capacités et limites", acc, "Capacités et limites de Claude", "Annexe H · tableau récapitulatif", [36, 60, 40])
    intro = [nettoie(l) for l in H.split("\n")[1:4] if l.strip() and not l.startswith("#")]
    for l in intro: f.note(l)
    for titre, tete, corps in tableaux(H):
        f.section(titre); f.entete(tete)
        for row in corps: f.ligne(row + [""] * (len(tete) - len(row)), hauteur=hauteur(*row, largeur=45))
    suivi_quiz(wb, 1)

# ------------------------------------------------------------------ TOME 2
def tome2(wb):
    acc = TOMES[2][2]; ch = chapitres()
    accueil(wb, 2, [("Bibliothèque de prompts", "Les 124 prompts de l'Annexe B, classés par métier, filtrables, avec un suivi de vos tests."),
                    ("Cas d'usage", "Tous les cas d'usage des chapitres 17 à 32, avec un suivi de réalisation et de validation."),
                    ("Tableau de bord", "Avancement par métier et par statut, calculé à partir de la feuille « Cas d'usage »."),
                    ("Suivi des quiz", "Enregistrer vos scores aux quiz des chapitres 17 à 32.")])
    B = lire(ANN / "B_bibliotheque_prompts.md")
    f = Feuille(wb, "Bibliothèque de prompts", acc, "Bibliothèque de prompts par métier", "Annexe B · remplacez les éléments entre crochets", [9, 26, 34, 90, 13, 30])
    f.note("Ajoutez le contexte de votre entreprise (méthode CADRE, chapitre 10), vérifiez la classification des données avant usage "
           "(chapitre 37) et contrôlez les résultats (Annexe E). Utilisez les filtres de la ligne d'en-tête pour afficher un métier.", hauteur=30)
    f.r += 1
    h = f.entete(["Code", "Métier", "Titre", "Prompt", "Testé", "Notes"]); d = f.r
    for sec in re.split(r"^### ", B, flags=re.M)[1:]:
        metier = re.sub(r"^B\.\d+\.\s*", "", nettoie(sec.split("\n")[0]))
        for code, titre, prompt in re.findall(r"\*\*(B\d{3}) : (.+?)\*\*\s*\n+```text\n(.+?)\n```", sec, re.S):
            f.ligne([code, metier, nettoie(titre), prompt.strip(), None, None], saisie=(5, 6), hauteur=hauteur(prompt, largeur=88))
    fin = f.r - 1
    f.liste(["Oui", "Non", "À adapter"], f"E{d}:E{fin}", "Avez-vous testé ce prompt ?")
    for c in f.ws[f"D{d}:D{fin}"]:
        c[0].font = Font(name="Consolas", size=9, color=INK)
    f.ws.auto_filter.ref = f"A{h}:F{fin}"; f.ws.freeze_panes = f.ws.cell(h + 1, 3)
    # Cas d'usage
    f = Feuille(wb, "Cas d'usage", acc, "Cas d'usage par métier", "Chapitres 17 à 32 · grille en douze points", [10, 40, 10, 58, 14, 13, 30, 30])
    f.note("Chaque cas d'usage suit la grille en douze points présentée en ouverture de la partie III. Mettez à jour le statut au fil de votre pratique.")
    f.r += 1
    h = f.entete(["Chapitre", "Métier ou processus", "Cas", "Titre du cas d'usage", "Statut", "Date", "Livrable produit", "Notes"]); d = f.r
    for n in TOMES[2][3]:
        fp = ch[n][1]; tt = metiers()[n]
        for num, titre in re.findall(r"^#### Cas d'usage (\d+\.\d+)(?: :|\.)\s*(.+)$", lire(fp), re.M):
            r = f.ligne([n, tt, num, nettoie(titre), "À faire", None, None, None], saisie=(5, 6, 7, 8), hauteur=hauteur(titre, tt, largeur=45))
            f.ws.cell(r, 6).number_format = "DD/MM/YYYY"
    fin = f.r - 1
    statuts = ["À faire", "En cours", "Réalisé", "Validé"]
    f.liste(statuts, f"E{d}:E{fin}", "Avancement du cas")
    couleurs = {"En cours": ("FBE9D9", "8A4B12"), "Réalisé": ("E3ECF5", "2C4A6E"), "Validé": ("DDEBDD", "2F5E3A")}
    for s_, (fond, enc) in couleurs.items():
        f.ws.conditional_formatting.add(f"E{d}:E{fin}", CellIsRule(operator="equal", formula=[f'"{s_}"'], fill=PatternFill("solid", fgColor=fond), font=Font(color=enc, bold=True)))
    f.ws.auto_filter.ref = f"A{h}:H{fin}"; f.ws.freeze_panes = f.ws.cell(h + 1, 4)
    # Tableau de bord
    g = Feuille(wb, "Tableau de bord", acc, "Tableau de bord", "Avancement calculé à partir de la feuille « Cas d'usage »", [48, 12, 12, 12, 12, 12, 14])
    g.r += 1
    hh = g.entete(["Métier ou processus", "Cas"] + statuts + ["Avancement"]); dd = g.r
    vus = []
    for n in TOMES[2][3]:
        tt = metiers()[n]
        vus.append(tt)
        rng = f"'Cas d''usage'!$B${d}:$B${fin}"; st = f"'Cas d''usage'!$E${d}:$E${fin}"
        r = g.ligne([tt, f'=COUNTIF({rng},A{g.r})'] + [f'=COUNTIFS({rng},A{g.r},{st},"{s_}")' for s_ in statuts] + [None])
        g.ws.cell(r, 7, f'=IF(B{r}=0,"",(E{r}+F{r})/B{r})').number_format = "0 %"
    gf = g.r - 1
    r = g.ligne(["Total", f"=SUM(B{dd}:B{gf})"] + [f"=SUM({get_column_letter(3 + i)}{dd}:{get_column_letter(3 + i)}{gf})" for i in range(4)] + [None], gras0=True)
    g.ws.cell(r, 7, f'=IF(B{r}=0,"",(E{r}+F{r})/B{r})').number_format = "0 %"
    from openpyxl.formatting.rule import DataBarRule
    g.ws.conditional_formatting.add(f"G{dd}:G{gf}", DataBarRule(start_type="num", start_value=0, end_type="num", end_value=1, color=acc))
    ch_ = BarChart(); ch_.type = "bar"; ch_.grouping = "stacked"; ch_.overlap = 100
    ch_.title = "Cas d'usage par statut"; ch_.style = 2
    data = Reference(g.ws, min_col=3, max_col=6, min_row=hh, max_row=gf)
    cats = Reference(g.ws, min_col=1, min_row=dd, max_row=gf)
    ch_.add_data(data, titles_from_data=True); ch_.set_categories(cats)
    for s_, col in zip(ch_.series, ["D9D4CC", "E0A86A", "7FA2C9", acc]):
        s_.graphicalProperties.solidFill = col; s_.graphicalProperties.line.solidFill = col
    ch_.y_axis.title = "Nombre de cas"; ch_.x_axis.scaling.orientation = "maxMin"
    ch_.height = 12; ch_.width = 22; ch_.legend.position = "b"
    g.ws.add_chart(ch_, f"A{g.r + 2}")
    suivi_quiz(wb, 2)

# ------------------------------------------------------------------ TOME 3
def tome3(wb):
    acc = TOMES[3][2]
    accueil(wb, 3, [("Grille de compétences", "Évaluer votre niveau sur les huit blocs de compétences (Annexe K), avec profil graphique et statut de référent."),
                    ("Programme 30 jours", "Planifier et suivre le programme d'apprentissage personnel (Annexe J)."),
                    ("Classification", "Les quatre niveaux de classification (Annexe G) et un registre pour classer vos documents."),
                    ("Registre des cas d'usage", "Tenir le registre des cas d'usage prévu par la politique IA (chapitre 40)."),
                    ("Suivi des quiz", "Enregistrer vos scores aux quiz des chapitres 33 à 43.")])
    K = lire(ANN / "K_grille_competences.md")
    f = Feuille(wb, "Grille de compétences", acc, "Grille d'évaluation des compétences", "Annexe K · le niveau est attribué sur preuves", [30, 26, 26, 30, 30, 30])
    f.note(nettoie(re.search(r"^\*Échelle.+\*$", K, re.M).group(0)))
    tabs = tableaux(K)
    titre, tete, corps = tabs[0]
    f.section("Référentiel"); f.entete(tete)
    for row in corps: f.ligne(row, hauteur=hauteur(*row, largeur=26), gras0=True)
    f.r += 1; f.section("Fiche de synthèse")
    h = f.entete(["Bloc", "Niveau (1 à 4)", "Preuve principale", "Date", "Évaluateur", "Écart au seuil de référent"]); d = f.r
    blocs = [re.match(r"(C\d)\s*(.*)", r_[0]) for r_ in corps]
    for m in blocs:
        exig = 4 if m.group(1) in ("C3", "C7") else 3
        r = f.ligne([f"{m.group(1)} {m.group(2)}", None, None, None, None, None], saisie=(2, 3, 4, 5), hauteur=30)
        f.ws.cell(r, 4).number_format = "DD/MM/YYYY"
        f.ws.cell(r, 6, f'=IF(B{r}="","",IF(B{r}>={exig},"Atteint (seuil {exig})","Manque "&{exig}-B{r}&" niveau(x)"))')
    fin = f.r - 1
    dv = DataValidation(type="whole", operator="between", formula1="1", formula2="4", allow_blank=True, showErrorMessage=True,
                        error="Niveau de 1 (découverte) à 4 (maîtrise).", promptTitle="Niveau", prompt="1 découverte, 2 application guidée, 3 autonomie, 4 maîtrise")
    f.ws.add_data_validation(dv); dv.add(f"B{d}:B{fin}")
    f.ws.conditional_formatting.add(f"F{d}:F{fin}", FormulaRule(formula=[f'LEFT(F{d},7)="Atteint"'], fill=PatternFill("solid", fgColor="DDEBDD"), font=Font(color="2F5E3A", bold=True)))
    f.ws.conditional_formatting.add(f"F{d}:F{fin}", FormulaRule(formula=[f'LEFT(F{d},6)="Manque"'], fill=PatternFill("solid", fgColor="F6DED8"), font=Font(color="8A2E22")))
    f.r += 1
    rt = f.ligne(["Test pratique de maîtrise (sur 100)", None, "Chapitre 42", None, None, None], saisie=(2,), gras0=True)
    rm = f.ligne(["Niveau moyen", f'=IF(COUNT(B{d}:B{fin})=0,"",AVERAGE(B{d}:B{fin}))', None, None, None, None], gras0=True)
    f.ws.cell(rm, 2).number_format = "0.0"
    i3 = d + 2; i7 = d + 6
    rs = f.ligne(["Statut d'utilisateur référent", None, None, None, None, None], gras0=True)
    f.ws.cell(rs, 2, f'=IF(COUNT(B{d}:B{fin})<8,"Évaluation incomplète",IF(AND(COUNTIF(B{d}:B{fin},"<3")=0,B{i3}>=4,B{i7}>=4,B{rt}>=85),"Référent","Pas encore référent"))')
    f.ws.merge_cells(start_row=rs, start_column=2, end_row=rs, end_column=3)
    f.note(nettoie(re.search(r"^\*Statut d'utilisateur.+\*$", K, re.M).group(0)))
    f.ws.conditional_formatting.add(f"B{rs}", CellIsRule(operator="equal", formula=['"Référent"'], fill=PatternFill("solid", fgColor="DDEBDD"), font=Font(color="2F5E3A", bold=True)))
    rc = RadarChart(); rc.type = "marker"; rc.style = 26; rc.title = "Profil de compétences"
    rc.add_data(Reference(f.ws, min_col=2, min_row=h, max_row=fin), titles_from_data=True)
    rc.set_categories(Reference(f.ws, min_col=1, min_row=d, max_row=fin))
    rc.y_axis.scaling.min = 0; rc.y_axis.scaling.max = 4; rc.y_axis.majorUnit = 1; rc.y_axis.delete = False
    rc.series[0].graphicalProperties.line.solidFill = acc; rc.series[0].graphicalProperties.line.width = 28000
    rc.height = 11; rc.width = 16; rc.legend = None
    f.ws.add_chart(rc, f"A{f.r + 1}")
    # Programme 30 jours
    J = lire(ANN / "J_programme_30_jours.md")
    f = Feuille(wb, "Programme 30 jours", acc, "Programme d'apprentissage sur 30 jours", "Annexe J · environ 45 minutes par jour", [8, 34, 18, 42, 36, 13, 14, 26])
    f.note(nettoie(re.search(r"^\*Rythme.+\*$", J, re.M).group(0)))
    f.r += 1
    rd = f.r; f.ws.cell(rd, 1, "Date de début").font = Font(name=CORPS_F, bold=True)
    f.ws.merge_cells(start_row=rd, start_column=1, end_row=rd, end_column=2)
    c = f.ws.cell(rd, 3); c.fill = PatternFill("solid", fgColor=SAISIE); c.border = filet(); c.number_format = "DD/MM/YYYY"
    f.ws.cell(rd, 4, "Repos le dimanche : six jours de travail par semaine.").font = Font(name=CORPS_F, italic=True, size=9.5, color="555555")
    f.r += 2
    h = f.entete(["Jour", "Semaine", "Lecture", "Pratique", "Trace", "Date prévue", "Statut", "Notes"]); d = f.r
    for sec in re.split(r"^### ", J, flags=re.M)[1:]:
        sem = nettoie(sec.split("\n")[0])
        tb = tableaux("### " + sec)
        if tb:
            for row in tb[0][2]:
                r = f.ligne([int(row[0]), sem, row[1], row[2], row[3], None, "À faire", None], saisie=(7, 8), hauteur=hauteur(*row, largeur=36))
        else:
            txt = nettoie(" ".join(l for l in sec.split("\n")[1:] if l.strip()))
            for j in (29, 30):
                r = f.ligne([j, sem, "Ch. 43", txt, "Dossier du système de travail assisté", None, "À faire", None], saisie=(7, 8), hauteur=hauteur(txt, largeur=40))
    fin = f.r - 1
    for r in range(d, fin + 1):
        c = f.ws.cell(r, 6, f'=IF($C${rd}="","",IF(A{r}=1,$C${rd},WORKDAY.INTL($C${rd},A{r}-1,11)))'); c.number_format = "ddd DD/MM"
    f.liste(["À faire", "Fait", "Reporté"], f"G{d}:G{fin}", "Avancement de la journée")
    f.ws.conditional_formatting.add(f"G{d}:G{fin}", CellIsRule(operator="equal", formula=['"Fait"'], fill=PatternFill("solid", fgColor="DDEBDD"), font=Font(color="2F5E3A", bold=True)))
    f.ws.conditional_formatting.add(f"G{d}:G{fin}", CellIsRule(operator="equal", formula=['"Reporté"'], fill=PatternFill("solid", fgColor="FBE9D9"), font=Font(color="8A4B12", bold=True)))
    f.ws.cell(rd, 6, "Avancement").font = Font(name=CORPS_F, bold=True)
    c = f.ws.cell(rd, 7, f'=COUNTIF(G{d}:G{fin},"Fait")/COUNTA(A{d}:A{fin})'); c.number_format = "0 %"; c.font = Font(name=CORPS_F, bold=True, size=12, color=acc)
    f.ws.freeze_panes = f.ws.cell(h + 1, 3)
    # Classification
    G = lire(ANN / "G_classification_donnees.md")
    f = Feuille(wb, "Classification", acc, "Classification et protection des données", "Annexe G · à appliquer avant toute utilisation de Claude", [26, 30, 40, 34, 34])
    tabs = tableaux(G)
    t1 = tabs[0]; f.section(t1[0]); f.entete(t1[1]); ref = f.r
    for row in t1[2]: f.ligne(row, hauteur=hauteur(*row, largeur=32), gras0=True)
    reff = f.r - 1
    for titre, tete, corps in tabs[1:]:
        f.section(titre); f.entete(tete)
        for row in corps: f.ligne(row + [""] * (len(tete) - len(row)), hauteur=hauteur(*row, largeur=40))
    f.r += 1; f.section("Registre de classification de vos documents")
    h = f.entete(["Document", "Propriétaire de la donnée", "Niveau", "Usage de Claude (Annexe G)", "Mesures (Annexe G)"]); d = f.r
    for _ in range(25):
        r = f.ligne([None, None, None, None, None], saisie=(1, 2, 3), hauteur=30)
        f.ws.cell(r, 4, f'=IF(C{r}="","",INDEX($D${ref}:$D${reff},MATCH(C{r},$A${ref}:$A${reff},0)))')
        f.ws.cell(r, 5, f'=IF(C{r}="","",INDEX($E${ref}:$E${reff},MATCH(C{r},$A${ref}:$A${reff},0)))')
    fin = f.r - 1
    f.liste([row[0] for row in t1[2]], f"C{d}:C{fin}", "Niveau de classification")
    f.ws.conditional_formatting.add(f"D{d}:D{fin}", CellIsRule(operator="equal", formula=['"Interdit"'], fill=PatternFill("solid", fgColor="F6DED8"), font=Font(color="8A2E22", bold=True)))
    # Registre des cas d'usage (chapitre 40)
    f = Feuille(wb, "Registre des cas d'usage", acc, "Registre des cas d'usage IA", "Chapitre 40 · cas validés, propriétaires, risques, contrôles", [34, 22, 16, 34, 34, 14, 14])
    f.note("Le registre recense les cas d'usage validés, leur propriétaire, leurs risques et les contrôles associés (politique d'utilisation de l'IA, chapitre 40).")
    f.r += 1
    h = f.entete(["Cas d'usage", "Propriétaire", "Niveau de données", "Risques", "Contrôles", "Statut", "Prochaine revue"]); d = f.r
    for _ in range(30):
        r = f.ligne([None] * 7, saisie=tuple(range(1, 8)), hauteur=30); f.ws.cell(r, 7).number_format = "DD/MM/YYYY"
    fin = f.r - 1
    f.liste([row[0] for row in t1[2]], f"C{d}:C{fin}", "Niveau de classification (Annexe G)")
    f.liste(["Proposé", "Validé", "Suspendu", "Retiré"], f"F{d}:F{fin}", "Statut du cas d'usage")
    f.ws.freeze_panes = f.ws.cell(h + 1, 2); f.ws.auto_filter.ref = f"A{h}:G{fin}"
    suivi_quiz(wb, 3)

if __name__ == "__main__":
    for t, fn in ((1, tome1), (2, tome2), (3, tome3)):
        wb = Workbook(); fn(wb)
        wb.properties.creator = AUTEUR; wb.properties.title = f"La Mine augmentée, tome {TOMES[t][0]} : classeur de travail"
        p = OUT / f"LA_MINE_AUGMENTEE_TOME_{t}_Classeur_de_travail.xlsx"; wb.save(p); print(p)
