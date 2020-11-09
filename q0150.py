from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        d = deque()
        for t in tokens:
            if t == "+" or t == '-' or t == '*' or t == '/':
                b = d.pop()
                a = d.pop()
                if t == '+':
                    d.append(int(a + b))
                if t == '-':
                    d.append(int(a - b))
                if t == '*':
                    d.append(int(a * b))
                if t == '/':
                    divide = int(abs(a)//abs(b))
                    sign = (a^b)//abs(a^b)
                    d.append(int(divide * sign))
            else:
                d.append(int(t))
        return d[0]