# Write a Python program to calculate two date difference in seconds.
from datetime import date


def calc_dates_diff(date1, date2):
    return date2 - date1

my_birthday = date(2004, 3, 27)
current_date = date.today()

print(calc_dates_diff(my_birthday, current_date).total_seconds())