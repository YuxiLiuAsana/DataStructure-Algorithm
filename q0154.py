class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        if nums[0] < nums[-1]:
            return nums[0]
        mid = len(nums)//2
        if nums[mid] < nums[-1]:
            return self.findMin(nums[:mid+1])
        if nums[mid] > nums[0]:
            return self.findMin(nums[mid+1:])
        return min(self.findMin(nums[:mid+1]), self.findMin(nums[mid:]))