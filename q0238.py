class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 1
        for n in nums:
            i *= n
        return [int(i/n) for n in nums]