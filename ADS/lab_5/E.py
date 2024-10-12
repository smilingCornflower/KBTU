import heapq

def process_queries(q, k, queries):
    min_heap = []
    current_sum = 0
    results = []

    for query in queries:
        if query[0] == "insert":
            n = query[1]
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
                current_sum += n
            else:
                if n > min_heap[0]:
                    current_sum += n - min_heap[0]
                    heapq.heapreplace(min_heap, n)
        
        elif query[0] == "print":
            results.append(current_sum)

    return results

q, k = map(int, input().split())
queries = []

for _ in range(q):
    query = input().split()
    if query[0] == "insert":
        queries.append((query[0], int(query[1])))
    else:
        queries.append((query[0],))

results = process_queries(q, k, queries)


for result in results:
    print(result)
