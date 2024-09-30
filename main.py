#Singal list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Node:
    def __init__(self, prev, element, next):
        self.val = element
        self.next = next
        self.prev = prev