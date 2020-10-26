class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        pre = self.getRow(rowIndex-1)
        ret = [1]
        for i in range(1,len(pre)):
            ret += [pre[i-1] + pre[i]]
        ret += [1]
        return ret