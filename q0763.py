class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if len(S) == 0:
            return []
        d = {}
        for i in range(len(S)):
            d[S[i]] = i

        current_index = 0
        ret = []
        while current_index < len(S):
            ret += [current_index]
            current_max = d[S[current_index]]
            while current_index <= current_max:
                current_max = max(current_max, d[S[current_index]])
                current_index += 1
        ret += [len(S)]
        return [j - i for i, j in zip(ret[:-1], ret[1:])]