import heapq

def mix_mixtures(m, densities):
    heapq.heapify(densities)
    
    operations = 0
    
    while densities[0] < m:
        if len(densities) < 2:
            return -1

        least = heapq.heappop(densities)
        second_least = heapq.heappop(densities)
        
        new_density = least + 2 * second_least
        
        heapq.heappush(densities, new_density)
        
        operations += 1
    
    return operations


_, m = [int(i) for i in input().split()]
densities = [int(i) for i in input().split()]


result = mix_mixtures(m, densities)
print(result)
