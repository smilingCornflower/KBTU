VOWELS: str = "aeiou"

input()
line: list[str] = list(input())

line.sort(key=lambda x: (x, x.upper())[x in VOWELS])
print(''.join(line))