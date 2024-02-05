def calc_factorial(n: int) -> int:
    if n < 2:
        return 1
    return n * calc_factorial(n - 1)

# Function's logic:

# 1)  calc_factorial(5)
# 2)                    if 5 < 2: --> False
# 3)  5 * factorial(5 - 1)
# 4)                    if 4 < 2: --> False
# 5)  5 * (4 * factorial(4 - 1))
# 6)                    if 3 < 2: --> False
# 7)  5 * (4 * (3 * factorial(3 - 1)))
# 8)                    if 2 < 2: --> False
# 9)  5 * (4 * (3 * (2 * factorial(1))))
# 10)                   if 1 < 2: --> True
# 11) 5 * (4 * (3 * (2 * 1)))