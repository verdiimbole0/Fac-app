import { detruireSession, origineValide } from "@/lib/auth";

export async function POST() {
  if (!(await origineValide())) {
    return Response.json({ erreur: "Origine non autorisée." }, { status: 403 });
  }
  await detruireSession();
  return Response.json({ ok: true });
}
