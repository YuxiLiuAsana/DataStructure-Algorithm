class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = ")" + s + "("
        stack = []
        for i in range(len(s)):
            if len(stack) > 0 and stack[-1][0] == '(' and s[i] == ")":
                stack.pop()
            else:
                stack += [(s[i], i)]
        maxLen = 0
        for i in range(1, len(stack)):
            maxLen = max(maxLen, stack[i][1] - stack[i-1][1] - 1)
        return maxLen
