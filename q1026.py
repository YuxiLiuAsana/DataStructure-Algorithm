# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    my_max = 0
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root == None: return 0
        else:
            self.findMinMax(root)
            return self.my_max

    def findMinMax(self, root: TreeNode) -> (int, int):

        if root.left == None and root.right == None:
            return (root.val, root.val)
        self_min = root.val
        self_max = root.val
        if not root.left == None:
            (temp_min, temp_max) =self.findMinMax(root.left)
            self_min = min(self_min, temp_min)
            self_max = max(self_max, temp_max)
        if not root.right == None:
            (temp_min, temp_max) = self.findMinMax(root.right)
            self_min = min(self_min, temp_min)
            self_max = max(self_max, temp_max)
        step_max = max(self_max-root.val, root.val-self_min)
        self.my_max = max(step_max, self.my_max)
        return (self_min, self_max)


