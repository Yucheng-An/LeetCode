arr = [100, 98, 23, 55, 89, 12]
pair = []
index = 0
for i in arr:
    pair.append((i, index))
    index += 1
print(arr)
print(pair)

pair.sort(reversed = True, key=lambda x : x[0])
print(pair)
