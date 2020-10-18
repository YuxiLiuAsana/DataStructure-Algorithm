class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0 : return 0
        lessFromLeft = [None] * len(heights)
        lessFromRight = [None] * len(heights)
        lessFromLeft[0] = -1
        lessFromRight[-1] = len(heights)
        for i in range(1,len(heights)):
            p = i - 1
            while(p >= 0 and heights[p] >= heights[i]):
                p = lessFromLeft[p]
            lessFromLeft[i] = p

        for i in range(len(heights)-2,-1,-1):
            p = i + 1
            while(p < len(heights) and heights[p] >= heights[i] ):
                p = lessFromRight[p]
            lessFromRight[i] = p
        mx = 0
        for i in range(len(heights)):
            mx = max(mx, heights[i] * (lessFromRight[i]-lessFromLeft[i]-1))
        return mx