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
        """
        Validate if the ID is a valid 9-digit ID.
        Args:
            v (str): The ID to validate.
        Returns:
            str: The validated ID.
        Raises:
            ValueError: If the ID is not a valid 9-digit ID.
        """
        return validation_function.is_valid_id(v)

    @validator('user_name')
    def user_name_must_not_be_empty(cls, v):
        """
        Validate if the username is not empty.
        Args:
            v (str): The username to validate.
        Returns:
            str: The validated username.
        Raises:
            ValueError: If the username is empty.
        """
        return validation_function.check_user_name(v)

    @validator('password')
    def password_complexity(cls, v):
        """
        Validate if the password meets complexity requirements.
        Args:
            v (str): The password to validate.
        Returns:
            str: The validated password.
        Raises:
            ValueError: If the password does not meet complexity requirements.
        """
        return validation_function.is_valid_password(v)

    @validator('phone')
    def phone_number_format(cls, v):
        """
        Validate if the phone number is in the correct format.
        Args:
            v (str): The phone number to validate.
        Returns:
            str: The validated phone number.
        Raises:
            ValueError: If the phone number is not in the correct format.
        """
        return validation_function.is_valid_phone(v)

    @validator('birth_date')
    def birth_date_minimum_age(cls, v):
        """
        Validate if the birthdate is valid (at least 15 years old).
        Args:
            v (datetime): The birthdate to validate.
        Returns:
            datetime: The validated birthdate.
        Raises:
            ValueError: If the birthdate is not at least 15 years old.
        """
        return validation_function.is_valid_date(v)
