# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        fakehead = ListNode(next=head)
        pre = fakehead
        current = head
        while current:
            n = current.next
            current.next = pre
            pre = current
            current = n
        head.next = None
        return pre
