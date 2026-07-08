import RapportRoast from "@/components/RapportRoast";
import type { RapportRoastData } from "@/lib/roast";

// Aperçu du composant RapportRoast avec des données d'exemple —
// le format exact que le persona « Brandon » renvoie en JSON.

const EXEMPLE: RapportRoastData = {
  titre: "Léa & Hugo : Une hotline dont un seul des deux paie l'abonnement",
  intro:
    "J'ai analysé vos **3 214 messages**. Il m'a fallu 200 messages pour comprendre le contrat implicite : Léa fournit le contenu, Hugo fournit les **« mdr »**. L'un de vous deux écrit une newsletter. L'autre s'est abonné par politesse.",
  statistiques: {
    nb_messages: 3214,
    periode: "février 2023 → avril 2024",
    ratio_messages: "Léa 71 % / Hugo 29 %",
  },
  dossiers: [
    {
      nom: "Léa",
      surnom: "La Procureure des accusés absents",
      analyse: [
        "Léa est infirmière, et ça se voit : elle fait des **gardes de nuit** dans cette conversation. 43 messages envoyés entre minuit et 6h, tous adressés à un homme qui dort.",
        "Sa spécialité : le triple message. Une question, puis la réponse qu'elle imagine, puis le procès de cette réponse imaginée. Hugo n'a même plus besoin de participer — elle plaide **les deux parties**.",
      ],
      pieces_a_conviction: [
        {
          citation: "non mais réponds pas, je sais déjà ce que tu vas dire",
          tacle:
            "Envoyé à 1h47. Il n'a effectivement **pas répondu**, ce qui, techniquement, est de l'obéissance.",
        },
        {
          citation: "c'est bon oublie. C'est OUBLIÉ.",
          tacle:
            "Le sujet est revenu **neuf fois** dans les trois semaines suivantes. La mémoire pardonne, l'archive jamais.",
        },
      ],
    },
    {
      nom: "Hugo",
      surnom: "Le Service Après-Vente fermé le week-end",
      analyse: [
        "Hugo travaille dans la logistique, et il gère cette relation comme un entrepôt : tout ce qui arrive est **accusé de réception**, rien n'est traité avant 48 heures ouvrées.",
        "Son vocabulaire tient sur un ticket de caisse : **« mdr »**, **« ah oui »**, **« je te dis ça »**. Il ne te dit jamais ça. Le colis est perdu en transit depuis février.",
      ],
      pieces_a_conviction: [
        {
          citation: "jsuis pas trop message en ce moment",
          tacle:
            "Posté sur une application de messagerie, l'endroit exact où l'on est censé être **« message »**.",
        },
        {
          citation: "on en parle ce week end promis 👍",
          tacle:
            "Ce message a **11 mois**. Le week-end en question n'a pas encore été livré.",
        },
      ],
    },
  ],
  teasing: [
    {
      icone: "🗣",
      titre: "Décodage du dialecte",
      accroche:
        "Ce que veut VRAIMENT dire **« je te dis ça »** — traduction assermentée incluse.",
    },
    {
      icone: "🏆",
      titre: "La cérémonie des récompenses",
      accroche:
        "Le prix du **vu sans réponse** le plus long se joue à 6 jours près. Suspense insoutenable.",
    },
    {
      icone: "🚩",
      titre: "Les red flags",
      accroche:
        "Il y en a quatre. L'un des deux les collectionne comme des **points fidélité**.",
    },
  ],
};

export const metadata = {
  title: "Aperçu — Rapport de Brandon",
};

export default function PageApercuRoast() {
  return (
    <main className="min-h-screen bg-stone-100 px-4 py-12">
      <RapportRoast rapport={EXEMPLE} />
      <p className="mx-auto mt-6 max-w-2xl text-center text-xs text-stone-400">
        Aperçu du composant <code>RapportRoast</code> avec des données
        d&apos;exemple — le JSON exact que renvoie le persona « Brandon »
        (voir <code>lib/roast.ts</code>).
      </p>
    </main>
  );
}
