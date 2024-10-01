arr = [100,98,23,55,54,65]
pair = []
index = 0
for i in arr:
    pair.append((i,index))
    index += 1
print(arr)
print(pair)

pair.sort()
print(pair)