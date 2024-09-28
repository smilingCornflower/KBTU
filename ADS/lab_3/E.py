n, k = map(int, input().split())
ans = []

for _ in range(n):
    coords = [int(i) for i in input().split()]
    ans.append(max(coords))

ans.sort()
print(ans[k - 1])