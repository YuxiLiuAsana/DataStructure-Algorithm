class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0: return [0]
        last = self.grayCode(n-1)
        add = int( math.pow(2, n-1) )
        app = [add + x for x in last[::-1]]
        return last + app