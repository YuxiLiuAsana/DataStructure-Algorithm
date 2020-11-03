class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 0:
            return 0
        if len(ratings) == 1:
            return 1

        def isLocalMin(ratings, i):
            if i == 0:
                return ratings[i] <= ratings[1]
            if i == len(ratings) - 1:
                return ratings[i] <= ratings[i - 1]
            return ratings[i] <= ratings[i + 1] and ratings[i] <= ratings[i - 1]

        def isLocalMax(ratings, i):
            if i == 0:
                return ratings[i] > ratings[i + 1]
            if i == len(ratings) - 1:
                return ratings[i] > ratings[i - 1]
            return ratings[i] >= ratings[i + 1] and ratings[i] >= ratings[i - 1] and not isLocalMin(ratings, i)

        def addCandy(n):
            return int((1 + n) * n / 2)

        candy = 0
        lastLocalMin = None
        lastLocalMax = None
        lastLocalMaxCandy = None
        for i in range(len(ratings)):
            if isLocalMin(ratings, i):
                if lastLocalMax != None:
                    if lastLocalMin != None and lastLocalMin > lastLocalMax:
                        candy += 1
                    elif lastLocalMaxCandy > i - lastLocalMax + 1:
                        candy += (lastLocalMaxCandy + addCandy(i - lastLocalMax))
                    else:
                        candy += addCandy(i - lastLocalMax + 1)
                else:
                    candy += 1
                lastLocalMin = i
            elif isLocalMax(ratings, i):
                if lastLocalMax != None and lastLocalMax > lastLocalMin:
                    candy += lastLocalMaxCandy
                    lastLocalMaxCandy = 0
                elif lastLocalMin != None:
                    lastLocalMaxCandy = i - lastLocalMin + 1
                    candy += addCandy(i - lastLocalMin) - 1
                else:
                    lastLocalMaxCandy = 1

                lastLocalMax = i

        if isLocalMax(ratings, len(ratings) - 1):
            candy += lastLocalMaxCandy
        return candy

