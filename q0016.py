class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ret = sum(nums[0:3])
        for i in range(len(nums)):
            front = i + 1
            end = len(nums)-1
            t = target - nums[i]
            while front < end:
                s = nums[front] + nums[end]
                if s < t:
                    front += 1
                elif s > t:
                    end -=1
                else:
                    return target
                if abs(target-ret) > abs(target-s-nums[i]):
                    ret = s + nums[i]
        return ret
                
                
