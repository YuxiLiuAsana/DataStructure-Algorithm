class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        r = []
        for q in queries:
            r += [self.match(q,pattern)]
        return r
    def match(self, q: str, p: str) -> bool:
        current_p = 0
        for c in q:
            if self.isUpper(c):
                if current_p >= len(p) or (not c == p[current_p]): return False
                else:
                    current_p += 1
            elif current_p < len(p):
                if c == p[current_p]: current_p += 1

        return current_p == len(p)

    def isUpper(self, q) -> bool:
        return q >="A" and q <="Z"
