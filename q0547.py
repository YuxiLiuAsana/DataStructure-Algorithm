class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if len(M) == 0:
            return 0
        visited = [0] * len(M)
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                self.bfs(M,i,visited)
                count += 1
        return count
    def bfs(self,friends, i ,visited):
        for j in range(len(friends)):
            if friends[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.bfs(friends, j, visited)



