class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        mi = float("inf")
        index = -1
        next_amount = 0
        for i in range(len(gas)):
            next_amount += (gas[i]-cost[i])
            if next_amount < mi:
                mi = next_amount
                index =( i + 1) % len(gas)
        if next_amount < 0: return -1
        else: return index

