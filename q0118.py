class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for i in range(numRows):
            add = [1] * (i+1)
            for j in range(1, i):
                add[j] = ret[-1][j-1] + ret[-1][j]
            ret += [add]
        return ret