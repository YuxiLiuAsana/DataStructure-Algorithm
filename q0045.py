class Solution:
    def jump(self, nums: List[int]) -> int:
        last = -1
        this = 0
        count = 0
        while this < len(nums) -1:
            count += 1
            next_pos = this
            for i in range(last+1, this+1):
                if i + nums[i] > next_pos: next_pos = i + nums[i]
            last = this
            this = next_pos
        return count