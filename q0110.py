# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root)[0]
    def helper(self, root):
        if not root: return (True, 0)
        (lt,lh) = self.helper(root.left)
        (rt,rh) = self.helper(root.right)
        return ((lt and rt and abs(lh-rh) <= 1), max(lh,rh)+1)