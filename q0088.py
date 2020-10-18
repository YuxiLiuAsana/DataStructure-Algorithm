class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m):
            nums1[n+m-1-i] = nums1[m-1-i]
        i = n
        j = 0
        current = 0
        while i < n + m and j < n:
            if nums2[j] < nums1[i]:
                nums1[current] = nums2[j]
                j +=1
            else:
                nums1[current] = nums1[i]
                i += 1
            current += 1
        if j!= n :
            nums1[m+j:] = nums2[j:]