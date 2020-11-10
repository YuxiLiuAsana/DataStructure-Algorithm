class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def helper(nums):
            if len(nums) == 1:
                return nums[0]
            odd = 0
            product = 1
            for n in nums:
                if n < 0:
                    odd += 1
                product *= n
            if odd % 2 == 0:
                return int(product)
            pre = 1
            for n in nums:
                pre *= n
                if n < 0:
                    break
            post = 1
            for i in range(len(nums) - 1, -1, -1):
                post *= nums[i]
                if nums[i] < 0:
                    break
            return int(max(product / pre, product / post))

        zero = [-1]
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += [i]
        zero += [len(nums)]
        if len(zero) > 2:
            max_value = 0
            for i in range(1, len(zero)):
                if zero[i - 1] + 1 != zero[i]:
                    max_value = max(max_value, helper(nums[zero[i - 1] + 1:zero[i]]))
            return int(max_value)
        else:
            return helper(nums)
