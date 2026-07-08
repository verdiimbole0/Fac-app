import { jsPDF } from "jspdf";

// Export PDF du rapport, entièrement côté client : le contenu ne quitte
// pas le navigateur. Gère le sous-ensemble markdown produit par Steve
// (titres, listes, gras, citations).

const MARGE = 18;
const LARGEUR = 210 - 2 * MARGE;
const BAS_PAGE = 285;

const TEAL = "#075e54";
const VERT = "#25d366";
const ENCRE = "#111b21";
const GRIS = "#667781";

function nettoyer(ligne: string): string {
  return ligne.replace(/\*\*([^*]+)\*\*/g, "$1").trim();
}

export function telechargerRapportPdf(
  markdown: string,
  titre: string,
  marque: string = "Que pense Steve",
  prefixeFichier: string = "rapport-steve",
) {
  const doc = new jsPDF({ unit: "mm", format: "a4" });
  let y = 0;

  const nouvellePage = () => {
    doc.addPage();
    y = MARGE;
  };

  const verifierPlace = (hauteur: number) => {
    if (y + hauteur > BAS_PAGE) nouvellePage();
  };

  const ecrire = (
    texte: string,
    opts: {
      taille: number;
      style?: "normal" | "bold" | "italic" | "bolditalic";
      police?: "helvetica" | "times";
      couleur?: string;
      retrait?: number;
      interligne?: number;
      avant?: number;
      apres?: number;
    },
  ) => {
    const {
      taille,
      style = "normal",
      police = "helvetica",
      couleur = ENCRE,
      retrait = 0,
      interligne = 1.45,
      avant = 0,
      apres = 2,
    } = opts;
    doc.setFont(police, style);
    doc.setFontSize(taille);
    doc.setTextColor(couleur);
    const lignes: string[] = doc.splitTextToSize(texte, LARGEUR - retrait);
    const hauteurLigne = (taille * 0.3528) * interligne;
    y += avant;
    for (const l of lignes) {
      verifierPlace(hauteurLigne);
      doc.text(l, MARGE + retrait, y + hauteurLigne * 0.75);
      y += hauteurLigne;
    }
    y += apres;
  };

  // Bandeau d'en-tête façon WhatsApp
  doc.setFillColor(TEAL);
  doc.rect(0, 0, 210, 26, "F");
  doc.setFillColor(VERT);
  doc.circle(MARGE + 5, 13, 5, "F");
  doc.setFont("helvetica", "bold");
  doc.setFontSize(13);
  doc.setTextColor("#ffffff");
  doc.text("S", MARGE + 5, 14.6, { align: "center" });
  doc.text(marque, MARGE + 14, 11.5);
  doc.setFont("helvetica", "normal");
  doc.setFontSize(8.5);
  doc.setTextColor("#c9ece5");
  doc.text(
    `Rapport généré le ${new Date().toLocaleDateString("fr-FR", { day: "numeric", month: "long", year: "numeric" })}`,
    MARGE + 14,
    17.5,
  );
  y = 36;

  const blocs = markdown.split(/\n{2,}/);
  for (const bloc of blocs) {
    const b = bloc.trim();
    if (!b) continue;

    if (b.startsWith("# ")) {
      ecrire(nettoyer(b.slice(2)), {
        taille: 19,
        style: "bolditalic",
        police: "times",
        couleur: TEAL,
        avant: 2,
        apres: 4,
        interligne: 1.25,
      });
    } else if (b.startsWith("## ")) {
      verifierPlace(16);
      ecrire(nettoyer(b.slice(3)), {
        taille: 13.5,
        style: "bolditalic",
        police: "times",
        couleur: TEAL,
        avant: 5,
        apres: 2.5,
        interligne: 1.25,
      });
      doc.setDrawColor(VERT);
      doc.setLineWidth(0.6);
      doc.line(MARGE, y - 1.5, MARGE + 24, y - 1.5);
      y += 2;
    } else if (b.startsWith("> ")) {
      ecrire(nettoyer(b.replace(/^> ?/gm, "")), {
        taille: 9.5,
        style: "italic",
        couleur: GRIS,
        retrait: 4,
        apres: 3,
      });
    } else if (/^(-|\d+\.)\s/.test(b)) {
      for (const item of b.split("\n")) {
        const m = item.match(/^(-|\d+\.)\s+(.*)$/);
        if (!m) continue;
        const puce = m[1] === "-" ? "•" : m[1];
        const texte = nettoyer(m[2]);
        doc.setFont("helvetica", "bold");
        doc.setFontSize(10.5);
        doc.setTextColor(VERT);
        verifierPlace(6);
        doc.text(puce, MARGE + 1, y + 3.9);
        ecrire(texte, { taille: 10.5, retrait: 7, apres: 1.5 });
      }
      y += 1.5;
    } else {
      ecrire(nettoyer(b), { taille: 10.5, apres: 3 });
    }
  }

  // Pied de page avec pagination
  const nbPages = doc.getNumberOfPages();
  for (let i = 1; i <= nbPages; i++) {
    doc.setPage(i);
    doc.setFont("helvetica", "normal");
    doc.setFontSize(8);
    doc.setTextColor(GRIS);
    doc.text(
      `${marque} — ${titre}`,
      MARGE,
      292,
    );
    doc.text(`${i} / ${nbPages}`, 210 - MARGE, 292, { align: "right" });
  }

  const nomFichier = `${prefixeFichier}-${titre
    .toLowerCase()
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 60)}.pdf`;
  doc.save(nomFichier || `${prefixeFichier}.pdf`);
}
