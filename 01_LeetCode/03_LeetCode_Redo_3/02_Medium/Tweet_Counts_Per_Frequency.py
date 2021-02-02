"""
Tweet Counts Per Frequency

Implement the class TweetCounts that supports two methods:
1. recordTweet(string tweetName, int time)

Stores the tweetName at the recorded time (in seconds).
2. getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime)

Returns the total number of occurrences for the given tweetName per minute, hour, or day 
(depending on freq) starting from the startTime (in seconds) and ending at the endTime (in seconds).
freq is always minute, hour or day, representing the time interval to get the total number of 
occurrences for the given tweetName.
The first time interval always starts from the startTime, so the time intervals are [startTime, 
startTime + delta*1>,  [startTime + delta*1, startTime + delta*2>, [startTime + delta*2, 
startTime + delta*3>, ... , [startTime + delta*i, min(startTime + delta*(i+1), endTime + 1)> 
for some non-negative number i and delta (which depends on freq).  

Code Logic: Knowing the formula (endTime - startTime)/(steps + 1)

T: O(n); S: O(n) where n is number of times a tweet has been tweeted.
"""

class Solution:
    def __init__(self):
        self.data = collections.defaultdict(lambda:[])

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.data[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        step = {'day': 24 * 60 * 60, 'hour': 60 * 60, 'minute': '60'}[freq]

        result = [0] * ( (endTime - startTime)//step )
        for time in self.data[tweetName]:
            if (startTime <= time <=endTime):
                result[ (time - startTime) //step ] += 1

        return result

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)