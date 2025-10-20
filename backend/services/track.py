
import math, datetime
from ..models.schemas import TrackRequest, Card
from .llm import summarize_with_llm
def get_track(req: TrackRequest):
    now = datetime.datetime.utcnow(); phase=(hash(req.ref)%360)+int(now.timestamp()/600)%360
    lat=20+10*math.sin(math.radians(phase)); lon=40+10*math.cos(math.radians(phase))
    eta_hours=72+(hash(req.ref)%24); eta=(now+datetime.timedelta(hours=eta_hours)).isoformat()
    txt=f"TRACKING\nRef: {req.ref}\nPos: {lat:.2f},{lon:.2f}\nETA: {eta} (±6h)"
    return {"message": summarize_with_llm(txt), "cards":[
        Card(type="map", title="Live Tracker", data={"lat":lat,"lon":lon,"eta":eta}).model_dump(),
        Card(type="kpi", title="ETA (hrs)", data={"value": eta_hours}).model_dump()
    ]}
