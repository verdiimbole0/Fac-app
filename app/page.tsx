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
    numero: "1",
    titre: "Exporte ta conversation",
    texte:
      "Depuis WhatsApp : Paramètres du chat → Exporter la discussion → Sans les médias. Un fichier .txt, c'est tout ce qu'il faut. Environ 2 minutes.",
  },
  {
    numero: "2",
    titre: "Bertrand lit tout",
    texte:
      "Chaque message. Les pics d'activité, les silences, les private jokes, les patterns que personne n'assume. Rien ne lui échappe.",
  },
  {
    numero: "3",
    titre: "Reçois ton rapport",
    texte:
      "Quelques minutes plus tard : un rapport complet avec son vrai avis, les dynamiques du groupe, les superlatifs et le verdict final.",
  },
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

function Bulle({
  auteur,
  children,
  droite = false,
}: {
  auteur: string;
  children: React.ReactNode;
  droite?: boolean;
}) {
  return (
    <div className={`flex ${droite ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-[85%] rounded-2xl px-4 py-2.5 text-sm leading-relaxed ${
          droite
            ? "bg-bubble text-paper rounded-br-sm"
            : "bg-ink-card text-paper rounded-bl-sm"
        }`}
      >
        <p className="text-[11px] font-semibold text-accent mb-0.5">{auteur}</p>
        {children}
      </div>
    </div>
  );
}

