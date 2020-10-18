class Solution:
    dp = {}

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.dp = {}
        return self.helper(obstacleGrid, 0, 0)

    def helper(self, obstacleGrid: List[List[int]], x, y) -> int:
        if (x, y) in self.dp: return self.dp[(x, y)]
        if x >= len(obstacleGrid):
            self.dp[(x, y)] = 0
            return 0
        if y >= len(obstacleGrid[0]):
            self.dp[(x, y)] = 0
            return 0
        if obstacleGrid[x][y] == 1:
            self.dp[(x, y)] = 0
            return 0
        if x == len(obstacleGrid) - 1 and y == len(obstacleGrid[0]) - 1:
            self.dp[(x, y)] = 1
            return 1

        self.dp[(x, y)] = self.helper(obstacleGrid, x + 1, y) + self.helper(obstacleGrid, x, y + 1)
        return self.dp[(x, y)]