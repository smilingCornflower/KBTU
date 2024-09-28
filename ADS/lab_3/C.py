_, queries = map(int, input().split())
numbers: list[int] = [int(i) for i in input().split()]

result: list[int] = []

for _ in range(queries):
    left_1, right_1, left_2, right_2 = map(int, input().split())
    counter: int = 0
    for i in numbers:
        if left_1 <= i <= right_1 or left_2 <= i <= right_2:
            counter += 1
    result.append(counter)

print(*result, sep="\n")