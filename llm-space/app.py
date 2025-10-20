
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
MODEL="Qwen/Qwen2.5-0.5B-Instruct"; DEV=0 if torch.cuda.is_available() else -1
app=FastAPI(title="FreightSense LLM (Free)")
tok=AutoTokenizer.from_pretrained(MODEL)
model=AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.float32)
pipe=pipeline("text-generation", model=model, tokenizer=tok, device=DEV)
SYS=("You are a concise logistics assistant. Summarize the provided structured data into a friendly, factual answer. "
     "Use bullet points when helpful. Do not invent data. Keep answers under 180 words.")
class Req(BaseModel): prompt:str; temperature:float=0.2; max_new_tokens:int=220
@app.get("/") def root(): return {"ok":True,"model":MODEL}
@app.post("/generate")
def gen(r:Req):
    p=f"{SYS}\n\n{r.prompt}"
    out=pipe(p, do_sample=True, temperature=r.temperature, max_new_tokens=r.max_new_tokens, pad_token_id=tok.eos_token_id)
    txt=out[0]["generated_text"]; return {"response": txt[len(p):].strip() or "OK"}
