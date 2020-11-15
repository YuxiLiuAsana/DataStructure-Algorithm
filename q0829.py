import math
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        i = 1
        count = 0
        while i < math.sqrt(2 * N):
            a = (N-(1 + i) * i * 0.5)/i
            if a == int(a):
                count += 1
            i += 1
        return count