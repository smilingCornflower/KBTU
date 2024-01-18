start, end = int(input()), int(input())
numbers = [i for i in range(start, end + 1)]
print(*numbers)
print('some change')
print(start * end)

def add(x, y):
    return x + y

def mult(x, y):
    return x * y


def div(x, y):
    return x / y

print(mult(start, end))
print(div(start, end))
