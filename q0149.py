from fractions import Fraction


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        cache = {}
        if len(points) <= 2:
            return len(points)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    if not (0, points[i][1]) in cache:
                        cache[(0, points[i][1])] = set()
                    cache[(0, points[i][1])].add(i)
                    cache[(0, points[i][1])].add(j)
                result = self.getLine(points[i], points[j])

                if not result in cache:
                    cache[result] = set()
                cache[result].add(i)
                cache[result].add(j)

        maxCount = 0
        for key, value in cache.items():
            if len(value) > maxCount:
                maxCount = len(value)
        return maxCount

    def getLine(self, p1, p2):
        if (p1[0] != p2[0]):
            a = Fraction(p1[1] - p2[1], p1[0] - p2[0])
            b = Fraction(p2[1] * p1[0] - p1[1] * p2[0], p1[0] - p2[0])
            return (a.numerator, a.denominator, b.numerator, b.denominator)
        else:
            return (p1[0], 0)
