class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        zero = ~0
        one = 0
        two = 0
        for n in nums:
            new_zero = (zero & ~one & ~two & ~n) | (~zero & ~one & two & n)
            new_one = (~zero & one & ~two & ~n) | (zero & ~one & ~two & n)
            new_two = (~zero & ~one & two & ~n) | (~zero & one & ~two & n)
            zero, one, two = new_zero, new_one, new_two
        return one