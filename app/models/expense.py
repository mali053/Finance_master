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
        """
        Validate if the user ID is a valid 9-digit ID.
        Args:
            v (str): The user ID to validate.
        Returns:
            str: The validated user ID.
        Raises:
            ValueError: If the user ID is not a valid 9-digit ID.
        """
        return validation_function.is_valid_id(v)

    @validator('date')
    def birth_date_minimum_age(cls, v):
        """
        Validate if the date is a valid birthdate (at least 15 years old).
        Args:
            v (datetime): The birthdate to validate.
        Returns:
            datetime: The validated birthdate.
        Raises:
            ValueError: If the birthdate is not at least 15 years old.
        """
        return validation_function.is_valid_date(v)

    @validator('amount')
    def check_amount(cls, v):
        """
        Validate if the amount is positive.
        Args:
            v (float): The amount to validate.
        Returns:
            float: The validated amount.
        Raises:
            ValueError: If the amount is negative.
        """
        return validation_function.check_amount(v)
