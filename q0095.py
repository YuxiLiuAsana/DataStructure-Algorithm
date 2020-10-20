# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        cache = {}
        def helper(start, end):
            nonlocal cache
            if (start,end) in cache:
                return cache[(start,end)]
            if start == end:
                cache[(start,end)]=[TreeNode(start)]
                return cache[(start,end)]
            ret=[]
            for i in range(start,end+1):
                left = [None]
                right = [None]
                if i != start:
                    left = helper(start,i-1)
                if i != end:
                    right = helper(i+1, end)
                for l in left:
                    for r in right:
                        head = TreeNode(i, left = l, right = r)
                        ret += [head]
            cache[(start, end)] = ret
            return ret
        return helper(1,n)


