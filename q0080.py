class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        slow = 0
        last = nums[0]-1
        count = 1
        for n in nums:
            if n == last:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[slow] = n
                slow += 1
            last = n
        return slow