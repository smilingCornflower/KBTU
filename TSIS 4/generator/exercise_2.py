# Write a program using generator to print the even numbers between 0 and n
# in comma separated form where n is input from console.


def gen_evens(end_seq):
    n = 0
    while n <= end_seq:
        yield n
        n += 2

num = int(input())

x = gen_evens(num)

print(*x, sep=', ')