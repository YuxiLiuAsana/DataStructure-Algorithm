class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0: return []
        if len(matrix[0]) == 0: return []
        return self.helper(matrix, 0,len(matrix)-1, 0,len(matrix[0])-1)
    def helper(self, matrix, row_top, row_bottom, col_left, col_right) -> List[int]:
        if row_top > row_bottom: return []
        if col_left > col_right: return []
        if row_top == row_bottom:
            return matrix[row_top][col_left:col_right+1]
        if col_left == col_right:
            return[x[col_left] for x in matrix[row_top:row_bottom+1]]
        ret = []
        for i in range(col_left, col_right + 1):
            ret += [matrix[row_top][i]]
        for i in range(row_top+1, row_bottom+1):
            ret += [matrix[i][col_right]]
        for i in range(col_right-1, col_left-1, -1):
            ret += [matrix[row_bottom][i]]
        for i in range(row_bottom-1, row_top, -1):
            ret += [matrix[i][col_left]]
        ret += self.helper(matrix, row_top + 1, row_bottom-1,col_left + 1, col_right -1)
        return ret