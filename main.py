
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Node:
    def __init__(self, prev, element, next):
        self.val = element
        self.next = None
        self.prev = None