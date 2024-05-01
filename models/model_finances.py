from datetime import datetime
from pydantic import BaseModel


class Finances(BaseModel):
    title: str
    description: str
    type: str
    value: float
    date: datetime
