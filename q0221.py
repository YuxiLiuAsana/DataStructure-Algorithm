class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def helper(matrix, i, j):
            area = 1
            expand = 1
            while i + expand < len(matrix) and j + expand < len(matrix[0]):
                for a in range(i, i + expand + 1):
                    if matrix[a][j + expand] != "1":
                        return area
                for b in range(j, j + expand + 1):
                    if matrix[i + expand][b] != "1":
                        return area

                area = (expand + 1) * (expand + 1)
                expand += 1
            return area

        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    t = helper(matrix, i, j)
                    max_area = max(max_area, t)
        return max_area
