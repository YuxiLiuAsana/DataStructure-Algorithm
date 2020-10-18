class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        stack = [(beginWord, 1)]
        wordList = set(wordList)
        dc = {}
        index = 0
        while index < len(stack):
            w, c = stack[index]
            index += 1
            if w == endWord:
                return c
            dc[w] = c
            for i in range(len(w)):
                for j in string.ascii_lowercase:
                    n = w[:i] + j + w[i+1:]
                    if n in wordList and not n in dc:
                        stack += [(n, c+1)]
        return 0