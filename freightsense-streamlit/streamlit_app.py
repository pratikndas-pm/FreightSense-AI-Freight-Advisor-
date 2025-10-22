import os, requests, pandas as pd, streamlit as st
API_BASE = os.getenv("API_BASE", "https://<your-space>.hf.space")

st.set_page_config(page_title="FreightSense Analyst", layout="wide")
st.title("🚢 FreightSense — Analyst Console")

quote_tab, route_tab, track_tab, leads_tab = st.tabs(["Quote", "Route", "Track", "Leads"]) 

with quote_tab:
    col1, col2, col3 = st.columns(3)
    origin = col1.text_input("Origin", "Dubai")
    dest = col2.text_input("Destination", "Hamburg")
    equip = col3.selectbox("Equipment", ["20FT","40FT","40HC"], index=1)
    if st.button("Generate Quote"):
        r = requests.post(f"{API_BASE}/generate_quote", json={"origin": origin, "destination": dest, "equipment": equip})
        data = r.json()
        c1,c2,c3,c4,c5 = st.columns(5)
        c1.metric("Base", f"${data['base_rate_usd']}")
        c2.metric("Surcharges", f"${data['surcharges_usd']}")
        c3.metric("Total", f"${data['total_usd']}")
        c4.metric("Margin", f"{data['margin_pct']}%")
        c5.metric("ETA", f"{data['eta_days']} days")

with route_tab:
    col1, col2 = st.columns(2)
    origin = col1.text_input("Origin", "Dubai", key="r1")
    dest = col2.text_input("Destination", "Hamburg", key="r2")
    priority = st.selectbox("Priority", ["time","cost","co2"], index=0)
    if st.button("Plan Route"):
        r = requests.post(f"{API_BASE}/plan_route", json={"origin": origin, "destination": dest, "priority": priority})
        opts = r.json()["options"]
        df = pd.DataFrame(opts)
        st.dataframe(df)

with track_tab:
    cid = st.text_input("Container ID", "ABCD123456")
    if st.button("Track"):
        r = requests.post(f"{API_BASE}/track", json={"container_id": cid})
        t = r.json()
        st.write(t)
        st.map(pd.DataFrame([{"lat": t["lat"], "lon": t["lon"]}]))

with leads_tab:
    if st.button("Get Lead Scores"):
        r = requests.post(f"{API_BASE}/lead_scores", json={})
        st.dataframe(pd.DataFrame(r.json()["leads"]))
