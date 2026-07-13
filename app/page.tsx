import Link from "next/link";
import EnTete from "@/components/EnTete";

const TYPES_DE_CONVERSATIONS = [
  {
    emoji: "👯",
    titre: "Le groupe de potes",
    texte:
      "Qui porte le groupe, qui ghoste, qui répond « mdr » à tout. Steve distribue les rôles — avec tendresse.",
  },
  {
    emoji: "❤️",
    titre: "Le couple",
    texte:
      "L'équilibre des messages, qui s'excuse en premier, qui laisse en vu. Un avis honnête, et des pistes pour avancer.",
  },
  {
    emoji: "👨‍👩‍👧",
    titre: "La famille",
    texte:
      "Le groupe familial, ses chaînes de bonjour, ses photos floues et ses non-dits. Steve a tout lu, et il comprend.",
  },
  {
    emoji: "💼",
    titre: "Le boulot",
    texte:
      "Les « petit point rapide ? », les 👍 passifs-agressifs, les messages du dimanche soir. Il voit tout, il conseille aussi.",
  },
  {
    emoji: "🫠",
    titre: "La situationship",
    texte:
      "Trois semaines de silence puis « tu me manques ». Steve te dit ce que tu refuses de voir — et quoi en faire.",
  },
  {
    emoji: "🔥",
    titre: "Le chaos total",
    texte:
      "Plus c'est le bazar, mieux c'est. Les conversations compliquées font les analyses les plus utiles.",
  },
];

const ETAPES = [
  {
    titre: "Crée ton compte",
    texte:
      "Une inscription rapide et sécurisée. Tes rapports restent dans ton espace, et toi seul peux les lire — ou les supprimer.",
  },
  {
    titre: "Envoie ta conversation",
    texte:
      "Export WhatsApp (.txt) ou copier-coller. Steve la lit intégralement et mène une analyse approfondie : chronologie, chiffres, dynamiques, moments-clés.",
  },
  {
    titre: "Reçois son rapport complet",
    texte:
      "Son ressenti, les portraits, l'analyse détaillée, son avis objectif et ses conseils concrets. À lire sur place ou à télécharger en PDF.",
  },
];

const FAQ = [
  {
    q: "C'est qui, Steve ?",
    r: "Steve lit ta conversation comme le ferait un ami lucide : il rit, il s'émeut, il remarque tout. Mais avant d'écrire une ligne, il mène une vraie analyse — chronologie, volumes, temps de réponse, dynamiques — et son avis final est objectif, appuyé sur des faits. C'est une IA (Claude, d'Anthropic) avec une consigne stricte : être humain, honnête et utile.",
  },
  {
    q: "Pourquoi faut-il un compte ?",
    r: "Pour que tes rapports restent à toi. Ils sont enregistrés dans ton espace personnel, consultables et téléchargeables en PDF quand tu veux — et supprimables en un clic avec le bouton « Supprimer mes données ».",
  },
  {
    q: "Mes conversations sont-elles stockées ?",
    r: "Non, jamais. La conversation sert uniquement à écrire le rapport, puis elle est oubliée. Seul le rapport est conservé dans ton compte, et tu peux l'effacer à tout moment. Rien n'est utilisé pour entraîner des modèles.",
  },
  {
    q: "Le site est-il sécurisé ?",
    r: "Oui : mots de passe hachés avec sel (jamais stockés en clair), sessions révocables à jeton opaque, cookies HttpOnly, protection anti-CSRF, limitation des tentatives de connexion et en-têtes de sécurité stricts. Le propriétaire du site gère les comptes et peut suspendre tout accès.",
  },
  {
    q: "Que contient le rapport ?",
    r: "Sept parties : le ressenti de Steve, les portraits des participants, l'analyse en profondeur (avec les chiffres), les moments-clés cités, les superlatifs, son avis objectif sans détour, et ses conseils concrets pour améliorer la situation.",
  },
  {
    q: "Les autres membres du groupe sauront ?",
    r: "Seulement si tu partages le rapport. Ce que tu en fais ensuite — le balancer dans le groupe, par exemple — c'est ta responsabilité. Steve décline toute implication dans les drames qui suivront.",
  },
];

