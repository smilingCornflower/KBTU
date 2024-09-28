input()
numbers: list[int] = [int(i) for i in input().split()]
numbers_set: set[int] = set(numbers)

height, width = [int(i) for i in input().split()]
matrix: list[list[int]] = [[int(i) for i in input().split()] for _ in range(height)]

result: dict = {}

for i, row in enumerate(matrix):
    for num in (numbers_set & set(row)):
        result[num] = (i, row.index(num))

for num in numbers:
    if num in result:
        print(*result[num])
    else:
        print(-1)