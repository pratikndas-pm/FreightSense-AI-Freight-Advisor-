import KpiCards from "../../components/KpiCards";
import ChatPaneMap from "../../components/ChatPaneMap";

export default function DashboardPage() {
  return (
    <main>
      <KpiCards quoteTime={42} etaMae={6} csat={82} />
      <ChatPaneMap />
    </main>
  );
}
