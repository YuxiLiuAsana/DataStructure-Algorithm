class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return "1"
        else:
            start = "1"
            for i in range(n-1):
                start = self.generate(start)
            return start
            
        
    def generate(self,s):
        if len(s) == 1:
            return "1"+s
        else:
            count = 1
            last = s[0]
            ret = ""
            for c in s[1:]:
                if c == last:
                    count += 1
                else:
                    ret = ret + str(count) + last
                    count = 1
                    last = c
            ret = ret + str(count)+last
            return ret
