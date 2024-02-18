# Implement a generator called squares to yield the square of all numbers from (a) to (b).
# Test it with a "for" loop and print each of the yielded values.

def gen_squares(start, end):
    n = start
    while n <= end:
        yield n ** 2
        n += 1


a, b = [int(i) for i in input().split()]
squares = gen_squares(a, b)
for i in squares:
    print(i)

