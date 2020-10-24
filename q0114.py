# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return root
        def helper(root):
            if not root.left and not root.right:
                return (root, root)
            if not root.left:
                return(root, helper(root.right)[1])
            if not root.right:
                (left, left_end) = helper(root.left)
                root.left = None
                root.right = left
                return (root, left_end)
            else:
                (left, left_end) = helper(root.left)
                (right, right_end) = helper(root.right)
                root.left = None
                root.right = left
                left_end.left = None
                left_end.right = right
                return (root, right_end)
        helper(root)