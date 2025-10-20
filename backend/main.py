from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from typing import Dict, Any
from io import BytesIO
import time

# ---- Pydantic schemas (make sure these exist in backend/models/schemas.py)
from models.schemas import (
    ChatRequest,
    ChatResponse,
    QuoteRequest,
    RouteRequest,
    TrackRequest,
    LeadsRequest,
    DocsRequest,
)

# ---- Service layer (these modules should exist in backend/services/)
from services.router import route_message
from services.quote import get_quote
from services.route import get_route
from services.track import get_track
from services.leads import score_leads
from services.docs import ask_docs
from services.docs_vector import ask_docs_vector
from services.quote_pdf import build_quote_pdf

# -----------------------------------------------------------------------------

app = FastAPI(title="FreightSense Online API")

# CORS: permissive for demo; tighten to your domain for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------
# Health check
# -----------------------------------------------------------------------------
@app.get("/")
def root() -> Dict[str, Any]:
    return {"ok": True, "service": "FreightSense API", "version": "1.0.0"}

# -----------------------------------------------------------------------------
# Chat router (parses /quote, /route, /track, /leads, /docs, /docs_vector)
# -----------------------------------------------------------------------------
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> Dict[str, Any]:
    t0 = time.time()
    out = route_message(req.message)
    out.setdefault("telemetry", {})["latency_ms"] = int((time.time() - t0) * 1000)
    return out

# -----------------------------------------------------------------------------
# Direct tool endpoints (useful for testing each module independently)
# -----------------------------------------------------------------------------
@app.post("/chat/quote")
def chat_quote(req: QuoteRequest) -> Dict[str, Any]:
    return get_quote(req)

@app.post("/chat/route")
def chat_route(req: RouteRequest) -> Dict[str, Any]:
    return get_route(req)

@app.post("/chat/track")
def chat_track(req: TrackRequest) -> Dict[str, Any]:
    return get_track(req)

@app.post("/chat/leads")
def chat_leads(req: LeadsRequest) -> Dict[str, Any]:
    return score_leads(req)

@app.post("/chat/docs")
def chat_docs(req: DocsRequest) -> Dict[str, Any]:
    return ask_docs(req)

@app.post("/chat/docs_vector")
def chat_docs_vec(req: DocsRequest) -> Dict[str, Any]:
    return ask_docs_vector(req)

# -----------------------------------------------------------------------------
# Exports
# -----------------------------------------------------------------------------
@app.post("/export/quote_pdf_from_data")
def export_quote_pdf_from_data(payload: Dict[str, Any]):
    """
    Expects the same dict structure returned in the 'quote' card's 'data' field:
    {
      "origin": "...", "destination": "...", "equipment": "...",
      "predicted_base": 1234.56,
      "surcharges": {"BAF+CAF": 111.11, "THC & Local": 99.99},
      "total": 1445.66,
      "eta_days": 14,
      "margin_pct": 22,
      "warning": "optional string"
    }
    """
    pdf_bytes = build_quote_pdf(payload)
    return StreamingResponse(
        BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=quote.pdf"},
    )
