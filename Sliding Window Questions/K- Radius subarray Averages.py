def kRadiusSubarrayAvg(nums, k):
    output = [-1] * len(nums)
    preSum = [0] * len(nums)

    preSum[0] = nums[0]
    for i in range(1, len(nums)):
        preSum[i] = preSum[i - 1] + nums[i]
    print(preSum)

    for i in range(k, len(nums) - k):
        if i - k - 1 < 0:
            output[i] = (preSum[i + k]) // (2 * k + 1)
        else:
            output[i] = (preSum[i+k] - preSum[i-k-1]) // (2 * k + 1)
    return output


nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
k = 3
print(kRadiusSubarrayAvg(nums, k))