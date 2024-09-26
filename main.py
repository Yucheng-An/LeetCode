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

