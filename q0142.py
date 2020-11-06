# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        current = head
        while True:
            if id(current) in visited: return current
            if current == None: return None
            visited.add(id(current))
            current = current.next
