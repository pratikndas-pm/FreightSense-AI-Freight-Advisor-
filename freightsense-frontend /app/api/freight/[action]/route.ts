// app/api/freight/[action]/route.ts
import { NextRequest, NextResponse } from 'next/server';

const STREAMLIT_BACKEND_URL = process.env.STREAMLIT_BACKEND_URL;

export async function GET(req: NextRequest, { params }: { params: { action: string } }) {
  try {
    if (!STREAMLIT_BACKEND_URL) return NextResponse.json({ error: 'Missing STREAMLIT_BACKEND_URL' }, { status: 500 });
    const action = params.action;
    const url = new URL(STREAMLIT_BACKEND_URL);
    url.searchParams.set('api', '1');
    url.searchParams.set('action', action);
    const qp = req.nextUrl.searchParams;
    qp.forEach((v, k) => url.searchParams.set(k, v));
    const r = await fetch(url.toString(), { method: 'GET', headers: { 'cache-control': 'no-cache' } });
    const html = await r.text();
    const start = html.indexOf('<!--JSON_START-->');
    const end = html.indexOf('<!--JSON_END-->');
    if (start === -1 || end === -1) {
      return NextResponse.json({ error: 'Backend JSON markers not found' }, { status: 502 });
    }
    const jsonStr = html.substring(start + '<!--JSON_START-->'.length, end).trim();
    const data = JSON.parse(jsonStr);
    return NextResponse.json(data);
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || 'Proxy error' }, { status: 500 });
  }
}

export const dynamic = 'force-dynamic';
