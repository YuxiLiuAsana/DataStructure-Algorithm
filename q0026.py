# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        fakeHead = ListNode(0)
        fakeHead.next = head
        pre = fakeHead
        while pre.next:
            start = pre.next
            end = start
            print(start.val, end.val)
            for _ in range(k-1):
                end = end.next
                if not end:
                    return fakeHead.next
            post = end.next
            
            last = post
            i = start
            while i != post:
                j = i.next
                i.next = last
                last = i
                i = j
            pre.next = end 
            pre = start
        return fakeHead.next
            
            
        
        
