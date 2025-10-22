from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import time

app = FastAPI(title="FreightSense API", version="0.1.0")

# CORS — open for demo; restrict to your domains in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuoteRequest(BaseModel):
    origin: str
    destination: str
    equipment: str = "40FT"
    ship_date: Optional[str] = None

class QuoteResponse(BaseModel):
    base_rate_usd: float
    surcharges_usd: float
    total_usd: float
    margin_pct: float
    confidence: str
    eta_days: int

class RouteRequest(BaseModel):
    origin: str
    destination: str
    priority: str = "time"  # time|cost|co2

class RouteOption(BaseModel):
    mode: str
    carrier: str
    transit_days: int
    est_cost_usd: int
    co2_kg: int
    waypoints: List[str]

class RouteResponse(BaseModel):
    options: List[RouteOption]

class TrackRequest(BaseModel):
    container_id: Optional[str] = None
    vessel_name: Optional[str] = None

class TrackResponse(BaseModel):
    location: str
    lat: float
    lon: float
    speed_knots: float
    eta_iso: str
    eta_confidence_hours: int
    risk: str
    reason: str

class LeadScoresRequest(BaseModel):
    region: Optional[str] = None

class LeadScore(BaseModel):
    account: str
    score: int
    confidence_pct: int
    action: str

class LeadScoresResponse(BaseModel):
    leads: List[LeadScore]

@app.get("/")
def root():
    return {"service": "FreightSense API", "status": "ok", "time": int(time.time())}

@app.post("/generate_quote", response_model=QuoteResponse)
def generate_quote(req: QuoteRequest):
    lane = f"{req.origin}->{req.destination}"
    # simple mock logic per lane
    base = 2430 if "Dubai" in lane and "Hamburg" in lane else 1800
    sur = round(base * 0.18, 2)
    total = round(base + sur, 2)
    margin = 22.0
    conf = "mid" if base == 1800 else "high"
    eta = 15 if base == 2430 else 21
    return QuoteResponse(
        base_rate_usd=base,
        surcharges_usd=sur,
        total_usd=total,
        margin_pct=margin,
        confidence=conf,
        eta_days=eta,
    )

@app.post("/plan_route", response_model=RouteResponse)
def plan_route(req: RouteRequest):
    # three options: fastest, cheapest, greenest
    opts = [
        RouteOption(mode="SEA", carrier="Maersk", transit_days=15, est_cost_usd=2430, co2_kg=980,
                    waypoints=[req.origin, "Jeddah", "Rotterdam", req.destination]),
        RouteOption(mode="SEA+RAIL", carrier="DB Schenker", transit_days=13, est_cost_usd=2680, co2_kg=820,
                    waypoints=[req.origin, "Piraeus", "Munich", req.destination]),
        RouteOption(mode="SEA", carrier="Hapag-Lloyd", transit_days=17, est_cost_usd=2210, co2_kg=890,
                    waypoints=[req.origin, "Valencia", req.destination]),
    ]
    if req.priority == "cost":
        opts = sorted(opts, key=lambda o: o.est_cost_usd)
    elif req.priority == "co2":
        opts = sorted(opts, key=lambda o: o.co2_kg)
    else:
        opts = sorted(opts, key=lambda o: o.transit_days)
    return RouteResponse(options=opts)

@app.post("/track", response_model=TrackResponse)
def track(req: TrackRequest):
    ident = req.container_id or req.vessel_name or "Unknown"
    # mock DXB→HAM progress
    return TrackResponse(
        location="Near Jeddah",
        lat=21.4858,
        lon=39.1925,
        speed_knots=16.2,
        eta_iso="2025-10-31T16:00:00Z",
        eta_confidence_hours=6,
        risk="Medium",
        reason=f"Port congestion signal on lane for {ident}",
    )

@app.post("/lead_scores", response_model=LeadScoresResponse)
def lead_scores(req: LeadScoresRequest):
    leads = [
        LeadScore(account="Alpha Logistics", score=92, confidence_pct=88, action="Call now"),
        LeadScore(account="BlueLine Freight", score=86, confidence_pct=81, action="Send quote"),
        LeadScore(account="Nordic Trade", score=79, confidence_pct=74, action="Book demo"),
    ]
    return LeadScoresResponse(leads=leads)
