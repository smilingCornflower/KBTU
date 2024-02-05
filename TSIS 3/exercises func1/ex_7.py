def is_007_there(nums):
    for i in range(len(nums) - 2):
        if nums[i: i + 3] == [0, 0, 7]:
            return True
    return False

good_nums = [0, 1, 2, 3, 4, 0, 0, 7, 8]
bad_nums = [1, 2, 3, 4, 5, 6]

print(is_007_there(good_nums))
print(is_007_there(bad_nums))