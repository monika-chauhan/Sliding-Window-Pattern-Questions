def LongestSubStringWithKDistinctChar(s, k):
    window = set()
    high = 0
    low = 0
    start = 0
    end = 0
    freq = [0] * 128

    while high < len(s):
        window.add(s[high])
        freq[ord(s[high])] += 1

        while len(window) > k:
            freq[ord(s[low])] -= 1
            if freq[ord(s[low])] == 0:
                window.remove(s[low])
            low += 1

        if end - start < high - low:
            end = high
            start = low
        high += 1
    return s[start: end+1], len(s[start:end+1])


s = 'abcbdbdbbdcdabd'
k = 2
print(LongestSubStringWithKDistinctChar(s, k))