export default function Home() {
  return (
    <main className="flex-1">
      {/* Nav */}
      <header className="sticky top-0 z-20 border-b border-white/5 bg-ink/90 backdrop-blur">
        <div className="mx-auto flex max-w-5xl items-center justify-between px-5 py-4">
          <Link href="/" className="font-display text-lg font-bold text-accent">
            Que pense Bertrand
          </Link>
          <nav className="flex items-center gap-5 text-sm text-paper-dim">
            <a href="#comment" className="hidden hover:text-paper sm:block">
              Comment ça marche
            </a>
            <a href="#faq" className="hidden hover:text-paper sm:block">
              FAQ
            </a>
            <Link
              href="/rapport"
              className="rounded-full bg-accent px-4 py-2 text-sm font-bold text-ink transition hover:bg-accent-strong"
            >
              Mon rapport
            </Link>
          </nav>
        </div>
      </header>

      {/* Hero */}
      <section className="mx-auto grid max-w-5xl items-center gap-12 px-5 pb-20 pt-16 md:grid-cols-2 md:pt-24">
        <div>
          <p className="mb-4 inline-block rounded-full border border-accent/40 bg-accent/10 px-3 py-1 text-xs font-semibold uppercase tracking-widest text-accent">
            Des rapports IA sur tes conversations
          </p>
          <h1 className="font-display text-4xl font-bold leading-tight md:text-5xl">
            Bertrand lit ta conversation.
            <br />
            <span className="text-accent">Et il a des choses à dire.</span>
          </h1>
          <p className="mt-5 text-lg leading-relaxed text-paper-dim">
            Donne-lui un export WhatsApp ou iMessage — le groupe de potes, le
            couple, la famille, le boulot, la situationship. Il lit chaque
            message et écrit un rapport avec son vrai avis : les dynamiques,
            les private jokes, les verdicts.
          </p>
          <div className="mt-8 flex flex-wrap items-center gap-4">
            <Link
              href="/rapport"
              className="rounded-full bg-accent px-6 py-3 text-base font-bold text-ink transition hover:bg-accent-strong"
            >
              Obtenir mon rapport →
            </Link>
            <a
              href="#comment"
              className="text-sm font-semibold text-paper-dim underline-offset-4 hover:text-paper hover:underline"
            >
              Comment ça marche ?
            </a>
          </div>
          <p className="mt-6 text-xs text-paper-dim">
            🔒 Ta conversation n&apos;est jamais stockée. Elle sert à écrire le
            rapport, puis elle est oubliée.
          </p>
        </div>

        {/* Aperçu façon chat */}
        <div className="rounded-3xl border border-white/10 bg-ink-soft p-5 shadow-2xl">
          <p className="mb-4 text-center text-xs uppercase tracking-widest text-paper-dim">
            Extrait d&apos;un rapport de Bertrand
          </p>
          <div className="flex flex-col gap-3">
            <Bulle auteur="Bertrand 🧠">
              <p>
                J&apos;ai lu vos 4 812 messages. Commençons par l&apos;évidence :
                ce groupe s&apos;appelle « Vacances 2024 » et personne
                n&apos;est parti en vacances.
              </p>
            </Bulle>
            <Bulle auteur="Bertrand 🧠">
              <p>
                Karim a proposé 9 dates différentes. Il a reçu 9 fois « je
                regarde et je te dis ». Karim, tu mérites mieux.
              </p>
            </Bulle>
            <Bulle auteur="Bertrand 🧠" droite>
              <p>
                🏆 Superlatif « Vu à 14h02, répond à 23h58 » : décerné à Julie,
                pour l&apos;ensemble de son œuvre.
              </p>
            </Bulle>
          </div>
        </div>
      </section>

      {/* Types de conversations */}
      <section className="border-t border-white/5 bg-ink-soft py-20">
        <div className="mx-auto max-w-5xl px-5">
          <h2 className="font-display text-center text-3xl font-bold">
            Le bazar, c&apos;est sa spécialité
          </h2>
          <p className="mx-auto mt-3 max-w-xl text-center text-paper-dim">
            Bertrand accepte toutes les conversations. Plus c&apos;est
            compliqué, plus il est content.
          </p>
          <div className="mt-12 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {TYPES_DE_CONVERSATIONS.map((t) => (
              <div
                key={t.titre}
                className="rounded-2xl border border-white/5 bg-ink-card p-6 transition hover:border-accent/40"
              >
                <p className="text-3xl">{t.emoji}</p>
                <h3 className="mt-3 font-display text-lg font-bold text-accent">
                  {t.titre}
                </h3>
                <p className="mt-2 text-sm leading-relaxed text-paper-dim">
                  {t.texte}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Comment ça marche */}
      <section id="comment" className="py-20">
        <div className="mx-auto max-w-5xl px-5">
          <h2 className="font-display text-center text-3xl font-bold">
            Comment ça marche
          </h2>
          <p className="mx-auto mt-3 max-w-xl text-center text-paper-dim">
            Trois étapes. Aucune excuse.
          </p>
          <div className="mt-12 grid gap-8 md:grid-cols-3">
            {ETAPES.map((e) => (
              <div key={e.numero} className="relative">
                <p className="font-display text-6xl font-bold text-accent/20">
                  {e.numero}
                </p>
                <h3 className="mt-2 font-display text-xl font-bold text-accent">
                  {e.titre}
                </h3>
                <p className="mt-2 text-sm leading-relaxed text-paper-dim">
                  {e.texte}
                </p>
              </div>
            ))}
          </div>
          <div className="mt-12 text-center">
            <Link
              href="/rapport"
              className="inline-block rounded-full bg-accent px-8 py-3 text-base font-bold text-ink transition hover:bg-accent-strong"
            >
              C&apos;est parti →
            </Link>
          </div>
        </div>
      </section>

      {/* Ce que contient le rapport */}
      <section className="border-t border-white/5 bg-ink-soft py-20">
        <div className="mx-auto max-w-5xl px-5">
          <h2 className="font-display text-center text-3xl font-bold">
            Dans chaque rapport
          </h2>
          <div className="mx-auto mt-10 grid max-w-3xl gap-4 text-sm">
            {[
              ["🧠 La première impression", "Ce que Bertrand a pensé de vous au bout de 200 messages. Spoiler : il a déjà tout compris."],
              ["🎭 Les rôles de chacun", "Le leader autoproclamé, le fantôme, le ministre du « mdr », l'archiviste des screenshots."],
              ["📈 Les dynamiques", "Qui relance, qui s'éclipse, qui répond en 0,3 seconde à 3h du matin. Les chiffres ne mentent pas."],
              ["🏆 Les superlatifs", "Des récompenses que personne n'a demandées, décernées avec une précision chirurgicale."],
              ["⚖️ Le verdict final", "Son avis global, sans filtre, sur ce que cette conversation dit de vous. Courage."],
            ].map(([titre, texte]) => (
              <div
                key={titre}
                className="flex gap-4 rounded-2xl border border-white/5 bg-ink-card p-5"
              >
                <p className="shrink-0 font-bold text-accent">{titre}</p>
                <p className="text-paper-dim">{texte}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Confidentialité */}
      <section className="py-20">
        <div className="mx-auto max-w-3xl px-5 text-center">
          <p className="text-4xl">🔒</p>
          <h2 className="mt-4 font-display text-3xl font-bold">
            Tes messages restent entre toi et Bertrand
          </h2>
          <p className="mt-4 leading-relaxed text-paper-dim">
            La conversation que tu envoies sert uniquement à écrire ton
            rapport. Elle n&apos;est jamais enregistrée en base de données,
            jamais partagée, jamais utilisée pour entraîner des modèles. Le
            rapport est généré par Claude, l&apos;IA d&apos;Anthropic, puis ta
            conversation est oubliée.
          </p>
        </div>
      </section>

      {/* FAQ */}
      <section id="faq" className="border-t border-white/5 bg-ink-soft py-20">
        <div className="mx-auto max-w-3xl px-5">
          <h2 className="font-display text-center text-3xl font-bold">
            Questions fréquentes
          </h2>
          <div className="mt-10 flex flex-col gap-3">
            {FAQ.map((item) => (
              <details
                key={item.q}
                className="group rounded-2xl border border-white/5 bg-ink-card p-5"
              >
                <summary className="cursor-pointer list-none font-bold text-paper marker:hidden">
                  <span className="mr-2 inline-block text-accent transition group-open:rotate-90">
                    ▸
                  </span>
                  {item.q}
                </summary>
                <p className="mt-3 pl-6 text-sm leading-relaxed text-paper-dim">
                  {item.r}
                </p>
              </details>
            ))}
          </div>
        </div>
      </section>

      {/* CTA final */}
      <section className="py-20">
        <div className="mx-auto max-w-3xl px-5 text-center">
          <h2 className="font-display text-3xl font-bold md:text-4xl">
            Ta conversation a des choses à cacher.
            <br />
            <span className="text-accent">Bertrand va les trouver.</span>
          </h2>
          <Link
            href="/rapport"
            className="mt-8 inline-block rounded-full bg-accent px-8 py-4 text-lg font-bold text-ink transition hover:bg-accent-strong"
          >
            Obtenir mon rapport →
          </Link>
        </div>
      </section>

      <footer className="border-t border-white/5 py-8">
        <div className="mx-auto flex max-w-5xl flex-col items-center gap-2 px-5 text-center text-xs text-paper-dim">
          <p>
            Que pense Bertrand — des rapports IA sur tes conversations. Projet
            de démonstration, sans paiement.
          </p>
          <p>
            Rapports rédigés par Claude (Anthropic). Tes conversations ne sont
            ni stockées, ni utilisées pour l&apos;entraînement.
          </p>
        </div>
      </footer>
    </main>
  );
}
