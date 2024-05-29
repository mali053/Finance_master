import re
from datetime import datetime, timezone, timedelta


def is_valid_id(v: str):
    """
    Validate if the string is a valid 9-digit ID.
    Args:
        v (str): The string to validate.
    Returns:
        str: The validated ID.
    Raises:
        ValueError: If the string is not a valid 9-digit ID.
    """
    if not re.fullmatch(r'^\d{9}$', v):
        raise ValueError('id must be exactly 9 digits')
    return v


def check_user_name(v: str):
    """
    Validate if the username string is not empty.
    Args:
        v (str): The username string to validate.
    Returns:
        str: The validated username.
    Raises:
        ValueError: If the username string is empty.
    """
    if not v.strip():
        raise ValueError('user_name must not be empty')
    return v


def is_valid_phone(phone_number: str):
    """
    Validate if the string is a valid Israeli phone number (landline or mobile).
    Args:
        phone_number (str): The Israeli phone number to validate.
    Returns:
        str: The validated phone number.
    Raises:
        ValueError: If the phone number is not in the correct format.
    """
    if not re.match(r"^05\d-\d{7}$", phone_number) and not re.match(r"^0\d-\d{7}$", phone_number):
        raise ValueError('Phone number must be in the format 05X-YYYYYYY.')
    return phone_number


def is_valid_date(date: datetime):
    """
    Validate if the date is a valid birthdate (at least 15 years old).
    Args:
        date (datetime): The birthdate to validate.
    Returns:
        datetime: The validated birthdate.
    Raises:
        ValueError: If the birthdate is not at least 15 years old.
    """
    today = datetime.now().date()
    min_birth_date = today - timedelta(days=0 * 365)  # Roughly 15 years
    if date.date() > min_birth_date:
        raise ValueError('User must be at least 15 years old')
    return date


def is_valid_password(v: str):
    """
    Validate if the string is a valid password.
    Args:
        v (str): The password string to validate.
    Returns:
        str: The validated password.
    Raises:
        ValueError: If the password string does not meet the criteria.
    """
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


def check_amount(amount: float):
    """
    Validate if the amount is positive.
    Args:
        amount (float): The amount to validate.
    Returns:
        float: The validated amount.
    Raises:
        ValueError: If the amount is negative.
    """
    if amount < 0:
        raise ValueError('The amount must be positive')
    return amount