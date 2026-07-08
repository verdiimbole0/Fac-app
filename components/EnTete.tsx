import Link from "next/link";
import { utilisateurCourant } from "@/lib/auth";
import BoutonDeconnexion from "./BoutonDeconnexion";

// Barre supérieure façon WhatsApp : bandeau sarcelle, avatar, actions.
export default async function EnTete() {
  const u = await utilisateurCourant();
  return (
    <header className="sticky top-0 z-20 bg-teal text-white shadow-md">
      <div className="mx-auto flex max-w-5xl items-center justify-between gap-3 px-5 py-3">
        <Link href="/" className="flex items-center gap-2.5">
          <span className="flex h-9 w-9 items-center justify-center rounded-full bg-vert text-lg font-bold text-teal">
            S
          </span>
          <span className="voice text-lg font-bold">Que pense Steve</span>
        </Link>
        <nav className="flex items-center gap-4 text-sm">
          {u ? (
            <>
              <Link
                href="/mes-rapports"
                className="hidden text-white/80 hover:text-white sm:block"
              >
                Mes rapports
              </Link>
              <Link
                href="/roast"
                className="hidden text-white/80 hover:text-white sm:block"
                title="Mode duo : le rapport de Brandon"
              >
                Duo 🔥
              </Link>
              {u.role === "admin" && (
                <Link
                  href="/admin"
                  className="hidden text-white/80 hover:text-white sm:block"
                >
                  Gestion
                </Link>
              )}
              <BoutonDeconnexion />
              <Link
                href="/rapport"
                className="btn-vert px-4 py-2 text-sm"
              >
                Parler à Steve
              </Link>
            </>
          ) : (
            <>
              <Link
                href="/connexion"
                className="text-white/80 hover:text-white"
              >
                Connexion
              </Link>
              <Link href="/inscription" className="btn-vert px-4 py-2 text-sm">
                S&apos;inscrire
              </Link>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}
