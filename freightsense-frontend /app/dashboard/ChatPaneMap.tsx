'use client';
import { useState } from 'react';
import dynamic from 'next/dynamic';

const MapView = dynamic(() => import('../../components/MapView'), { ssr: false });

async function getJSON(path: string, params: Record<string, string | number>) {
  const url = new URL(path, typeof window !== 'undefined' ? window.location.origin : 'http://localhost');
  Object.entries(params).forEach(([k, v]) => url.searchParams.set(k, String(v)));
  const r = await fetch(url.toString(), { cache: 'no-store' });
  if (!r.ok) throw new Error('API error');
  return r.json();
}

export default function ChatPaneMap() {
  const [origin, setOrigin] = useState('Dubai');
  const [destination, setDestination] = useState('Hamburg');
  const [quote, setQuote] = useState<any>(null);
  const [routes, setRoutes] = useState<any[]>([]);
  const [track, setTrack] = useState<any>(null);

  const onQuote = async () => setQuote(await getJSON('/api/freight/quote', { origin, destination, equipment: '40FT' }));
  const onRoute = async () => { const d = await getJSON('/api/freight/route', { origin, destination, priority: 'time' }); setRoutes(d.options); };
  const onTrack = async () => setTrack(await getJSON('/api/freight/track', { container_id: 'ABCD123456' }));
  const onLeads = async () => alert(JSON.stringify(await getJSON('/api/freight/leads', {}), null, 2));

  return (
    <div className="bg-white rounded-2xl shadow p-4 space-y-4">
      <div className="grid sm:grid-cols-4 gap-3">
        <input className="border rounded-xl p-2" value={origin} onChange={e=>setOrigin(e.target.value)} placeholder="Origin" />
        <input className="border rounded-xl p-2" value={destination} onChange={e=>setDestination(e.target.value)} placeholder="Destination" />
        <div className="flex gap-2">
          <button onClick={onQuote} className="px-3 py-2 rounded-xl bg-slate-900 text-white">Quote</button>
          <button onClick={onRoute} className="px-3 py-2 rounded-xl bg-slate-200">Route</button>
          <button onClick={onTrack} className="px-3 py-2 rounded-xl bg-slate-200">Track</button>
        </div>
        <button onClick={onLeads} className="px-3 py-2 rounded-xl bg-emerald-600 text-white">Leads</button>
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
        <div className="text-sm">
          <h3 className="font-semibold mb-2">Route Options</h3>
          <ul className="list-disc ml-5">
            {routes.map((o:any, i:number) => (
              <li key={i}>{o.carrier} • {o.mode} • {o.transit_days}d • ${o.est_cost_usd} • CO₂ {o.co2_kg}kg</li>
            ))}
          </ul>
        </div>
      ) : null}

      {track && (
        <div className="space-y-2">
          <div className="text-sm">
            <b>Location:</b> {track.location} ({track.lat.toFixed(2)}, {track.lon.toFixed(2)}) ·
            <b> ETA:</b> {new Date(track.eta_iso).toUTCString()} ± {track.eta_confidence_hours}h ·
            <b> Risk:</b> {track.risk} — {track.reason}
          </div>
          <MapView lat={track.lat} lon={track.lon} label={track.location} />
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
