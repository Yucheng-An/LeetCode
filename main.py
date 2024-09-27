from audioop import reverse

print("Nice to meet you")
t = [130291875,474356040,1,8]
t.sort(reverse=True)
def minTime(files, numCores, limit):
    files.sort(reverse=True)
    result = 0
    for file in files:
        if file >= numCores and limit != 0:
            result = result + (file//numCores)
            limit -= 1
        else:
            result = result + file
    return result
print(minTime(t,5,3))

t = int(input().strip())
result = []
for a0 in range(t):
    n = int(input().strip())
    count = 0
    for i in range(1,n+1):
        if i % 3 == 0 or i % 5 == 0:
            count += i
            print(count)
    result.append(count)
print(result)
