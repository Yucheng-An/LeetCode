def find(il):
    if len(il) == 1:
        return None
    if il[-1] - il[-2] == 1:
        il.pop()
        return find(il)
    else:
        return il[-1] - 1


t = [0, 1, 3, 4, 5, 6]
print(find(t))
def find_missing(arr, left, right):
    # Base case: if left and right converge, return the missing number
    if left >= right:
        return left

    # Find the middle index
    mid = (left + right) // 2

    # If the value at mid matches the index, the missing number is in the right half
    if arr[mid] == mid:
        return find_missing(arr, mid + 1, right)
    # Otherwise, the missing number is in the left half
    else:
        return find_missing(arr, left, mid)

# Example usage:
arr = [0, 1, 3, 4, 5, 6]
missing_number = find_missing(arr, 0, len(arr))
print("The missing number is:", missing_number)
