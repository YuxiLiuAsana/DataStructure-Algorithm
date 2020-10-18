class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0: return 1
        n = 0
        i = 0
        while N:
            n += (N%2==0) * math.pow(2,i)
            N = N//2
            i = i + 1
        return int(n)