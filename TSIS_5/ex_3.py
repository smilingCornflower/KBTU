# Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

def find_sequences(text):
    sequences = re.findall('[a-z]+_[a-z]+', text)
    return sequences

data = 'Los_Angelos spider_man Hello World cyberpank_2077 lenovo flowers_from_dandelions'

for line in find_sequences(data):
    print(line)