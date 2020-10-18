class Solution:
    def shipWithinDays(self, weights, D):
        start = max(weights)
        end = sum(weights)
        while start < end:
            mid = (start + end)//2
            day = 0
            container = 0
            for w in weights:
                if container + w > mid:
                    day += 1
                    container = 0
                container += w
            if container != 0: day += 1
            if day > D:
                start = mid + 1
            else :
                end = mid
        return start