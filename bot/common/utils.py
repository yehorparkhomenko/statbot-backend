import datetime

from django.utils.timezone import make_aware


def range_to_list_dates(from_date: datetime.datetime,
                        to_date: datetime.datetime) -> list:
    """
    Makes list of dates from interval
    :param from_date:
    :param to_date:
    :return: list of dates
    """
    from_date = make_aware(from_date)
    to_date = make_aware(to_date)
    numdays = abs((to_date - from_date).days) or 1
    dates = [to_date - datetime.timedelta(days=x) for x in range(numdays)]
    return dates
