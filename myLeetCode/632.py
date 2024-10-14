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
