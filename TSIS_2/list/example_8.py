matrix = [[" D " if i == j else j for j in range(10)] for i in range(10)]
[print(*r) for r in matrix]
