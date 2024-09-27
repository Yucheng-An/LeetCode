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

def timeConversion(s):
    hours = s[0] + s[1]
    minutes = s[3] + s[4]
    seconds = s[6] + s[7]
    if s[8] + s[9] == "PM":
        hours = int(hours) + 12
        if hours == 24:
            hours = 00
        return str(hours)+ ":" + minutes + ":" + seconds
    elif s[8] + s[9] == "AM":
        if hours == "12":
            hours == "00"
        return hours + ":" + minutes + ":" + seconds

timeConversion("12:40:22AM")
