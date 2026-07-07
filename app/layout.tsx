import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Que pense Bertrand — Des rapports IA sur tes conversations",
  description:
    "Bertrand est une IA qui lit tes conversations WhatsApp ou iMessage et écrit ce qu'il en pense vraiment. Les dynamiques, les private jokes, les verdicts.",
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
