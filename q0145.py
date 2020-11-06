# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        rootLeft = []
        rootRight = []
        if root.left:
            rootLeft = self.postorderTraversal(root.left)
        if root.right:
            rootRight = self.postorderTraversal(root.right)
        return rootLeft + rootRight + [root.val]