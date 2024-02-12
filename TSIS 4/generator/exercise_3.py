# Define a function with a generator which can iterate the numbers, 
# which are divisible by 3 and 4, between a given range 0 and n.

def gen_divisible(divisior, up_limit=1000):
    n = divisior
    while n <= up_limit:
        yield n
        n += divisior

some_gen = gen_divisible(12)

for i in some_gen:
    print(i)
