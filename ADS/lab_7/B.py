_ = input()
numbers_1 = [int(i) for i in input().split()]

_ = input()
numbers_2 = [int(i) for i in input().split()]

numbers = numbers_1 + numbers_2
numbers.sort()

print(*numbers)