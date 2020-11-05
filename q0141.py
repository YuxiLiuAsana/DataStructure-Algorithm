# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        fast = head.next
        slow = head
        while True:
            if fast == slow: return True
            if fast.next == None: return False

            fast = fast.next
            if fast.next == None: return False
            fast = fast.next
            slow = slow.next
