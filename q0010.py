class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        stack = []
        i = 0
        j = 0
        while True:
            while j < len(p) -1 and p[j+1] == "*" :
                if i < len(s) and (s[i] == p[j] or p[j] =="."):
                    stack.append([i + 1 ,j])
                j = j + 2
            
            if i == len(s) and j == len(p):
                return True
            if i == len(s) and j < len(p):
                return False           
            
            if  i < len(s) and j < len(p) and (s[i] == p[j] or p[j] == "."):
                i += 1
                j += 1
            else:
                if len(stack) == 0:
                    return False
                else:
                    (i ,j)= stack[-1]
                    stack.pop()
            
            

            
