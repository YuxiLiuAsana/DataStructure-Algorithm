class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.helper(s, 4)

    def helper(self, s , n):
        if n > len(s):
            return None

        if n == 1:
            if int(s) <= 255 and (s[0] != '0' or len(s) == 1):
                return [s]
            else:
                return None
        if s[0] == '0':
            less = self.helper(s[1:],n-1)
            if less:
                return ['0.'+x for x in less]
        ret = []
        i = 1
        while s[0] != '0' and int(s[:i]) <= 255 and i < len(s):
            less = self.helper(s[i:],n-1)
            if less:
                ret += [s[:i]+'.'+x for x in less]
            i += 1
        return ret


