
from ..models.schemas import LeadsRequest, Card
from .llm import summarize_with_llm
def score_leads(req: LeadsRequest):
    leads=[{"name":"Alpha Logistics","score":92,"lane":"CN→EU","value":"High","next":"Call"},
           {"name":"BlueLine Freight","score":86,"lane":"GCC→EU","value":"Medium","next":"Email"},
           {"name":"Nordic Trade Co.","score":79,"lane":"US→EU","value":"Medium","next":"Call"}]
    txt="Top Leads:\n" + "\n".join([f"- {l['name']} {l['lane']} score {l['score']} next {l['next']}" for l in leads])
    return {"message": summarize_with_llm(txt), "cards":[Card(type="leads", title="Lead Priority", data=leads).model_dump()]}
