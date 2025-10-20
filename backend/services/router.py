
from typing import Dict, Any
from ..models.schemas import QuoteRequest, RouteRequest, TrackRequest, LeadsRequest, DocsRequest
from .quote import get_quote
from .route import get_route
from .track import get_track
from .leads import score_leads
from .docs import ask_docs
from .docs_vector import ask_docs_vector

def route_message(msg: str) -> Dict[str, Any]:
    m=msg.lower().strip()
    if m.startswith("/quote"):
        p=m.split(); return get_quote(QuoteRequest(origin=p[2] if len(p)>2 else "Dubai", destination=p[3] if len(p)>3 else "Hamburg", equipment=p[1] if len(p)>1 else "40FT", date="next week"))
    if m.startswith("/route"):
        p=m.split(); return get_route(RouteRequest(origin=p[1] if len(p)>1 else "Shanghai", destination=p[2] if len(p)>2 else "Rotterdam", priority=p[3] if len(p)>3 else "cheapest"))
    if m.startswith("/track"):
        p=m.split(); return get_track(TrackRequest(ref=p[1] if len(p)>1 else "ABCD123456"))
    if m.startswith("/leads"): return score_leads(LeadsRequest())
    if m.startswith("/docs_vector"): return ask_docs_vector(DocsRequest(query=m.replace("/docs_vector","",1).strip() or "BAF surcharge"))
    if m.startswith("/docs"): return ask_docs(DocsRequest(query=m.replace("/docs","",1).strip() or "BAF surcharge"))
    if "track" in m or "container" in m: return get_track(TrackRequest(ref="ABCD123456"))
    if "route" in m or "fastest" in m or "cheapest" in m: return get_route(RouteRequest(origin="Shanghai", destination="Rotterdam", priority="cheapest"))
    if "quote" in m or "price" in m or "rate" in m: return get_quote(QuoteRequest(origin="Dubai", destination="Hamburg", equipment="40FT", date="next week"))
    if "lead" in m: return score_leads(LeadsRequest())
    return {"message":"Commands: /quote, /route, /track, /leads, /docs, /docs_vector"}
