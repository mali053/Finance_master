from datetime import datetime, timedelta
from pydantic import BaseModel, validator


class Expense(BaseModel):
    id: int
    userId: str
    amount: float
    date: datetime
    beneficiary: str
    documentation: str

    @validator('date')
    def birth_date_minimum_age(cls, v):
        today = datetime.now().date()
        if v.date() > today:
            raise ValueError('The date cannot be in the future')
        return v
