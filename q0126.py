from string import ascii_lowercase
class Node:
    def __init__(self, val, parents = []):
        self.val = val
        self.parents = parents
    def __str__(self):
        return self.val
from collections import deque
from string import ascii_lowercase
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not endWord in wordList:
            return []
        root = Node(beginWord)
        dq = deque()
        dq.append((root, 0))
        wl = set(wordList)
        endNode = None
        pre_level = -1
        add = {}
        while len(dq):
            (head, level) = dq.popleft()
            if level != pre_level:
                for _, value in add.items():
                    wl.remove(value.val)
                add = {}
            pre_level = level
            if self.diffByOne(head.val, endWord):
                endNode = Node(endWord, [head])
                while len(dq) and dq[0][1] == level:
                    (head1, level1) = dq.popleft()
                    if self.diffByOne(endWord, head1.val):
                        endNode.parents += [head1]
                break
            for i in range(len(head.val)):
                for s in ascii_lowercase:
                    newWord = head.val[:i] + s + head.val[1 + i:]
                    if newWord in wl:
                        if not newWord in add:
                            add[newWord] = Node(newWord,[head])
                            dq.append((add[newWord], level + 1))
                        else:
                            add[newWord].parents += [head]
        if endNode:
            return self.formLists(endNode)
        else:
            return []

    def formLists(self, endNode):
        if len(endNode.parents) == 0:
            return [[endNode.val]]
        ret = []
        for p in endNode.parents:
            l = self.formLists(p)
            ret += [x + [endNode.val] for x in l]
        return ret

    def diffByOne(self, s1, s2):
        if len(s1) != len(s2): return False
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
        return diff == 1