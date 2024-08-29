def CountOccurrence(word, text):
    wHeap = [0] * 26
    tHeap = [0] * 26
    start = 0
    count = 0

    for ch in word:
        wHeap[ord(ch) - ord('a')] += 1

    for i in range(len(text)):
        tHeap[ord(text[i]) - ord('a')] += 1
        if (i - start + 1) == len(word):
            if wHeap == tHeap:
                count += 1
            tHeap[ord(text[start]) - ord('a')] -= 1
            start += 1
    return count


word = 'got'
text = 'gotxxotgxdogt'
print(CountOccurrence(word, text))
