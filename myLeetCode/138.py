def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return None
    current = head
    while current:
        copy = Node(current.val, current.next)
        current.next = copy
        current = copy.next
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    current = head
    dummy = Node(-1)
    copyCurrent = dummy
    while current:
        copy = current.next
        copyCurrent.next = copy
        copyCurrent = copy

        current.next = copy.next
        current = current.next
    return dummy.next