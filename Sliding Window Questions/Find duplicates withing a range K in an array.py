def findDuplicateWithInRangeK(nums, k):
    num_dict = {}
    for i, num in enumerate(nums):
        if num in num_dict and i - num_dict[num] <= k:
            return True
        num_dict[num] = i
    return False


nums = [5, 6, 8, 2, 4, 6, 9]
k = 2
print(findDuplicateWithInRangeK(nums, k))
