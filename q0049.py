class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            sort = ''.join(sorted(i))
            if not sort in d:
                d[sort]=[]
            d[sort] += [i]
        return d.values()