import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return self.helper(list(range(1,n+1)), k)
    def helper(self, l:List[int], k: int) -> str:
        if k == 1: return ''.join(map(str, l))
        n = len(l)
        fac = math.factorial(n-1)
        index = (k-1)// fac
        return str(l[index])  + self.helper(l[:index] + l[index+1:],k - (index) * fac)