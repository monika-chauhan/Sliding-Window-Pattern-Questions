def getMinMaxDiffOfKLengthSubbary(nums, k):
    start = 0
    max_avg = float('-inf')
    min_avg = float('inf')
    sum = 0
    for end in range(len(nums)):
        sum += nums[end]

        if end - start + 1 == k:
            avg = sum / k
            max_avg = max(max_avg, avg)
            min_avg = min(min_avg, avg)
            sum -= nums[start]
            start += 1
    return max_avg - min_avg


a = [3, 8, 9, 15]
k = 2
print(getMinMaxDiffOfKLengthSubbary(a, k))
