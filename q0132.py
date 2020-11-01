class Solution:
    cache = {}

    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        if s in self.cache:
            return self.cache[s]
        cut = len(s) - 1
        for i in range(len(s)):
            if s[:i + 1] == s[:i + 1][::-1]:
                cut = min(cut, 1 + self.minCut(s[i + 1:]))
        self.cache[s] = cut
        return cut
