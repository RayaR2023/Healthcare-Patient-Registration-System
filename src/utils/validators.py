import re
from datetime import datetime


def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None


def is_valid_phone(phone):

    digits = "".join(c for c in phone if c.isdigit())

    return len(digits) == 10


def is_not_empty(value):
    return value.strip() != ""