# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0: return None
        if len(preorder) == 1: return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        i = 0
        while True:
            if inorder[i] == preorder[0]: break
            i += 1
        left = self.buildTree(preorder[1:1+i],inorder[:i])
        right = self.buildTree(preorder[1+i:], inorder[1+i:])
        root.left = left
        root.right = right
        return root