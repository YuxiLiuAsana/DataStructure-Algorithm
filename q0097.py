class Solution:
    cache = {}
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (s1,s2,s3) in self.cache: return self.cache[(s1,s2,s3)]
        if len(s1) + len(s2) != len(s3): return False
        if s1=='' and s2=='' and s3=='': return True
        if s1=='' : return s2==s3
        if s2 == '': return s1 == s3
        t1 = False
        t2 = False
        if s3[0] == s1[0]:
            t1 = self.isInterleave(s1[1:],s2,s3[1:])
        if s3[0] == s2[0]:
            t2 = self.isInterleave(s1,s2[1:],s3[1:])
        self.cache[(s1,s2,s3)] = (t1 or t2)
        return t1 or t2