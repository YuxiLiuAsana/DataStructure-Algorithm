class Solution:
   
    def solveSudoku(self, board: List[List[str]]) -> None:
        empty_cell = []  # all the empty cells given
        potential_values = []  # the next value that we can try on this cell
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty_cell += [[i, j]]
        potential_values = [1] * len(empty_cell)
        index = 0  # the next empty cell index we should try
        while index < len(empty_cell):
            board[empty_cell[index][0]][empty_cell[index][1]] = "."
            flag = False
            for p in range(potential_values[index], 10):
                if self.checkValidity(empty_cell[index][0], empty_cell[index][1], board, str(p)):
                    board[empty_cell[index][0]][empty_cell[index][1]] = str(p)
                    potential_values[index] = p + 1
                    index += 1
                    flag = True
                    break
            if not flag:
                potential_values[index] = 1
                index -= 1
        
            
            
    def checkValidity(self, i, j, board, target):
        for k in range(9):
            if board[i][k] == target: return False
            if board[k][j] == target: return False
        block_start_row = i // 3 * 3
        block_start_col = j // 3 * 3
        for m in range(block_start_row, block_start_row + 3):
            for n in range(block_start_col, block_start_col + 3):
                if board[m][n] == target: return False
        return True
        
