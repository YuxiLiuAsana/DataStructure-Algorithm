class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        half_index = len(matrix)// 2
        max_col = len(matrix) -1
        for i in range(half_index):
            for j in range(half_index):
                matrix[i][j], matrix[j][max_col-i], matrix[max_col-i][max_col - j], matrix[max_col-j][i] = matrix[max_col-j][i] , matrix[i][j], matrix[j][max_col-i], matrix[max_col-i][max_col - j]
        if len(matrix) % 2 == 1:
            for i in range(half_index):
                matrix[i][half_index], matrix[half_index][max_col-i], matrix[max_col-i][half_index], matrix[half_index][i] =matrix[half_index][i], matrix[i][half_index], matrix[half_index][max_col-i], matrix[max_col-i][half_index]