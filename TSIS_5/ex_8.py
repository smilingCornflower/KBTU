import re

def insert_spaces(text):
    pattern = r'([A-Z][^A-Z]*)'
    modified_text = re.sub(pattern, r' \1', text)
    return modified_text

text = "ThisIsAWordStartingWithCapitalLetters"
modified_text = insert_spaces(text)
print(modified_text)