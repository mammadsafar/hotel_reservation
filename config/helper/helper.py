from datetime import datetime
from jdatetime import datetime as jdatetime


def ptg(persian_date):
    """
    persian to gregorian
    """
    return jdatetime.strptime(persian_date, '%Y/%m/%d').togregorian().strftime('%Y-%m-%d')


def gtp(gregorian_date):
    """
    gregorian to persian
    """
    return jdatetime.strptime(gregorian_date, '%Y-%m-%d').tojalali().strftime('%Y/%m/%d')


def date_interval(date1, date2):
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    delta = date2 - date1
    return delta.days
