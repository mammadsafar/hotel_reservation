from datetime import datetime, timedelta
from jdatetime import datetime as jdatetime


def ptg(persian_date):
    """
    persian to gregorian
    """
    return jdatetime.strptime(persian_date, '%Y-%m-%d').togregorian().strftime('%Y-%m-%d')


def gtp(gregorian_date):
    """
    gregorian to persian
    """
    return jdatetime.strptime(gregorian_date, '%Y-%m-%d').tojalali().strftime('%Y-%m-%d')


def date_interval(date1, date2):
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    delta = date2 - date1
    return delta.days


def check_dates(date1, date2):
    today = datetime.now().date()
    date1 = datetime.strptime(date1, '%Y-%m-%d').date()
    date2 = datetime.strptime(date2, '%Y-%m-%d').date()
    if date1 < today and (date2 - date1) >= timedelta(days=1):
        return True
    else:
        return False


def persian_numbers_converter(string):
    numbers = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
    for e, p in numbers.items():
        string = string.replace(e, p)
    return string


def en_numbers_converter(string):
    numbers = {
        "۰": "0",
        "۱": "1",
        "۲": "2",
        "۳": "3",
        "۴": "4",
        "۵": "5",
        "۶": "6",
        "۷": "7",
        "۸": "8",
        "۹": "9",
    }
    for e, p in numbers.items():
        string = string.replace(e, p)
    return string
