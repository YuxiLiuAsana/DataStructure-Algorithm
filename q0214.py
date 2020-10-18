class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s),0,-1):
            if(s[i-1] == s[0]) and self.isPalindrome(s[:i]):
                return s[:i-1:-1] + s
        return s
    def isPalindrome(self,s):
        return s == s[::-1]