import queue

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ListNode()
        q = queue.Queue()
        q.put(a)

        while q:
            head = q.get()
            if not l1:
                head = l2
            elif not l2:
                head = l1
            else:
                if l1.val <= l2.val:
                    head = l1
                    l1 = l1.next
                else:
                    head = l2
                    l2 = l2.next
                head.next = ListNode()
                q.put(head.next)
        return a
