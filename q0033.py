class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0 , len(nums) -1, target)
        
        
    def binarySearch(self, nums: List[int], start, end, target:int) -> int:
        if start > end: return -1
        if start == end: 
            if target == nums[start]: return start
            else: return -1
        mid = (start + end) //2 
        if target == nums[mid]: return mid
        if target == nums[start]: return start
        if target == nums[end]: return end
        if nums[start] > nums[end]:
            if nums[mid] > nums[start]: # first half is in order
                if target > nums[start] and target < nums[mid] : return self.binarySearch(nums, start+1, mid-1 ,target)
                elif target > nums[mid] or target < nums[end] : return self.binarySearch(nums, mid + 1, end-1, target)
                else: return -1
            else: # second half is in order
                if target > nums[start] or target < nums[mid]: return self.binarySearch(nums, start+1, mid-1 ,target)
                elif target < nums[end] and target > nums[mid]: return self.binarySearch(nums, mid + 1, end-1, target)
                else: return -1  
        else:
            if target > nums[end] or target < nums[start] : return -1
            elif target < nums[mid]: return self.binarySearch(nums, start + 1, mid-1, target)
            else: return self.binarySearch(nums, mid + 1, end-1, target)

