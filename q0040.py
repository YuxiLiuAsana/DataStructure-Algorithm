class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates.sort()
        for i, v in enumerate(candidates):
            if v == target:
                if not [v] in ret:
                    ret+=[[v]]
            elif v < target:
                temp = self.combinationSum2(candidates[i+1:], target-v)
                for x in temp:
                    if not [v] + x in ret:
                        ret += [[v] + x]
        return ret
