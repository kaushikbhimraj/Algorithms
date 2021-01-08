"""
Given a stream of integers and a window size, calculate the moving average of all integers 
in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.runSum = []
        self.count  = 0
     
    def next(self, val: int) -> float:
        if len(self.runSum) == self.size:
            self.runSum.pop(0)
        else:
            self.count += 1
        self.runSum.append(val)
        return sum(self.runSum)/self.count

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)