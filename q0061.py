# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None: return None
        if k == 0: return head
        fast = head
        count = 0
        for i in range(k):
            if fast.next == None:
                count += 1
                fast = head
                break
            else:
                fast = fast.next
                count += 1
        for i in range(k%count):
                fast = fast.next
        slow = head
        if fast == slow: return head
        while fast.next!= None:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head