# Implement a generator that returns all numbers from (n) down to 0.

def gen_reverse(start_seq):
    n = start_seq
    while n > -1:
        yield n
        n -= 1

x = gen_reverse(10)
print(*x)