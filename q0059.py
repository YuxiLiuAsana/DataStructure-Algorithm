class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i = 0
        start = [0, 0]
        ret = [[0] * n for x in range(n)]
        for j in range(1, n * n + 1):
            ret[start[0]][start[1]] = j
            if not self.isValid(start[0] + direction[i][0], start[1] + direction[i][1], ret):
                i = (i + 1) % 4
            start = [start[0] + direction[i][0], start[1] + direction[i][1]]
        return ret

    def isValid(self, i, j, mat):
        return i < len(mat) and j < len(mat) and mat[i][j] == 0