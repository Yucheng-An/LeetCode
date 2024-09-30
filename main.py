
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Node:
    def __init__(self, prev, element, next):
        self.val = element
        self.next = None
        self.prev = None



# 长度为 5 的数组
arr = [1, 2, 3, 4, 5]
i = 0
# 模拟环形数组，这个循环永远不会结束
while i < len(arr):
    print(arr[i])
    i = (i + 1) % len(arr)
