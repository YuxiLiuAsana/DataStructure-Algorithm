class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        store = []
        i = 0
        j = 0
        while i < len(s):
            if j == len(p):
                if len(store) != 0:
                    i = store[-1][0]
                    j = store[-1][1]
                    store.pop()
                else:
                    return False
            else:
                if p[j] == "*":
                    store += [[i + 1, j]]
                    j += 1
                elif p[j] == "?" or p[j] == s[i]:
                    i += 1
                    j += 1
                elif len(store) != 0:
                    i = store[-1][0]
                    j = store[-1][1]
                    store.pop()
                else:
                    return False
        while j < len(p) and p[j] == "*": j += 1
        return j == len(p)
