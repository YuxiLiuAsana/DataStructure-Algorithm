class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {')': '(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if i in m.values():
                stack.append(i)
            else:
                if len(stack) == 0: return False
                if stack[-1] != m[i]: return False
                else: stack.pop()
        return len(stack) == 0
