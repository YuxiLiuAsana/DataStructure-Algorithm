class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) >= 2:
            i = len(nums) -2
            while nums[i] >= nums[i+1] and i >= 0:
                i -=1
            if not i == -1:
                j = len(nums) -1
                while nums[j] <= nums[i]:
                    j -=1
                nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            j = len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
