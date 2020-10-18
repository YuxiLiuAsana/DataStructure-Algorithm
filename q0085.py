class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0: return 0
        mx = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    mx = max(mx, self.helper(matrix,i,j))
        return mx
    def helper(self, matrix, sr, sc):
        mn = len(matrix[0])-sc
        mx = 0
        for i in range(sr,len(matrix)):
            if matrix[i][sc] == "0":
                break
            for j in range(sc,len(matrix[i]) + 1):
                if j == len(matrix[i]) or matrix[i][j] == "0":
                    mn = min(mn,j-sc)
                    mx = max(mx, (i + 1 -sr)* mn)
                    break
        return mx