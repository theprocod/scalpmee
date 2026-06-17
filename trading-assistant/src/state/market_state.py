from pydantic import BaseModel
from typing import List, Optional

class MarketState(BaseModel):
    symbol: str = "XAUUSD"
    current_price: float
    spread: float
    trend_h4: str
    trend_h1: str
    trend_m15: str
    trend_m5: str
    atr: float
    volatility: str
    support_levels: List[float]
    resistance_levels: List[float]
    liquidity_zones: List[dict]
    bos: Optional[str] = None
    choch: Optional[str] = None
    session: str
    high_impact_news: bool = False
    minutes_to_news: Optional[int] = None
