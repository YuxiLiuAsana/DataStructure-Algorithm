class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]
        if newInterval[0] > intervals[-1][1]: return intervals + [newInterval]
        if newInterval[1] < intervals[0][0]: return [newInterval] + intervals
        left = 0
        while left < len(intervals) and intervals[left][1] < newInterval[0]:
            left += 1
        right = len(intervals)-1
        while right > -1 and intervals[right][0] > newInterval[1]:
            right -=1
        addInterval = [min(intervals[left][0], newInterval[0]), max(intervals[right][1], newInterval[1])]
        return intervals[:left] + [addInterval] + intervals[right + 1 :]