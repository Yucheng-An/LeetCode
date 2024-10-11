times = [[3,10],[1,5],[2,6]]
friendList = []
for i in range(len(times)):
    friendList.append((times[i],i))

friendList.sort(key=lambda x: x[0][0])

chair 
print(friendList)
for people in friendList:
