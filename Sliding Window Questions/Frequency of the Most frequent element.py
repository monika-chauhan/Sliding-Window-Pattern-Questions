def frequencyOfMostfrequent(nums, k):
    n = len(nums)
    nums.sort()
    max_freq = 1
    freq = 1
    left = 0
    ops = k
    for right in range(len(nums)):
        ops -= (nums[right] - nums[right - 1]) * freq
        freq += 1
        if ops >= 0:
            max_freq = max(freq, max_freq)
        else:
            while ops < 0:
                ops += nums[right] - nums[left]
                left += 1
                freq -= 1
    return max_freq


nums = [1, 2, 4]
k = 3
print(frequencyOfMostfrequent(nums, k))
