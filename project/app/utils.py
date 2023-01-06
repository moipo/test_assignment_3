from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
import datetime



def is_phone_number(phone_number):
    match = re.search(r"\+7\s?[0-9]{3}\s?[0-9]{3}\s?[0-9]{2}\s?[0-9]{2}", phone_number)
    if match and len(phone_number)==16: return True
    else: return False

def is_email(email):
    try:
        if validate_email() is None:
            return True
    except:
        return False


def is_date(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except:
            try:
                datetime.datetime.strptime(date_text, '%d.%m.%Y')
                return True
            except:
                return False

def get_type(data):
    if is_phone_number(data): return "phone_number"
    elif is_email(data): return "email"
    elif is_date(data): return "date"
    elif isinstance(data,str): return "text"
    else: return "incorrect_input"
