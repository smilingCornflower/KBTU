# Write a Python program to split a string at uppercase letters
import re
def split_at_upper(line: set) -> list:
    parts = re.findall('[A-Z][^A-Z]*', line)
    return parts
string = "SplitThisStringAtUpperCaseLetters"
print(split_at_upper(string))