class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        wordSet = set(wordDict + [''])
        def helper( s, wordSet):
            if s == '': return True
            nonlocal cache
            if s in cache:
                return cache[s]
            for i in range(1,len(s)+1):
                if s[:i] in wordSet:
                    temp = helper(s[i:], wordSet)
                    if temp:
                        cache[s] = True
                        return True
            cache[s] = False
            return False
        return helper(s, wordSet)