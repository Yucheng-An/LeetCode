citations = [3,0,6,1,5]
citations.sort(reverse=True)
print(citations)
newlist =[]
for i in range(1,len(citations)+1):
    newlist.append(i)
print(newlist)
for i in range(len(citations)):
    if citations[i] 