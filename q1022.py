# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        c=int(1e9+7)

        if root == None: return 0

        if root.left == None and root.right == None:
            return (root.val)%c

        left = 0
        right = 0

        if not root.left == None:
            root.left.val = (root.left.val +  root.val * 2 ) %c
            left = self.sumRootToLeaf(root.left)
        if not root.right == None:
            root.right.val = (root.right.val +  root.val * 2 ) %c
            right = self.sumRootToLeaf(root.right)

        return (left + right)%c


