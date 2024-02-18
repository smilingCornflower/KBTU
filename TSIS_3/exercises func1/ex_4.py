# Write a function that accepts string from user
# and print all permutations of that string.
from itertools import permutations

line = input()

perms = [''.join(p) for p in permutations(line)]
print(perms)