
import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from ..models.schemas import DocsRequest, Card
from .llm import summarize_with_llm
DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "docs")
client=chromadb.Client(Settings(anonymized_telemetry=False))
col=client.create_collection("freightsense_docs", metadata={"hnsw:space":"cosine"})
model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
# bootstrap
existing=set(col.get().get("ids",[]) or [])
for fn in os.listdir(DOCS_DIR):
    p=os.path.join(DOCS_DIR,fn)
    if os.path.isfile(p) and fn not in existing:
        doc=open(p,"r",encoding="utf-8",errors="ignore").read()
        emb=model.encode([doc], normalize_embeddings=True).tolist()[0]
        col.add(ids=[fn], documents=[doc], metadatas=[{"file":fn}], embeddings=[emb])
def ask_docs_vector(req: DocsRequest):
    qemb=model.encode([req.query], normalize_embeddings=True).tolist()[0]
    res=col.query(query_embeddings=[qemb], n_results=3, include=["documents","metadatas","distances"])
    hits=[]
    if res.get("ids"):
        for i in range(len(res["ids"][0])):
            hits.append({"file":res["metadatas"][0][i]["file"],"distance":res["distances"][0][i],"snippet":(res["documents"][0][i] or "")[:220].replace("\n"," ")})
    txt="DOCS (Vector RAG):\n"+("\n".join([f"- {h['file']} d={h['distance']:.3f}: {h['snippet']}..." for h in hits]) if hits else "No match")
    return {"message": summarize_with_llm(txt), "cards":[Card(type="text", title="Vector Sources", data=hits).model_dump()], "sources":[{"title":h["file"]} for h in hits]}
