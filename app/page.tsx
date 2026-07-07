import Link from "next/link";

const TYPES_DE_CONVERSATIONS = [
  {
    emoji: "👯",
    titre: "Le groupe de potes",
    texte:
      "Qui porte le groupe, qui ghoste, qui répond « mdr » à tout. Bertrand distribue les rôles.",
  },
  {
    emoji: "❤️",
    titre: "Le couple",
    texte:
      "L'équilibre des messages, qui s'excuse en premier, qui laisse en vu. Verdict sans anesthésie.",
  },
  {
    emoji: "👨‍👩‍👧",
    titre: "La famille",
    texte:
      "Le groupe familial, ses chaînes de bonjour, ses photos floues et ses non-dits. Bertrand a tout lu.",
  },
  {
    emoji: "💼",
    titre: "Le boulot",
    texte:
      "Les « petit point rapide ? », les 👍 passifs-agressifs, les messages du dimanche soir. Il voit tout.",
  },
  {
    emoji: "🫠",
    titre: "La situationship",
    texte:
      "Trois semaines de silence puis « tu me manques ». Bertrand te dit ce que tu refuses de voir.",
  },
  {
    emoji: "🔥",
    titre: "Le chaos total",
    texte:
      "Plus c'est le bazar, mieux c'est. Les conversations les plus gênantes font les meilleurs rapports.",
  },
];

const ETAPES = [
  {
    numero: "01",
    titre: "Exporte ta conversation",
    texte:
      "Depuis WhatsApp : Paramètres du chat → Exporter la discussion → Sans les médias. Un fichier .txt, c'est tout ce qu'il faut. Environ 2 minutes.",
  },
  {
    numero: "02",
    titre: "Bertrand lit tout",
    texte:
      "Chaque message. Les pics d'activité, les silences, les private jokes, les patterns que personne n'assume. Rien ne lui échappe.",
  },
  {
    numero: "03",
    titre: "Reçois ton rapport",
    texte:
      "Quelques minutes plus tard : un rapport complet avec son vrai avis, les dynamiques du groupe, les superlatifs et le verdict final.",
  },
];

const SUPERLATIFS = [
  "🏆 Prix du « vu à 14h02, répond à 23h58 »",
  "🏆 Prix du plus beau « on se fait un call pour en parler »",
  "🏆 Prix du ministre du mdr",
  "🏆 Prix de la réponse la plus courte à la question la plus longue",
  "🏆 Prix du « je regarde et je te dis »",
  "🏆 Prix du fantôme qui like quand même",
  "🏆 Prix du retour de flamme à 2h47",
];

const CONTENU_RAPPORT = [
  [
    "La première impression",
    "Ce que Bertrand a pensé de vous au bout de 200 messages. Spoiler : il a déjà tout compris.",
  ],
  [
    "Les rôles de chacun",
    "Le leader autoproclamé, le fantôme, le ministre du « mdr », l'archiviste des screenshots.",
  ],
  [
    "Les dynamiques",
    "Qui relance, qui s'éclipse, qui répond en 0,3 seconde à 3h du matin. Les chiffres ne mentent pas.",
  ],
  [
    "Les superlatifs",
    "Des récompenses que personne n'a demandées, décernées avec une précision chirurgicale.",
  ],
  [
    "Le verdict final",
    "Son avis global, sans filtre, sur ce que cette conversation dit de vous. Courage.",
  ],
];

const FAQ = [
  {
    q: "C'est qui, Bertrand ?",
    r: "Bertrand est une IA. Il lit les messages de ta conversation et écrit ce qu'il en pense vraiment — les dynamiques, les rôles de chacun, les moments gênants, le verdict. Il est honnête. Parfois trop.",
  },
  {
    q: "Quelles conversations je peux lui donner ?",
    r: "Groupes d'amis, couple, famille, collègues, situationships… Tout export WhatsApp (.txt) ou texte copié-collé fonctionne. Plus c'est le bazar, meilleur c'est le rapport.",
  },
  {
    q: "Mes conversations sont stockées quelque part ?",
    r: "Non. La conversation que tu envoies sert uniquement à écrire ton rapport, puis elle est oubliée. Rien n'est enregistré en base de données, rien n'est utilisé pour entraîner des modèles.",
  },
  {
    q: "Combien de temps ça prend ?",
    r: "Environ 2 minutes de ton côté pour exporter la conversation, et quelques minutes pour que Bertrand écrive le rapport. Tu le vois s'écrire en direct.",
  },
  {
    q: "Qui écrit vraiment le rapport ?",
    r: "Claude, le modèle d'IA d'Anthropic, incarne Bertrand. Tes messages ne servent pas à entraîner le modèle.",
  },
  {
    q: "Les autres membres du groupe sauront ?",
    r: "Seulement si tu partages le rapport. Ce que tu en fais ensuite — le balancer dans le groupe, par exemple — c'est ta responsabilité. On décline toute implication dans les drames qui suivront.",
  },
];

