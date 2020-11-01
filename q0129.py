# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ret = 0

        def helper(root):
            nonlocal ret
            if not root: return
            if not root.left and not root.right:
                ret += root.val
            if root.left:
                left_level = self.getLevel(root.left.val)
                root.left.val += root.val * pow(10, left_level + 1)
                helper(root.left)
            if root.right:
                right_level = self.getLevel(root.right.val)
                root.right.val += root.val * pow(10, right_level + 1)
                helper(root.right)

        helper(root)
        return ret

    def getLevel(self, number):
        if number == 0:
            return 0
        else:
            return int(math.log10(numberl))