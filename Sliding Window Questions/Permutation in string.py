def permutation(s1, s2):
    dict_s1 = [0] * 26
    dict_s2 = [0] * 26
    for ch in s1:
        dict_s1[ord(ch) - ord('a')] += 1

    for index in range(0, len(s2)):
        dict_s2[ord(s2[index]) - ord('a')] += 1

        if index >= len(s1) - 1:
            if dict_s1 == dict_s2:
                return True

            dict_s2[ord(s2[index-len(s1)+1]) - ord('a')] -= 1
    return False
s1 = 'ab'
s2 = 'eidbaooo'
print(permutation(s1, s2))
