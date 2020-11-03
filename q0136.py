class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return s.pop()

    def singleNumberBitMask(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a