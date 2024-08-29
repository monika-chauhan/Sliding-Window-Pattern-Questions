def minimumSumSubarrayK(nums, k):
    min_sum = float('inf')
    sum = 0
    start = 0
    for end in range(len(nums)):
        sum += nums[end]

        if end - start + 1 == k:
            min_sum = min(min_sum, sum)
            sum -= nums[start]
            start += 1
    return min_sum


nums = [10, 4, 2, 5, 6, 3, 8, 1]
k = 3
print(minimumSumSubarrayK(nums, k))
