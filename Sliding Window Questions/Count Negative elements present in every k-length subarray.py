def countNegElementInKLengthSubarray(nums, k):
    count = 0
    start = 0
    result = []
    for end in range(len(nums)):
        if nums[end] < 0:
            count += 1

        if end - start + 1 == k:
            result.append(count)
            if nums[start] < 0:
                count -= 1
            start += 1
    return result


nums = [-1, 2, -2, 3, 5, -7, -5]
k = 3
print(countNegElementInKLengthSubarray(nums, k))
