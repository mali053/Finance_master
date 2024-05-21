from pydantic import BaseModel, EmailStr, validator
from datetime import datetime, timedelta
import re

from app.validation import validation_function


class User(BaseModel):
    id: str
    user_name: str
    password: str
    email: EmailStr
    phone: str
    birth_date: datetime
    balance: float

    @validator('id')
    def id_must_be_9_digits(cls, v):
        return validation_function.is_valid_id(v)

    @validator('user_name')
    def user_name_must_not_be_empty(cls, v):
        return validation_function.check_user_name(v)

    @validator('password')
    def password_complexity(cls, v):
        return validation_function.is_valid_password(v)

    @validator('phone')
    def phone_number_format(cls, v):
        return validation_function.is_valid_phone(v)

    @validator('birth_date')
    def birth_date_minimum_age(cls, v):
        return validation_function.is_valid_date(v)
