class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board):
            row = len(board)
            col = len(board[0])
            for i in range(row):
                if board[i][0] == "O":
                    self.helper(board, i,0)
                if board[i][col-1] == "O":
                    self.helper(board,i,col-1)
            for j in range(col):
                if board[0][j] == "O":
                    self.helper(board, 0, j)
                if board[row-1][j] == "O":
                    self.helper(board, row-1, j)
            for i in range(row):
                for j in range(col):
                    if board[i][j] == "O":
                        board[i][j] = "X"
                    if board[i][j] =="K":
                        board[i][j] = "O"

    def helper(self, board, i,j):
        board[i][j] = "K"
        if i > 0 and board[i-1][j] == "O":
            self.helper(board, i-1, j)
        if j > 0 and board[i][j-1] == "O":
            self.helper(board, i, j-1)
        if i < len(board)-2 and board[i+1][j] == "O":
            self.helper(board, i + 1, j)
        if j < len(board[0]) -2 and board[i][j+1] == "O":
            self.helper(board, i, j+1)

