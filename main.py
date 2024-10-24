def maxQualityOfString(y):
    n = len(y)
    OPT = [0] * (n + 1)
    for right in range(1, n + 1):
        maxQuality = float('-inf')
        for j in range(1, right + 1):
            newWord = y[j-1:right]
            current_quality = quality(newWord) + OPT[j - 1]
            maxQuality = max(maxQuality, current_quality)
        OPT[right] = maxQuality
    return OPT[n]