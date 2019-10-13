class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        if len(candidates) == 0: return ret
        if len(candidates) == 1 and candidates[0] > target: return ret
        for i, value in enumerate(candidates):
            if value < target:
                iterate = self.combinationSum(candidates[i:], target - value)
                if len(iterate) != 0:
                    ret += [[value] + x for x in iterate]
            if value == target:
                ret += [[value]]
        return ret
