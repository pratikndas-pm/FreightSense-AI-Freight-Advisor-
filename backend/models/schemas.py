
from pydantic import BaseModel, Field
from typing import Optional, List, Literal, Dict, Any

class ChatRequest(BaseModel): message: str
class QuoteRequest(BaseModel):
    origin: str; destination: str; equipment: str = Field(...); date: Optional[str]=None
class RouteRequest(BaseModel):
    origin: str; destination: str; priority: Literal["fastest","cheapest","green"]="cheapest"
class TrackRequest(BaseModel): ref: str
class LeadsRequest(BaseModel): timeframe: Literal["today","week","month"]="today"
class DocsRequest(BaseModel): query: str
class Card(BaseModel): type: Literal["kpi","table","map","quote","leads","text"]; title: Optional[str]=None; data: Any=None
class ChatResponse(BaseModel):
    message: str; cards: List[Card]=[]; sources: Optional[List[Dict[str,Any]]]=None
    confidence: Optional[float]=0.8; actions: Optional[List[Dict[str,str]]]=None; telemetry: Optional[Dict[str,Any]]=None
