from pydantic import BaseModel, EmailStr, validator
from datetime import datetime, timedelta
import re


class User(BaseModel):
    id: str
    user_name: str
    password: str
    email: str
    phone: str
    birth_date: datetime
    balance: float

    @validator('id')
    def id_must_be_9_digits(cls, v):
        if not re.fullmatch(r'^\d{9}$', v):
            raise ValueError('id must be exactly 9 digits')
        return v

    @validator('user_name')
    def user_name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('user_name must not be empty')
        return v

    @validator('password')
    def password_complexity(cls, v):
        if len(v) < 8:
            raise ValueError('password must be at least 8 characters long')
        if not re.search(r'[A-Z]', v):
            raise ValueError('password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('password must contain at least one lowercase letter')
        if not re.search(r'[0-9]', v):
            raise ValueError('password must contain at least one number')
        if not re.search(r'[!@#\$%\^&\*]', v):
            raise ValueError('password must contain at least one special character')
        return v

    @validator('phone')
    def phone_number_format(cls, v):
        phone_pattern = re.compile(r'^(\(\d{3}\)\s|\d{3}-)\d{7}$')
        if not phone_pattern.match(v):
            raise ValueError('phone must be in the format (123) 456-7890 or 123-456-7890')
        return v

    @validator('birth_date')
    def birth_date_minimum_age(cls, v):
        today = datetime.now().date()
        min_birth_date = today - timedelta(days=15 * 365)  # Roughly 15 years
        if v.date() > min_birth_date:
            raise ValueError('User must be at least 15 years old')
        return v
