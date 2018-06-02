class Solution(object):
    def __init__(self):
        self.DP = {}
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        return self.isInterleaveHelper(s1,0,s2,0,s3,0)
    def isInterleaveHelper(self, s1,i1,s2,i2,s3,i3 ):
        if i1 not in self.DP:
            self.DP[i1] = {}
        # if we have it already in DP then return it
        if i2 in self.DP[i1]:
            return self.DP[i1][i2]
        #i1 is the end of s1
        if i1 == len(s1):
            self.DP[i1][i2] = (s2[i2:] == s3[i3:])
            return s2[i2:] == s3[i3:]
        # i2 is the end of s2
        if i2 == len(s2):
            self.DP[i1][i2] = (s1[i1:] == s3[i3:])
            return self.DP[i1][i2]
        # if len(subs1) + len(subs2) != len(subs3) return false
        if len(s1) - i1 + len(s2) - i2 != len(s3) - i3:
            self.DP[i1][i2] = False
            return False
        # if s1[i1] != s3[i3] and s2[i2] != s3[i3]
        if s1[i1] != s3[i3] and s2[i2] != s3[i3]:
            self.DP[i1][i2] = False
            return False
        if s1[i1] == s3[i3] and s2[i2] != s3[i3]:
            self.DP[i1][i2] = self.isInterleaveHelper(s1,i1+1,s2,i2,s3,i3+1)
            return self.DP[i1][i2]
        if s1[i1] != s3[i3] and s2[i2] == s3[i3]:
            self.DP[i1][i2] = self.isInterleaveHelper(s1,i1,s2,i2+1,s3,i3+1)
            return self.DP[i1][i2]
        if s1[i1] == s3[i3] and s2[i2] == s3[i3]:
            first = self.isInterleaveHelper(s1,i1+1,s2,i2,s3,i3+1)
            second = self.isInterleaveHelper(s1,i1,s2,i2+1,s3,i3+1)
            self.DP[i1][i2] = first or second
            return self.DP[i1][i2]

if __name__ == "__main__":
    test = Solution()
    test.isInterleave("bc","bbc","bbcbc")