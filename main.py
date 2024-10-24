def maxQualityOfString(y):
    n = len(y)
    OPT = [0] * (n + 1)
    for right in range(1, n + 1):
        maxQuality = float('-inf')
        for left in range(1, right + 1):
            newWord = y[left-1:right]
            current_quality = quality(newWord) + OPT[left - 1]
            maxQuality = max(maxQuality, current_quality)
            # Update 
        OPT[right] = maxQuality
    return OPT[n]