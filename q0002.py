# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h =  p = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            s = a + b + carry
            carry = s//10
            p.next = ListNode(s %10)
            p = p.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        return h.next
