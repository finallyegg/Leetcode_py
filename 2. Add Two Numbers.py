# June 11 2020
# Linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def helper(self, l1, l2, p):
        if not l1 and not l2 and not p:
            return None

        t = False
        ret = ListNode(0, None)

        o1 = None
        o2 = None
        if l1:
            ret.val += l1.val
            o1 = l1.next
        if l2:
            ret.val += l2.val
            o2 = l2.next
        if p:
            ret.val += 1

        if ret.val >= 10:
            ret.val = ret.val % 10
            t = True

        ret.next = self.helper(o1, o2, t)
        return ret

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.helper(l1, l2, False)
