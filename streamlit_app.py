
# streamlit_app.py
# FreightSense — AI Freight Advisor (Chat UI Demo)
import re
from datetime import datetime
from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="FreightSense — AI Freight Chat", page_icon=":ship:", layout="wide")

st.markdown("""<style>
.chatbox {max-width: 1100px; margin: 0 auto;}
.assistant {background:#f8fafc;border:1px solid #e2e8f0;border-radius:16px;padding:14px;margin:8px 0;}
.user {text-align:right;margin:8px 0;}
.user .bubble{display:inline-block;background:#0ea5e9;color:white;border-radius:16px;padding:12px 14px;}
.toolbox {display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
.toolchip{border:1px solid #e2e8f0;border-radius:999px;padding:6px 10px;background:#fff;font-size:12px;cursor:pointer}
.kpi{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px;margin-top:8px}
.kpicard{border:1px solid #e5e7eb;border-radius:14px;padding:10px;background:#fff}
.kpilabel{font-size:11px;color:#64748b;text-transform:uppercase;letter-spacing:.04em}
.kpiv{font-weight:700;font-size:18px;margin-top:2px}
.footer{color:#94a3b8;font-size:12px;text-align:center;padding-top:10px}
</style>""", unsafe_allow_html=True)

DATA_DIR = Path(__file__).parent / "data"
@st.cache_data
def load_data():
    lanes = pd.read_csv(DATA_DIR / "lanes.csv")
    schedules = pd.read_csv(DATA_DIR / "schedules.csv")
    containers = pd.read_csv(DATA_DIR / "containers.csv")
    leads = pd.read_csv(DATA_DIR / "leads.csv")
    return lanes, schedules, containers, leads

LANES, SCHEDULES, CONTAINERS, LEADS = load_data()

def money(x): return f"${x:,.0f}" if pd.notna(x) else "-"
def co2(x): return f"{x:,.0f} kg" if pd.notna(x) else "-"

def predictive_quote(o, d, equipment="40FT"):
    m = LANES[(LANES.origin.str.lower()==o.lower()) & (LANES.destination.str.lower()==d.lower())]
    if m.empty: return None
    row = m.iloc[0]
    base = float(row.base_usd_40ft)
    sur = round(base * 0.18, 2)
    return {
        "origin": o, "destination": d, "equipment": equipment,
        "base_rate": base, "surcharges": sur,
        "total": round(base+sur, 2),
        "eta_days": int(row.eta_days), "co2": int(row.co2_kg)
    }

def route_options(o, d):
    df = SCHEDULES[(SCHEDULES.origin.str.lower()==o.lower()) & (SCHEDULES.destination.str.lower()==d.lower())]
    return df if not df.empty else None

def track_container(cid):
    df = CONTAINERS[CONTAINERS.container_id==cid.upper()]
    if df.empty: return None
    r = df.iloc[0]
    risk = "High" if r.delay_hours>=6 else ("Medium" if r.delay_hours>=3 else "Low")
    eta = datetime.fromisoformat(r.eta_iso.replace("Z","")).strftime("%Y-%m-%d %H:%M UTC")
    return {**r, "risk":risk, "eta_human":eta}

def score_leads():
    df = LEADS.copy()
    df["score"] = (df.engagement_score*60 + df.ticket_kusd/1.5 + df.last_quote_win*20).clip(0,100)
    df["band"] = pd.cut(df.score,[-1,69,84,100],labels=["Cold","Warm","Hot"])
    df["action"] = df.band.map({"Hot":"Call now","Warm":"Send quote","Cold":"Nurture email"})
    return df.sort_values("score",ascending=False)

def detect_intent(msg:str):
    t=msg.lower()
    if "quote" in t or "rate" in t: return "quote"
    if "route" in t or "compare" in t or "transit" in t: return "route"
    if "track" in t or "container" in t or "eta" in t: return "track"
    if "lead" in t or "prospect" in t or "hot deals" in t: return "leads"
    return "unknown"

if "chat" not in st.session_state:
    st.session_state.chat = [
        {"role":"assistant","content":"Hi! I can help with freight quotes, route comparisons (CO2 too), live tracking ETA, and lead scoring. Try: 'Quote 40FT from Dubai to Hamburg', 'Compare routes from Dubai to Hamburg', 'Track ABCD123456', or 'Show top leads'."}
    ]

st.title("FreightSense — AI Freight Advisor (Chat Demo)")

chips = ["Quote 40FT from Dubai to Hamburg","Compare routes from Dubai to Hamburg","Track ABCD123456","Show top leads"]
st.write('<div class="toolbox">'+ "".join([f'<span class="toolchip">{c}</span>' for c in chips]) +'</div>', unsafe_allow_html=True)

with st.container():
    st.write('<div class="chatbox">', unsafe_allow_html=True)
    for m in st.session_state.chat:
        if m["role"]=="assistant":
            st.markdown(f'<div class="assistant">{m["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="user"><span class="bubble">{m["content"]}</span></div>', unsafe_allow_html=True)
    st.write('</div>', unsafe_allow_html=True)

msg = st.chat_input("Ask about quotes, routes, tracking, or leads…")
if msg:
    st.session_state.chat.append({"role":"user","content":msg})
    i=detect_intent(msg)
    if i=="quote":
        res=predictive_quote("Dubai","Hamburg")
        if res:
            kpi=f"""
<div class='kpi'>
  <div class='kpicard'><div class='kpilabel'>Base</div><div class='kpiv'>{money(res['base_rate'])}</div></div>
  <div class='kpicard'><div class='kpilabel'>Surcharges</div><div class='kpiv'>{money(res['surcharges'])}</div></div>
  <div class='kpicard'><div class='kpilabel'>Total</div><div class='kpiv'>{money(res['total'])}</div></div>
  <div class='kpicard'><div class='kpilabel'>ETA</div><div class='kpiv'>{res['eta_days']} days</div></div>
  <div class='kpicard'><div class='kpilabel'>CO2</div><div class='kpiv'>{co2(res['co2'])}</div></div>
</div>"""
            st.session_state.chat.append({"role":"assistant","content":f"**Predicted quote for Dubai -> Hamburg (40FT)** {kpi}"})
    elif i=="route":
        df=route_options("Dubai","Hamburg")
        if df is not None:
            st.session_state.chat.append({"role":"assistant","content":"**Top route options (time, cost, CO2)**"})
            st.dataframe(df,use_container_width=True)
        else:
            st.session_state.chat.append({"role":"assistant","content":"No route options found."})
    elif i=="track":
        r=track_container("ABCD123456")
        if r is not None:
            st.session_state.chat.append({"role":"assistant","content":f"**{r['container_id']}** — {r['location']} at {r['speed_knots']} kn · ETA **{r['eta_human']}** · Risk **{r['risk']}**"})
            st.map(pd.DataFrame([{"lat":r.lat,"lon":r.lon}]),zoom=3)
        else:
            st.session_state.chat.append({"role":"assistant","content":"Unknown container ID."})
    elif i=="leads":
        df=score_leads()
        st.session_state.chat.append({"role":"assistant","content":"**Ranked leads by win probability**"})
        st.dataframe(df[["account","region","industry","ticket_kusd","engagement_score","score","band","action"]],use_container_width=True)
    else:
        st.session_state.chat.append({"role":"assistant","content":"I can help with quotes, routes, tracking, and leads. Try one of the chips above!"})
    st.experimental_rerun()

st.markdown("<div class='footer'>© 2025 FreightSense — Demo data only</div>", unsafe_allow_html=True)
