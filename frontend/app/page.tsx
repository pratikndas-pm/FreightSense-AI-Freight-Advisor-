
'use client';
import React, { useState } from 'react';
type Card = { type: string; title?: string; data?: any };
type ApiResp = { message: string; cards?: Card[]; confidence?: number; telemetry?: any; };
const API = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
export default function Page() {
  const [text, setText] = useState('');
  const [msgs, setMsgs] = useState<{role:'user'|'ai', text:string, cards?:Card[] }[]>([
    {role:'ai', text:"Hi! Try: /quote 40FT Dubai Hamburg nextweek, /route Shanghai Rotterdam green, /track ABCD123456, /leads today, /docs What is BAF surcharge?, /docs_vector What is BAF surcharge?"}
  ]);
  async function send() {
    if(!text.trim()) return;
    const user = {role:'user' as const, text}; setMsgs(m=>[...m,user]); setText('');
    const resp = await fetch(`${API}/chat`, { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({message: user.text}) });
    const json: ApiResp = await resp.json(); const ai = {role:'ai' as const, text: json.message, cards: json.cards}; setMsgs(m=>[...m, ai]);
  }
  async function downloadPDF(data:any){
    const resp = await fetch(`${API}/export/quote_pdf_from_data`, {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(data)});
    const blob = await resp.blob(); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href=url; a.download='quote.pdf'; a.click(); URL.revokeObjectURL(url);
  }
  function CardView(c: Card, i:number) {
    if(c.type === 'quote') { const d=c.data;
      return (<div key={i} style={{border:'1px solid #eee', padding:12, borderRadius:12}}>
        <b>{c.title}</b>
        <div>Lane: {d.origin} → {d.destination} ({d.equipment})</div>
        <div>Predicted base: ${d.predicted_base}</div>
        <div>Surcharges: {Object.entries(d.surcharges||{}).map(([k,v])=>`${k}: $${v}`).join(', ')}</div>
        <div>Total: <b>${d.total}</b> | ETA: {d.eta_days} days | Margin: {d.margin_pct}%</div>
        {d.warning && <div style={{color:'tomato'}}>{d.warning}</div>}
        <button onClick={()=>downloadPDF(d)} style={{marginTop:8, padding:'6px 10px', border:'1px solid #ddd', borderRadius:8}}>Download PDF</button>
      </div> ); }
    if(c.type === 'table'){ const rows=c.data||[];
      return (<div key={i} style={{border:'1px solid #eee', padding:12, borderRadius:12}}>
        <b>{c.title}</b>
        <table style={{width:'100%', marginTop:8}}><thead><tr><th>Carrier</th><th>Mode</th><th>Cost</th><th>ETA(d)</th><th>CO₂ idx</th><th>Score</th></tr></thead>
        <tbody>{rows.map((r:any,idx:number)=>(<tr key={idx}><td>{r.carrier}</td><td>{r.mode}</td><td>${r.cost}</td><td>{r.eta_days}</td><td>{r.co2}</td><td>{r.score}</td></tr>))}</tbody></table>
      </div> ); }
    if(c.type === 'map'){ const d=c.data||{};
      return (<div key={i} style={{border:'1px solid #eee', padding:12, borderRadius:12}}>
        <b>{c.title}</b><div>Lat/Lon: {d.lat?.toFixed?.(2)}, {d.lon?.toFixed?.(2)}</div><div>ETA UTC: {d.eta}</div>
        <div style={{height:120, background:'radial-gradient(circle at 30% 30%, #eef, #fff)'}} />
      </div> ); }
    if(c.type === 'leads'){ const rows=c.data||[];
      return (<div key={i} style={{border:'1px solid #eee', padding:12, borderRadius:12}}>
        <b>{c.title}</b>{rows.map((r:any,idx:number)=>(<div key={idx}>{r.name} — {r.lane} — score {r.score} — Next: {r.next}</div>))}
      </div> ); }
    return (<div key={i} style={{border:'1px solid #eee', padding:12, borderRadius:12}}><b>{c.title}</b><pre style={{whiteSpace:'pre-wrap'}}>{JSON.stringify(c.data,null,2)}</pre></div>);
  }
  return (<div style={{maxWidth:900, margin:'30px auto', fontFamily:'ui-sans-serif'}}>
    <h1 style={{fontSize:24, fontWeight:700}}>FreightSense — Online Demo</h1>
    <p>Try a command like <code>/quote 40FT Dubai Hamburg nextweek</code> and hit Send.</p>
    <div style={{border:'1px solid #ddd', padding:16, borderRadius:16, minHeight:400}}>
      {msgs.map((m,i)=>(<div key={i} style={{margin:'12px 0', display:'flex', justifyContent:m.role==='user'?'flex-end':'flex-start'}}>
        <div style={{background:m.role==='user'?'#2563eb':'#f9fafb', color:m.role==='user'?'#fff':'#111', padding:12, borderRadius:12, maxWidth:'70%'}}>
          <div style={{whiteSpace:'pre-wrap'}}>{m.text}</div>
          {m.cards && m.cards.length>0 && <div style={{marginTop:8, display:'grid', gap:8}}>{m.cards.map(CardView)}</div>}
        </div></div>))}
    </div>
    <div style={{display:'flex', gap:8, marginTop:12}}>
      <input value={text} onChange={e=>setText(e.target.value)} placeholder="Type /quote, /route, /track, /leads, /docs, /docs_vector ..." style={{flex:1, padding:12, borderRadius:12, border:'1px solid #ddd'}}/>
      <button onClick={send} style={{padding:'12px 16px', borderRadius:12, background:'#111', color:'#fff'}}>Send</button>
    </div>
  </div>);
}
