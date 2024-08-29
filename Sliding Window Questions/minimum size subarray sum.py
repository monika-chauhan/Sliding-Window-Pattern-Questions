def minimumSizeSubarraySum(nums, target):
    start = 0
    sum = 0
    min_count = float('inf')
    for end in range(len(nums)):
        sum += nums[end]

        while sum >= target:
            min_count = min(min_count, end - start + 1)
            sum -= nums[start]
            start += 1
    if min_count == float('inf'):
        return 0

    return min_count


a = [2, 3, 1, 2, 4, 3]
target = 7
print(minimumSizeSubarraySum(a, target))
