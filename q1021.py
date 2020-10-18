class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        l = 0
        t = ""
        r = ""
        for s in S:
            t += s
            if s == '(' : l += 1
            else: l -=1
            if l == 0 :
                r += t[1:-1]
                t = ""
        return r

