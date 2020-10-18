class Solution(object):
    dp = {}
    def minDistance(self, word1, word2):
        if (word1, word2) in self.dp:
            return self.dp[(word1,word2)]
        """Naive recursive solution"""
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            self.dp[(word1, word2)] = self.minDistance(word1[1:], word2[1:])
            return self.dp[(word1,word2)]
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        self.dp[(word1,word2)]=min(insert, replace, delete)
        return self.dp[(word1,word2)]