from copy import deepcopy
from _heapq import heapify, heappop, heappush


def get_min_cost_of_merge(lst: list[int], n: int) -> int:
    heap: list[int] = deepcopy(lst)
    heapify(heap)
    total_cost: int = 0   

    for _ in range(n - 1):
        first: int = heappop(heap)
        second: int = heappop(heap)

        current_cost: int = first + second        
        total_cost += current_cost    

        heappush(heap, current_cost)

    return total_cost


size: int = int(input())
numbers: list[int] = [int(i) for i in input().split()]
merge_min_cost: int = get_min_cost_of_merge(lst=numbers, n=size)

print(merge_min_cost)