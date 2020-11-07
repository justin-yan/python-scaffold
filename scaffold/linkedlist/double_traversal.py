# https://leetcode.com/problems/add-two-numbers/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    cursor1 = l1
    cursor2 = l2
    outputhead = outputcursor = ListNode(0) # double assignment
    carry = 0
    while cursor1 or cursor2 or carry: # use of carry ensures last node appended
        # add two digits
        v1 = cursor1.val if cursor1 else 0
        v2 = cursor2.val if cursor2 else 0
        cursor1 = cursor1.next if cursor1 else None
        cursor2 = cursor2.next if cursor2 else None

        carry, remainder = divmod(v1 + v2 + carry, 10)
        outputcursor.next = ListNode(remainder)
        outputcursor = outputcursor.next

    return outputhead.next