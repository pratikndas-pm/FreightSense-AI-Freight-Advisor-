# freightsense-api/chat_endpoint.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional, Literal

router = APIRouter(prefix="", tags=["chat"])

class ChatMessage(BaseModel):
    role: Literal["user","assistant","tool"]
    content: str

class ChatToolCall(BaseModel):
    tool: Literal["quote","route","track","leads"]
    args: dict

class ChatRequest(BaseModel):
    messages: List[ChatMessage]

class ChatResponse(BaseModel):
    answer: str
    tool_called: Optional[ChatToolCall] = None
    data: Optional[dict] = None

def _simple_intent_parse(text: str) -> ChatToolCall:
    t = text.lower()
    if any(k in t for k in ["quote","price","rate"]):
        origin = "Dubai" if "dubai" in t else "Shanghai" if "shanghai" in t else "Dubai"
        dest   = "Hamburg" if "hamburg" in t else "Rotterdam" if "rotterdam" in t else "Hamburg"
        return ChatToolCall(tool="quote", args={"origin": origin, "destination": dest, "equipment": "40FT"})
    if any(k in t for k in ["route","path","option"]):
        return ChatToolCall(tool="route", args={"origin": "Dubai", "destination": "Hamburg", "priority": "time"})
    if any(k in t for k in ["track","container","vessel","eta"]):
        return ChatToolCall(tool="track", args={"container_id": "ABCD123456"})
    if any(k in t for k in ["lead","prospect","score"]):
        return ChatToolCall(tool="leads", args={})
    return ChatToolCall(tool="quote", args={"origin": "Dubai", "destination": "Hamburg", "equipment": "40FT"})

def _mock_generate_quote(args: dict) -> dict:
    lane = f"{args.get('origin')}->{args.get('destination')}"
    base = 2430 if "Dubai" in lane and "Hamburg" in lane else 1800
    sur = round(base * 0.18, 2)
    total = round(base + sur, 2)
    return {"base_rate_usd": base, "surcharges_usd": sur, "total_usd": total, "margin_pct": 22.0,
            "confidence": "high" if base == 2430 else "mid", "eta_days": 15 if base == 2430 else 21}

def _mock_plan_route(args: dict) -> dict:
    o, d = args.get("origin","Dubai"), args.get("destination","Hamburg")
    opts = [
        {"mode":"SEA","carrier":"Maersk","transit_days":15,"est_cost_usd":2430,"co2_kg":980,"waypoints":[o,"Jeddah","Rotterdam",d]},
        {"mode":"SEA+RAIL","carrier":"DB Schenker","transit_days":13,"est_cost_usd":2680,"co2_kg":820,"waypoints":[o,"Piraeus","Munich",d]},
        {"mode":"SEA","carrier":"Hapag-Lloyd","transit_days":17,"est_cost_usd":2210,"co2_kg":890,"waypoints":[o,"Valencia",d]},
    ]
    pr = args.get("priority","time")
    key = "transit_days" if pr=="time" else ("est_cost_usd" if pr=="cost" else "co2_kg")
    opts = sorted(opts, key=lambda x: x[key])
    return {"options": opts}

def _mock_track(args: dict) -> dict:
    ident = args.get("container_id") or args.get("vessel_name") or "Unknown"
    return {"location": "Near Jeddah", "lat": 21.4858, "lon": 39.1925, "speed_knots": 16.2,
            "eta_iso": "2025-10-31T16:00:00Z", "eta_confidence_hours": 6,
            "risk": "Medium", "reason": f"Port congestion signal for {ident}"}

def _mock_leads(_: dict) -> dict:
    return {"leads": [{"account":"Alpha Logistics","score":92,"confidence_pct":88,"action":"Call now"},
                      {"account":"BlueLine Freight","score":86,"confidence_pct":81,"action":"Send quote"},
                      {"account":"Nordic Trade","score":79,"confidence_pct":74,"action":"Book demo"}]}

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    user_msg = next((m.content for m in reversed(req.messages) if m.role == "user"), "")
    call = _simple_intent_parse(user_msg)
    if call.tool == "quote":
        q = _mock_generate_quote(call.args)
        return ChatResponse(answer=f"Predicted {q['total_usd']} USD (base {q['base_rate_usd']} + surcharges {q['surcharges_usd']}), margin {q['margin_pct']}%, ETA ~{q['eta_days']} days.", tool_called=call, data=q)
    if call.tool == "route":
        r = _mock_plan_route(call.args); best = r["options"][0]
        return ChatResponse(answer=f"Best route: {best['carrier']} via {', '.join(best['waypoints'])} in {best['transit_days']} days, ~${best['est_cost_usd']}, CO₂ {best['co2_kg']} kg.", tool_called=call, data=r)
    if call.tool == "track":
        t = _mock_track(call.args)
        return ChatResponse(answer=f"{t['location']} at {t['speed_knots']} kn. ETA {t['eta_iso']} ± {t['eta_confidence_hours']}h. Risk: {t['risk']} ({t['reason']}).", tool_called=call, data=t)
    if call.tool == "leads":
        l = _mock_leads(call.args); top = l["leads"][0]
        return ChatResponse(answer=f"Top lead: {top['account']} (score {top['score']}, {top['confidence_pct']}% conf). Suggestion: {top['action']}.", tool_called=call, data=l)
