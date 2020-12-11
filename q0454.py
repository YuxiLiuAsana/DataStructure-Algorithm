class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        s = 0
        ret = 0
        for i in nums:
            s = s + i
            if s - k in d:
                ret += d[s-k]
            if not s in d:
                d[s] = 0
            d[s] += 1
        return ret