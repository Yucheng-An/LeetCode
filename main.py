class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Node:
    def __init__(self, prev, element, next):
        self.val = element
        self.next = None
        self.prev = None


class Solution:
    def findListKNode(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        for _ in range(n):
            p1 = p1.next
        p2 = head
        while p1 != None:
            p1 = p1.next
            p2 = p2.next
        return p2

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        x = self.findListKNode(dummy, n + 1)
        x.next = x.next.next
        return dummy.next