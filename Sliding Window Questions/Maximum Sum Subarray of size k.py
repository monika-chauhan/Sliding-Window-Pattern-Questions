def maxSumSubarray(nums, k):
    start = 0
    max_sum = float('-inf')
    sum = 0
    for end in range(len(nums)):
        sum += nums[end]
        if end - start + 1 == k:
            max_sum = max(max_sum, sum)
            sum -= nums[start]
            start += 1
    return max_sum


a = [3, 5, 2, 1, 7]
k = 2
print(maxSumSubarray(a, k))