function Telephone() {
  return (
    <div className="relative">
      <span className="tampon absolute -top-4 right-2 z-10 rounded-lg px-3 py-1.5 sm:-right-4">
        Rapport n°4812 — confidentiel (ou pas)
      </span>
      <div className="telephone relative mx-auto w-full max-w-sm p-3">
        {/* En-tête du chat */}
        <div className="flex items-center gap-3 rounded-t-[1.8rem] border-b border-line bg-ink-2 px-4 py-3">
          <div className="flex h-9 w-9 items-center justify-center rounded-full bg-green-deep text-sm font-bold text-green">
            V24
          </div>
          <div className="flex-1">
            <p className="text-sm font-bold leading-tight">Vacances 2024</p>
            <p className="flex items-center gap-1.5 text-[11px] text-dim">
              <span className="inline-block h-1.5 w-1.5 rounded-full bg-green" />
              4 membres, 0 vacances
            </p>
          </div>
          <p className="etiquette text-dim">23:58</p>
        </div>
        {/* Messages */}
        <div className="flex flex-col gap-2.5 px-3 py-4">
          <div className="bulle-in" style={{ animationDelay: "0.2s" }}>
            <p className="mb-0.5 text-[10px] font-bold text-green">Karim</p>
            bon on les fait ces vacances ou pas 😤
          </div>
          <div className="bulle-in" style={{ animationDelay: "0.7s" }}>
            <p className="mb-0.5 text-[10px] font-bold text-accent-2">Julie</p>
            je regarde et je te dis
          </div>
          <div className="bulle-out" style={{ animationDelay: "1.2s" }}>
            mdrrr
          </div>
          <div className="bulle-bertrand" style={{ animationDelay: "1.9s" }}>
            <p className="mb-0.5 text-[10px] font-bold text-accent">
              Bertrand 🧠
            </p>
            J&apos;ai lu vos 4 812 messages. Julie, « je regarde et je te
            dis » : tu as regardé 9 fois. Tu n&apos;as jamais dit.
          </div>
          <div
            className="bulle-bertrand"
            style={{ animationDelay: "2.6s" }}
          >
            <p className="mb-0.5 text-[10px] font-bold text-accent">
              Bertrand 🧠
            </p>
            Ce groupe s&apos;appelle « Vacances 2024 ». Personne n&apos;est
            parti en vacances. Ce n&apos;est pas un groupe de voyage,
            c&apos;est un mémorial.
          </div>
          <div
            className="bulle-in flex items-center gap-2"
            style={{ animationDelay: "3.4s" }}
          >
            <span className="points-frappe">
              <span />
              <span />
              <span />
            </span>
            <span className="text-[11px] text-dim">
              Bertrand rédige le verdict…
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function Home() {
  return (
    <main className="flex-1">
      {/* Nav */}
      <header className="sticky top-0 z-20 border-b border-line bg-ink/85 backdrop-blur">
        <div className="mx-auto flex max-w-5xl items-center justify-between px-5 py-3.5">
          <Link href="/" className="flex items-center gap-2">
            <span className="flex h-8 w-8 items-center justify-center rounded-xl bg-gradient-to-br from-accent to-accent-2 text-base">
              🧠
            </span>
            <span className="voice text-lg font-bold">Que pense Bertrand</span>
          </Link>
          <nav className="flex items-center gap-5 text-sm text-dim">
            <a href="#comment" className="hidden hover:text-paper sm:block">
              Comment ça marche
            </a>
            <a href="#faq" className="hidden hover:text-paper sm:block">
              FAQ
            </a>
            <Link
              href="/rapport"
              className="btn-accent rounded-full px-4 py-2 text-sm font-bold"
            >
              Mon rapport
            </Link>
          </nav>
        </div>
      </header>

      {/* Hero */}
      <section className="halo">
        <div className="mx-auto grid max-w-5xl items-center gap-14 px-5 pb-20 pt-16 md:grid-cols-[1.1fr_0.9fr] md:pt-24">
          <div>
            <p className="etiquette lever text-accent">
              Des rapports IA sur tes conversations
            </p>
            <h1
              className="lever mt-5 text-[2.6rem] font-extrabold leading-[1.05] tracking-tight md:text-6xl"
              style={{ animationDelay: "0.1s" }}
            >
              Bertrand lit ta conversation.
              <br />
              <span className="voice degrade-accent font-bold">
                Et il a des choses à dire.
              </span>
            </h1>
            <p
              className="lever mt-6 max-w-lg text-lg leading-relaxed text-dim"
              style={{ animationDelay: "0.2s" }}
            >
              Donne-lui un export WhatsApp ou iMessage — le groupe de potes, le
              couple, la famille, le boulot, la situationship. Il lit chaque
              message et écrit un rapport avec son vrai avis : les dynamiques,
              les private jokes, les verdicts.
            </p>
            <div
              className="lever mt-9 flex flex-wrap items-center gap-5"
              style={{ animationDelay: "0.3s" }}
            >
              <Link
                href="/rapport"
                className="btn-accent rounded-full px-7 py-3.5 text-base font-bold"
              >
                Obtenir mon rapport →
              </Link>
              <a
                href="#comment"
                className="text-sm font-semibold text-dim underline-offset-4 hover:text-paper hover:underline"
              >
                Comment ça marche ?
              </a>
            </div>
            <p
              className="lever mt-7 flex items-center gap-2 text-xs text-dim"
              style={{ animationDelay: "0.4s" }}
            >
              <span>🔒</span> Ta conversation n&apos;est jamais stockée. Elle
              sert à écrire le rapport, puis elle est oubliée.
            </p>
          </div>
          <Telephone />
        </div>
      </section>

      {/* Bandeau superlatifs */}
      <div className="marquee" aria-hidden>
        <div className="marquee-piste etiquette text-dim">
          {[...SUPERLATIFS, ...SUPERLATIFS].map((s, i) => (
            <span key={i} className="whitespace-nowrap">
              {s}
            </span>
          ))}
        </div>
      </div>

      {/* Types de conversations */}
      <section className="py-24">
        <div className="mx-auto max-w-5xl px-5">
          <p className="etiquette text-center text-accent">Le terrain de jeu</p>
          <h2 className="mt-3 text-center text-3xl font-extrabold tracking-tight md:text-4xl">
            Le bazar, c&apos;est sa{" "}
            <span className="voice degrade-accent">spécialité</span>
          </h2>
          <p className="mx-auto mt-4 max-w-xl text-center text-dim">
            Bertrand accepte toutes les conversations. Plus c&apos;est
            compliqué, plus il est content.
          </p>
          <div className="mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {TYPES_DE_CONVERSATIONS.map((t) => (
              <div key={t.titre} className="carte rounded-2xl p-6">
                <p className="text-3xl">{t.emoji}</p>
                <h3 className="mt-4 text-lg font-bold">{t.titre}</h3>
                <p className="mt-2 text-sm leading-relaxed text-dim">
                  {t.texte}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Comment ça marche */}
      <section id="comment" className="border-y border-line bg-ink-2 py-24">
        <div className="mx-auto max-w-5xl px-5">
          <p className="etiquette text-center text-accent">La procédure</p>
          <h2 className="mt-3 text-center text-3xl font-extrabold tracking-tight md:text-4xl">
            Trois étapes.{" "}
            <span className="voice degrade-accent">Aucune excuse.</span>
          </h2>
          <div className="mt-16 grid gap-10 md:grid-cols-3">
            {ETAPES.map((e, i) => (
              <div key={e.numero} className="relative">
                <div className="flex items-center gap-4">
                  <span className="etiquette flex h-11 w-11 shrink-0 items-center justify-center rounded-full border border-accent/50 text-sm font-bold text-accent">
                    {e.numero}
                  </span>
                  {i < ETAPES.length - 1 && (
                    <span
                      className="hidden h-px flex-1 border-t border-dashed border-line md:block"
                      aria-hidden
                    />
                  )}
                </div>
                <h3 className="mt-5 text-xl font-bold">{e.titre}</h3>
                <p className="mt-2.5 text-sm leading-relaxed text-dim">
                  {e.texte}
                </p>
              </div>
            ))}
          </div>
          <div className="mt-14 text-center">
            <Link
              href="/rapport"
              className="btn-accent inline-block rounded-full px-8 py-3.5 text-base font-bold"
            >
              C&apos;est parti →
            </Link>
          </div>
        </div>
      </section>

      {/* Contenu du rapport */}
      <section className="py-24">
        <div className="mx-auto max-w-5xl px-5">
          <p className="etiquette text-center text-accent">Pièces du dossier</p>
          <h2 className="mt-3 text-center text-3xl font-extrabold tracking-tight md:text-4xl">
            Dans chaque <span className="voice degrade-accent">rapport</span>
          </h2>
          <div className="mx-auto mt-12 flex max-w-3xl flex-col gap-3">
            {CONTENU_RAPPORT.map(([titre, texte], i) => (
              <div
                key={titre}
                className="carte flex items-start gap-5 rounded-2xl p-5"
              >
                <span className="etiquette mt-1 shrink-0 text-accent">
                  {String(i + 1).padStart(2, "0")}
                </span>
                <div>
                  <p className="font-bold">{titre}</p>
                  <p className="mt-1 text-sm leading-relaxed text-dim">
                    {texte}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Confidentialité */}
      <section className="border-y border-line bg-ink-2 py-24">
        <div className="mx-auto max-w-3xl px-5 text-center">
          <p className="text-4xl">🔒</p>
          <h2 className="mt-5 text-3xl font-extrabold tracking-tight">
            Tes messages restent entre toi et{" "}
            <span className="voice degrade-accent">Bertrand</span>
          </h2>
          <p className="mt-5 leading-relaxed text-dim">
            La conversation que tu envoies sert uniquement à écrire ton
            rapport. Elle n&apos;est jamais enregistrée en base de données,
            jamais partagée, jamais utilisée pour entraîner des modèles. Le
            rapport est généré par Claude, l&apos;IA d&apos;Anthropic, puis ta
            conversation est oubliée.
          </p>
        </div>
      </section>

      {/* FAQ */}
      <section id="faq" className="py-24">
        <div className="mx-auto max-w-3xl px-5">
          <p className="etiquette text-center text-accent">
            Questions fréquentes
          </p>
          <h2 className="mt-3 text-center text-3xl font-extrabold tracking-tight">
            Tout ce que tu n&apos;oses pas{" "}
            <span className="voice degrade-accent">demander</span>
          </h2>
          <div className="mt-12 flex flex-col gap-3">
            {FAQ.map((item) => (
              <details key={item.q} className="carte group rounded-2xl p-5">
                <summary className="cursor-pointer list-none font-bold marker:hidden">
                  <span className="mr-3 inline-block text-accent transition-transform group-open:rotate-90">
                    ▸
                  </span>
                  {item.q}
                </summary>
                <p className="mt-3 pl-7 text-sm leading-relaxed text-dim">
                  {item.r}
                </p>
              </details>
            ))}
          </div>
        </div>
      </section>

      {/* CTA final */}
      <section className="halo py-28">
        <div className="mx-auto max-w-3xl px-5 text-center">
          <h2 className="text-3xl font-extrabold leading-tight tracking-tight md:text-5xl">
            Ta conversation a des choses à cacher.
            <br />
            <span className="voice degrade-accent">
              Bertrand va les trouver.
            </span>
          </h2>
          <Link
            href="/rapport"
            className="btn-accent mt-10 inline-block rounded-full px-9 py-4 text-lg font-bold"
          >
            Obtenir mon rapport →
          </Link>
        </div>
      </section>

      <footer className="border-t border-line py-9">
        <div className="mx-auto flex max-w-5xl flex-col items-center gap-2 px-5 text-center text-xs text-dim">
          <p className="voice text-sm text-paper">
            Que pense Bertrand — des rapports IA sur tes conversations.
          </p>
          <p>
            Projet de démonstration, sans paiement. Rapports rédigés par Claude
            (Anthropic). Tes conversations ne sont ni stockées, ni utilisées
            pour l&apos;entraînement.
          </p>
        </div>
      </footer>
    </main>
  );
}
