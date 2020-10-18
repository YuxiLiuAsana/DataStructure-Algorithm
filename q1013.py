class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sum(A)
        if not s % 3 ==0:
            return False
        else:
            g = s/3
            t = 0
            c = 0
            for i in A:
                if t + i == g:
                    t = 0
                    c += 1
                else:
                    t = t + i
            return c == 3