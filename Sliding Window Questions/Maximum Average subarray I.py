def MaxAvgSubarray(nums, k):
    curr_sum = 0
    max_avg = float('-inf')
    start = 0
    for end in range(len(nums)):
        curr_sum += nums[end]

        if end - start + 1 == k:
            avg = curr_sum / k
            max_avg = max(max_avg, avg)
            curr_sum -= nums[start]
            start += 1
    return max_avg


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(MaxAvgSubarray(nums, k))
