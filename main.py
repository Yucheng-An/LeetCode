def maxQualityOfString(y):
    n = len(y)
    OPT = [0] * (n + 1)
    for right in range(1, n + 1):
        maxQuality = float('-inf')
        for left in range(1, right + 1):
            newWord = y[left-1:right]
            subQuality = quality(newWord) + OPT[left - 1]
            maxQuality = max(maxQuality, current_quality)
            # Update base on the right edge max-quality
        OPT[right] = maxQuality
    return OPT[n]