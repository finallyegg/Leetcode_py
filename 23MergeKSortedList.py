# Definition for singly-linked list.
import queue
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        pq = queue.PriorityQueue
        head = point = ListNode(0)
        for i in lists:
            if i:
                pq.put((i.val,i))
        while pq:
            v,node = pq.get()
            
            point.next = ListNode(v)
            point = point.next
            if node.next:
                pq.put((node.next.val,node.next))
        return head.next