
from ..models.schemas import QuoteRequest, Card
from .llm import summarize_with_llm
def get_quote(req: QuoteRequest):
    equip_factor = 1.0 if req.equipment.upper().startswith("20") else 1.4
    lane_hash = (hash(req.origin+req.destination)%300)+1200
    fuel = 1.0 + (hash(req.origin)%10)/100.0
    cong = 1.0 + (hash(req.destination)%8)/100.0
    predicted = round(lane_hash*equip_factor*fuel*cong,2)
    sur = {"BAF+CAF": round(predicted*0.11,2), "THC & Local": round(predicted*0.08,2)}
    total = round(predicted+sum(sur.values()),2)
    eta_days = 12 + (hash(req.destination)%6)
    margin_pct = 22; warning = None
    txt = f"QUOTE SUMMARY\nLane: {req.origin} → {req.destination} ({req.equipment})\nPredicted base: ${predicted}\nSurcharges: {sur}\nTotal (suggested): ${total}\nETA (days): ~{eta_days}\nMargin: {margin_pct}%"
    msg = summarize_with_llm(txt)
    return {"message": msg, "cards":[Card(type="quote", title="Quote Summary", data={
        "origin": req.origin, "destination": req.destination, "equipment": req.equipment,
        "predicted_base": predicted, "surcharges": sur, "total": total, "eta_days": eta_days,
        "margin_pct": margin_pct, "warning": warning}).model_dump()]}
