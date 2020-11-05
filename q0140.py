class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}

        def helper(s, wordSet):

            nonlocal cache
            if s == '': return ['']
            if s in cache: return cache[s]
            ret = []
            for i in range(1, len(s) + 1):
                if s[:i] in wordSet:
                    temp = helper(s[i:], wordSet)
                    for t in temp:
                        ret += [s[:i] + ' ' + t if t != '' else s[:i]]
            cache[s] = ret
            return ret

        return helper(s, set(wordDict))