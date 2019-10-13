# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None: return None
        fast = head
        i = n-1
        while i:
            fast = fast.next
            i = i -1
        slow = head
        pre = ListNode(0)
        pre.next = head
        start = pre
        while fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next
        pre.next = slow.next
        return start.next
        
