# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _,m = self.helper(root)
        return m

    def helper(self, root):
        # max through this root
        # max under this nood
        lp,lm,rp, rm = None, None, None, None
        if root.left:
            lp,lm = self.helper(root.left)
        if root.right:
            rp,rm = self.helper(root.right)
        left,right = root.val, root.val
        if lp :
            left= max(left, lp + root.val)
        if rp:
            right = max(right, rp + root.val)
        p = max(left, right)
        u = left + right - root.val
        if lm :
            u = max(u, lm)
        if rm:
            u = max(u, rm)
        return (p, u)
