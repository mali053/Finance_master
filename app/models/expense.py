from pydantic import BaseModel


class Expenses(BaseModel):
    expenseId: int
    userid: int
    amount: float
    recipient: str
