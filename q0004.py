class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        # if the total length is even, then seperation length is half
        # if the total length is odd, then it takes smaller integer: e.g. 5 -> 2
        seperation_length = (l1 + l2) // 2 
        start = 0
        end = l1
        while start < end:
            mid = (start + end) //2
            if start + 1 == end:
                # see the start value
                l2_sep = seperation_length - start
                if self.check_seperation(start, l2_sep, nums1, nums2):
                    end = start
                    break
                else: 
                    start = end
                    break 
            elif self.check_seperation(mid, seperation_length - mid, nums1, nums2):
                start = mid
                end = mid
                break
            else:    
                if self.get_index_value(nums1, mid-1) > min(self.get_index_value(nums1,mid), self.get_index_value(nums2, seperation_length-mid)):
                    end = mid - 1
                else:
                    start = mid + 1
                    
        if (l1 + l2) % 2 == 1:
            return min(self.get_index_value(nums1, start), self.get_index_value(nums2, seperation_length-start))
        else:
            return 0.5 * ( max(self.get_index_value(nums1,start-1), self.get_index_value(nums2, seperation_length-start-1)) + min(self.get_index_value(nums1,start), self.get_index_value(nums2, seperation_length-start)))
    
                          
    def get_index_value(self, l: List[int], index: int) -> float:
        if index < 0: return -float("inf")
        if index >= len(l): return float("inf")
        return l[index]
                          
                          
    def check_seperation(self, l1_sep, l2_sep, l1, l2):
        return max(self.get_index_value(l1,l1_sep-1), self.get_index_value(l2, l2_sep-1)) <= min(self.get_index_value(l1,l1_sep), self.get_index_value(l2, l2_sep))
