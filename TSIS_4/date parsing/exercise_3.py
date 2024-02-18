# Write a Python program to drop microseconds from datetime.
from datetime import datetime

PATTERN_SHORT = '%d.%m.%Y'
PATTERN_FULL = '%d.%m.%Y %H:%M'

current_dt = datetime.now()

print(current_dt.strftime(PATTERN_SHORT))
print(current_dt.strftime(PATTERN_FULL))
