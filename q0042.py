class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0 : return 0
        start = 0 
        end = len(height) - 1
        level = min(height[start], height[end])
        ret = 0
        while start < end:
            while height[start] <= height[end] and start < end:
                start += 1
                if height[start] < level: ret += (level-height[start])
                level = max(level,min(height[start], height[end]))
            while height[start] > height[end] and start < end:
                end -=1
                if height[end] < level: ret += (level - height[end])
                level = max(level,min(height[start], height[end]))
        return ret
        
