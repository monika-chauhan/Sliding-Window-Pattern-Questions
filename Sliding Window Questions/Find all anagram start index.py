def findIndexOfAnagram(s, p):
    num_s = [0] * 26
    num_p = [0] * 26
    res = []
    start = 0
    for ch in p:
        num_p[ord(ch) - ord('a')] += 1

    for i in range(len(s)):
        num_s[ord(s[i]) - ord('a')] += 1

        if i - start == len(p):
            num_s[ord(s[start]) - ord('a')] -= 1
            start += 1

        if num_p == num_s:
            res.append(start)
    return res


s = 'cbaebabacd'
p = 'abc'
print(findIndexOfAnagram(s, p))
