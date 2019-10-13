class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 1
        index = 0
        while index < len(nums):
            while nums[index] > 0 and nums[index] <= len(nums) and nums[index] != index + 1 and nums[index] != nums[nums[index]-1]:
                t = nums[index]
                nums[index] = nums[t- 1]
                nums[t - 1] = t
            index += 1
        for i, v in enumerate(nums):
            if v != i + 1:
                return i + 1
        return len(nums) + 1
