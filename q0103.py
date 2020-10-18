# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        stack = [(root,1)]
        ret = []
        while len(stack):
            n, l = stack[0]
            if len(ret) < l:
                ret += [[]]
            ret[l-1] += [n.val]
            if n.left: stack += [(n.left, l + 1)]
            if n.right: stack += [(n.right, l+1)]
            stack.pop(0)
        for i in range(1,len(ret),2):
            ret[i] = ret[i][::-1]
        return ret