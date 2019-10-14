class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) == 1:  return [nums]
        ret = []
        for i, v in enumerate(nums):
            if i == 0 or nums[i-1] != v:
                nums[0], nums[i] = nums[i], nums[0]
                small = self.permuteUnique(nums[1:])
                for s in small:
                    ret += [[nums[0]] + s]
                nums[0], nums[i] = nums[i], nums[0]
        return ret