def SubstringWithDistinct3Char(s, k):
    freq = {}
    count = 0
    start = 0
    if k > len(s):
        return 0

    for end in range(len(s)):
        if s[end] not in freq:
            freq[s[end]] = 0
        freq[s[end]] += 1

        if end >= k - 1:
            if len(freq) == k:
                count += 1

            freq[s[start]] -= 1
            if freq[s[start]] == 0:
                del freq[s[start]]
            start += 1
    return count


s = 'xyzzaz'
print(SubstringWithDistinct3Char(s, 3))