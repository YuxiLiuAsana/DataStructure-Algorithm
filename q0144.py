# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        rootLeft = []
        rootRight = []
        if root.left:
            rootLeft = self.preorderTraversal(root.left)
        if root.right:
            rootRight = self.preorderTraversal(root.right)
        return [root.val] + rootLeft + rootRight