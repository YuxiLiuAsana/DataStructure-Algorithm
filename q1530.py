# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        return self.helper(root, distance)[0]

    def helper(self, root:TreeNode, distance: int) :
        if not root: return (0, [])
        if not root.left and not root.right: return (0, [0])
        left, distance_left = self.helper(root.left, distance)
        right, distance_right = self.helper(root.right, distance)
        i = 0
        j = len(distance_right) -1
        through = 0
        while i < len(distance_left) and j >=0:
            while distance_left[i] + distance_right[j] + 2 > distance and j >= 0:
                j -= 1
            through += (j+1)
            i += 1
        return (through + left + right, self.mergesort(distance_left, distance_right))
    def mergesort(self, left, right):
        i = 0
        j = 0
        ret = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ret += [left[i] + 1]
                i += 1
            else:
                ret += [right[j] + 1]
                j += 1
        ret += [(x + 1) for x in left[i:]]
        ret += [(x + 1) for x in right[j:]]
        return ret
