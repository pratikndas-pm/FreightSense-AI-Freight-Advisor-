
import os, requests
LLM_URL = os.getenv("LLM_URL")
SYS = ("You are a concise logistics assistant. Summarize the provided structured data into a friendly, factual answer. "
       "Use bullet points when helpful. Do not invent data.")
def summarize_fallback(text:str)->str:
    lines=[l.strip() for l in text.splitlines() if l.strip()]; return (lines[0] if lines else text)[:500]
def summarize_with_llm(text:str)->str:
    if not LLM_URL: return summarize_fallback(text)
    try:
        r = requests.post(LLM_URL, json={"prompt": f"{SYS}\n\n{text}", "temperature":0.2, "max_new_tokens": 220}, timeout=45)
        return (r.json() or {}).get("response") or summarize_fallback(text)
    except Exception: return summarize_fallback(text)
