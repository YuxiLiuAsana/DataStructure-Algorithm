# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        fake_head = ListNode(head.val-1)
        fake_head.next = head
        pre = fake_head
        current = head
        while current:
            if current.val != pre.val:
                pre.next = current
                pre = pre.next
            current = current.next
        pre.next= None
        return fake_head.next
