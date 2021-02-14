"""
Implement the UndergroundSystem class:

    void checkIn(int id, string stationName, int t)
        A customer with a card id equal to id, gets in the station stationName at time t.
        A customer can only be checked into one place at a time.
    void checkOut(int id, string stationName, int t)
        A customer with a card id equal to id, gets out from the station stationName at time t.
    double getAverageTime(string startStation, string endStation)
        Returns the average time to travel between the startStation and the endStation.
        The average time is computed from all the previous traveling from startStation to endStation that happened directly.
        Call to getAverageTime is always valid.

You can assume all calls to checkIn and checkOut methods are consistent. If a customer 
gets in at time t1 at some station, they get out at time t2 with t2 > t1. All events happen in chronological order.

T: O(1); S: P(P + S^2) where P is number of passengers and S is number of stations. We can expect to all possible 
combinations of stations in the self.stations dictionary we will have S^2 space complexity. 
"""
class UndergroundSystem:

    def __init__(self):
        self.users = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.users[id] = [[stationName, t], []]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.users[id][1] = [stationName, t]
        temp = self.users[id][0][0] + stationName
        if temp in self.stations:
            self.stations[temp].append(t - self.users[id][0][1])
        else:
            self.stations[temp] = [t - self.users[id][0][1]]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        size = len(self.stations[startStation+endStation])
        return sum(self.stations[startStation+endStation])/size


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)