import re
from datetime import datetime, timezone, timedelta


def is_valid_id(v: str):
    """
    Validate if the string is a valid alphanumeric string with special characters.
    Args:
        string (str): The string to validate.
    Returns:
        bool: True if the string is valid, False otherwise.
        :param v:
    """
    if not re.fullmatch(r'^\d{9}$', v):
        raise ValueError('id must be exactly 9 digits')
    return v


def check_user_name(v: str):
    if not v.strip():
        raise ValueError('user_name must not be empty')
    return v

def is_valid_phone(phone_number: str):
    """
    Validate if the string is a valid Israeli phone number (landline or mobile).
    Args:
        phone_number (str): The Israeli phone number to validate.
    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    if not re.match(r"^05\d-\d{7}$", phone_number) and not re.match(r"^0\d-\d{7}$", phone_number):
        raise ValueError('Phone number must be in the format 05X-YYYYYYY.')
    return phone_number


def is_valid_date(date: datetime):
    """
    Validate if the birthdate is valid.
    Args:
        birth_date (datetime): The birthdate to validate.
    Returns:
        bool: True if the birthdate is valid, False otherwise.
        :param date:
    """
    today = datetime.now().date()
    min_birth_date = today - timedelta(days=0 * 365)  # Roughly 15 years
    if date.date() > min_birth_date:
        raise ValueError('User must be at least 15 years old')
    return date


def is_valid_password(v: str):
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
    if amount < 0:
        raise ValueError('The amount must be positive')
    return amount