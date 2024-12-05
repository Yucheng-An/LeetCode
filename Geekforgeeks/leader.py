def leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = float('-inf')  # Initialize with the smallest possible value

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    # Reverse the leaders to get the correct order
    leaders.reverse()
    return leaders

# Example usage
arr = [16, 17, 4, 3, 5, 2]
print("Leaders:", leaders(arr))
