class UndergroundSystem:

    def __init__(self):
        self.time = {}  # (startStation, endStation) -> (totalTime, totalCount)
        self.person = {}  # (id)->(startStation, startTime)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.person[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (startStation, startTime) = self.person[id]
        del self.person[id]
        if not ((startStation, stationName)) in self.time:
            self.time[(startStation, stationName)] = (0, 0)
        (pt, c) = self.time[(startStation, stationName)]
        self.time[(startStation, stationName)] = (t - startTime + pt, c + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        (t, c) = self.time[(startStation, endStation)]
        return t / c

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)