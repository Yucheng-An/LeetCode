def mergeAlternately(word1, word2):
    p1 = 0
    p2 = 0
    res = ""
    while p1 < len(word1) and p2 < len(word2):
        res += word1[p1]
        res += word2[p2]
        p1 += 1
        p2 += 1
    if p1 < len(word1):
        for i in range(p1,len(word1)):
            res += word1[p1]
    else:
        for i in range(p2,len(word2)):
            res += word2[i]
    return res

word1 ="ab"
word2 ="pqrs"
print(mergeAlternately(word1, word2))
print(word2[0:len(word2)-1])
