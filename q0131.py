class Solution(object):
    dp = {}
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s in self.dp: return self.dp[s]
        if s == "": return [[]]
        ret = []
        for i in range(len(s)):
            if s[i] == s[0] and s[:i+1] == s[:i+1][::-1]:
                temp = self.partition(s[i+1:])
                self.dp[s[i+1:]] = temp
                for j in temp:
                    ret += [[s[:i+1]] + j]
        return ret
