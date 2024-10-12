import heapq

def max_money_from_tickets(x, seats):
    max_heap = [-seat for seat in seats]
    heapq.heapify(max_heap)
    
    total_money = 0
    
    for _ in range(x):
        max_seats = heapq.heappop(max_heap)
        total_money += max_seats
        
        if max_seats < -1:
            heapq.heappush(max_heap, max_seats + 1)
    
    return -total_money


_, x = [int(i) for i in input().split()]
seats = [int(i) for i in input().split()]

print(max_money_from_tickets(x, seats))
