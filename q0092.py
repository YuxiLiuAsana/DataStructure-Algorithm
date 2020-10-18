# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        fake_head = ListNode()
        fake_head.next = head
        i = 0
        current_head = fake_head
        previous_head = None
        start = None
        start1 = None
        while i <= n :
            if i < m-1:
                previous_head = current_head
                current_head = current_head.next
            if i == m-1:
                start = current_head
                previous_head = current_head
                current_head = current_head.next
            if i == m:
                start1 = current_head
                previous_head = current_head
                current_head = current_head.next
            if i > m and i <= n:
                current_next = current_head.next
                current_head.next = previous_head
                previous_head = current_head
                current_head = current_next
            i += 1
        start1.next = current_head
        start.next = previous_head
        return fake_head.next
