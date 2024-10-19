size_1, size_2 = map(int, input().split())
if size_1 != 0 and size_2 != 0:
    numbers_1: list[int] = [int(i) for i in input().split()]
    numbers_2: list[int] = [int(i) for i in input().split()]
    result: list[int] = []
    for i in numbers_1:
        if i in numbers_2:
            numbers_2.remove(i)
            result.append(i)
    print(*sorted(result))
elif size_1 != 0 or size_2 != 0:
    _ = input()
    print()
else:
    print()