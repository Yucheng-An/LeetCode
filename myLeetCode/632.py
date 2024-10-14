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
def find_missing(inputList, left, right, start):
    if left >= right:
        return start + left
    mid = (left + right) // 2
    if inputList[mid] == start + mid:
        return find_missing(inputList, mid + 1, right, start)
    else:
        return find_missing(inputList, left, mid, start)

# Example usage:
arr = [9, 10, 11, 12, 13, 15, 16]
missing_number = find_missing(arr, 0, len(arr), arr[0])
print("The missing number is:", missing_number)


# # Example usage:
# # inputList = [0, 1, 3, 4, 5, 6]
# inputList = [1,2,4,5,6,7,8]
# missing_number = find_missing(inputList, 0, len(inputList))
# print("The missing number is:", missing_number)
