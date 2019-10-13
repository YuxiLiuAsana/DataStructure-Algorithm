class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre_pos = {}
        max_sub = 0
        start_pos = -1
        for i, v in enumerate(s):
            if v in pre_pos:
                max_sub = max(max_sub, i-start_pos-1)
                start_pos = max(start_pos,pre_pos[v]) 
            pre_pos[v]=i
        max_sub = max(max_sub, len(s)-start_pos-1)
        return max_sub
