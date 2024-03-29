"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that 
calls are being made to the system in chronological order (ie, the timestamp is monotonically 
increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
Follow up:
What if the number of hits per second could be very large? Does your design scale?
"""
from collections import deque

class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = deque()
        self.counter = 0
        
    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not self.hits or self.hits[-1][0] != timestamp:
            self.hits.append([timestamp,1])
        else:
            self.hits[-1][1] += 1
            
        self.counter += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # You want the time period between the start and the current timestamp to always be 
        # 300 seconds. So all the hits that occured outside that interval will have to be 
        # deleted. 
        while self.hits and self.hits[0][0] <= timestamp - 300:
            self.counter -= self.hits.popleft()[1]
            
        return self.counter


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)