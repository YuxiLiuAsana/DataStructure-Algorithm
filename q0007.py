class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > math.pow(2,31)-1 or x < -math.pow(2,31):return 0
        is_neg = x < 0
        ret = 0
        x = abs(x)
        while x !=0:
            ret *= 10
            ret += x%10
            x = x //10
        if is_neg:
            ret = -ret
        if ret > math.pow(2,31)-1 or ret < -math.pow(2,31):return 0
        else: return ret
            
