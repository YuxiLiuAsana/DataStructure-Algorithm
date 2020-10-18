class Solution(object):
    dp = {}
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":return 0
        return self.helper(s)

    def helper(self, s):
        if s in self.dp: return self.dp[s]
        if s == "": self.dp[s] = 1
        elif s[0] == '0': self.dp[s] = 0
        elif len(s) == 1: self.dp[s] = 1
        elif s[0] > '2' or (s[0] == '2' and s[1] > '6'):  self.dp[s] = self.helper(s[1:])
        else:  self.dp[s] =  self.helper(s[1:]) + self.helper(s[2:])
        return self.dp[s]

