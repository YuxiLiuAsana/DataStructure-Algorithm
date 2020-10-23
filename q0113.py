# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        if not root.left and not root.right:
            if root.val == sum:
                return [[sum]]
            else:
                return []
        left = self.pathSum(root.left, sum-root.val)
        right = self.pathSum(root.right, sum-root.val)
        return [[root.val] + x for x in left+right]