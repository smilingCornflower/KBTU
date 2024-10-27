size: int = int(input())
lines: list[list[str]] = [input().split() for _ in range(size)]

for line in lines:
    line: list[str] = sorted(line, key=len)
    print(*line)
