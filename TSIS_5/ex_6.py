# Write a python program to convert snake case string to camel case string
import re

def snake_to_camel(text):
    words = re.split(r'_', text)
    camel_case_string = ''.join(word.capitalize() for word in words)
    return camel_case_string


snake = 'snake_style_text_sss'
camel = snake_to_camel(snake)
print(camel)