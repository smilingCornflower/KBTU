def count_case(s):
    uppers = sum([1 for char in s if char.isupper()])
    lowers = sum([1 for char in s if char.islower()])
    return uppers, lowers

s = "Hello World"
upper, lower = count_case(s)
print(f"Upper case: {upper}, Lower case: {lower}")
