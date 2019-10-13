import numpy as np
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m = {}
        ret = []
        for n in nums:
            if not n in m:
                m[n] = 0
            if  n == 0 and m[n] < 3:
                m[n] += 1
            elif n != 0 and m[n] < 2:
                m[n] += 1
        print(m)       
        for n in m:
            if n == 0 and m[n] == 3:
                ret += [[n,n,n]]
            elif n!= 0 and m[n] ==2:
                if -2*n in m:
                    ret += [[n,n,-2*n]]
        unique = m.keys()
        unique.sort()
        uniqueSet = set(unique)
        for i in range(len(unique)):
            for j in range(i+1, len(unique)):
                t = -unique[i]-unique[j]
                if t in uniqueSet and t > unique[i] and t > unique[j]:
                    ret += [[unique[i],unique[j],t]]
        return ret
                    
                
