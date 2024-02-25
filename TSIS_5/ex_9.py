# Write a Python program to convert a given camel case string to snake case.
from ex_7 import split_at_upper


def convert_camel_to_snake(line: str) -> str:
    line = split_at_upper(line)
    return '_'.join(map(str.lower, line))

text = 'ThisIsCamleStyleString'

print(convert_camel_to_snake(text))