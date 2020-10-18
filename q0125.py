class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = lower(s)
        i = 0
        j = len(s) -1
        while i < j and i < len(s) and j >=0:
            while i < len(s) and (not self.isChar(s[i])):
                i += 1
            while j >=0 and (not self.isChar(s[j]) ):
                j -= 1
            if i >= j: break
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True

    def isChar(self, c):
        return (c >= 'a' and c <= 'z') or(c >= '0' and c <='9')
