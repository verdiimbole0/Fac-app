import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Que pense Steve — Des rapports humains sur tes conversations",
  description:
    "Steve lit tes conversations WhatsApp ou iMessage, mène une analyse approfondie et te dit ce qu'il en pense vraiment — avec humour, cœur et des conseils concrets.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="fr" className="h-full antialiased">
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
