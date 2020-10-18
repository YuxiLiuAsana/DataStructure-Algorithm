class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        ret = 0
        dp = [{} for i in range(len(A))]
        dp[-2] = {A[-1]-A[-2]:2}
        for i in range(len(A)-3,-1,-1):
            for j in range(len(A)-1,i ,-1):
                diff = A[j]-A[i]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                if ret < dp[i][diff]: ret = dp[i][diff]
        return ret