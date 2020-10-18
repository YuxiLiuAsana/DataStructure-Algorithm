class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) <= 3:
            for n in nums:
                if n == target: return True
            return False
        if target == nums[0] or target == nums[-1]: return True
        if nums[-1] > nums[0]: # in order
            if target > nums[-1] or target < nums[0]: return False
            mid_i = len(nums)/2
            if target == nums[mid_i]: return True
            elif target > nums[mid_i]: return self.search(nums[mid_i+1:len(nums)-1], target)
            else: return self.search(nums[1:mid_i], target)
        elif nums[-1] <= nums[0]: # maybe not in order
            if target > nums[-1] and target < nums[0]:
                return False
            mid_i = len(nums)/2
            if target == nums[mid_i]: return True
            if nums[mid_i] > nums[0]:
                if target < nums[mid_i] and target > nums[0]: return self.search(nums[1:mid_i], target)
                else: return self.search(nums[mid_i+1:len(nums)-1], target)
            elif nums[mid_i] < nums[-1]:
                if target > nums[mid_i] and target < nums[-1]: return self.search(nums[mid_i+1: len(nums)-1], target)
                else: return self.search(nums[1:mid_i], target)
            else:
                return self.search(nums[1:mid_i], target) or self.search(nums[mid_i+1: len(nums)-1], target)



