def maxQualitySegmentation(y):
    n = len(y)
    OPT = [0] * (n + 1)

    # Iterate over all characters in y to fill OPT
    for i in range(1, n + 1):
        # Find the best segmentation ending at position i
        max_quality = float('-inf')
        for j in range(1, i + 1):
            # Consider the word y[j-1:i] (from j to i inclusive)
            word = y[j-1:i]
            # Calculate the quality if this word is used
            current_quality = quality(word) + OPT[j - 1]
            # Update the maximum quality for OPT(i)
            max_quality = max(max_quality, current_quality)

        # Store the best quality achievable for the first i characters
        OPT[i] = max_quality

    # The result is the maximum quality for the full string y
    return OPT[n]