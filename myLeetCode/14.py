def longestCommonPrefix(strs):
    # Edge case: If the array is empty, return an empty string
    if not strs:
        return ""

    # Start by assuming the prefix is the first string
    prefix = strs[0]

    # Compare the prefix with each string in the list
    for s in strs[1:]:
        # Update the prefix by reducing it until it matches
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            # If the prefix is reduced to an empty string, return ""
            if not prefix:
                return ""

    return prefix





# this is test


# Example usage:
strings = ["flower", "flow", "flight"]
print(longestCommonPrefix(strings))  # Output: "fl"