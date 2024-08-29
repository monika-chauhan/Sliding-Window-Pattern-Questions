def CountAnagram(text, word):
    ana = ''
    count = 0
    hashMap = {}
    w = len(word)
    for i in range(w):
         ana += text[i]

    if isAnagram(ana, word):
        count += 1

    for i in range(1, len(text)):
        ana = ana[1:] + text[i]

        if ana not in hashMap and isAnagram(ana, word):
            count += 1
            hashMap[ana] = 0
        hashMap[ana] = 0
    return count


def isAnagram(ana, w):

    if len(ana) != len(w):
        return False

    ana_dict = [0] * 26

    for ch in ana:
        ana_dict[ord(ch) - ord('a')] = 1

    for c in w:
        if ana_dict[ord(c) - ord('a')] == 0:
            return False
    return True


word = 'got'
text = 'gotxxotgxdogt'
print(CountAnagram(text, word))
