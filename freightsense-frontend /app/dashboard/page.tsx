import dynamic from "next/dynamic";
const ChatPaneMap = dynamic(() => import("./ChatPaneMap"), { ssr: false });

export default function DashboardPage() {
  return (
    <main className="mx-auto max-w-6xl p-6">
      <h1 className="text-2xl font-bold mb-4">🚢 FreightSense — Dashboard</h1>
      <ChatPaneMap />
    </main>
  );
}
