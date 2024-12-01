def count_greater(inputArray, targetVlue):
    if len(inputArray) == 0:
        return 0
    if len(inputArray) == 1:
        return 1 if inputArray[0] > targetVlue else 0
    right = inputArray[len(inputArray) // 2:]
    return count_greater(inputArray[:len(inputArray) // 2], targetVlue) + count_greater(inputArray[len(inputArray) // 2:], targetVlue)


A = [1, 2, 3, 4, 5, 6, 7, 8]
x = 6
res = count_greater(A, x)
print(res)
