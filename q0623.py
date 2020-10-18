# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        start = TreeNode(0)
        start.left = root
        myRoot = self.helper(start,v,d)
        return myRoot.left


    def helper(self, root, v, d):
        if d == 1:
            l = TreeNode(v)
            r = TreeNode(v)
            l.left = root.left
            r.right = root.right
            root.left = l
            root.right = r
        else:
            if root.left: root.left = self.helper(root.left,v,d-1)
            if root.right: root.right = self.helper(root.right,v,d-1)
        return root
