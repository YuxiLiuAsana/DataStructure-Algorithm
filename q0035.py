class Solution:
    start = -1
    end = -1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.start = 2 * len(nums)
        self.binarySearchRange(nums, 0, len(nums)-1, target)
        if self.start >= len(nums): self.start = -1
        return(self.start, self.end)
    def binarySearchRange(self, nums, start, end, target):
        if start > end: return
        if target < nums[start] or target > nums[end]: return
        if nums[start] == target:
            self.start = min(self.start, start)
            self.end = max(self.end, start)
        if nums[end] == target:
            self.start = min(self.start, end)
            self.end = max(self.end, end)
        if start == end or nums[start] == nums[end]: return
        
        mid = (start + end) //2
        if target == nums[mid]:
            self.start = min(self.start, mid)
            self.end = max(self.end, mid)
        if target <= nums[mid]: self.binarySearchRange(nums, start+1, mid-1 ,target )
        if target >= nums[mid]: self.binarySearchRange(nums, mid+1, end-1, target)

