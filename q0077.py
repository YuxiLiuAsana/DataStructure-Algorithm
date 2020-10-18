class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k < 1: return []
        if k == 1:
            return [[x] for x in range(1, n + 1)]
        ret = []
        for i in range(n, k - 2, -1):
            temp = self.combine(i - 1, k - 1)
            for t in temp:
                ret += [t + [i]]

        return ret