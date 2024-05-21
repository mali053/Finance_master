import re
from datetime import datetime
from pydantic import BaseModel, validator

from app.validation import validation_function


class Revenue(BaseModel):
    id: int
    userId: str
    amount: float
    date: datetime
    benefactor: str
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
