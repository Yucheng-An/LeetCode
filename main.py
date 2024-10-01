import heapq

arr = [11,23,33,42,54,65]
pq = []
for i,j in enumerate(arr):
    heapq.heappush(pq,i,j)
print(pq)