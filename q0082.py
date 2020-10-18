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
        pre_value = fake_head
        pre = fake_head
        current = head
        count = 0
        while current:
            if current.val != pre.val:
                if count == 1:
                    pre_value.next = pre
                    pre_value = pre_value.next
                count = 1
            else:
                count += 1
            pre = current
            current = current.next
        if count == 1:
            pre_value.next = pre
            pre_value = pre_value.next
        pre_value.next = None
        return fake_head.next
