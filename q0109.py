# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def size(self, head):
        c = 0
        current = head
        while current:
            c += 1
            current = current.next
        return c

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        size = self.size(head)
        current = head

        def helper(start, end):
            nonlocal current
            if start >= end:
                return None
            mid = (start + end) // 2
            left = helper(start, mid)
            root = TreeNode(current.val)
            root.left = left
            current = current.next
            root.right = helper(mid + 1, end)
            return root

        return helper(0, size)