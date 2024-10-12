from copy import deepcopy
from _heapq import heapify, heappop, heappush


def play_rock_game(lst: list[int]) -> int:
    heap: list[int] = [-i for i in lst]
    heapify(heap)

    while len(heap) > 1:
        first: int = heappop(heap)
        second: int = heappop(heap)
        if first != second:
            smash_result: int = first - second
            heappush(heap, smash_result)
    if not heap:
        return 0
    
    result: int = heappop(heap)
    return -result


_ = input()
numbers: list[int] = [int(i) for i in input().split()]
rock_game_result: int = play_rock_game(lst=numbers)

print(rock_game_result)