class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.valid9(0,9,i,i+1, board): return False
            if not self.valid9(i,i+1,0,9, board): return False
        for i in range(0,3):
            for j in range(0,3):
                if not self.valid9(i * 3, i * 3 + 3, j * 3, j * 3 + 3, board):
                    return False
        return True
        
    def valid9(self,rowStart, rowEnd, colStart, colEnd, board):
        value = set()
        for i in range(rowStart, rowEnd):
            for j in range(colStart, colEnd):
                if board[i][j] != ".":
                    if board[i][j] in value: return False
                    else: value.add(board[i][j])
        return True          
