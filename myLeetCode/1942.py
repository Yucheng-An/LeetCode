times = [[1,4],[2,3],[4,6]]
targetFriend = 1


friendList = []
for i in range(len(times)):
    friendList.append((times[i],i))

print(friendList)
friendList.sort()