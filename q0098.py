# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        v, _, _ = self.helper(root)
        return v
    def helper(self,root):
        mx = mi = root.val
        flag = True
        if root.left:
            lg, lx,li = self.helper(root.left)
            if not lg or lx >= root.val: flag = False
            mx = max(mx, lx)
            mi = min(mi, li)
        if root.right:
            rg, rx, ri = self.helper(root.right)
            if not rg or ri <= root.val: flag = False
            mx = max(mx, rx)
            mi = min(mi, ri)
        return flag, mx, mi
