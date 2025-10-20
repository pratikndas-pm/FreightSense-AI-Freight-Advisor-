
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from typing import Dict, Any
from io import BytesIO
import time
from models.schemas import ChatRequest, ChatResponse, QuoteRequest, RouteRequest, TrackRequest, LeadsRequest, DocsRequest
from services.router import route_message
from services.quote import get_quote
from services.route import get_route
from services.track import get_track
from services.leads import score_leads
from services.docs import ask_docs
from services.docs_vector import ask_docs_vector
from services.quote_pdf import build_quote_pdf

app = FastAPI(title="FreightSense Online API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> Dict[str, Any]:
    t0=time.time(); out=route_message(req.message); out.setdefault("telemetry",{})["latency_ms"]=int((time.time()-t0)*1000); return out
@app.post("/chat/quote") def chat_quote(req: QuoteRequest): return get_quote(req)
@app.post("/chat/route") def chat_route(req: RouteRequest): return get_route(req)
@app.post("/chat/track") def chat_track(req: TrackRequest): return get_track(req)
@app.post("/chat/leads") def chat_leads(req: LeadsRequest): return score_leads(req)
@app.post("/chat/docs") def chat_docs(req: DocsRequest): return ask_docs(req)
@app.post("/chat/docs_vector") def chat_docs_vec(req: DocsRequest): return ask_docs_vector(req)
@app.post("/export/quote_pdf_from_data")
def export_quote_pdf_from_data(payload: dict):
    pdf=build_quote_pdf(payload); return StreamingResponse(BytesIO(pdf), media_type="application/pdf", headers={"Content-Disposition":"attachment; filename=quote.pdf"})
