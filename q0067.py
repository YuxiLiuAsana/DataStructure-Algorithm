class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a): return self.addBinary(b, a)
        carry = 0
        ret = ""
        for i in range(1, len(a) + 1):
            add = 0
            if i <= len(b): add = int(b[-i])
            val = int(a[-i]) + (add + carry)
            carry = val // 2
            ret = str(val % 2) + ret

        if carry != 0:
            return str(carry) + ret
        else:
            return ret
