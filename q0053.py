class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = None
        cum_sum = 0
        for i in nums:
            if max_sum==None or cum_sum + i > max_sum:
                max_sum = cum_sum + i
            if cum_sum + i > 0:
                cum_sum += i
            else:
                cum_sum = 0
        return max_sum