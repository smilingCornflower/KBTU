# Given a list of ints, return True if the array 
# contains a 3 next to a 3 somewhere.

def is_33_there(numbers):
    for i, n in enumerate(numbers):
        if n == 3 and numbers[i + 1] == 3:
            return True
    return False


good_nums = [1, 2, 2, 3, 3, 4, 5]
bad_nums = [1, 2, 3, 4, 5]

print(is_33_there(good_nums))
print(is_33_there(bad_nums))