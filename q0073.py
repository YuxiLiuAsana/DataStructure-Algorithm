class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        col = 1
        for i, rv in enumerate(matrix):
            for j, v in enumerate(rv):
                if v == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        col = 0
                    else:
                        matrix[0][j] = 0

        for i, v in enumerate(matrix):
            if i != 0:
                if v[0] == 0:
                    for j in range(len(matrix[i])):
                        matrix[i][j] = 0

        for j, v in enumerate(matrix[0]):
            if j != 0:
                if v == 0:
                    for i in range(len(matrix)):
                        matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        if col == 0:
            for i, v in enumerate(matrix):
                matrix[i][0] = 0


