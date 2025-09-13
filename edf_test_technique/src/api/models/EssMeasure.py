from pydantic import BaseModel
from typing import Optional

class EssMeasure(BaseModel):
    eess: int
    ess_capacity: int
    amount_power: Optional[int]
