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
def find_missing(arr, left, right, start):
    # Base case: if left and right converge, return the missing number
    if left >= right:
        return start + left

    # Find the middle index
    mid = (left + right) // 2

    # If the value at mid matches the expected value (start + mid), the missing number is in the right half
    if arr[mid] == start + mid:
        return find_missing(arr, mid + 1, right, start)
    # Otherwise, the missing number is in the left half
    else:
        return find_missing(arr, left, mid, start)

# Example usage:
arr = [1, 2, 4, 5, 6, 7, 8]
missing_number = find_missing(arr, 0, len(arr), arr[0])
print("The missing number is:", missing_number)


# Example usage:
# arr = [0, 1, 3, 4, 5, 6]
arr = [1,2,4,5,6,7,8]
missing_number = find_missing(arr, 0, len(arr))
print("The missing number is:", missing_number)
