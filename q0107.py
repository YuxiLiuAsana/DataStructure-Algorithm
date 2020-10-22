# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        dq = deque()
        dq.append((root, 0))
        ret = []
        while len(dq):
            (head,level)=dq.popleft()
            if len(ret) <= level:
                ret += [[]]
            ret[level] += [head.val]
            if head.left:
                dq.append((head.left,level+1))
            if head.right:
                dq.append((head.right,level+1))
        ret.reverse()
        return ret