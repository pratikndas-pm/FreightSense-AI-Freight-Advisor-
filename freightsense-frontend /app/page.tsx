import KpiCards from "../components/KpiCards";
import ChatPane from "../components/ChatPane";

export default function Page() {
  return (
    <main>
      <KpiCards quoteTime={42} etaMae={6} csat={82} />
      <ChatPane />
    </main>
  );
}
