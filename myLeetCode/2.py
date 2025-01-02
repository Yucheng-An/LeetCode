def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0
    while l1 is not None or l2 is not None or carry > 0:
        if l1:
            val1 = l1.val
        else:
            val1 = 0
        if l2:
            val2 = l2.val
        else:
            val2 = 0
        total = val1 + val2 + carry
        carry = total // 10
        newVal = total % 10
        current.next = ListNode(newVal)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next        