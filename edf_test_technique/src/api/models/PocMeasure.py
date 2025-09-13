from pydantic import BaseModel

class PocMeasure(BaseModel):
    ppoc: int
    pmaxsite: int
