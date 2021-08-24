"""
Implement the `UndergroundSystem` class:

- `void checkIn(int id, string stationName, int t)`
    - A customer with a card id equal to `id`, gets in the station `stationName` at time `t`.
    - A customer can only be checked into one place at a time.
- `void checkOut(int id, string stationName, int t)`
    - A customer with a card id equal to `id`, gets out from the station `stationName` at time `t`.
- `double getAverageTime(string startStation, string endStation)`
    - Returns the average time to travel between the `startStation` and the `endStation`.
    - The average time is computed from all the previous traveling from `startStation` to `endStation` that happened **directly**.
    - Call to `getAverageTime` is always valid.

You can assume all calls to `checkIn` and `checkOut` methods are consistent. If a customer gets in at time **t1** at some station, 
they get out at time **t2** with **t2 > t1**. All events happen in chronological order.
"""
class UndergroundSystem:

    def __init__(self):
        self.passenger = {}
        self.time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger[id] = [stationName, "", t, 0]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.passenger[id][1] = stationName
        self.passenger[id][3] = t
        if ((self.passenger[id][0], stationName) in self.time):
            self.time[(self.passenger[id][0], stationName)].append(t-self.passenger[id][2])
        else:
            self.time[(self.passenger[id][0], stationName)]= [t-self.passenger[id][2]]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        avg = self.time[(startStation, endStation)]
        return sum(avg)/len(avg)
        
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)