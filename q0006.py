class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        l = [""] * numRows
        cycle = (numRows-1) * 2
        for i in range(len(s)):
            x = i%cycle
            if x >= numRows: x = cycle - x
            l[x] += s[i]
        
        return reduce( lambda x,y: x + y, l)
            
