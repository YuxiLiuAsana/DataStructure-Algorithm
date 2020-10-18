class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        if len(prices) <= 1: return 0
        for i in range(1, len(prices)):
            if prices[i]-prices[i-1] > 0:
                ret += prices[i]-prices[i-1]
        return ret