class Solution:
    def minimumTotal(self, triangle) -> int:
        if len(triangle) == 0:
            return 0
        for i in range(len(triangle)-2,-1, -1):
            print(triangle[i])
            for j in range(len(triangle[i])):
                print(triangle[i][j])
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
            print(triangle[i])
        return triangle[0][0]

s = Solution()
s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])