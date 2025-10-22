'use client';
export default function RouteTable({ options }: { options: any[] }) {
  if (!options?.length) return null;
  return (
    <table className="w-full text-sm bg-white rounded-2xl shadow">
      <thead><tr className="text-left">
        <th className="p-3">Mode</th><th className="p-3">Carrier</th><th className="p-3">Transit (d)</th>
        <th className="p-3">Cost (USD)</th><th className="p-3">CO₂ (kg)</th><th className="p-3">Waypoints</th>
      </tr></thead>
      <tbody>
        {options.map((o, i) => (
          <tr key={i} className="border-t">
            <td className="p-3">{o.mode}</td>
            <td className="p-3">{o.carrier}</td>
            <td className="p-3">{o.transit_days}</td>
            <td className="p-3">{o.est_cost_usd}</td>
            <td className="p-3">{o.co2_kg}</td>
            <td className="p-3">{o.waypoints?.join(' → ')}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
