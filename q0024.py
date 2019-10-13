# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fakeHead = ListNode(0)
        fakeHead.next = head
        pre = fakeHead
        while pre.next and pre.next.next:
            i = pre.next
            j = i.next
            pre.next = j
            i.next = j.next
            j.next = i
            pre = i
            
        return fakeHead.next
