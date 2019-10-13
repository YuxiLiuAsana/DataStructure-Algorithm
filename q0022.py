class Solution(object):
    dp = {}
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        if n == 1: return ["()"]
        if n in self.dp : return self.dp[n]
        s = set()
        for i in range(1,n):
            if not i in self.dp:
                self.dp[i] = self.generateParenthesis(i)
            if not n-i in self.dp:
                self.dp[n-i] = self.generateParenthesis(n-i)
            for f in self.dp[i]:
                for b in self.dp[n-i]:
                    s.add(f + b)
        for j in self.dp[n-1]:
            s.add('(' + j + ')')
        self.dp[n] = list(s)
        return self.dp[n]
        
                
                
        
        
