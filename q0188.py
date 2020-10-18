import calendar
import time
import numpy as np
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0

        elif 2 * k >= len(prices):

            return sum(max(0, b-a) for a, b in zip(prices[:-1], prices[1:]))

        min_prices, max_profits = [float('inf')] * k, [0]*k

        for price in prices:

            for i in range(k):

                max_profits[i] = max(max_profits[i],
                                     price - min_prices[i])

                min_prices[i] = min(min_prices[i],
                                    price - (0 if i == 0 else max_profits[i-1]))

        return max_profits[-1]