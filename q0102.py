# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        stack = [(root, 1)]
        ret = []
        while len(stack):
            n, i = stack[0]
            if len(ret) < i:
                ret += [[]]
            ret[i-1] += [n.val]
            if n.left: stack += [(n.left,i + 1)]
            if n.right: stack += [(n.right, i+1)]
            stack.pop(0)
        return ret