class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        for n in nums:
            size = len(ret)
            for t in ret[0:size]:
                ret += [t+[n]]
        return ret
