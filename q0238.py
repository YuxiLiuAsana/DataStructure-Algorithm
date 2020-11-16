class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_index = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index += [i]
            else:
                product *= nums[i]
        if len(zero_index) > 1:
            return [0] * len(nums)
        if len(zero_index) == 1:
            return [0] * zero_index[0] + [product] + [0] * (len(nums) - zero_index[0] - 1)

        return [int(product / n) for n in nums]