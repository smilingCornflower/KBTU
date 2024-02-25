# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

def math_pattern(text):
    if re.search('a.*b$', text):
        return True
    return False

test_strings = ["acdb", "ab", "abbbbb", "acb", "abbbb", "assdfee", 'ssffaaeeefb']
for l in test_strings:
    if math_pattern(l):
        print(l)
    