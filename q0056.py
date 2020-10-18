class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        tuples = [tuple(x) for x in intervals]
        tuples.sort()
        if len(tuples) == 0: return []
        ret = []
        last = tuples[0]
        for i in range(1, len(tuples)):
            if tuples[i][0] <= last[1]:
                if tuples[i][1] > last[1]:
                    last = (last[0], tuples[i][1])
            else:
                ret += [[last[0], last[1]]]
                last = tuples[i]
        ret += [list(last)]
        return ret