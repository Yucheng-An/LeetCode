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
def findMissing(inputList, left, right, start):
    if left >= right:
        return start + left
    mid = (left + right) // 2
    if inputList[mid] == start + mid:
        return findMissing(inputList, mid + 1, right, start)
    else:
        return findMissing(inputList, left, mid, start)

# Example usage:
arr = [9, 10, 11, 12, 13, 15, 16]
missing_number = findMissing(arr, 0, len(arr), arr[0])


def findLargestIndex(arr, left, right):
    if left == right:
        return left
    mid = (left + right) // 2
    left_pos = findLargestIndex(arr, left, mid)
    right_pos = findLargestIndex(arr, mid + 1, right)
    if arr[left_pos] > arr[right_pos]:
        return left_pos
    else:
        return right_pos

# Example usage:
arr = [3, 6, 2, 9, 7, 5]
position = findLargestIndex(arr, 0, len(arr) - 1)
print("The largest element is at position:", position)
