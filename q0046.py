class Solution:
    dp = {}
    def permute(self, nums: List[int]) -> List[List[int]]:
        tp = tuple(nums)
        if tp in self.dp: return self.dp[tp]
        if len(nums) == 1:
            self.dp[tp] = [nums]
            return [nums]
        ret = []
        for i, v in enumerate(nums):
            nums[0], nums[i] = nums[i], nums[0]
            small = self.permute(nums[1:])
            for s in small:
                ret += [[nums[0]] + s]
            nums[0], nums[i] = nums[i], nums[0]
        self.dp[tp] = ret
        return ret