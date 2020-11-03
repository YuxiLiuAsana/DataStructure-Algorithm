"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def copy(node):
            nonlocal visited
            if node.val in visited:
                return visited[node.val]
            newNode = Node(node.val)
            visited[newNode.val] = newNode
            for n in node.neighbors:
                newNode.neighbors += [copy(n)]

            return newNode

        if not node: return None
        return copy(node)
