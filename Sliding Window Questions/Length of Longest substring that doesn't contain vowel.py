def lengthOfLongestSubStringNoVowel(string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    result = ''
    max_length = 0
    for i in range(len(string)):
        if string[i] not in vowel:
            result += string[i]
            if len(result) > max_length:
                max_length = len(result)
        else:
            result = ''
    return result, max_length


s = 'codeforintelligents'
print(lengthOfLongestSubStringNoVowel(s))
