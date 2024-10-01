arr = [100, 98, 23, 55, 89, 12]


for index , value in enumerate(arr):
    arr[index]= (value, index)

print(pair)

pair.sort(key=lambda x: x[1], reverse = True)
print(pair)
