def can_divide(ghouls, max_blocks, max_sum) -> bool:
    current_sum: int = 0
    current_blocks: int = 1

    for ghoul in ghouls:
        if current_sum + ghoul > max_sum:
            current_sum = ghoul
            current_blocks += 1
            if current_blocks > max_blocks:
                return False
        else:
            current_sum += ghoul
    return True


def minimize_max_ghouls(ghouls: list[int], k) -> int:
    left, right = max(ghouls), sum(ghouls)

    while left < right:
        mid = (left + right) // 2
        if can_divide(ghouls, max_blocks, mid):
            right = mid
        else:
            left = mid + 1
    return left

_, max_blocks = map(int, input().split())
ghouls: list[int] = [int(i) for i in input().split()]
result: int = minimize_max_ghouls(ghouls=ghouls, k=max_blocks)
print(result)