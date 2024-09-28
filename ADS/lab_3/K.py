def min_subarray_length(n, k, arr):
    start = 0
    curr_sum = 0
    min_length = float('inf')

    for end in range(n):
        curr_sum += arr[end]

        while curr_sum >= k:
            min_length = min(min_length, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    return min_length if min_length != float('inf') else 0

n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = min_subarray_length(n, k, arr)
print(result)
