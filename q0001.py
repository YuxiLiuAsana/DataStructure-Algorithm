class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i,k in enumerate(nums):
            if target-k in d:
                return [d[target-k],i]
            d[k]=i
