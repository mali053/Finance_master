from datetime import datetime, timedelta
import re
from pydantic import BaseModel, validator

from app.validation import validation_function


class Expense(BaseModel):
    id: int
    userId: str
    amount: float
    date: datetime
    beneficiary: str
    documentation: str

    @validator('userId')
    def id_must_be_9_digits(cls, v):
        return validation_function.is_valid_id(v)

    @validator('date')
    def birth_date_minimum_age(cls, v):
        return validation_function.is_valid_date(v)

    @validator('amount')
    def check_amount(cls, v):
        return validation_function.check_amount(v)
