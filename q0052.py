class Solution(object):
    num = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.num = 0
        def dfs(row, diff, add):
            p = len(row)
            if p == n:
                self.num = self.num + 1
            for q in range(n):
                if (not q in row) and (not p-q in diff) and (not p + q in add):
                    dfs(row+[q], diff+[p-q], add+[p+q])
        dfs([],[],[])
        return self.num