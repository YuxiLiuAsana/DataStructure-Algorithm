"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        newHead = Node(head.val)
        current = head
        newCurrent = newHead
        object_map = {}
        object_map[id(current)] = newCurrent
        while current.next:
            newCurrent.next = Node(current.next.val)
            current = current.next
            newCurrent = newCurrent.next
            object_map[id(current)] = newCurrent
        object_map[id(current)] = newCurrent
        current = head
        newCurrent = newHead

        while current:
            if current.random == None:
                newCurrent.random = None
            else:
                newCurrent.random = object_map[id(current.random)]
            current = current.next
            newCurrent = newCurrent.next
        return newHead