# Write a Python program that matches a string that has an "a" followed by two to three "b".
import re

test_strings = ["a", "ab", "abb", "abbb", "ac", "b", "bb"]
for line in test_strings:
    pattern = 'ab{2,3}'
    if re.match(pattern, line):
        print(line)
        