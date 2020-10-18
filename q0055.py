class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = -1
        this = 0
        while last != this:
            max_value = nums[this]
            for i in range(last + 1, this + 1):
                if i + nums[i] > max_value:
                    max_value = i + nums[i]
            if max_value >= len(nums)-1: return True
            last = this
            this = max_value
        return this >= len(nums) -1