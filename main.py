def maxQualityOfString(y):
    n = len(y)
    OPT = [0] * (n + 1)
    for i in range(1, n + 1):
        max_quality = float('-inf')
        for j in range(1, i + 1):
            newWord = y[j-1:i]
            current_quality = quality(newWord) + OPT[j - 1]
            max_quality = max(max_quality, current_quality)
        OPT[i] = max_quality
    return OPT[n]