# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        number = []
        level = [0]
        pre = ""
        d = 0
        p = ""
        for s in S:
            if s=="-":
                if pre != "-":
                    number += [int(p)]
                    p = ""
                    d = 1
                else:
                    d += 1
            else:
                if pre == "-":
                    level += [d]
                    d = 0
                    p = s
                else:
                    p = p + s
            pre = s
        number += [int(p)]

        nodeMap = {}
        root = None
        for i in range(len(number)):
            if level[i] == 0:
                root = TreeNode(number[i])
                nodeMap[0] = root
            else:
                parent = level[i]-1
                node = TreeNode(number[i])
                if nodeMap[parent].left == None:
                    nodeMap[parent].left =  node
                else: nodeMap[parent].right =  node
                nodeMap[level[i]] = node
        return nodeMap[0]