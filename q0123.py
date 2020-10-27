class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        forward = [None] * len(prices)
        backward = [None] * len(prices)
        running_min = None
        max_value = None
        for i in range(len(prices)):
            if running_min == None or prices[i] < running_min:
                running_min = prices[i]
            if max_value == None or prices[i] - running_min > max_value:
                max_value = prices[i] - running_min
            forward[i] = max_value

        running_max = None
        min_value = None
        for i in range(len(prices) - 1, -1, -1):
            if running_max == None or prices[i] > running_max:
                running_max = prices[i]
            if min_value == None or prices[i] - running_max < min_value:
                min_value = prices[i] - running_max
            backward[i] = running_max - prices[i]
        max_ret = 0
        for i in range(len(prices)):
            if forward[i] + backward[i] > max_ret:
                max_ret = forward[i] + backward[i]
        return max_ret