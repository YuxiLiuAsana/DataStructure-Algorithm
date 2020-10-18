class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        tempMax = -1
        preNum = A[0]-1
        for a in A[1:]:
            if a + preNum > tempMax:
                tempMax = a + preNum
            if a > preNum -1:
                preNum = a
            preNum -=1
        return tempMax