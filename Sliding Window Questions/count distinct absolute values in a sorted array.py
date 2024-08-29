def getCountDistinct(nums):
    count = 0
    d = {}
    for item in nums:
        if item >= 0 and item not in d:
            d[item] = 1
            count += 1
    return count


nums = [-1, -1, 0, 1, 1, 1]
print(getCountDistinct(nums))
