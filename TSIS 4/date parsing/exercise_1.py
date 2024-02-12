# Write a Python program to subtract five days from current date.
from datetime import datetime, date, timedelta


PATTERN = '%d.%m.%Y'


def subtract_days(dt=date.today(), days=5):
    return dt - timedelta(days)

print(subtract_days().strftime(PATTERN))
