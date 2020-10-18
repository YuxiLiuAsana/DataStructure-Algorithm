class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if(K%2 == 0 or K%5 == 0):
            return -1
        num = int(0)
        for i in range(K):
            num =( num * 10 + 1) % K
            if num == 0:
                return i + 1
        return -1
