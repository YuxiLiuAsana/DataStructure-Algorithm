class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visit = [[False for _ in range(len(board[0]))] for _ in range(len(board)) ]
        for i,row in enumerate(board):
            for j ,c in enumerate(row):
                if c == word[0]:
                    visit[i][j]=True
                    temp = self.DFS(board, visit,word[1:], i,j)
                    if temp:
                        return True
                    else:
                        visit[i][j]=False
        return False

    def DFS(self, board, visited, word, i ,j ):
        if word=="": return True
        dir_list = [[-1, 0], [0, -1], [1, 0], [ 0, 1]]
        for n in range(4):
            ni, nj = i+dir_list[n][0], j + dir_list[n][1]
            if self.match(board, visited, ni, nj, word[0]):
                visited[ni][nj]=True
                temp = self.DFS(board, visited, word[1:], ni, nj)
                if temp == True: return True
                else:
                    visited[ni][nj]=False
        return False

    def match(self, board, visited, i, j, v):
        return i >= 0 and i < len(board) and j >=0 and j < len(board[0]) and (not visited[i][j]) and board[i][j] == v



