class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        i = 0
        while True:
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
                
            i += 1
                    
        return strs[0][:i]
