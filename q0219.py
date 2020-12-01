from sortedcontainers import SortedList


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end_time = SortedList([])
        for i in intervals:
            if len(end_time) == 0:
                end_time.add(i[1])
            else:
                if end_time[0] <= i[0]:
                    end_time.pop(index=0)
                end_time.add(i[1])
        return len(end_time)
