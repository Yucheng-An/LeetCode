def hasCycle(self, head:) -> bool:
    f = head
    s = head
    while f is not None and f.next is not None:
        f = f.next.next
        s = s.next
        if f == s:
            break
    if not f or not f.next:
        return False
    s = head
    while s != f:
        s = s.next
        f = f.next
    return True