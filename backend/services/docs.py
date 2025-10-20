
import os
from ..models.schemas import DocsRequest, Card
from .llm import summarize_with_llm
DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "docs")
def load_docs():
    out=[]; 
    for fn in os.listdir(DOCS_DIR):
        p=os.path.join(DOCS_DIR,fn)
        if os.path.isfile(p): out.append((fn, open(p,"r",encoding="utf-8",errors="ignore").read()))
    return out
DOCS = load_docs()
def ask_docs(req: DocsRequest):
    q=req.query.lower(); hits=[]
    for fn,content in DOCS:
        score=content.lower().count(q)
        if score>0: hits.append({"file":fn,"score":score,"snippet":content[:200].replace("\n"," ")})
    hits=sorted(hits,key=lambda x:x["score"],reverse=True)[:3]
    txt="DOCS ANSWER:\n"+("\n".join([f"- {h['file']}: {h['snippet']}..." for h in hits]) if hits else "No match")
    return {"message": summarize_with_llm(txt), "cards":[Card(type="text", title="Sources", data=hits).model_dump()], "sources":[{"title":h["file"]} for h in hits]}
