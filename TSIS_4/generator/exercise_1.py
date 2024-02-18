# Create a generator that generates the squares of numbers up to some number N.

def gen_nums(end_seq):
    n = 1
    while n <= end_seq:
        yield n
        n += 1

x = gen_nums(10)
y = gen_nums(20)
z = gen_nums(5)
print(*x)
print(*y)
print(z.__next__())
print(z.__next__())
print(z.__next__())
print(z.__next__())
print(z.__next__())