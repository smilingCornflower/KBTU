start, end = int(input()), int(input())
numbers = [i for i in range(start, end + 1)]
print(*numbers)
print('some change')
print(start * end)

def div(x, y):
    return x / y
