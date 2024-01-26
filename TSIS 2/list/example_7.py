from string import ascii_lowercase

letters = list(ascii_lowercase)
[print(f"Letter: {l} \t ASCII number: {ord(l)}") for l in letters]