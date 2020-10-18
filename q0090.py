class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mp = list(Counter(nums).items())
        return self.helper(mp,[[]])

    def helper(self, cnt, pre):
        if len(cnt) == 0:
            return pre
        head = cnt[0]
        ret = pre
        l = len(pre)
        for i in range(head[1]):
            temp = [p + [head[0]] * (i+1) for p in pre[:l]]
            ret += temp
        return self.helper(cnt[1:],ret)

