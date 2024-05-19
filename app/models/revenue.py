from pydantic import BaseModel


class Revenues(BaseModel):
    revenueId: int
    userid: int
    amount: float
    whom: str
