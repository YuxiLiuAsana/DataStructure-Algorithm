# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = ListNode(0)
        bigEq = ListNode(0)
        sc = small
        sb = bigEq
        curr = head
        while curr:
            if curr.val < x:
                sc.next = curr
                sc = sc.next
                curr = curr.next
                sc.next= None
            else:
                sb.next = curr
                sb = sb.next
                curr = curr.next
                sb.next = None
        sc.next = bigEq.next
        return small.next
