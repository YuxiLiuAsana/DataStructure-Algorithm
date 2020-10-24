"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dp = deque()
        if not root: return root
        dp.append((root, 0))
        while len(dp):
            (current, level) = dp.popleft()
            if current.left:
                dp.append((current.left, level + 1))
            if current.right:
                dp.append((current.right, level + 1))
            if len(dp) != 0 and level == dp[0][1]:
                current.next = dp[0][0]
        return root