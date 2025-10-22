'use client';
export default function KpiCards({ quoteTime, etaMae, csat }: { quoteTime: number; etaMae: number; csat: number; }) {
  const card = "bg-white rounded-2xl shadow p-4";
  return (
    <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
      <div className={card}><div className="text-sm text-slate-500">Time to Quote</div><div className="text-2xl font-semibold">{quoteTime}s</div></div>
      <div className={card}><div className="text-sm text-slate-500">ETA MAE</div><div className="text-2xl font-semibold">{etaMae}h</div></div>
      <div className={card}><div className="text-sm text-slate-500">CSAT</div><div className="text-2xl font-semibold">{csat}%</div></div>
    </div>
  );
}
