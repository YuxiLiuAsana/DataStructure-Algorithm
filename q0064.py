class Solution:
    dp = {}

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.dp = {}
        return self.helper(grid, 0, 0)

    def helper(self, grid, x, y) -> int:
        if (x, y) in self.dp:
            return self.dp[(x, y)]
        if x >= len(grid):
            return float('inf')
        if y >= len(grid[0]):
            return float('inf')
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            self.dp[(x, y)] = grid[x][y]
            return self.dp[(x, y)]
        self.dp[(x, y)] = grid[x][y] + min(self.helper(grid, x + 1, y), self.helper(grid, x, y + 1))
        return self.dp[(x, y)]