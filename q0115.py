class Solution:
    cache = {}
    def numDistinct(self, s: str, t: str) -> int:
        i = 0
        while i < len(s):
            if not s[i] in t:
                s = s.replace(s[i],'')
            else:
                i += 1
        return self.helper(s,t)
    def helper(self, s: str, t: str) -> int:
        if (s,t) in self.cache:
            return self.cache[(s,t)]
        if s == '': return 0
        if len(s) < len(t): return 0
        if s == t : return 1
        if t == '': return 1
        if s[0] != t[0]:
            self.cache[(s,t)] = self.helper(s[1:], t)
            return self.cache[(s,t)]
        else:
            self.cache[(s,t)] = self.helper(s[1:],t[1:]) + self.helper(s[1:], t)
            return self.cache[(s,t)]