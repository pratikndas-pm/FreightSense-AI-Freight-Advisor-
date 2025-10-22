export const metadata = { title: "FreightSense", description: "AI Freight Advisor" };
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen">
        <div className="mx-auto max-w-6xl p-6">
          <header className="flex items-center justify-between mb-6">
            <h1 className="text-2xl font-bold">🚢 FreightSense — AI Freight Advisor</h1>
            <a className="text-sm underline" href="https://github.com/pratikndas-pm" target="_blank">GitHub</a>
          </header>
          {children}
        </div>
      </body>
    </html>
  );
}
