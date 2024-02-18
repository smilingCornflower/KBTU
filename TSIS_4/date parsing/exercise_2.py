#Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, date, timedelta


PATTERN = '%d.%m.%Y'

today_dt = date.today()
yesterday_dt = today_dt - timedelta(days=1)
tomorrow_dt = today_dt + timedelta(days=1)

print('Yesterday:'.ljust(16), yesterday_dt.strftime(PATTERN))
print('Today:'.ljust(16), today_dt.strftime(PATTERN))
print('Tomorrow'.ljust(16), tomorrow_dt.strftime(PATTERN))