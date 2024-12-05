def sort012(arr):
    zeroList = []
    oneList = []
    twoList = []
    for i in arr:
        if i == 0:
            zeroList.append(i)
        elif i == 1:
            oneList.append(i)
        elif i == 2:
            twoList.append(i)
    return zeroList + oneList + twoList

print(sort012())