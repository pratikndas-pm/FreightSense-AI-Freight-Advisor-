'use client';
import { useState } from 'react';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || '';

export default function ChatPane() {
  const [origin, setOrigin] = useState('Dubai');
  const [destination, setDestination] = useState('Hamburg');
  const [quote, setQuote] = useState<any>(null);
  const [routes, setRoutes] = useState<any[]>([]);
  const [track, setTrack] = useState<any>(null);

  async function fetchJSON(path: string, body: any) {
    const res = await fetch(`${API_BASE}${path}`, {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body)
    });
    if (!res.ok) throw new Error('API error');
    return res.json();
  }

  const onQuote = async () => {
    const data = await fetchJSON('/generate_quote', { origin, destination, equipment: '40FT' });
    setQuote(data);
  };

  const onRoute = async () => {
    const data = await fetchJSON('/plan_route', { origin, destination, priority: 'time' });
    setRoutes(data.options);
  };

  const onTrack = async () => {
    const data = await fetchJSON('/track', { container_id: 'ABCD123456' });
    setTrack(data);
  };

  return (
    <div className="bg-white rounded-2xl shadow p-4 space-y-4">
      <div className="grid sm:grid-cols-3 gap-3">
        <input className="border rounded-xl p-2" value={origin} onChange={e=>setOrigin(e.target.value)} placeholder="Origin" />
        <input className="border rounded-xl p-2" value={destination} onChange={e=>setDestination(e.target.value)} placeholder="Destination" />
        <div className="flex gap-2">
          <button onClick={onQuote} className="px-3 py-2 rounded-xl bg-slate-900 text-white">Quote</button>
          <button onClick={onRoute} className="px-3 py-2 rounded-xl bg-slate-200">Route</button>
          <button onClick={onTrack} className="px-3 py-2 rounded-xl bg-slate-200">Track</button>
        </div>
      </div>

      {quote && (
        <div className="grid sm:grid-cols-5 gap-3">
          <Card label="Base" val={`$${quote.base_rate_usd.toLocaleString()}`} />
          <Card label="Surcharges" val={`$${quote.surcharges_usd.toLocaleString()}`} />
          <Card label="Total" val={`$${quote.total_usd.toLocaleString()}`} />
          <Card label="Margin" val={`${quote.margin_pct}%`} />
          <Card label="ETA" val={`${quote.eta_days} days`} />
        </div>
      )}

      {routes?.length ? (
        <div>
          <h3 className="font-semibold mb-2">Route Options</h3>
        </div>
      ) : null}

      {track && (
        <div className="text-sm">
          <div><b>Location:</b> {track.location} ({track.lat.toFixed(2)}, {track.lon.toFixed(2)})</div>
          <div><b>ETA:</b> {new Date(track.eta_iso).toUTCString()} ± {track.eta_confidence_hours}h</div>
          <div><b>Risk:</b> {track.risk} — {track.reason}</div>
        </div>
      )}
    </div>
  );
}

function Card({ label, val }: { label: string; val: string }) {
  return (
    <div className="bg-slate-50 rounded-xl p-3 border">
      <div className="text-xs text-slate-500">{label}</div>
      <div className="text-xl font-semibold">{val}</div>
    </div>
  );
}
