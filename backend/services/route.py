
from ..models.schemas import RouteRequest, Card
from .llm import summarize_with_llm
def get_route(req: RouteRequest):
    opts=[{"carrier":"Maersk","mode":"sea","eta_days":15,"cost":2400,"co2":1.0},
          {"carrier":"CMA CGM","mode":"sea+rail","eta_days":12,"cost":2750,"co2":0.85},
          {"carrier":"DHL","mode":"air+sea","eta_days":7,"cost":4800,"co2":1.6}]
    for o in opts:
        o["score"] = (100-o["eta_days"]) if req.priority=="fastest" else (int((1/o["co2"])*70) if req.priority=="green" else int((5000-o["cost"])/50))
    opts.sort(key=lambda x:x["score"], reverse=True)
    txt = f"Route options for {req.origin} → {req.destination} ({req.priority}):\n" + "\n".join([f"- {o['carrier']} {o['mode']} ${o['cost']} ETA {o['eta_days']}d CO2 {o['co2']} score {o['score']}" for o in opts])
    return {"message": summarize_with_llm(txt), "cards":[Card(type="table", title="Route Options", data=opts).model_dump()]}
