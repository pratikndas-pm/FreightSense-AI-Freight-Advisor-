import os, requests, streamlit as st
API_BASE = os.getenv("API_BASE", "https://<your-space>.hf.space")

st.set_page_config(page_title="FreightSense Chat Demo", layout="centered")
st.title("💬 FreightSense — Chat Demo")

prompt = st.text_input("Ask FreightSense", "Quote 40FT Dubai to Hamburg")
if st.button("Send"):
    r = requests.post(f"{API_BASE}/chat", json={"messages":[{"role":"user","content":prompt}]})
    data = r.json()
    st.markdown("**Answer:** " + data.get("answer",""))
    st.json(data.get("data", {}))