function TelephoneDemo() {
  return (
    <div className="carte mx-auto w-full max-w-sm overflow-hidden !rounded-3xl p-0 shadow-xl">
      {/* En-tête du chat */}
      <div className="flex items-center gap-3 bg-teal px-4 py-3 text-white">
        <div className="flex h-9 w-9 items-center justify-center rounded-full bg-vert text-sm font-bold text-teal">
          S
        </div>
        <div className="flex-1">
          <p className="text-sm font-bold leading-tight">Steve</p>
          <p className="text-[11px] text-white/75">en ligne</p>
        </div>
        <span className="text-white/60">⋮</span>
      </div>
      {/* Messages */}
      <div className="papier-peint flex flex-col gap-2.5 px-3 py-4">
        <div className="bulle-envoyee apparait" style={{ animationDelay: "0.2s" }}>
          Steve, analyse notre groupe « Vacances 2024 » stp 🙏
          <span className="heure-bulle">
            23:54 <span className="coches">✓</span>
          </span>
        </div>
        <div className="bulle-recue apparait" style={{ animationDelay: "0.9s" }}>
          Reçu. 4 812 messages… installe-toi, je lis tout. ☕
          <span className="heure-bulle">23:55</span>
        </div>
        <div className="bulle-recue apparait" style={{ animationDelay: "1.7s" }}>
          Bon. J&apos;ai ri, j&apos;ai soupiré, j&apos;ai même été ému une
          fois (le message de Julie du 22 mars — vous savez).
          <span className="heure-bulle">23:58</span>
        </div>
        <div className="bulle-recue apparait" style={{ animationDelay: "2.6s" }}>
          Verdict : personne ne partira tant que la question du budget
          restera taboue. 11 faux départs, zéro vrai départ. Je vous
          explique tout — et je vous dis comment débloquer ça. 📋
          <span className="heure-bulle">23:59</span>
        </div>
        <div
          className="bulle-recue apparait flex items-center gap-2"
          style={{ animationDelay: "3.5s" }}
        >
          <span className="points-frappe">
            <span />
            <span />
            <span />
          </span>
          <span className="text-xs text-gris">Steve rédige le rapport…</span>
        </div>
      </div>
    </div>
  );
}

