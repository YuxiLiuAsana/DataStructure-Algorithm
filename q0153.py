class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        if nums[0] < nums[-1]:
            return nums[0]
        mid = len(nums)//2
        if nums[0] < nums[mid]:
            return self.findMin(nums[mid:])
        else:
            return self.findMin(nums[:mid+1])