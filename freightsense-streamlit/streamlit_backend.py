import os, json, time
import streamlit as st

st.set_page_config(page_title="FreightSense Backend (Streamlit)", layout="wide")

def quote(origin, destination, equipment="40FT"):
    lane = f"{origin}->{destination}"
    base = 2430 if ("dubai" in origin.lower() and "hamburg" in destination.lower()) else 1800
    sur = round(base * 0.18, 2)
    total = round(base + sur, 2)
    return {"base_rate_usd": base,"surcharges_usd": sur,"total_usd": total,"margin_pct": 22.0,
            "confidence": "high" if base == 2430 else "mid","eta_days": 15 if base == 2430 else 21}

def plan_route(origin, destination, priority="time"):
    opts = [
        {"mode":"SEA","carrier":"Maersk","transit_days":15,"est_cost_usd":2430,"co2_kg":980,"waypoints":[origin,"Jeddah","Rotterdam",destination]},
        {"mode":"SEA+RAIL","carrier":"DB Schenker","transit_days":13,"est_cost_usd":2680,"co2_kg":820,"waypoints":[origin,"Piraeus","Munich",destination]},
        {"mode":"SEA","carrier":"Hapag-Lloyd","transit_days":17,"est_cost_usd":2210,"co2_kg":890,"waypoints":[origin,"Valencia",destination]},
    ]
    key = "transit_days" if priority=="time" else ("est_cost_usd" if priority=="cost" else "co2_kg")
    return {"options": sorted(opts, key=lambda x: x[key])}

def track(container_id="ABCD123456"):
    return {"location": "Near Jeddah","lat": 21.4858,"lon": 39.1925,"speed_knots": 16.2,
            "eta_iso": "2025-10-31T16:00:00Z","eta_confidence_hours": 6,
            "risk": "Medium","reason": f"Port congestion signal for {container_id}"}

def lead_scores():
    return {"leads": [{"account":"Alpha Logistics","score":92,"confidence_pct":88,"action":"Call now"},
                      {"account":"BlueLine Freight","score":86,"confidence_pct":81,"action":"Send quote"},
                      {"account":"Nordic Trade","score":79,"confidence_pct":74,"action":"Book demo"}]}

params = st.query_params
api_mode = params.get("api", ["0"])[0] == "1"
action = params.get("action", [""])[0]

if api_mode:
    origin = params.get("origin", ["Dubai"])[0]
    destination = params.get("destination", ["Hamburg"])[0]
    equipment = params.get("equipment", ["40FT"])[0]
    container_id = params.get("container_id", ["ABCD123456"])[0]
    priority = params.get("priority", ["time"])[0]

    if action == "quote":
        data = quote(origin, destination, equipment)
    elif action == "route":
        data = plan_route(origin, destination, priority)
    elif action == "track":
        data = track(container_id)
    elif action == "leads":
        data = lead_scores()
    else:
        data = {"error": "unknown action"}

    st.markdown("<!--JSON_START-->")
    st.write(json.dumps(data))
    st.markdown("<!--JSON_END-->")
    st.stop()

st.title("🚢 FreightSense — Streamlit Backend")
st.caption("Vercel proxies API calls here with ?api=1&action=...")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Quote")
    o = st.text_input("Origin", "Dubai", key="qo")
    d = st.text_input("Destination", "Hamburg", key="qd")
    if st.button("Get quote"):
        st.json(quote(o, d))

with col2:
    st.subheader("Route")
    o2 = st.text_input("Origin", "Dubai", key="ro")
    d2 = st.text_input("Destination", "Hamburg", key="rd")
    pr = st.selectbox("Priority", ["time","cost","co2"], index=0)
    if st.button("Plan route"):
        st.json(plan_route(o2, d2, pr))

st.subheader("Track")
cid = st.text_input("Container ID", "ABCD123456")
if st.button("Track now"):
    st.json(track(cid))

st.subheader("Leads")
if st.button("Get lead scores"):
    st.json(lead_scores())
