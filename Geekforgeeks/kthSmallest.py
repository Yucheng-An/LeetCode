def kthSmallest(arr,k):
    if not arr:
        return -1

max_element = max(arr)
count = [0] * (max_element + 1)

# Step 1: Count the frequency of each element
for num in arr:
    count[num] += 1

# Step 2: Find the k-th smallest element
cumulative_count = 0
for i in range(len(count)):
    cumulative_count += count[i]
    if cumulative_count >= k:
        return i

return -1

testcase = [7,10,4,3,20,15]
print(kthSmallest(testcase,0))
print(testcase)