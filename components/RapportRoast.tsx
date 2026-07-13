import type {
  DossierPersonne,
  PieceAConviction,
  RapportRoastData,
  TeasingSection,
} from "@/lib/roast";

/**
 * RapportRoast — affichage « Rapport Classique » du dossier de Brandon.
 *
 * Autonome : uniquement des classes Tailwind standard (aucun token custom),
 * réutilisable tel quel dans n'importe quel projet Next.js / Tailwind.
 * Rendu pensé pour le scan : phrases courtes, gras chirurgical (**…** dans
 * les chaînes), citations isolées en <blockquote> monospace.
 */

/** Rend le gras markdown (**mot**) en <strong>, sans lib externe. */
function Gras({ texte }: { texte: string }) {
  const segments = texte.split(/(\*\*[^*]+\*\*)/g);
  return (
    <>
      {segments.map((s, i) =>
        s.startsWith("**") && s.endsWith("**") ? (
          <strong key={i} className="font-bold text-stone-900">
            {s.slice(2, -2)}
          </strong>
        ) : (
          <span key={i}>{s}</span>
        ),
      )}
    </>
  );
}

/** Séparateur de section : icône minimaliste + filet. */
function Separateur({ icone }: { icone: string }) {
  return (
    <div className="my-10 flex items-center gap-4" aria-hidden>
      <hr className="flex-1 border-stone-200" />
      <span className="text-lg">{icone}</span>
      <hr className="flex-1 border-stone-200" />
    </div>
  );
}

/** Citation verbatim du chat + tacle de Brandon. */
function Piece({
  piece,
  numero,
}: {
  piece: PieceAConviction;
  numero: number;
}) {
  return (
    <figure className="my-4">
      <p className="mb-1.5 text-[11px] font-bold uppercase tracking-[0.18em] text-stone-400">
        Pièce à conviction n°{numero}
      </p>
      <blockquote className="rounded-r-lg border-l-4 border-stone-800 bg-stone-100 px-4 py-3 font-mono text-[13px] leading-relaxed text-stone-800">
        « {piece.citation} »
      </blockquote>
      <figcaption className="mt-2 pl-4 text-sm italic text-stone-600">
        — <Gras texte={piece.tacle} />
      </figcaption>
    </figure>
  );
}

/** Le dossier psychologique d'une personne. */
function Dossier({ dossier }: { dossier: DossierPersonne }) {
  return (
    <section>
      <header>
        <p className="text-[11px] font-bold uppercase tracking-[0.18em] text-stone-400">
          📁 Le dossier de
        </p>
        <h2 className="mt-1 font-serif text-2xl font-bold text-stone-900">
          {dossier.nom}
          <span className="ml-2 text-lg font-normal italic text-stone-500">
            — {dossier.surnom}
          </span>
        </h2>
      </header>
      <div className="mt-4 flex flex-col gap-3">
        {dossier.analyse.map((paragraphe, i) => (
          <p key={i} className="max-w-prose text-[15px] leading-relaxed text-stone-700">
            <Gras texte={paragraphe} />
          </p>
        ))}
      </div>
      <div className="mt-5">
        {dossier.pieces_a_conviction.map((piece, i) => (
          <Piece key={i} piece={piece} numero={i + 1} />
        ))}
      </div>
    </section>
  );
}

function Teasing({ sections }: { sections: TeasingSection[] }) {
  return (
    <section>
      <p className="text-center text-[11px] font-bold uppercase tracking-[0.18em] text-stone-400">
        Dans la suite du rapport
      </p>
      <div className="mt-5 grid gap-3 sm:grid-cols-3">
        {sections.map((s) => (
          <div
            key={s.titre}
            className="rounded-xl border border-stone-200 bg-stone-50 p-4 text-center"
          >
            <p className="text-2xl" aria-hidden>
              {s.icone}
            </p>
            <p className="mt-2 font-serif text-base font-bold text-stone-900">
              {s.titre}
            </p>
            <p className="mt-1.5 text-xs leading-relaxed text-stone-500">
              <Gras texte={s.accroche} />
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default function RapportRoast({
  rapport,
}: {
  rapport: RapportRoastData;
}) {
  const [dossierA, dossierB] = rapport.dossiers;
  return (
    <article className="mx-auto max-w-2xl rounded-2xl border border-stone-200 bg-white px-6 py-10 shadow-sm sm:px-10">
      {/* En-tête du rapport */}
      <header className="text-center">
        <p className="text-[11px] font-bold uppercase tracking-[0.24em] text-stone-400">
          Rapport d&apos;analyse — confidentiel (en théorie)
        </p>
        <h1 className="mx-auto mt-3 max-w-xl text-balance font-serif text-3xl font-bold leading-tight text-stone-900">
          {rapport.titre}
        </h1>
        <p className="mx-auto mt-4 max-w-prose text-[15px] leading-relaxed text-stone-700">
          <Gras texte={rapport.intro} />
        </p>
        {/* Bandeau de statistiques */}
        <dl className="mx-auto mt-6 flex max-w-lg flex-wrap justify-center gap-x-8 gap-y-2 border-y border-stone-200 py-3 font-mono text-xs text-stone-500 [font-variant-numeric:tabular-nums]">
          <div>
            <dt className="sr-only">Messages analysés</dt>
            <dd>
              💬 {rapport.statistiques.nb_messages.toLocaleString("fr-FR")}{" "}
              messages
            </dd>
          </div>
          <div>
            <dt className="sr-only">Période</dt>
            <dd>📅 {rapport.statistiques.periode}</dd>
          </div>
          <div>
            <dt className="sr-only">Ratio</dt>
            <dd>⚖️ {rapport.statistiques.ratio_messages}</dd>
          </div>
        </dl>
      </header>

      <Separateur icone="📁" />
      {dossierA && <Dossier dossier={dossierA} />}

      <Separateur icone="📁" />
      {dossierB && <Dossier dossier={dossierB} />}

      <Separateur icone="🔮" />
      <Teasing sections={rapport.teasing} />

      <footer className="mt-10 text-center">
        <p className="font-serif text-sm italic text-stone-500">— Brandon</p>
      </footer>
    </article>
  );
}
