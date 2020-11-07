# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None: return None
        if head.next == None: return head
        if head.next.next == None:
            if head.val > head.next.val:
                head.val, head.next.val = head.next.val, head.val
            return head
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        slowNext = slow.next
        slow.next = None
        start1 = self.sortList(head)
        start2 = self.sortList(slowNext)

        fakeHead = ListNode(0)
        current = fakeHead
        s1 = start1
        s2 = start2
        while s1 != None and s2 != None:
            if s1.val < s2.val:
                current.next = s1
                s1 = s1.next
            else:
                current.next = s2
                s2 = s2.next
            current = current.next
        if s1!= None:
            current.next = s1
        if s2!= None:
            current.next = s2
        return fakeHead.next

