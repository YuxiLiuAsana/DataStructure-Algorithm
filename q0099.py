#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque


class Solution:
    def recoverTree_Interative(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = None
        start = None
        end = None
        if not root: return root
        dq = deque([(root, 0)])

        while len(dq):
            (last_node, direction) = dq[-1]
            if direction == 0:
                dq[-1] = (last_node, 1)
                if last_node.left:
                    dq.append((last_node.left, 0))
            if direction == 1:
                current = dq.pop()[0]
                if pre and pre.val > current.val and (not start):
                    start = pre
                if pre and pre.val > current.val and start:
                    end = current
                if last_node.right:
                    dq.append((last_node.right, 0))
                pre = current

        start.val, end.val = end.val, start.val
        return root
    def recoverTree_Recursion(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = None
        start = None
        end = None
        def DFS(root):
            nonlocal pre,start,end
            if root.left:
                DFS(root.left)
            if pre and pre.val > root.val and (not start):
                start = pre
            if pre and pre.val > root.val and start:
                end = root
            pre = root
            if root.right:
                DFS(root.right)
        DFS(root)
        start.val, end.val = end.val,start.val
        return root

root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)
s = Solution()
s.recoverTree(root)