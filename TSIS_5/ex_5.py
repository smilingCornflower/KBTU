# Write a Python program to replace all occurrences of space,
# comma, or dot with a colon.
import re

def replace_it(text: str) -> str:
    new_text = re.sub(r'[ ,.]', ':', text)
    return new_text



string = "The quick brown fox jumps over the lazy dog. However, the lazy dog doesn't seem to care."
print(replace_it(string))