export default function Home() {
  return (
    <main className="flex-1">
      <EnTete />

      {/* Hero */}
      <section className="papier-peint">
        <div className="mx-auto grid max-w-5xl items-center gap-12 px-5 pb-20 pt-14 md:grid-cols-[1.05fr_0.95fr] md:pt-20">
          <div>
            <p className="lever inline-block rounded-full bg-bulle-sortie px-3.5 py-1.5 text-xs font-bold uppercase tracking-wider text-teal">
              Des rapports humains sur tes conversations
            </p>
            <h1
              className="lever mt-5 text-4xl font-extrabold leading-[1.08] tracking-tight text-teal md:text-5xl"
              style={{ animationDelay: "0.1s" }}
            >
              Steve lit ta conversation.
              <br />
              <span className="voice text-teal-2">
                Il analyse tout. Puis il te parle franchement.
              </span>
            </h1>
            <p
              className="lever mt-5 max-w-lg text-lg leading-relaxed text-gris"
              style={{ animationDelay: "0.2s" }}
            >
              Envoie-lui un export WhatsApp ou iMessage. Steve mène une analyse
              approfondie — chronologie, chiffres, dynamiques, moments-clés —
              puis écrit un rapport drôle et sincère, avec un avis objectif et
              des conseils concrets pour la suite.
            </p>
            <div
              className="lever mt-8 flex flex-wrap items-center gap-4"
              style={{ animationDelay: "0.3s" }}
            >
              <Link href="/inscription" className="btn-vert px-7 py-3.5 text-base">
                Créer mon compte gratuit →
              </Link>
              <Link
                href="/connexion"
                className="btn-blanc px-6 py-3.5 text-base"
              >
                J&apos;ai déjà un compte
              </Link>
            </div>
            <p
              className="lever mt-6 text-xs text-gris"
              style={{ animationDelay: "0.4s" }}
            >
              🔒 Conversations jamais stockées · rapports supprimables en un
              clic · export PDF
            </p>
          </div>
          <TelephoneDemo />
        </div>
      </section>

      {/* Types de conversations */}
      <section className="bg-blanc py-20">
        <div className="mx-auto max-w-5xl px-5">
          <h2 className="text-center text-3xl font-extrabold tracking-tight text-teal">
            Le bazar, c&apos;est sa <span className="voice">spécialité</span>
          </h2>
          <p className="mx-auto mt-3 max-w-xl text-center text-gris">
            Steve accepte toutes les conversations. Plus c&apos;est compliqué,
            plus son analyse est utile.
          </p>
          <div className="mt-12 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {TYPES_DE_CONVERSATIONS.map((t) => (
              <div key={t.titre} className="carte carte-survol p-6">
                <p className="text-3xl">{t.emoji}</p>
                <h3 className="mt-3 text-lg font-bold text-teal">{t.titre}</h3>
                <p className="mt-2 text-sm leading-relaxed text-gris">
                  {t.texte}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Les deux modes */}
      <section className="bg-blanc pb-20">
        <div className="mx-auto max-w-5xl px-5">
          <h2 className="text-center text-3xl font-extrabold tracking-tight text-teal">
            Deux analystes, <span className="voice">deux ambiances</span>
          </h2>
          <p className="mx-auto mt-3 max-w-xl text-center text-gris">
            Choisis ton rapport selon la conversation — et selon ton courage.
          </p>
          <div className="mt-10 grid gap-6 md:grid-cols-2">
            {/* Carte Steve */}
            <div className="carte carte-survol flex flex-col p-7">
              <div className="flex items-center gap-3">
                <span className="flex h-12 w-12 items-center justify-center rounded-full bg-vert text-xl font-bold text-teal">
                  S
                </span>
                <div>
                  <h3 className="text-xl font-extrabold text-teal">Steve</h3>
                  <p className="text-xs font-semibold uppercase tracking-wider text-gris">
                    Groupes &amp; conversations à plusieurs
                  </p>
                </div>
              </div>
              <p className="mt-4 flex-1 text-sm leading-relaxed text-gris">
                Le pote lucide et bienveillant. Il lit tout le groupe, analyse
                en profondeur, tacle avec tendresse — et termine toujours par
                des <strong className="text-teal">conseils concrets</strong>{" "}
                pour améliorer la situation. Rapport rédigé en direct, dans une
                vraie discussion.
              </p>
              <Link
                href="/rapport"
                className="btn-vert mt-6 inline-block self-start px-6 py-3 text-sm"
              >
                💬 Parler à Steve →
              </Link>
            </div>
            {/* Carte Brandon */}
            <div className="carte carte-survol flex flex-col !border-stone-300 !bg-stone-50 p-7">
              <div className="flex items-center gap-3">
                <span className="flex h-12 w-12 items-center justify-center rounded-full bg-stone-800 text-xl font-bold text-white">
                  B
                </span>
                <div>
                  <h3 className="text-xl font-extrabold text-stone-800">
                    Brandon
                  </h3>
                  <p className="text-xs font-semibold uppercase tracking-wider text-stone-500">
                    Mode duo 🔥 — tête-à-tête uniquement
                  </p>
                </div>
              </div>
              <p className="mt-4 flex-1 text-sm leading-relaxed text-stone-600">
                Le procureur satirique, zéro filtre. Il instruit le{" "}
                <strong className="text-stone-800">dossier de chacun</strong>{" "}
                avec pièces à conviction verbatim, superlatifs et métaphores
                chirurgicales. Pour les couples, les ex, les situationships —
                et les curieux qui assument.
              </p>
              <Link
                href="/roast"
                className="mt-6 inline-block self-start rounded-full bg-stone-900 px-6 py-3 text-sm font-bold text-white shadow-md transition hover:bg-stone-700"
              >
                🗂️ Ouvrir un dossier →
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Comment ça marche */}
      <section className="papier-peint py-20" id="comment">
        <div className="mx-auto max-w-5xl px-5">
          <h2 className="text-center text-3xl font-extrabold tracking-tight text-teal">
            Trois étapes. <span className="voice">Zéro prise de tête.</span>
          </h2>
          <div className="mt-12 grid gap-6 md:grid-cols-3">
            {ETAPES.map((e, i) => (
              <div key={e.titre} className="carte p-6">
                <span className="flex h-10 w-10 items-center justify-center rounded-full bg-vert text-base font-extrabold text-teal">
                  {i + 1}
                </span>
                <h3 className="mt-4 text-lg font-bold text-teal">{e.titre}</h3>
                <p className="mt-2 text-sm leading-relaxed text-gris">
                  {e.texte}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Le rapport */}
      <section className="bg-blanc py-20">
        <div className="mx-auto max-w-3xl px-5">
          <h2 className="text-center text-3xl font-extrabold tracking-tight text-teal">
            Un rapport <span className="voice">complet</span>, pas un gadget
          </h2>
          <div className="mt-10 flex flex-col gap-3">
            {[
              ["💬 Ce qu'il a ressenti", "Sa première impression, sincère — ce qui l'a fait rire, ce qui l'a touché."],
              ["🎭 Les personnages", "Un portrait tendre et précis de chaque participant, appuyé sur ses messages réels."],
              ["🔬 Ce qui se joue vraiment", "L'analyse approfondie : chiffres, déséquilibres, patterns, non-dits."],
              ["📌 Les moments qui disent tout", "Les messages pivots, cités mot pour mot, et ce qu'ils révèlent."],
              ["🏆 Les superlatifs", "Des récompenses que personne n'a demandées, décernées avec précision."],
              ["⚖️ Son avis, sans détour", "Un verdict objectif : le positif comme ce qui coince, faits à l'appui."],
              ["🧭 Les conseils de Steve", "3 à 5 conseils concrets et réalistes pour améliorer la situation — et un mot d'encouragement."],
            ].map(([titre, texte]) => (
              <div key={titre} className="carte flex items-start gap-4 p-5">
                <p className="shrink-0 font-bold text-teal">{titre}</p>
                <p className="text-sm text-gris">{texte}</p>
              </div>
            ))}
          </div>
          <p className="mt-8 text-center text-sm text-gris">
            À lire dans ton espace, à télécharger en PDF, ou à effacer
            définitivement avec le bouton{" "}
            <strong className="text-danger">« Supprimer mes données »</strong>.
          </p>
        </div>
      </section>

      {/* Sécurité */}
      <section className="bg-teal py-20 text-white">
        <div className="mx-auto max-w-3xl px-5 text-center">
          <p className="text-4xl">🔐</p>
          <h2 className="mt-4 text-3xl font-extrabold tracking-tight">
            Tes données, <span className="voice">ta décision</span>
          </h2>
          <div className="mx-auto mt-8 grid max-w-2xl gap-4 text-left sm:grid-cols-2">
            {[
              ["Conversations jamais stockées", "Elles servent à écrire le rapport, puis elles sont oubliées. Point."],
              ["Mots de passe protégés", "Hachés avec sel (scrypt), jamais lisibles, même par le propriétaire."],
              ["Sessions maîtrisées", "Cookies HttpOnly, jetons révocables, tentatives de connexion limitées."],
              ["Suppression en un clic", "Le bouton « Supprimer mes données » efface tes rapports, immédiatement."],
            ].map(([t, x]) => (
              <div key={t} className="rounded-xl bg-white/10 p-4">
                <p className="font-bold">{t}</p>
                <p className="mt-1 text-sm text-white/75">{x}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="papier-peint py-20" id="faq">
        <div className="mx-auto max-w-3xl px-5">
          <h2 className="text-center text-3xl font-extrabold tracking-tight text-teal">
            Questions <span className="voice">fréquentes</span>
          </h2>
          <div className="mt-10 flex flex-col gap-3">
            {FAQ.map((item) => (
              <details key={item.q} className="carte group p-5">
                <summary className="cursor-pointer list-none font-bold text-encre marker:hidden">
                  <span className="mr-2 inline-block text-vert-fonce transition group-open:rotate-90">
                    ▸
                  </span>
                  {item.q}
                </summary>
                <p className="mt-3 pl-6 text-sm leading-relaxed text-gris">
                  {item.r}
                </p>
              </details>
            ))}
          </div>
        </div>
      </section>

      {/* CTA final */}
      <section className="bg-blanc py-20">
        <div className="mx-auto max-w-3xl px-5 text-center">
          <h2 className="text-3xl font-extrabold leading-tight tracking-tight text-teal md:text-4xl">
            Ta conversation a des choses à dire.
            <br />
            <span className="voice text-teal-2">
              Steve va les écouter — et t&apos;aider à y voir clair.
            </span>
          </h2>
          <Link
            href="/inscription"
            className="btn-vert mt-9 inline-block px-9 py-4 text-lg"
          >
            Créer mon compte gratuit →
          </Link>
        </div>
      </section>

      <footer className="bg-teal py-8 text-white/80">
        <div className="mx-auto flex max-w-5xl flex-col items-center gap-2 px-5 text-center text-xs">
          <p className="voice text-sm text-white">
            Que pense Steve — des rapports humains sur tes conversations.
          </p>
          <p>
            Projet de démonstration, sans paiement. Rapports générés par Claude
            (Anthropic). Conversations jamais stockées, jamais utilisées pour
            l&apos;entraînement.
          </p>
        </div>
      </footer>
    </main>
  );
}
