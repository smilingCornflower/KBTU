def find_commons(seq_1: list, seq_2: list):
    seq_1_copy = seq_1.copy()
    seq_2_copy = seq_2.copy()
    
    result = []
    for i in seq_1:
        if i in seq_2_copy:
            result.append(i)
            seq_1_copy.remove(i)
            seq_2_copy.remove(i)
            
    for i in seq_2_copy:
        if i in seq_1_copy:
            result.append(i)
            seq_1_copy.remove(i)
    return result

size_1, size_2 = [int(i) for i in input().split()]
if size_1 and size_2:
    numbers_1: list[int] = [int(i) for i in input().split()]
    numbers_2: list[int] = [int(i) for i in input().split()]
    result = find_commons(numbers_1, numbers_2)
    print(*sorted(result))
else:
    print()