class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        mi = prices[0]
        mx = 0
        for p in prices:
            if p < mi: mi = p
            else: mx = max(mx, p-mi)
        return mx