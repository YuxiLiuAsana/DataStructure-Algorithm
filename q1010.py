class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        store = [0] * 60
        for t in time:
            store[t%60] += 1
        number = 0
        for i in range(1,30):
            number += store[i] * store[60-i]
        if store[0] >1:
            number += (store[0] * (store[0]-1)/2)
        if store[30] >1:
            number += (store[30] * (store[30]-1)/2)
        return int(number)