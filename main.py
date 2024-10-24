def maxQualityOfString(y):
    n = len(y)
    OPT = [0] * (n + 1)
    for i in range(1, n + 1):
        maxQuality = float('-inf')
        for j in range(1, i + 1):
            newWord = y[j-1:i]
            current_quality = quality(newWord) + OPT[j - 1]
            maxQuality = max(maxQuality, current_quality)
        OPT[i] = maxQuality
    return OPT[n]